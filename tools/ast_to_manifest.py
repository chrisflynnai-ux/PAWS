"""AST -> manifest.json renderer.

Renders a normalized AST dictionary into a manifest.json
for machine validation, indexing, and routing.
"""
import json
from datetime import date
from typing import Any


def render_manifest(ast: dict[str, Any], source_xml: str = "") -> str:
    """Render a skill AST into manifest.json format.

    Args:
        ast: Normalized skill dictionary.
        source_xml: Original XML filename for provenance tracking.

    Returns:
        JSON string of the manifest.
    """
    manifest = {
        "id": ast["id"],
        "name": ast["name"],
        "version": ast["version"],
        "status": ast["status"],
        "category": ast.get("category", ""),
        "tags": ast.get("tags", []),
        "description": ast.get("description", ""),
        "relationships": {
            "depends_on": ast.get("depends_on", []),
            "delegates_to": ast.get("delegates_to", []),
            "complements": ast.get("complements", []),
        },
        "tool_requirements": ast.get("required_tools", []),
        "memory_contract": {
            "reads": ast.get("memory_reads", []),
            "writes": ast.get("memory_writes", []),
        },
        "input_schema": [
            {
                "name": i["name"],
                "type": i.get("type", "string"),
                "required": i.get("required", True),
            }
            for i in ast.get("inputs", [])
        ],
        "output_schema": [
            {
                "name": o["name"],
                "type": o.get("type", "string"),
            }
            for o in ast.get("outputs", [])
        ],
        "runtime": {
            "model_preference": ast.get("model_preference", "any"),
            "token_budget": ast.get("token_budget", "medium"),
            "risk_level": ast.get("risk_level", "medium"),
        },
        "eval_suite": ast.get("eval_suite", ""),
        "package": {
            "has_examples": bool(ast.get("examples")),
            "has_evals": False,
            "has_scripts": False,
            "has_sub_skills": bool(ast.get("sub_skills")),
            "has_templates": False,
            "has_experiences": False,
        },
        "provenance": {
            "migrated_from": source_xml,
            "migration_date": date.today().isoformat(),
            "migration_tool": "xskill-migrator",
            "validated": False,
        },
    }

    return json.dumps(manifest, indent=2)

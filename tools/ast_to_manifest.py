"""AST -> manifest.json renderer.

Renders a normalized AST dictionary into a manifest.json
for machine validation, indexing, and routing.
"""
import json
from datetime import date
from typing import Any


def _schema_items(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Normalize AST I/O items into manifest schema entries."""
    schema_items = []
    for item in items:
        schema_entry = {
            "name": item["name"],
            "type": item.get("type", "string"),
            "required": item.get("required", True),
        }
        if item.get("condition"):
            schema_entry["condition"] = item["condition"]
        schema_items.append(schema_entry)
    return schema_items


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
        "input_schema": _schema_items(ast.get("inputs", [])),
        "output_schema": _schema_items(ast.get("outputs", [])),
        "optional_input_schema": _schema_items(ast.get("optional_inputs", [])),
        "conditional_input_schema": _schema_items(ast.get("conditional_inputs", [])),
        "optional_output_schema": _schema_items(ast.get("optional_outputs", [])),
        "conditional_output_schema": _schema_items(ast.get("conditional_outputs", [])),
        "phase_type": ast.get("phase_type", ""),
        "maturity_stage": ast.get("maturity_stage", ""),
        "runtime": {
            "model_preference": ast.get("model_preference", "any"),
            "token_budget": ast.get("token_budget", "medium"),
            "risk_level": ast.get("risk_level", "medium"),
        },
        "eval_suite": ast.get("eval_suite", ""),
        "domain_context": ast.get("domain_context", {}),
        "eval_expectations": ast.get("eval_expectations", {}),
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

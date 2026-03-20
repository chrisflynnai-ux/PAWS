"""AST -> skill.md renderer.

Renders a normalized AST dictionary into a canonical skill.md
with YAML frontmatter and structured body sections.
"""
import yaml
from typing import Any


def render_skill_md(ast: dict[str, Any]) -> str:
    """Render a skill AST into canonical skill.md format.

    Args:
        ast: Normalized skill dictionary from xml_to_ast.parse_xml_skill().

    Returns:
        Complete skill.md content as a string.
    """
    # Build frontmatter
    fm = {
        "id": ast["id"],
        "name": ast["name"],
        "version": ast["version"],
        "status": ast["status"],
        "owner": ast["owner"],
        "category": ast["category"],
        "tags": ast["tags"],
        "description": ast["description"],
        "inputs": [i["name"] for i in ast.get("inputs", [])],
        "outputs": [o["name"] for o in ast.get("outputs", [])],
        "depends_on": ast.get("depends_on", []),
        "delegates_to": ast.get("delegates_to", []),
        "complements": ast.get("complements", []),
        "required_tools": ast.get("required_tools", []),
        "memory_reads": ast.get("memory_reads", []),
        "memory_writes": ast.get("memory_writes", []),
        "token_budget": ast.get("token_budget", "medium"),
        "risk_level": ast.get("risk_level", "medium"),
        "model_preference": ast.get("model_preference", "any"),
        "eval_suite": ast.get("eval_suite", ""),
    }

    lines = ["---"]
    lines.append(yaml.dump(fm, default_flow_style=False, sort_keys=False).strip())
    lines.append("---")
    lines.append("")

    # Title
    lines.append(f"# {ast['name']}")
    lines.append("")
    lines.append(ast["description"])
    lines.append("")

    # Purpose
    lines.append("## Purpose")
    lines.append("")
    lines.append(ast.get("purpose", "") or "TODO: Define the purpose of this skill.")
    lines.append("")

    # Use When
    lines.append("## Use When")
    lines.append("")
    if ast.get("use_when"):
        for item in ast["use_when"]:
            lines.append(f"- {item}")
    else:
        lines.append("- TODO: Define activation triggers")
    lines.append("")

    # Do Not Use When
    lines.append("## Do Not Use When")
    lines.append("")
    if ast.get("do_not_use_when"):
        for item in ast["do_not_use_when"]:
            lines.append(f"- {item}")
    else:
        lines.append("- TODO: Define exclusion conditions")
    lines.append("")

    # Inputs
    lines.append("## Inputs")
    lines.append("")
    if ast.get("inputs"):
        lines.append("| Input | Type | Required | Description |")
        lines.append("|-------|------|----------|-------------|")
        for inp in ast["inputs"]:
            req = "yes" if inp.get("required", True) else "no"
            lines.append(f"| {inp['name']} | {inp.get('type', 'string')} | {req} | {inp.get('description', '')} |")
    else:
        lines.append("No formal inputs defined.")
    lines.append("")

    # Outputs
    lines.append("## Outputs")
    lines.append("")
    if ast.get("outputs"):
        lines.append("| Output | Type | Description |")
        lines.append("|--------|------|-------------|")
        for out in ast["outputs"]:
            lines.append(f"| {out['name']} | {out.get('type', 'string')} | {out.get('description', '')} |")
    else:
        lines.append("No formal outputs defined.")
    lines.append("")

    # Workflow
    lines.append("## Workflow")
    lines.append("")
    if ast.get("workflow_steps"):
        for i, step in enumerate(ast["workflow_steps"], 1):
            lines.append(f"{i}. {step}")
    else:
        lines.append("TODO: Define workflow steps.")
    lines.append("")

    # Failure Modes
    lines.append("## Failure Modes")
    lines.append("")
    if ast.get("failure_modes"):
        lines.append("| Failure | Detection | Recovery |")
        lines.append("|---------|-----------|----------|")
        for fm in ast["failure_modes"]:
            lines.append(f"| {fm.get('name', '')} | {fm.get('detection', '')} | {fm.get('recovery', '')} |")
    else:
        lines.append("No failure modes documented yet.")
    lines.append("")

    # Examples
    lines.append("## Examples")
    lines.append("")
    if ast.get("examples"):
        for ex in ast["examples"]:
            lines.append(f"### {ex.get('title', 'Example')}")
            lines.append("")
            lines.append(ex.get("content", ""))
            lines.append("")
    else:
        lines.append("TODO: Add usage examples.")
    lines.append("")

    # Notes
    lines.append("## Notes")
    lines.append("")
    lines.append(ast.get("notes", "") or "No additional notes.")
    lines.append("")

    return "\n".join(lines)

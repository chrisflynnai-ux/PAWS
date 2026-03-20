"""AST -> skill.md renderer.

Renders a normalized AST dictionary into a canonical skill.md
with YAML frontmatter and structured body sections.
"""
import yaml
from typing import Any


def _field_names(items: list[dict[str, Any]]) -> list[str]:
    """Extract just the item names for frontmatter arrays."""
    return [item["name"] for item in items if item.get("name")]


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
        "optional_inputs": _field_names(ast.get("optional_inputs", [])),
        "conditional_inputs": _field_names(ast.get("conditional_inputs", [])),
        "outputs": [o["name"] for o in ast.get("outputs", [])],
        "optional_outputs": _field_names(ast.get("optional_outputs", [])),
        "conditional_outputs": _field_names(ast.get("conditional_outputs", [])),
        "depends_on": ast.get("depends_on", []),
        "delegates_to": ast.get("delegates_to", []),
        "complements": ast.get("complements", []),
        "required_tools": ast.get("required_tools", []),
        "memory_reads": ast.get("memory_reads", []),
        "memory_writes": ast.get("memory_writes", []),
        "phase_type": ast.get("phase_type", ""),
        "maturity_stage": ast.get("maturity_stage", ""),
        "token_budget": ast.get("token_budget", "medium"),
        "risk_level": ast.get("risk_level", "medium"),
        "model_preference": ast.get("model_preference", "any"),
        "eval_suite": ast.get("eval_suite", ""),
    }
    if ast.get("domain_context"):
        fm["domain_context"] = ast["domain_context"]
    if ast.get("eval_expectations"):
        fm["eval_expectations"] = ast["eval_expectations"]

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
    all_inputs = (
        [(item, "required") for item in ast.get("inputs", [])]
        + [(item, "optional") for item in ast.get("optional_inputs", [])]
        + [(item, f"conditional ({item.get('condition', 'see workflow')})") for item in ast.get("conditional_inputs", [])]
    )
    if all_inputs:
        lines.append("| Input | Type | Requirement | Description |")
        lines.append("|-------|------|-------------|-------------|")
        for inp, requirement in all_inputs:
            lines.append(
                f"| {inp['name']} | {inp.get('type', 'string')} | {requirement} | {inp.get('description', '')} |"
            )
    else:
        lines.append("No formal inputs defined.")
    lines.append("")

    # Outputs
    lines.append("## Outputs")
    lines.append("")
    all_outputs = (
        [(item, "primary") for item in ast.get("outputs", [])]
        + [(item, "optional") for item in ast.get("optional_outputs", [])]
        + [(item, f"conditional ({item.get('condition', 'see workflow')})") for item in ast.get("conditional_outputs", [])]
    )
    if all_outputs:
        lines.append("| Output | Type | Requirement | Description |")
        lines.append("|--------|------|-------------|-------------|")
        for out, requirement in all_outputs:
            lines.append(
                f"| {out['name']} | {out.get('type', 'string')} | {requirement} | {out.get('description', '')} |"
            )
    else:
        lines.append("No formal outputs defined.")
    lines.append("")

    if ast.get("phase_type") or ast.get("maturity_stage"):
        lines.append("## Phase Behavior")
        lines.append("")
        if ast.get("phase_type"):
            lines.append(f"- Phase Type: `{ast['phase_type']}`")
        if ast.get("maturity_stage"):
            lines.append(f"- Maturity Stage: `{ast['maturity_stage']}`")
        lines.append("")

    if ast.get("domain_context"):
        lines.append("## Domain Context")
        lines.append("")
        context = ast["domain_context"]
        lines.append(f"- Primary Domain: `{context.get('primary_domain', 'general')}`")
        if context.get("sub_domain"):
            lines.append(f"- Sub Domain: `{context['sub_domain']}`")
        if context.get("market_awareness"):
            lines.append(f"- Market Awareness: `{context['market_awareness']}`")
        if context.get("voice_orientation"):
            lines.append(f"- Voice Orientation: `{context['voice_orientation']}`")
        if context.get("industry_patterns"):
            lines.append(f"- Industry Patterns: {', '.join(context['industry_patterns'])}")
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

    if ast.get("eval_expectations"):
        evals = ast["eval_expectations"]
        lines.append("## Eval Expectations")
        lines.append("")
        for field in ["base_model_baseline", "skill_only_target", "skill_plus_experience"]:
            if field in evals:
                lines.append(f"- {field}: `{evals[field]}`")
        for metric in evals.get("key_metrics", []):
            lines.append(f"- Metric `{metric.get('name', 'unknown')}` target: `{metric.get('target', '')}`")
        if evals.get("control_test"):
            lines.append(f"- Control Test: {evals['control_test']}")
        lines.append("")

    # Notes
    lines.append("## Notes")
    lines.append("")
    lines.append(ast.get("notes", "") or "No additional notes.")
    lines.append("")

    return "\n".join(lines)

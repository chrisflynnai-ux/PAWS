"""XML -> AST parser for SkillML XML files.

Parses SkillML XML into a normalized Python dictionary (AST)
that can be rendered to skill.md and manifest.json.
"""
import xml.etree.ElementTree as ET
from typing import Any


def parse_xml_skill(xml_source: str | bytes) -> dict[str, Any]:
    """Parse a SkillML XML string into a normalized AST dictionary.

    Args:
        xml_source: XML string or bytes containing a <Skill> root element.

    Returns:
        Dictionary with normalized skill data.
    """
    root = ET.fromstring(xml_source)

    ast = {
        # Core identity
        "id": root.get("skill_id", ""),
        "name": root.get("name", ""),
        "version": root.get("version", "0.1.0"),
        "status": root.get("status", "draft"),
        "model_preference": root.get("model", "any"),
        "tier": root.get("tier", "draft"),

        # From Meta
        "description": "",
        "owner": "supermind",
        "tags": [],
        "category": "",
        "patch_history": [],

        # Relationships
        "depends_on": [],
        "delegates_to": [],
        "complements": [],
        "required_tools": [],

        # Memory
        "memory_reads": [],
        "memory_writes": [],

        # I/O
        "inputs": [],
        "outputs": [],

        # Content sections (for skill.md body)
        "purpose": "",
        "use_when": [],
        "do_not_use_when": [],
        "workflow_steps": [],
        "sub_skills": [],
        "failure_modes": [],
        "recovery_steps": [],
        "examples": [],
        "notes": "",

        # Runtime
        "token_budget": "medium",
        "risk_level": "medium",
        "eval_suite": "",
    }

    # Parse Meta
    meta = root.find("Meta")
    if meta is not None:
        desc = meta.find("Description")
        if desc is not None and desc.text:
            ast["description"] = desc.text.strip()

        owner = meta.find("Owner")
        if owner is not None and owner.text:
            ast["owner"] = owner.text.strip()

        tags_el = meta.find("Tags")
        if tags_el is not None:
            ast["tags"] = [t.text.strip() for t in tags_el.findall("Tag") if t.text]

        # Infer category from skill_id
        parts = ast["id"].split(".")
        if len(parts) >= 3:
            ast["category"] = parts[1]

    # Parse InputSpec
    input_spec = root.find("InputSpec")
    if input_spec is not None:
        for inp in input_spec.findall("Input"):
            ast["inputs"].append({
                "name": inp.get("name", ""),
                "type": inp.get("type", "string"),
                "required": inp.get("required", "true").lower() == "true",
                "description": (inp.text or "").strip(),
            })

    # Parse OutputSpec
    output_spec = root.find("OutputSpec")
    if output_spec is not None:
        for out in output_spec.findall("Output"):
            ast["outputs"].append({
                "name": out.get("name", ""),
                "type": out.get("type", "string"),
                "description": (out.text or "").strip(),
            })

    # Parse Dependencies/Relationships
    deps = root.find("Dependencies")
    if deps is not None:
        for dep in deps.findall("Dependency"):
            dep_type = dep.get("type", "depends_on")
            dep_id = dep.get("skill_id", dep.text or "").strip()
            if dep_id and dep_type in ast:
                ast[dep_type].append(dep_id)

    # Parse FailureModes
    fm_section = root.find(".//FailureModes")
    if fm_section is not None:
        for fm in fm_section.findall("FailureMode"):
            mode = {
                "name": fm.get("name", ""),
                "detection": "",
                "recovery": "",
            }
            name_el = fm.find("Name")
            if not mode["name"] and name_el is not None and name_el.text:
                mode["name"] = name_el.text.strip()
            det = fm.find("Detection")
            if det is not None and det.text:
                mode["detection"] = det.text.strip()
            rec = fm.find("Recovery")
            if rec is not None and rec.text:
                mode["recovery"] = rec.text.strip()
            ast["failure_modes"].append(mode)

    # Parse Workflow/Procedure steps
    for tag_name in ["Workflow", "Procedure", "Execution"]:
        workflow = root.find(f".//{tag_name}")
        if workflow is not None:
            for step in workflow:
                if step.text:
                    ast["workflow_steps"].append(step.text.strip())
                elif step.get("name"):
                    ast["workflow_steps"].append(step.get("name"))

    # Collect raw text from major content sections for skill.md body
    for section_name in ["Purpose", "Context", "CoreInsight"]:
        el = root.find(f".//{section_name}")
        if el is not None and el.text:
            ast["purpose"] += el.text.strip() + "\n\n"
    ast["purpose"] = ast["purpose"].strip()

    return ast


def parse_xml_file(filepath: str) -> dict[str, Any]:
    """Parse a SkillML XML file from disk.

    Args:
        filepath: Path to the XML file.

    Returns:
        Normalized AST dictionary.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        return parse_xml_skill(f.read())

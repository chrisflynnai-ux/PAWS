"""XML -> AST parser for SkillML XML files.

Parses SkillML XML into a normalized Python dictionary (AST)
that can be rendered to skill.md and manifest.json.
"""
import re
import xml.etree.ElementTree as ET
from typing import Any


PHASE_TYPE_BY_TRACK = {
    "t1": "exploratory",
    "research": "exploratory",
    "t2": "compositional",
    "draft": "compositional",
    "drafts": "compositional",
    "t3": "executional",
    "production": "executional",
    "cross": "executional",
    "cross-track": "executional",
    "t4": "resonant",
    "polish": "resonant",
}

PHASE_TYPE_BY_TIER = {
    "draft": "exploratory",
    "meta": "executional",
    "production": "executional",
}

MATURITY_STAGE_BY_STATUS = {
    "draft": "seed",
    "active": "production",
    "deprecated": "mature",
    "archived": "mature",
}

MOJIBAKE_REPLACEMENTS = {
    "\u00e2\u20ac\u201d": "--",
    "\u00e2\u20ac\u201c": "-",
    "\u00e2\u20ac\u02dc": "'",
    "\u00e2\u20ac\u2122": "'",
    "\u00e2\u20ac\u0153": '"',
    "\u00e2\u20ac\u009d": '"',
    "\u00e2\u2020\u2019": "->",
    "\u00e2\u2030\u00a5": ">=",
    "\u00e2\u2030\u00a4": "<=",
}


def _normalize_text(value: str | None) -> str:
    """Normalize whitespace and common mojibake sequences."""
    if not value:
        return ""

    text = value.strip()
    for bad, good in MOJIBAKE_REPLACEMENTS.items():
        text = text.replace(bad, good)
    return re.sub(r"\s+", " ", text).strip()


def _child_text(node: ET.Element | None, tag: str) -> str:
    """Return normalized text content from a direct child tag."""
    if node is None:
        return ""
    child = node.find(tag)
    if child is None:
        return ""
    return _normalize_text(" ".join(child.itertext()))


def _infer_phase_type(track: str, tier: str) -> str:
    """Infer a skill's phase type from track/tier metadata."""
    normalized_track = _normalize_text(track).lower()
    normalized_tier = _normalize_text(tier).lower()

    if normalized_track in PHASE_TYPE_BY_TRACK:
        return PHASE_TYPE_BY_TRACK[normalized_track]
    if normalized_tier in PHASE_TYPE_BY_TIER:
        return PHASE_TYPE_BY_TIER[normalized_tier]
    return "executional"


def _extract_contract_item(item: ET.Element, required: bool) -> dict[str, Any]:
    """Extract a normalized input/output item from a contract block."""
    name = item.get("name") or _child_text(item, "Name")
    item_type = item.get("type") or item.get("format") or "string"
    description = (
        item.get("description")
        or _child_text(item, "Description")
        or _normalize_text(" ".join(item.itertext()))
    )
    condition = ""

    match = re.search(r"(required for .+)", description, flags=re.IGNORECASE)
    if match:
        condition = match.group(1)

    return {
        "name": name,
        "type": item_type,
        "required": required,
        "description": description,
        "condition": condition,
    }


def _extract_workflow_step(step: ET.Element) -> str:
    """Flatten nested workflow/process steps into a readable line."""
    name = _child_text(step, "Name")
    action = _child_text(step, "Action")
    validation = _child_text(step, "Validation")

    if name and action:
        text = f"{name}: {action}"
    elif action:
        text = action
    elif name:
        text = name
    else:
        text = _normalize_text(" ".join(step.itertext()))

    if validation:
        text = f"{text} Validation: {validation}"
    return text


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
        "optional_inputs": [],
        "conditional_inputs": [],
        "outputs": [],
        "optional_outputs": [],
        "conditional_outputs": [],

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
        "phase_type": "",
        "maturity_stage": "",
        "domain_context": {},
        "eval_expectations": {},
    }

    meta = root.find("Meta")
    if meta is not None:
        description = _child_text(meta, "Description")
        if description:
            ast["description"] = description

        owner = _child_text(meta, "Owner")
        if owner:
            ast["owner"] = owner

        tags_el = meta.find("Tags")
        if tags_el is not None:
            ast["tags"] = [_normalize_text(t.text) for t in tags_el.findall("Tag") if _normalize_text(t.text)]

        domain = _child_text(meta, "Domain")
        if domain:
            ast["category"] = domain.lower()

        track = _child_text(meta, "Track")
        if track or ast["tier"]:
            ast["phase_type"] = _infer_phase_type(track, ast["tier"])

        parts = ast["id"].split(".")
        if len(parts) >= 3 and not ast["category"]:
            ast["category"] = parts[1]

    ast["phase_type"] = ast["phase_type"] or _infer_phase_type("", ast["tier"])
    ast["maturity_stage"] = MATURITY_STAGE_BY_STATUS.get(ast["status"], "developing")

    input_spec = root.find("InputSpec")
    if input_spec is not None:
        for inp in input_spec.findall("Input"):
            ast["inputs"].append({
                "name": inp.get("name", ""),
                "type": inp.get("type", "string"),
                "required": inp.get("required", "true").lower() == "true",
                "description": _normalize_text(inp.text),
            })

    output_spec = root.find("OutputSpec")
    if output_spec is not None:
        for out in output_spec.findall("Output"):
            ast["outputs"].append({
                "name": out.get("name", ""),
                "type": out.get("type", "string"),
                "required": True,
                "description": _normalize_text(out.text),
            })

    contract = root.find("Contract")
    if contract is not None:
        for block_name, target_key, required in [
            ("InputsRequired", "inputs", True),
            ("OutputsPrimary", "outputs", True),
        ]:
            block = contract.find(block_name)
            if block is None:
                continue
            item_tag = "Input" if "Input" in block_name else "Output"
            for item in block.findall(item_tag):
                parsed = _extract_contract_item(item, required=required)
                if parsed["name"]:
                    ast[target_key].append(parsed)

        inputs_optional = contract.find("InputsOptional")
        if inputs_optional is not None:
            for item in inputs_optional.findall("Input"):
                parsed = _extract_contract_item(item, required=False)
                if not parsed["name"]:
                    continue
                if parsed["condition"]:
                    ast["conditional_inputs"].append(parsed)
                else:
                    ast["optional_inputs"].append(parsed)

        outputs_optional = contract.find("OutputsOptional")
        if outputs_optional is not None:
            for item in outputs_optional.findall("Output"):
                parsed = _extract_contract_item(item, required=False)
                if not parsed["name"]:
                    continue
                if parsed["condition"]:
                    ast["conditional_outputs"].append(parsed)
                else:
                    ast["optional_outputs"].append(parsed)

    deps = root.find("Dependencies")
    if deps is not None:
        for dep in deps.findall("Dependency"):
            dep_type = dep.get("type", "depends_on")
            dep_id = dep.get("skill_id", dep.text or "").strip()
            if dep_id and dep_type in ast:
                ast[dep_type].append(dep_id)

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
                mode["name"] = _normalize_text(name_el.text)
            det = fm.find("Detection")
            if det is not None and det.text:
                mode["detection"] = _normalize_text(det.text)
            rec = fm.find("Recovery")
            if rec is not None and rec.text:
                mode["recovery"] = _normalize_text(rec.text)
            ast["failure_modes"].append(mode)

    for tag_name in ["Workflow", "Procedure", "Execution"]:
        workflow = root.find(f".//{tag_name}")
        if workflow is not None:
            for step in workflow:
                step_text = _extract_workflow_step(step)
                if step_text:
                    ast["workflow_steps"].append(step_text)

    for step in root.findall(".//ReasoningFramework/Step"):
        step_text = _extract_workflow_step(step)
        if step_text:
            ast["workflow_steps"].append(step_text)

    for step in root.findall(".//Process/Step"):
        step_text = _extract_workflow_step(step)
        if step_text:
            ast["workflow_steps"].append(step_text)

    for trigger in root.findall(".//UseWhen/Trigger"):
        trigger_text = _normalize_text(" ".join(trigger.itertext()))
        if trigger_text:
            ast["use_when"].append(trigger_text)

    for trigger in root.findall(".//DoNotUseWhen/Trigger"):
        trigger_text = _normalize_text(" ".join(trigger.itertext()))
        if trigger_text:
            ast["do_not_use_when"].append(trigger_text)

    for section_name in ["Purpose", "Context", "CoreInsight"]:
        el = root.find(f".//{section_name}")
        if el is not None:
            section_text = _normalize_text(" ".join(el.itertext()))
            if section_text:
                ast["purpose"] += section_text + "\n\n"
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

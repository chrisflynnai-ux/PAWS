"""Structural validator and drift detector for XSkill packages.

Layer 1: Validates frontmatter fields and manifest schema.
Layer 2: Detects drift between skill.md and manifest.json.
"""
from typing import Any


REQUIRED_FRONTMATTER = ["id", "name", "version", "status", "owner", "category", "tags", "description", "inputs", "outputs"]
SYNC_FIELDS = [
    "id",
    "version",
    "status",
    "category",
    "tags",
    "phase_type",
    "maturity_stage",
    "domain_context",
    "eval_expectations",
]
SCHEMA_SYNC_FIELDS = {
    "inputs": "input_schema",
    "optional_inputs": "optional_input_schema",
    "conditional_inputs": "conditional_input_schema",
    "outputs": "output_schema",
    "optional_outputs": "optional_output_schema",
    "conditional_outputs": "conditional_output_schema",
}
PHASE_TYPES = {"exploratory", "compositional", "executional", "resonant"}
MATURITY_STAGES = {"seed", "developing", "production", "mature"}


def _validate_name_list(field: str, value: Any, errors: list[str]) -> None:
    """Validate a frontmatter list of names."""
    if value is None:
        return
    if not isinstance(value, list):
        errors.append(f"Field '{field}' must be a list")
        return
    if any(not isinstance(item, str) or not item for item in value):
        errors.append(f"Field '{field}' must contain only non-empty strings")


def _validate_domain_context(domain_context: Any, errors: list[str], field_name: str = "domain_context") -> None:
    """Validate the structured domain context block when present."""
    if domain_context in ({}, None):
        return
    if not isinstance(domain_context, dict):
        errors.append(f"Field '{field_name}' must be an object")
        return

    industry_patterns = domain_context.get("industry_patterns", [])
    if industry_patterns and (not isinstance(industry_patterns, list) or any(not isinstance(item, str) for item in industry_patterns)):
        errors.append(f"Field '{field_name}.industry_patterns' must be a list of strings")


def _validate_eval_expectations(eval_expectations: Any, errors: list[str], field_name: str = "eval_expectations") -> None:
    """Validate the eval expectations block when present."""
    if eval_expectations in ({}, None):
        return
    if not isinstance(eval_expectations, dict):
        errors.append(f"Field '{field_name}' must be an object")
        return

    for metric_field in ["base_model_baseline", "skill_only_target", "skill_plus_experience"]:
        if metric_field in eval_expectations and not isinstance(eval_expectations[metric_field], (int, float)):
            errors.append(f"Field '{field_name}.{metric_field}' must be numeric")

    key_metrics = eval_expectations.get("key_metrics", [])
    if key_metrics and not isinstance(key_metrics, list):
        errors.append(f"Field '{field_name}.key_metrics' must be a list")
        return

    for metric in key_metrics:
        if not isinstance(metric, dict):
            errors.append(f"Field '{field_name}.key_metrics' must contain objects")
            continue
        if "name" not in metric or "target" not in metric:
            errors.append(f"Field '{field_name}.key_metrics' entries require 'name' and 'target'")


def validate_frontmatter(fm: dict[str, Any]) -> list[str]:
    """Validate skill.md frontmatter against required fields.

    Args:
        fm: Parsed YAML frontmatter dictionary.

    Returns:
        List of error strings. Empty list means valid.
    """
    errors = []

    for field in REQUIRED_FRONTMATTER:
        if field not in fm:
            errors.append(f"Missing required field: {field}")

    if "id" in fm and not isinstance(fm["id"], str):
        errors.append("Field 'id' must be a string")

    if "version" in fm:
        parts = str(fm["version"]).split(".")
        if len(parts) != 3:
            errors.append(f"Field 'version' must be semver (got: {fm['version']})")

    if "status" in fm and fm["status"] not in ("draft", "active", "deprecated", "archived"):
        errors.append(f"Invalid status: {fm['status']}")

    if "tags" in fm and (not isinstance(fm["tags"], list) or len(fm["tags"]) == 0):
        errors.append("Field 'tags' must be a non-empty list")

    if "description" in fm and (not isinstance(fm["description"], str) or len(fm["description"]) < 10):
        errors.append("Field 'description' must be at least 10 characters")

    for field in [
        "inputs",
        "optional_inputs",
        "conditional_inputs",
        "outputs",
        "optional_outputs",
        "conditional_outputs",
    ]:
        _validate_name_list(field, fm.get(field), errors)

    if "phase_type" in fm and fm["phase_type"] and fm["phase_type"] not in PHASE_TYPES:
        errors.append(f"Invalid phase_type: {fm['phase_type']}")

    if "maturity_stage" in fm and fm["maturity_stage"] and fm["maturity_stage"] not in MATURITY_STAGES:
        errors.append(f"Invalid maturity_stage: {fm['maturity_stage']}")

    _validate_domain_context(fm.get("domain_context"), errors)
    _validate_eval_expectations(fm.get("eval_expectations"), errors)

    return errors


def validate_manifest(manifest: dict[str, Any]) -> list[str]:
    """Validate manifest.json against required fields.

    Args:
        manifest: Parsed manifest dictionary.

    Returns:
        List of error strings.
    """
    errors = []
    required = ["id", "name", "version", "status", "category", "tags",
                 "relationships", "memory_contract", "input_schema", "output_schema", "runtime"]

    for field in required:
        if field not in manifest:
            errors.append(f"Manifest missing required field: {field}")

    if "relationships" in manifest:
        for rel in ["depends_on", "delegates_to", "complements"]:
            if rel not in manifest["relationships"]:
                errors.append(f"Manifest relationships missing: {rel}")

    if "memory_contract" in manifest:
        for key in ["reads", "writes"]:
            if key not in manifest["memory_contract"]:
                errors.append(f"Manifest memory_contract missing: {key}")

    for field in [
        "input_schema",
        "optional_input_schema",
        "conditional_input_schema",
        "output_schema",
        "optional_output_schema",
        "conditional_output_schema",
    ]:
        if field in manifest and not isinstance(manifest[field], list):
            errors.append(f"Manifest field '{field}' must be a list")

    if "phase_type" in manifest and manifest["phase_type"] and manifest["phase_type"] not in PHASE_TYPES:
        errors.append(f"Manifest phase_type invalid: {manifest['phase_type']}")

    if "maturity_stage" in manifest and manifest["maturity_stage"] and manifest["maturity_stage"] not in MATURITY_STAGES:
        errors.append(f"Manifest maturity_stage invalid: {manifest['maturity_stage']}")

    _validate_domain_context(manifest.get("domain_context"), errors)
    _validate_eval_expectations(manifest.get("eval_expectations"), errors)

    return errors


def detect_drift(frontmatter: dict[str, Any], manifest: dict[str, Any]) -> list[str]:
    """Detect drift between skill.md frontmatter and manifest.json.

    Args:
        frontmatter: Parsed YAML frontmatter from skill.md.
        manifest: Parsed manifest.json.

    Returns:
        List of drift descriptions.
    """
    drifts = []

    for field in SYNC_FIELDS:
        fm_val = frontmatter.get(field)
        mf_val = manifest.get(field)
        if fm_val is not None and mf_val is not None and fm_val != mf_val:
            drifts.append(f"Drift on '{field}': skill.md={fm_val} vs manifest.json={mf_val}")

    for fm_field, mf_field in SCHEMA_SYNC_FIELDS.items():
        fm_val = frontmatter.get(fm_field, [])
        mf_val = [item.get("name") for item in manifest.get(mf_field, [])]
        if fm_val != mf_val:
            drifts.append(f"Drift on '{fm_field}': skill.md={fm_val} vs manifest.json={mf_val}")

    return drifts

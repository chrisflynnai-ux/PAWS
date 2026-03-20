"""Structural validator and drift detector for XSkill packages.

Layer 1: Validates frontmatter fields and manifest schema.
Layer 2: Detects drift between skill.md and manifest.json.
"""
from typing import Any


REQUIRED_FRONTMATTER = ["id", "name", "version", "status", "owner", "category", "tags", "description", "inputs", "outputs"]
SYNC_FIELDS = ["id", "version", "status", "category", "tags"]


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

    return drifts

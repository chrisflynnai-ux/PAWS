"""Tests for structural validator."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from validate import validate_frontmatter, validate_manifest, detect_drift


def test_valid_frontmatter_passes():
    fm = {
        "id": "skill.copy.test.v1_0_0",
        "name": "Test Skill",
        "version": "1.0.0",
        "status": "active",
        "owner": "supermind",
        "category": "copy",
        "tags": ["test"],
        "description": "A valid test skill for pipeline.",
        "inputs": ["brief"],
        "outputs": ["draft"],
    }
    errors = validate_frontmatter(fm)
    assert errors == [], f"Expected no errors, got: {errors}"


def test_missing_required_field_fails():
    fm = {"id": "skill.copy.test.v1_0_0", "name": "Test"}
    errors = validate_frontmatter(fm)
    assert len(errors) > 0
    assert any("version" in e for e in errors)


def test_drift_detection_catches_mismatch():
    fm = {"id": "skill.copy.test.v1_0_0", "version": "1.0.0", "status": "active"}
    manifest = {"id": "skill.copy.test.v1_0_0", "version": "2.0.0", "status": "active"}
    drifts = detect_drift(fm, manifest)
    assert len(drifts) > 0
    assert any("version" in d for d in drifts)


def test_no_drift_when_in_sync():
    fm = {"id": "skill.copy.test.v1_0_0", "version": "1.0.0", "status": "active"}
    manifest = {"id": "skill.copy.test.v1_0_0", "version": "1.0.0", "status": "active"}
    drifts = detect_drift(fm, manifest)
    assert drifts == []


if __name__ == "__main__":
    test_valid_frontmatter_passes()
    test_missing_required_field_fails()
    test_drift_detection_catches_mismatch()
    test_no_drift_when_in_sync()
    print("All tests passed!")

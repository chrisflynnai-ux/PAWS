"""Tests for AST -> manifest.json renderer."""
import json
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from ast_to_manifest import render_manifest


def test_render_produces_valid_json():
    ast = {
        "id": "skill.copy.test.v1_0_0",
        "name": "Test Skill",
        "version": "1.0.0",
        "status": "active",
        "category": "copy",
        "tags": ["test"],
        "description": "A test skill.",
        "depends_on": [],
        "delegates_to": [],
        "complements": [],
        "required_tools": [],
        "memory_reads": ["obsidian"],
        "memory_writes": ["experience_bank"],
        "inputs": [{"name": "brief", "type": "string", "required": True, "description": "The brief"}],
        "outputs": [{"name": "draft", "type": "string", "description": "Output"}],
        "token_budget": "medium",
        "risk_level": "medium",
        "model_preference": "sonnet",
        "eval_suite": "",
        "examples": [],
        "sub_skills": [],
    }
    manifest = render_manifest(ast)
    parsed = json.loads(manifest)
    assert parsed["id"] == "skill.copy.test.v1_0_0"
    assert parsed["relationships"]["depends_on"] == []
    assert parsed["memory_contract"]["reads"] == ["obsidian"]
    assert parsed["memory_contract"]["writes"] == ["experience_bank"]
    assert len(parsed["input_schema"]) == 1
    assert parsed["runtime"]["model_preference"] == "sonnet"


if __name__ == "__main__":
    test_render_produces_valid_json()
    print("All tests passed!")

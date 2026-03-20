"""Tests for AST -> skill.md renderer."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from ast_to_skill_md import render_skill_md


SAMPLE_AST = {
    "id": "skill.copy.test.v1_0_0",
    "name": "Test Skill",
    "version": "1.0.0",
    "status": "active",
    "owner": "supermind",
    "category": "copy",
    "tags": ["test", "copy"],
    "description": "A test skill for validation.",
    "inputs": [{"name": "brief", "type": "string", "required": True, "description": "The brief"}],
    "outputs": [{"name": "draft", "type": "string", "description": "The output"}],
    "depends_on": [],
    "delegates_to": [],
    "complements": [],
    "required_tools": [],
    "memory_reads": [],
    "memory_writes": [],
    "token_budget": "medium",
    "risk_level": "medium",
    "model_preference": "sonnet",
    "purpose": "Tests the rendering pipeline.",
    "use_when": [],
    "do_not_use_when": [],
    "workflow_steps": ["Analyze", "Draft", "Review"],
    "sub_skills": [],
    "failure_modes": [],
    "recovery_steps": [],
    "examples": [],
    "notes": "",
    "tier": "production",
    "patch_history": [],
    "eval_suite": "",
}


def test_render_produces_valid_frontmatter():
    md = render_skill_md(SAMPLE_AST)
    assert md.startswith("---\n")
    assert "id: skill.copy.test.v1_0_0" in md
    assert "# Test Skill" in md
    assert "## Purpose" in md
    assert "## Workflow" in md
    assert "| brief |" in md


def test_render_handles_empty_sections():
    minimal = {
        "id": "skill.copy.minimal.v1_0_0",
        "name": "Minimal",
        "version": "1.0.0",
        "status": "draft",
        "owner": "supermind",
        "category": "copy",
        "tags": ["test"],
        "description": "Bare minimum.",
        "inputs": [], "outputs": [],
        "depends_on": [], "delegates_to": [], "complements": [],
        "required_tools": [], "memory_reads": [], "memory_writes": [],
        "token_budget": "medium", "risk_level": "medium", "model_preference": "any",
        "purpose": "", "use_when": [], "do_not_use_when": [],
        "workflow_steps": [], "sub_skills": [], "failure_modes": [],
        "recovery_steps": [], "examples": [], "notes": "",
        "tier": "draft", "patch_history": [], "eval_suite": "",
    }
    md = render_skill_md(minimal)
    assert "---\n" in md
    assert "# Minimal" in md


if __name__ == "__main__":
    test_render_produces_valid_frontmatter()
    test_render_handles_empty_sections()
    print("All tests passed!")

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
    "optional_inputs": [{"name": "voice_guide", "type": "yaml", "required": False, "description": "Optional voice guide"}],
    "conditional_inputs": [{"name": "evidence_pack", "type": "yaml", "required": False, "description": "Required for T3+", "condition": "required for T3+"}],
    "outputs": [{"name": "draft", "type": "string", "description": "The output"}],
    "optional_outputs": [],
    "conditional_outputs": [{"name": "escalation_packet", "type": "json", "description": "Emitted on halt", "condition": "on circuit breaker"}],
    "depends_on": [],
    "delegates_to": [],
    "complements": [],
    "required_tools": [],
    "memory_reads": [],
    "memory_writes": [],
    "phase_type": "executional",
    "maturity_stage": "production",
    "domain_context": {
        "primary_domain": "general",
        "sub_domain": "",
        "market_awareness": "direct_response",
        "industry_patterns": ["proof"],
        "voice_orientation": "conversational",
    },
    "eval_expectations": {
        "base_model_baseline": 0.45,
        "skill_only_target": 0.65,
        "skill_plus_experience": 0.8,
        "key_metrics": [{"name": "task_completion_rate", "target": 0.85}],
        "control_test": "Compare with and without the skill",
    },
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
    assert "phase_type: executional" in md
    assert "conditional_inputs:" in md
    assert "# Test Skill" in md
    assert "## Purpose" in md
    assert "## Phase Behavior" in md
    assert "## Domain Context" in md
    assert "## Eval Expectations" in md
    assert "## Workflow" in md
    assert "| brief |" in md
    assert "evidence_pack" in md


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
        "inputs": [], "optional_inputs": [], "conditional_inputs": [],
        "outputs": [], "optional_outputs": [], "conditional_outputs": [],
        "depends_on": [], "delegates_to": [], "complements": [],
        "required_tools": [], "memory_reads": [], "memory_writes": [],
        "phase_type": "executional", "maturity_stage": "developing",
        "domain_context": {}, "eval_expectations": {},
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

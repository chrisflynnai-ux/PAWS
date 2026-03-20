# Day 1: Schema Lock + Pipeline Tooling — Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Lock the three canonical schemas (skill.md frontmatter, manifest.json, experiences.jsonl) and build the XML → AST → skill.md → manifest.json migration pipeline.

**Architecture:** XML skills are parsed into a normalized Python AST (dictionary). The AST is then rendered to canonical skill.md (with YAML frontmatter) and manifest.json. A drift detector validates they stay in sync. Experiences are seeded separately.

**Tech Stack:** Python 3.x, JSON Schema (jsonschema lib), PyYAML, xml.etree.ElementTree

---

## Chunk 1: Schema Definitions

### Task 1: Create the skill.md frontmatter JSON Schema

**Files:**
- Create: `schemas/skill-frontmatter.schema.json`

- [ ] **Step 1: Write the JSON Schema file**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "XSkill Frontmatter Schema",
  "description": "Required YAML frontmatter for every skill.md file",
  "type": "object",
  "required": ["id", "name", "version", "status", "owner", "category", "tags", "description", "inputs", "outputs"],
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^skill\\.[a-z_]+\\.[a-z_]+\\.v[0-9]+_[0-9]+_[0-9]+$",
      "description": "Unique skill identifier: skill.<family>.<name>.v<major>_<minor>_<patch>"
    },
    "name": {
      "type": "string",
      "minLength": 3,
      "maxLength": 80
    },
    "version": {
      "type": "string",
      "pattern": "^[0-9]+\\.[0-9]+\\.[0-9]+$"
    },
    "status": {
      "type": "string",
      "enum": ["draft", "active", "deprecated", "archived"]
    },
    "owner": {
      "type": "string",
      "default": "supermind"
    },
    "category": {
      "type": "string",
      "enum": ["copy", "research", "design", "ads", "email", "leadgen", "product", "meta", "systems", "automations", "knowledge", "voice", "social", "video", "webinar", "writing", "advisor", "tools"]
    },
    "tags": {
      "type": "array",
      "items": { "type": "string" },
      "minItems": 1
    },
    "description": {
      "type": "string",
      "minLength": 10,
      "maxLength": 300
    },
    "inputs": {
      "type": "array",
      "items": { "type": "string" }
    },
    "outputs": {
      "type": "array",
      "items": { "type": "string" }
    },
    "depends_on": {
      "type": "array",
      "items": { "type": "string" },
      "default": []
    },
    "delegates_to": {
      "type": "array",
      "items": { "type": "string" },
      "default": []
    },
    "complements": {
      "type": "array",
      "items": { "type": "string" },
      "default": []
    },
    "required_tools": {
      "type": "array",
      "items": { "type": "string" },
      "default": []
    },
    "memory_reads": {
      "type": "array",
      "items": { "type": "string", "enum": ["obsidian", "threadex", "experience_bank", "session_state"] },
      "default": []
    },
    "memory_writes": {
      "type": "array",
      "items": { "type": "string", "enum": ["obsidian", "threadex", "experience_bank", "session_state"] },
      "default": []
    },
    "token_budget": {
      "type": "string",
      "enum": ["micro", "small", "medium", "large", "unbounded"],
      "default": "medium"
    },
    "risk_level": {
      "type": "string",
      "enum": ["low", "medium", "high", "critical"],
      "default": "medium"
    },
    "model_preference": {
      "type": "string",
      "enum": ["opus", "sonnet", "haiku", "codex", "gemini", "any"],
      "default": "any"
    },
    "eval_suite": {
      "type": "string",
      "default": ""
    }
  },
  "additionalProperties": false
}
```

- [ ] **Step 2: Commit**

```bash
git add schemas/skill-frontmatter.schema.json
git commit -m "feat: add skill.md frontmatter JSON Schema"
```

### Task 2: Create the manifest.json JSON Schema

**Files:**
- Create: `schemas/manifest.schema.json`

- [ ] **Step 1: Write the JSON Schema file**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "XSkill Manifest Schema",
  "description": "Machine-readable compiled manifest for each skill package",
  "type": "object",
  "required": ["id", "name", "version", "status", "category", "tags", "relationships", "memory_contract", "input_schema", "output_schema", "runtime"],
  "properties": {
    "id": { "type": "string" },
    "name": { "type": "string" },
    "version": { "type": "string", "pattern": "^[0-9]+\\.[0-9]+\\.[0-9]+$" },
    "status": { "type": "string", "enum": ["draft", "active", "deprecated", "archived"] },
    "category": { "type": "string" },
    "tags": { "type": "array", "items": { "type": "string" } },
    "description": { "type": "string" },
    "relationships": {
      "type": "object",
      "properties": {
        "depends_on": { "type": "array", "items": { "type": "string" } },
        "delegates_to": { "type": "array", "items": { "type": "string" } },
        "complements": { "type": "array", "items": { "type": "string" } }
      },
      "required": ["depends_on", "delegates_to", "complements"]
    },
    "tool_requirements": {
      "type": "array",
      "items": { "type": "string" },
      "default": []
    },
    "memory_contract": {
      "type": "object",
      "properties": {
        "reads": { "type": "array", "items": { "type": "string" } },
        "writes": { "type": "array", "items": { "type": "string" } }
      },
      "required": ["reads", "writes"]
    },
    "input_schema": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": { "type": "string" },
          "type": { "type": "string", "default": "string" },
          "required": { "type": "boolean", "default": true }
        },
        "required": ["name"]
      }
    },
    "output_schema": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": { "type": "string" },
          "type": { "type": "string", "default": "string" }
        },
        "required": ["name"]
      }
    },
    "runtime": {
      "type": "object",
      "properties": {
        "model_preference": { "type": "string", "default": "any" },
        "token_budget": { "type": "string", "default": "medium" },
        "risk_level": { "type": "string", "default": "medium" }
      }
    },
    "eval_suite": { "type": "string", "default": "" },
    "package": {
      "type": "object",
      "properties": {
        "has_examples": { "type": "boolean" },
        "has_evals": { "type": "boolean" },
        "has_scripts": { "type": "boolean" },
        "has_sub_skills": { "type": "boolean" },
        "has_templates": { "type": "boolean" },
        "has_experiences": { "type": "boolean" }
      }
    },
    "provenance": {
      "type": "object",
      "properties": {
        "migrated_from": { "type": "string", "description": "Original XML filename" },
        "migration_date": { "type": "string", "format": "date" },
        "migration_tool": { "type": "string", "default": "xskill-migrator" },
        "validated": { "type": "boolean", "default": false }
      }
    }
  },
  "additionalProperties": false
}
```

- [ ] **Step 2: Commit**

```bash
git add schemas/manifest.schema.json
git commit -m "feat: add manifest.json JSON Schema"
```

### Task 3: Create the experiences.jsonl record schema

**Files:**
- Create: `schemas/experience.schema.json`

- [ ] **Step 1: Write the JSON Schema file**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "XSkill Experience Record Schema",
  "description": "Schema for individual records in experiences.jsonl",
  "type": "object",
  "required": ["experience_id", "skill_id", "timestamp", "scenario", "outcome"],
  "properties": {
    "experience_id": {
      "type": "string",
      "pattern": "^exp-[a-z0-9]{8}$",
      "description": "Unique ID: exp-<8 char hex>"
    },
    "skill_id": {
      "type": "string",
      "description": "References the skill this experience belongs to"
    },
    "timestamp": {
      "type": "string",
      "format": "date-time"
    },
    "scenario": {
      "type": "string",
      "description": "What situation triggered this experience"
    },
    "trigger": {
      "type": "string",
      "description": "Specific input or condition"
    },
    "action_taken": {
      "type": "string",
      "description": "What the agent did"
    },
    "tool_choice": {
      "type": "string",
      "description": "Which tool was selected and why"
    },
    "failure_mode": {
      "type": "string",
      "default": "",
      "description": "What went wrong, if anything"
    },
    "recovery_tactic": {
      "type": "string",
      "default": "",
      "description": "How the agent recovered"
    },
    "outcome": {
      "type": "string",
      "enum": ["success", "partial", "failure", "unknown"]
    },
    "score": {
      "type": "number",
      "minimum": 0,
      "maximum": 1,
      "description": "Confidence-weighted quality score"
    },
    "confidence": {
      "type": "number",
      "minimum": 0,
      "maximum": 1
    },
    "source": {
      "type": "string",
      "enum": ["runtime", "migration_seed", "human_authored", "eval_result"],
      "default": "runtime"
    },
    "tags": {
      "type": "array",
      "items": { "type": "string" },
      "default": []
    }
  },
  "additionalProperties": false
}
```

- [ ] **Step 2: Commit**

```bash
git add schemas/experience.schema.json
git commit -m "feat: add experiences.jsonl record JSON Schema"
```

### Task 4: Create the skill.md body template

**Files:**
- Create: `schemas/skill-template.md`

- [ ] **Step 1: Write the canonical template**

```markdown
---
# [YAML frontmatter per skill-frontmatter.schema.json]
---

# {name}

{description}

## Purpose

What this skill does and why it exists.

## Use When

- Specific triggers and conditions for activation
- Task types that match this skill

## Do Not Use When

- Conditions where this skill should NOT activate
- Anti-patterns or out-of-scope scenarios

## Inputs

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| input_name | string | yes | What this input is |

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| output_name | string | What this output contains |

## Workflow

1. Step one
2. Step two
3. Step three

## Sub-Skills

- `sub_skill_name` — what it does (if applicable)

## Tooling

- Tool requirements and integrations

## Failure Modes

| Failure | Detection | Recovery |
|---------|-----------|----------|
| failure_type | how to detect | how to recover |

## Recovery Steps

1. Step one for recovery
2. Step two for recovery

## Examples

### Example 1: {scenario}

**Input:** {input}
**Output:** {expected output}

## Notes

Additional context, caveats, or historical notes.
```

- [ ] **Step 2: Commit**

```bash
git add schemas/skill-template.md
git commit -m "feat: add canonical skill.md body template"
```

---

## Chunk 2: XML Parser + AST

### Task 5: Build the XML → AST parser

**Files:**
- Create: `tools/xml_to_ast.py`
- Test: `tools/tests/test_xml_to_ast.py`

- [ ] **Step 1: Write the failing test**

```python
"""Tests for XML → AST parser."""
import json
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from xml_to_ast import parse_xml_skill


def test_parse_extracts_metadata():
    """Parser should extract id, name, version from XML Skill element."""
    xml = '''<?xml version="1.0" encoding="UTF-8"?>
    <Skill skill_id="skill.copy.test.v1_0_0" name="Test Skill" version="1.0.0"
           tier="production" status="active" model="sonnet">
      <Meta>
        <n>Test Skill</n>
        <Description>A test skill for validation.</Description>
        <Owner>supermind</Owner>
        <Tags><Tag>test</Tag><Tag>copy</Tag></Tags>
      </Meta>
    </Skill>'''
    ast = parse_xml_skill(xml)
    assert ast["id"] == "skill.copy.test.v1_0_0"
    assert ast["name"] == "Test Skill"
    assert ast["version"] == "1.0.0"
    assert ast["status"] == "active"
    assert ast["description"] == "A test skill for validation."
    assert ast["tags"] == ["test", "copy"]
    assert ast["owner"] == "supermind"


def test_parse_extracts_inputs_outputs():
    """Parser should extract InputSpec and OutputSpec elements."""
    xml = '''<?xml version="1.0" encoding="UTF-8"?>
    <Skill skill_id="skill.copy.test.v1_0_0" name="Test" version="1.0.0"
           tier="production" status="active" model="sonnet">
      <Meta><n>Test</n><Description>Test</Description><Owner>supermind</Owner>
        <Tags><Tag>test</Tag></Tags></Meta>
      <InputSpec>
        <Input name="sales_page_url" type="string" required="true">The URL to analyze</Input>
        <Input name="brand_brief" type="string" required="false">Optional brand context</Input>
      </InputSpec>
      <OutputSpec>
        <Output name="analysis_report" type="markdown">Full analysis</Output>
      </OutputSpec>
    </Skill>'''
    ast = parse_xml_skill(xml)
    assert len(ast["inputs"]) == 2
    assert ast["inputs"][0]["name"] == "sales_page_url"
    assert ast["inputs"][0]["required"] is True
    assert len(ast["outputs"]) == 1
    assert ast["outputs"][0]["name"] == "analysis_report"


def test_parse_handles_missing_sections_gracefully():
    """Parser should return empty defaults for missing XML sections."""
    xml = '''<?xml version="1.0" encoding="UTF-8"?>
    <Skill skill_id="skill.copy.minimal.v1_0_0" name="Minimal" version="1.0.0"
           tier="draft" status="draft" model="sonnet">
      <Meta><n>Minimal</n><Description>Bare minimum</Description>
        <Owner>supermind</Owner><Tags><Tag>test</Tag></Tags></Meta>
    </Skill>'''
    ast = parse_xml_skill(xml)
    assert ast["inputs"] == []
    assert ast["outputs"] == []
    assert ast["depends_on"] == []
    assert ast["failure_modes"] == []


if __name__ == "__main__":
    test_parse_extracts_metadata()
    test_parse_extracts_inputs_outputs()
    test_parse_handles_missing_sections_gracefully()
    print("All tests passed!")
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd C:\DEV\SUPERMIND && python tools/tests/test_xml_to_ast.py`
Expected: FAIL with "No module named 'xml_to_ast'" or "cannot import name 'parse_xml_skill'"

- [ ] **Step 3: Write the XML → AST parser**

```python
"""XML → AST parser for SkillML XML files.

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
                "name": fm.get("name", fm.find("Name").text if fm.find("Name") is not None else ""),
                "detection": "",
                "recovery": "",
            }
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
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd C:\DEV\SUPERMIND && python tools/tests/test_xml_to_ast.py`
Expected: "All tests passed!"

- [ ] **Step 5: Commit**

```bash
git add tools/xml_to_ast.py tools/tests/test_xml_to_ast.py
git commit -m "feat: XML → AST parser with tests"
```

---

## Chunk 3: AST → skill.md + manifest.json Generators

### Task 6: Build the AST → skill.md renderer

**Files:**
- Create: `tools/ast_to_skill_md.py`
- Test: `tools/tests/test_ast_to_skill_md.py`

- [ ] **Step 1: Write the failing test**

```python
"""Tests for AST → skill.md renderer."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from ast_to_skill_md import render_skill_md


def test_render_produces_valid_frontmatter():
    """Rendered skill.md should have YAML frontmatter with required fields."""
    ast = {
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
    md = render_skill_md(ast)
    assert md.startswith("---\n")
    assert "id: skill.copy.test.v1_0_0" in md
    assert "# Test Skill" in md
    assert "## Purpose" in md
    assert "## Workflow" in md
    assert "| brief |" in md


def test_render_handles_empty_sections():
    """Renderer should produce valid markdown even with empty optional sections."""
    ast = {
        "id": "skill.copy.minimal.v1_0_0",
        "name": "Minimal",
        "version": "1.0.0",
        "status": "draft",
        "owner": "supermind",
        "category": "copy",
        "tags": ["test"],
        "description": "Bare minimum.",
        "inputs": [],
        "outputs": [],
        "depends_on": [],
        "delegates_to": [],
        "complements": [],
        "required_tools": [],
        "memory_reads": [],
        "memory_writes": [],
        "token_budget": "medium",
        "risk_level": "medium",
        "model_preference": "any",
        "purpose": "",
        "use_when": [],
        "do_not_use_when": [],
        "workflow_steps": [],
        "sub_skills": [],
        "failure_modes": [],
        "recovery_steps": [],
        "examples": [],
        "notes": "",
        "tier": "draft",
        "patch_history": [],
        "eval_suite": "",
    }
    md = render_skill_md(ast)
    assert "---\n" in md
    assert "# Minimal" in md


if __name__ == "__main__":
    test_render_produces_valid_frontmatter()
    test_render_handles_empty_sections()
    print("All tests passed!")
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd C:\DEV\SUPERMIND && python tools/tests/test_ast_to_skill_md.py`
Expected: FAIL

- [ ] **Step 3: Write the AST → skill.md renderer**

```python
"""AST → skill.md renderer.

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
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd C:\DEV\SUPERMIND && python tools/tests/test_ast_to_skill_md.py`
Expected: "All tests passed!"

- [ ] **Step 5: Commit**

```bash
git add tools/ast_to_skill_md.py tools/tests/test_ast_to_skill_md.py
git commit -m "feat: AST → skill.md renderer with tests"
```

### Task 7: Build the AST → manifest.json renderer

**Files:**
- Create: `tools/ast_to_manifest.py`
- Test: `tools/tests/test_ast_to_manifest.py`

- [ ] **Step 1: Write the failing test**

```python
"""Tests for AST → manifest.json renderer."""
import json
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from ast_to_manifest import render_manifest


def test_render_produces_valid_json():
    """Rendered manifest should be valid JSON with required fields."""
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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd C:\DEV\SUPERMIND && python tools/tests/test_ast_to_manifest.py`
Expected: FAIL

- [ ] **Step 3: Write the AST → manifest.json renderer**

```python
"""AST → manifest.json renderer.

Renders a normalized AST dictionary into a manifest.json
for machine validation, indexing, and routing.
"""
import json
from datetime import date
from typing import Any


def render_manifest(ast: dict[str, Any], source_xml: str = "") -> str:
    """Render a skill AST into manifest.json format.

    Args:
        ast: Normalized skill dictionary.
        source_xml: Original XML filename for provenance tracking.

    Returns:
        JSON string of the manifest.
    """
    manifest = {
        "id": ast["id"],
        "name": ast["name"],
        "version": ast["version"],
        "status": ast["status"],
        "category": ast.get("category", ""),
        "tags": ast.get("tags", []),
        "description": ast.get("description", ""),
        "relationships": {
            "depends_on": ast.get("depends_on", []),
            "delegates_to": ast.get("delegates_to", []),
            "complements": ast.get("complements", []),
        },
        "tool_requirements": ast.get("required_tools", []),
        "memory_contract": {
            "reads": ast.get("memory_reads", []),
            "writes": ast.get("memory_writes", []),
        },
        "input_schema": [
            {
                "name": i["name"],
                "type": i.get("type", "string"),
                "required": i.get("required", True),
            }
            for i in ast.get("inputs", [])
        ],
        "output_schema": [
            {
                "name": o["name"],
                "type": o.get("type", "string"),
            }
            for o in ast.get("outputs", [])
        ],
        "runtime": {
            "model_preference": ast.get("model_preference", "any"),
            "token_budget": ast.get("token_budget", "medium"),
            "risk_level": ast.get("risk_level", "medium"),
        },
        "eval_suite": ast.get("eval_suite", ""),
        "package": {
            "has_examples": bool(ast.get("examples")),
            "has_evals": False,
            "has_scripts": False,
            "has_sub_skills": bool(ast.get("sub_skills")),
            "has_templates": False,
            "has_experiences": False,
        },
        "provenance": {
            "migrated_from": source_xml,
            "migration_date": date.today().isoformat(),
            "migration_tool": "xskill-migrator",
            "validated": False,
        },
    }

    return json.dumps(manifest, indent=2)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd C:\DEV\SUPERMIND && python tools/tests/test_ast_to_manifest.py`
Expected: "All tests passed!"

- [ ] **Step 5: Commit**

```bash
git add tools/ast_to_manifest.py tools/tests/test_ast_to_manifest.py
git commit -m "feat: AST → manifest.json renderer with tests"
```

---

## Chunk 4: Validators + CLI Migrator

### Task 8: Build the structural validator

**Files:**
- Create: `tools/validate.py`
- Test: `tools/tests/test_validate.py`

- [ ] **Step 1: Write the failing test**

```python
"""Tests for structural validator."""
import json
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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd C:\DEV\SUPERMIND && python tools/tests/test_validate.py`
Expected: FAIL

- [ ] **Step 3: Write the validator**

```python
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
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd C:\DEV\SUPERMIND && python tools/tests/test_validate.py`
Expected: "All tests passed!"

- [ ] **Step 5: Commit**

```bash
git add tools/validate.py tools/tests/test_validate.py
git commit -m "feat: structural validator + drift detector with tests"
```

### Task 9: Build the CLI migrator that ties everything together

**Files:**
- Create: `tools/migrate.py`
- Create: `tools/tests/__init__.py`

- [ ] **Step 1: Write the CLI migrator**

```python
"""XSkill Migration CLI.

Usage:
    python tools/migrate.py <xml_file> <output_dir>
    python tools/migrate.py --batch <xml_dir> <output_dir>

Runs the full pipeline: XML → AST → skill.md + manifest.json → validate
"""
import argparse
import json
import os
import sys
from pathlib import Path

from xml_to_ast import parse_xml_file
from ast_to_skill_md import render_skill_md
from ast_to_manifest import render_manifest
from validate import validate_frontmatter, validate_manifest as validate_mf


def migrate_single(xml_path: str, output_dir: str) -> dict:
    """Migrate a single XML skill file to the XSkill package format.

    Args:
        xml_path: Path to source XML file.
        output_dir: Directory to write the skill package into.

    Returns:
        Result dictionary with status and any errors.
    """
    xml_name = os.path.basename(xml_path)
    print(f"  Parsing: {xml_name}")

    # Step 1: XML → AST
    ast = parse_xml_file(xml_path)

    # Step 2: Derive package directory name from skill id
    skill_name = ast["id"].replace(".", "-") if ast["id"] else Path(xml_path).stem
    pkg_dir = os.path.join(output_dir, skill_name)
    os.makedirs(pkg_dir, exist_ok=True)

    # Step 3: AST → skill.md
    skill_md = render_skill_md(ast)
    skill_md_path = os.path.join(pkg_dir, "skill.md")
    with open(skill_md_path, "w", encoding="utf-8") as f:
        f.write(skill_md)
    print(f"  Wrote: {skill_md_path}")

    # Step 4: AST → manifest.json
    manifest_json = render_manifest(ast, source_xml=xml_name)
    manifest_path = os.path.join(pkg_dir, "manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        f.write(manifest_json)
    print(f"  Wrote: {manifest_path}")

    # Step 5: Create empty experiences.jsonl
    exp_path = os.path.join(pkg_dir, "experiences.jsonl")
    if not os.path.exists(exp_path):
        with open(exp_path, "w", encoding="utf-8") as f:
            pass  # Empty file
        print(f"  Wrote: {exp_path}")

    # Step 6: Create stub directories
    for subdir in ["examples", "evals", "references", "scripts", "sub_skills", "templates"]:
        os.makedirs(os.path.join(pkg_dir, subdir), exist_ok=True)

    # Step 7: Validate
    import yaml
    with open(skill_md_path, "r", encoding="utf-8") as f:
        content = f.read()
    # Extract frontmatter
    parts = content.split("---", 2)
    if len(parts) >= 3:
        fm = yaml.safe_load(parts[1])
    else:
        fm = {}

    manifest = json.loads(manifest_json)

    fm_errors = validate_frontmatter(fm)
    mf_errors = validate_mf(manifest)

    result = {
        "skill_id": ast["id"],
        "xml_source": xml_name,
        "package_dir": pkg_dir,
        "frontmatter_errors": fm_errors,
        "manifest_errors": mf_errors,
        "status": "PASS" if not fm_errors and not mf_errors else "FAIL",
    }

    if fm_errors:
        print(f"  ⚠ Frontmatter errors: {fm_errors}")
    if mf_errors:
        print(f"  ⚠ Manifest errors: {mf_errors}")
    if not fm_errors and not mf_errors:
        print(f"  ✓ Validation passed")

    return result


def migrate_batch(xml_dir: str, output_dir: str):
    """Migrate all XML files in a directory."""
    xml_files = sorted(Path(xml_dir).glob("*.xml"))
    print(f"Found {len(xml_files)} XML files in {xml_dir}\n")

    results = []
    for xml_file in xml_files:
        print(f"[{len(results)+1}/{len(xml_files)}] Migrating {xml_file.name}")
        try:
            result = migrate_single(str(xml_file), output_dir)
            results.append(result)
        except Exception as e:
            print(f"  ✗ ERROR: {e}")
            results.append({"xml_source": xml_file.name, "status": "ERROR", "error": str(e)})
        print()

    # Summary
    passed = sum(1 for r in results if r["status"] == "PASS")
    failed = sum(1 for r in results if r["status"] == "FAIL")
    errors = sum(1 for r in results if r["status"] == "ERROR")
    print(f"Migration complete: {passed} passed, {failed} failed, {errors} errors out of {len(results)} total")

    # Write results
    results_path = os.path.join(output_dir, "migration_report.json")
    with open(results_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print(f"Report: {results_path}")


def main():
    parser = argparse.ArgumentParser(description="XSkill Migration CLI")
    parser.add_argument("source", help="XML file or directory (with --batch)")
    parser.add_argument("output", help="Output directory for skill packages")
    parser.add_argument("--batch", action="store_true", help="Migrate all XMLs in directory")
    args = parser.parse_args()

    if args.batch:
        migrate_batch(args.source, args.output)
    else:
        result = migrate_single(args.source, args.output)
        print(f"\nResult: {result['status']}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Create tests/__init__.py**

```python
# tools/tests/__init__.py
```

- [ ] **Step 3: Test the full pipeline against a real XML from the archive**

Run: `cd C:\DEV\SUPERMIND && python tools/migrate.py "C:\DEV\ULTRAMIND_MASTER\.claude\skills\copy\sales_page_deconstructor_v4_0_0.xml" skills/copy/`
Expected: Creates `skills/copy/skill-copy-sales_page_deconstructor-v4_0_0/` with skill.md, manifest.json, experiences.jsonl

- [ ] **Step 4: Verify the generated files look correct**

Run: `head -30 skills/copy/*/skill.md` and `cat skills/copy/*/manifest.json | python -m json.tool`
Expected: Valid frontmatter, correct fields, parseable JSON

- [ ] **Step 5: Commit**

```bash
git add tools/migrate.py tools/tests/__init__.py
git commit -m "feat: XSkill migration CLI — full XML → AST → skill.md + manifest.json pipeline"
```

### Task 10: Final push

- [ ] **Step 1: Push all work to GitHub**

```bash
cd C:\DEV\SUPERMIND
git push origin main
```

- [ ] **Step 2: Verify on GitHub**

Check https://github.com/chrisflynnai-ux/PAWS — should show all schemas, tools, and tests.

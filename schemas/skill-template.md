---
id: skill.<category>.<name>.v<major>_<minor>_<patch>
name: Skill Name
version: 0.1.0
status: draft
owner: supermind
category: copy
tags: [tag1, tag2]
description: A clear description of what this skill does (10-300 chars).
inputs:
  - input_name
outputs:
  - output_name
depends_on: []
delegates_to: []
complements: []
required_tools: []
memory_reads: []
memory_writes: []
token_budget: medium
risk_level: medium
model_preference: any
eval_suite: ""
---

# Skill Name

A clear description of what this skill does.

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

### Example 1: Scenario Name

**Input:** description
**Output:** expected result

## Notes

Additional context, caveats, or historical notes.

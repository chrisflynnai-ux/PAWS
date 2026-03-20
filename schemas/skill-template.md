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
optional_inputs: []
conditional_inputs: []
outputs:
  - output_name
optional_outputs: []
conditional_outputs: []
depends_on: []
delegates_to: []
complements: []
required_tools: []
memory_reads: []
memory_writes: []
phase_type: executional
maturity_stage: developing
domain_context:
  primary_domain: general
  sub_domain: ""
  market_awareness: general
  industry_patterns: []
  voice_orientation: conversational
token_budget: medium
risk_level: medium
model_preference: any
eval_suite: ""
eval_expectations: {}
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

| Input | Type | Requirement | Description |
|-------|------|-------------|-------------|
| input_name | string | required | What this input is |

## Outputs

| Output | Type | Requirement | Description |
|--------|------|-------------|-------------|
| output_name | string | primary | What this output contains |

## Phase Behavior

- Phase Type: `executional`
- Maturity Stage: `developing`

## Domain Context

- Primary Domain: `general`
- Market Awareness: `general`
- Voice Orientation: `conversational`

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

## Eval Expectations

- base_model_baseline: `0.45`
- skill_only_target: `0.65`
- skill_plus_experience: `0.80`

## Notes

Additional context, caveats, or historical notes.

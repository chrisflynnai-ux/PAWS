---
id: meta_zpwo
name: Zero-Point Workflow Orchestrator
version: 4.0.0
status: active
owner: supermind
category: ''
tags: []
description: "Ultra-lean meta-orchestrator. Routes commands to specialized skills\
  \ via\n      4-track pipeline, manages SSOT state, enforces circuit breakers and\
  \ tiered\n      MMA gates. Does NOT execute content generation \u2014 only coordinates."
inputs: []
outputs: []
depends_on: []
delegates_to: []
complements: []
required_tools: []
memory_reads: []
memory_writes: []
token_budget: medium
risk_level: medium
model_preference: any
eval_suite: ''
---

# Zero-Point Workflow Orchestrator

Ultra-lean meta-orchestrator. Routes commands to specialized skills via
      4-track pipeline, manages SSOT state, enforces circuit breakers and tiered
      MMA gates. Does NOT execute content generation — only coordinates.

## Purpose

TODO: Define the purpose of this skill.

## Use When

- TODO: Define activation triggers

## Do Not Use When

- TODO: Define exclusion conditions

## Inputs

No formal inputs defined.

## Outputs

No formal outputs defined.

## Workflow

1. 1. Read SESSION_STATE.json (python tools/scripts/session_state.py show)
          2. Check current track and pending tasks
          3. Verify SSOT lock integrity (python tools/validate_ssot.py --check-locks)
          4. Check context usage — if > 70%, trigger /gc first
2. 1. Parse incoming command
          2. Resolve skill via alias_resolver (python tools/alias_resolver.py {command})
          3. Look up route in routing_table.yaml
          4. Check prerequisites for target track
          5. Compose team and generate TaskRequest
3. 1. Track fix_counts per MMA dimension
          2. Enforce circuit breaker (max 3 per dimension)
          3. Update SESSION_STATE after each TaskResult
          4. Log SIPs to insights.md
          5. Trigger human gates at track transitions

## Failure Modes

No failure modes documented yet.

## Examples

TODO: Add usage examples.

## Notes

No additional notes.

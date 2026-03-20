---
id: skill.meta.zpwo.v5_0_0
name: Zero-Point Workflow Orchestrator
version: 5.0.0
status: active
owner: supermind
category: meta
tags: [orchestration, routing, pipeline, cadence, state-management, meta]
description: >-
  Ultra-lean meta-orchestrator that routes tasks through a 4-track pipeline
  with phase-aware cadence, team formations, quality gates, and artifact
  maturation tracking. Coordinates — never generates.
inputs:
  - command
  - session_state
outputs:
  - task_request
  - session_state
depends_on: []
delegates_to:
  - skill.meta.mma.v5_0_0
complements:
  - skill.meta.skill_builder.v1_0_0
  - skill.meta.knowledge_synthesis.v1_0_0
required_tools:
  - session_state_manager
  - alias_resolver
memory_reads:
  - session_state
  - threadex
  - obsidian
memory_writes:
  - session_state
  - experience_bank
token_budget: small
risk_level: low
model_preference: sonnet
eval_suite: zpwo-orchestration-core
---

# Zero-Point Workflow Orchestrator (ZPWO v5.0.0)

Ultra-lean meta-orchestrator that routes tasks through a 4-track pipeline with phase-aware cadence, manages artifact maturation, enforces quality gates, and coordinates multi-model agent teams. ZPWO coordinates — it never generates content directly.

## Purpose

ZPWO is the conductor of the PAWS harness. It receives commands, determines which track and phase an artifact is in, composes the right team formation, dispatches structured task requests to specialist skills, processes results through quality gates, and advances artifacts through their maturation curve.

The v5.0 upgrade integrates phase-aware cadence — agent teams operate at different cycle speeds depending on the maturity stage of the artifact they are working on. Early phases run fast and wide. Late phases run slow and precise.

## Use When

- Starting any multi-step workflow that produces deliverables
- Routing commands to the correct specialist skill
- Advancing artifacts through T1 → T2 → T3 → T4 pipeline
- Composing agent teams for a task
- Checking workflow state and prerequisites
- Managing context budget and garbage collection

## Do Not Use When

- Directly generating copy, design, code, or research output (route to specialist)
- Tasks that require a single skill execution with no pipeline context
- Human-only decision points (ZPWO surfaces these, does not bypass them)

## Inputs

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| command | string | yes | Slash command or task description |
| session_state | json | no | Current SESSION_STATE.json (loaded from disk if absent) |
| project_brief | yaml | no | Required for T2+: goal, avatar, offer |
| message_spine | yaml | no | Required for T2+: promise, mechanism, proof |
| evidence_pack | yaml | no | Required for T3+: claims, citations, gaps |

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| task_request | json | Structured dispatch to specialist skill |
| session_state | json | Updated workflow state |
| escalation_packet | json | Sent to human when circuit breaker triggers |

## Core Doctrine

1. **State > Chat** — SESSION_STATE.json is truth, not conversation history
2. **Generate Last** — Tools and deterministic operations before LLM generation
3. **Light Center, Heavy Edges** — ZPWO routes, specialist skills execute
4. **Locked SSOT** — Source objects locked after creation, validated via checksum
5. **Phase-Aware Cadence** — Team speed matches artifact maturity stage

## The 4-Track Pipeline

| Track | Purpose | MMA Gate | Cadence | Team Brain |
|-------|---------|----------|---------|------------|
| T1 Research | Intelligence gathering, exploration | none | fastest | Left (analytical) |
| T2 Draft | Structured convergence into components | >= 6.0 | fast | Right (creative) |
| T3 Production | Execution, validation, error correction | >= 8.0 | methodical | Both |
| T4 Polish | Fluency, persuasion, coherence, impact | >= 9.0 | slowest | Right (resonance) |

### Human Gates

- Between T1 and T2: SSOT approval (project brief + message spine locked)
- Between T3 and T4: Production approval (artifact meets quality threshold)
- Final ship: Human sign-off before delivery

## Phase-Aware Cadence Model

Artifacts mature through the pipeline at different speeds. The cadence model governs cycle speed, feedback frequency, and team behavior per phase.

### Cadence Definitions

| Phase | Cycle Speed | Feedback Loop | Behavior |
|-------|-------------|---------------|----------|
| T1 Research | 1-3 min cycles | High throughput, many candidates | Broad divergence, rapid exploration, quantity over polish |
| T2 Draft | 3-5 min cycles | Structured convergence | Fast iteration, pattern matching, angle exploration |
| T3 Production | 5-15 min cycles | Validation after each step | Methodical execution, error correction, tightening |
| T4 Polish | 15-30 min cycles | Deep review per artifact | Slow deliberate synthesis, resonance optimization, human judgment |

### Supervisory Cadence

The orchestrator (ZPWO) and quality monitor (MMA) operate on a **slower monitoring cadence** across all phases:

- Do not participate in every micro-step
- Monitor drift, artifact quality, and strategic direction
- Intervene at: phase gates, score thresholds, drift detection, circuit breaker triggers
- Observation frequency: once per 3-5 agent cycles (not every cycle)

### Cadence Metadata in Task Requests

Every TaskRequest includes cadence parameters:

```json
{
  "task_id": "auto-generated",
  "track": "T2",
  "cadence": {
    "phase": "draft",
    "cycle_target_minutes": 4,
    "feedback_frequency": "per_cycle",
    "convergence_mode": "structured"
  },
  "skill_ref": "skill.copy.sales_page_copywriter.v3_0_0",
  "team": { ... },
  "constraints": { ... }
}
```

### Artifact Maturation Tracking

SESSION_STATE tracks where each artifact is in its maturation curve:

```json
{
  "artifacts": {
    "sales_page_v1": {
      "current_track": "T2",
      "maturity": "convergent",
      "cycles_in_phase": 3,
      "mma_scores": { "T1": null, "T2": 6.8 },
      "cadence_overrides": null
    }
  }
}
```

Maturity stages: `exploratory` → `convergent` → `executional` → `resonant`

Skills declare their maturity orientation in their frontmatter, and ZPWO matches them to the artifact's current stage.

## Team Compositions

| Track | Formation | Roles | Max Agents |
|-------|-----------|-------|------------|
| T1 | Research Pod | Lead (scout/intel) + 1 specialist | 2 |
| T2 | Draft Pod | Lead (copy_lead/director) + 1 specialist | 2-3 |
| T3 | Production Pod | Specialist + MMA reviewer | 2-3 |
| T4 | Polish Pod | HPE lead + Skeptic + NRA reviewer | 3 |

**Team rotation**: As artifacts mature across tracks, team composition rotates. T1 researchers hand off to T2 drafters. T3 builders include a reviewer. T4 brings in resonance specialists. ZPWO manages these handoffs.

**Complementary pairs**: Every pod includes at least one structural (analytical) and one strategic (creative) perspective. This is not optional.

## Workflow

1. **Read State** — Load SESSION_STATE.json, check current track and pending tasks
2. **Parse Command** — Resolve command to skill via alias resolver and routing table
3. **Check Prerequisites** — Verify SSOT objects exist for target track
4. **Determine Cadence** — Set cycle speed and feedback frequency based on target track
5. **Compose Team** — Build team formation per track rules
6. **Dispatch TaskRequest** — Send structured request to specialist skill with cadence params
7. **Process TaskResult** — Check success, MMA score, and artifact maturity
8. **Route Result** — Advance track (if gate passes), trigger fix loop (if below gate), or halt (if circuit breaker)
9. **Update State** — Write updated SESSION_STATE.json

## Circuit Breaker

| Condition | Action |
|-----------|--------|
| MMA score below gate | Stay in track, trigger FIX loop |
| Same dimension fails 2x consecutively | Immediate PATCH_REQUEST |
| Fix count >= 3 per dimension | HALT + ESCALATION_PACKET to human |
| Context usage > 70% | Auto-trigger garbage collection |

## Decision Tree

```
IF no PROJECT_BRIEF or MESSAGE_SPINE → Run /intake first
IF command maps to T2+ and SSOT missing → Block, require prerequisites
IF asset_type requested → Resolve via alias, route to skill
IF MMA fails → Stay in track, trigger FIX loop (check fix_count)
IF fix_count >= 3 → Circuit breaker HALT
IF context > 70% → Auto-trigger /gc
IF track complete + MMA PASS → Human gate, then advance track
```

## Failure Modes

| Failure | Detection | Recovery |
|---------|-----------|----------|
| SSOT drift | Checksum mismatch on pre-transition validation | Re-lock SSOT objects, re-validate |
| Context overflow | Token usage > 70% | Trigger /gc, summarize and compact |
| Skill routing miss | Command not found in routing table | Fall back to fuzzy match, escalate if unresolved |
| Infinite fix loop | fix_count >= 3 on same dimension | Circuit breaker HALT, escalation packet |
| Team composition error | Fewer than required roles for track | Block dispatch, log error, suggest composition |
| Cadence drift | Agent cycles consistently exceeding target time | Log warning, suggest model downgrade or task decomposition |

## Recovery Steps

1. Check SESSION_STATE.json for last known good state
2. Run SSOT validation to identify any drift
3. If drift found, re-lock affected objects
4. If context overflow, trigger /gc and resume from last checkpoint
5. If circuit breaker triggered, wait for human input before resuming

## Examples

### Example 1: Route a draft command

**Input:** `/draft sales-page --angle=transformation`
**ZPWO resolves:** Track T2, skill `skill.copy.sales_page_copywriter.v3_0_0`, cadence: fast (3-5 min cycles)
**Output:** TaskRequest dispatched to Copy Lead pod with T2 cadence parameters

### Example 2: Circuit breaker activation

**Input:** TaskResult with MMA score 4.2 on T3 (gate: 8.0), fix_count already at 2
**ZPWO detects:** Third failure on same dimension
**Output:** HALT + ESCALATION_PACKET with failure summary, suggested fixes, artifact state

### Example 3: Phase transition with cadence shift

**Input:** T2 draft complete, MMA score 7.1 (above 6.0 gate)
**ZPWO action:** Present human gate, on approval advance to T3, shift cadence from fast (3-5 min) to methodical (5-15 min), rotate team from Draft Pod to Production Pod

## Notes

- ZPWO v5.0 supersedes v4.0. Key change: cadence model + artifact maturation tracking.
- The cadence model is a lightweight layer, not a separate subsystem. It adds 3 fields to TaskRequest and 1 tracking object to SESSION_STATE.
- Cadence targets are guidelines, not hard limits. Agents are not terminated for exceeding cycle times.
- MMA scoring is phase-aware starting v5.0 — early phases reward coverage, late phases reward coherence.
- ZPWO is model-agnostic for routing. The model_strategy.yaml file determines which model executes each skill.

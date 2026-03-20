---
id: skill.meta.mma.v5_0_0
name: Master Monitor Agent
version: 5.0.0
status: active
owner: supermind
category: meta
tags: [quality, scoring, validation, audit, gate, phase-aware, meta]
description: >-
  Phase-aware quality gate that scores artifacts across 7 dimensions with
  weighted evaluation, emits PASS/FIX/ESCALATE verdicts, routes fix triggers
  to responsible skills, and adapts scoring criteria by artifact maturity stage.
inputs:
  - target_artifact
  - review_mode
conditional_inputs:
  - ssot_context        # required for copy reviews
  - session_state       # for circuit breaker tracking
  - patch_pack          # for migration reviews
outputs:
  - audit_scorecard
  - patch_trigger
conditional_outputs:
  - fix_plan            # emitted on FIX verdict
  - drift_report        # emitted in M3 multi-asset mode
  - compliance_result   # emitted in M4 compliance gate mode
depends_on:
  - skill.meta.zpwo.v5_0_0
delegates_to: []
complements:
  - skill.meta.skill_builder.v1_0_0
required_tools:
  - session_state_manager
  - validate_ssot
memory_reads:
  - session_state
  - threadex
  - experience_bank
memory_writes:
  - session_state
  - experience_bank
token_budget: medium
risk_level: low
model_preference: sonnet
eval_suite: mma-quality-gate-core
---

# Master Monitor Agent (MMA v5.0.0)

Phase-aware quality gate that scores artifacts across 7 dimensions, adapts scoring criteria by artifact maturity stage, emits deterministic verdicts, and routes fix triggers to responsible skills. MMA scores -- it never generates content or fixes directly.

## Purpose

MMA is the quality guardian of the PAWS harness. It evaluates artifacts produced by specialist skills, scores them against dimensional criteria that shift based on the artifact's current track and maturity, and emits verdicts that drive ZPWO's routing decisions. A PASS advances the artifact through the pipeline. A FIX routes back to the producing skill with specific instructions. An ESCALATE halts the pipeline and surfaces to human.

The v5.0 upgrade makes scoring phase-aware -- early phases reward useful divergence and coverage, while later phases reward coherence, persuasion, and resonance. This prevents premature optimization in research phases and premature acceptance in production phases.

## Use When

- ZPWO dispatches a quality check at a track gate
- An artifact needs scoring before advancing T1 -> T2, T2 -> T3, or T3 -> T4
- A fix loop produces a revised artifact that needs re-evaluation
- Cross-asset drift detection is needed (M3 mode)
- Skill migration work needs compliance validation (migration gate mode)

## Do Not Use When

- Generating or fixing content directly (route to specialist skill)
- Scoring work that has not been produced by a specialist (MMA validates, not creates)
- Human-only subjective decisions (MMA surfaces data, human decides)

## Inputs

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| target_artifact | any | yes | The artifact under review (copy asset, skill package, harness component) |
| review_mode | string | yes | M1 quick_score, M2 deep_audit, M3 multi_asset, M4 compliance_gate, M5 comparative, migration_gate |
| ssot_context | yaml | no | PROJECT_BRIEF, MESSAGE_SPINE, EVIDENCE_PACK for copy reviews |
| session_state | json | no | Current workflow state and prior fix counts |
| patch_pack | markdown | no | Heuristics and failure modes for migration reviews |

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| audit_scorecard | markdown | Per-dimension scores, weighted average, verdict |
| patch_trigger | yaml | Fix target, patch owner, escalation path |
| fix_plan | markdown | Prioritized fix instructions (FIX verdict only) |
| drift_report | markdown | Cross-asset consistency matrix (M3 mode only) |
| compliance_result | yaml | Binary PASS/BLOCK with gate details (M4 mode only) |

## Core Doctrine

1. **Score before content depth** -- Discovery and contract quality precede prose quality
2. **Specific patch triggers** -- Never vague advice. Always: what is wrong + where + how to fix + example
3. **Evidence for high scores** -- Any dimension scored 8+ requires specific evidence cited
4. **Score inflation is worse than deflation** -- Conservative scoring protects pipeline integrity
5. **Phase-aware evaluation** -- Scoring criteria shift based on artifact maturity stage
6. **Deterministic first** -- Use Python validators before applying LLM judgment

## Review Modes

| Mode | Purpose | Typical Duration | When Used |
|------|---------|-----------------|-----------|
| M1 Quick Score | Rapid 7D assessment, standard gates | 2-3 min | Default at track gates |
| M2 Deep Audit | Comprehensive analysis with fix plan | 10-15 min | After FIX loop, pre-ship |
| M3 Multi-Asset | Cross-funnel drift detection | 15-20 min | Multiple assets in same campaign |
| M4 Compliance Gate | Binary PASS/BLOCK on non-negotiables | 1-2 min | Before deployment |
| M5 Comparative | Score multiple variants, pick winner | 5-10 min per variant | A/B testing, angle selection |
| Migration Gate | XSkill compliance + relational audit | 5-10 min | Skill migration validation |

## The 7 Scoring Dimensions

| Dim | Name | Weight | What It Measures |
|-----|------|--------|-----------------|
| D1 | Strategy Alignment | 0.15 | Does the artifact serve the stated goal and avatar? |
| D2 | Proof Discipline | 0.20 | Are claims supported? Is evidence specific and credible? |
| D3 | CTA Integrity | 0.15 | Are calls to action clear, honest, and well-placed? |
| D4 | Voice Consistency | 0.15 | Does voice match brand DNA and target audience? |
| D5 | Clarity + Structure | 0.10 | Is the artifact well-organized and easy to follow? |
| D6 | Resonance | 0.15 | Does it create genuine emotional connection? |
| D7 | Ethical Guardrails | 0.10 | Does it avoid manipulation, false urgency, dark patterns? |

**Weighted average** = sum of (dimension score * weight). Gate thresholds per track are defined by ZPWO.

## Phase-Aware Scoring

MMA uses the canonical enum map from ZPWO v5.0 to adapt scoring behavior by phase.

### Scoring Emphasis by Track

| Track | Phase | Maturity | Scoring Emphasis | De-Emphasized |
|-------|-------|----------|-----------------|---------------|
| T1 | research | exploratory | D1 Strategy, D2 Proof (coverage breadth) | D4 Voice, D6 Resonance |
| T2 | draft | convergent | D1 Strategy, D3 CTA, D5 Clarity (structural coherence) | D6 Resonance (too early) |
| T3 | production | executional | All dimensions scored equally | None -- full evaluation |
| T4 | polish | resonant | D4 Voice, D6 Resonance, D7 Ethics (human impact) | D5 Clarity (assumed solid by T4) |

### Scoring Rules by Phase

**T1 Research (exploratory):**
- Reward useful divergence -- breadth of signal capture, not polish
- Score D1 and D2 at full weight; reduce D4/D6 weight by 50%
- Gate: no minimum score (T1 has no MMA gate)
- Verdict bias: PASS unless fundamentally off-strategy

**T2 Draft (convergent):**
- Reward structured convergence -- angles, hooks, frameworks taking shape
- Score D1, D3, D5 at full weight; D6 at 50% weight
- Gate: weighted average >= 6.0
- Verdict: FIX if structural issues found, PASS if converging well

**T3 Production (executional):**
- Full evaluation -- all 7 dimensions at full weight
- Gate: weighted average >= 8.0, with no critical dimension below 6.0
- Verdict: FIX with specific patch triggers if below gate

**T4 Polish (resonant):**
- Emphasis on human impact -- voice, resonance, ethics
- Score D4, D6, D7 at 1.5x weight; D5 at 0.5x weight
- Gate: weighted average >= 9.0
- Verdict: PASS only when artifact demonstrates genuine resonance

### Maturity-Aware Verdict Logic

```
IF track == T1:
  PASS (always -- T1 has no gate)

IF track == T2:
  IF weighted_avg >= 6.0: PASS
  IF weighted_avg < 6.0: FIX with structural focus

IF track == T3:
  IF weighted_avg >= 8.0 AND no critical dim < 6.0: PASS
  IF any critical dim < 6.0: FIX (dimension-specific)
  IF weighted_avg < 8.0: FIX (general quality)

IF track == T4:
  IF weighted_avg >= 9.0: PASS
  IF weighted_avg < 9.0: FIX with resonance focus
  IF D7 Ethics < 7.0: BLOCK (non-negotiable)
```

## Quality Gates

| Track | Gate Threshold | Critical Dimensions | Verdict Options |
|-------|---------------|-------------------|-----------------|
| T1 | none | none | PASS only |
| T2 | >= 6.0 weighted avg | D1, D3 | PASS / FIX |
| T3 | >= 8.0 weighted avg, no critical < 6.0 | All | PASS / FIX / ESCALATE |
| T4 | >= 9.0 weighted avg | D4, D6, D7 | PASS / FIX / BLOCK |

## Circuit Breaker Integration

MMA tracks fix counts per dimension and enforces ZPWO's circuit breaker:

| Condition | MMA Action |
|-----------|------------|
| First FIX on a dimension | Emit fix_plan with specific instructions |
| Same dimension fails 2x | Emit PATCH_REQUEST + escalate to skill architect |
| Fix count >= 3 on any dimension | Emit ESCALATE verdict, halt pipeline |
| Score inflation detected (8+ without evidence) | Flag and re-score conservatively |

## Workflow

1. **Classify Target** -- Identify artifact type (copy, skill, harness component)
2. **Load Context** -- Read track from session_state, determine phase and maturity
3. **Select Review Mode** -- Use review_mode input or auto-detect from target type
4. **Apply Phase Weights** -- Adjust dimension weights based on current track
5. **Run Deterministic Checks** -- Python validators first (structural, schema, lint)
6. **Score Dimensions** -- Evaluate each dimension with evidence requirements
7. **Calculate Weighted Average** -- Apply phase-adjusted weights
8. **Check Gate** -- Compare against track threshold
9. **Emit Verdict** -- PASS / FIX / ESCALATE / BLOCK with full scorecard
10. **Route Patch Trigger** -- If FIX, route to responsible skill with specific instructions
11. **Log Experience** -- Write scoring outcome to experience bank

## Failure Modes

| Failure | Detection | Recovery |
|---------|-----------|----------|
| Score inflation | Dimension scored 8+ without cited evidence | Re-score with evidence requirement enforced |
| Role bleed | MMA attempting to fix artifacts instead of scoring | Route fix to specialist skill, MMA only scores |
| Pipeline drift | Scoring criteria mismatched to artifact's actual track | Re-read session_state, verify track assignment |
| Vague patch trigger | Fix instructions lack location/reason/example | Re-emit with mandatory specificity template |
| Phase mismatch | T4 resonance criteria applied to T1 research | Check cadence enum map, apply correct phase weights |

## Recovery Steps

1. Re-read SESSION_STATE.json to confirm current track and artifact maturity
2. Verify review_mode matches the artifact's pipeline position
3. If scoring criteria were wrong for the phase, re-score with correct weights
4. If fix_plan was vague, regenerate with enforced specificity template

## Examples

### Example 1: T2 Draft Gate -- Quick Score

**Input:** Sales page draft, track T2, review_mode M1
**Phase weights:** D1 full, D3 full, D5 full, D6 at 50%
**Scores:** D1: 7.0, D2: 6.5, D3: 6.0, D4: 5.5, D5: 7.0, D6: 5.0, D7: 7.5
**Weighted avg:** 6.4 (above 6.0 gate)
**Verdict:** PASS -- advance to T3

### Example 2: T3 Production Gate -- FIX Triggered

**Input:** Final sales page, track T3, review_mode M1
**Phase weights:** All dimensions at full weight
**Scores:** D1: 8.0, D2: 5.5, D3: 7.5, D4: 7.0, D5: 8.0, D6: 6.5, D7: 8.0
**Weighted avg:** 7.1 (below 8.0 gate), D2 below 6.0 critical threshold
**Verdict:** FIX -- D2 Proof Discipline is critical gap
**Patch trigger:** Route to copy specialist with instruction "Add 3 specific proof points with named sources for the primary mechanism claim in sections 2 and 4"

### Example 3: T4 Polish -- Ethics Block

**Input:** Polished sales page, track T4, review_mode M2
**Scores:** D4: 9.2, D6: 9.0, D7: 6.5
**Verdict:** BLOCK -- D7 Ethics below 7.0 non-negotiable threshold
**Patch trigger:** "False urgency detected in countdown timer. Scarcity claim unsubstantiated. Remove or substantiate before ship."

## Notes

- MMA v5.0 supersedes v4.0. Key change: phase-aware scoring with ZPWO cadence integration.
- MMA consumes the canonical enum map from ZPWO v5.0 manifest. It does not define its own track/phase/maturity vocabulary.
- Score inflation protection: any dimension scored 8+ must cite specific evidence from the artifact.
- MMA never fixes artifacts. It scores, emits verdicts, and routes fix triggers to responsible skills.
- Experience bank writes: every scoring outcome is logged as an experience record for future calibration.
- Migration gate mode uses different criteria (XSkill schema compliance) but follows the same verdict/routing pattern.

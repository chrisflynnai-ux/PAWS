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
optional_inputs:
  - review_mode           # auto-detected from target type if omitted
conditional_inputs:
  - ssot_context        # required for copy reviews
  - session_state       # for circuit breaker tracking
  - patch_pack          # for migration reviews
outputs:
  - audit_scorecard
conditional_outputs:
  - patch_trigger       # emitted on FIX/ESCALATE/BLOCK verdict only
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
| review_mode | string | no | M1 quick_score, M2 deep_audit, M3 multi_asset, M4 compliance_gate, M5 comparative, migration_gate. Auto-detected from target type if omitted. |
| ssot_context | yaml | no | PROJECT_BRIEF, MESSAGE_SPINE, EVIDENCE_PACK for copy reviews |
| session_state | json | no | Current workflow state and prior fix counts |
| patch_pack | markdown | no | Heuristics and failure modes for migration reviews |

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| audit_scorecard | markdown | Per-dimension scores, normalized weighted average, verdict. Always emitted. |
| patch_trigger | yaml | Fix target, patch owner, escalation path. Emitted on FIX/ESCALATE/BLOCK only. |
| fix_plan | markdown | Prioritized fix instructions. Emitted on FIX verdict only. |
| drift_report | markdown | Cross-asset consistency matrix. Emitted in M3 mode only. |
| compliance_result | yaml | Binary PASS/BLOCK with gate details. Emitted in M4 mode only. |

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

**Normalized weighted average:** After applying phase adjustments, MMA renormalizes all adjusted weights back to sum 1.0 before computing the weighted average. This ensures gate thresholds mean the same thing across all phases.

```
adjusted_weights = apply_phase_multipliers(base_weights, current_track)
normalized_weights = {dim: w / sum(adjusted_weights.values()) for dim, w in adjusted_weights.items()}
weighted_avg = sum(score[dim] * normalized_weights[dim] for dim in dimensions)
```

**Gate thresholds are single-homed in ZPWO v5.0.** MMA reads them from ZPWO's manifest at runtime. MMA does not define or restate gate thresholds -- it only applies them. If ZPWO changes a threshold, MMA inherits the change automatically.

## Phase-Aware Scoring

MMA uses the canonical enum map from ZPWO v5.0 to adapt scoring behavior by phase.

### Phase Weight Multipliers (Pre-Renormalization)

| Track | Phase | Maturity | Multiplier Adjustments | Scoring Emphasis |
|-------|-------|----------|----------------------|-----------------|
| T1 | research | exploratory | D4: 0.5x, D6: 0.5x | Divergence and coverage breadth |
| T2 | draft | convergent | D6: 0.5x | Structural coherence |
| T3 | production | executional | (none -- all at 1.0x) | Full balanced evaluation |
| T4 | polish | resonant | D4: 1.5x, D6: 1.5x, D7: 1.5x, D5: 0.5x | Human impact and resonance |

After multipliers are applied, **all weights are renormalized to sum 1.0** before scoring. This prevents phase adjustments from inflating or deflating the total weight mass.

### Scoring Rules by Phase

**T1 Research (exploratory):**
- Reward useful divergence -- breadth of signal capture, not polish
- D4/D6 de-emphasized via 0.5x multiplier (renormalized)
- Gate: read from ZPWO (currently: none)
- Verdict: PASS unless fundamentally off-strategy

**T2 Draft (convergent):**
- Reward structured convergence -- angles, hooks, frameworks taking shape
- D6 de-emphasized via 0.5x multiplier (renormalized)
- Gate: read from ZPWO (currently: normalized weighted avg >= 6.0)
- Verdict: FIX if structural issues found, PASS if converging well

**T3 Production (executional):**
- Full evaluation -- all 7 dimensions at base weight (no multipliers)
- Gate: read from ZPWO (currently: normalized weighted avg >= 8.0, no critical dim < 6.0)
- Verdict: FIX with specific patch triggers if below gate

**T4 Polish (resonant):**
- Emphasis on human impact -- voice, resonance, ethics boosted
- D4/D6/D7 emphasized via 1.5x, D5 de-emphasized via 0.5x (renormalized)
- Gate: read from ZPWO (currently: normalized weighted avg >= 9.0)
- Verdict: PASS only when artifact demonstrates genuine resonance

### Verdict Logic

MMA emits exactly one verdict per evaluation. Verdicts are:

- **PASS** -- artifact meets or exceeds the gate threshold for its current track
- **FIX** -- artifact is below gate; patch_trigger emitted with specific instructions
- **BLOCK** -- non-negotiable threshold violated (e.g., D7 Ethics floor in T4); artifact cannot advance regardless of other scores

**ESCALATE** is not a direct scoring verdict. It is triggered only by the circuit breaker when fix loops are exhausted (see Circuit Breaker Integration below). This distinction matters: MMA scoring produces PASS/FIX/BLOCK. The circuit breaker produces ESCALATE.

```
1. Read gate thresholds from ZPWO manifest for current track
2. Apply phase weight multipliers
3. Renormalize weights to sum 1.0
4. Compute normalized weighted average
5. Check non-negotiable floors (D7 >= 7.0 in T4)
6. IF floor violated: BLOCK
7. ELIF weighted_avg >= gate_threshold AND no critical dim below floor: PASS
8. ELSE: FIX (emit patch_trigger with dimension-specific instructions)
```

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
3. **Select Review Mode** -- Use review_mode input if provided; otherwise auto-detect from target type (copy asset -> M1, skill package -> migration_gate, etc.)
4. **Apply Phase Weights** -- Apply multipliers for current track, then renormalize to sum 1.0
5. **Run Deterministic Checks** -- Python validators first (structural, schema, lint)
6. **Score Dimensions** -- Evaluate each dimension with evidence requirements
7. **Calculate Normalized Weighted Average** -- Renormalize adjusted weights to sum 1.0, then compute
8. **Check Gate** -- Read track threshold from ZPWO manifest, compare normalized score
9. **Emit Verdict** -- PASS / FIX / BLOCK with full scorecard (ESCALATE is circuit-breaker only)
10. **Route Patch Trigger** -- If FIX or BLOCK, route to responsible skill with specific instructions
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

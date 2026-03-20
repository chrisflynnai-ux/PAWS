---
id: skill.meta.knowledge_synthesis.v1_0_0
name: Knowledge Synthesis Pipeline
version: 1.0.0
status: active
owner: supermind
category: meta
tags: [meta, knowledge, extraction, synthesis, atoms, filtering, experience-bank]
description: >-
  Extracts candidate atoms from raw source materials, classifies them into
  skills, experiences, scripts, patterns, failures, or references, filters
  aggressively before admission, ranks by usefulness and novelty, and only
  promotes validated atoms into the Superskills system. The refinery that
  turns raw knowledge into compounding intelligence.
inputs:
  - source_material
  - synthesis_mode
  - target_domain
conditional_inputs:
  - existing_skill_registry
  - domain_context
  - quality_threshold
outputs:
  - candidate_atoms
  - synthesis_report
  - rejection_log
conditional_outputs:
  - admission_proposals    # proposed insertions for Skill Builder to apply under validation
  - skill_seeds            # delegated to Skill Builder for package creation
  - script_candidates      # proposed xScripts for Skill Builder to integrate
depends_on:
  - skill.meta.zpwo.v5_0_0
  - skill.meta.mma.v5_0_0
delegates_to:
  - skill.meta.skill_builder.v1_0_0
complements: []
required_tools:
  - validate
memory_reads:
  - threadex
  - experience_bank
  - obsidian
memory_writes:
  - threadex              # graph edges for new knowledge relationships only
  # NOTE: Knowledge Synthesis does NOT write directly to experience banks or skill packages.
  # It emits admission_proposals that Skill Builder applies under validation.
token_budget: large
risk_level: medium
model_preference: sonnet
eval_suite: knowledge-synthesis-core
---

# Knowledge Synthesis Pipeline (v1.0.0)

The refinery that turns raw knowledge into compounding intelligence. Extracts candidate atoms from source materials, classifies them, filters aggressively, ranks by usefulness, and only promotes validated atoms into the Superskills system. External knowledge is treated as candidate intelligence, never trusted doctrine.

## Purpose

Knowledge Synthesis is the intake pipeline for the PAWS system. Raw sources come in (documents, transcripts, competitor analyses, training materials, research outputs). Structured atoms come out. The pipeline ensures that only material which improves actual agent performance enters the system -- everything else is logged and rejected.

This is not a knowledge dump. It is a knowledge refinery with strict admission criteria.

## Use When

- Ingesting new source material (docs, transcripts, frameworks, competitor pages)
- Extracting reusable patterns from completed work sessions
- Processing NotebookLM query results into structured atoms
- Evaluating external skill libraries for potential adoption
- Populating experience banks from runtime observations
- Upgrading existing skills with newly discovered patterns

## Do Not Use When

- Building a new skill from scratch (use Skill Builder)
- Scoring an existing artifact (use MMA)
- Routing a task at runtime (use ZPWO)
- Material is already in canonical XSkill format (already processed)

## Inputs

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| source_material | any | yes | Raw source: docs, transcripts, XMLs, web extracts, session logs |
| synthesis_mode | string | yes | extract, evaluate, import, enrich, audit |
| target_domain | string | yes | Domain family: copy, research, design, ads, email, etc. |
| existing_skill_registry | json | no | For novelty detection and redundancy filtering |
| domain_context | markdown | no | Domain-specific framing for relevance scoring |
| quality_threshold | float | no | Minimum score for atom admission (default: 0.7) |

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| candidate_atoms | list | Classified atoms with scores and recommendations |
| synthesis_report | markdown | Extraction stats, admission/rejection counts, recommendations |
| admission_proposals | jsonl | Proposed insertions (experiences, patterns, failures, references) for Skill Builder to apply under package validation. KS does NOT write directly to skill packages. |
| skill_seeds | list | Patterns substantial enough to become new skills. Delegated to Skill Builder for package creation. MMA scores the built package, not the raw seed. |
| script_candidates | list | Deterministic procedures proposed for xScript extraction. Skill Builder integrates them. |
| rejection_log | jsonl | Rejected atoms with reasons (for audit and learning) |

## Synthesis Modes

| Mode | Purpose | Input Type | Output Focus |
|------|---------|-----------|--------------|
| extract | Pull atoms from raw source material | docs, transcripts | candidate_atoms |
| evaluate | Score external skills/patterns for potential adoption | external skill files | admission_decision |
| import | Bring validated atoms into the system | pre-scored candidates | experience_records, skill_seeds |
| enrich | Add new patterns to existing skills | runtime observations | experience_records |
| audit | Review existing atoms for decay, redundancy, or upgrade | existing experience bank | synthesis_report |

## Atom Classification

Every extracted fragment is classified into exactly one type:

| Atom Type | Description | Destination |
|-----------|-------------|-------------|
| **skill_seed** | Procedural pattern substantial enough to become a skill | Delegates to Skill Builder |
| **experience** | Tactical insight about when/why/how something works | experiences.jsonl |
| **script** | Deterministic operation that should be code, not prose | scripts/ directory |
| **pattern** | Reusable structural template (hook, framework, sequence) | references/ or sub_skills/ |
| **failure** | Documented failure mode with detection and recovery | Failure Modes section of relevant skill |
| **reference** | Contextual information useful but not procedural | references/ directory |

## The Admission Gate

**Core doctrine: nothing enters the system without passing the admission gate.**

### Admission Criteria

| Criterion | Weight | Threshold | Description |
|-----------|--------|-----------|-------------|
| Usefulness | 0.30 | >= 0.6 | Does this improve agent performance on real tasks? |
| Novelty | 0.25 | >= 0.4 | Is this genuinely new vs what we already have? |
| Coherence | 0.20 | >= 0.5 | Does this fit cleanly into our existing architecture? |
| Domain Fit | 0.15 | >= 0.5 | Is this relevant to the target domain? |
| Token Efficiency | 0.10 | >= 0.3 | Is the value-per-token ratio acceptable? |

**Weighted admission score** = sum of (criterion score * weight)

**Admission threshold:** >= 0.7 (configurable via quality_threshold input)

### Admission Decisions

| Score | Decision | Action |
|-------|----------|--------|
| >= 0.85 | **Admit: Priority** | Fast-track into system, flag for immediate integration |
| >= 0.70 | **Admit: Standard** | Add to system with normal validation |
| >= 0.50 | **Hold: Review** | Flag for human review before admission |
| < 0.50 | **Reject** | Log rejection reason, do not admit |

## Workflow

### Phase 1: Source Intake

1. Classify source type (document, transcript, XML, web extract, session log, external skill)
2. Estimate source quality and relevance to target domain
3. If external skill: flag as candidate intelligence, not trusted doctrine
4. Segment source into extractable chunks

### Phase 2: Atomic Extraction

5. Extract candidate atoms from each chunk
6. Classify each atom (skill_seed, experience, script, pattern, failure, reference)
7. De-duplicate against each other within the batch
8. Attach provenance metadata (source, extraction date, extractor model)

### Phase 3: Scoring and Filtering

9. Score each atom on 5 admission criteria
10. Calculate weighted admission score
11. Apply admission threshold
12. For atoms below threshold: log to rejection_log with specific reason
13. For atoms above threshold: proceed to Phase 4
14. If existing_skill_registry provided: run novelty check against existing atoms

### Phase 4: Proposal Emission (Not Direct Write)

**Critical boundary: Knowledge Synthesis discovers and recommends. It does NOT write directly into existing skill packages.** Direct writes would bypass Skill Builder's package integrity layer and create skill.md/manifest.json drift.

15. Delegate skill_seeds to Skill Builder via delegates_to (Skill Builder creates the package, then MMA scores the built result)
16. Emit admission_proposals for experiences, patterns, failures, and references as structured proposals
17. Each proposal specifies: target_skill_id, atom_type, proposed_content, insertion_location, admission_score
18. Skill Builder (or a future package mutator) applies proposals under validation, ensuring manifest stays in sync
19. Write synthesis_report with extraction stats, admission/rejection counts, and proposal summary

### Phase 5: Validation

20. For admission_proposals: validate proposed content against experience.schema.json (experiences) or structural rules (patterns, failures, references)
21. For skill_seeds: validate they have enough substance for Skill Builder (minimum: clear inputs, outputs, and at least 3 workflow steps)
22. For script_candidates: verify they are actually deterministic (no LLM judgment required)
23. NOTE: MMA does NOT score raw seeds or proposals. MMA scores built packages after Skill Builder produces them. The flow is: KS extracts -> SB builds -> MMA scores.

## Novelty Detection

When existing_skill_registry is provided, every candidate atom is checked for novelty:

| Signal | Classification | Action |
|--------|---------------|--------|
| No similar atom exists in system | **Novel** | Full admission scoring |
| Similar atom exists but candidate is higher quality | **Upgrade** | Replace existing with candidate |
| Similar atom exists at equal quality | **Redundant** | Reject with "already covered" reason |
| Candidate contradicts existing validated atom | **Conflict** | Flag for human review |

## External Skill Evaluation

When synthesis_mode is evaluate and source is an external skill library:

1. Parse external skill into atoms
2. Score each atom against admission criteria
3. Compare against existing skills for overlap
4. Run control eval: base model alone vs base model + external atom
5. Only admit atoms that demonstrate measurable improvement
6. Log all rejected atoms with reasons for future reference

**Doctrine: external skills are candidates, not imports. They earn their way in.**

## Experience Bank Integration

Admitted experience records follow this flow:

```
Raw observation -> Atomic extraction -> Classification -> Scoring ->
Admission gate -> Schema validation -> admission_proposal emitted ->
Skill Builder applies proposal under package validation ->
experiences.jsonl insertion + manifest update + ThreadEx graph edge ->
Available for future skill loading
```

**Knowledge Synthesis emits the proposal. Skill Builder (or package mutator) applies it.** This preserves package integrity and prevents drift between skill.md and manifest.json.

Experience records include:
- What happened (scenario)
- What triggered it (trigger)
- What was done (action_taken)
- What tool was used (tool_choice)
- What went wrong (failure_mode)
- How it was fixed (recovery_tactic)
- Did it work (outcome + score)

This is the tactical memory layer that makes skills compound over time.

## Lifecycle Audit Mode

When synthesis_mode is audit, the pipeline reviews existing atoms:

| Signal | Direction | Recommendation |
|--------|-----------|----------------|
| Experience score improving over time | **Compounding** | Keep, consider promotion to skill rule |
| Experience score flat, no recent usage | **Stale** | Review for relevance, consider archival |
| Experience contradicted by newer data | **Decaying** | Flag for update or removal |
| Multiple experiences saying the same thing | **Redundant** | Consolidate into single stronger entry |
| Experience from deprecated skill | **Orphaned** | Migrate to replacement skill or archive |

## Failure Modes

| Failure | Detection | Recovery |
|---------|-----------|----------|
| Admitting low-quality atoms | Scores below threshold slip through | Enforce gate strictly, no overrides without human approval |
| Extracting prose as experience | Non-actionable text classified as tactical insight | Require action_taken and outcome fields to be non-empty |
| External import bypassing scoring | Atoms admitted without admission gate | All imports must pass through Phase 3 scoring |
| Token bloat from over-extraction | Too many atoms extracted from single source | Limit extraction to top-N scored atoms per source chunk |
| Conflicting atoms both admitted | Contradictory guidance in experience bank | Novelty detection catches conflicts, flags for human review |

## Recovery Steps

1. If low-quality atoms detected post-admission: re-run audit mode, remove below-threshold entries
2. If experience bank bloated: consolidate redundant entries, archive stale ones
3. If external import corrupted system: revert from ThreadEx graph snapshot, re-extract with stricter threshold
4. If skill seeds delegated to Skill Builder fail MMA: review extraction quality, tighten scoring criteria

## Examples

### Example 1: Extract from Training Document

**Input:** "Modern Persuasive Copy Feb 2026.markdown", synthesis_mode: extract, target_domain: copy
**Extracted:** 8 candidate atoms (3 patterns, 2 experiences, 1 failure, 2 references)
**Admitted:** 5 (scores 0.72-0.91), Rejected: 3 (below 0.70 threshold)
**Routing:** 2 experiences -> copy_director/experiences.jsonl, 1 failure -> sales_page_writer failure modes, 2 patterns -> copy/references/

### Example 2: Evaluate External Skill

**Input:** External "email-sequence-optimizer" skill from marketplace, synthesis_mode: evaluate
**Scored:** 12 atoms extracted, 4 scored above threshold
**Control eval:** Base model: 0.42, Base + external atoms: 0.51 (marginal improvement)
**Decision:** Admit 2 strongest experiences, reject skill_seeds (too narrow), reject patterns (redundant with existing email skills)

### Example 3: Enrich from Runtime

**Input:** Session log showing copy_director failing on long-form VSL structure, synthesis_mode: enrich
**Extracted:** 1 failure mode atom, 1 recovery tactic experience
**Admitted:** Both (scores 0.88 and 0.82)
**Routing:** Failure -> copy_director failure modes, Experience -> copy_director/experiences.jsonl

## Notes

- Knowledge Synthesis is the ONLY sanctioned intake path for new knowledge. No side-loading.
- External skill evaluation requires control evals before any admission. No exceptions.
- The rejection log is valuable data -- it shows what the system decided NOT to learn.
- Audit mode should run periodically (weekly or after major build sessions) to prevent experience bank decay.
- Skill seeds are handed off to Skill Builder, not built by Knowledge Synthesis. Clear separation of concerns.
- The admission gate threshold (0.7) can be raised for mature domains where quality bar is higher.

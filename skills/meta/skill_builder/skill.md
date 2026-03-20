---
id: skill.meta.skill_builder.v1_0_0
name: Skill Builder
version: 1.0.0
status: active
owner: supermind
category: meta
tags: [meta, skill-creation, packaging, validation, composition, relational]
description: >-
  Builds canonical XSkill packages from source material. Detects redundancy,
  generates sub-skills and xScripts, attaches eval expectations, and ensures
  every package declares domain, phase behavior, maturity orientation, and
  relational context. Produces skill.md + manifest.json + experiences.jsonl
  as a validated unit.
inputs:
  - source_material
  - build_mode
  - target_family
conditional_inputs:
  - existing_skill_registry
  - domain_context
  - voice_profile
outputs:
  - build_report
conditional_outputs:
  - skill_package         # not emitted on redundancy halt
  - redundancy_analysis   # emitted when registry provided
  - sub_skill_candidates  # emitted on decomposition
  - eval_expectations     # emitted on successful build
depends_on:
  - skill.meta.zpwo.v5_0_0
  - skill.meta.mma.v5_0_0
delegates_to: []
complements:
  - skill.meta.knowledge_synthesis.v1_0_0
required_tools:
  - validate
  - migrate
memory_reads:
  - threadex
  - experience_bank
  - obsidian
memory_writes:
  - threadex              # graph edges for new skill relationships
  - experience_bank       # seed experiences only (migration_seed source); runtime experiences are NOT written at build time
token_budget: large
risk_level: medium
model_preference: opus
eval_suite: skill-builder-core
---

# Skill Builder (v1.0.0)

Builds canonical XSkill packages from source material. Every output is a validated unit containing skill.md, manifest.json, and experiences.jsonl that declares its domain, phase behavior, maturity orientation, and relational position within the skill ecosystem.

Skill Builder does not just generate skills. It reduces redundancy, detects whether proposed material is better, redundant, too narrow, or complementary to existing skills, and packages the result with eval expectations and coherence checks.

## Purpose

Skill Builder is the factory that produces XSkill packages. It consumes source material (raw docs, XML legacy skills, transcripts, frameworks, patterns) and produces canonical packages in the locked format. It sits between Knowledge Synthesis (which extracts candidate atoms) and MMA (which scores the output).

The critical distinction: Skill Builder produces procedural skill specs. It does not produce experiences -- those come from runtime execution and Knowledge Synthesis. Skill Builder declares the contract; experiences record what actually happens.

## Use When

- Creating a new skill from raw source material (docs, transcripts, frameworks)
- Migrating a legacy XML skill into the XSkill format with architectural upgrades
- Decomposing a large skill into sub-skills and xScripts
- Refactoring an existing skill after MMA flags quality issues
- Packaging a skill family for distribution or marketplace

## Do Not Use When

- Scoring or validating an existing skill (use MMA)
- Extracting candidate atoms from raw sources (use Knowledge Synthesis)
- Routing tasks to skills at runtime (use ZPWO)
- Populating experience banks from runtime data (automatic via harness)

## Inputs

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| source_material | any | yes | Raw source: docs, XML, transcripts, frameworks, patterns |
| build_mode | string | yes | new_build, migrate, refactor, decompose, package |
| target_family | string | yes | Domain family: copy, research, design, ads, email, etc. |
| existing_skill_registry | json | no | Current skill inventory for redundancy detection |
| domain_context | markdown | no | Domain-specific context (industry, niche, market) |
| voice_profile | yaml | no | Brand voice DNA for persona-aware skills |

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| skill_package | directory | Complete XSkill package: skill.md + manifest.json + experiences.jsonl + sub-dirs |
| build_report | markdown | Build decisions, redundancy analysis, eval expectations |
| redundancy_analysis | markdown | Comparison against existing skills (emitted when registry provided) |
| sub_skill_candidates | list | Proposed sub-skills extracted during decomposition |
| eval_expectations | yaml | Expected performance benchmarks for the new skill |

## Build Modes

| Mode | Source | Output | When Used |
|------|--------|--------|-----------|
| new_build | Raw docs, transcripts, frameworks | Fresh XSkill package | Creating a skill that does not exist |
| migrate | Legacy XML skill | XSkill package (upgraded architecture) | Converting XML to new format |
| refactor | Existing skill.md + MMA fix_plan | Revised XSkill package | After MMA flags quality issues |
| decompose | Large skill.md | Parent skill + sub-skills + xScripts | Breaking monolith into composable units |
| package | Validated skill family | Distribution-ready bundle | Preparing for marketplace or plugin install (PLANNED -- not yet operational) |

## Workflow

### Phase 1: Analyze Source Material

1. Classify source type (raw doc, XML, existing skill, transcript, framework)
2. If existing_skill_registry provided, run redundancy detection
3. Determine whether source is: better than existing, redundant, too narrow, or complementary
4. If redundant, emit redundancy_analysis and halt -- do not create duplicate skills
5. If complementary, identify integration points with existing skills

### Phase 2: Extract Skill Structure

6. Identify the core procedural contract (inputs, outputs, workflow steps)
7. Identify domain, phase behavior, and maturity orientation
8. Classify as exploratory (T1), compositional (T2), executional (T3), or resonance-oriented (T4)
9. Extract sub-skill candidates -- any reusable procedure that could serve multiple parent skills
10. Extract xScript candidates -- any deterministic operation that should be a script, not a prompt

### Phase 3: Author Canonical Package

11. Generate skill.md with locked frontmatter schema
12. Populate all 12 body sections (Purpose through Notes)
13. Declare relational metadata: depends_on, delegates_to, complements
14. Declare memory contract: what this skill reads and writes
15. Generate manifest.json compiled from frontmatter
16. Create empty experiences.jsonl (populated at runtime, not at build time)
17. Create sub-skill stubs in sub_skills/ if candidates were identified
18. Create xScript stubs in scripts/ if deterministic operations were identified

### Phase 4: Validate and Report

19. Run structural validator against frontmatter and manifest
20. Run drift detector between skill.md and manifest.json
21. Run relational validator -- do depends_on targets actually exist?
22. Generate eval_expectations based on skill type and domain
23. Emit build_report with all decisions documented

## Redundancy Detection

Before building any new skill, Skill Builder compares against the existing registry:

| Signal | Classification | Action |
|--------|---------------|--------|
| Same inputs, same outputs, same workflow | **Redundant** | Halt. Do not build. Suggest using existing skill. |
| Same domain, different workflow, better coverage | **Upgrade candidate** | Build as replacement. Flag existing for deprecation. |
| Same domain, narrower scope | **Too narrow** | Absorb into existing skill as sub-skill or reject. |
| Different domain or complementary workflow | **Complementary** | Build and declare complements relationship. |
| Overlapping inputs but different outputs | **Composable** | Build and declare delegates_to or depends_on. |

## Sub-Skills and xScripts

### Sub-Skills (sub_skills/)
Reusable procedural components nested inside a parent skill package. Sub-skills are **private components** -- they do not get their own registry entries, IDs, or standalone manifests. They are scoped to their parent and accessed through the parent's workflow.

If a sub-skill becomes useful to multiple parent skills, it should be promoted to a full standalone skill with its own ID, manifest, and registry entry. Until then, it stays private.

**Criteria for extraction:**
- The procedure has clear inputs and outputs independent of the parent workflow
- It can be tested independently (even if not registered independently)
- It reduces the parent skill.md below the 400-line budget

### xScripts (scripts/)
Deterministic operations that should execute as code, not as LLM prompts.

**Criteria for extraction:**
- The operation has deterministic inputs and outputs
- It does not require judgment, creativity, or reasoning
- It can be tested with unit tests
- Examples: validation, formatting, scoring calculation, file operations

## Phase Behavior Declaration (Locked Schema Fields)

Every skill built by Skill Builder must declare its phase behavior using these exact frontmatter field names. ZPWO and MMA consume these mechanically.

**Locked frontmatter field:** `phase_type`
**Locked enum:** `exploratory | compositional | executional | resonant`

| Phase Type | Description | Example Skills |
|-----------|-------------|----------------|
| exploratory | Generates candidates, explores options, diverges | Market research, competitor analysis |
| compositional | Structures and frames, converges options | Offer architecture, funnel design |
| executional | Produces deliverables, implements plans | Copy writing, code generation |
| resonant | Polishes for human impact, maximizes persuasion | Voice editing, headline optimization |

**Locked frontmatter field:** `maturity_stage`
**Locked enum:** `seed | developing | production | mature`

This declaration feeds ZPWO's cadence routing and MMA's phase-aware scoring. Skills without these fields will fail structural validation.

## Domain and Context Framing (Locked Schema Fields)

Skills must declare domain awareness using these exact frontmatter field names:

**Locked frontmatter field:** `domain_context`

```yaml
domain_context:
  primary_domain: ecommerce    # ecom | saas | b2b | coaching | apps | health | general
  sub_domain: supplement        # niche within domain (freeform string)
  market_awareness: direct_response  # direct_response | content | enterprise | community
  industry_patterns: [urgency, social_proof, authority]  # list of known patterns
  voice_orientation: conversational  # formal | conversational | technical | provocative
```

**Locked manifest field:** `domain_context` (same structure, compiled from frontmatter)

This enables domain-specific scoring in MMA and contextual routing in ZPWO.

## Eval Expectations (Locked Schema Fields)

Every skill package must include eval expectations. These define what "good" looks like and are the basis for proving the architecture improves real performance.

**Locked frontmatter field:** `eval_expectations`

```yaml
eval_expectations:
  base_model_baseline: 0.45     # expected score without skill
  skill_only_target: 0.65       # expected score with skill loaded
  skill_plus_experience: 0.80   # expected score with skill + experience bank
  key_metrics:
    - name: task_completion_rate
      target: 0.85
    - name: output_quality_score
      target: 7.5
    - name: token_efficiency
      target: medium
  control_test: "Run base task without skill, then with skill, compare scores"
```

**Locked manifest field:** `eval_expectations` (same structure, compiled from frontmatter)

## Lifecycle Tracking

Skills compound or decay. Skill Builder attaches lifecycle metadata:

| Signal | Direction | Action |
|--------|-----------|--------|
| Experience bank growing, scores improving | **Compounding** | Mark as healthy, consider promotion |
| Scores stable, no new experiences | **Plateau** | Review for refresh or consolidation |
| Scores declining, experiences show failures | **Decaying** | Flag for refactor or deprecation |
| Replaced by better skill in same domain | **Superseded** | Archive with pointer to replacement |

## Failure Modes

| Failure | Detection | Recovery |
|---------|-----------|----------|
| Building redundant skill | Registry comparison shows >80% overlap | Halt build, suggest existing skill |
| Monolith skill (>500 lines) | Line count check on generated skill.md | Trigger decompose mode, extract sub-skills |
| Missing phase declaration | Validator flags empty phase behavior | Require classification before package completion |
| Orphaned relationships | depends_on target not in registry | Flag for resolution, do not ship orphaned package |
| No eval expectations | Package missing eval section | Generate baseline expectations from domain averages |

## Recovery Steps

1. If redundancy detected: present comparison to human, get explicit override or redirect
2. If monolith detected: run decompose mode, present sub-skill candidates
3. If validation fails: fix structural issues, re-run validator
4. If relationships orphaned: resolve targets or remove relationship declaration

## Examples

### Example 1: New Build from Raw Docs

**Input:** 3 sales copy training documents (docx), build_mode: new_build, target_family: copy
**Process:** Extract procedural patterns, identify 2 sub-skill candidates (hook_generator, proof_stacker), classify as executional, declare copy domain with direct_response market
**Output:** skill-copy-sales_page_writer-v1_0_0/ with skill.md, manifest.json, experiences.jsonl, sub_skills/hook_generator/, sub_skills/proof_stacker/, eval expectations targeting 0.70 skill-only score

### Example 2: Migrate with Redundancy Detection

**Input:** Legacy XML advertorial_copy_master_v2.0.xml, build_mode: migrate, existing_skill_registry provided
**Process:** Parse XML to AST, compare against registry, find 85% overlap with copy_director_v3
**Output:** redundancy_analysis showing overlap, recommendation to absorb unique patterns into copy_director as sub-skill rather than creating duplicate

### Example 3: Decompose Monolith

**Input:** sales_page_deconstructor_v4 (550 lines), build_mode: decompose
**Process:** Identify 4 independent procedures: neuro_box_scorer, chain_validator, framework_extractor, surgical_reviser
**Output:** Refactored parent skill (180 lines) + 4 sub-skills in sub_skills/, each independently testable

## Notes

- Skill Builder consumes ZPWO v5.0 contracts for phase routing and MMA v5.0 contracts for quality gates.
- It does NOT populate experience banks at build time. Experiences come from runtime execution.
- Seed experiences (migration_seed source) are the exception -- these capture known patterns from legacy docs.
- Every package must pass structural validation before Skill Builder marks it complete.
- Marketplace packaging (build_mode: package) is future work -- the infrastructure is declared but not yet operational.

# MODULE FOUR V1 → V2 PATCH UPGRADE REQUIREMENTS

## OBJECTIVE
Upgrade **Module FOUR YouTube Script Generator V1.markdown** (323 lines, ~22 pages) to **MODULE FOUR V2 COMPLETE** (35-40 pages) by integrating content from the 4 working section files while preserving V1's existing structure.

---

## UPGRADE STRATEGY: PRESERVE + ENHANCE + EXPAND

**DO NOT replace V1.** Instead, **enhance and expand** it using this patch approach:

### Phase 1: PRESERVE (Keep V1 Foundation)
Retain these sections from V1 exactly as written:
- Section 1: GEO Knowledge Compendium (lines 1-65)
- Section 2A-C: Module Blueprint - Purpose, Inputs, Outputs (lines 66-118)
- Section 2D: Workflow - 6 Phases (lines 69-95) — **BUT enhance with expanded detail from MODULE FOUR WORKFLOW EXPANDED.docx**

### Phase 2: ENHANCE (Upgrade Existing Sections)
Replace/expand these V1 sections with enhanced versions from working files:

#### 2.1 Workflow Section (Currently lines 69-95 in V1)
**Current State:** Brief 6-phase outline (~27 lines)
**Upgrade With:** MODULE FOUR WORKFLOW EXPANDED.docx
**New Length:** 6-7 pages with Day/Hour/Step detail
**Integration Point:** Replace V1 lines 69-95, insert expanded workflow

**Example of Enhancement:**
```
V1 (Current):
Phase 1: Pre-Production Foundation (Day 1 Morning)
• Step 1.1: Load WSA Input. Import the 7-section WSA from Module 3.
• Step 1.2: EVR Planning. Define the Expectation vs Reality. Score the gap.

V2 (Enhanced from WORKFLOW-EXPANDED.docx):
Phase 1: Pre-Production Foundation (Day 1 Morning - 3 hours)

Step 1.1: Load WSA Input (30 minutes)

Action 1: Import the 7-section WSA from Module 3
- Open WSA article in Google Docs
- Extract core sections: Safety Anchor, Mechanism, Proof, Action Path, Objection Kill, Value Stack, Closer
- Copy into new document titled "Video Source Material"

Action 2: Identify Core Insights
- Read through WSA
- Highlight the 3 most surprising/valuable insights
- Ask: "What made me go 'Whoa, I didn't know that' when researching this?"
- Mark these as "EVR Candidates"

Tool: Google Docs or Notion

Output: Single document with WSA content + 3 EVR candidates + keyword data

Quality Gate: Can you explain the article's value in one sentence? If not, re-read.
```

#### 2.2 Failure Modes Section (Currently lines 96-99 in V1)
**Current State:** 4 failure modes, 1 line each (~4 lines total)
**Upgrade With:** MODULE FOUR REMAINING SECTIONS.docx (Failure Modes 1-6)
**New Length:** 3-4 pages with full diagnostics
**Integration Point:** Replace V1 lines 96-99, insert expanded failure modes

**Enhancement Requirements:**
Each failure mode MUST include (from REMAINING SECTIONS.docx):
1. Symptom (3-5 observable bullet points)
2. Root Cause (clear explanation)
3. Diagnostic Questions (3-5 questions)
4. Real-World Example (story with metrics)
5. Step-by-Step Recovery (6-8 detailed steps with time estimates)
6. Prevention Strategies (5-6 actionable tactics)
7. Tools Needed (specific tool names)
8. Timeline to Recovery (total time estimate)

Add Failure Modes 5 & 6 from REMAINING SECTIONS.docx:
- Mode 5: CTA Rejection
- Mode 6: Viral-But-Wrong-Audience

### Phase 3: EXPAND (Add New Sections)
Insert these NEW major sections that don't exist in V1:

#### 3.1 Knowledge Blocks Section (NEW - Insert after Section 2I)
**Source:** MODULE FOUR KB SECTIONS.docx
**Length:** 20-24 pages
**Content:**
- KB-VIDEO-SCRIPT-ARCHITECTURE-v1.0 (5-6 pages)
  - WSA → Video Transformation (7-section mapping)
  - 5-Part Video Structure
  - 12 Story Archetypes (BOFU-adapted)
  - Video Schema & Code Examples
  - BOFU Video Types (Comparison, Best Of, Problem-Solution, Alternative)

- KB-VIRAL-HOOK-ENGINEERING-v1.0 (6-7 pages)
  - EVR Psychology (Expectations vs Reality gap scoring 0-10)
  - Hook Models (Single Subject + Single Question, 3-Hook Alignment, 4 Stun Types)
  - 20 Hook Templates (each with: structure, BOFU adaptation, neuro-axis, EVR score, example)
  - Hook Quality Audit Checklist (8 criteria)
  - Trauma-Aware EVR (ethical boundaries, blocked axes handling)

- KB-RETENTION-MECHANICS-v1.0 (5-6 pages)
  - Script Workflow (Psychology → Packaging → Outline → Intro → Body → Outro)
  - Body Sequencing (purchase driver timeline, neuro-axis activation by minute)
  - Grease-Slide Connectors (20+ transition phrases)
  - Rehook Strategy (every 90-120 seconds)
  - Visual Retention Aids (B-roll timing, on-screen text, pattern interrupts)
  - Balance Checking for Video (excitatory ↔ inhibitory pairing)

- KB-VIDEO-SEO-OPTIMIZATION-v1.0 (4-5 pages)
  - YouTube SEO Architecture (title, description, tags, thumbnail optimization)
  - AI Discovery Optimization (citation magnets for video, transcript optimization, chapter timestamps)
  - Schema for Video (VideoObject + FAQPage JSON-LD code examples)
  - Video-to-Article Integration (hub-and-spoke, bi-directional linking, repurposing strategy)

**Integration Point:** Insert as new "Section 3: Knowledge Blocks" between current V1 Section 2 and Section 3

#### 3.2 Case Studies Section (NEW - Insert after Knowledge Blocks)
**Source:**
- MODULE FOUR REMAINING SECTIONS.docx (Case Study 1)
- MODULE FOUR FINAL ELEMENTS.docx (Case Studies 2-3)
**Length:** 6-7 pages (2+ pages per study)
**Content:**

**Case Study 1: B2B SaaS (Rankability) - "Technical SEO Audit for SaaS"**
- Context: Company background, team size, starting metrics
- Challenge: Specific problem with founder quotes
- Strategy Approach: Month-by-month planning
- Execution: Week-by-week timeline with EVR score, neuro-axis timeline, CTA strategy
- Results: 14,800 views, 6.2% CTR, 64% AVD, 127 trial signups, $31,750 revenue (90 days)
- Lessons Learned: What worked/didn't with specifics
- Downstream Impact: How it fed other modules

**Case Study 2: E-Commerce (Outdoor Gear) - "Best Tents for Tall People"**
- Results: 284K views, 9.4% CTR, 61% AVD, $47,320 revenue (affiliate + direct)

**Case Study 3: B2B Consulting (Agency) - "How to Sell SEO Retainers"**
- Results: 31,400 views, 11.2% CTR, 67% AVD, 7 clients won, $84K revenue (180 days)

**Integration Point:** Insert as new "Section 4: Case Studies" after Knowledge Blocks

#### 3.3 Pattern Library Section (NEW - Insert after Case Studies)
**Source:** MODULE FOUR FINAL ELEMENTS.docx
**Length:** 2 pages
**Content:** 10 YAML Patterns with full structure:

```yaml
- pattern_id: "p_neuro_video_timeline_map"
  name: "Neuro-Axis Video Timeline Mapping"
  category: "structure"
  when_to_use: "Module 4 - Phase 1 (Neuro-Mapping)"
  structure: |
    Step 1: Map video minutes to 6 axes
    Step 2: Score activation intensity (1-10)
    Step 3: Check balance (≤4 point difference)
    Step 4: Adjust script for weak axes
  mma_impact: "High - Ensures complete neurochemical activation"
  example_context: "8-minute video: BODY (0-1 min), MIND (1-3), SPIRIT (3-5), PSYCHE (5-7), CONNECTION (7-8)"
```

Include all 10 patterns:
1. p_neuro_video_timeline_map
2. p_evr_gap_engineering
3. p_3_hook_alignment_validator
4. p_grease_slide_connector_library
5. p_native_cta_embed
6. p_video_seo_schema
7. p_chapter_timestamp_optimizer
8. p_velvet_hammer_video_adapt
9. p_retention_cliff_recovery
10. p_short_form_clip_generator

**Integration Point:** Insert as new "Section 5: Pattern Library" after Case Studies

#### 3.4 Output Templates Section (NEW - Insert after Pattern Library)
**Source:** MODULE FOUR FINAL ELEMENTS.docx
**Length:** 2 pages
**Content:** 4 production-ready templates:

1. **Template 1: Video Script Outline**
   - EVR gap score
   - Neuro-timeline map
   - Chapter outline with timestamps
   - 3-Hook alignment check
   - Native CTA placement
   - Metadata structure

2. **Template 2: Neuro-Axis Video Scorecard**
   - 6-axis coverage (each scored 1-10)
   - Balance check (excitatory vs inhibitory)
   - Overall score /60
   - Gap identification
   - Improvement recommendations

3. **Template 3: Hook Quality Audit Checklist**
   - 8 criteria with pass/fail
   - EVR gap score validation
   - 3-Hook alignment verification
   - Stun type assessment
   - BOFU qualification check

4. **Template 4: Video SEO Optimization Checklist**
   - 40-point pre/post-publish checklist
   - Title optimization (keyword front-loading)
   - Description architecture
   - Chapter timestamp formatting
   - Schema implementation
   - Thumbnail optimization
   - Transcript optimization

**Integration Point:** Insert as new "Section 6: Output Templates" after Pattern Library

---

## CROSS-REFERENCE INTEGRATION

Throughout the expanded content, add cross-references to supplemental frameworks using this format:

```markdown
**Note:** This section builds on the comprehensive [concept] documented in [FRAMEWORK.docx]. For complete [methodology]:

→ Refer to: [FRAMEWORK.docx]

This section provides the BOFU-specific video adaptation and YouTube integration.
```

**Required Cross-References:**

1. In KB-VIRAL-HOOK-ENGINEERING:
```markdown
→ Refer to: VIRAL RESONANCE ARCHITECT v1.0.docx
```

2. In Neuro-Axis sections:
```markdown
→ Refer to: NEURO RESONANCE AUDITOR v2.1.docx
```

3. In Human Voice Polish sections:
```markdown
→ Refer to: HUMAN PERSUASION EDITOR v2.1.docx
```

4. In Voice validation sections:
```markdown
→ Refer to: VOICE DNA v1.0.docx
```

---

## INTEGRATION CHECKLIST

Before finalizing V2, validate:

### Content Completeness
- [ ] All V1 foundation content preserved
- [ ] 6-Phase Workflow expanded to 6-7 pages with Day/Hour/Step detail
- [ ] 6 Failure Modes expanded to 3-4 pages with full diagnostics
- [ ] 4 Knowledge Blocks added (20-24 pages total)
- [ ] 3 Case Studies added (6-7 pages total, 2+ pages each)
- [ ] 10 YAML Patterns added (2 pages)
- [ ] 4 Output Templates added (2 pages)

### Quality Standards
- [ ] Evidence-based: Every claim cited (analytics, case studies, research)
- [ ] Actionable: Day/Hour/Step workflow detail maintained
- [ ] BOFU-focused: Commercial intent throughout (Intent Score 7-10)
- [ ] Integrated: GEO + Neuro + Viral working together
- [ ] Neuro-aware: 6-axis integration with balance checking
- [ ] Viral engineering: EVR 7+, hook templates, grease-slide connectors
- [ ] GEO-optimized: YouTube SEO, AI citation magnets, schema
- [ ] Human voice: Kitchen table test language

### Structure Validation
- [ ] Page count: 35-40 pages ✓
- [ ] Section numbering consistent (1-7)
- [ ] Cross-references formatted correctly
- [ ] YAML patterns valid syntax
- [ ] Code examples (JSON-LD) properly formatted
- [ ] Tables properly formatted
- [ ] Examples concrete (with numbers/metrics)

### Cross-Module Integration
- [ ] References to Module 1 (Strategy) validated
- [ ] References to Module 2 (Research) validated
- [ ] References to Module 3 (Writing) validated
- [ ] References to Module 5 (Lead Magnet) validated
- [ ] References to Module 6 (Site Orchestrator) validated
- [ ] References to Module 7 (Auditor) validated

---

## FINAL STRUCTURE (V2 Complete)

```
MODULE 4: youtube-script-generator (MASTER COMPENDIUM V2)

├── 1. GEO Knowledge Compendium: Video Intelligence Layer (5 pages) [FROM V1 - PRESERVED]
│   ├── A. Category Map: The Video Battlefield (2026)
│   ├── B. FAQ → SHAQ Ladder (Video Focused)
│   └── C. HCTS Library (Video Tactics)

├── 2. Module Blueprint (12-15 pages) [FROM V1 - ENHANCED]
│   ├── A. Purpose & Strategic Context [V1 - PRESERVED]
│   ├── B. Inputs Required [V1 - PRESERVED]
│   ├── C. Outputs Produced [V1 - PRESERVED]
│   ├── D. Workflow - 6 Phases [V1 - EXPANDED with WORKFLOW-EXPANDED.docx]
│   ├── E. Quality Checks [V1 - PRESERVED]
│   ├── F. Failure Modes [V1 - EXPANDED with REMAINING-SECTIONS.docx]
│   ├── G. Success Metrics [V1 - PRESERVED]
│   ├── H. Integration with Other Modules [V1 - PRESERVED]
│   └── I. Automation Opportunities [V1 - PRESERVED]

├── 3. Knowledge Blocks (20-24 pages) [NEW - FROM KB-SECTIONS.docx]
│   ├── KB-VIDEO-SCRIPT-ARCHITECTURE-v1.0 (5-6 pages)
│   ├── KB-VIRAL-HOOK-ENGINEERING-v1.0 (6-7 pages)
│   ├── KB-RETENTION-MECHANICS-v1.0 (5-6 pages)
│   └── KB-VIDEO-SEO-OPTIMIZATION-v1.0 (4-5 pages)

├── 4. Case Studies (6-7 pages) [NEW - FROM REMAINING-SECTIONS.docx + FINAL-ELEMENTS.docx]
│   ├── Case Study 1: B2B SaaS (Rankability)
│   ├── Case Study 2: E-Commerce (Outdoor Gear)
│   └── Case Study 3: B2B Consulting (Agency)

├── 5. Pattern Library (2 pages) [NEW - FROM FINAL-ELEMENTS.docx]
│   └── 10 YAML Patterns with full structure

├── 6. Output Templates (2 pages) [NEW - FROM FINAL-ELEMENTS.docx]
│   ├── Template 1: Video Script Outline
│   ├── Template 2: Neuro-Axis Video Scorecard
│   ├── Template 3: Hook Quality Audit Checklist
│   └── Template 4: Video SEO Optimization Checklist

└── 7. README (Deployment Guide) (1 page) [FROM V1 - PRESERVED/ENHANCED]
    ├── What This Is
    ├── How to Run It (6-phase execution)
    ├── Integration Points (Modules 1-7)
    ├── Constitutional Warnings
    └── Start Command
```

**Total:** 35-40 pages

---

## NOTEBOOKLM EXECUTION INSTRUCTIONS

**Step 1:** Load MODULE FOUR YouTube Script Generator V1.markdown as the base

**Step 2:** Apply patches in this order:
1. Expand Workflow (Section 2D) with WORKFLOW-EXPANDED.docx
2. Expand Failure Modes (Section 2F) with REMAINING-SECTIONS.docx
3. Insert Knowledge Blocks (New Section 3) with KB-SECTIONS.docx
4. Insert Case Studies (New Section 4) with REMAINING-SECTIONS.docx + FINAL-ELEMENTS.docx
5. Insert Pattern Library (New Section 5) with FINAL-ELEMENTS.docx
6. Insert Output Templates (New Section 6) with FINAL-ELEMENTS.docx

**Step 3:** Add cross-references to supplemental frameworks:
- VIRAL RESONANCE ARCHITECT v1.0.docx
- NEURO RESONANCE AUDITOR v2.1.docx
- HUMAN PERSUASION EDITOR v2.1.docx
- VOICE DNA v1.0.docx

**Step 4:** Model quality/tone on:
- AI GEO STRATEGY ARCHITECT V4 Module ONE.docx
- AI SEO BOFU QUERY RESEARCHER V2 Module TWO.docx
- AI SEO WHOLE SOLUTION WRITER V2 Module THREE.docx

**Step 5:** Validate against checklist above

**Step 6:** Output as MODULE-FOUR-YOUTUBE-SCRIPT-GENERATOR-V2-COMPLETE.md

---

## SUCCESS CRITERIA

✅ Page count: 35-40 pages
✅ All V1 content preserved
✅ All 4 working section files integrated
✅ All cross-references formatted correctly
✅ Quality matches Modules ONE/TWO/THREE
✅ BOFU-focused throughout
✅ Evidence-based (every claim cited)
✅ Actionable (Day/Hour/Step detail)
✅ Neuro-aware (6-axis integration)
✅ Viral engineering (EVR 7+, hooks, connectors)
✅ GEO-optimized (YouTube SEO, AI citations, schema)

---

**PATCH UPGRADE COMPLETE**

This approach preserves your V1 investment while systematically upgrading to V2's 35-40 page depth through modular integration of the working section files.

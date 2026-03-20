# MODULE FOUR V3 + KB-SECTIONS MERGE DIRECTIVE

## OBJECTIVE
Merge **Module FOUR YouTube Script Generator V3.markdown** (660 lines, ~30-32 pages) with **MODULE-FOUR-KB-SECTIONS.md** full detailed Knowledge Blocks to create **MODULE FOUR FINAL** (35-40 pages).

## PROBLEM IDENTIFIED
V3 already contains abbreviated KB content (lines 323-397, ~3 pages total) covering:
- KB-VIRAL-HOOK-ENGINEERING (brief)
- KB-RETENTION-MECHANICS (brief)
- KB-VIDEO-SEO-OPTIMIZATION (brief)

MODULE-FOUR-KB-SECTIONS.md contains the **full detailed** versions (20-24 pages total).

## MERGE STRATEGY

### Step 1: REMOVE Brief KB Section from V3
**Delete lines 323-397** from V3 (the condensed KB section starting with "3. Knowledge Blocks")

### Step 2: INSERT Full KB Section from KB-SECTIONS.md
**Insert at line 323** the complete detailed content from MODULE-FOUR-KB-SECTIONS.md containing:

1. **KB-VIRAL-HOOK-ENGINEERING-v1.0** (6-7 pages)
   - Full 20 Hook Templates with complete details (structure, BOFU adaptation, neuro-axis, EVR score, example, when to use, thumbnail concept, first 15 seconds script)
   - Hook Quality Audit Checklist (8 criteria)
   - Trauma-Aware EVR guidelines

2. **KB-RETENTION-MECHANICS-v1.0** (5-6 pages)
   - Complete Script Workflow (6-step process with timing)
   - Body Sequencing with Purchase Driver Timeline (5-stage breakdown)
   - Grease-Slide Connector Library (20+ transition phrases with examples)
   - Rehook Strategy (every 90-120 seconds with implementation guide)
   - Visual Retention Aids (B-roll timing, on-screen text, pattern interrupts)
   - Balance Checking for Video (excitatory ↔ inhibitory pairing formulas)

3. **KB-VIDEO-SEO-OPTIMIZATION-v1.0** (4-5 pages)
   - YouTube SEO Architecture (detailed title/description/tags optimization)
   - AI Discovery Optimization (citation magnets, transcript optimization, chapter timestamps)
   - Complete Schema Implementation (VideoObject + FAQPage JSON-LD with full code examples)
   - Video-to-Article Integration (hub-and-spoke strategy, bi-directional linking, repurposing workflow)

4. **KB-VIDEO-SCRIPT-ARCHITECTURE-v1.0** (5-6 pages)
   - WSA → Video Transformation (complete 7-section mapping with examples)
   - 5-Part Video Structure (detailed breakdown)
   - 12 Story Archetypes (BOFU-adapted with use cases)
   - BOFU Video Types (Comparison, Best Of, Problem-Solution, Alternative with full details)
   - Complete Schema Code Examples

### Step 3: RENUMBER Sections
After insertion:
- Current V3 "4. Case Studies" (line 399) → becomes "4. Case Studies" (stays same)
- Current V3 "5. Pattern Library" (line 434) → becomes "5. Pattern Library" (stays same)
- Current V3 "6. Output Templates" (line 568) → becomes "6. Output Templates" (stays same)
- Current V3 "7. README" (line 644) → becomes "7. README" (stays same)

**No renumbering needed** - V3 already has space for Knowledge Blocks between Section 2 and Section 4.

### Step 4: ADD Cross-References
In the inserted KB sections, add these cross-references:

**In KB-VIRAL-HOOK-ENGINEERING:**
```markdown
**Note:** This KB builds on the comprehensive hook engineering system documented in VIRAL RESONANCE ARCHITECT v1.0.docx. For complete EVR Psychology scoring methodology, full hook template examples, and derisking loops:

→ Refer to: VIRAL RESONANCE ARCHITECT v1.0.docx

This KB provides the BOFU-specific video adaptation and YouTube integration.
```

**In Neuro-Axis sections:**
```markdown
→ Refer to: NEURO RESONANCE AUDITOR v2.1.docx for complete 6-axis framework definitions and balance calculation methodology.
```

**In Human Voice sections:**
```markdown
→ Refer to: HUMAN PERSUASION EDITOR v2.1.docx for complete Velvet Hammer 6-Pass process and AI word purge list.
```

**In Voice validation sections:**
```markdown
→ Refer to: VOICE DNA v1.0.docx for complete G.I.V.E. framework and voice validation checklist.
```

## FINAL STRUCTURE

```
MODULE 4: youtube-script-generator (MASTER COMPENDIUM FINAL)

├── 1. GEO Knowledge Compendium: Video Intelligence Layer (5 pages) [FROM V3]
│   ├── A. Category Map: The Video Battlefield (2026)
│   ├── B. FAQ → SHAQ Ladder (Video Focused)
│   └── C. HCTS Library (Video Tactics)

├── 2. Module 4 Blueprint (12-15 pages) [FROM V3]
│   ├── A. Purpose & Strategic Context
│   ├── B. Inputs Required
│   ├── C. Outputs Produced
│   ├── D. Step-by-Step Workflow (6 Phases - Detailed)
│   ├── E. Quality Checks
│   ├── F. Failure Modes (6 modes with full diagnostics)
│   ├── G. Success Metrics
│   ├── H. Integration with Other Modules
│   └── I. Automation Opportunities

├── 3. Knowledge Blocks (20-24 pages) [FROM KB-SECTIONS.md - FULL DETAIL ⭐⭐⭐]
│   ├── KB-VIRAL-HOOK-ENGINEERING-v1.0 (6-7 pages)
│   ├── KB-RETENTION-MECHANICS-v1.0 (5-6 pages)
│   ├── KB-VIDEO-SEO-OPTIMIZATION-v1.0 (4-5 pages)
│   └── KB-VIDEO-SCRIPT-ARCHITECTURE-v1.0 (5-6 pages)

├── 4. Case Studies (6-7 pages) [FROM V3]
│   ├── Case Study 1: B2B SaaS (Rankability)
│   ├── Case Study 2: E-Commerce (Outdoor Gear)
│   └── Case Study 3: B2B Consulting (Agency)

├── 5. Pattern Library (2 pages) [FROM V3]
│   └── 10 YAML Patterns with full structure

├── 6. Output Templates (2 pages) [FROM V3]
│   ├── Template 1: Video Script Outline
│   ├── Template 2: Neuro-Axis Video Scorecard
│   ├── Template 3: Hook Quality Audit Checklist
│   └── Template 4: Video SEO Optimization Checklist

└── 7. README (Deployment Guide) (1 page) [FROM V3]
    ├── What This Is
    ├── How to Run It
    ├── Integration
    ├── Constitutional Warnings
    └── Start Command
```

**Total:** 35-40 pages

## EXECUTION

**Manual Merge Steps:**
1. Open Module FOUR YouTube Script Generator V3.markdown
2. Delete lines 323-397 (brief KB section)
3. At line 323, insert complete content from MODULE-FOUR-KB-SECTIONS.md
4. Add cross-references to supplemental frameworks
5. Save as: Module FOUR YouTube Script Generator FINAL.markdown
6. Validate page count: 35-40 pages

**OR Use Claude/GPT to Merge:**
Upload both files with this directive and ask to perform the merge automatically.

## VALIDATION CHECKLIST

- [ ] V3 brief KB section removed (lines 323-397)
- [ ] Full KB-SECTIONS content inserted (20-24 pages)
- [ ] All 4 KBs present with full detail
- [ ] Cross-references to supplemental frameworks added
- [ ] Section numbering consistent (1-7)
- [ ] Total page count: 35-40 pages
- [ ] All V3 case studies, patterns, templates preserved
- [ ] Quality matches Modules ONE/TWO/THREE depth

---

**MERGE NOW TO CREATE MODULE FOUR FINAL (35-40 pages)**

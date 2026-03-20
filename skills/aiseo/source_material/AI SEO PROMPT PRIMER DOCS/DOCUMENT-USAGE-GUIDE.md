# AI GEO Framework Documents: Usage Guide
## When and How to Reference Each Document

---

## THE 5 FRAMEWORK DOCUMENTS

### **Document 1: AI-GEO-SUPER-SKILL-PRIMER.docx** (Your Original - 35KB)
**What It Is**: Your strategic vision, principles, and guidance points
**Primary Author**: You (Vision Capitalist)
**Voice**: Strategic, directive, principled

#### **When to Reference**:
✅ **Strategic Direction** - For "why" questions and priorities
- "Should we focus on BOFU vs TOFU content?" → Reference PRIMER's content approach guidance
- "Is Reddit SEO worth investing in?" → Reference PRIMER's warning about Reddit spam decline
- "How should we measure success?" → Reference PRIMER's measurement philosophy (bespoke analytics, accept broken attribution)

✅ **Ethical Boundaries** - For what NOT to do
- "Can we buy links?" → Reference PRIMER's explicit "stop buying links immediately" guidance
- "Should we spam Reddit?" → Reference PRIMER's parasite SEO warning
- "Can we use AI to write 100 posts?" → Reference PRIMER's topical authority vs listicle guidance

✅ **Voice/Tone Calibration** - For maintaining YOUR strategic voice
- When NotebookLM generates content that sounds too generic → Remind it to reference PRIMER's specific phrasing and urgency
- Example: PRIMER uses "Stop buying links immediately" (directive, urgent) vs generic "link building may not be effective"

#### **What to Extract From It**:
- **Guidance Ideas Section** (emoji-tagged strategic warnings):
  - 🎯 Avoid parasite SEO → Use in HCTS "Cracks" section
  - 📉 Expect Reddit decline → Use in Module 1 (platform strategy)
  - 🔗 Stop buying links → Use in compliance guardrails
  - 🎯 Target BOFU queries → Use in Module 2 (query researcher)
  - 🤖 Optimize for top 10 traditional rankings → Use in FAQ/SHAQ section
  - 📺 YouTube SEO priority → Use in Module 4 blueprint
  - 📉 Build bespoke analytics → Use in measurement framework

- **DSA Model** (Deep Solutions Authority):
  - FAQ → SHAQ → HCTS → Whole Solution
  - Use as foundation for Module 3 (whole-solution-writer)

- **NotebookLM Workflow Context**:
  - How you've been using NotebookLM already
  - Helps NotebookLM understand its role in your system

#### **How to Reference It**:
```
"Reference the AI-GEO-SUPER-SKILL-PRIMER for strategic priorities and ethical boundaries. Use the Guidance Ideas section to inform warnings about:
- Reddit spam saturation timeline
- Link buying risks
- BOFU priority over TOFU
- Measurement philosophy (citations over clicks)

Preserve the directive, urgent tone from the PRIMER (e.g., 'Stop buying links immediately' not 'link buying may decline in effectiveness')."
```

---

### **Document 2: NOTEBOOKLM-META-PROMPT-AI-GEO-COMPENDIUM-v1.0.md** (My Meta Prompt - 55KB)
**What It Is**: Complete instruction manual for NotebookLM
**Primary Author**: Claude (me)
**Voice**: Systematic, detailed, operational

#### **When to Reference**:
✅ **Structure & Format** - For "how to organize" questions
- "What sections should the compendium have?" → Reference META-PROMPT's 5 deliverable specifications
- "How should FAQ/SHAQ ladder be structured?" → Reference META-PROMPT's table format
- "What's the 9-Block DSA framework?" → Reference META-PROMPT's detailed template

✅ **Quality Standards** - For "how good is good enough" questions
- "What's the AVE Standard?" → Reference META-PROMPT's Authority/Value/Expertise criteria
- "What's the DSA Test?" → Reference META-PROMPT's "One Sentence Rule" (full solution + why it works)
- "How do I cite sources safely?" → Reference META-PROMPT's Proof Toolkit (5-tier claim hierarchy)

✅ **Constitutional Compliance** - For ULTRAMIND v2.0 alignment
- "Does this follow autonomy over automation?" → Reference META-PROMPT's compliance framework
- "How do I map to Neuro-Box 6D?" → Reference META-PROMPT's consciousness integration guide

#### **What to Extract From It**:
- **Deliverable 1 Template**: GEO Knowledge Compendium structure
  - Category Map (pains, outcomes, misconceptions)
  - FAQ → SHAQ Ladder (table format with 6 columns)
  - Whole Solution Framework (9-block template)
  - HCTS Library (Hacks/Cracks/Tracks/Stacks categories)
  - Authority & Proof Toolkit (5-tier claim hierarchy)

- **Deliverable 2 Template**: Skill Module Blueprints
  - For each module: Purpose, Inputs, Outputs, Workflow, Quality Checks, Failure Modes

- **Deliverable 3 Template**: Pattern Library YAML
  - Structure with all fields: pattern_id, name, category, when_to_use, when_NOT_to_use, examples, mma_impact, effectiveness_rating

- **Deliverable 4 Template**: Output Templates
  - WSA template, YouTube script, Lead magnet, Programmatic page

- **Deliverable 5 Template**: Skill Formation README
  - Deployment guide, measurement strategy, troubleshooting

#### **How to Reference It**:
```
"Follow the NOTEBOOKLM-META-PROMPT-AI-GEO-COMPENDIUM-v1.0 for exact deliverable structure. Use the templates provided for:
- FAQ → SHAQ Ladder (6-column table)
- 9-Block DSA Framework (Problem → Causes → Mechanisms → Missteps → Protocol → Stacks → Objections → Proof → CTA)
- Pattern Library YAML (all fields required)
- Quality gates (AVE Standard, DSA Test, Proof Toolkit)

Ensure all outputs pass constitutional compliance checks specified in the meta prompt."
```

---

### **Document 3: AI-GEO-SKILL-MODULE-ARCHITECTURE.md** (Technical Specs - 16KB)
**What It Is**: Technical blueprint for Modules 1-6
**Primary Author**: Claude (me)
**Voice**: Technical, precise, architectural

#### **When to Reference**:
✅ **Module Design** - For "how should this skill work" questions
- "What are the 6 core modules?" → Reference ARCHITECTURE's module list
- "What's the naming convention?" → Reference ARCHITECTURE's direct Noun-Verb format (no KB prefix)
- "What Knowledge Blocks does each module need?" → Reference ARCHITECTURE's dependency maps

✅ **Technical Integration** - For "how do modules connect" questions
- "What are the dependencies?" → Reference ARCHITECTURE's dependency chain (Module 1 → 2 → 3 → 4/5 → 6)
- "How do npm scripts work?" → Reference ARCHITECTURE's npm integration examples
- "What's the deployment sequence?" → Reference ARCHITECTURE's 4-phase roadmap

✅ **Constitutional Mapping** - For "which consciousness dimension" questions
- "Which Neuro-Box 6D dimension does this module activate?" → Reference ARCHITECTURE's consciousness mappings
- Example: Module 1 (geo-strategy-architect) → RIGHT-SMART + SAFE-BOTTOM

#### **What to Extract From It**:
- **Module 1-6 Specifications**:
  - Skill IDs (geo-strategy-architect-v1.0, bofu-query-researcher-v1.0, etc.)
  - Function summaries (one-line descriptions)
  - Dependencies (primary, secondary)
  - Key outputs (what each module produces)
  - Knowledge Blocks required (KB-GEO-STRATEGY-FRAMEWORK-v1.0, etc.)

- **Knowledge Block XML Structure**:
  - Template following Meta Ads pattern
  - Constitutional compliance audit format
  - Consciousness profile mapping

- **npm Scripts Integration**:
  ```json
  {
    "scripts": {
      "geo:strategy": "node scripts/geo-strategy-architect.js",
      "geo:research": "node scripts/bofu-query-researcher.js",
      // etc.
    }
  }
  ```

- **Deployment Sequence**:
  - Phase 1: Foundation (Weeks 1-2) → Module 1
  - Phase 2: Research (Weeks 3-4) → Module 2
  - Phase 3: Content (Weeks 5-8) → Modules 3, 4, 5
  - Phase 4: Infrastructure (Weeks 9-12) → Module 6

#### **How to Reference It**:
```
"Reference AI-GEO-SKILL-MODULE-ARCHITECTURE for technical specifications of Modules 1-6:
- Use direct Noun-Verb naming (geo-strategy-architect, not KB-GEO-STRATEGY)
- Follow Knowledge Block XML structure (metadata, constitutional_compliance, dependencies, frameworks, heuristics, patterns)
- Map each module to Neuro-Box 6D dimensions as specified
- Maintain dependency chain (Module 1 feeds Module 2, Module 2 feeds Module 3, etc.)

Include npm scripts and deployment sequence in Deliverable 5 (README)."
```

---

### **Document 4: MODULE-7-AI-SEO-SITE-AUDITOR-ANALYST.md** (Client Discovery - 29KB)
**What It Is**: Complete audit module for client acquisition
**Primary Author**: Claude (me)
**Voice**: Sales-oriented, diagnostic, revenue-focused

#### **When to Reference**:
✅ **Client Discovery** - For "how to close deals" questions
- "How do we demonstrate value before engagement?" → Reference MODULE-7's audit methodology
- "What should a discovery call look like?" → Reference MODULE-7's client interview script
- "How do we position against competitors?" → Reference MODULE-7's competitive intelligence frameworks

✅ **Audit Components** - For "what to analyze" questions
- "What's a BOFU Gap Analysis?" → Reference MODULE-7's detailed framework (revenue opportunity quantification)
- "How do I map topical authority?" → Reference MODULE-7's coverage % methodology
- "What's a Niche Interest Tree?" → Reference MODULE-7's adjacent/emerging/dominated niche classification

✅ **Value Demonstration** - For "how to show ROI" questions
- "How do we calculate revenue opportunity?" → Reference MODULE-7's estimation formulas
- "What metrics matter for audits?" → Reference MODULE-7's Site Authority Scorecard (0-100 scoring)
- "How do we create urgency without manipulation?" → Reference MODULE-7's ethical framing (data-driven, not fear-based)

#### **What to Extract From It**:
- **6 Audit Analysis Frameworks**:
  1. BOFU Gap Analysis (missing high-intent queries, revenue opportunity)
  2. Topical Authority Mapping (coverage %, missing branches)
  3. Niche Interest Tree (adjacent, emerging, dominated niches)
  4. Emerging Trend Detection (growth rate, opportunity window)
  5. Competitor Direction Analysis (where they're investing)
  6. Site Authority Scorecard (6 categories, 0-100 score)

- **Client Interview Scripts**:
  - Discovery call flow (Problem Framing → Audit Preview → Objection Handling → Close)
  - Value demo examples (show anonymized audit, explain findings)
  - Objection responses ("We already have an SEO agency", "No budget for SEO")

- **Pricing Strategies**:
  - Option 1: Free audit (lead gen, close retainer)
  - Option 2: Paid standalone ($2,500-$7,500, credit toward retainer)
  - Option 3: Quarterly audit (retainer add-on, track progress)

- **Integration Points**:
  - How Module 7 creates demand for Modules 1-6
  - Example: "BOFU gaps identified → Recommend Module 2 + Module 3"

#### **How to Reference It**:
```
"Reference MODULE-7-AI-SEO-SITE-AUDITOR-ANALYST for the complete client discovery system:
- Use the 6 audit frameworks (BOFU Gap, Topical Authority, Niche Interest Tree, Emerging Trends, Competitor Direction, Site Scorecard)
- Include client interview scripts in Module 7 blueprint
- Explain how audit findings lead to recommendations for Modules 1-6
- Emphasize revenue-focused positioning (not technical jargon)

This is Module 7, the client acquisition engine that drives demand for production modules (1-6)."
```

---

### **Document 5: README-IMPLEMENTATION-GUIDE.md** (Workflow Guide - 11KB)
**What It Is**: Quick start instructions and troubleshooting
**Primary Author**: Claude (me)
**Voice**: Practical, step-by-step, user-friendly

#### **When to Reference**:
✅ **Quick Start** - For "how do I get started" questions
- "What's the NotebookLM → Claude workflow?" → Reference README's Step 1-6 process
- "What sources do I upload?" → Reference README's source categories (Market, Authority, Strategy, Competitor)
- "What prompt do I use?" → Reference README's NotebookLM prompt template

✅ **Troubleshooting** - For "what if X doesn't work" questions
- "NotebookLM output is too generic" → Reference README's fix (add more Market Language sources)
- "Claude generates overclaimed content" → Reference README's fix (use Proof Toolkit)
- "FAQ/SHAQ sounds like jargon" → Reference README's fix (use verbatim customer quotes)

✅ **Measurement** - For "what should I track" questions
- "What metrics matter most?" → Reference README's Tier 1 metrics (BOFU conversions, topical authority coverage)
- "What should I ignore?" → Reference README's Tier 3 metrics (total traffic, bounce rate, time on page)

#### **What to Extract From It**:
- **NotebookLM Workflow** (6 steps):
  1. Upload sources (30-50 total: 4 framework docs + 25-50 market/authority/strategy/competitor)
  2. Prompt NotebookLM (use provided template)
  3. Export compendium (5 deliverables as markdown)
  4. Feed to Claude (paste compendium, request KB generation)
  5. Iterate through modules (build 7 modules with ~28 KBs total)
  6. Test pipeline (npm scripts, validate outputs)

- **Troubleshooting Guide**:
  - Issue: Generic output → Fix: Add market language sources
  - Issue: Overclaimed content → Fix: Reference Proof Toolkit
  - Issue: Skills feel rigid → Fix: Emphasize autonomy principle
  - Issue: FAQ sounds like jargon → Fix: Use verbatim quotes
  - Issue: BOFU queries are informational → Fix: Re-audit for commercial intent

- **Measurement Framework**:
  - Tier 1 (Most Important): BOFU conversions, topical authority coverage, AI Overview appearances, lead magnet downloads
  - Tier 2 (Context): YouTube watch time, cohort conversion rates, brand search volume
  - Tier 3 (Ignore): Total traffic, bounce rate, time on page (broken in AI Mode era)

- **Next Actions Checklist**:
  - [ ] Gather sources
  - [ ] Upload to NotebookLM
  - [ ] Generate compendium
  - [ ] Feed to Claude
  - [ ] Build skills
  - [ ] Test pipeline
  - [ ] Deploy

#### **How to Reference It**:
```
"Reference README-IMPLEMENTATION-GUIDE for practical deployment instructions:
- Follow the 6-step NotebookLM → Claude workflow
- Use troubleshooting fixes for common issues (generic output, overclaimed content, rigid skills)
- Adopt measurement framework (Tier 1 metrics prioritized, Tier 3 ignored)
- Include Next Actions checklist in Deliverable 5 (Skill Formation README)

This document translates the other 4 framework docs into actionable steps."
```

---

## USAGE MATRIX: WHICH DOCUMENT FOR WHICH PURPOSE

| **Question Type** | **Primary Document** | **Supporting Documents** |
|-------------------|---------------------|--------------------------|
| **Strategic Direction** ("Should we focus on X?") | PRIMER (Doc 1) | META-PROMPT (Doc 2) for compliance checks |
| **Ethical Boundaries** ("Can we do X tactic?") | PRIMER (Doc 1) | META-PROMPT (Doc 2) for guardrails |
| **Structure & Format** ("How should X be organized?") | META-PROMPT (Doc 2) | ARCHITECTURE (Doc 3) for module structure |
| **Quality Standards** ("Is this good enough?") | META-PROMPT (Doc 2) | PRIMER (Doc 1) for strategic fit |
| **Module Design** ("How should this skill work?") | ARCHITECTURE (Doc 3) | META-PROMPT (Doc 2) for template |
| **Client Acquisition** ("How do we close deals?") | MODULE-7 (Doc 4) | PRIMER (Doc 1) for value positioning |
| **Audit Methodology** ("What should we analyze?") | MODULE-7 (Doc 4) | ARCHITECTURE (Doc 3) for integration |
| **Quick Start** ("How do I get started?") | README (Doc 5) | All others as reference |
| **Troubleshooting** ("What if X doesn't work?") | README (Doc 5) | Relevant doc based on issue |
| **Measurement** ("What should I track?") | README (Doc 5) | PRIMER (Doc 1) for philosophy |

---

## PROMPT TEMPLATE FOR NOTEBOOKLM

When uploading all 5 documents to NotebookLM, use this prompt:

```
I've uploaded 5 framework documents that form a complete system for AI GEO (Generative Engine Optimization):

1. AI-GEO-SUPER-SKILL-PRIMER.docx - My strategic vision and principles
2. NOTEBOOKLM-META-PROMPT-AI-GEO-COMPENDIUM-v1.0.md - Your instruction manual
3. AI-GEO-SKILL-MODULE-ARCHITECTURE.md - Technical specs for Modules 1-6
4. MODULE-7-AI-SEO-SITE-AUDITOR-ANALYST.md - Client discovery module
5. README-IMPLEMENTATION-GUIDE.md - Workflow guide

PLUS: I've uploaded 25-50 market/authority/strategy/competitor sources.

AND: I've uploaded NOTEBOOKLM-EXPANSION-PROMPT-v1.0.md which shows you EXACTLY how much depth and detail I need.

Please generate the complete AI GEO Knowledge Compendium using this guidance:

STRATEGIC DIRECTION → Reference PRIMER (Doc 1)
- Use the Guidance Ideas (emoji-tagged warnings) to inform strategic priorities
- Preserve the directive, urgent tone ("Stop buying links immediately")
- Extract DSA model (FAQ → SHAQ → HCTS → Whole Solution)

STRUCTURE & FORMAT → Reference META-PROMPT (Doc 2)
- Follow the 5 deliverable specifications exactly
- Use provided templates (FAQ → SHAQ table, 9-Block DSA, YAML patterns)
- Apply quality gates (AVE Standard, DSA Test, Proof Toolkit)

MODULE DESIGN → Reference ARCHITECTURE (Doc 3)
- Build all 7 modules (Modules 1-6 from ARCHITECTURE, Module 7 from MODULE-7 doc)
- Use direct Noun-Verb naming (geo-strategy-architect, not KB-GEO-STRATEGY)
- Include npm scripts, deployment sequence, Neuro-Box 6D mappings

CLIENT DISCOVERY → Reference MODULE-7 (Doc 4)
- Include all 6 audit frameworks (BOFU Gap, Topical Authority, etc.)
- Add client interview scripts and pricing strategies
- Explain how audit creates demand for Modules 1-6

WORKFLOW & MEASUREMENT → Reference README (Doc 5)
- Include troubleshooting guide in Deliverable 5
- Use Tier 1/2/3 measurement framework
- Add Next Actions checklist

DEPTH & DETAIL → Reference EXPANSION-PROMPT
- Expand each section to the level shown in EXPANSION-PROMPT examples
- Target: 230-290 pages when converted to PDF
- Include: Case studies, metrics, tactical steps, failure modes, success criteria for EVERYTHING

CONSTITUTIONAL COMPLIANCE → Check against ULTRAMIND v2.0
- Autonomy over Automation (frameworks, not rigid templates)
- Three-Layer Architecture (Directive → Orchestration → Execution)
- No Manipulation (honest claims, no fake urgency, no overclaiming)
- Proof Discipline (cite sources, use 5-tier claim hierarchy)

Output all 5 deliverables as separate markdown files ready for Claude to convert into 28 Knowledge Blocks (XML format).

Ready to generate?
```

---

## SUMMARY

**When in doubt, use this decision tree**:

1. **Question about "Why" or "What matters"?** → PRIMER (Doc 1)
2. **Question about "How to structure"?** → META-PROMPT (Doc 2)
3. **Question about "How modules work"?** → ARCHITECTURE (Doc 3)
4. **Question about "How to close clients"?** → MODULE-7 (Doc 4)
5. **Question about "How to get started"?** → README (Doc 5)

**All 5 documents work together**:
- PRIMER provides strategic north star
- META-PROMPT provides operational framework
- ARCHITECTURE provides technical blueprint
- MODULE-7 provides client acquisition system
- README provides practical deployment guide

**Upload all 5 to NotebookLM** to get the most comprehensive, aligned output.

# AI GEO Super-Skill Suite: Implementation Guide
## Quick Start for NotebookLM → Claude Pipeline

---

## WHAT YOU NOW HAVE

### 📄 3 Core Documents Created

1. **`NOTEBOOKLM-META-PROMPT-AI-GEO-COMPENDIUM-v1.0.md`**
   - Comprehensive meta prompt for NotebookLM
   - Tells NotebookLM exactly how to synthesize your sources
   - Produces 5 deliverables that Claude needs to build the skills
   - Length: ~15,000 words (designed for NotebookLM source upload)

2. **`AI-GEO-SKILL-MODULE-ARCHITECTURE.md`**
   - Technical architecture for the 6 skill modules
   - Naming conventions (direct Noun-Verb format)
   - Knowledge Block structure (XML templates)
   - Constitutional compliance mapping
   - Deployment sequence

3. **`README-IMPLEMENTATION-GUIDE.md`** (this file)
   - Quick start instructions
   - What to do next

---

## THE 7 MODULES YOU'RE BUILDING

**Using Direct Noun-Verb Naming** (not KB-prefixed):

### Core Production Modules (1-6)
1. **`geo-strategy-architect`** → Builds platform strategy + topic clusters + BOFU roadmap
2. **`bofu-query-researcher`** → Finds high-intent queries + extracts pain language + generates FAQ/SHAQ
3. **`whole-solution-writer`** → Creates DSA-compliant articles using 9-block framework
4. **`youtube-script-generator`** → Repurposes WSA content for video SEO
5. **`lead-magnet-creator`** → Builds conversion assets (templates, checklists, mini-courses)
6. **`geo-site-orchestrator`** → Manages programmatic pages + internal linking + schema

### Client Discovery Module (7)
7. **`ai-seo-site-auditor`** → Diagnoses BOFU gaps, topical authority coverage, emerging trends, competitor direction, niche opportunities + generates revenue-focused audit reports for client acquisition

Each module contains **3-6 Knowledge Blocks** (KB-prefixed XML files, following Meta Ads pattern).

---

## WORKFLOW: NotebookLM → Claude → Skills

### STEP 1: Upload Sources to NotebookLM

Create a new NotebookLM notebook called: **"AI GEO Super-Skill Compendium 2026"**

**Upload these sources** (use the naming convention):

#### Market Language Sources (5-10)
- `[Market] Reddit – AI Mode SEO – "Zero-click panic" – 2025`
- `[Market] Reddit – BOFU content strategy – "What converts" – 2025`
- `[Market] Amazon Reviews – SEO tools – Pain points – 2024`
- `[Market] YouTube Comments – AI SEO tutorials – Objections – 2025`

#### Authority Sources (3-8)
- `[Authority] Google Blog – AI Mode rollout – 2025-05-20`
- `[Authority] Schema.org – FAQPage documentation – 2025`
- `[Authority] YouTube Creator Academy – SEO best practices – 2024`

#### Strategy Sources (3-10)
- `[Strategy] Search Engine Land – HubSpot traffic drop – 2025-01-23`
- `[Strategy] Reuters – AI Mode tab announcement – 2025-03-05`
- `[Strategy] Yoast – Zero-click analytics – 2024`

#### Competitor Sources (3-10)
- `[Competitor] HubSpot – Blog strategy analysis – 2024`
- `[Competitor] Ahrefs – SEO content approach – 2025`
- `[Competitor] Semrush – Topical authority playbook – 2024`

**IMPORTANT**: Also upload the **`NOTEBOOKLM-META-PROMPT-AI-GEO-COMPENDIUM-v1.0.md`** file as a source!

This allows NotebookLM to reference the prompt structure while synthesizing.

---

### STEP 2: Prompt NotebookLM

Use this prompt in the NotebookLM notebook:

```
I've uploaded the NotebookLM Meta Prompt as one of the sources. Please follow
that prompt exactly to generate the AI GEO Knowledge Compendium.

Specifically, produce all 5 deliverables:

1. GEO Knowledge Compendium (Master Document)
   - Category Map
   - FAQ → SHAQ Ladder (30-50 entries)
   - Whole Solution Framework (9-block DSA template)
   - HCTS Library (40-60 Hacks/Cracks/Tracks/Stacks)
   - Authority & Proof Toolkit

2. Skill Module Blueprints (6 modules)
   - geo-strategy-architect
   - bofu-query-researcher
   - whole-solution-writer
   - youtube-script-generator
   - lead-magnet-creator
   - geo-site-orchestrator

3. Pattern Library YAML (30-50 tactical patterns)

4. Machine-Friendly Output Templates
   - WSA template
   - YouTube script template
   - Lead magnet landing page template
   - Programmatic GEO page template

5. Skill Formation Pack README

Follow the constitutional compliance checklist and use the voice/tone guidelines
from the meta prompt. Prioritize BOFU queries and avoid parasite SEO tactics.
```

---

### STEP 3: Export from NotebookLM

NotebookLM will generate the 5 deliverables as markdown.

**Copy each deliverable** into separate files:

1. `GEO-Knowledge-Compendium-Master.md`
2. `Skill-Module-Blueprints.md`
3. `Pattern-Library.yaml`
4. `Output-Templates.md`
5. `Skill-Formation-README.md`

Save these in: `C:\Users\cfar7\Desktop\ULTRAMIND\.claude\skills\aiseo\compendium\`

---

### STEP 4: Feed to Claude for Skill Building

**Create a new Claude conversation** with this prompt:

```
I have the AI GEO Knowledge Compendium from NotebookLM. I need you to build
6 agentic skill modules following the ULTRAMIND v2.0 constitutional framework.

Here are the 5 compendium deliverables:

[Paste GEO-Knowledge-Compendium-Master.md]

[Paste Skill-Module-Blueprints.md]

[Paste Pattern-Library.yaml]

[Paste Output-Templates.md]

[Paste Skill-Formation-README.md]

Please build the first module: geo-strategy-architect-v1.0

Create the following Knowledge Blocks in XML format (following the Meta Ads pattern):
1. KB-GEO-STRATEGY-FRAMEWORK-v1.0.xml
2. KB-BOFU-TARGETING-SYSTEM-v1.0.xml
3. KB-TOPICAL-AUTHORITY-MAPPING-v1.0.xml
4. KB-PLATFORM-OPPORTUNITY-SCORING-v1.0.xml

Each KB should include:
- Constitutional compliance audit
- Consciousness profile (Neuro-Box 6D mapping)
- Frameworks (strategic methodologies)
- Heuristics (tactical rules)
- Patterns (repeatable tactics)
- Compliance guardrails (critical warnings)

Use the compendium content to populate these blocks. Ensure all claims are cited
or labeled as hypothesis. Avoid manipulation tactics (fake scarcity, overclaiming).

Start with KB-GEO-STRATEGY-FRAMEWORK-v1.0.xml
```

Claude will then generate the XML knowledge blocks one by one.

---

### STEP 5: Iterate Through All 6 Modules

Repeat Step 4 for each module:

1. `geo-strategy-architect` (4 KBs)
2. `bofu-query-researcher` (4 KBs)
3. `whole-solution-writer` (5 KBs)
4. `youtube-script-generator` (3 KBs)
5. `lead-magnet-creator` (4 KBs)
6. `geo-site-orchestrator` (4 KBs)

**Total**: ~24 Knowledge Blocks

---

### STEP 6: Test the Pipeline

Once all modules are built, test the workflow:

```bash
# Install dependencies
npm install

# Run the full GEO pipeline
npm run geo:pipeline

# Or run modules individually
npm run geo:audit        # Runs site audit (Module 7 - client discovery)
npm run geo:strategy     # Generates topic clusters + BOFU queries
npm run geo:research     # Extracts pain language + FAQ/SHAQ
npm run geo:write        # Creates WSA content
npm run geo:video        # Generates YouTube scripts
npm run geo:magnet       # Builds lead magnets
npm run geo:site         # Manages programmatic pages
```

---

## KEY CONSTITUTIONAL COMPLIANCE POINTS

### ✅ What This System DOES
- Provides intelligent frameworks (not rigid templates)
- Uses real customer pain language (Reddit, reviews, forums)
- Prioritizes BOFU queries (high-intent, conversion-focused)
- Builds topical authority (comprehensive coverage)
- Cites all claims or labels as hypothesis
- Focuses on quality over volume (DSA standard)

### ❌ What This System AVOIDS
- **No Reddit parasite SEO** (unsustainable, Google will penalize)
- **No link buying** (Google will stop counting them)
- **No AI-generated listicles** (commoditized, low trust)
- **No fake scarcity or urgency** (manipulation tactics)
- **No guaranteed outcomes** (overclaiming)
- **No separate LLM optimization** (AI Mode pulls from top 10 traditional rankings)

---

## MEASUREMENT STRATEGY

### What to Track (Beyond GA4)

**Tier 1 Metrics** (Most Important):
- BOFU conversions (leads/sales from high-intent queries)
- Topical authority coverage (% of target queries ranking top 10)
- AI Overview appearances (via Google Search Console when available)
- Lead magnet download rate (proxy for content value)

**Tier 2 Metrics** (Context):
- YouTube watch time (engagement quality)
- Cohort conversion rates (which content paths convert best)
- Brand search volume (organic awareness)
- Reddit/forum mentions (unprompted brand awareness)

**Tier 3 Metrics** (Ignore):
- Total organic traffic (zero-click makes this unreliable)
- Bounce rate (doesn't correlate with conversions in AI Mode)
- Time on page (AI Mode users skim differently)

---

## TROUBLESHOOTING

### Issue: NotebookLM output is too generic
**Fix**: Add more Market Language sources (Reddit threads, Amazon reviews). The more specific pain language you provide, the better the output.

### Issue: Claude generates overclaimed content
**Fix**: Reference the Proof Toolkit section in the compendium. Use "observable trends" and "hypothesis" framing instead of guaranteed outcomes.

### Issue: Skills feel like rigid templates
**Fix**: Emphasize the "Autonomy over Automation" principle. Frameworks should guide intelligence, not prescribe exact steps.

### Issue: FAQ/SHAQ banks sound like marketer jargon
**Fix**: Use verbatim customer quotes from Reddit/forums. Preserve grammatical errors and informal language.

### Issue: BOFU queries are actually informational
**Fix**: Re-audit for commercial/transactional intent. Look for "vs", "alternative to", "pricing", "review" query patterns.

---

## NEXT ACTIONS

1. ✅ **Review the NotebookLM meta prompt** (`NOTEBOOKLM-META-PROMPT-AI-GEO-COMPENDIUM-v1.0.md`)
2. ⬜ **Gather sources**: Reddit threads, Google announcements, competitor content
3. ⬜ **Upload to NotebookLM**: Create notebook, upload sources + meta prompt
4. ⬜ **Generate compendium**: Prompt NotebookLM to produce 5 deliverables
5. ⬜ **Build skills with Claude**: Feed compendium to Claude, generate 24 Knowledge Blocks
6. ⬜ **Test pipeline**: Run npm scripts, validate outputs
7. ⬜ **Deploy to production**: Integrate with existing ULTRAMIND skill suite

---

## FILES CREATED

All files are in: `C:\Users\cfar7\Desktop\ULTRAMIND\.claude\skills\aiseo\`

1. ✅ `NOTEBOOKLM-META-PROMPT-AI-GEO-COMPENDIUM-v1.0.md` (15,000 words)
2. ✅ `AI-GEO-SKILL-MODULE-ARCHITECTURE.md` (technical specs)
3. ✅ `AI-GEO-SUPER-SKILL-PRIMER.docx` (your original primer)
4. ✅ `README-IMPLEMENTATION-GUIDE.md` (this file)

**Next**: Upload sources to NotebookLM and generate the compendium!

---

## CONSTITUTIONAL ALIGNMENT VERIFIED

This AI GEO Super-Skill Suite aligns with:
- ✅ ULTRAMIND Constitution v2.0
- ✅ Neuro-Box 6D consciousness mapping
- ✅ Three-Layer Architecture (Directive → Orchestration → Execution)
- ✅ AVE Standard (Authority / Value / Expertise)
- ✅ DSA Model (Deep Solutions Authority)
- ✅ Ethical execution (no manipulation, no overclaiming)

**Status**: Ready for NotebookLM synthesis → Claude skill building → Production deployment

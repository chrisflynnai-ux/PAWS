# SESSION 2: Build Module 2 - bofu-query-researcher

## 🎯 YOUR TASK FOR THIS SESSION

Build ONLY **Module 2: bofu-query-researcher**

Do NOT attempt other modules yet. Focus 100% on making this ONE module complete and detailed.

---

## MODULE 2 OVERVIEW

**Name**: bofu-query-researcher
**Purpose**: Discovers high-intent "money keywords" and builds deep query intelligence for conversion-focused content
**Type**: Research/Discovery (Intelligence Layer)
**Dependencies**: Module 1 (receives Platform Matrix and BOFU keyword list)

---

## WHAT TO PRODUCE (30-40 pages total for this module)

### 1. Module Blueprint (12-15 pages)

#### A. Purpose & Strategic Context (1-2 pages)
- **What problem does this solve?** Most content fails because it targets informational queries ("What is SEO?") that AI Mode answers instantly with zero clicks. This module identifies the **commercial intent queries** where users still need to click, compare, and convert.
- **Strategic Role:** The "Intelligence Officer." Module 1 (Strategy) tells you to target BOFU. Module 2 (Research) finds the exact questions high-intent buyers are asking.
- **Key Output:** A prioritized list of 50-100 "Money Keywords" with search intent analysis, competitive difficulty, and AI Mode risk assessment.

#### B. Inputs Required (2 pages)
List everything this module needs to start:
- **From Module 1:** Platform Priority List, Initial BOFU Keyword Seed List (from Commercial Intent Filter)
- **Client Inputs:**
  - Competitor URLs (3-5 direct competitors)
  - Product/Service details (What are we selling? What's the unique mechanism?)
  - Current GSC export (optional but recommended for quick wins)
  - Target audience persona (Job title, pain points, budget level)
- **Tools Required:**
  - GSC (Google Search Console) or Ahrefs/Semrush for keyword data
  - Perplexity or ChatGPT for intent analysis
  - Reddit/Quora for pain point mining
  - SE Ranking or similar for AI Overview tracking

#### C. Outputs Produced (2 pages)
What this module delivers:
1. **BOFU Keyword Master List** (50-100 queries) with columns:
   - Keyword
   - Search Volume
   - Commercial Intent Score (1-10)
   - AI Mode Risk (Does AI Overview appear? Yes/No)
   - Competitive Difficulty
   - Revenue Potential (High/Med/Low)
   - Recommended Content Type (WSA, Video, Tool, etc.)

2. **Query Intent Map:** Groups keywords by buyer stage:
   - Problem Aware ("How to fix [X]")
   - Solution Aware ("Best tools for [X]")
   - Product Aware ("[Product A] vs [Product B]")
   - Purchase Ready ("Pricing," "Demo," "Audit")

3. **Pain Point Library:** 20-30 verbatim user questions from Reddit/Quora that expose real frustrations

4. **Competitive Gap Report:** What queries competitors rank for that we don't (our blind spots)

#### D. Step-by-Step Workflow (4-5 pages)

**Phase 1: Seed Keyword Expansion (Day 1-2)**
- **Step 1.1:** Take the BOFU seed list from Module 1 (e.g., "AI SEO tools," "SEO agency pricing")
- **Step 1.2:** Feed each seed into Ahrefs "Related Keywords" or Semrush "Keyword Magic Tool"
  - *Action:* Filter by "Questions" and "Commercial" modifiers (best, vs, review, pricing, etc.)
- **Step 1.3:** Export 200-300 raw keywords
- **Output:** Raw keyword dump (unfiltered)

**Phase 2: Commercial Intent Filtering (Day 2-3)**
- **Step 2.1:** Apply the **p_bofu_regex_filter** pattern:
  - Regex: `(best|review|vs|alternative|pricing|cost|comparison|demo|audit|software|tool|service|agency|consultant|hire)`
- **Step 2.2:** Delete any keyword that is purely informational:
  - ❌ "What is SEO?" → AI Mode answers this instantly
  - ✅ "Best SEO tools for SaaS startups" → User needs comparison, likely to click
- **Step 2.3:** Manually score each keyword 1-10 for "Wallet Proximity"
  - 1-3: Informational (delete)
  - 4-6: Consideration (keep for nurture content)
  - 7-10: High Intent (prioritize)
- **Output:** Filtered list of 100-150 keywords with intent scores

**Phase 3: AI Mode Risk Assessment (Day 3)**
- **Step 3.1:** For each keyword, manually Google it
- **Step 3.2:** Check: Does an "AI Overview" appear?
  - If YES: Mark as "High AI Risk" → Strategy must shift to **Citation Optimization** (use data tables, original research, Schema markup)
  - If NO: Mark as "Traditional SEO Safe"
- **Step 3.3:** Use SE Ranking or similar to track AI Overview frequency over time
- **Output:** AI Risk column added to keyword list

**Phase 4: Pain Point Mining (Day 4-5)**
- **Step 4.1:** Take top 20 keywords and search them on:
  - Reddit (subreddit search)
  - Quora
  - Twitter/X (search tab)
  - LinkedIn (post search)
- **Step 4.2:** Copy verbatim questions/complaints:
  - Example: "I've tried 5 SEO agencies and they all just spam low-quality backlinks. How do I find one that actually understands SaaS?"
- **Step 4.3:** Tag each pain point with:
  - Persona (e.g., "Frustrated SaaS Founder")
  - Stage (Problem Aware vs Solution Aware)
  - Emotion (Anger, Fear, Confusion)
- **Output:** Pain Point Library (20-30 entries)

**Phase 5: Competitive Gap Analysis (Day 5-6)**
- **Step 5.1:** Take competitor URLs and run through Ahrefs "Site Explorer"
- **Step 5.2:** Export their top 50 ranking keywords
- **Step 5.3:** Identify:
  - Keywords they rank for that we don't (our gaps)
  - Keywords where we outrank them (our strengths)
  - Keywords where they have AI Overviews and we don't (citation opportunities)
- **Output:** Gap Report with action items

**Phase 6: Prioritization & Roadmap (Day 6-7)**
- **Step 6.1:** Score each keyword using the **MMA Framework:**
  - **Money:** Revenue potential (Does this query indicate budget?)
  - **Movement:** Ease of ranking (Low competition = faster wins)
  - **Authority:** Does ranking here build topical authority?
- **Step 6.2:** Sort by MMA score (highest first)
- **Step 6.3:** Map to content types:
  - High MMA + Video-friendly → Module 4 (YouTube)
  - High MMA + Comparison → Module 3 (WSA)
  - High MMA + Tool/Calculator → Module 5 (Lead Magnet)
- **Output:** Prioritized BOFU Keyword Master List

#### E. Quality Checks (1-2 pages)
Before finalizing the keyword list, verify:
- [ ] **The "Wallet" Test:** Do the keywords imply the user has purchasing intent? (e.g., "pricing," "demo," "vs," "best")
- [ ] **The "Zero-Click" Filter:** Have we removed all keywords where AI Mode provides a complete answer? (e.g., definitions, simple how-to's)
- [ ] **The "Volume" Reality Check:** Are we chasing 100k/month broad terms or focusing on 500/month long-tail terms that convert 10x better?
- [ ] **The "Platform Alignment" Check:** Do the keywords match the Platform Matrix from Module 1? (e.g., if YouTube is primary, do we have video-friendly queries?)
- [ ] **The "Pain Language" Check:** Do the keywords use the exact phrases found in Reddit/Quora pain points?

#### F. Failure Modes (2-3 pages)

**Failure Mode 1: The "Vanity Metric" Trap**
- **Symptom:** Targeting keywords with 50k+ monthly searches but zero commercial intent
- **Example:** "SEO guide" (informational) vs "SEO agency for SaaS" (commercial)
- **Why it fails:** AI Mode answers broad queries instantly. Users don't click.
- **Fix:** Delete any keyword without a commercial modifier. Volume is a vanity metric in the AI era.

**Failure Mode 2: The "Keyword Stuffing" Relic**
- **Symptom:** Creating separate pages for "SEO services," "SEO agency," "SEO company" (all the same intent)
- **Why it fails:** Google and LLMs understand semantic similarity. This is seen as thin content.
- **Fix:** Cluster semantically identical keywords into ONE target URL. Use variations naturally in the content.

**Failure Mode 3: The "Reddit Spam" Illusion**
- **Symptom:** Seeing "reddit.com" rank for target keywords and thinking, "I should just post there!"
- **Why it fails:** Google's spam filters now detect commercial accounts. Reddit shadowbans are instant.
- **Fix:** Use Reddit for RESEARCH (pain mining), not distribution. Build authority on owned/safer platforms (YouTube, LinkedIn).

**Failure Mode 4: Ignoring "Adjacent Queries"**
- **Symptom:** Only targeting exact-match keywords (e.g., "SEO tools") and missing related high-intent queries (e.g., "content optimization software")
- **Why it fails:** LLMs pull from broad semantic clusters. If you only cover one angle, you lose citations.
- **Fix:** Use the "Also Ask" section in Google and Perplexity's "Related" tab to find adjacent queries.

#### G. Success Metrics (1-2 pages)
How to know this module succeeded:
1. **Keyword List Quality:**
   - 80%+ of keywords have commercial modifiers
   - Average "Wallet Proximity" score ≥ 7/10
   - <20% of keywords trigger AI Overviews (low AI risk)

2. **Pain Point Coverage:**
   - Every major customer pain from sales calls is reflected in the Pain Point Library
   - Keywords use customer language (not corporate jargon)

3. **Competitive Intelligence:**
   - Gap Report reveals 10+ "easy win" keywords (low competition, medium volume)
   - We've identified competitor blind spots (topics they don't cover)

4. **Downstream Impact:**
   - Module 3 (Writer) can map every keyword to a specific content piece
   - Module 4 (YouTube) has a clear video roadmap
   - Module 5 (Lead Magnet) knows which tools/calculators to build

#### H. Integration with Other Modules (1 page)
- **From Module 1 (Strategy):** Receives Platform Matrix, initial BOFU seed list, Topic Cluster map
- **To Module 3 (Writer):** Sends prioritized BOFU Keyword Master List + Pain Point Library
- **To Module 4 (YouTube):** Sends video-friendly keywords (how-to, vs, demo, etc.)
- **To Module 5 (Lead Magnet):** Sends "tool" or "calculator" keyword opportunities
- **To Module 6 (Orchestrator):** Sends content calendar (which keywords to tackle first)
- **To Module 7 (Auditor):** Sends competitive Gap Report (what's missing on the site)

#### I. Automation Opportunities (1 page)
What can be automated vs what needs human judgment:
- **Automate:**
  - Keyword exports from Ahrefs/Semrush
  - Regex filtering for commercial intent
  - AI Overview detection (using SE Ranking API)
  - Competitor keyword scraping
- **Human Judgment Required:**
  - "Wallet Proximity" scoring (requires understanding buyer psychology)
  - Pain Point tagging (emotion, persona, stage)
  - Final prioritization (MMA scoring involves strategic trade-offs)
  - Platform-to-keyword mapping (requires understanding content strengths)

---

### 2. Knowledge Blocks Required (15-20 pages)

Create **4 Knowledge Blocks** at 4-5 pages each:

#### KB-BOFU-QUERY-INTELLIGENCE-v1.0 (5-6 pages)

**What it contains:**
- Commercial Intent Taxonomy (12+ commercial modifiers beyond "best" and "vs")
  - Comparison: vs, versus, alternative, compared to, instead of
  - Evaluation: review, rating, pros and cons, worth it
  - Purchase: pricing, cost, demo, trial, buy, hire
  - Implementation: how to use, setup, install, integrate
  - Problem-solving: fix, troubleshoot, not working, error
- Buyer Stage Mapping (4 stages with keyword examples for each)
  - Problem Aware: "How to [solve X]"
  - Solution Aware: "Best [category] for [use case]"
  - Product Aware: "[Brand A] vs [Brand B]"
  - Purchase Ready: "Pricing," "Demo," "Audit"
- AI Mode Risk Indicators (when to expect AI Overviews)
  - Definitional queries ("What is X?")
  - Simple how-to's ("How to tie a tie")
  - Listicles ("Top 10 X")
  - Calculations ("15% of 200")

**When to reference:** Every time you filter keywords for commercial intent or assess AI risk

**Example application:**
```
Query: "Ahrefs vs Semrush for SaaS startups"
- Commercial Modifier: "vs" (Comparison)
- Buyer Stage: Product Aware (comparing specific tools)
- AI Mode Risk: Medium (AI might summarize, but user needs depth)
- Strategy: Create deep comparison WSA (Module 3) + Video (Module 4)
```

#### KB-PAIN-POINT-MINING-v1.0 (4-5 pages)

**What it contains:**
- Where to Find Real Pain (platform-specific strategies)
  - Reddit: Search `site:reddit.com [keyword] "frustrated" OR "problem" OR "doesn't work"`
  - Quora: Use "Followed Questions" to find active pain threads
  - Twitter/X: Advanced search for complaints (`[keyword] min_faves:50`)
  - Review sites (G2, Capterra): Filter 1-3 star reviews
- How to Tag Pain Points (3-dimensional framework)
  - Persona (job title, company size)
  - Emotion (anger, fear, confusion, urgency)
  - Stage (unaware, problem aware, solution aware)
- Pain-to-Keyword Translation (turning complaints into search queries)
  - Pain: "Our agency keeps building links that get us penalized"
  - Keyword: "White hat link building services," "Safe backlink strategies for SaaS"
- The "Verbatim Rule:" Always capture exact user language (don't paraphrase)

**When to reference:** When mining Reddit/Quora for query ideas and content angles

**Example application:**
```
Reddit Post: "I hired 3 SEO freelancers from Upwork and they all just spammed my site with garbage blog posts. How do I find someone who actually knows B2B?"

Tags:
- Persona: B2B SaaS Founder, burned by bad agencies
- Emotion: Frustration + Distrust
- Stage: Solution Aware (knows they need SEO, doesn't trust providers)

Keyword Opportunities:
- "B2B SEO agency reviews"
- "How to vet an SEO agency"
- "SEO for SaaS vs ecommerce"
```

#### KB-COMPETITIVE-INTELLIGENCE-v1.0 (4-5 pages)

**What it contains:**
- Gap Analysis Framework (4 types of gaps)
  - **Content Gaps:** Topics they cover, we don't
  - **Keyword Gaps:** Queries they rank for, we don't
  - **Authority Gaps:** Backlinks/mentions they have, we don't
  - **Platform Gaps:** Channels they dominate (YouTube, LinkedIn), we don't
- How to Extract Competitor Keywords (tool-specific workflows)
  - Ahrefs Site Explorer → Organic Keywords → Filter by Position 1-10
  - Semrush Keyword Gap Tool → Enter 3 competitors → Find "Missing" keywords
  - AlsoAsked.com → Enter competitor URL → See question hierarchy
- The "Steal and Improve" Strategy
  - Find their top-ranking page
  - Identify why it ranks (backlinks? depth? schema? video?)
  - Build a better version (more data, better visuals, updated info)
- Competitive Entity Analysis (Knowledge Graph comparison)
  - Search "[Competitor Name]" in Perplexity
  - If Perplexity gives detailed bio → they have strong entity signals
  - If Perplexity says "No specific information" → weak entity (opportunity)

**When to reference:** When identifying which keywords to target and how to differentiate

**Example application:**
```
Competitor: Backlinko (Brian Dean's site)

Analysis:
- Top Keyword: "SEO techniques" (Position 1, 12k searches/mo)
- Why it ranks: 15k-word guide, 200+ backlinks, embedded video, updated 2025
- Our Gap: We have zero content on "SEO techniques"
- Our Opportunity: Create an AI-era version ("SEO techniques for 2026: Post-AI Mode")
- Differentiation: Add live data (our own GSC case study), video interview with agency owner
```

#### KB-MMA-PRIORITIZATION-v1.0 (4-5 pages)

**What it contains:**
- The MMA Scoring Framework (how to rank keywords)
  - **Money (1-10):** Does this query indicate budget?
    - 1-3: Informational ("What is X?")
    - 4-6: Consideration ("Best X")
    - 7-10: Purchase intent ("Pricing," "Demo," "vs [specific product]")
  - **Movement (1-10):** How fast can we rank?
    - 1-3: Dominated by huge brands (Ahrefs, HubSpot)
    - 4-6: Mixed results (opportunity for authority sites)
    - 7-10: Low competition (new query, niche long-tail)
  - **Authority (1-10):** Does ranking here build topical power?
    - 1-3: Tangentially related (avoid unless high Money)
    - 4-6: Related but not core (nice-to-have)
    - 7-10: Core to brand positioning (must-rank)
- How to Calculate Total MMA Score
  - Formula: `(Money × 2) + Movement + Authority = Max 50 points`
  - Why Money is weighted 2x: Revenue > Speed > Authority
- The "Quick Win" Filter (Movement ≥7, Money ≥5)
  - These are low-competition, commercial queries
  - Target these first for early momentum
- The "Authority Play" (Authority ≥8, Money ≥4)
  - These build long-term topical dominance
  - Worth investing in even if slow to rank

**When to reference:** Final prioritization phase of Module 2 workflow

**Example application:**
```
Keyword: "AI SEO tools for SaaS startups"
- Money: 8/10 (specific use case + "tools" implies buying)
- Movement: 7/10 (medium competition, new query)
- Authority: 9/10 (core to our positioning)
- Total MMA: (8×2) + 7 + 9 = 32/50 → HIGH PRIORITY

Keyword: "What is SEO?"
- Money: 2/10 (pure education)
- Movement: 1/10 (dominated by Wikipedia, Moz, etc.)
- Authority: 3/10 (not unique to our expertise)
- Total MMA: (2×2) + 1 + 3 = 8/50 → DELETE
```

---

### 3. Patterns for This Module (3-5 pages)

Create **8-10 tactical patterns** in YAML format:

```yaml
patterns:
  - pattern_id: "p_bofu_regex_filter"
    name: "Commercial Intent Regex Filter"
    category: "research"
    when_to_use: "Module 2 - Phase 2 (Filtering raw keyword exports)"
    structure: "Regex: (best|review|vs|alternative|pricing|cost|comparison|demo|audit|software|tool|service|agency|consultant|hire)"
    mma_impact: "High - Eliminates 60-80% of waste traffic"
    example_context: "Apply in Ahrefs/Semrush export or GSC data to isolate money keywords"

  - pattern_id: "p_ai_overview_detector"
    name: "AI Mode Risk Assessment"
    category: "research"
    when_to_use: "Module 2 - Phase 3 (Checking if keywords are AI-safe)"
    structure: "Manually Google keyword → Check for AI Overview → Tag as High/Medium/Low Risk"
    mma_impact: "High - Prevents investing in zero-click keywords"
    example_context: "If AI Overview appears, shift strategy to citation optimization (data tables, Schema)"

  - pattern_id: "p_reddit_pain_mining"
    name: "Reddit Pain Point Extraction"
    category: "research"
    when_to_use: "Module 2 - Phase 4 (Finding real customer language)"
    structure: "Search: site:reddit.com [keyword] (frustrated OR problem OR 'doesn't work' OR failure)"
    mma_impact: "Medium - Uncovers angles competitors miss"
    example_context: "Use verbatim quotes in content to match search intent perfectly"

  - pattern_id: "p_competitive_gap_finder"
    name: "Ahrefs Keyword Gap Analysis"
    category: "research"
    when_to_use: "Module 2 - Phase 5 (Identifying blind spots)"
    structure: "Ahrefs Site Explorer → Enter competitor URL → Organic Keywords → Filter Position 1-10 → Export → Compare to our rankings"
    mma_impact: "High - Reveals easy wins (they rank, we don't)"
    example_context: "Prioritize gaps where competitor has low DR (we can outrank fast)"

  - pattern_id: "p_mma_scoring_formula"
    name: "MMA Keyword Prioritization"
    category: "prioritization"
    when_to_use: "Module 2 - Phase 6 (Final ranking of keywords)"
    structure: "(Money × 2) + Movement + Authority = Total Score (Max 50)"
    mma_impact: "Critical - Ensures we chase revenue, not vanity metrics"
    example_context: "Sort keyword list by MMA score, tackle top 20 first"

  - pattern_id: "p_buyer_stage_mapping"
    name: "Query Intent Categorization"
    category: "research"
    when_to_use: "Module 2 - Phase 2 (Understanding user mindset)"
    structure: "Tag each keyword: Problem Aware / Solution Aware / Product Aware / Purchase Ready"
    mma_impact: "Medium - Informs content angle and CTA strategy"
    example_context: "Problem Aware → Educational content, Solution Aware → Comparison, Purchase Ready → Pricing page"

  - pattern_id: "p_also_asked_expander"
    name: "Google 'People Also Ask' Harvester"
    category: "research"
    when_to_use: "Module 2 - Phase 1 (Seed expansion)"
    structure: "Google target keyword → Expand all 'People Also Ask' boxes → Copy questions → Feed into Ahrefs for volume data"
    mma_impact: "Medium - Finds related long-tail queries"
    example_context: "Use to build comprehensive topic clusters"

  - pattern_id: "p_perplexity_intent_analyzer"
    name: "Perplexity Query Simulation"
    category: "research"
    when_to_use: "Module 2 - Phase 3 (Understanding AI Mode behavior)"
    structure: "Ask Perplexity the target query → Note which sources it cites → Check if we could be cited"
    mma_impact: "High - Shows what content type/depth is needed for AI citations"
    example_context: "If Perplexity cites data tables, we need original research to compete"

  - pattern_id: "p_quora_question_scraper"
    name: "Quora Pain Discovery"
    category: "research"
    when_to_use: "Module 2 - Phase 4 (Finding niche anxieties)"
    structure: "Search Quora for [keyword] → Filter by 'Most Viewed' → Copy top 10 questions → Tag by emotion"
    mma_impact: "Medium - Reveals hidden objections/fears"
    example_context: "Use in FAQ sections and ad copy to address specific doubts"

  - pattern_id: "p_wallet_proximity_test"
    name: "Commercial Intent Scoring (1-10)"
    category: "validation"
    when_to_use: "Module 2 - Phase 2 (Quality check)"
    structure: "Ask: 'Does this query imply the user has their wallet out?' 1-3 = No, 4-6 = Maybe, 7-10 = Yes"
    mma_impact: "Critical - Final filter before keyword approval"
    example_context: "Delete anything scoring <4 unless it's a necessary Hub page for topical authority"
```

---

### 4. Case Studies (3-5 pages)

Provide **2-3 detailed case studies** showing Module 2 in action:

#### Case Study 1: SaaS SEO Agency Keyword Research

**Context:**
- Client: B2B SaaS SEO agency (5-person team)
- Problem: Targeting broad terms like "SEO services" (100k searches/mo) but getting zero conversions
- Goal: Find high-intent BOFU queries that convert

**Module 2 Workflow Applied:**
1. **Phase 1 (Seed Expansion):**
   - Started with seed: "SaaS SEO"
   - Used Ahrefs "Related Keywords" → Found 450 variations
2. **Phase 2 (Commercial Filtering):**
   - Applied p_bofu_regex_filter → Reduced to 120 keywords
   - Manually scored Wallet Proximity → Kept 65 keywords (score ≥6)
3. **Phase 3 (AI Risk Assessment):**
   - Checked top 20 in Google → 8 had AI Overviews
   - Tagged those 8 as "Citation Strategy Required"
4. **Phase 4 (Pain Mining):**
   - Searched Reddit: `site:reddit.com "SaaS SEO" (frustrated OR problem)`
   - Found pain: "Every agency just builds spammy links. I need technical SEO for product pages."
   - Generated new keyword: "Technical SEO for SaaS product pages"
5. **Phase 5 (Competitive Gap):**
   - Analyzed top competitor (Ahrefs blog)
   - Gap found: They rank for "SaaS content strategy" (1.2k searches, Position 3)
   - We had zero content on this → Added to roadmap
6. **Phase 6 (MMA Prioritization):**
   - Top keyword: "SaaS SEO agency" (Money: 9, Movement: 6, Authority: 10) = 34/50
   - Quick win: "Technical SEO audit for SaaS" (Money: 8, Movement: 8, Authority: 7) = 31/50

**Results:**
- Delivered 65 prioritized BOFU keywords
- 12 "Quick Win" keywords (MMA ≥28, Movement ≥7)
- 15 pain points for content angles
- 8 competitive gaps identified

**Downstream Impact:**
- Module 3 (Writer) built 5 WSAs targeting top keywords
- Module 4 (YouTube) created video series on "Technical SEO for SaaS"
- Module 5 (Lead Magnet) built "SaaS SEO Audit Checklist"

---

#### Case Study 2: E-commerce Brand (Outdoor Gear)

**Context:**
- Client: E-commerce brand selling camping gear
- Problem: Competing with Amazon/REI on product terms ("camping tent")
- Goal: Find differentiated queries where smaller brands can win

**Module 2 Workflow Applied:**
1. **Phase 1 (Seed Expansion):**
   - Seed: "Camping gear"
   - Used Semrush Keyword Magic → Found 2,300 variations
2. **Phase 2 (Commercial Filtering):**
   - Applied regex + added e-commerce modifiers: (buy|shop|sale|review|best|cheap|discount)
   - Reduced to 340 keywords
   - Deleted generic product terms (too competitive) → Kept 180
3. **Phase 3 (AI Risk Assessment):**
   - Found that "Best camping tents" triggers AI Overview with product carousel
   - Strategy shift: Target niche use cases AI can't pre-answer
   - Example: "Best camping tent for tall people" (no AI Overview)
4. **Phase 4 (Pain Mining):**
   - Searched Reddit r/CampingGear
   - Pain: "I'm 6'5\" and every tent is too short. Recommendations?"
   - Generated keyword: "Camping tents for tall people"
   - Pain: "Tent poles keep breaking in wind. What's actually durable?"
   - Generated keyword: "Most durable camping tent poles"
5. **Phase 5 (Competitive Gap):**
   - Analyzed REI's blog
   - Gap: They have zero content on "Camping gear for plus-size hikers"
   - Opportunity: Underserved niche with commercial intent
6. **Phase 6 (MMA Prioritization):**
   - Top keyword: "Camping tent for tall people" (Money: 9, Movement: 8, Authority: 5) = 31/50
   - Authority play: "How to choose camping gear" (Money: 5, Movement: 4, Authority: 10) = 24/50 (kept for topical depth)

**Results:**
- Delivered 180 niche commercial keywords
- 25 underserved use cases (tall people, plus-size, disabilities)
- 30 pain points focused on product failures
- 10 competitive gaps (topics REI/Amazon don't cover)

**Downstream Impact:**
- Module 3 (Writer) built buying guides for niche segments
- Module 4 (YouTube) created gear review videos for underserved audiences
- Conversion rate increased 3x (targeting specific pain vs generic terms)

---

## DEPTH REQUIREMENTS

Remember from EXPECTATIONS-OVERVIEW:
- **Module Blueprint:** 10-12 pages (not 1 paragraph). Include detailed substeps, examples, and failure modes.
- **Knowledge Blocks:** 4-5 pages each (detailed frameworks with examples, not summaries).
- **Patterns:** Fully specified YAML with when_to_use, structure, and example_context.
- **Case Studies:** 1.5-2 pages each, showing real workflow application.

---

## STRATEGIC GUARDRAILS (from PRIMER)

- **BOFU Focus:** Every keyword must have commercial intent. Delete informational queries unless they're Hub pages for authority.
- **No Reddit Spam:** Use Reddit for research (pain mining), NOT distribution. Don't recommend posting links there.
- **AI Mode Reality:** Acknowledge that AI Overviews are killing click-through on informational queries. Focus on complex comparisons and niche use cases.
- **Voice Variations:** Use "Clinical" tone for frameworks, "Coach" tone for failure modes, "Founder" tone for case studies.
- **Proof Discipline:** Every claim needs a citation or example (e.g., "Reddit shadowbans commercial accounts" → Link to Reddit's spam policy).

---

## OUTPUT FOR THIS SESSION

Return **1 markdown file:**

**`MODULE-2-bofu-query-researcher-COMPLETE.md`** (30-40 pages)

Structure it exactly like Module 1:
1. GEO Knowledge Compendium: Research/Discovery Layer (Category Map, FAQ/SHAQ, HCTS)
2. Module 2 Blueprint (12-15 pages with A-I sections)
3. Pattern Library YAML (8-10 patterns)
4. Case Studies (2-3 detailed examples)
5. Output Templates (if applicable - e.g., BOFU Keyword Master List template)
6. README snippet (how to deploy Module 2)

---

## QUALITY CHECKS BEFORE SUBMITTING

- [ ] Blueprint includes ALL substeps (not just high-level phases)
- [ ] Each Knowledge Block is 4-5 pages with examples and when-to-reference notes
- [ ] Patterns are in valid YAML with all required fields
- [ ] Case studies show real decision points (not just summaries)
- [ ] No generic advice—everything is specific to BOFU research
- [ ] Strategic guardrails from PRIMER are reflected (BOFU focus, anti-Reddit-spam, AI Mode awareness)

---

## FILES TO REFERENCE

You have access to:
- **NOTEBOOKLM-EXPECTATIONS-OVERVIEW.md** (quality standards, depth requirements)
- **AI-GEO-SUPER-SKILL-PRIMER.docx** (strategic vision, BOFU focus, Reddit warnings)
- **AI-GEO-SKILL-MODULE-ARCHITECTURE.md** (technical specs for Module 2)
- **MODULE-1-geo-strategy-architect-COMPLETE.md** (for integration context)
- **50 video transcripts + source materials** (for real pain points, query examples, case study data)

Synthesize insights from ALL sources to build a comprehensive Module 2 knowledge compendium.

---

🎯 **YOUR MISSION:** Build the definitive BOFU query research guide that teaches an AI agent (or human SEO) how to find the exact keywords that drive revenue in 2026's AI-dominated search landscape.

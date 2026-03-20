Here is the **ULTRAMIND Knowledge Extraction** for **KB-CAMPAIGN-ARCHITECTURE**.

***

# A) SOURCE MAP

1.  **Sam Piliero** `[SRC: Sam Piliero | 190, 507, 638, 711]`
    *   *Key Topics:* M3 Swim Lane Architecture, Incremental Attribution, Cost Caps, Pack System.
    *   *Unique Contribution:* The "Swim Lane" philosophy separating Prospecting, Retargeting, and Retention to prevent budget misappropriation.
2.  **Professor Charley T** `[SRC: Professor Charley T | 95]`
    *   *Key Topics:* 3:2:2 Flexible Ads, Post ID Harvesting, Control vs. Test environments.
    *   *Unique Contribution:* The specific technical setup for 3:2:2 Flexible Ads and the methodology of "Harvesting" winning Post IDs.
3.  **Jared Robinson** `[SRC: Jared Robinson | 80, 480]`
    *   *Key Topics:* Broad CBO Prospecting, Creative Batches, Hook Banks.
    *   *Unique Contribution:* The strategy of using "Creative Batches" rather than individual ads to force diversity in CBO.
4.  **Dr. Matt Shiver** `[SRC: Dr. Matt Shiver | 50]`
    *   *Key Topics:* Scaling under $1M, Avatar targeting via creative, Two-Campaign Structure.
    *   *Unique Contribution:* Simplified structure for smaller accounts focusing on "One Avatar, Multiple Angles."
5.  **Chase Chappell** `[SRC: Chase Chappell | 249, 726]`
    *   *Key Topics:* 5x5 Testing Matrix, Conversion Velocity, Algorithmic Rhythm.
    *   *Unique Contribution:* The "5x5" testing methodology and the focus on "Conversion Velocity" over cheap clicks.
6.  **Ben Heath** `[SRC: Ben Heath | 571]`
    *   *Key Topics:* Budget distribution issues, forced testing.
    *   *Unique Contribution:* Solutions for when Meta allocates 100% of spend to a single creative (Separate Testing Campaigns).
7.  **Caden Thompson** `[SRC: Caden Thompson | 279]`
    *   *Key Topics:* Lead Gen Architecture, Lag Time optimization.
    *   *Unique Contribution:* Adjusting optimization events based on the "Lag Time" of the sales cycle (Top vs. Bottom funnel).
8.  **The Ecom King** `[SRC: THE ECOM KING | 370]`
    *   *Key Topics:* Andromeda updates, Angle-based Ad Sets.
    *   *Unique Contribution:* Transitioning from interest targeting to "Concept Targeting."

***

# B) TAXONOMY

*   **Core Philosophy:** **Andromeda** (Creative IS Targeting).
    *   *Consensus:* Manual targeting (Interests/Lookalikes) is largely obsolete or secondary. Broad targeting is the primary mechanism for scaling `[SRC: Dr. Matt Shiver | 53]`.
    *   *Divergence:* Some experts (Piliero) still suggest using "Interest Clusters" as a guide for new pixels before going fully broad `[SRC: Sam Piliero | 641]`.
*   **Architecture Models:**
    *   *M3 Swim Lanes:* Strict separation of New vs. Existing customers `[SRC: Sam Piliero | 510]`.
    *   *Two-Campaign System:* One for Testing (sandbox), one for Scaling (winners) `[SRC: Dr. Matt Shiver | 57]`.
    *   *One Campaign Method:* Consolidating everything into one CBO for maximum machine learning signal `[SRC: Jared Robinson | 84]`.
*   **Testing Mechanics:**
    *   *3:2:2:* (3 Creatives, 2 Headlines, 2 Texts) `[SRC: Professor Charley T | 96]`.
    *   *5x5:* (5 Creatives, 5 Headlines, 5 Texts) `[SRC: Chase Chappell | 728]`.
    *   *Dynamic/Flexible:* Allowing Meta to mix and match assets.

***

# C) FRAMEWORKS (8-15)

```yaml
frameworks:
  - name: "M3 Swim Lane Architecture"
    source_tag: "[SRC: Sam Piliero | 509-511]"
    key_quote: "We need to make sure the distribution of spend is mostly focused on our new audiences."
    summary: "A campaign structure that strictly separates New Customers (Prospecting), Engaged Audiences (Retargeting), and Existing Customers (Retention) to prevent ROAS inflation."
    when_to_use: "Accounts spending >$3k/month where blended ROAS hides poor new customer acquisition."
    when_not_to_use: "Brand new accounts with <50 conversions/week (consolidate instead)."
    steps:
      1. "Create 'Prospecting' CBO: Exclude 180-day Purchasers + 30-day Visitors."
      2. "Create 'Retargeting' CBO: Include 30-day Visitors/Engagers; Exclude 180-day Purchasers."
      3. "Create 'Retention' CBO: Include 180-day Purchasers."
    key_metrics: "ncROAS (New Customer ROAS), MER (Marketing Efficiency Ratio)."
    failure_modes: "Exclusion overlap failures causing prospecting to retarget hot leads."

  - name: "The 3:2:2 Flexible Ad System"
    source_tag: "[SRC: Professor Charley T | 95-96]"
    key_quote: "Three creatives, two headlines, two primary texts... We are not trying to give everything a fair chance."
    summary: "A specific ad-level testing structure designed to let Meta's AI determine the best combination of assets without fragmenting data."
    when_to_use: "Testing new creative concepts within a broad audience."
    steps:
      1. "Select 'Flexible Ad' format."
      2. "Upload 3 distinct visual creatives (all video OR all image)."
      3. "Write 2 distinct Primary Texts."
      4. "Write 2 distinct Headlines."
      5. "Launch in Broad Ad Set."
    key_metrics: "Spend Share (which asset gets the budget)."
    failure_modes: "Mixing formats (image + video) in one flex ad confuses the algorithm."

  - name: "The 'Pack' System (CBO Scaling)"
    source_tag: "[SRC: Sam Piliero | 508-509]"
    key_quote: "Every time you have a new creative... that gets grouped together in a new pack."
    summary: "Launching new creative batches as new Ad Sets within an existing Prospecting CBO, dated by launch."
    when_to_use: "High-volume creative testing environments."
    steps:
      1. "Create CBO Campaign."
      2. "Create Ad Set: 'Broad Pack [Date]'."
      3. "Load 3-6 new creatives into that Ad Set."
      4. "Launch. Do not pause old packs unless they fail metrics; let CBO reallocate spend."
    key_metrics: "Ad Set Spend, CPA."
    failure_modes: "Pausing packs too early before the algorithm stabilizes (give 7 days)."

  - name: "Post ID Harvesting"
    source_tag: "[SRC: Professor Charley T | 103-105]"
    key_quote: "You've isolated the unicorn... and you've added it to your all-star team."
    summary: "Moving a winning ad from a testing environment to a scaling environment by copying its Post ID to retain social proof."
    when_to_use: "When a test ad shows high spend and low CPA/high ROAS."
    steps:
      1. "Identify winner in Flexible Ad/Test Campaign."
      2. "Filter by 'Facebook Posts with Comments' to find the Post ID."
      3. "Copy Post ID."
      4. "Create new ad in 'Control/Scaling' Ad Set -> 'Use Existing Post'."
    key_metrics: "Social Proof (Likes/Comments), ROAS."
    failure_modes: "Turning off the original test ad too soon (can kill the momentum)."

  - name: "Ad Set Spending Limits (Forced Testing)"
    source_tag: "[SRC: Sam Piliero | 654]"
    key_quote: "Set your daily minimum to one time your target cost per acquisition."
    summary: "Using 'Ad Set Spend Limits' (Min/Max) within a CBO to force the algorithm to test new creative packs that would otherwise get zero budget."
    when_to_use: "When launching new creative packs in a CBO dominated by an existing winner."
    steps:
      1. "Go to Ad Set settings -> Budget & Schedule."
      2. "Set Daily Minimum to 1x Target CPA (e.g., $50)."
      3. "Run for max 7 days."
      4. "Remove limit if it performs; pause if it fails."
    key_metrics: "Spend, CPA."
    failure_modes: "Leaving the minimum limit on indefinitely for bad ads."

  - name: "5x5 Testing Matrix"
    source_tag: "[SRC: Chase Chappell | 728-737]"
    key_quote: "Five unique ad copy... five unique headlines... five unique creatives."
    summary: "A high-volume testing structure to feed the algorithm maximum variety in a single ad set."
    when_to_use: "Initial account launch or major quarterly resets."
    steps:
      1. "Create 5 distinct creatives (Video, Static, Carousel, etc.)."
      2. "Write 5 distinct primary texts (Long, Short, Review, Feature, Story)."
      3. "Write 5 distinct headlines."
      4. "Launch in one ad set."
    key_metrics: "Conversion Velocity."
    failure_modes: "Using similar variations instead of distinct concepts."

  - name: "Lead Gen Lag-Time Optimization"
    source_tag: "[SRC: Caden Thompson | 289-291]"
    key_quote: "If we wait all the way to the end point we have a massive gap in between."
    summary: "Adjusting the optimization event based on the sales cycle length to ensure the pixel gets data within the 7-day window."
    when_to_use: "High-ticket B2B or Service businesses with sales cycles >7 days."
    steps:
      1. "Determine Lag Time (Lead to Sale)."
      2. "IF <7 days: Optimize for Bottom of Funnel (Sale/Purchase)."
      3. "IF >7 days: Optimize for Middle of Funnel (Qualified Lead/Call Booked)."
    key_metrics: "Event Volume (need 15-30/week)."
    failure_modes: "Optimizing for deep funnel events with zero data volume."

  - name: "Value Rules Bidding"
    source_tag: "[SRC: Sam Piliero | 713-714]"
    key_quote: "Create rule sets... based on outcomes that Facebook can't see like lifetime value."
    summary: "Adjusting bids automatically based on high-value attributes (e.g., Men have higher LTV, so bid +20% for Men)."
    when_to_use: "Advanced accounts with clear LTV data segments."
    steps:
      1. "Identify high-LTV segment (Geo, Gender, Age)."
      2. "Go to Campaign/Ad Set -> Value Rules."
      3. "Set rule: Increase/Decrease bid by X% if [Criteria]."
    key_metrics: "LTV, Repeat Purchase Rate."
    failure_modes: " applying rules without statistical backing."
```

***

# D) SOPs (10-15)

**SOP 1: The Creative Flywheel (Weekly Routine)**
*   **Source:** `[SRC: Sam Piliero | 196]`
*   **Frequency:** Weekly.
*   **Steps:**
    1.  **Analyze:** Review last 7-14 days using *Incremental Attribution*.
    2.  **Identify:** Find top "Concepts" (e.g., UGC in car, Press Screenshot).
    3.  **Brief:** Create 4-6 iterations of the winning concept.
    4.  **Source:** Find 1 *new* concept from competitors (MagicBrief/Ad Library).
    5.  **Launch:** Upload new batch to Prospecting CBO as a new "Pack" (Ad Set).

**SOP 2: Campaign Launch Checklist (Pre-Launch)**
*   **Source:** `[SRC: Chase Chappell | 726-730]`
*   **Frequency:** Per Launch.
*   **Steps:**
    1.  **Campaign:** Sales Objective, CBO enabled.
    2.  **Ad Set:** Broad Targeting (unless new pixel -> use Interest Clusters `[SRC: Sam Piliero | 641]`).
    3.  **Exclusions:** Exclude 180-day Purchasers (Define "New" swim lane).
    4.  **Placements:** Advantage+ Placements (Automatic).
    5.  **Creatives:** Ensure 3-5 distinct formats (Video, Static, Carousel).
    6.  **Enhancements:** Turn OFF "Visual Touch-ups" (to prevent Meta from cropping/ruining brand assets).

**SOP 3: Nano Banana AI Asset Creation**
*   **Source:** `[SRC: Sam Piliero | 597-598]`
*   **Frequency:** On-demand for static volume.
*   **Steps:**
    1.  Find winning static ad (own or competitor).
    2.  Copy image to Gemini (Nano Banana Pro model).
    3.  Prompt: "Replace [Person/Object] with [My Product/Model], keep composition identical."
    4.  Generate 4-10 variations.
    5.  Export for testing.

**SOP 4: Ad Set Spending Limit Injection**
*   **Source:** `[SRC: Sam Piliero | 654]`
*   **Frequency:** When launching new tests in established CBOs.
*   **Steps:**
    1.  Identify Target CPA (e.g., $50).
    2.  Set Ad Set Daily Minimum to 1x CPA ($50).
    3.  Set Calendar Reminder for 7 days.
    4.  **Day 7 Check:**
        *   IF spend > minimum and results good -> Remove limit (it flies on its own).
        *   IF spend = minimum and results bad -> Pause Ad Set.

**SOP 5: Post-Andromeda Optimization Routine**
*   **Source:** `[SRC: The Ecom King | 391]`
*   **Frequency:** Every 2-3 Days.
*   **Steps:**
    1.  Check Ad Sets. IF spread across too many tiny ad sets -> Consolidate to ONE Broad CBO.
    2.  Check Ad Frequency. IF >3.0 in prospecting -> Refresh creative.
    3.  Check "Concept" performance (not just individual ad).
    4.  Kill losers (High CPA, low spend).

***

# E) HEURISTICS (25-50)

**Diagnostic (Identifying Problems)**
*   **IF** learning limited >7 days, **THEN** consolidate ad sets or increase budget to hit 50 conversions/week `[SRC: Ben Heath | 580]`.
*   **IF** retargeting ROAS is high (>4x) but blended ROAS is low, **THEN** you are over-investing in retargeting; shift budget to prospecting `[SRC: Sam Piliero | 511]`.
*   **IF** one ad hogs 90% of CBO spend, **THEN** launch a separate "Testing Campaign" to force budget to new concepts `[SRC: Ben Heath | 578]`.
*   **IF** CPMs are spiking, **THEN** check creative diversity; Andromeda penalizes repetitive formats `[SRC: THE ECOM KING | 372]`.
*   **IF** "One Day View" conversions are >50% of total, **THEN** your ads are retargeting, not prospecting; switch to Incremental/Click attribution `[SRC: Tier 11 | 627]`.

**Optimization (Improving)**
*   **IF** spending <$3k/month, **THEN** use 1 Campaign (Prospecting) + 1 Re-marketing (Retention) `[SRC: Sam Piliero | 644]`.
*   **IF** spending >$30k/month, **THEN** use Cost Caps to manage volatility `[SRC: Sam Piliero | 653]`.
*   **IF** an ad has high Incremental ROAS (lift), **THEN** graduate it to the Scaling/Control ad set `[SRC: Sam Piliero | 509]`.
*   **IF** launching a new CBO test, **THEN** use Ad Set Spending Limits (Min = 1x CPA) for the first 7 days `[SRC: Sam Piliero | 654]`.
*   **IF** under $1M annual revenue, **THEN** focus on ONE avatar with multiple angles, not multiple avatars `[SRC: Dr. Matt Shiver | 54]`.

**Scaling (Growth)**
*   **IF** a creative works, **THEN** do not pause it; create a new "Pack" with variations to run alongside it `[SRC: Precision Frameworks | 608]`.
*   **IF** you spend $10k/month, **THEN** produce at least 1 new ad per week (Rule of 1:10k) `[SRC: Sam Piliero | 190]`.
*   **IF** scaling a winner, **THEN** use "Post ID Harvesting" to move it to the control campaign without losing engagement `[SRC: Professor Charley T | 103]`.
*   **IF** broad targeting fails, **THEN** test "Interest Clusters" as a temporary guide for the pixel `[SRC: Sam Piliero | 641]`.

**Troubleshooting (Fixing)**
*   **IF** lead gen lag time is >7 days, **THEN** optimize for "Qualified Lead" or "Call Booked" instead of "Sale" `[SRC: Caden Thompson | 290]`.
*   **IF** static ads are failing, **THEN** test "Native" formats (Apple Notes, News Articles) `[SRC: Omar Eddaoudi | 268]`.
*   **IF** CPA rises but CTR is stable, **THEN** the issue is likely post-click (Landing Page/Offer) `[SRC: Chase Chappell | 250]`.
*   **IF** clients demand "On-Brand" creatives but "Ugly" ads perform better, **THEN** run both in separate ad sets to prove the data `[SRC: Justin Lalonde | 10]`.

***

# F) METRICS TABLE

| Metric | Purpose | Threshold | Action Trigger | Source |
| :--- | :--- | :--- | :--- | :--- |
| **Incremental ROAS** | True profitability | > Break-even | Scale ad / Move to Control | `[SRC: Sam Piliero, 595]` |
| **Hook Rate** | Attention capture | > 30% | If low: Fix first 3 seconds | `[SRC: Jared Robinson, 483]` |
| **Hold Rate** | Retention | > 10-20% | If low: Fix content/pacing | `[SRC: Jared Robinson, 483]` |
| **Frequency** | Saturation | > 3.0 (Prospecting) | Refresh Creative | `[SRC: THE ECOM KING, 391]` |
| **Conversion Volume** | Optimization | < 50/week | Consolidate Ad Sets | `[SRC: Ben Heath, 580]` |
| **Lag Time** | Event Selection | > 7 Days | Move Optimization Up-Funnel | `[SRC: Caden Thompson, 289]` |

***

# G) PATTERNS (10-20)

1.  **Naming Convention:** `[Funnel]_[Objective]_[Concept]_[Date]` (e.g., `PROS_CONV_UGC-Mashup_2025-10-12`) `[SRC: Sam Piliero | 712]`.
2.  **M3 Setup Sequence:** Prospecting First -> Validate -> Add Retargeting -> Add Retention `[SRC: Sam Piliero | 509]`.
3.  **Exclusion Chain:** Prospecting excludes (Retargeting + Retention); Retargeting excludes (Retention) `[SRC: Jared Robinson | 81]`.
4.  **Creative Batches:** Grouping 3-6 creatives into a single ad set ("Pack") rather than 1 ad per ad set `[SRC: Jared Robinson | 81]`.
5.  **Broad Targeting:** Removing all interests, lookalikes, and demographics (except Age/Geo) `[SRC: Dr. Matt Shiver | 59]`.
6.  **Flexible Ads:** Using 3:2:2 structure to consolidate data `[SRC: Professor Charley T | 95]`.
7.  **Cost Caps:** Using cost controls to limit spend on bad days and scale on good days `[SRC: Sam Piliero | 519]`.
8.  **Visual Hooks:** High contrast, weird textures, or "scam" warnings in the first 3 seconds `[SRC: Fraser Cottrell | 798]`.
9.  **Founder Ads:** Face-to-camera storytelling from the owner to build trust `[SRC: Fraser Cottrell | 449]`.
10. **Native Formats:** Ads that look like Notes app, Twitter screenshots, or News articles `[SRC: Omar Eddaoudi | 268]`.

***

# H) FAILURE MODES (8-12)

1.  **Name:** **The "Learning Limited" Loop**
    *   *Symptoms:* Ad sets stuck in "Learning," high volatility.
    *   *Root Cause:* Budget too dispersed across too many ad sets/creatives.
    *   *Recovery:* Consolidate ad sets; use 3:2:2 to group creatives.
    *   *Source:* `[SRC: Ben Heath | 580]`
2.  **Name:** **Attribution Hallucination**
    *   *Symptoms:* Ads Manager shows 5x ROAS, Shopify shows flat revenue.
    *   *Root Cause:* Over-crediting View-Through conversions (Retargeting disguised as Prospecting).
    *   *Recovery:* Switch to Incremental Attribution or stricter exclusions (M3 lanes).
    *   *Source:* `[SRC: Sam Piliero | 595]`
3.  **Name:** **Creative Fatigue (Andromeda)**
    *   *Symptoms:* Rising CPMs, dropping CTR on previously winning ads.
    *   *Root Cause:* Repetitive formats (Andromeda penalizes lack of diversity).
    *   *Recovery:* Launch a new *Concept* (not variation) in a fresh pack.
    *   *Source:* `[SRC: THE ECOM KING | 372]`
4.  **Name:** **The Spend Hog**
    *   *Symptoms:* One ad gets 90% of CBO budget; new tests get zero.
    *   *Root Cause:* Meta's predictive action rate favors the known winner.
    *   *Recovery:* Use "Ad Set Spend Limits" (Min/Max) or a separate testing campaign.
    *   *Source:* `[SRC: Ben Heath | 571]`
5.  **Name:** **Lag Time Disconnect**
    *   *Symptoms:* Ad account shows zero conversions despite budget spend.
    *   *Root Cause:* Sales cycle > 7 days (Optimization window missed).
    *   *Recovery:* Optimize for a higher-funnel event (e.g., Lead instead of Purchase).
    *   *Source:* `[SRC: Caden Thompson | 290]`

***

# I) GOLDEN RUNS (2-4)

**Scenario 1: The Ecom Launch (Scale from $0 to $10k)**
*   **Inputs:** Fashion Brand, $3k/mo budget, 5 Creative Concepts.
*   **Setup:**
    *   1 Campaign (Prospecting CBO).
    *   2 Ad Sets: 1 Broad (Broad Pack 1), 1 Interest Cluster (Competitor Interest).
    *   Ads: 3:2:2 Flexible in Broad, Best 2 winners in Interest.
*   **Success Criteria:** Learning phase exits <7 days, Ad Set Spend Limit removed after Day 7, winning Post ID harvested to "Scale" ad set.
*   **Source:** `[SRC: Sam Piliero | 640]`

**Scenario 2: The High-Volume Lead Gen**
*   **Inputs:** Service Business, >7 day sales cycle.
*   **Setup:**
    *   Optimization Event: "Qualified Lead" (Middle of Funnel).
    *   Structure: Broad CBO.
    *   Creative: "Call out" hooks (e.g., "If you have back pain...").
*   **Success Criteria:** 15-30 Optimization Events per week fed to pixel.
*   **Source:** `[SRC: Caden Thompson | 296]`

***

# J) COMPLIANCE & GUARDRAILS

*   **Broad Targeting:** Meta now *requires* broad targeting for efficient AI delivery; restrictive targeting increases CPM `[SRC: THE ECOM KING | 373]`.
*   **Exclusions:** Must exclude 180-day purchasers from Prospecting to ensure accurate ncROAS `[SRC: Jared Robinson | 81]`.
*   **Creative Diversity:** Do not just test button colors. Andromeda requires *concept* changes (e.g., UGC vs. Static vs. Founder) `[SRC: Alex Robinson | 121]`.
*   **Budget Scaling:** Scale budget by ~20% every few days to avoid resetting the learning phase `[SRC: AI Strategist | 46]`.

***

# K) CHECKLISTS

**Launch Checklist**
- [ ] Campaign Objective = Sales `[SRC: Jared Robinson | 81]`
- [ ] CBO Enabled `[SRC: Sam Piliero | 508]`
- [ ] Attribution = 7-day click or Incremental `[SRC: Sam Piliero | 716]`
- [ ] Exclusions set (Purchasers 180d) `[SRC: Jared Robinson | 81]`
- [ ] "Visual Touch-ups" turned OFF `[SRC: Chase Chappell | 730]`
- [ ] 3-5 Distinct Creatives Uploaded `[SRC: Chase Chappell | 728]`

**Weekly Review Checklist**
- [ ] Check Incremental ROAS `[SRC: Sam Piliero | 595]`
- [ ] Harvest winning Post IDs to Control/Scale `[SRC: Professor Charley T | 103]`
- [ ] Check Frequency (>3.0 = danger) `[SRC: THE ECOM KING | 391]`
- [ ] Brief new creative pack (Rule of 1:10k) `[SRC: Sam Piliero | 656]`
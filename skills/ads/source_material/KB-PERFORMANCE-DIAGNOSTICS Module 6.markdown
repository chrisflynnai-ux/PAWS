KB-PERFORMANCE-DIAGNOSTICS.

--------------------------------------------------------------------------------
A) SOURCE MAP
1. Chase Chappell [SRC: Chase Chappell | 249-260]
    ? Key Topics: Optimization mistakes, Algorithmic Rhythm, Conversion Velocity.
    ? Unique Contribution: The concept of "Algorithmic Rhythm" (not disrupting the learning phase) and "Conversion Velocity" over front-end metrics.
2. Sam Piliero [SRC: Sam Piliero | 507-525, 786-800]
    ? Key Topics: M3 Structure, Incremental Attribution, Cost Caps, Ad Set Limits.
    ? Unique Contribution: "Attribution Hallucination" (Platform ROAS vs. Real Revenue) and using Ad Set Spending Limits to fix "Spend Hog" issues.
3. Ben Heath [SRC: Ben Heath | 603-625]
    ? Key Topics: Budget distribution, Spend Hogs, Testing Campaigns.
    ? Unique Contribution: The "Separate Testing Campaign" protocol for when Meta refuses to spend on new creatives in a CBO.
4. Tier 11 [SRC: Tier 11 | 702-727]
    ? Key Topics: Pixel Malnutrition, Offline Conversions, Signal Resilience.
    ? Unique Contribution: Diagnosing "Pixel Malnutrition" (algorithm starving for data) and retraining the pixel with offline events.
5. Alex Robinson [SRC: Alex Robinson | 120-123]
    ? Key Topics: Concepts vs. Variations, Ad Fatigue.
    ? Unique Contribution: Identifying the "Variable Testing" trap (testing button colors vs. concepts) as a primary failure mode in Andromeda.
6. Professor Charley T [SRC: Professor Charley T | 98-102]
    ? Key Topics: Fragmented Learning, 3:2:2.
    ? Unique Contribution: The diagnosis of "Fragmented Learning" where data is split across too many buckets, causing performance degradation.
7. Caden Thompson [SRC: Caden Thompson | 290-293]
    ? Key Topics: Lead Gen Lag Time, Optimization Events.
    ? Unique Contribution: Diagnosing "Lag Time Disconnect" where the sales cycle exceeds the attribution window.

--------------------------------------------------------------------------------
B) TAXONOMY
• Diagnostic Philosophy: Optimization via Elimination.
    ? Consensus: Most performance issues are self-inflicted by disrupting the algorithm (pausing too fast, over-segmenting) or feeding it bad data (attribution errors).
    ? The Shift: Move from "What button do I click to fix this?" to "Is the algorithm receiving enough signal and creative variety?"
• Problem Categories:
    1. Signal Failures: Pixel not firing, attribution windows missed, low match quality.
    2. Structural Failures: Fragmented learning, overlap, spend hogs.
    3. Creative Failures: Fatigue, hook-body mismatch, lack of diversity.
    4. Behavioral Failures: Reactionary pausing, micro-management.

--------------------------------------------------------------------------------
C) FAILURE MODES (15 PLAYBOOKS)
1. CREATIVE FATIGUE
• Symptoms: Hook Rate drops >30% from baseline; Frequency >3.0 (Prospecting); CPA rises while CTR drops.
• Root Cause: Audience saturation of a specific visual/hook; novelty has worn off.
• Diagnosis: Compare current Hook Rate (last 3 days) vs. Launch Week Hook Rate.
• Recovery: Launch a new Concept (not variation) in a fresh pack immediately.
• Prevention: Follow "Rule of 1:10k" (1 new ad per week per $10k spend) [SRC: Sam Piliero | 190].
2. ATTRIBUTION HALLUCINATION
• Symptoms: Ads Manager shows 4.0+ ROAS, but bank account is empty / MER is flat.
• Root Cause: Platform over-crediting View-Through conversions (Retargeting disguised as Prospecting).
• Diagnosis: Compare "1-day View" vs "7-day Click" breakdown; Calculate ncROAS (New Customer Revenue / Spend).
• Recovery: Switch attribution setting to "Incremental" or "7-day Click" only; tighten Exclusions.
• Prevention: Use M3 Swim Lanes to strictly separate Prospecting from Retargeting [SRC: Sam Piliero | 511].
3. THE "SPEND HOG"
• Symptoms: One ad gets 90% of CBO budget; new test ads get zero spend.
• Root Cause: Meta’s predicted action rate favors the known historical winner over the unknown new test.
• Diagnosis: Check spend distribution in CBO over last 3 days.
• Recovery: Apply "Ad Set Spending Limit" (Min = 1x CPA) to the starved ad sets for 3-7 days to force data.
• Prevention: Launch new creative packs in separate ad sets [SRC: Ben Heath | 603].
4. LEARNING LIMITED LOOP
• Symptoms: Ad sets stuck in "Learning Limited," high CPA volatility day-to-day.
• Root Cause: Budget too dispersed across too many ad sets; <50 conversions/week per set.
• Diagnosis: Check conversion volume per ad set (<50 = starving).
• Recovery: Consolidate ad sets (merge audiences); move to Broad CBO.
• Prevention: Use 3:2:2 Flexible Ads to consolidate creative data into fewer objects [SRC: Professor Charley T | 98].
5. PIXEL MALNUTRITION
• Symptoms: Zero conversions in Ads Manager despite sales occurring; "Learning" never progresses.
• Root Cause: Data signal loss (iOS14, AdBlockers) or CAPI disconnect.
• Diagnosis: Check Events Manager "Event Match Quality" (<6.0 = critical failure).
• Recovery: Setup CAPI (Conversion API) or import "Offline Events" from CRM.
• Prevention: Enable "Enhanced Matching" and CAPI during setup [SRC: Tier 11 | 706].
6. HOOK-BODY MISMATCH (Clickbait)
• Symptoms: High Hook Rate (>40%), High CTR, but Low Conversion Rate / Low Hold Rate.
• Root Cause: The hook promises something the body/offer does not deliver (Expectation misalignment).
• Diagnosis: Compare Hook Rate vs. Hold Rate (15s). If gap is massive, it's clickbait.
• Recovery: Re-edit video body to match hook tone; ensure landing page headline matches ad hook.
• Prevention: Ensure "Topic Clarity" in the first 2 seconds [SRC: Chase Chappell | 313].
7. LAG TIME DISCONNECT
• Symptoms: Ad account shows zero results; budget spends but algorithm can't optimize.
• Root Cause: Sales cycle > 7 days (Optimization window missed).
• Diagnosis: Calculate time from Lead -> Sale. If >7 days, Pixel is blind.
• Recovery: Optimize for a higher-funnel event (e.g., "Qualified Lead" or "Booked Call") instead of Purchase.
• Prevention: Lead Gen Lag-Time Optimization Framework [SRC: Caden Thompson | 290].
8. AUDIENCE FRAGMENTATION
• Symptoms: High CPMs, overlapping audiences, competing against yourself.
• Root Cause: Too many ad sets targeting similar people (e.g., "Lookalike 1%" vs "Lookalike 2%").
• Diagnosis: Use "Audience Overlap" tool; check for multiple ad sets targeting same geo/interest.
• Recovery: Collapse all non-distinct audiences into one "Broad" or "Stack" ad set.
• Prevention: Adopt the "One Campaign, Broad Targeting" philosophy [SRC: Dr. Matt Shiver | 55].
9. THE "JUNK LEAD" SPIRAL
• Symptoms: Low CPL (Cost Per Lead) but zero backend sales; sales team complaints.
• Root Cause: Optimizing for volume (Lead) without quality signals; algorithm finding bots/low-intent users.
• Diagnosis: Check Lead-to-Sale conversion rate.
• Recovery: Add friction (more form questions) or optimize for "Conversion Leads" (CRM integration).
• Prevention: Use "Offline Conversions" to train pixel on qualified leads only [SRC: Tier 11 | 685].
10. COST CAP FREEZE
• Symptoms: Campaign stops spending completely; zero impressions.
• Root Cause: Bid cap/Cost cap is set lower than the market auction price.
• Diagnosis: Check "Delivery" status; if "Active" but no spend, bid is too low.
• Recovery: Raise bid by 10-20% daily until spend resumes, or switch to Lowest Cost.
• Prevention: Set initial caps based on historical CPA + 20% buffer [SRC: Sam Piliero | 519].
11. VARIABLE TESTING TRAP
• Symptoms: Testing many ads but performance stays flat; no "breakout" winners.
• Root Cause: Testing minor variations (button color, font) instead of distinct concepts.
• Diagnosis: visual audit of active ads. Do they look 80% the same?
• Recovery: Adopt "Concept Over Variation" protocol; test entirely different angles.
• Prevention: Ensure new tests are "Meaningfully Different" [SRC: Alex Robinson | 121].
12. RETARGETING SATURATION
• Symptoms: Retargeting frequency >10; CPMs astronomical; ROAS declining.
• Root Cause: Retargeting pool is too small for the budget allocated.
• Diagnosis: Check Frequency on Retargeting Ad Set.
• Recovery: Reduce retargeting budget or expand window (30 days -> 180 days).
• Prevention: M3 Swim Lanes: Force budget to Prospecting to feed the funnel [SRC: Sam Piliero | 512].
13. NATIVE FORMAT MISFIT
• Symptoms: Low CTR, high CPM; ads look like "commercials."
• Root Cause: Creative looks too polished/produced for the placement (Reels/TikTok).
• Diagnosis: "Native Audit" - does it look like a friend's post or an ad?
• Recovery: Remove logos, use system fonts, add "Ugly" filters or UGC style.
• Prevention: Use "Lazy Static" or "iPhone Native" styles [SRC: Franky Shaw | 235].
14. FRONT-END OBSESSION
• Symptoms: High CTR, Low CPC, but low ROAS/High CPA.
• Root Cause: Optimizing for clicks (traffic) rather than conversions; attracting window shoppers.
• Diagnosis: Check objective (Traffic vs. Sales) and optimization event.
• Recovery: Switch objective to "Sales" (Conversions); accept higher CPC for better intent.
• Prevention: Optimize for "Conversion Velocity" not cheap clicks [SRC: Chase Chappell | 250].
15. ALGORITHMIC WHIPLASH
• Symptoms: Performance crashes after making manual edits.
• Root Cause: Making major changes (budget >20%, creative swaps) resetting the learning phase.
• Diagnosis: Check "History" for frequent edits (daily tinkering).
• Recovery: Stop touching it. Let it settle for 72 hours.
• Prevention: Batch updates; use automated rules for scaling [SRC: Chase Chappell | 253].

--------------------------------------------------------------------------------
D) ANTI-PATTERNS (7 TO AVOID)
1. Variable Testing: "Testing one hook, one thumbnail... that was the old way." Instead: Test multiple unique creative formats simultaneously in one audience [SRC: Chase Chappell | 252].
2. Frequent Pausing: "Pausing or duplicating ads daily... forces Meta to restart the learning phase." Instead: Allow 7-day windows and algorithmic rhythm [SRC: Chase Chappell | 253].
3. Front-End Obsession: "Optimizing for front-end metrics like CTR... cheap clicks doesn't mean buying intent." Instead: Optimize for Conversion Velocity/Payback loop [SRC: Chase Chappell | 250].
4. Reactionary Pausing: Turning off a winning ad because of one bad day. Instead: Look at 7-day trends; spend is variable [SRC: Sam Piliero | 520].
5. Micro-Segmentation: Breaking audiences into tiny ad sets (Men 25-34). Instead: Broad targeting allows Andromeda to find the pocket [SRC: Dr. Matt Shiver | 56].
6. The "Perfect" Ad: Waiting for high-production assets. Instead: "Ugly" ads and "Lazy Statics" often outperform branded content [SRC: Justin Lalonde | 10].
7. The Retargeting Trap: Spending >20% of budget on retargeting. Instead: Focus spend on New Customer Acquisition (ncROAS) [SRC: Sam Piliero | 511].

--------------------------------------------------------------------------------
E) DIAGNOSTIC HEURISTICS (IF-THEN)
Diagnostic (Identifying Problems)
• IF learning limited >7 days, THEN consolidate ad sets or increase budget to hit 50 conversions/week [SRC: Ben Heath | 612].
• IF one ad hogs >80% of CBO spend, THEN launch a separate "Testing Campaign" or use Ad Set Spending Limits [SRC: Ben Heath | 603].
• IF Hook Rate <25%, THEN audit the first 3 seconds; visual interrupt is weak [SRC: Fraser Cottrell | 888].
• IF Hook Rate >40% but Hold Rate <10%, THEN creative is clickbait; align body with hook [SRC: Jared Robinson | 483].
• IF CPMs spike, THEN check creative diversity; Andromeda penalizes repetitive formats [SRC: THE ECOM KING | 372].
• IF Platform ROAS >3.0 but MER <2.0, THEN attribution hallucination; calculate ncROAS [SRC: Sam Piliero | 192].
• IF frequency >3.0 in prospecting, THEN creative is fatigued; launch new concept [SRC: Tier 11 | 724].
• IF no conversions but clicks are high, THEN check "Post-Click" experience (Landing Page) [SRC: blake ecom | 416].
Optimization (Improving)
• IF ncROAS >1.5x, THEN scale budget by 20% [SRC: Justin Lalonde | 7].
• IF using Cost Caps and spend stops, THEN raise bid by 10-20% [SRC: Sam Piliero | 521].
• IF a creative works, THEN do not edit it; harvest Post ID to a scaling campaign [SRC: Professor Charley T | 103].
• IF under $1M revenue, THEN focus on ONE avatar with multiple angles [SRC: Dr. Matt Shiver | 54].
• IF you find a winning concept, THEN create 10 variations of that concept immediately [SRC: Sam Piliero | 193].
Scaling (When/How)
• IF spending $10k/month, THEN produce 1 new ad per week (Rule of 1:10k) [SRC: Sam Piliero | 190].
• IF scaling a winner, THEN add a banner (e.g., "Black Friday") to the existing creative rather than reshooting [SRC: Fraser Cottrell | 858].
• IF broad targeting works, THEN do not narrow it; let the creative do the targeting [SRC: Dr. Matt Shiver | 53].
Troubleshooting (Fixing)
• IF leads are low quality, THEN add friction (questions) to the form [SRC: Caden Thompson | 294].
• IF static ads fail, THEN try "Native" formats (Notes app, news headline) [SRC: Franky Shaw | 235].
• IF video ads are too expensive (CPM), THEN switch to Static Image ads [SRC: Franky Shaw | 234].
• IF production is the bottleneck, THEN use "Nano Banana" (AI) to generate variations [SRC: Sam Piliero | 627].

--------------------------------------------------------------------------------
F) TROUBLESHOOTING WORKFLOWS
Workflow 1: "My Ads Stopped Working" (Fatigue vs. Broken)
1. Check Date Range: Look at "Last 7 Days" vs "Previous Period."
2. Check Frequency: Is it >3.0? -> Fatigue. Action: New Creative.
3. Check CPM: Did it double? -> Competition/Quality Drop. Action: Refresh Creative.
4. Check CTR: Did it drop? -> Ad Blindness. Action: New Hook.
5. Check CVR: CTR stable but CVR dropped? -> Landing Page/Offer issue. Action: Audit site speed/stock.
Workflow 2: "I Can't Exit Learning Phase"
1. Check Event Count: Are you getting 50 conversions/week?
2. IF NO: Is budget <$50/day? -> Increase Budget.
3. IF BUDGET OK: Are you splitting it across 5 ad sets? -> Consolidate to 1 Ad Set.
4. IF CONSOLIDATED: Is the event too rare (e.g., Purchase)? -> Move Up-Funnel (e.g., Add to Cart or Lead) temporarily [SRC: Caden Thompson | 291].

--------------------------------------------------------------------------------
G) CIRCUIT BREAKERS (When to Stop)
1. The "Profit Floor": IF ncROAS < 1.0 for 7 days, STOP SCALING. You are losing money on every new customer [SRC: Sam Piliero | 776].
2. The "Spend Spiral": IF CPA > 3x Target for 48 hours with no conversions, KILL AD. It is not going to "optimize" its way out [SRC: Chase Chappell | 44].
3. The "Creative Dead End": IF you launch 10 new concepts and 0 get spend, AUDIT OFFER. The problem is likely the product/offer, not the ads [SRC: blake ecom | 416].

--------------------------------------------------------------------------------
H) SOPs (STANDARD OPERATING PROCEDURES)
SOP 1: Daily Diagnostic Check
• Frequency: Daily (Morning).
• Steps:
    1. Check Spend Amount (Did we hit budget?).
    2. Check MER (Total Revenue / Total Spend). Is it healthy?
    3. Check Top Ads. Any "Spend Hogs" with low ROAS?
    4. Action: If Spend Hog CPA > Target, apply "Ad Set Limit" or Pause [SRC: Sam Piliero | 744].
SOP 2: The "Creative Refresh" Protocol
• Frequency: Weekly (or when Frequency > 3.0).
• Steps:
    1. Identify "Fatigued" winners (High Freq, Dropping CTR).
    2. Select 1 new "Concept" from the bench.
    3. Launch in "Prospecting CBO" as a new "Pack" (Ad Set).
    4. Do NOT turn off the old winner yet; let Andromeda shift the spend naturally [SRC: Jared Robinson | 84].
SOP 3: Tracking Validation (Monthly)
• Frequency: Monthly.
• Steps:
    1. Open Events Manager.
    2. Check "Event Match Quality" score (Target > 7.0).
    3. Check "Incremental" vs "Click" attribution gap.
    4. Action: If Match Quality < 5.0, refresh CAPI token or check server integration [SRC: Tier 11 | 691].

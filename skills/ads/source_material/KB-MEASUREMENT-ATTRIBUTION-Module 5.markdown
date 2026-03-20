KB-MEASUREMENT-ATTRIBUTION.

--------------------------------------------------------------------------------
A) SOURCE MAP
1. Sam Piliero [SRC: Sam Piliero | 192, 511, 729, 774-788]
    ? Key Topics: Incremental Attribution, ncROAS, MER, "Attribution Hallucination."
    ? Unique Contribution: The specific workflow for using "Compare Attribution Settings" to isolate incremental lift and the shift to optimizing for "Incremental" directly in Ad Sets.
2. Tier 11 (John Moran/Ralph Burns) [SRC: Tier 11 | 683-698]
    ? Key Topics: Lead quality, CAPI imports, Offline Conversions, Retraining the pixel.
    ? Unique Contribution: The "AOS New Customer" custom event strategy to force the algorithm to ignore returning customers and optimizing for deep-funnel events.
3. Caden Thompson [SRC: Caden Thompson | 289-296]
    ? Key Topics: Lead Gen Lag-Time, Optimization Event Selection.
    ? Unique Contribution: The framework for selecting optimization events (Top vs. Bottom funnel) based on the specific "Lag Time" of the sales cycle (e.g., <7 days vs. >7 days).
4. Justin Lalonde [SRC: Justin Lalonde | 7-11]
    ? Key Topics: Platform ROAS vs. Blended ROAS, Client Assets vs. Performance.
    ? Unique Contribution: Using "Platform ROAS" trends to validate creative scaling decisions even when third-party tools show different data.
5. Ben Heath [SRC: Ben Heath | 616-618]
    ? Key Topics: Third-party tracking (Hyros).
    ? Unique Contribution: Highlighting discrepancies where Meta under-reports high-ticket/recurring revenue compared to third-party trackers.

--------------------------------------------------------------------------------
B) TAXONOMY
• North Star Metric: ncROAS (New Customer ROAS) and Incremental ROAS.
    ? Consensus: Blended ROAS and standard Platform ROAS (7-day click/1-day view) are often inflated by returning customers [SRC: Sam Piliero | 192].
    ? Shift: Move from "Attribution" (who gets credit) to "Incrementality" (did this ad cause the sale?).
• Measurement Models:
    ? Platform Standard: 7-day click / 1-day view (Default, often inflated).
    ? Incremental: Meta's specific attribution setting that discounts view-through conversions [SRC: Sam Piliero | 787].
    ? MER: Marketing Efficiency Ratio (Total Revenue / Total Spend) as the "King Goal" [SRC: Sam Piliero | 777].
• Lead Gen Specifics:
    ? Lag Time: The duration between lead capture and sale determines the optimization event [SRC: Caden Thompson | 290].

--------------------------------------------------------------------------------
C) FRAMEWORKS (8-12)
1. The Incremental Attribution Check
• Source: [SRC: Sam Piliero | 788]
• Quote: "It's only focused on conversions that happened because of Facebook... not Facebook slipping in at the last second."
• Summary: A method to validate if ads are driving new revenue or just retargeting people who would have bought anyway.
• When to use: Weekly analysis of winning creatives.
• Steps:
    1. Go to Ads Manager -> Columns.
    2. Select "Compare Attribution Settings."
    3. Check "Incremental Attribution."
    4. Compare "Incremental Purchases" vs. "7-day Click Purchases."
    5. Metric: If the gap is >30%, the ad is likely over-crediting retargeting.
2. Lead Gen Lag-Time Optimization
• Source: [SRC: Caden Thompson | 290-291]
• Quote: "If we wait all the way to the end point we have a massive gap in between."
• Summary: Adjusting the conversion event based on sales cycle length to ensure the algorithm gets data within the 7-day window.
• When to use: Service businesses or B2B with sales cycles.
• Steps:
    1. Determine Sales Cycle Length (Lag Time).
    2. IF <7 Days: Optimize for Bottom of Funnel (Sale/Booked Call).
    3. IF >7 Days: Optimize for Middle of Funnel (Qualified Lead).
    4. Goal: Feed the pixel 15-30 events per week minimum.
3. ncROAS Calculation (New Customer ROAS)
• Source: [SRC: Justin Lalonde | 7; Sam Piliero | 777]
• Quote: "We're pretty much maintaining though this month to date in terms of new customer rorowas."
• Summary: Separating New vs. Returning revenue to determine the true scalability of ad spend.
• Formula: (Total Revenue - Returning Customer Revenue) / Ad Spend.
• Target: >1.5x ncROAS is generally scalable; <1.0x is burning cash (unless LTV is massive).
4. The "AOS New Customer" Optimization
• Source: [SRC: Tier 11 | 694]
• Quote: "This one says I'm going to pick you up and bring you to close."
• Summary: Creating a custom conversion event that only fires for new customers (filtering out existing ones via CAPI/CRM) and optimizing for that specific event.
• Steps:
    1. Connect CRM (HubSpot/Klaviyo) to Meta via CAPI.
    2. Define "New Customer Purchase" as a unique event.
    3. Launch a campaign optimizing specifically for "AOS New Customer" alongside standard campaigns.
5. MER "King Goal" Monitoring
• Source: [SRC: Sam Piliero | 777-778]
• Quote: "Your king goal... overrides all other goals... back in my day... we used to say CAC is king."
• Summary: Using the macro business health metric to validate ad performance when platform metrics are messy.
• Steps:
    1. Calculate Total Revenue from Shopify/CRM.
    2. Divide by Total Ad Spend (Facebook + Google + Tik Tok).
    3. Rule: If Platform ROAS rises but MER stays flat, you are cannibalizing organic sales (Attribution Hallucination).
6. Attribution Window Configuration
• Source: [SRC: Sam Piliero | 729]
• Quote: "Gone are the days of 7-day click... 7-day click one day view is typically a little bit too big."
• Summary: Tightening attribution windows for high-volume accounts to prevent over-crediting view-throughs.
• Strategy:
    ? <$100k/mo: Stick to 7-day click / 1-day view.
    ? >$100k/mo: Switch to 1-day click or Incremental to force the algorithm to find immediate converters.
7. Offline Conversion Validation
• Source: [SRC: Tier 11 | 685-687]
• Quote: "The metadata was counting things that weren't real... so now that we have it real we're retraining it."
• Summary: Manually uploading or syncing offline events (booked calls, closed deals) to correct the pixel's "hallucinations" of bad leads.
• Steps:
    1. Export lead list with statuses (Sold/Junk) from CRM.
    2. Upload to Meta Events Manager as "Offline Events."
    3. Match data points (Email, Phone, Name).
    4. Create Custom Audience of "Junk Leads" to exclude.
8. Value Rules Bidding
• Source: [SRC: Sam Piliero | 784]
• Quote: "Create rule sets... based on outcomes that Facebook can't see like lifetime value."
• Summary: Telling Meta to bid higher/lower for specific segments based on backend LTV data.
• Steps:
    1. Identify high LTV segment (e.g., Men return 50% more).
    2. Go to Ad Set -> Value Rules.
    3. Set: "If Gender = Men, Bid +20%."

--------------------------------------------------------------------------------
D) SOPs (5-8)
SOP 1: Weekly Incrementality Audit
• Source: [SRC: Sam Piliero | 788]
• Frequency: Weekly (Monday).
• Steps:
    1. Open Ads Manager.
    2. Select columns -> "Compare Attribution Settings."
    3. Look at top 5 spending ads.
    4. Calculate the drop-off from "Default" to "Incremental."
    5. Action: If an ad drops >50% in ROAS under Incremental, pause or move to Retargeting (it's not a prospecting winner).
SOP 2: Lead Gen Quality Feedback Loop
• Source: [SRC: Tier 11 | 684]
• Frequency: Daily or Weekly.
• Steps:
    1. Review leads in CRM (HubSpot/GoHighLevel).
    2. Mark leads as "Qualified" or "Junk."
    3. Push "Qualified" events back to Meta via CAPI.
    4. Verify in Events Manager that "Qualified Lead" events are matching.
SOP 3: ncROAS Calculation Routine
• Source: [SRC: Justin Lalonde | 7]
• Frequency: Daily/Weekly reporting.
• Steps:
    1. Pull "New Customer Sales" from Shopify/Triple Whale.
    2. Pull Total Ad Spend from Meta.
    3. Formula: New Customer Revenue / Spend.
    4. Target: Maintain >1.5x ncROAS for scaling.
SOP 4: Ad Set Spending Limit Injection
• Source: [SRC: Sam Piliero | 725]
• Frequency: When launching new tests.
• Steps:
    1. Identify Target CPA (e.g., $50).
    2. Set Ad Set Daily Minimum to 1x CPA ($50).
    3. Run for max 7 days.
    4. Decision: If performing, remove limit. If failing, kill ad set.

--------------------------------------------------------------------------------
E) HEURISTICS (20-30)
Diagnostic (Identifying Problems)
• IF Platform ROAS is >3.0 but MER is <2.0, THEN you are suffering from "Attribution Hallucination" (Meta claiming organic sales) [SRC: Sam Piliero | 777].
• IF "One Day View" conversions account for >50% of total conversions, THEN your ads are retargeting, not prospecting [SRC: Tier 11 | 698].
• IF lead volume is high but "Booked Call" volume is low, THEN optimize deeper in the funnel (Lag Time Optimization) [SRC: Caden Thompson | 291].
• IF ncROAS drops below 1.0, THEN you are paying more to acquire a customer than they are worth; stop scaling immediately [SRC: Sam Piliero | 777].
• IF Ads Manager shows sales but Shopify shows none, THEN check "Event Match Quality" in Events Manager (likely <6.0 score) [SRC: Tier 11 | 691].
Optimization (Improving)
• IF you have a high LTV segment (e.g., Men), THEN use "Value Rules" to increase bids for that segment by 20% [SRC: Sam Piliero | 784].
• IF you are spending >$100k/mo, THEN switch attribution setting to "Incremental" or "1-day click" to force higher quality traffic [SRC: Sam Piliero | 729].
• IF a creative has high "Incremental ROAS" (Lift), THEN it is a true scaler; move it to the scale campaign [SRC: Sam Piliero | 628].
• IF Lead Gen lag time is >7 days, THEN optimize for "Qualified Lead" instead of "Sale" to keep data flowing to the pixel [SRC: Caden Thompson | 296].
Scaling (Growth)
• IF ncROAS is >1.5x, THEN you have permission to increase budget by 20% [SRC: Justin Lalonde | 7].
• IF using Cost Caps, THEN understand spend will be volatile (high on good days, low on bad days) [SRC: Sam Piliero | 520].
• IF scaling a winner, THEN use "Post ID Harvesting" to keep social proof attached to the attribution history [SRC: Professor Charley T | 103].
Troubleshooting (Fixing)
• IF leads are low quality, THEN add friction to the form (questions) or optimize for a deeper event (Booked Call) [SRC: Caden Thompson | 294].
• IF blended ROAS drops, THEN check if you over-spent on "Existing Customers" (Retention) vs "Prospecting" [SRC: Sam Piliero | 512].
• IF standard events aren't tracking real value, THEN import "Offline Events" (e.g., Deal Closed) to retrain the algorithm [SRC: Tier 11 | 683].

--------------------------------------------------------------------------------
F) METRICS TABLE
Metric
Purpose
Threshold
Action Trigger
Source
ncROAS
True Scalability
> 1.5x
Scale Budget
`[SRC: Sam Piliero
Incremental ROAS
Attribution Truth
> 1.0 (Lift)
Move to Scale Campaign
`[SRC: Sam Piliero
MER
Business Health
> 2.5 - 3.0
If dropping: Cut wasted spend
`[SRC: Sam Piliero
Lag Time
Event Selection
< 7 Days
If >7 Days: Move optimization up-funnel
`[SRC: Caden Thompson
Event Match Quality
Data Integrity
> 7.0 (out of 10)
If <6.0: Fix CAPI/Pixel setup
`[SRC: Tier 11
View-Through %
Retargeting Check
< 30% of total
If >50%: Switch to Click Attribution
`[SRC: Tier 11

--------------------------------------------------------------------------------
H) FAILURE MODES (5-8)
1. Name: Attribution Hallucination
    ? Symptoms: Ads Manager shows 5x ROAS, but bank account is empty / MER is flat.
    ? Root Cause: Platform over-crediting "View-Through" conversions from retargeting audiences who would have bought anyway.
    ? Diagnosis: Compare "1-day View" vs "7-day Click" breakdown.
    ? Recovery: Switch to Incremental Attribution or stricter exclusions.
    ? Source: [SRC: Sam Piliero | 775]
2. Name: Pixel Malnutrition
    ? Symptoms: Zero conversions showing in Ads Manager despite sales happening.
    ? Root Cause: Lag time > 7 days or CAPI disconnected.
    ? Diagnosis: Check Events Manager for "Last Event Received."
    ? Recovery: Optimize for a higher-funnel event (e.g., Lead instead of Sale) or fix CAPI.
    ? Source: [SRC: Caden Thompson | 290]
3. Name: The "Junk Lead" Spiral
    ? Symptoms: Low CPL (Cost Per Lead) but zero sales/booked calls.
    ? Root Cause: Optimizing for "Lead" event without quality filters; Algorithm finding bots/low-intent users.
    ? Recovery: Switch optimization to "Booked Call" or import "Qualified Lead" offline events.
    ? Source: [SRC: Caden Thompson | 293]
4. Name: Retention Overspend
    ? Symptoms: High blended ROAS, but new customer growth is flat.
    ? Root Cause: Budget allocation shifting naturally to "Existing Customers" (easiest conversions).
    ? Recovery: Implement M3 Swim Lanes with strict exclusions (Exclude 180d Purchasers).
    ? Source: [SRC: Sam Piliero | 512]

--------------------------------------------------------------------------------
I) GOLDEN RUNS (3-5)
Scenario 1: Ecom Scale Validation ($10k -> $50k/mo)
• Context: Fashion brand scaling up.
• Action: Switch from measuring Platform ROAS to ncROAS.
• Inputs: Revenue $100k, New Customer Revenue $60k, Ad Spend $30k.
• Calculation: ncROAS = $60k / $30k = 2.0.
• Decision: 2.0 is > 1.5 target. Scale budget by 20%.
• Source: [SRC: Justin Lalonde | 7]
Scenario 2: High-Ticket Service Lead Gen
• Context: Home renovation, $20k projects, 3-week sales cycle.
• Problem: Optimizing for "Sale" yields no data (Lag time > 7 days).
• Action: Change optimization event to "Booked Designer Call" (Middle of Funnel).
• Result: Algorithm gets 50+ events/week; CPA stabilizes.
• Source: [SRC: Tier 11 | 685]
Scenario 3: Fixing "Fake" Performance
• Context: Account shows 4.0 ROAS but cash flow is tight.
• Action: Run Incremental Attribution Check.
• Result: 4.0 ROAS drops to 1.2 Incremental ROAS (mostly retargeting).
• Fix: Cut Retargeting budget by 50%, move spend to Broad Prospecting with exclusions.
• Source: [SRC: Sam Piliero | 788]

--------------------------------------------------------------------------------
J) COMPLIANCE & GUARDRAILS
• Privacy: When using CAPI or Offline Imports, you must hash PII (Personally Identifiable Information) like emails and phone numbers before sending to Meta [SRC: Tier 11 | 699].
• Truth in Reporting: Do not report "Blended ROAS" to clients as "Ad Performance." Distinguish between "Platform ROAS" and "MER" to maintain integrity [SRC: Sam Piliero | 777].
• Exclusions: Ensure you exclude 180-day purchasers from Prospecting to ensure ncROAS data is clean [SRC: Sam Piliero | 716].

--------------------------------------------------------------------------------
K) CHECKLISTS
Weekly Measurement Audit
• [ ] Check MER (Total Rev / Total Spend) [SRC: Sam Piliero | 777]
• [ ] Check ncROAS (New Rev / Spend) [SRC: Justin Lalonde | 7]
• [ ] Compare Attribution Settings (Incremental vs Default) [SRC: Sam Piliero | 788]
• [ ] Check Event Match Quality (>7.0) [SRC: Tier 11 | 699]
Lead Gen Setup Checklist
• [ ] Determine Lag Time (Lead -> Sale) [SRC: Caden Thompson | 290]
• [ ] Select Optimization Event (Bottom if <7 days, Middle if >7 days) [SRC: Caden Thompson | 291]
• [ ] Verify CAPI connection for offline events [SRC: Tier 11 | 699]
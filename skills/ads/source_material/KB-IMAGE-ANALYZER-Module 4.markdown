KB-IMAGE-ANALYZER.

--------------------------------------------------------------------------------
A) SOURCE MAP
1. Fraser Cottrell [SRC: Fraser Cottrell | 848-852]
    ? Key Topics: Visual attention control, color theory, visual chaos.
    ? Unique Contribution: The "Visual Chaos" reduction theory and using "fecal matter looking rocks" (weird textures) to seize attention.
2. J.B. | Vibe Marketing [SRC: J.B. | Vibe Marketing | 464-476]
    ? Key Topics: Automated competitive analysis, N8N workflows, ad scraping.
    ? Unique Contribution: A fully automated AI system that scrapes competitor ads, transcribes them, and outputs a "Deep Analysis Report" on hooks and emotional triggers.
3. Mike Futia | SCALE AI [SRC: Mike Futia | SCALE AI | 822-831]
    ? Key Topics: Video ad scraping, AI analysis of visual notes.
    ? Unique Contribution: Method for extracting "Visual Notes" and "Primary Messages" from video ads using Gemini and AirTable.
4. Dara Denney [SRC: Dara Denney | 497-498]
    ? Key Topics: Hook structure (Text, Sound, Visual, Vibe), Visual Hook types.
    ? Unique Contribution: The concept that "changing the visual hook... tends to have a bigger impact on performance than the text overlay."
5. Chase Chappell [SRC: Chase Chappell | 311-321]
    ? Key Topics: Hook diagnostics, confusion analysis, interest loops.
    ? Unique Contribution: Identifying "Confusion" and "Delayed Value" as the primary reasons for scroll-past behavior.
6. Kallaway [SRC: Kallaway | 360-362]
    ? Key Topics: Visual hooks vs. spoken hooks, motion thresholds.
    ? Unique Contribution: The insight that "Visual hooks are probably 100 times more powerful than just spoken word Hooks."
7. Jared Robinson [SRC: Jared Robinson | 481-483]
    ? Key Topics: Hook Rate vs. ICP Quality.
    ? Unique Contribution: The warning that high hook rates with "cute dogs" attract low-quality leads; hooks must qualify the ICP.
8. Franky Shaw [SRC: Franky Shaw | 235-238]
    ? Key Topics: Native formats, "Breaking News" aesthetics.
    ? Unique Contribution: Analyzing ads that look like "scroll stoppers" because they resemble news articles or blog snippets.

--------------------------------------------------------------------------------
B) TAXONOMY
• Core Philosophy: Visual Interrupt & Retention.
    ? Consensus: The first 3 seconds must visually disrupt the pattern of the feed. "Visual hooks are... 100 times more powerful than just spoken word" [SRC: Kallaway | 360].
    ? Measurement: Success is measured by Hook Rate (3s Video Plays / Impressions) and Hold Rate (ThruPlays / 3s Plays).
• Diagnostic Layers:
    1. The Squint Test: Can you identify the focal point instantly? [SRC: Fraser Cottrell | 849].
    2. The Confusion Audit: Does the viewer know what this is within 2 seconds? [SRC: Chase Chappell | 313].
    3. The Native Check: Does it look like an ad (bad) or content (good)? [SRC: Franky Shaw | 235].
• Analytical Tools:
    ? Manual: Visual Hook Audit checklists.
    ? Automated: N8N + Apify + Gemini workflows to scrape and analyze competitor creative at scale [SRC: J.B. | Vibe Marketing | 467].

--------------------------------------------------------------------------------
C) FRAMEWORKS (8-15)
1. The "Visual Chaos" Audit
• Source: [SRC: Fraser Cottrell | 849-850]
• Quote: "Remove any kind of visual chaos and just allow people to focus on one thing."
• Summary: A diagnostic process to ensure the viewer's eye is guided immediately to the hook element without distraction.
• Steps:
    1. Freeze Frame: Pause at 0:01.
    2. Identify Focal Point: Where do eyes go? (Product, Face, Text).
    3. Eliminate Distraction: Blur background, remove clutter, increase contrast.
    4. Verify: Ensure the "weird" or "satisfying" texture is the brightest/sharpest element.
2. The 4-Element Hook Structure
• Source: [SRC: Dara Denney | 497]
• Quote: "Your hook is actually these four things... Text overlay... Sound... Visual... and the Vibe."
• Summary: Analyzing a hook not just by copy, but by the interplay of four distinct distinct signals.
• Elements:
    1. Text Overlay: Readability, placement, keyword triggers.
    2. Sound: Voiceover timing, SFX, music swell.
    3. Visual: The actual footage (Action, Reaction, Texture).
    4. Vibe: Lighting, font choice, editing pace (does it feel native?).
3. Automated Competitor Spy Protocol (N8N)
• Source: [SRC: J.B. | Vibe Marketing | 464-475]
• Quote: "Scrapes your competitor's top five video ads and breaks down exactly why they're working."
• Summary: A technical framework for automating the analysis of competitor creatives to extract winning patterns.
• Steps:
    1. Input: Facebook Page ID into AirTable.
    2. Scrape: Use N8N + Apify to pull "Active Ads" running >14 days.
    3. Process: Send video URL to Deepgram (transcription) and Gemini (Visual Analysis).
    4. Output: Generate a report listing "Hook Type," "Awareness Level," and "Emotional Triggers."
4. The "Confusion" Diagnostic
• Source: [SRC: Chase Chappell | 313-314]
• Quote: "When you delay the big benefit... it creates confusion and the human brain immediately tells you to scroll."
• Summary: A check to ensure the ad delivers "Topic Clarity" within the first 2 seconds.
• Analysis:
    ? Bad: "What's up guys..." (Who are you? What is this?).
    ? Good: "The thermal shred stack is great for..." (Product shown + Audience named).
5. Native Format Analysis
• Source: [SRC: Franky Shaw | 235-236]
• Quote: "This is a scroll stopper it looks like a news article so people are curious."
• Summary: Evaluating ads based on their ability to camouflage as organic content or news.
• Checklist:
    ? Does it use standard UI elements (e.g., iPhone Notes, News Headers)?
    ? Is the font "Ad-like" (fancy) or "Native" (Arial/System font)?
    ? Is the image "Perfect" (Stock) or "Ugly" (UGC/AI)?
6. The "Weird Texture" Analysis
• Source: [SRC: Fraser Cottrell | 849]
• Quote: "What looks like some weird almost fecal matter looking rocks... curiosity... gave this video such a high hook rate."
• Summary: Leveraging "Gross" or "Satisfying" textures to trigger visceral curiosity.
• When to use: When standard product shots fail to stop the scroll.
• Visuals: Slime, dirt, peeling, cracking, "weird rocks."
7. Hook Rate vs. ICP Quality Matrix
• Source: [SRC: Jared Robinson | 481-483]
• Quote: "A cute dog... is going to spike your hook rate but it's not actually going to convert."
• Summary: Balancing high attention (Hook Rate) with correct qualification (Conversion).
• Quadrants:
    ? High Hook / Low Conv: Clickbait (Cute dog, unconnected viral clip).
    ? Low Hook / High Conv: Boring but relevant (Scale this by fixing hook).
    ? High Hook / High Conv: The Goal (Relevant emotional trigger).
8. Creative Fatigue Detection (Ad Set Level)
• Source: [SRC: Tier 11 | 685]
• Quote: "Ads don't fatigue the ad set does... you're testing kind of everything in the audience."
• Summary: Fatigue is audience saturation relative to a concept.
• Signals:
    ? Frequency > 3.0.
    ? First-time Impression Ratio drops.
    ? CPA rises while CTR drops.

--------------------------------------------------------------------------------
D) SOPs (10-15)
SOP 1: Weekly Visual Hook Audit
• Source: [SRC: Fraser Cottrell | 848]
• Frequency: Weekly.
• Steps:
    1. Pull report of ads with Hook Rate <25%.
    2. Watch first 3 seconds of each.
    3. Check 1: Is there "Visual Chaos"? (Too many focal points).
    4. Check 2: Is the text readable in 1 second?
    5. Check 3: Is there motion? (Static video intros kill retention).
    6. Action: Re-edit first 3s (Zoom, Crop, Text Change) and relaunch.
SOP 2: Automated Competitor Swipe
• Source: [SRC: Mike Futia | SCALE AI | 827-831]
• Frequency: Weekly (Automated).
• Steps:
    1. Add new competitor URLs to AirTable "Brands" tab.
    2. Run N8N workflow (Scrape -> Analyze).
    3. Review "Video Analysis" tab in AirTable.
    4. Filter by "Hook Excerpt" to find patterns (e.g., "How is this profitable?").
    5. Send top 3 concepts to creative team.
SOP 3: The "Split-Screen" Variation Test
• Source: [SRC: Jared Robinson | 88]
• Frequency: When iterating winners.
• Steps:
    1. Take a winning concept (e.g., product demo).
    2. Create Variant A: Full screen.
    3. Create Variant B: Split screen (Product on top, Reaction/Result on bottom).
    4. Create Variant C: "Us vs. Them" split.
    5. Launch in 3:2:2 test to see which visual layout holds attention best.
SOP 4: Native Asset Polish Removal
• Source: [SRC: Justin Lalonde | 10-12]
• Frequency: Pre-launch QA.
• Steps:
    1. Review ad creative.
    2. Does it look like a "Client Asset" (Polished, Studio)?
    3. If YES: Apply "Ugly" filter. Add native text overlay (Instagram font), add handheld camera shake effect, or replace background with "messy" environment (using AI).
    4. Goal: Make it look 50% less professional.
SOP 5: Post-Click Congruency Check
• Source: [SRC: blake ecom | 415]
• Frequency: Monthly.
• Steps:
    1. Open top 5 ads on mobile.
    2. Click "Shop Now."
    3. Check: Does the landing page visual match the ad visual? (Same colors, same model, same "Vibe").
    4. Check: Does the headline on the lander answer the hook in the ad?
    5. Action: If disconnected, build specific landing page (listicle/advertorial) for that creative angle.

--------------------------------------------------------------------------------
E) HEURISTICS (25-50)
Diagnostic (Identifying Problems)
1. IF Hook Rate is <25%, THEN your visual interrupt is weak; add motion or "weird" texture [SRC: Fraser Cottrell | 849].
2. IF Hook Rate is >40% but Hold Rate is <10%, THEN you are click-baiting; the video body does not match the promise [SRC: Jared Robinson | 483].
3. IF CPMs are >$50 (broad), THEN your creative is triggering "Ad Blindness"; switch to "Native/News" formats [SRC: Franky Shaw | 235].
4. IF CTR is low (<0.8%) despite high Hold Rate, THEN your CTA is weak or the offer is unclear [SRC: Chase Chappell | 318].
5. IF text overlay covers >20% of the screen, THEN performance may drop due to "Visual Chaos" [SRC: Fraser Cottrell | 830].
6. IF competitors are running an ad for >30 days, THEN scrape it immediately; it is a proven winner [SRC: J.B. | Vibe Marketing | 468].
Optimization (Improving) 7.  IF you have a winning static, THEN use AI (Nano Banana) to swap the background to a "Messy Room" to increase authenticity [SRC: Sam Piliero | 633]. 8.  IF a video hook works, THEN test it with "Sound Off" to ensure the visual alone carries the weight [SRC: Fraser Cottrell | 849]. 9.  IF using a "Scam Hook" (verbal), THEN pair it with a visual of someone looking skeptical or disappointed [SRC: Dara Denney | 496]. 10. IF you want to increase authority, THEN add a "Founder Introduction" hook ("I'm [Name], founder of...") [SRC: Dara Denney | 502]. 11. IF testing "Us vs. Them", THEN use a visual split screen; do not rely on text alone [SRC: Jared Robinson | 88]. 12. IF targeting a specific demographic (e.g., Over 50), THEN call them out visually in the first frame (Text: "Over 50?") [SRC: Dara Denney | 505].
Scaling (When/How) 13. IF an ad has >30% Hook and >2% CTR, THEN it is a "Unicorn"; harvest the Post ID and move to scale [SRC: Professor Charley T | 105]. 14. IF you find a winning "Concept" (e.g., Unboxing), THEN iterate 10 variations of that concept, not just the hook [SRC: Sam Piliero | 773]. 15. IF scaling hard, THEN monitor "First Time Impression Ratio"; if it drops, refresh creative [SRC: Tier 11 | 686].
Troubleshooting (Fixing) 16. IF viewers drop at 0:03, THEN your "Scroll Stop Interjection" (The "But wait...") is missing or weak [SRC: Kallaway | 352]. 17. IF the ad is confusing, THEN rewrite the script to a 5th-grade reading level [SRC: Chase Chappell | 325]. 18. IF production is slow, THEN use "Storyblocks" footage with native text overlays to simulate UGC [SRC: Dara Denney | 736]. 19. IF you have a product with "Lag Time" (results take time), THEN use "Timeline Ads" (Day 1 vs Day 30 visuals) to bridge the gap [SRC: Tiana Asperjan | 30]. 20. IF ad account performance tanks, THEN check if you are over-segmenting; consolidate into Broad CBO [SRC: Sam Piliero | 753].

--------------------------------------------------------------------------------
F) VISUAL EXAMPLES (Diagnostic Patterns)
• The "Weird Rock" Pattern:
    ? Visual: Hand holding brown, textured resin (looks like poop/rocks).
    ? Mechanism: Curiosity Gap + Disgust/Intrigue.
    ? Result: High Hook Rate due to "What is that?" factor [SRC: Fraser Cottrell | 849].
• The "Apology" Pattern:
    ? Visual: Founder looking sad/serious, text "We Apologize."
    ? Mechanism: Pattern Interrupt (Brands usually brag, they don't apologize).
    ? Result: Stops scroll to see what went wrong (Twist: We lied about stock levels/quality) [SRC: J.B. | Vibe Marketing | 465].
• The "Fake News" Pattern:
    ? Visual: Header "Breaking News" or "Live", Chef holding knife.
    ? Mechanism: Authority + Urgency.
    ? Result: High CTR because it feels informational, not commercial [SRC: Franky Shaw | 236].
• The "Color Block" Pattern:
    ? Visual: Solid Black background, Yellow text, White product.
    ? Mechanism: Contrast against white FB/IG feed.
    ? Result: Involuntary eye attraction [SRC: Fraser Cottrell | 852].
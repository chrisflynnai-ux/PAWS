# CONTENT SCRIPT ARCHITECT — SKILL BRIEF + EXTRACTION STRATEGY
## CSA v1.0 | The Deep Video Production Skill

**Status:** Discovery → Ready for Extraction  
**Complexity:** Complex (Track C) — 30-50+ sources, extensive patterns  
**Domain:** copy  
**Priority:** P1  
**Estimated Build Time:** 8-12 hours  
**Date:** 2026-02-14

---

## 1. EXECUTIVE SUMMARY

### The Gap

The ULTRAMIND copy ecosystem has **zero coverage for non-conversion video production**:

| Skill | What It Owns | Video Depth |
|-------|-------------|-------------|
| **Short-Form VSL Writer** v2.0 | 5-10 min sales VSLs | Conversion only |
| **Long-Form VSL Architect** v2.0 | 12-20 min documentary VSLs | Conversion only |
| **Viral Theme Developer** v1.0 | Social posts/threads/carousels + hooks | Wide but shallow on video |
| **Master Writing Partner** v2.0 | Blog, social, email, website copy | Text only |
| **Copy Lead** v1.1.0 | Written sales pages | Text only |

**Nobody owns:**
- YouTube long-form educational/story-driven content
- YouTube algorithm optimization (retention curves, CTR engineering)
- Deep story arc construction (scene-level craft)
- Podcast scripts
- Webinar/presentation scripts
- Visual scripting methodology (beat sheets, B-roll, camera direction)
- Open loop / curiosity engineering for video
- Retention psychology for video (Dopamine Ladder, Q→A Spine)

### The Solution

**Content Script Architect (CSA)** — a deep video production skill that transforms ideas into retention-engineered, story-driven video scripts with visual direction. Owns everything from YouTube long-form to podcast scripts. Has its own video-specific hook system (distinct from VTD's text-first 13-C).

### Architecture Decision

```
Strategic Copy Director receives content brief
    │
    ├── WRITTEN CONTENT (text-first)
    │   ├── Sales pages, advertorials → Copy Lead
    │   ├── Blog, newsletter, website, social text → Master Writing Partner
    │   └── Email sequences → Email Copy Genius
    │
    ├── VIDEO SCRIPTS (camera/screen production)
    │   ├── Sales VSL 5-10 min → Short-Form VSL Writer
    │   ├── Sales VSL 12-20 min → Long-Form VSL Architect
    │   └── YouTube, educational, podcast, story-driven → Content Script Architect ← NEW
    │
    ├── SOCIAL CONTENT (platform-native posts)
    │   └── LinkedIn posts, X threads, carousels, short social → Viral Theme Developer
    │
    └── CROSS-CUTTING INFRASTRUCTURE
        ├── Voice consistency → Voice DNA / Voice Guide (shared SSOT)
        └── Distribution/growth strategy → VTD Social Growth Architect
```

### Routing Boundary: VTD vs CSA

| Signal | Routes To |
|--------|-----------|
| "Write me a LinkedIn post" | VTD |
| "Write me a YouTube script" | **CSA** |
| "Create an X thread" | VTD |
| "Script a 15-min educational video" | **CSA** |
| "Hook ideas for social" | VTD |
| "Hook + first 30 seconds for my video" | **CSA** |
| "Carousel about X" | VTD |
| "Podcast episode script" | **CSA** |
| "Short-form Reel/TikTok" | VTD (social-first) OR **CSA** (if production-heavy) |
| "Webinar script" | **CSA** |

**The bright line:** If it involves a camera/microphone and production planning, it's CSA. If it's typed-and-posted social content, it's VTD.

---

## 2. CSA CAPABILITY MAP

### What CSA Must Own (Unique Territory)

**A. Video Script Architecture**
- YouTube long-form structures (8-30+ min)
- Educational/tutorial structures (explain, demonstrate, apply)
- Story-driven content (documentary, journey, investigation)
- Thought leadership video (manifesto, contrarian thesis, vision piece)
- Podcast episode scripts (solo, interview prep, panel)
- Webinar/presentation scripts (teach + convert)
- Short-form video scripts with production depth (Shorts/Reels IF production-focused)

**B. Video-Specific Hook System**
- First 30 seconds engineering (different from text's first 3 lines)
- Title + Thumbnail + Hook trinity (video-specific)
- Audio hook vs visual hook vs text overlay hook (3-channel alignment for video)
- Cold open patterns (in medias res, provocative claim, impossible result)
- Hook-to-retention bridge (the first 30 → first 2 minutes connection)

**C. Retention Engineering for Video**
- Dopamine Ladder (6 levels: Stimulation → Captivation → Anticipation → Validation → Affection → Revelation)
- Q→A Spine (curiosity loops that carry viewers through)
- Open loop taxonomy (Question, Promise, Mystery, Tension, Countdown, Nested)
- Curiosity gap calibration (too small / too large / Goldilocks zone)
- Mid-video retention techniques (value drops, pattern breaks, tease-forward, recap+escalate)
- Platform retention curves (YouTube long-form vs Shorts vs podcast episode)
- Minute-by-minute pacing maps

**D. Story Arc Deep Patterns**
- 5+ master story arcs (Origin, Transformation, Discovery, Parable, Before/After mini-arc)
- Scene construction (sensory detail, dialogue/narration balance, show-don't-tell)
- Emotional beat mapping (scene-level pacing)
- PAST framework depth (Place, Action, Sensation, Thought)
- Story → lesson bridges (narrative exit ramps into teaching)
- Tension engineering (stakes escalation, vulnerability, contrast, worst-moment technique)

**E. Visual Scripting Methodology**
- Two-column script format (audio | visual)
- Beat sheets for video (timing, B-roll cues, graphics cues)
- B-roll strategy (illustrative, metaphorical, proof, pattern interrupt)
- Camera direction level (talking head, screen share, whiteboard, location, mixed)
- Text-on-screen strategy (key phrase reinforcement, data visualization, captions)
- Cut timing / pacing (3-second rule, jump cuts, smooth transitions)
- Production notes format (what director/editor needs)

**F. Platform Algorithm Optimization**
- YouTube long-form signals (CTR benchmarks, retention % targets, session time)
- YouTube Shorts algorithm mechanics
- Podcast discovery optimization (episode titles, descriptions, clip strategy)
- Content pillar architecture (series, playlists, topic clusters)
- Packaging optimization (title formulas, thumbnail frameworks, description templates)

### What CSA References (From Other Skills)

| Referenced From | What CSA Borrows | How |
|----------------|-----------------|-----|
| VTD's Voice DNA | Voice consistency in scripts | References VOICE_GUIDE SSOT |
| VTD's EVR concept | Reality > Expectations retention | Adapts for video (visual reality gaps) |
| Long-Form VSL | Documentary structure patterns | Adapts belief-building for non-sales |
| Short-Form VSL | Value equation, COMPEL system | References for conversion-adjacent content |
| Compendium | Dopamine Ladder, Q→A Spine, PAST, Hook typology | Direct integration (these are CSA-native) |

---

## 3. KNOWLEDGE INVENTORY

### Already Extracted (Compendium — 811 lines)

The Master Script Compendium provides strong foundations in these areas:

| Compendium Module | CSA Relevance | Depth |
|-------------------|---------------|-------|
| M1: Avatar Intelligence | Universal | ✅ Good |
| M2: Idea Architecture | Topic→script development | ✅ Good |
| M3: Packaging System | Title/thumb/hook for video | ✅ Good |
| M4: Hook Arsenal | Hook types for video | ⚠️ Needs video-specific depth |
| M5: Retention Architecture | Dopamine Ladder, Q→A Spine | ✅ Good foundation, needs platform data |
| M6: Story Loop Engineering | PAST framework, story arcs | ⚠️ Thin — needs scene construction depth |
| M7: Controlled Authority | Trust in video | ✅ Good |
| M8: Clarity Pyramid | Explanation methodology | ✅ Good |
| M9: Offer Architecture | Soft-sell in content | ⚠️ VSL-heavy, needs content adaptation |
| M10: Testing & Repackaging | Iteration | ✅ Good |
| F5: Dopamine Ladder | 6-level retention | ✅ Good |
| F8: Q→A Spine | Curiosity loop engineering | ✅ Good |
| F12: PAST Framework | Scene construction | ⚠️ Mentioned but not deep |
| F14: Hook Typology | Video hooks | ⚠️ Needs expansion |

### Extraction Gaps (What 30-50 Sources Must Fill)

| Gap | Priority | Source Types Needed |
|-----|----------|-------------------|
| **Content script structures** (non-VSL) | 🔴 Critical | YouTube creator courses, educational video methodology |
| **Deep story arcs / scene construction** | 🔴 Critical | Storytelling masterclasses, screenwriting for video |
| **Video-specific hooks (first 30 sec)** | 🔴 Critical | YouTube growth channels, hook analysis content |
| **Platform algorithm optimization** | 🔴 Critical | YouTube strategy content, creator economy analysis |
| **Open loop / curiosity engineering** | 🟡 High | Retention psychology, content strategy courses |
| **Visual scripting methodology** | 🟡 High | Video production courses, editor workflow content |
| **Podcast script structures** | 🟡 High | Podcasting methodology, interview frameworks |
| **Educational video optimization** | 🟡 High | EdTech content, explanation methodology |
| **Retention curve analytics** | 🟠 Medium | YouTube analytics deep-dives, data-driven content strategy |
| **Short-form production patterns** | 🟠 Medium | Short-form creator courses (distinct from VTD social) |

---

## 4. EXTRACTION STRATEGY — 7 SEQUENTIAL RUNS

### Source Targeting Guidance

**Ideal source mix (30-50 sources across all runs):**

- 10-15 YouTube long-form creator strategy sources (Paddy Galloway, Film Booth, Think Media, Colin & Samir, etc.)
- 5-8 storytelling/screenwriting for digital video sources
- 5-8 retention psychology / hook engineering for video
- 3-5 podcast scripting methodology sources
- 3-5 educational video / explanation methodology sources
- 3-5 visual direction / production workflow sources
- 2-3 algorithm / analytics deep-dive sources

---

### RUN 1: CONTENT SCRIPT ARCHITECTURE (Non-VSL Structures)
**Focus:** YouTube long-form, educational, story-driven, tutorial, thought leadership
**Expected Atoms:** 8-12

```markdown
# NOTEBOOKLM EXTRACTION: Content Script Architect — RUN 1: SCRIPT STRUCTURES

## CONTEXT
I am building a Content Script Architect skill for the ULTRAMIND ecosystem.
This skill owns ALL non-sales video production: YouTube long-form, educational,
story-driven, podcast, webinar, thought leadership video.

This run extracts SCRIPT STRUCTURES — the macro-architectures for different
video types. These are NOT sales VSLs (we have separate skills for those).

## SOURCE BASE
[Your sources about YouTube content creation, educational video, etc.]

## EXTRACTION TASK

**Extract ONLY script structures** — the overall architecture/skeleton for
different types of non-sales video content.

For each structure, generate an atom using this exact format:

---

# ATOM: framework.content_script.[structure_name].v1
# Source Ref: [Video/Course name + timestamp/section]

## 1. STRUCTURE IDENTITY

- **Name:** [Structure name — e.g., "The Explanation Arc"]
- **Video Type:** [Educational | Story-Driven | Documentary | Tutorial |
  Thought Leadership | Hybrid]
- **Ideal Length:** [Time range — e.g., "10-20 minutes"]
- **Best For:** [When this structure excels — e.g., "Complex topics that
  need progressive understanding"]
- **Platform:** [YouTube Long | YouTube Short | Podcast | Webinar | Universal]

## 2. MACRO-STRUCTURE (The Skeleton)

- **Section 1:** [Name] — [Purpose] — [% of total runtime] — [Key technique]
- **Section 2:** [Name] — [Purpose] — [% of total runtime] — [Key technique]
- **Section 3:** [Name] — [Purpose] — [% of total runtime] — [Key technique]
- [Continue for all sections...]

Example format:
- **Hook (0-30sec, 3-5%):** Pattern interrupt → Promise → "Stay for X"
- **Context (30sec-2min, 10%):** Why this matters now → Stakes → Credibility
- **Core Teaching (2-12min, 60%):** Point 1 → Point 2 → Point 3 [with details]
- **Application (12-16min, 20%):** How to use this → Examples → Common mistakes
- **Close (16-18min, 7%):** Summary → Transformation statement → CTA

## 3. RETENTION MECHANICS (Built Into Structure)

- **Where viewers typically drop:** [Danger zones in this structure]
- **Built-in retention tools:** [How structure prevents drop-off]
- **Pacing pattern:** [Fast-slow-fast? Steady build? Oscillating?]

## 4. DIFFERENTIATION

- **How this differs from a VSL:** [What makes it non-sales]
- **How this differs from generic "how-to":** [What makes it engineered]
- **Unique advantage:** [Why use this structure vs alternatives]

## 5. CROSS-REFERENCES

- **Related Structures:** [Which other structures complement this]
- **When to combine:** [Hybrid scenarios]

---

## STRUCTURES TO LOOK FOR

Extract as many distinct structures as the sources contain. Priority targets:

1. **The Explanation Arc** — Complex topic → progressive understanding
2. **The Investigation** — "I tried X for 30 days" / "Testing the claim"
3. **The Documentary** — Story-first, teaching embedded in narrative
4. **The Tutorial** — Step-by-step "do this" instruction
5. **The Listicle Video** — "7 mistakes", "5 strategies", ranked/unranked
6. **The Comparison** — "X vs Y" / "Which is better?"
7. **The Manifesto** — Thought leadership, vision piece, contrarian thesis
8. **The Case Study** — "How [person/company] achieved [result]"
9. **The Roundup/Review** — Product reviews, tool comparisons
10. **The Story-Lesson Hybrid** — Personal story → universal principle
11. **The Q&A / FAQ** — Answering audience questions
12. **The Behind-the-Scenes** — Process reveal, transparency content

Also extract:
- **Podcast structures** (solo episode, interview, panel)
- **Webinar structures** (teach → convert)
- **Series/playlist architecture** (multi-episode arcs)

## OUTPUT CONSTRAINTS
- Each atom: 2-3 pages MAX
- Naming: framework.content_script.[descriptive_name].v1
- Include the percentage time allocation per section
- Include retention mechanics per structure
- If a structure is platform-specific, note which platform
```

---

### RUN 2: VIDEO HOOK ENGINEERING (First 30 Seconds)
**Focus:** Video-specific hooks, title+thumbnail+hook trinity, cold opens
**Expected Atoms:** 8-10

```markdown
# NOTEBOOKLM EXTRACTION: Content Script Architect — RUN 2: VIDEO HOOKS

## CONTEXT
I am building a Content Script Architect skill that needs its OWN video-specific
hook system. We already have VTD's 13-C Engine for social text hooks — this is
DIFFERENT. Video hooks operate in a multi-sensory environment (audio + visual +
text overlay simultaneously) and must solve the "first 30 seconds" problem.

## IMPORTANT DISTINCTION
- VTD 13-C = text-first hooks for social posts (first 3 lines)
- CSA hooks = video-first hooks (first 30 seconds, multi-channel)

Do NOT extract generic "hook formulas." Extract specifically how video hooks
work differently from text hooks.

## EXTRACTION TASK

**Extract ONLY video hook patterns** — how the first 30 seconds of a
non-sales video retains viewers.

For each pattern, generate an atom:

---

# ATOM: pattern.video_hook.[pattern_name].v1
# Source Ref: [Citation]

## 1. HOOK IDENTITY

- **Name:** [Pattern name — e.g., "The Impossible Result Open"]
- **Type:** [Cold Open | Direct Promise | Question Hook | In Medias Res |
  Provocative Claim | Story Fragment | Pattern Interrupt | Data Shock]
- **Best For:** [Which video types this works with]
- **Time to Execute:** [How many seconds this hook takes]

## 2. THE MULTI-CHANNEL FORMULA

**Audio (what they hear):**
[Exact formula with timing — e.g., "Sentence 1 (0-3sec): Direct claim.
Sentence 2 (3-8sec): Why that claim matters. Sentence 3 (8-15sec): What's
coming in this video."]

**Visual (what they see):**
[What should be on screen during each audio beat — talking head, B-roll,
text overlay, prop, location, screen recording, etc.]

**Text Overlay (what they read):**
[Any on-screen text that reinforces the hook — key phrase, stat, question]

## 3. THE 30-SECOND MAP

- **0-3 seconds:** [Scroll-stop moment — what grabs]
- **3-10 seconds:** [Context lock — why they should care]
- **10-20 seconds:** [Promise/curiosity — what's coming]
- **20-30 seconds:** [Transition to content — bridge to body]

## 4. TITLE + THUMBNAIL + HOOK TRINITY

- **How title sets up this hook:** [Relationship between title and first words]
- **How thumbnail complements:** [Visual promise that hook confirms]
- **Alignment test:** [How to verify all three point same direction]

## 5. FAILURE MODES

- **What kills this hook:** [Common mistakes]
- **Retention cliff risk:** [Where viewers leave if hook isn't tight]

---

## HOOK TYPES TO LOOK FOR

1. **Cold Open (In Medias Res)** — Start in the middle of action/result
2. **The Impossible Result** — "I did X and got [shocking result]"
3. **The Contrarian Claim** — "Everything you know about X is wrong"
4. **The Direct Question** — Rhetorical question that creates curiosity
5. **The Story Fragment** — Start a story, pause before resolution
6. **The Data Shock** — Lead with a surprising statistic
7. **The Pattern Interrupt** — Something visually/audibly unexpected
8. **The Preview Montage** — Quick cuts showing what's coming
9. **The "If You" Filter** — "If you're [avatar], this video..."
10. **The Time Contrast** — "X took me 3 years. This video: 15 minutes."

Also extract:
- **Hook-to-retention bridge** (how hook connects to body — not just first 3 seconds but the whole first 30-60 seconds as a unit)
- **Title formulas** specific to YouTube (curiosity gap, benefit, how-to, listicle)
- **Thumbnail frameworks** (visual patterns that drive CTR)
- **The "re-hook" at 30 seconds** (second hook after initial grab)

## OUTPUT CONSTRAINTS
- Each atom: 2-3 pages MAX
- Naming: pattern.video_hook.[descriptive_name].v1
- MUST include the multi-channel formula (audio + visual + text)
- MUST include timing (second-by-second for first 30 sec)
- Distinguish from text-only hooks explicitly
```

---

### RUN 3: RETENTION ENGINEERING & CURIOSITY LOOPS
**Focus:** Dopamine Ladder depth, open loop taxonomy, mid-video retention, pacing
**Expected Atoms:** 6-8

```markdown
# NOTEBOOKLM EXTRACTION: Content Script Architect — RUN 3: RETENTION ENGINEERING

## CONTEXT
Building a Content Script Architect. This run goes DEEP on retention mechanics
— how to keep viewers watching through an entire video. We have surface-level
concepts (Dopamine Ladder, Q→A Spine, rehooks) from our compendium. Now we
need the ENGINEERING depth: how these work minute-by-minute, how they interact,
how they differ by platform and video length.

## EXTRACTION TASK

**Extract retention engineering patterns** — the mechanics of keeping viewers
watching through complete videos.

For each pattern, generate an atom:

---

# ATOM: [category].[name].v1
# Source Ref: [Citation]

## 1. MECHANISM

- **What it is:** [The retention technique]
- **Why it works psychologically:** [The brain science / behavior driver]
- **Where in video it applies:** [Beginning / Middle / End / Throughout]

## 2. IMPLEMENTATION

- **How to script it:** [Exact scripting technique]
- **Timing/frequency:** [How often, at what intervals]
- **Example in context:** [Real or constructed example]

## 3. PLATFORM VARIATION

- **YouTube long-form:** [How this works in 10-20 min videos]
- **YouTube Shorts:** [How this adapts for <60 sec]
- **Podcast:** [How this works in audio-only]

## 4. FAILURE MODES

- **Overuse:** [What happens if you do too much]
- **Underuse:** [What happens if you skip it]
- **Misuse:** [Common mistakes]

---

## RETENTION PATTERNS TO EXTRACT

**Open Loop Taxonomy:**
1. Question Loops — "Why does X happen?" (answered later)
2. Promise Loops — "I'll show you the solution in a moment"
3. Mystery Loops — "Something unexpected happened..."
4. Tension Loops — Unresolved conflict carrying forward
5. Countdown Loops — "Third of five secrets..." (completionist drive)
6. Nested Loops — Loops within loops (story inside a lesson inside a larger narrative)

For each loop type: how to open, when to close, optimal nesting depth,
what happens if you close too early/late.

**Dopamine Ladder Engineering:**
- How each level maps to video pacing
- When to escalate vs plateau
- How different video types use different ladders
- Minute-by-minute dopamine pacing maps

**Mid-Video Retention Techniques:**
- Value drops (unexpected bonus value)
- Pattern breaks (change of pace, format shift, visual change)
- Tease-forward ("but the next part is even more surprising")
- Recap + escalate (remind what we learned, raise stakes)
- Audience callouts ("if you're the kind of person who...")
- Payoff deliveries (close a loop, then open a new one)

**Retention Curves:**
- YouTube long-form typical retention shape
- Where viewers drop (minute 2-3, minute 7-8, etc.)
- "Minute 8 cliff" prevention strategies
- Short-form retention (first 3 seconds, middle, replay trigger)

## OUTPUT CONSTRAINTS
- Each atom: 2-3 pages MAX
- MUST include timing data (when in video)
- MUST include platform-specific variation
- Distinguish between loop TYPES (not just "use open loops")
```

---

### RUN 4: STORY ARC DEEP PATTERNS & SCENE CONSTRUCTION
**Focus:** Master story arcs, scene-level craft, emotional pacing, PAST depth
**Expected Atoms:** 6-8

```markdown
# NOTEBOOKLM EXTRACTION: Content Script Architect — RUN 4: STORY ARCS

## CONTEXT
Building a Content Script Architect. This run goes DEEP on storytelling for
video — not screenwriting theory, but practical story construction for YouTube,
podcasts, and educational content. We need the scene-level craft that makes
stories LAND in video format.

Our compendium has the PAST framework (Place, Action, Sensation, Thought) but
it's thin. We need full depth: how to construct scenes, pace emotion, build
tension, bridge stories into lessons, and choose which arc fits which video.

## EXTRACTION TASK

**Extract story patterns** — arcs, scene construction, emotional engineering
for video content.

For each pattern, generate an atom:

---

# ATOM: framework.story.[name].v1
# Source Ref: [Citation]

---

## STORY ARCS TO EXTRACT

**Master Arcs (extract template + time allocation + emotional map for each):**
1. **The Origin Story** — "How I got here" (credibility + connection)
2. **The Transformation Arc** — "I was X, now I'm Y" (proof + aspiration)
3. **The Discovery Journey** — "I found something and here's what happened"
4. **The Parable** — Other person's story → universal lesson
5. **The Before/After Mini-Arc** — Compressed transformation (for mid-video)
6. **The Investigation** — "I tested X / tried X / went to X"
7. **The Failure-to-Wisdom** — "I failed at X, here's what I learned"
8. **The David vs Goliath** — "Everyone said it couldn't be done"

For each arc: section breakdown with % time, emotional curve (tension map),
where the lesson emerges, how to exit story into teaching.

**Scene Construction (the CRAFT level):**
- PAST framework depth: Place → Action → Sensation → Thought
  (How to write each element for video; how much detail; when to expand vs compress)
- Sensory detail for video: What to DESCRIBE vs what to SHOW
- Dialogue vs narration: When to quote directly vs paraphrase
- Show don't tell: How this works differently in video vs text
- The "worst moment" technique: Going to the bottom before the turn
- Vulnerability calibration: How much is authentic vs oversharing

**Emotional Beat Mapping:**
- How to map emotion across a video (not just "build tension")
- The tension-release-tension cycle
- Stakes escalation patterns
- Contrast engineering (juxtapose high/low, before/after, expected/actual)
- The "turn" — where story shifts direction (timing + technique)
- Landing the lesson: How to exit a story into a teaching point without whiplash

**Story → Lesson Bridges:**
- The "narrative exit ramp" technique
- "What this taught me" bridge
- "And this is where most people miss it" bridge
- "The principle behind the story" bridge
- How to avoid the "and then he gave a TED talk" antipattern

## OUTPUT CONSTRAINTS
- Each atom: 2-3 pages MAX
- MUST include emotional beat maps (where tension rises/falls)
- MUST include video-specific application (not just prose storytelling)
- MUST include time allocation for each arc element
```

---

### RUN 5: VISUAL SCRIPTING & PRODUCTION DIRECTION
**Focus:** Beat sheets, B-roll strategy, camera direction, text-on-screen, pacing
**Expected Atoms:** 5-7

```markdown
# NOTEBOOKLM EXTRACTION: Content Script Architect — RUN 5: VISUAL SCRIPTING

## CONTEXT
Building a Content Script Architect. This run extracts VISUAL SCRIPTING
methodology — how to script what the camera shows, not just what the host says.
Most script skills stop at words. CSA scripts the complete viewer experience.

## EXTRACTION TASK

**Extract visual scripting patterns** — how to direct the visual experience
alongside the audio/verbal script.

For each pattern, generate an atom:

---

# ATOM: spec.visual_scripting.[name].v1
# Source Ref: [Citation]

---

## VISUAL PATTERNS TO EXTRACT

**Script Format:**
- Two-column format (Audio | Visual) — when and how to use
- Inline visual cues format — "[B-ROLL: factory floor]" style
- Beat sheet format — timing + visual + audio + text overlay + emotion
- Which format for which video type
- What level of visual direction to include (minimal notes vs full direction)

**B-Roll Strategy:**
- Illustrative B-roll (shows what you're talking about)
- Metaphorical B-roll (visual metaphor for abstract concept)
- Proof B-roll (evidence, screenshots, data)
- Pattern interrupt B-roll (unexpected visual to reset attention)
- Ambient/aesthetic B-roll (mood, energy, texture)
- B-roll timing: how long per cut, when to cut, how often
- "B-roll density" — how much B-roll vs talking head per video type

**Camera Direction for Creators:**
- Talking head compositions (framing, eye line, energy levels)
- Screen share/screencast scripting (what to show when)
- Whiteboard/drawing segments (pacing, reveal timing)
- Location shoots (environmental storytelling)
- Mixed format (when to switch between modes)
- Energy levels on camera (calm authority vs high energy vs conversational)

**Text on Screen:**
- Key phrase reinforcement (when spoken word needs visual echo)
- Data visualization cues (charts, numbers, stats)
- Caption/subtitle strategy (always-on vs key moments)
- Lower thirds (identification, topic labels)
- Text hook overlays (bold text that reinforces spoken hook)
- "Highlight text" moments (zoom to specific text/quote)

**Visual Pacing:**
- Cut timing by video type (educational = slower, entertainment = faster)
- The "3-second rule" (max time on single visual)
- Jump cut pacing (when to use, how to script pauses for cuts)
- Motion as retention (movement keeps attention)
- Static vs dynamic balance (too much static = boring, too much motion = chaotic)
- Visual pattern breaks (deliberate change in visual style for emphasis)

## OUTPUT CONSTRAINTS
- Each atom: 2-3 pages MAX
- MUST include specific timing guidance
- MUST include examples of each pattern in a script context
- Focus on SCRIPTING the visuals, not editing/post-production
```

---

### RUN 6: PLATFORM OPTIMIZATION & ALGORITHM SIGNALS
**Focus:** YouTube algorithm mechanics, retention benchmarks, CTR, series architecture
**Expected Atoms:** 5-7

```markdown
# NOTEBOOKLM EXTRACTION: Content Script Architect — RUN 6: PLATFORM OPTIMIZATION

## CONTEXT
Building a Content Script Architect. This run extracts platform-specific
optimization data — how YouTube (and other platforms) evaluate and distribute
content, and how to script FOR the algorithm, not against it.

## EXTRACTION TASK

**Extract platform optimization patterns** — algorithm signals, benchmarks,
and scripting strategies that improve distribution.

For each pattern, generate an atom:

---

# ATOM: spec.platform.[name].v1
# Source Ref: [Citation]

---

## PLATFORM PATTERNS TO EXTRACT

**YouTube Long-Form Algorithm:**
- CTR benchmarks by niche (what's "good" CTR)
- Retention % targets (30-sec, 2-min, 50%, end-of-video)
- Average view duration signals (AVD vs video length optimization)
- Session time impact (how video length affects recommendation)
- Impression → click → watch funnel
- When YouTube "tests" a video (browse, suggested, search paths)
- How script choices affect algorithm signals

**YouTube Shorts Algorithm:**
- Replay rate importance (what drives Shorts distribution)
- Completion rate targets
- Loop scripting (ending that triggers replay)
- Swipe-away prevention (first-frame optimization)
- Engagement signals (comments, shares, saves)

**Packaging Optimization:**
- Title formulas that drive CTR (curiosity gap, benefit, how-to, listicle, number, contrast)
- Thumbnail frameworks (face + text, before/after, abstract, tool/prop)
- Description templates (first 2 lines, chapters, links)
- Title + thumbnail A/B testing methodology
- "Packaging is 50% of success" — how to script with packaging in mind

**Content Architecture for Growth:**
- Pillar content strategy (breadth vs depth, topic clusters)
- Series architecture (episodic, seasonal, thematic)
- Playlist optimization (binge-watching engineering)
- Content calendar for different growth stages
- New vs returning viewer content balance
- "Gateway video" strategy (designed to introduce new audience)

**Podcast-Specific Optimization:**
- Episode title optimization (search vs browse)
- Show notes/descriptions for discovery
- Clip strategy (full episode → short clips for social)
- Interview structure optimization
- Solo episode pacing
- Listener retention patterns (audio-specific)

## OUTPUT CONSTRAINTS
- Each atom: 2-3 pages MAX
- MUST include actual benchmarks/numbers where available
- MUST connect algorithm signals to SCRIPTING decisions
- Focus on what the SCRIPT WRITER controls, not the editor/publisher
```

---

### RUN 7: EDUCATIONAL VIDEO & PODCAST DEEP PATTERNS
**Focus:** Explanation methodology, tutorial pacing, podcast structures
**Expected Atoms:** 5-7

```markdown
# NOTEBOOKLM EXTRACTION: Content Script Architect — RUN 7: EDUCATIONAL + PODCAST

## CONTEXT
Building a Content Script Architect. This final run goes deep on two specific
video types that need their own methodology: educational/explanation videos and
podcast scripts. These are distinct from story-driven or hook-driven content —
they have their own craft.

## EXTRACTION TASK

**Extract educational and podcast patterns** — how to explain complex topics
engagingly, and how to structure podcast episodes.

For each pattern, generate an atom:

---

# ATOM: [category].[name].v1
# Source Ref: [Citation]

---

## EDUCATIONAL VIDEO PATTERNS TO EXTRACT

**Explanation Methodology:**
- The "known → unknown" bridge (start from what they know)
- Analogy engineering (complex → familiar comparison)
- Progressive complexity (layer understanding, don't dump)
- The "aha moment" design (engineering the insight moment)
- Visual explanation: when to draw/diagram vs tell
- The "wrong way first" technique (show common mistake before correct approach)

**Tutorial Scripting:**
- Step-by-step pacing (how long per step, when to pause)
- "Follow along" vs "watch then do" structure
- Prerequisite handling (when to explain vs assume)
- Error prevention scripting (anticipate mistakes, address proactively)
- Tool/software walkthrough pacing

**Teaching Retention (different from entertainment retention):**
- "Value stacking" — each minute feels more valuable than the last
- Comprehension checkpoints (mini-summaries that help retention)
- Application prompts ("pause the video and try this")
- The "so what" bridge (why this matters after explaining what it is)

**Complexity Management:**
- How to simplify without dumbing down
- Jargon introduction protocol (when to define, when to avoid)
- Cognitive load management (too much info = viewer leaves)
- "Chunk and check" pattern (teach chunk → verify understanding → next chunk)

## PODCAST PATTERNS TO EXTRACT

**Solo Episode Structures:**
- Monologue arc (thesis → evidence → conclusion → call to action)
- "Notes to self" format (conversational solo thinking-out-loud)
- Lesson-of-the-week format
- Storytelling solo format (narrative-driven)
- Rant format (controlled passion on a topic)

**Interview Structures:**
- Question arc design (warm-up → depth → insight → close)
- "Signature question" technique (recurring question across guests)
- Follow-up engineering (going deeper, not just next question)
- Story extraction questions ("tell me about a time when...")
- Handling tangents (when to follow, when to redirect)
- Pre-interview research template

**Podcast-Specific Retention:**
- Opening ritual / cold open choice
- Mid-episode engagement ("if you're enjoying this, here's what's coming...")
- Listener interaction hooks (ask questions for social)
- Episode-to-episode bridges (series thinking)
- Audio pacing (silence, speed variation, emphasis)

## OUTPUT CONSTRAINTS
- Each atom: 2-3 pages MAX
- Naming: framework.educational.[name].v1 or framework.podcast.[name].v1
- MUST include timing/pacing guidance
- MUST distinguish from entertainment video patterns
```

---

## 5. POST-EXTRACTION: CROSS-REFERENCE QUERIES

After all 7 runs, upload atoms to fresh NotebookLM notebook and run these queries:

### Query 1: Hook → Retention Connection
```
"How do video hooks (Run 2 atoms) connect to retention mechanics (Run 3 atoms)?
Map which hook types naturally lead into which retention patterns."
```

### Query 2: Structure → Story Integration
```
"Which script structures (Run 1) naturally incorporate which story arcs (Run 4)?
Create a compatibility matrix."
```

### Query 3: Gap Analysis
```
"Based on the complete atom library, what knowledge gaps remain for building
a production-quality Content Script Architect? What atoms are missing?"
```

### Query 4: Contradiction Check
```
"Do any atoms contradict each other? Where do different sources disagree
about video scripting best practices?"
```

### Query 5: Synthesis Clusters
```
"Group all atoms into logical clusters for the final skill build:
- Core Script Engine Cluster (structures + hooks + retention)
- Story Craft Cluster (arcs + scenes + emotional pacing)
- Visual Production Cluster (beat sheets + B-roll + camera)
- Platform Optimization Cluster (algorithm + packaging + growth)
- Specialized Format Cluster (educational + podcast + tutorial)"
```

---

## 6. SYNTHESIS PLAN (Post-Extraction)

### CSA Skill Bundle (Double-II Output)

**SKILL.md** — Information layer with:
- Zero-Point Schema (< 100 tokens)
- Core Thesis: Video scripts as retention-engineered experiences
- 5+ script structures with complete templates
- Video hook system (distinct from VTD 13-C)
- Retention engineering playbook
- Story arc library with scene construction guide
- Visual scripting methodology
- Platform optimization reference
- Educational + podcast modules

**implementation.py** — Code layer with:
- Pydantic models for script I/O
- Script structure router (video type → optimal structure)
- Hook generator (video-specific)
- Retention analyzer (checks for loop placement, pacing, etc.)
- Visual direction formatter (generates two-column scripts)
- Platform optimization checker

**flowgram.mmd** — Visual bridge showing:
- Idea → Structure Selection → Hook → Retention Planning → Story Integration → Visual Direction → Script → Quality Check

**zero_point.json** — Index with:
- Trigger keywords, routing rules, integration points

### Progressive Disclosure Layers

| Layer | Token Budget | Contents |
|-------|-------------|----------|
| **L1** | < 500 | Quick ref, structure router, hook types, routing rules |
| **L2** | < 1500 | Core execution: structure templates, hook formulas, retention checklist |
| **L3** | < 3000 | Deep patterns: story arcs, scene construction, visual scripting |
| **L4** | < 6000 | Complete reference: all structures, all hooks, all arcs, platform data, golden runs |

### Quality Gates (CSA-Specific)

| Gate | What It Checks |
|------|---------------|
| **Structure Gate** | Script follows identified structure with correct time allocation |
| **Hook Gate** | First 30 seconds engineered with multi-channel formula |
| **Retention Gate** | Open loops placed, Dopamine Ladder pacing, no dead zones |
| **Story Gate** | Story arcs have scene construction, emotional beats mapped |
| **Visual Gate** | Visual direction included, B-roll cued, text-on-screen noted |
| **Platform Gate** | Script optimized for target platform's algorithm signals |
| **Voice Gate** | Script matches VOICE_GUIDE (references shared SSOT) |

---

## 7. INTEGRATION MAP

### Sister Skills Coordination

```yaml
sister_skills:
  strategic_copy_director:
    role: "Routes video briefs to CSA"
    handoff: "SCD provides brief, CSA returns script"
    authority: "SCD = strategic direction, CSA = script craft"

  viral_theme_developer:
    role: "Social + hooks; CSA is video depth"
    boundary: "Text posts → VTD. Video scripts → CSA. Shorts → context-dependent"
    shared: "Both reference VOICE_GUIDE SSOT"
    no_overlap: "CSA has own hook system for video; does NOT use 13-C"

  short_form_vsl_writer:
    role: "Sales VSLs (5-10 min warm traffic)"
    boundary: "Sales intent → VSL skills. Growth/trust intent → CSA"

  long_form_vsl_architect:
    role: "Sales VSLs (12-20 min documentary)"
    boundary: "Conversion goal → LFVA. Education/authority goal → CSA"
    shared_patterns: "Documentary structure adapted differently for sales vs content"

  master_writing_partner:
    role: "Text-first content generalist"
    boundary: "Written content → MWP. Video scripts → CSA"
    handoff: "MWP may request CSA for video repurposing of written content"
```

### SSOT Contracts

```yaml
required_inputs:
  - VIDEO_BRIEF: "Topic, audience, platform, goal, length target"
  - CONTENT_TYPE: "Educational | Story-Driven | Tutorial | Documentary |
                    Thought Leadership | Podcast | Webinar"

recommended_inputs:
  - VOICE_GUIDE: "Voice profile for script consistency"
  - MESSAGE_SPINE: "If content aligns with strategic messaging"
  - EVIDENCE_PACK: "If making claims that need proof"

primary_outputs:
  - VIDEO_SCRIPT: "Complete script with visual direction"
  - HOOK_OPTIONS: "3-5 video hooks with multi-channel formulas"
  - PACKAGING_SPEC: "Title options + thumbnail concepts + description"

secondary_outputs:
  - RETENTION_MAP: "Minute-by-minute retention engineering plan"
  - VISUAL_DIRECTION: "B-roll cues, text overlays, camera notes"
  - REPURPOSE_BRIEF: "How to extract social content from this video"
```

---

## 8. BUILD TIMELINE

| Phase | Activity | Time | Output |
|-------|----------|------|--------|
| **Extraction** | 7 NotebookLM runs | 4-6 hours | 43-59 atoms |
| **Organization** | Atom library + folder structure | 30 min | Organized atom library |
| **Cross-Reference** | 5 NotebookLM queries | 1 hour | Clustered, gap-checked atoms |
| **Synthesis** | Claude compilation → Double-II bundle | 2-3 hours | SKILL.md + implementation.py + flowgram.mmd + zero_point.json |
| **Polish** | Constitution v2.1 compliance + tests | 1-2 hours | Production-ready skill |
| **Total** | | **8-12 hours** | CSA v1.0 Production |

---

## 9. SUCCESS CRITERIA

CSA v1.0 is complete when:

- [ ] Covers 5+ distinct video script structures (non-VSL)
- [ ] Has its own video-specific hook system (not VTD 13-C)
- [ ] Includes retention engineering (Dopamine Ladder, open loops, pacing maps)
- [ ] Has deep story arc patterns (3+ arcs with scene-level construction)
- [ ] Includes visual scripting methodology (beat sheets, B-roll, camera)
- [ ] Platform optimization for YouTube + podcast
- [ ] Educational + tutorial + podcast structures included
- [ ] Clear routing boundary with VTD (no overlap)
- [ ] References VOICE_GUIDE SSOT (doesn't duplicate voice system)
- [ ] Passes Constitution v2.1 compliance
- [ ] Progressive disclosure L1-L4 within token budgets
- [ ] Integration points with all sister skills documented
- [ ] 3+ Golden Runs with complete input → output examples

---

*Content Script Architect — Skill Brief v1.0*
*"Scripts that retain. Stories that transform. Visuals that direct."*
*Knowledge → Intelligence → Autonomy*

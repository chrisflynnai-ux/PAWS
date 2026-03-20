# ORCHESTRATION FINALIZATION & PROJECT BASE PLAN
## From Skill Arsenal to Operational Assembly Lines

**Date:** 2026-02-15  
**Context:** LFVA v3.0 + SFVW v3.0 complete. Full skill ecosystem review conducted.  
**Goal:** Finalize orchestrators + build manual project bases for Sales Pages and VSLs.

---

## PART 1: DIAGNOSTIC — WHAT EXISTS VS WHAT'S NEEDED

### The Skill Arsenal (Current State)

```
PRODUCTION READY (v2.x or v3.x):
├── LFVA v3.0.0 ✅ (1,555 lines — just built)
├── SFVW v3.0.0 ✅ (1,448 lines — recently upgraded)
├── CSA v1.0.0 ✅ (Content Script Architect)
├── Copy Lead ✅ (strategic angle selection)
├── MMA v1.0.0 ✅ (1,066 lines — quality guardian)
├── ZPWO v3.0 Micro ✅ (543 lines — lean orchestrator)
├── HPE v2.1 ✅ (Human Persuasion Editor)
├── NRA v2.1 ✅ (Neuro-Resonance Auditor)
├── MWP v2.0 ✅ (Master Writing Partner — 77KB)
├── Email Copy Genius v2.0 ✅
├── Advertorial Copy Master v2.0 ✅
├── Sales Page Copywriter v2.0 ✅
├── Market Intelligence Synthesizer v2.1 ✅
├── Evidence Pack Builder v1.0 ✅
├── Viral Theme Developer v2.0 ✅ (87KB)
├── Offer Architect v2.0 ✅ (69KB)
├── Viral Resonance Architect ✅
└── Cold Outreach Architect ✅

PLANNED v3 UPGRADES (Atoms-ready, knowledge bases identified):
├── HPE → v3.0
├── NRA → v3.0
├── MWP → v3.0
├── Email Copy Genius → v3.0
├── Advertorial Copy Master → v3.0
├── Sales Page Copywriter → v3.0
├── Market Scout → v3.0
├── Research Ops → v3.0
└── MIS → v3.0

MISSING / TBA:
├── Copy Director ❌ (THE critical gap — strategic routing layer)
├── Skeptic Avatar / Red Team ❌ (spec exists, not built)
├── Sales Copy Consistency Contract → needs v3 alignment
└── ZPWO v4 (4-Track aware) ❌ (current v3 is 3-phase only)
```

### The Orchestration Layer (Current State)

```
DOCUMENT                          STATUS    ISSUE
─────────────────────────────────────────────────────────────
ZPWO v3.0 Micro                   ✅ Live   3-phase model, not 4-track
ORCHESTRATOR_CORE v4.1             ✅ Live   Two-Brain model, good foundations
SUB_AGENT_CONFIGS v2.0             ✅ Live   References v2.0 skills (stale)
ORCHESTRATION_INTEGRATION_GUIDE    ✅ Live   ZPWO↔TWA↔TWE↔MMA mapped
MMA v1.0.0                        ✅ Live   Solid, minimal updates needed
```

### The Critical Mismatches

```
MISMATCH 1: 3-Phase vs 4-Track
───────────────────────────────
Current ZPWO:   Draft → Produce → Polish (3 phases)
Your reality:   Research → Drafts → Production → Polish (4 tracks)

RESOLUTION: Track 1 (Research) = /intake phase
            Track 2 (Drafts)   = /draft phase  
            Track 3 (Production) = /produce phase
            Track 4 (Polish)   = /polish phase
            
The 4-track model is a SUPERSET. ZPWO's /intake already handles Track 1.
The missing piece: /intake currently routes to MIS only.
It needs to route to Market Scout → Research Ops → MIS as a CHAIN.

MISMATCH 2: VSL Pods Reference v2.0 Skills
───────────────────────────────────────────
SUB_AGENT_CONFIGS line 734: long_form_vsl_script_architect_v2.0.xml
SUB_AGENT_CONFIGS line 746: short_form_vsl_script_writer_v2.0.xml
SUB_AGENT_CONFIGS line 759: long_form_vsl_script_architect_v2.0.xml

These need: LFVA v3.0.0 and SFVW v3.0.0

MISMATCH 3: No Copy Director in Routing
────────────────────────────────────────
ZPWO routing table has NO entry for Copy Director.
"strategic_copy_director_v2.1.0_full.xml" is referenced in salespage_pods
but it's the WRONG skill — it's a general strategy director, not the 
VSL/sales-specific Copy Director that assigns skill parameters.

MISMATCH 4: Copy Lead Not Wired
────────────────────────────────
Copy Lead exists but isn't in ZPWO routing table, SUB_AGENT_CONFIGS,
or ORCHESTRATOR_CORE skill dependency map.

MISMATCH 5: CSA Not in Any Pod
──────────────────────────────
Content Script Architect exists but has no pod, no routing entry.
```

---

## PART 2: THE 4-TRACK ACTIVATION MODEL (Corrected)

### How Skills Actually Rotate Through Tracks

```
TRACK 1: RESEARCH & PLAN (Human-driven, agent-executes)
═══════════════════════════════════════════════════════════
│ ACTIVATION: Human says "new project" or provides brief
│ SKILLS LOADED (sequentially, not simultaneously):
│
│  ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  │  Market Scout    │────▶│  Research Ops    │────▶│      MIS        │
│  │  (Reconnaissance)│     │  (Deep Extract)  │     │  (Synthesize)   │
│  └─────────────────┘     └─────────────────┘     └─────────────────┘
│         │                        │                        │
│         ▼                        ▼                        ▼
│  MARKET_INTEL_PACKET      Raw Extraction          PROJECT_BRIEF
│                                                   MESSAGE_SPINE
│                                                   EVIDENCE_PACK
│
│ OPTIONAL SKILLS (loaded if needed):
│  • Offer Architect — if offer structure undefined
│  • Viral Theme Developer — if positioning unclear
│
│ EXIT GATE: All 3 foundational SSOTs exist + human approves
│ ──────────────────────────────────────────────────────────

TRACK 2: DRAFTS & DEVELOPMENT (Agent-led, human-reviews)
═══════════════════════════════════════════════════════════
│ ACTIVATION: Track 1 SSOTs exist (dependency gate)
│ STRATEGIC LAYER (loads first, sets parameters):
│
│  ┌─────────────────┐     ┌─────────────────┐
│  │   Copy Lead      │────▶│  Copy Director   │
│  │  (Angle Select)  │     │  (Assign + Config)│
│  └─────────────────┘     └─────────────────┘
│         │                        │
│         ▼                        ▼
│  ANGLE_SET (3-5 angles)   SKILL_ACTIVATION_ORDER:
│  Human picks angle(s)     - Which skill (LFVA/SFVW/SPC/ACM)
│                           - Which style (S1-S4)
│                           - Which bridge pattern
│                           - Sophistication level
│                           - Length/format parameters
│
│ EXECUTION LAYER (loads based on Copy Director assignment):
│  ┌─────────────────┐
│  │  [ASSIGNED SKILL]│  ← LFVA v3.0 / SFVW v3.0 / SPC / ACM / Email
│  │  + MWP support   │
│  └─────────────────┘
│         │
│         ▼
│  DRAFT ASSETS (scripts, copy, visual direction)
│
│ LIGHT MMA: Quick Score (M1) ≥7.0 on strategy alignment only
│ EXIT GATE: Draft complete + human approves direction
│ ──────────────────────────────────────────────────────────

TRACK 3: PRODUCTION & REFINE (Agent-autonomous, human-spot-checks)
═══════════════════════════════════════════════════════════
│ ACTIVATION: Draft approved by human
│ SKILLS LOADED (same skill as Track 2, production mode):
│
│  ┌─────────────────┐     ┌─────────────────┐
│  │  [ASSIGNED SKILL]│────▶│      MMA        │
│  │  Production Mode │     │  Deep Audit (M2) │
│  └─────────────────┘     └─────────────────┘
│         │                        │
│         ▼                        ▼
│  Production Asset         SCORECARD + VERDICT
│  (full script/copy)       PASS / FIX / ESCALATE
│         │                        │
│         └────────────────────────┘
│                    │
│              FIX LOOP (max 3)
│
│ FOR VSLs SPECIFICALLY:
│  • Run Python validators (VT-01 through VT-10)
│  • Belief sequence check
│  • Visual coverage audit
│  • Congruency audit
│
│ HEAVY MMA: Deep Audit (M2) — all 7 dimensions, ≥8.0 avg, ≥9.0 critical
│ EXIT GATE: MMA PASS or human override after circuit breaker
│ ──────────────────────────────────────────────────────────

TRACK 4: POLISH & PERFECT (Validator agents, human publishes)
═══════════════════════════════════════════════════════════
│ ACTIVATION: Track 3 MMA PASS
│ SKILLS LOADED (sequentially):
│
│  ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  │  Skeptic Avatar  │────▶│      HPE        │────▶│      NRA        │
│  │  (Stress Test)   │     │  (Voice Polish)  │     │  (Resonance)    │
│  └─────────────────┘     └─────────────────┘     └─────────────────┘
│         │                        │                        │
│         ▼                        ▼                        ▼
│  SKEPTIC_REPORT           Polished Asset           Resonance Audit
│  (fix critical first)     (AI detox, voice)        (7S coverage)
│
│ FINAL MMA: Compliance Gate (M4) — platform safety
│ EXIT GATE: Human final publish decision
│ ──────────────────────────────────────────────────────────
```

### The Skill Rotation Protocol (Instrument Change)

```
HOW A SINGLE AGENT CHANGES INSTRUMENTS:

1. UNLOAD CURRENT SKILL
   ├── Save any outputs to SSOT files
   ├── Compress skill-specific state into SESSION_STATE
   └── Clear skill context from working memory

2. LOAD NEW SKILL  
   ├── Load skill XML as system context
   ├── Load required SSOTs from Track 1
   ├── Load any outputs from previous Track
   └── Verify SSOT checksums (no drift)

3. EXECUTE
   ├── Skill "becomes" the agent's identity
   ├── Agent operates within skill's guardrails
   └── Produces outputs in skill's defined formats

4. UNLOAD AFTER EXECUTION
   ├── Save outputs
   ├── Log learned constraints
   └── Return to orchestrator context

WHAT PERSISTS ACROSS ROTATIONS:
✅ SSOTs (PROJECT_BRIEF, MESSAGE_SPINE, EVIDENCE_PACK)
✅ SESSION_STATE.json
✅ LOCKED_OBJECTS checksums
✅ MMA scorecards from previous phases

WHAT GETS WIPED:
❌ Skill-specific execution context
❌ Intermediate drafts (archived, not active)
❌ Previous skill's identity/guardrails
```

---

## PART 3: THE TWO PROJECT BASES

### PROJECT BASE A: VSL PRODUCTION

**Purpose:** Manual Claude Project for producing Video Sales Letters  
**Skill Focus:** LFVA v3.0 (long-form) or SFVW v3.0 (short-form)

```yaml
# VSL_PRODUCTION_PROJECT_BASE.yaml

project_name: "VSL Production — [Client/Product Name]"
project_type: "vsl_production"

# ═══════════════════════════════════════════════════════
# PROJECT KNOWLEDGE (Always Loaded)
# ═══════════════════════════════════════════════════════

always_loaded:
  orchestration:
    - ZPWO_v3_MICRO.xml            # Lean orchestrator (543 lines)
    - MMA_v1.0.0.xml               # Quality guardian (1,066 lines)
    # TOTAL: ~1,600 lines always loaded
  
  # NOTE: Do NOT load LFVA/SFVW into project knowledge permanently.
  # They are 1,448-1,555 lines each. Load on-demand per conversation.

# ═══════════════════════════════════════════════════════
# SSOT DOCUMENTS (Upload per project)
# ═══════════════════════════════════════════════════════

required_ssots:
  - name: "PROJECT_BRIEF.yaml"
    source: "Track 1 output or manual creation"
    contains: "Avatar, offer, constraints, market sophistication, price point"
    
  - name: "MESSAGE_SPINE.yaml"
    source: "Track 1 output (MIS)"
    contains: "Promise, UMP, UMS, proof pillars, belief stack"
    
  - name: "EVIDENCE_PACK.yaml"
    source: "Track 1 output or manual assembly"
    contains: "Claims→sources, testimonials, statistics, studies"

recommended_ssots:
  - name: "VOICE_GUIDE.yaml"
    source: "Brand documents or extraction"
    contains: "Tone, taboos, rhythm, vocabulary, persona"
    
  - name: "COMPETITOR_ANALYSIS.yaml"
    source: "Market Scout or manual research"
    contains: "Competing VSLs, hooks, mechanisms, gaps"

# ═══════════════════════════════════════════════════════
# CONVERSATION SEQUENCE (Manual Skill Rotation)
# ═══════════════════════════════════════════════════════

conversation_sequence:

  conversation_1_strategy:
    title: "VSL Strategy & Angle Selection"
    skill_to_paste: "Copy Lead (or Copy Director when built)"
    ssots_to_upload: [PROJECT_BRIEF, MESSAGE_SPINE]
    task: |
      1. Review brief and spine
      2. Select VSL type: Long-form (LFVA) or Short-form (SFVW)
      3. Generate 3-5 angles with hook variants
      4. Select style: S1-Documentary/S2-Customer Story/S3-Authority/S4-Comparison
      5. Map belief sequence (4 beliefs)
      6. Choose bridge pattern
      7. Set length target based on offer price
    outputs:
      - ANGLE_SET (selected angle + rationale)
      - VSL_CONFIG (style, bridge, length, sophistication level)
    human_decision: "Approve angle and configuration"

  conversation_2_draft:
    title: "VSL Script Draft"
    skill_to_paste: "LFVA v3.0.0 OR SFVW v3.0.0"
    ssots_to_upload: [PROJECT_BRIEF, MESSAGE_SPINE, EVIDENCE_PACK, ANGLE_SET]
    task: |
      1. Execute Pre-Writing Protocol:
         a. Belief Map (4 beliefs in sequence)
         b. Ad Creative Concept (thumbnail/hook alignment)
         c. Retention Map (minute-by-minute objectives)
      2. Write 11-Step script (Steps 1-11)
      3. Two-column format (Audio | Visual Direction)
      4. Include HOOK_OPTIONS (4 variants)
    outputs:
      - VSL_SCRIPT_VISUAL_v1 (two-column draft)
      - HOOK_OPTIONS (4 hooks)
      - RETENTION_MAP
      - PROOF_PLAN
    light_mma: "Strategy alignment ≥7.0"
    human_decision: "Approve draft direction, select hook"

  conversation_3_production:
    title: "VSL Production Refinement"
    skill_to_paste: "LFVA v3.0.0 OR SFVW v3.0.0 (same skill, production focus)"
    ssots_to_upload: [All previous + VSL_SCRIPT_v1 + selected HOOK]
    task: |
      1. Refine full script based on draft feedback
      2. Run Python validators:
         - VT-01: Belief sequence validator
         - VT-02: Visual coverage checker
         - VT-03: Minute 8 cliff detector (LFVA only)
         - VT-05: Belief ratio calculator (target 80/20)
         - VT-06: Bridge pattern detector
         - VT-07: Proof architecture validator
         - VT-08: Congruency audit
         - VT-09: Conspiracy compliance checker
         - VT-10: Every minute pays rent
      3. Address any validator failures
      4. Generate EDITOR_BRIEF and B_ROLL_ASSET_LIST
    outputs:
      - VSL_SCRIPT_VISUAL_v2 (production quality)
      - EDITOR_BRIEF
      - B_ROLL_ASSET_LIST
      - COMPLIANCE_NOTES
    heavy_mma: "All 7D, ≥8.0 avg, ≥9.0 critical"

  conversation_4_polish:
    title: "VSL Polish & Validation"
    skill_to_paste: "HPE v2.1 (then NRA v2.1)"
    ssots_to_upload: [VSL_SCRIPT_v2, VOICE_GUIDE, MESSAGE_SPINE]
    task: |
      1. HPE Pass:
         a. AI detox (remove AI-isms from VO lines)
         b. Voice consistency (match VOICE_GUIDE)
         c. Kitchen Table Test (sounds like real person talking)
         d. Trans Rhythm check (sentence length variation)
      2. NRA Pass (new conversation or continuation):
         a. 7S coverage audit
         b. Dimensional gap identification
         c. Resonance enhancement recommendations
      3. Final MMA: Compliance Gate (M4)
    outputs:
      - VSL_SCRIPT_FINAL
      - POLISH_REPORT
      - 7S_COVERAGE_MAP
    human_decision: "Final publish approval"

  conversation_5_skeptic:  # OPTIONAL — when Skeptic Avatar is built
    title: "Skeptic Stress Test"
    skill_to_paste: "Skeptic Avatar v1.0"
    ssots_to_upload: [VSL_SCRIPT_FINAL, EVIDENCE_PACK, MESSAGE_SPINE]
    task: |
      1. Deep Devil's Advocate review
      2. Proof stress test (every claim vs evidence)
      3. Market burnout simulation
    outputs:
      - SKEPTIC_REPORT
      - WEAK_POINTS_MAP
      - FIX_RECOMMENDATIONS
    note: "Run BEFORE conversation_4 polish if high-stakes launch"

# ═══════════════════════════════════════════════════════
# CONTEXT BUDGET PER CONVERSATION
# ═══════════════════════════════════════════════════════

context_budget_guide:
  conversation_1: "Copy Lead (~800 lines) + SSOTs (~2K tokens) = Light"
  conversation_2: "LFVA v3.0 (1,555 lines) + SSOTs = Heavy (primary work)"
  conversation_3: "LFVA v3.0 (1,555 lines) + draft + SSOTs = Maximum"
  conversation_4: "HPE (~1,200 lines) + script + SSOTs = Moderate"
  note: |
    Never load LFVA + HPE + MMA simultaneously. They total ~3,800 lines.
    Rotate: one skill per conversation, carry SSOTs forward.
```

---

### PROJECT BASE B: SALES PAGE PRODUCTION

```yaml
# SALES_PAGE_PRODUCTION_PROJECT_BASE.yaml

project_name: "Sales Page Production — [Client/Product Name]"
project_type: "sales_page_production"

# ═══════════════════════════════════════════════════════
# PROJECT KNOWLEDGE (Always Loaded)
# ═══════════════════════════════════════════════════════

always_loaded:
  orchestration:
    - ZPWO_v3_MICRO.xml            # Lean orchestrator
    - MMA_v1.0.0.xml               # Quality guardian

# ═══════════════════════════════════════════════════════
# SSOT DOCUMENTS (Same as VSL — Track 1 produces these)
# ═══════════════════════════════════════════════════════

required_ssots:
  - PROJECT_BRIEF.yaml
  - MESSAGE_SPINE.yaml
  - EVIDENCE_PACK.yaml

recommended_ssots:
  - VOICE_GUIDE.yaml
  - COMPETITOR_ANALYSIS.yaml

# ═══════════════════════════════════════════════════════
# CONVERSATION SEQUENCE
# ═══════════════════════════════════════════════════════

conversation_sequence:

  conversation_1_strategy:
    title: "Sales Page Strategy & Structure"
    skill_to_paste: "Copy Lead → Copy Director (when built)"
    ssots_to_upload: [PROJECT_BRIEF, MESSAGE_SPINE]
    task: |
      1. Determine page length: Short / Medium / Long
         - Short: <$100 offers, warm traffic, simple mechanism
         - Medium: $100-$500, mixed traffic, moderate complexity
         - Long: $500+, cold traffic, complex mechanism
      2. Select page architecture:
         - Problem-Mechanism-Solution (standard)
         - Story-Led (testimonial-driven)
         - Comparison (vs alternatives)
         - Quiz-to-Page (personalized)
      3. Map section flow to 7S dimensions
      4. Generate 3-5 headline angles
      5. Define proof architecture (what proof goes where)
    outputs:
      - PAGE_STRATEGY (length, architecture, section map)
      - HEADLINE_OPTIONS (3-5 variants)
      - PROOF_PLACEMENT_MAP
      - 7S_SECTION_MAPPING
    human_decision: "Approve strategy and headline"

  conversation_2_draft:
    title: "Sales Page Draft"
    skill_to_paste: "Sales Page Copywriter v2.0 (or v3.0 when upgraded)"
    ssots_to_upload: [All SSOTs + PAGE_STRATEGY + selected HEADLINE]
    task: |
      1. Write full page draft following section map:
         - Hero (headline, sub-head, hook copy, CTA above fold)
         - Problem section (agitation, validation)
         - Mechanism section (UMP/UMS reveal)
         - Proof section (testimonials, case studies, data)
         - Offer stack (core + bonuses + value anchoring)
         - Guarantee (risk reversal)
         - FAQ (objection handling)
         - Final CTA (urgency + close)
      2. Apply Purchase Driver Sequence:
         Status → Emotion → Validation → Social → Value
      3. Include section-level visual/design notes
    outputs:
      - SALES_PAGE_DRAFT_v1
      - SECTION_BREAKDOWN (word counts, 7S coverage per section)
    light_mma: "Strategy alignment ≥7.0"
    human_decision: "Approve draft direction"

  conversation_3_production:
    title: "Sales Page Production Build"
    skill_to_paste: "Sales Page Copywriter v2.0 (production mode)"
    additional_support: "Sales Copy Consistency Contract (if available)"
    ssots_to_upload: [All previous + SALES_PAGE_DRAFT_v1]
    task: |
      1. Full production build:
         - Every claim grounded in EVIDENCE_PACK
         - Mechanism language matches MESSAGE_SPINE exactly
         - Value stack math is specific and believable
         - Guarantee language is clear and honest
         - CTA copy is action-oriented (no "click here")
      2. Run validation:
         - Proof mapping (claim → source)
         - Mechanism consistency (UMP/UMS language)
         - Voice check (matches VOICE_GUIDE)
         - Compliance review (platform-safe)
      3. Generate design direction notes per section
    outputs:
      - SALES_PAGE_v2 (production quality)
      - PROOF_MAP (every claim → evidence source)
      - DESIGN_DIRECTION_NOTES
    heavy_mma: "All 7D, ≥8.0 avg, ≥9.0 on Proof + CTA"

  conversation_4_polish:
    title: "Sales Page Polish"
    skill_to_paste: "HPE v2.1 (then NRA v2.1)"
    ssots_to_upload: [SALES_PAGE_v2, VOICE_GUIDE, MESSAGE_SPINE]
    task: |
      HPE Pass:
      1. AI detox across full page
      2. Voice consistency section-by-section
      3. Rhythm check (vary section energy levels)
      4. Kitchen Table Test on key sections (hero, mechanism, CTA)
      
      NRA Pass:
      1. 7S coverage audit (all 7 must be present for sales pages)
      2. Purchase Driver Sequence check
      3. Dimensional gap remediation
      
      Final MMA: Compliance Gate
    outputs:
      - SALES_PAGE_FINAL
      - POLISH_REPORT
      - 7S_AUDIT

  conversation_5_design:  # Track 3 handoff
    title: "Design Direction Handoff"
    skill_to_paste: "Strategic Design Master / Image Concept Planner"
    ssots_to_upload: [SALES_PAGE_FINAL, DESIGN_DIRECTION_NOTES, PROJECT_BRIEF]
    task: |
      1. Generate section-by-section design specs
      2. Color/typography recommendations based on avatar + market
      3. Image concepts for hero, proof, mechanism sections
      4. Responsive layout guidelines
      5. CTA button design + placement strategy
    outputs:
      - DESIGN_SPEC
      - IMAGE_CONCEPTS
      - LAYOUT_WIREFRAME
    note: "This bridges Track 2 (copy) → Track 3 (production/build)"
```

---

## PART 4: WHAT NEEDS BUILDING (Priority Sequence)

### Priority 1: COPY DIRECTOR (The Missing Link)

```
STATUS: TBA — not built
IMPACT: Without it, humans manually do skill parameter assignment
TIME: 4-6 hours (Standard complexity, Track B)
```

**What Copy Director Does:**
It sits between Copy Lead (which selects angles) and the execution skill (LFVA/SFVW/SPC). Copy Lead says "use this angle." Copy Director says "use THIS skill, in THIS configuration, with THESE parameters."

**Copy Director's Routing Logic:**
```
IF asset_type == "vsl" AND duration > 10min:
    skill = LFVA_v3.0
    style = [select from S1-S4 based on market sophistication]
    bridge = [select based on offer price + audience temperature]
    
IF asset_type == "vsl" AND duration <= 10min:
    skill = SFVW_v3.0
    hook_system = [Alignment Triad for ads, Dopamine 2-Hit for organic]
    
IF asset_type == "sales_page":
    skill = Sales_Page_Copywriter
    length = [Short/Medium/Long based on price + traffic temp]
    architecture = [Problem-Mech-Solution / Story-Led / Comparison]
    
IF asset_type == "advertorial":
    skill = Advertorial_Copy_Master
    
IF asset_type == "email":
    skill = Email_Copy_Genius
    sequence_type = [Welcome / Launch / Nurture]
    
IF asset_type == "content_video":
    skill = CSA_v1.0
```

**Copy Director Output (SKILL_ACTIVATION_ORDER):**
```yaml
activation:
  skill: "long_form_vsl_script_architect_v3.0.0"
  style: "S1_documentary_investigative"
  bridge_pattern: "blind_solution"
  hook_archetype: "investigative_expose"
  belief_count: 4
  target_length_minutes: 16
  market_sophistication: 4
  platform_primary: "youtube_ads"
  platform_secondary: "landing_page"
  warm_traffic_adaptations: false
  chaptering_enabled: false
```

**Build Approach:** 
- Simple skill (Track A) initially — routing logic + parameter assignment
- Upgrade to Standard (Track B) after real-world testing
- Can be built from existing Strategic Copy Director as foundation
- Add LFVA v3.0 + SFVW v3.0 routing awareness

### Priority 2: ZPWO v3.1 ROUTING TABLE UPDATE

```
STATUS: Quick patch — 1-2 hours
IMPACT: Correct skill references across all pods
```

**Changes Needed:**
```xml
<!-- CURRENT (stale) -->
<Route command="/vsl" skill="long_form_vsl_script_architect_v2.0" />

<!-- UPDATED -->
<Route command="/vsl-long" skill="long_form_vsl_script_architect_v3.0.0" />
<Route command="/vsl-short" skill="short_form_vsl_script_writer_v3.0.0" />
<Route command="/vsl" skill="copy_director → routes to LFVA or SFVW" />
<Route command="/content-video" skill="content_script_architect_v1.0.0" />
<Route command="/salespage" skill="copy_director → routes to SPC" />
```

**Also Add:**
```xml
<!-- Track 1 chain -->
<Route command="/intake" skill="market_scout → research_ops → MIS" />

<!-- Strategic layer -->
<Route command="/strategy" skill="copy_lead + copy_director" />

<!-- Track 4 validators -->
<Route command="/skeptic" skill="skeptic_avatar_red_team_v1.0" />
<Route command="/resonance" skill="neuro_resonance_auditor_v2.1" />
```

### Priority 3: SUB_AGENT_CONFIGS v3.0 (VSL Pod Update)

```
STATUS: Structural update — 2-3 hours
IMPACT: Correct VSL pod definitions for v3.0 skills
```

**VSL Pod Rewrite:**
```yaml
vsl_pods:
  description: "Video Sales Letter production — Long Form + Short Form"
  
  # NEW: Strategic layer before draft
  strategy:
    copy_lead:
      name: "VSL Angle Selection"
      type: sub_agent
      phase: P0  # Pre-draft strategic
      model: claude-sonnet
      skills:
        - copy_lead_v2.0.xml  # or v3.0 when upgraded
      output_to: copy_director
      
    copy_director:
      name: "VSL Skill Assignment"
      type: orchestration
      phase: P0
      model: claude-sonnet
      skills:
        - copy_director_v1.0.xml  # NEW — Priority 1 build
      output_to: [long_form_writer OR short_form_writer]
      
  draft:
    long_form_writer:
      name: "Long Form VSL Writer"
      type: sub_agent
      phase: P1
      model: claude-opus  # Opus for complex 1,555-line skill
      skills:
        - long_form_vsl_script_architect_v3.0.0.xml  # UPDATED
      ssot_required:
        - MESSAGE_SPINE
        - PROJECT_BRIEF
        - EVIDENCE_PACK
      mma_gate: true
      mma_threshold: 7.0
      note: "Executes Pre-Writing Protocol first, then 11-Step"

    short_form_writer:
      name: "Short Form VSL Writer"
      type: sub_agent
      phase: P1
      model: claude-sonnet  # Sonnet sufficient for shorter scripts
      skills:
        - short_form_vsl_script_writer_v3.0.0.xml  # UPDATED
      mma_gate: true
      mma_threshold: 7.0

  production:
    builder:
      name: "VSL Production Builder"
      type: sub_agent
      phase: P2
      model: claude-opus
      skills:
        - long_form_vsl_script_architect_v3.0.0.xml  # UPDATED
        # OR short_form_vsl_script_writer_v3.0.0.xml
      python_validators:  # NEW — v3.0 validators
        - belief_sequence_validator
        - visual_coverage_checker
        - minute_8_cliff_detector
        - belief_ratio_calculator
        - bridge_pattern_detector
        - proof_architecture_validator
        - congruency_audit
        - conspiracy_compliance_checker
        - every_minute_pays_rent
      mma_gate: true
      mma_mode: "M2_deep_audit"
      mma_threshold: 8.0

    validator:
      name: "VSL Validator"
      type: validator
      phase: P2
      model: claude-sonnet
      skills:
        - mma_master_monitor_agent_v1.0.0.xml
      loop_max: 3

  polish:
    skeptic_review:  # NEW — Track 4 addition
      name: "VSL Skeptic Review"
      type: validator
      phase: P3
      model: claude-sonnet
      skills:
        - skeptic_avatar_red_team_v1.0.xml  # When built
      output_to: voice_editor

    voice_editor:
      name: "VSL Voice Editor"
      type: sub_agent
      phase: P3
      model: claude-opus
      skills:
        - human_persuasion_editor_v2.1.0.xml
      mma_threshold: 9.0

    resonance_auditor:  # NEW — Track 4 addition
      name: "VSL Resonance Check"
      type: validator
      phase: P3
      model: claude-sonnet
      skills:
        - neuro_resonance_auditor_v2.1.0.xml
```

### Priority 4: SKEPTIC AVATAR BUILD

```
STATUS: Spec exists (SKEPTIC_AVATAR_RED_TEAM_BUILD_SPEC.md)
IMPACT: Critical for Track 4 — currently no stress-test capability
TIME: 2-3 hours (spec is detailed, Track A-B)
BUILD: Use existing spec + Atomic Pipeline
```

### Priority 5: SSOT TEMPLATE STANDARDIZATION

```
STATUS: Partial — some templates exist, not all standardized
IMPACT: Track 1 → Track 2 handoff breaks without standard schemas
TIME: 2-3 hours
```

**Templates Needed:**
```
MESSAGE_SPINE_TEMPLATE.yaml    — Standard schema with all fields
PROJECT_BRIEF_TEMPLATE.yaml    — Standard schema  
EVIDENCE_PACK_TEMPLATE.yaml    — Standard schema
VOICE_GUIDE_TEMPLATE.yaml      — Already exists (reference)
ANGLE_SET_TEMPLATE.yaml        — NEW (Copy Lead output)
SKILL_ACTIVATION_ORDER.yaml    — NEW (Copy Director output)
```

---

## PART 5: BUILD SEQUENCE (Recommended Order)

```
PHASE A: IMMEDIATE (This Week) — Make v3.0 Skills Usable
────────────────────────────────────────────────────────
□ A1. Create VSL Production Project Base (manual Claude Project)
      → Load ZPWO + MMA as project knowledge
      → Upload SSOTs per project
      → Follow conversation sequence manually
      → USE LFVA v3.0 / SFVW v3.0 immediately
      
□ A2. Create Sales Page Production Project Base (same pattern)

□ A3. SSOT Template Standardization
      → MESSAGE_SPINE, PROJECT_BRIEF, EVIDENCE_PACK schemas
      → Ensures Track 1 → Track 2 handoff works

ESTIMATED: 3-4 hours

PHASE B: SHORT-TERM (Next 1-2 Weeks) — Fill Critical Gaps
────────────────────────────────────────────────────────
□ B1. Build Copy Director v1.0
      → Routing logic + parameter assignment
      → LFVA/SFVW/SPC/ACM/Email routing awareness
      → Track A-B build (4-6 hours)

□ B2. ZPWO v3.1 Routing Table Patch
      → Update skill references to v3.0
      → Add Copy Director routing
      → Add CSA routing
      → 1-2 hours

□ B3. Build Skeptic Avatar v1.0
      → From existing build spec
      → Track 4 stress-test capability
      → 2-3 hours

ESTIMATED: 8-11 hours

PHASE C: MEDIUM-TERM (2-4 Weeks) — Full Orchestration
────────────────────────────────────────────────────────
□ C1. SUB_AGENT_CONFIGS v3.0
      → Rewrite VSL pods for v3.0 skills
      → Rewrite Sales Page pods
      → Add strategic layer (Copy Lead → Copy Director)
      → Add Track 4 validators (Skeptic + NRA)
      
□ C2. ORCHESTRATOR_CORE v5.0
      → Update from 3-phase to 4-track model
      → Add Copy Lead + Copy Director to skill dependency map
      → Update VSL/Sales Page routing rules
      → Add CSA routing

□ C3. LangGraph Workflow Update
      → VSL workflow with v3.0 node references
      → Sales Page workflow with correct skill chain
      → CopilotKit breakpoints at track transitions

ESTIMATED: 6-8 hours

PHASE D: ONGOING — v3.0 Upgrades for All Skills
────────────────────────────────────────────────────────
Each skill gets Atomic Pipeline v2.0 treatment:
□ HPE v3.0 (high priority — polish layer)
□ NRA v3.0 (high priority — resonance layer)
□ Sales Page Copywriter v3.0 (high priority)
□ Advertorial Copy Master v3.0
□ Email Copy Genius v3.0
□ MWP v3.0
□ Market Scout v3.0
□ Research Ops v3.0
□ MIS v3.0

Each upgrade: 6-10 hours via Atomic Pipeline
(NotebookLM extraction → Claude synthesis → Polish)
```

---

## PART 6: THE "START TODAY" QUICK-START

### To Use LFVA v3.0 RIGHT NOW in Claude:

**Step 1:** Create a new Claude Project called "VSL Production — [Product Name]"

**Step 2:** Add to Project Knowledge:
- ZPWO v3 Micro XML
- MMA v1.0.0 XML

**Step 3:** Prepare your SSOTs (even rough drafts work):
- PROJECT_BRIEF with: avatar, offer, price, platform, market sophistication
- MESSAGE_SPINE with: promise, UMP, UMS, proof pillars, 4-belief stack
- EVIDENCE_PACK with: claims mapped to sources, testimonials

**Step 4:** Start Conversation 1 — Strategy:
Upload SSOTs. Tell Claude: "I need a VSL for [product]. Review the brief and spine, then give me 3-5 angle options with hook variants for each. Recommend the best angle and explain why."

**Step 5:** Start Conversation 2 — Draft:
Paste the FULL LFVA v3.0.0 XML into the conversation (or upload as file). Upload SSOTs + selected angle. Tell Claude: "You are now the Long-Form VSL Script Architect. Execute the Pre-Writing Protocol first (Belief Map, Ad Creative Concept, Retention Map), then write the full 11-step script in two-column format."

**Step 6:** Start Conversation 3 — Production:
Same skill, upload draft. Tell Claude: "Refine this script to production quality. Run all validation checks. Ensure belief sequence integrity, visual coverage on every line, and 80/20 belief-to-pitch ratio."

**Step 7:** Start Conversation 4 — Polish:
Paste HPE v2.1 XML. Upload production script + VOICE_GUIDE. Tell Claude: "You are the Human Persuasion Editor. Run AI detox, voice consistency check, Kitchen Table Test, and Trans Rhythm audit on this VSL script."

**That's it.** You're operating the full 4-track manually with skill rotation.
The orchestrator just automates what you're doing by hand in these steps.

---

## SUMMARY: THE MAP

```
                    YOU ARE HERE
                         ↓
    ┌────────────────────●────────────────────┐
    │                                          │
    │  PHASE A: Manual Project Bases           │ ← THIS WEEK
    │  (Use v3.0 skills in Claude Projects)    │
    │                                          │
    ├──────────────────────────────────────────┤
    │                                          │
    │  PHASE B: Fill Gaps                      │ ← NEXT 1-2 WEEKS
    │  (Copy Director + Skeptic Avatar +       │
    │   ZPWO routing patch)                    │
    │                                          │
    ├──────────────────────────────────────────┤
    │                                          │
    │  PHASE C: Full Orchestration             │ ← 2-4 WEEKS
    │  (SUB_AGENT v3.0 + ORCHESTRATOR v5.0 +  │
    │   LangGraph workflows)                   │
    │                                          │
    ├──────────────────────────────────────────┤
    │                                          │
    │  PHASE D: Arsenal Upgrade                │ ← ONGOING
    │  (All skills → v3.0 via Atomic Pipeline) │
    │                                          │
    └──────────────────────────────────────────┘
    
    IMMEDIATE ACTION:
    1. Create VSL Production Claude Project
    2. Create Sales Page Production Claude Project
    3. Start using LFVA v3.0 + SFVW v3.0 TODAY
    4. Build Copy Director next (highest-leverage gap)
```

---

*Orchestration Finalization Plan v1.0*  
*"The skills are the instruments. The project bases are the operating theaters. The orchestrator is the surgeon's assistant."*  
*2026-02-15*

---
id: skill.copy_director.v3_0_0
name: Copy Director
version: 3.0.0
status: active
owner: Vision Capitalist / ULTRAMIND
category: copy_director
tags:
- orchestrator
- router
- production_track
- awareness_routing
- market_type_routing
- delegation
description: "Routes campaigns through the 4-phase production track. Reads a campaign\
  \ brief or\n      MarketIntelPacket, diagnoses traffic temperature + awareness level\
  \ + market type,\n      selects the correct asset formats, assigns the right production\
  \ skills,\n      emits structured SKILL_ACTIVATION_ORDERs with tone/voice guidance,\
  \ and\n      validates handoffs at every phase boundary. Does NOT write copy, build\
  \ mechanisms,\n      design offers, or perform research."
inputs: []
outputs: []
depends_on: []
delegates_to: []
complements: []
required_tools: []
memory_reads: []
memory_writes: []
token_budget: medium
risk_level: medium
model_preference: sonnet
eval_suite: ''
---

# Copy Director

Routes campaigns through the 4-phase production track. Reads a campaign brief or
      MarketIntelPacket, diagnoses traffic temperature + awareness level + market type,
      selects the correct asset formats, assigns the right production skills,
      emits structured SKILL_ACTIVATION_ORDERs with tone/voice guidance, and
      validates handoffs at every phase boundary. Does NOT write copy, build mechanisms,
      design offers, or perform research.

## Purpose

Read the brief. Build the full diagnostic picture.

## Use When

- TODO: Define activation triggers

## Do Not Use When

- TODO: Define exclusion conditions

## Inputs

No formal inputs defined.

## Outputs

No formal outputs defined.

## Workflow

1. THE 4-PHASE PRODUCTION TRACK
════════════════════════════════════════════════════════════════════

  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
  │  TOP TEAM   │    │  TOP TEAM   │    │  TOP TEAM   │    │  TOP TEAM   │
  │  Creative   │    │  Narrative  │    │  Revision   │    │  Language   │
  │  Strategic  │    │  Copy       │    │  Creative   │    │  Polish     │
  ├─────────────┤    ├─────────────┤    ├─────────────┤    ├─────────────┤
  │ BOTTOM TEAM │    │ BOTTOM TEAM │    │ BOTTOM TEAM │    │ BOTTOM TEAM │
  │  Structural │    │  Structural │    │  QA Audit   │    │  Final QA   │
  │  Offers     │    │  Page Copy  │    │  Scoring    │    │  Sign-off   │
  └──────┬──────┘    └──────┬──────┘    └──────┬──────┘    └──────┬──────┘
    PHASE 1            PHASE 2            PHASE 3            PHASE 4
    PLAN &             DRAFT &            BUILD &            POLISH &
    STRATEGIZE         DEVELOP            REFINE             PERFECT

  ◄──────────────────── WORK FLOWS LEFT TO RIGHT ────────────────────────►
2. 
3. ROUTING DIMENSIONS: Market Type × Traffic × Awareness
══════════════════════════════════════════════════════════════════════════

DIMENSION 1: TRAFFIC TEMPERATURE + AWARENESS LEVEL
────────────────────────────────────────────────────────────────────────
Cold Paid (Unaware)         → Education bridge REQUIRED before ask
                              Format: Advertorial → VSL → Sales Page
Cold Paid (Problem-Aware)   → Agitate then educate mechanism
                              Format: Short VSL or Advertorial → Sales Page
Warm Email (Solution-Aware) → Angle + mechanism + direct offer
                              Format: Email sequence → Sales Page
Warm Retarget (Product-Aware)→ Objection handling + social proof
                              Format: Retarget ad → Sales Page
Hot / Buyer (Most-Aware)    → Offer + value stack + urgency
                              Format: Direct offer page / Upsell page
Organic Search (Problem-Aware)→ SEO + educational → soft CTA
                              Format: Blog / Content → Lead magnet / Opt-in
Organic Social (Unaware→Problem)→ Hook → value → curiosity gap
                              Format: Thread / Carousel → DM / Link in bio

RULE: Move ONE awareness stage per asset. Never skip stages.
RULE: Cold traffic ALWAYS needs an education bridge. No direct sales pages.
RULE: Every brief must declare awareness ENTRY level and EXIT target.

DIMENSION 2: ASSET TYPE → SKILL ASSIGNMENT
────────────────────────────────────────────────────────────────────────
Asset Type                  Traffic/Length          Skill
─────────────────────────────────────────────────────────
Long-form VSL / Advertorial Cold, 12-20 min         Long-Form VSL Architect
Short-form VSL              Warm/Retarget, 5-10 min  Short-Form VSL Writer
Sales Video (organic/YT)    Content/Educational      Content Script Architect
Sales Page (deep persuasion) High-ticket / Complex   Copy Lead
Sales Page (standard warm)  Warm, <$500             Sales Page Copywriter LITE
Blog / Newsletter / Email   Organic / Nurture        Master Writing Partner
Social Post / Thread        Organic social           Viral Theme Developer
Carousel / LinkedIn         Organic B2B/D2C          Viral Theme Developer
Offer Design (pre-writing)  Any                     Offer Architect (Phase 1)

VSL ROUTING DECISION:
  Duration > 10 min?         → Long-Form VSL Architect
  Duration ≤ 10 min?         → Short-Form VSL Writer
  Non-sales / educational?   → Content Script Architect
  Not sure on length?        → Use price point as proxy:
    >$500 price point        → Long-Form VSL Architect
    <$500 / warm list        → Short-Form VSL Writer

SALES PAGE ROUTING DECISION:
  Price > $500 OR complex mechanism OR cold→warm bridge needed?
                             → Copy Lead (deep-persuasion architecture)
  Price < $500 AND warm traffic AND proven offer?
                             → Sales Page Copywriter LITE
4. MARKET TYPE ROUTING LAYER
══════════════════════════════════════════════════════════════════════════

SAAS / B2B
────────────────────────────────────────────────────────────────────────
Awareness Entry:    Solution-Aware or Product-Aware (rarely unaware)
Default Asset Set:  Landing page + Email nurture + Case studies + Ads
Primary Skill:      Copy Lead (has SaaS/B2B template built-in)
Content Skills:     Master Writing Partner (blog/docs), Viral Theme Developer (LinkedIn)
Tone Register:      Authoritative, logical-first, ROI-focused, peer-to-peer
Copy Mode:          Technical-conversational (not hard DR)
Intensity:          2-3 / 5 (educate and demonstrate, not push)
Urgency Style:      Deadline-free or soft urgency (feature launch windows, cohort dates)
CTA Language:       "Start Free Trial" / "Book a Demo" / "See How It Works"
Proof Priority:     Case studies + metrics + integration logos + client logos
Avoid:              Fake countdown timers, aggressive scarcity, transformation-centric language
Neuro-Box Axis:     SMART + SIGNIFICANT primary (left/right axis — logic + social proof)

ECOM / PHYSICAL PRODUCT
────────────────────────────────────────────────────────────────────────
Awareness Entry:    Unaware → Problem-Aware (cold) / Product-Aware (warm retarget)
Default Asset Set:  Product page + Email sequence + Social ads + UGC
Primary Skill:      Sales Page Copywriter LITE (standard) / Copy Lead (hero products)
Video Skills:       Short-Form VSL Writer (warm retarget ads)
Content Skills:     Master Writing Partner (email), Viral Theme Developer (social)
Tone Register:      Visual-led, outcome-focused, lifestyle-aspiration
Copy Mode:          Benefit-forward, testimonial-heavy
Intensity:          3-4 / 5 (urgency and scarcity appropriate when real)
Urgency Style:      Real stock scarcity, sale deadlines, seasonal
CTA Language:       "Add to Cart" / "Get Yours" / "Shop Now"
Proof Priority:     Before/after photos, star ratings, UGC video, volume sold
Avoid:              Long mechanism explanations, complex belief sequences for standard products
Neuro-Box Axis:     SAFE + SPECIAL primary (top/bottom — trust + uniqueness)

HIGH-TICKET (>$1,000 — Coaching, Masterminds, Consulting, Courses)
────────────────────────────────────────────────────────────────────────
Awareness Entry:    Problem-Aware to Solution-Aware
Default Asset Set:  VSL or webinar + Application/booking page + Email sequence
Primary Skill:      Long-Form VSL Architect (cold) / Copy Lead (warm, application page)
Content Skills:     Master Writing Partner (email nurture), Content Script Architect (YT)
Tone Register:      Authority + Empathy, peer-to-peer, transformation-forward
Copy Mode:          Narrative + direct response hybrid (story leads, logic closes)
Intensity:          3-4 / 5 (conviction without aggression)
Urgency Style:      Cohort enrollment limits, application deadlines, access gates
CTA Language:       "Apply Now" / "Book a Strategy Call" / "Join the Program"
Proof Priority:     Transformation stories, income/outcome proof, founder credibility
Avoid:              Cheap urgency tactics, commodity pricing language, generic testimonials
Neuro-Box Axis:     SALVATION + SUPERIOR primary (inspire action + belonging)

INFO PRODUCT / DIGITAL (<$500 — Courses, Templates, Communities, SaaS Lite)
────────────────────────────────────────────────────────────────────────
Awareness Entry:    Problem-Aware to Solution-Aware
Default Asset Set:  Sales page + Email launch sequence + Social content + Ads
Primary Skill:      Copy Lead (if persuasion-complex) / Sales Page Copywriter LITE (if proven offer)
Video Skills:       Short-Form VSL Writer (5-7 min explainer VSL)
Content Skills:     Viral Theme Developer (social), Master Writing Partner (email)
Tone Register:      Educational-aspirational, value-demonstrating, relatable
Copy Mode:          Teaching → selling (earn trust, then ask)
Intensity:          3 / 5
Urgency Style:      Launch windows, price increases, bonuses expiring
CTA Language:       "Get Instant Access" / "Enroll Now" / "Grab Your Copy"
Proof Priority:     Student results, content previews, "what's inside" clarity
Avoid:              Overpromising outcomes, fake guru positioning, thin proof

BRAND / CONTENT (Organic Growth, Audience Building, Awareness)
────────────────────────────────────────────────────────────────────────
Awareness Entry:    Unaware to Problem-Aware
Default Asset Set:  Blog, newsletter, social content, organic video
Primary Skills:     Master Writing Partner, Viral Theme Developer, Content Script Architect
Tone Register:      Brand voice-consistent, value-first, educational, personality-led
Copy Mode:          Serve → share → soft-ask
Intensity:          1-2 / 5 (no hard sell in brand/content layer)
CTA Language:       "Read more" / "Subscribe" / "Follow for more"
Proof Priority:     Consistent publishing, authority positioning, community size
Avoid:              Premature hard CTAs in organic content, overly promotional tone
5. SKILL_ACTIVATION_ORDER — OUTPUT FORMAT
══════════════════════════════════════════════════════════════════════════

SKILL_ACTIVATION_ORDER:
  asset: "[What is being created]"
  skill: "[skill_id from SkillRoster]"
  phase: "[1 / 2 / 3 / 4]"
  team_position: "[TOP or BOTTOM]"

AWARENESS:
  entry: "[Audience awareness level when they arrive]"
  exit: "[Target awareness level when they leave]"
  bridge_required: "[true/false — true if moving >1 stage]"

MARKET_TYPE:
  type: "[saas / ecom / high_ticket / info / brand]"
  price_point: "[price or range]"
  traffic_source: "[cold_paid / warm_email / organic_social / retarget / organic_search]"

STRATEGIC_DIRECTION:
  primary_angle: "[The angle or hook — from MAD or research]"
  core_promise: "[One sentence — the main transformation or outcome]"
  mechanism: "[UMP name + UMS name — exact, from Mechanism Builder]"
  belief_chain: "[Belief numbers to activate, e.g. 1,3,5,7]"

TONE & VOICE:
  primary_register: "[urgency / curiosity / authority / empathy / aspiration / education]"
  copy_mode: "[direct-response / narrative / editorial / conversational / technical]"
  intensity: "[1-5, where 1=educational, 5=hard DR]"
  neuro_box_primary_axis: "[RESONATE / PERSUADE / INFLUENCE / INSPIRE]"
  neuro_box_sequence: "[copy-scripts: SAFE+SPECIAL→SMART+SIGNIFICANT→SUPPORTED+SUPERIOR→STEAL+SALVATION
                       OR conversational: SAFE+SMART→SPECIAL+SIGNIFICANT→SUPPORTED+SUPERIOR→STEAL+SALVATION]"
  voice_notes: "[Brand-specific tone guidance, say-this/not-that if available]"

PROOF_REQUIREMENTS:
  proof_types_needed: "[case studies / testimonials / stats / before-after / income proof / social proof]"
  proof_placement: "[above fold / mid-page / near CTA / throughout]"
  compliance_flags: "[health claims / income claims / platform restrictions — if any]"

CTA:
  primary_cta_text: "[Suggested CTA language]"
  urgency_mechanism: "[real scarcity / deadline / enrollment limit / none]"

HANDOFF:
  receives_from: "[Which skill / asset feeds this one]"
  delivers_to: "[Which skill / asset this feeds next]"
  success_criteria: "[What 'done' looks like for this asset]"
6. NEURO-BOX 7S DIMENSIONS:
  SAFE        — Reader feels protected, not threatened
  SPECIAL     — Offer feels unique, not generic
  SMART       — Logic is clear, decision makes sense
  SIGNIFICANT — Others want this, it matters socially
  SUPPORTED   — Path forward is clear, they can act
  SUPERIOR    — This is the best option, they belong here
  STEAL       — Value overwhelms the price
  SALVATION   — This transforms their life

NEURO-BOX SEQUENCES:
  Copy/Scripts:        SAFE+SPECIAL → SMART+SIGNIFICANT → SUPPORTED+SUPERIOR → STEAL+SALVATION
  Conversational:      SAFE+SMART → SPECIAL+SIGNIFICANT → SUPPORTED+SUPERIOR → STEAL+SALVATION

AXIS PRIORITIES BY MARKET TYPE:
  SaaS/B2B:      SMART + SIGNIFICANT (logic + social proof)
  Ecom:          SAFE + SPECIAL (trust + uniqueness)
  High-Ticket:   SALVATION + SUPERIOR (transformation + belonging)
  Info Product:  SMART + STEAL (value clarity + price rationalization)
  Brand:         SAFE + SUPPORTED (trust + guidance)
7. 

## Failure Modes

No failure modes documented yet.

## Examples

TODO: Add usage examples.

## Notes

No additional notes.

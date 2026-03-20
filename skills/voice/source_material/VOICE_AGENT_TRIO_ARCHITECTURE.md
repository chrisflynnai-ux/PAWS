# VOICE AGENT TRIO ARCHITECTURE
## M5 ATLAS + M6 BRIDGE + M7 CONDUCTOR

**Version:** 1.0.0  
**Purpose:** Complete voice agent sales system from intelligence to execution  
**Philosophy:** Neuro-Box → T.A.P. → Production Deployment

---

## THE TRIO

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         VOICE AGENT TRIO                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  M5: ATLAS                M6: BRIDGE               M7: CONDUCTOR            │
│  "The Intelligence"       "The Conversation"       "The Execution"          │
│  ━━━━━━━━━━━━━━━━━        ━━━━━━━━━━━━━━━━━━       ━━━━━━━━━━━━━━━          │
│                                                                              │
│  WHAT WE KNOW             WHAT WE SAY              HOW WE RUN               │
│  • Company research       • Value-drop scripts     • Platform deployment    │
│  • Contact intel          • T.A.P. framework       • Latency optimization   │
│  • Pain extraction        • 4-phase structure      • Telephony integration  │
│  • Systems mapping        • Objection handling     • Post-call automation   │
│  • Competitor intel       • Channel orchestration  • Human fallback         │
│                           • Guardian scoring       • Productization         │
│                                                                              │
│        ▼                         ▼                        ▼                 │
│  State Artifacts         Conversation Flow         Live Voice Session       │
│        │                         │                        │                 │
│        └─────────────────────────┴────────────────────────┘                 │
│                                  │                                           │
│                         UNIFIED OUTCOME                                      │
│                    "Booked meeting with value delivered"                    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## MODULE ROLES

### M5: ATLAS — The Intelligence Engine
**Codename:** "What We Know"

```yaml
RESPONSIBILITY:
  - Research and enrich leads before conversation
  - Extract pain points and buying signals
  - Map competitive landscape
  - Generate state artifacts for M6
  
OUTPUTS:
  - LeadState JSON (firmographics, contacts, signals)
  - Pain point extraction (primary, evidence, metric)
  - Semantic nuggets (their exact language)
  - Recommended tone and template
  
STATUS: ✅ Complete (8,700+ lines, 5 domains)
```

---

### M6: BRIDGE — The Conversation Engine  
**Codename:** "What We Say"

```yaml
RESPONSIBILITY:
  - Design conversation flow and scripts
  - Personalize using M5 intelligence
  - Handle objections with gift-frame responses
  - Score quality with Guardian 8D
  - Orchestrate across channels
  
OUTPUTS:
  - JIT-assembled messages
  - Voice scripts (T.A.P. framework)
  - Objection response trees
  - Channel routing decisions
  
STATUS: ✅ Complete (8,200+ lines, 7 domains, Value-Drop v2)
```

---

### M7: CONDUCTOR — The Execution Platform
**Codename:** "How We Run"

```yaml
RESPONSIBILITY:
  - Deploy conversations on voice platforms
  - Optimize for sub-500ms latency
  - Integrate telephony/booking/CRM
  - Handle real-time RAG with speed constraints
  - Manage human fallback and escalation
  - Productize for vertical deployment
  
OUTPUTS:
  - Platform configurations (Vapi, Retell, LiveKit)
  - Latency-optimized RAG pipelines
  - Post-call automation workflows
  - Deployment playbooks by vertical
  
STATUS: 📋 TO BUILD (from Voice Agent Master Knowledge)
```

---

## DATA FLOW

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              DATA FLOW                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  LEAD ENTERS                                                                 │
│       │                                                                      │
│       ▼                                                                      │
│  ┌─────────────┐                                                            │
│  │  M5: ATLAS  │ ──► Research ──► Enrich ──► Extract pain                   │
│  └─────────────┘                                                            │
│       │                                                                      │
│       │ State Artifact (JSON)                                               │
│       │ • company_research                                                  │
│       │ • pain_points.primary                                               │
│       │ • semantic_nuggets[]                                                │
│       │ • recommended_tone                                                  │
│       ▼                                                                      │
│  ┌─────────────┐                                                            │
│  │  M6: BRIDGE │ ──► Select template ──► Inject variables ──► Score        │
│  └─────────────┘                                                            │
│       │                                                                      │
│       │ Conversation Script                                                 │
│       │ • T.A.P. opener                                                     │
│       │ • Value drop (phase 2)                                              │
│       │ • Show & tell (phase 3)                                             │
│       │ • Close script (phase 4)                                            │
│       │ • Objection branches                                                │
│       ▼                                                                      │
│  ┌─────────────┐                                                            │
│  │ M7:CONDUCTOR│ ──► Deploy ──► Execute ──► Monitor ──► Automate            │
│  └─────────────┘                                                            │
│       │                                                                      │
│       │ Live Voice Session                                                  │
│       │ • Sub-500ms latency                                                 │
│       │ • Real-time RAG                                                     │
│       │ • Interruption handling                                             │
│       │ • Human fallback triggers                                           │
│       │ • Post-call extraction                                              │
│       ▼                                                                      │
│  OUTCOME                                                                     │
│  • Meeting booked                                                           │
│  • CRM updated                                                              │
│  • Follow-up triggered                                                      │
│  • Learning loop fed                                                        │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## NEURO-BOX + T.A.P. INTEGRATION

### The 4-Phase Voice Architecture

```yaml
PHASE_1_LIFT_OFF:
  neuro_box: "SAFE + SPECIAL"
  tap: "Trust, Authority, Proof"
  
  timing: "0-30 seconds"
  
  components:
    trust:
      signal: "I'm not a bot/scammer"
      script: "Hey {{name}}, did I catch you at a bad time?"
      voice: "Natural pace, warm tone"
    
    authority:
      signal: "I know your industry"
      script: "Just helped {{similar}} with {{result}}"
      voice: "Confident but not arrogant"
    
    proof:
      signal: "I've already done the work"
      script: "Put together the same for {{company}}"
      voice: "Gift energy, not pitch"
  
  goal: "Permission to continue ('OK, I'm listening')"
  
  m7_execution:
    - "Sub-300ms response to opener"
    - "VAD tuned for interruption"
    - "Backchanneling active"

PHASE_2_RELEVANCE:
  neuro_box: "SMART + SIGNIFICANT"
  
  timing: "30-90 seconds"
  
  components:
    smart:
      signal: "Direct, relevant offer"
      script: "Here's the thing—{{specific_insight}}"
      voice: "Pace picks up slightly"
    
    significant:
      signal: "Clear value and outcome"
      script: "Could mean {{outcome}} in {{timeframe}}"
      voice: "Emphasis on numbers"
  
  goal: "Interest sparked ('That sounds useful')"
  
  m7_execution:
    - "Knowledge RAG < 350ms"
    - "Dynamic variable injection"
    - "Sentiment monitoring active"

PHASE_3_VISUALIZATION:
  neuro_box: "SUPPORTED + SUPERIOR"
  
  timing: "90 seconds - 3 minutes"
  
  components:
    supported:
      signal: "Walk through scenario"
      script: "Here's how it would work for {{company}}..."
      voice: "Slower, collaborative"
    
    superior:
      signal: "Demonstrate solution"
      script: "[SCREEN SHARE] This is what I made..."
      voice: "Show confidence"
  
  goal: "Belief established ('I can see this working')"
  
  m7_execution:
    - "Screen share if video call"
    - "Gamma doc ready for send"
    - "Tool calls deferred to post-show"

PHASE_4_CLOSE:
  neuro_box: "SALVATION + STEAL"
  
  timing: "3-5 minutes"
  
  components:
    salvation:
      signal: "Breakthrough they desire"
      script: "This is what we did for {{similar}}—{{result}}"
      voice: "Inspiring, peer success"
    
    steal:
      signal: "Irresistible offer"
      script: "Want me to set this up? Free until it works."
      voice: "Confident, no pressure"
  
  goal: "Commitment ('Yes, let's do it')"
  
  m7_execution:
    - "Calendar API ready"
    - "Booking confirmation immediate"
    - "SMS bridge trigger"
```

---

## M7 CONDUCTOR: DOMAIN STRUCTURE

Based on Voice Agent Master Knowledge, M7 should have **6 domains**:

```yaml
M7_DOMAINS:

  domain_1:
    name: "Platform Architecture"
    covers:
      - "Cascade vs End-to-End Multimodal"
      - "Realtime APIs (WebRTC, WebSockets)"
      - "Platform selection (Vapi, Retell, LiveKit, Gemini Live)"
      - "Full-duplex and interruption handling"
      - "Native S2S integration patterns"
    
    from_source: "Module 1: Industry Shift"

  domain_2:
    name: "Core Stack Integration"
    covers:
      - "Telephony/SIP layer"
      - "Conversation engine configuration"
      - "Tool integration (booking, CRM, calendar)"
      - "Post-call automation pipelines"
      - "Backend workflow patterns"
    
    from_source: "Module 2: Core Voice Stack"

  domain_3:
    name: "Agent Experience Design"
    covers:
      - "Naturalness and timing"
      - "Interruption sensitivity tuning"
      - "Backchanneling patterns"
      - "Voice selection and humanization"
      - "Deterministic vs creative output"
    
    from_source: "Module 3: Agent Experience Design"

  domain_4:
    name: "Voice RAG & Knowledge"
    covers:
      - "Latency budget architecture"
      - "Local vs cloud vector stores"
      - "Embedding optimization"
      - "Caching strategies"
      - "Hallucination prevention"
    
    from_source: "Module 4: Prompting, KB, Voice RAG"

  domain_5:
    name: "Business Workflow Patterns"
    covers:
      - "Receptionist flows"
      - "Booking/scheduling patterns"
      - "Qualification workflows"
      - "Support triage"
      - "Speed-to-lead execution"
    
    from_source: "Module 5 + 6: Business & Sales Workflows"

  domain_6:
    name: "Production Operations"
    covers:
      - "Compliance and disclosure"
      - "Human fallback design"
      - "Latency monitoring"
      - "Verticalization playbooks"
      - "Agency delivery patterns"
    
    from_source: "Module 7-10: Automation, Performance, Compliance, Productization"
```

---

## NOTEBOOKLM EXTRACTION QUERIES

To extract deep knowledge from your new notebook, use these atomic queries:

### Query M7.1: Platform Architecture

```
EXTRACTION QUERY: Platform Architecture

Extract specific technical patterns for voice platform deployment:

1. REALTIME API PATTERNS
   - WebRTC configuration details
   - WebSocket setup for voice streaming
   - Platform-specific integration (Vapi, Retell, LiveKit)
   - Audio codec considerations

2. MULTIMODAL SYSTEM DESIGN
   - Native S2S vs cascade architecture
   - When to use which approach
   - Latency comparisons with specific numbers
   - Provider capabilities matrix

3. INTERRUPTION HANDLING
   - VAD configuration parameters
   - Sensitivity thresholds (specific numbers)
   - Barge-in behavior tuning
   - Turn-taking logic

FORMAT: Technical specifications with code snippets and config examples.
SKIP: High-level concepts (already have those).
TARGET: ~100 lines of implementation detail.
```

### Query M7.2: Latency Engineering

```
EXTRACTION QUERY: Latency Engineering

Extract specific latency optimization patterns:

1. LATENCY BUDGETS
   - Exact ms thresholds for each component
   - Total budget breakdown (VAD, STT, LLM, TTS)
   - Where to measure and monitor
   - Acceptable vs unacceptable ranges

2. RAG OPTIMIZATION
   - Local FAISS configuration
   - Embedding latency reduction techniques
   - Chunk size optimization for voice
   - Caching implementation patterns

3. DATABASE SELECTION
   - Latency benchmarks by provider
   - When local beats cloud (specific thresholds)
   - Configuration for sub-500ms retrieval
   - Failure mode handling

FORMAT: Benchmarks, configs, and decision trees.
SKIP: General advice.
TARGET: ~100 lines of specific numbers and patterns.
```

### Query M7.3: Post-Call Automation

```
EXTRACTION QUERY: Post-Call Automation

Extract post-call workflow patterns:

1. STRUCTURED EXTRACTION
   - JSON schema for call outcomes
   - What to extract and when
   - LLM prompt for transcript analysis
   - Field mapping to CRM

2. AUTOMATION TRIGGERS
   - Webhook event definitions
   - n8n/Make workflow patterns
   - Slack/email notification logic
   - Calendar/booking integration

3. FOLLOW-UP SEQUENCES
   - Trigger conditions
   - Timing rules
   - Content selection logic
   - Escalation criteria

FORMAT: Workflow diagrams, JSON schemas, n8n patterns.
SKIP: Conceptual explanations.
TARGET: ~100 lines of implementation patterns.
```

### Query M7.4: Human Fallback Design

```
EXTRACTION QUERY: Human Fallback Design

Extract escalation and fallback patterns:

1. TRIGGER CONDITIONS
   - Sentiment thresholds (specific numbers)
   - Keyword detection patterns
   - Objection count limits
   - Complexity signals

2. TRANSFER TYPES
   - Hot transfer implementation
   - Warm transfer with context
   - Cold transfer patterns
   - Callback scheduling

3. CONTEXT HANDOFF
   - What to pass to human
   - Summary generation
   - Priority signaling
   - Queue management

FORMAT: Decision trees, scripts, config patterns.
SKIP: General fallback philosophy.
TARGET: ~100 lines of implementation detail.
```

### Query M7.5: Vertical Deployment

```
EXTRACTION QUERY: Vertical Deployment

Extract productization patterns by industry:

1. LOCAL SERVICES
   - HVAC/Plumbing receptionist config
   - Dental/medical booking patterns
   - Emergency vs routine routing
   - After-hours handling

2. PROFESSIONAL SERVICES
   - Law firm intake
   - Accounting/consulting qualification
   - High-ticket routing rules
   - Compliance requirements

3. E-COMMERCE/SAAS
   - Support triage patterns
   - Order status handling
   - Refund/return flows
   - Account management

FORMAT: Vertical-specific configs and prompt templates.
SKIP: Generic advice.
TARGET: ~100 lines of vertical patterns.
```

### Query M7.6: Speed-to-Lead Execution

```
EXTRACTION QUERY: Speed-to-Lead Execution

Extract immediate response patterns:

1. TRIGGER → CALL TIMING
   - Form fill to call latency targets
   - Webhook configuration
   - Queue management
   - Concurrent call handling

2. OPENING SCRIPT VARIANTS
   - By lead source
   - By time of day
   - By urgency signal
   - Warm vs cold form fills

3. BOOKING FLOW
   - Availability check timing
   - Calendar integration patterns
   - SMS bridge execution
   - Confirmation sequence

FORMAT: Timing specs, scripts, workflow configs.
SKIP: Why speed matters (we know).
TARGET: ~100 lines of execution patterns.
```

---

## BUILD PLAN

```yaml
SESSION_1: (Current)
  deliverables:
    - Voice Agent Trio Architecture ✅ (this doc)
    - M7 CONDUCTOR Domain Structure ✅ (above)
    - NotebookLM Extraction Queries ✅ (above)
    - M6 Voice Skill XML (below)

SESSION_2: (Next conversation)
  input: "NotebookLM extractions from new notebook"
  deliverables:
    - M7 Domain 1: Platform Architecture
    - M7 Domain 2: Core Stack Integration
    - M7 Domain 3: Agent Experience Design

SESSION_3:
  deliverables:
    - M7 Domain 4: Voice RAG & Knowledge
    - M7 Domain 5: Business Workflow Patterns
    - M7 Domain 6: Production Operations
    - M7 Complete Integration

FINAL:
  - M5 ATLAS (8,700 lines) ✅
  - M6 BRIDGE (8,200 lines) ✅
  - M7 CONDUCTOR (~6,000 lines target)
  - TRIO_ORCHESTRATION.md
  - Deployment Playbook
```

---

## QUICK REFERENCE: TRIO SYNERGY

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         TRIO SYNERGY MATRIX                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  QUESTION              M5 ANSWERS    M6 ANSWERS     M7 ANSWERS              │
│  ─────────────────     ──────────    ──────────     ──────────              │
│  Who is this lead?     ✓                                                    │
│  What's their pain?    ✓                                                    │
│  What should we say?                 ✓                                      │
│  How personalized?                   ✓                                      │
│  Is it good quality?                 ✓                                      │
│  Which platform?                                    ✓                       │
│  Will it be fast?                                   ✓                       │
│  What if they're mad?                               ✓                       │
│  What happens after?                                ✓                       │
│  Can we scale this?                                 ✓                       │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

*Voice Agent Trio Architecture v1.0*
*"Intelligence → Conversation → Execution"*

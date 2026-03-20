# M7 CONDUCTOR — DOMAIN 4: HUMAN FALLBACK DESIGN
## Escalation, Transfer & Safety Patterns

**Version:** 1.0.0  
**Module:** M7 CONDUCTOR (The Execution)  
**Domain:** 4 of 6  
**Lines:** ~700  
**Source:** NotebookLM Voice Architecture Synthesis

---

## DOMAIN OVERVIEW

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      HUMAN FALLBACK SCOPE                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  "Human fallback is not failure—it's good design."                          │
│                                                                              │
│  THIS DOMAIN ANSWERS:                                                        │
│  • When should the agent transfer to a human?                               │
│  • What context should the human receive?                                   │
│  • How do we handle security/compliance escalations?                        │
│  • What are the transfer types and when to use each?                        │
│                                                                              │
│  NON-NEGOTIABLE:                                                            │
│  Human fallback MUST exist for:                                             │
│  • Frustrated users                                                         │
│  • "I want a real person" requests                                          │
│  • Compliance/security triggers                                             │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 4.1 TRIGGER CONDITIONS

### Decision Tree & Thresholds

```yaml
ESCALATION_TRIGGERS:

  sentiment_objection_limits:
    rule_1:
      condition: "sentiment.score < 0.3 OR sentiment.anger > 0.9"
      action: "forced_escalation(hot)"
      script: "I want to make sure this gets sorted out. Let me connect you right now."
      
    rule_2:
      condition: "objection_count > 3 OR consecutive_same_objection > 2"
      action: "offer_handover(warm)"
      script: "I hear you. Would you like me to connect you with a specialist?"
      
    rule_3:
      condition: 'intent.exact_match IN ["speak to a real person", "connect me to support", "human please"]'
      action: "forced_escalation(immediate)"
      script: "Absolutely. Let me get someone for you."

  complexity_knowledge_gaps:
    rule_4:
      condition: 'llm_judge.status == "No relevant clause found" OR llm_judge.hallucination_risk == "High"'
      action: "offer_handover(warm)"
      script: "I want to make sure you get accurate information. Let me transfer you to someone who can help."
      
    rule_5:
      condition: 'user_request == "complex_jurisdiction_rules" AND region == "Unknown"'
      action: "forced_escalation(tier_2)"
      script: "That's a specialized area. Let me connect you with our expert team."

  compliance_security:
    rule_6:
      condition: 'data_request == "PHI" AND user.auth_status == "unverified"'
      action: "reply_and_continue(auth_workflow)"
      script: "I can't access or share those details until we verify you."
      
    rule_7:
      condition: 'security_monitor.detect == "prompt_injection" OR user.intent == "instruction_override"'
      action: "forced_escalation(security_queue)"
      script: "I cannot help with that request. I'm routing your call to our specialized team."
      
    rule_8:
      condition: 'topic_classifier == "SAR/investigation"'
      action: "forced_escalation(BSA_AML_queue)"
      script: "I cannot help with questions about internal reviews. Let me connect you to the appropriate department."
```

### Visual Decision Tree

```
START: Evaluate Turn
         │
         ▼
┌────────────────────────┐
│ Explicit Human Request?│─────YES────► IMMEDIATE TRANSFER
└────────────────────────┘              "Absolutely, let me get someone."
         │
         NO
         ▼
┌────────────────────────┐
│ Security/Compliance    │─────YES────► FORCED ESCALATION
│ Trigger Detected?      │              (security_queue)
└────────────────────────┘
         │
         NO
         ▼
┌────────────────────────┐
│ Sentiment < 0.3 OR     │─────YES────► HOT TRANSFER
│ Anger > 0.9?           │              "Let me connect you right now."
└────────────────────────┘
         │
         NO
         ▼
┌────────────────────────┐
│ Objections > 3 OR      │─────YES────► OFFER WARM TRANSFER
│ Same Objection x2?     │              "Would you like to speak with..."
└────────────────────────┘
         │
         NO
         ▼
┌────────────────────────┐
│ Outside Knowledge Base │─────YES────► OFFER WARM TRANSFER
│ OR Hallucination Risk? │              "Let me connect you with an expert."
└────────────────────────┘
         │
         NO
         ▼
┌────────────────────────┐
│ PHI Request +          │─────YES────► AUTH WORKFLOW
│ Unverified User?       │              "I need to verify you first."
└────────────────────────┘
         │
         NO
         ▼
    CONTINUE CONVERSATION
```

---

## 4.2 TRANSFER TYPES

### Reply + Continue (In-Bounds Fallback)

```yaml
REPLY_AND_CONTINUE:

  purpose: "Handle request without transferring"
  
  triggers:
    - "Unauthenticated request for restricted info"
    - "Missing workflow prerequisites"
    - "Request can be handled with alternative"
    
  system_actions:
    1. "Refuse specific request neutrally"
    2. "Lock restricted tools"
    3. "Keep conversation active"
    4. "Initiate authentication/alternative workflow"
    
  script_examples:
    unverified_phi: |
      "I can't access or share claim-specific details 
       until we verify you. Can I get your member ID 
       and date of birth?"
       
    missing_info: |
      "I'd need your order number to look that up. 
       Do you have it handy?"
       
    outside_scope: |
      "I can't make changes to that, but I can 
       walk you through how to do it yourself."
```

### Offer Handover (Warm Transfer)

```yaml
OFFER_HANDOVER:

  purpose: "Give customer choice to transfer"
  
  triggers:
    - "Missing retrieval grounding"
    - "Edge-case complexity"
    - "Repeated objections (no security risk)"
    - "Customer seems frustrated but not angry"
    
  system_actions:
    1. "State inability to proceed safely"
    2. "Ask permission to transfer"
    3. "Compile context package if accepted"
    4. "Execute SIP/telephony transfer"
    
  script_examples:
    knowledge_gap: |
      "I cannot confirm coverage without the exact 
       policy language. Would you like me to transfer 
       you to a licensed claims specialist?"
       
    complexity: |
      "That's a specialized question. I can connect 
       you with someone who handles these cases daily. 
       Would that help?"
       
    repeated_objection: |
      "I hear your concern. Would you prefer to 
       speak with a team member who can give you 
       more details?"
```

### Forced Escalation (Hot Transfer)

```yaml
FORCED_ESCALATION:

  purpose: "Transfer without asking (safety/compliance)"
  
  triggers:
    - "Jailbreak/prompt injection attempts"
    - "Confidential compliance inquiries (tipping-off risk)"
    - "High anger/frustration"
    - "Explicit human request"
    - "Security red flags"
    
  system_actions:
    1. "Immediately route to specialized human queue"
    2. "Constrain further dialog (prevent tool manipulation)"
    3. "Log as security/compliance signal"
    4. "No choice offered to user"
    
  script_examples:
    security_block: |
      "I cannot help with questions about internal reviews. 
       I am routing your call to our specialized team."
       
    human_request: |
      "Absolutely, let me get someone for you."
      
    high_anger: |
      "I can hear this is frustrating. Let me connect 
       you with someone who can help right away."
```

### Callback Scheduling (Async)

```yaml
CALLBACK_SCHEDULING:

  purpose: "Defer to human when unavailable"
  
  triggers:
    - "Agents unavailable"
    - "Outside business hours"
    - "User prefers callback"
    - "Complex issue requiring research"
    
  system_actions:
    1. "Create async ticket"
    2. "Generate automated summary"
    3. "Schedule callback calendar event"
    4. "Send confirmation SMS/email"
    
  script_examples:
    after_hours: |
      "Our team isn't available right now, but I can 
       schedule a callback. What time works best tomorrow?"
       
    complex_research: |
      "This will need some research. Can I have someone 
       call you back within 2 hours with the answer?"
```

---

## 4.3 CONTEXT HANDOFF

### Context Package Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "TransferContextPackage",
  "description": "Context passed to human agent on transfer",
  "type": "object",
  "properties": {
    "lead_identity": {
      "type": "object",
      "properties": {
        "name": {"type": "string"},
        "phone": {"type": "string"},
        "email": {"type": ["string", "null"]},
        "auth_status": {"type": "boolean"}
      },
      "required": ["name", "phone", "auth_status"]
    },
    "transfer_trigger": {
      "type": "string",
      "enum": [
        "hallucination_risk",
        "anger",
        "prompt_injection",
        "explicit_request",
        "missing_auth",
        "objection_limit",
        "knowledge_gap",
        "compliance_block"
      ]
    },
    "conversation_summary": {
      "type": "string",
      "maxLength": 500,
      "description": "Max 3 sentences"
    },
    "identified_intent": {
      "type": "string",
      "description": "What the user is trying to accomplish"
    },
    "key_metadata": {
      "type": "object",
      "description": "Extracted data points"
    },
    "last_failed_action": {
      "type": ["string", "null"],
      "description": "What the agent couldn't do"
    },
    "objections_raised": {
      "type": "array",
      "items": {"type": "string"}
    },
    "sentiment_score": {
      "type": "number",
      "minimum": -1,
      "maximum": 1
    },
    "full_transcript_link": {
      "type": "string",
      "format": "uri"
    }
  },
  "required": [
    "lead_identity",
    "transfer_trigger",
    "conversation_summary",
    "identified_intent"
  ]
}
```

### Summary Generation Rules

```python
# CONTEXT SUMMARY GENERATION FOR TRANSFER

class TransferSummaryGenerator:
    """
    Generate context summary for human handoff.
    Max 3 sentences, privacy-aware.
    """
    
    def __init__(self):
        self.max_sentences = 3
        self.max_chars = 500
        
    async def generate_summary(
        self,
        transcript: str,
        extracted_intent: str,
        auth_status: bool
    ) -> dict:
        """
        Generate transfer context summary.
        
        Privacy Rule: Omit PII/PHI if user unverified.
        """
        
        prompt = f"""
Summarize this conversation for a human agent taking over.

RULES:
- Maximum 3 sentences
- Focus on: what the user wants, what's been tried, why transfer needed
- {'OMIT any personally identifiable information' if not auth_status else 'Include relevant details'}

TRANSCRIPT:
{transcript}

IDENTIFIED INTENT:
{extracted_intent}

OUTPUT FORMAT:
{{
  "conversation_summary": "string (max 3 sentences)",
  "identified_intent": "string (one line)",
  "recommended_action": "string (suggestion for human)"
}}
"""
        
        result = await self._call_llm(prompt)
        return result
    
    def build_context_package(
        self,
        caller: dict,
        summary: dict,
        trigger: str,
        metadata: dict
    ) -> dict:
        """
        Build full context package for transfer.
        """
        
        return {
            "lead_identity": {
                "name": caller.get("name"),
                "phone": caller.get("phone"),
                "email": caller.get("email"),
                "auth_status": caller.get("verified", False)
            },
            "transfer_trigger": trigger,
            "conversation_summary": summary["conversation_summary"],
            "identified_intent": summary["identified_intent"],
            "key_metadata": metadata,
            "last_failed_action": metadata.get("last_failed_action"),
            "objections_raised": metadata.get("objections", []),
            "sentiment_score": metadata.get("sentiment", 0),
            "full_transcript_link": f"https://dashboard.com/calls/{metadata['call_id']}"
        }
```

---

## 4.4 QUEUE MANAGEMENT

### Priority Routing

```yaml
QUEUE_PRIORITY_ROUTING:

  priority_1_critical:
    triggers:
      - 'transfer_trigger == "prompt_injection"'
      - 'transfer_trigger == "SAR_inquiry"'
      - 'compliance_flag == true'
    route_to: "Compliance/Security Operations"
    response_sla: "< 30 seconds"
    notification: "Immediate page to on-call"
    
  priority_2_urgent:
    triggers:
      - 'sentiment < 0.3'
      - 'VIP_account == true'
      - 'anger_detected == true'
    route_to: "Senior Retention Queue"
    response_sla: "< 2 minutes"
    notification: "Slack alert to team lead"
    
  priority_3_standard:
    triggers:
      - 'transfer_trigger == "hallucination_risk"'
      - 'transfer_trigger == "explicit_request"'
      - 'transfer_trigger == "knowledge_gap"'
    route_to: "General Support / Technical Specialist"
    response_sla: "< 5 minutes"
    notification: "Queue notification"
    
  priority_4_callback:
    triggers:
      - 'outside_business_hours == true'
      - 'all_agents_busy == true'
    route_to: "Callback Queue"
    response_sla: "Next business day"
    notification: "Ticket created"
```

### Queue Implementation

```python
# PRIORITY QUEUE ROUTING

from enum import IntEnum
from dataclasses import dataclass
from typing import Optional
import asyncio

class Priority(IntEnum):
    CRITICAL = 1
    URGENT = 2
    STANDARD = 3
    CALLBACK = 4

@dataclass
class TransferRequest:
    call_id: str
    caller_phone: str
    trigger: str
    context_package: dict
    priority: Priority
    queue_name: str
    created_at: float

class TransferRouter:
    """
    M7 CONDUCTOR: Priority-based transfer routing.
    """
    
    def __init__(self):
        self.queues = {
            "security": asyncio.Queue(),
            "retention": asyncio.Queue(),
            "support": asyncio.Queue(),
            "callback": asyncio.Queue()
        }
        
    def determine_priority(
        self,
        trigger: str,
        sentiment: float,
        is_vip: bool,
        compliance_flag: bool
    ) -> tuple[Priority, str]:
        """
        Determine priority and queue based on transfer context.
        """
        
        # Priority 1: Critical/Security
        if trigger in ["prompt_injection", "SAR_inquiry"] or compliance_flag:
            return Priority.CRITICAL, "security"
            
        # Priority 2: Urgent/At-Risk
        if sentiment < 0.3 or is_vip:
            return Priority.URGENT, "retention"
            
        # Priority 3: Standard
        if trigger in ["hallucination_risk", "explicit_request", "knowledge_gap"]:
            return Priority.STANDARD, "support"
            
        # Priority 4: Callback
        return Priority.CALLBACK, "callback"
    
    async def route_transfer(
        self,
        request: TransferRequest
    ):
        """
        Route transfer request to appropriate queue.
        """
        
        queue = self.queues[request.queue_name]
        await queue.put(request)
        
        # Notify based on priority
        if request.priority == Priority.CRITICAL:
            await self._page_oncall(request)
        elif request.priority == Priority.URGENT:
            await self._notify_team_lead(request)
        else:
            await self._notify_queue(request)
    
    async def _page_oncall(self, request: TransferRequest):
        """Immediate page for critical transfers."""
        # Integration: PagerDuty, Opsgenie, etc.
        pass
    
    async def _notify_team_lead(self, request: TransferRequest):
        """Slack DM to team lead for urgent transfers."""
        pass
    
    async def _notify_queue(self, request: TransferRequest):
        """Standard queue notification."""
        pass
```

---

## 4.5 TRANSFER SCRIPTS

### By Transfer Type

```yaml
TRANSFER_SCRIPTS:

  immediate_human_request:
    trigger: "User explicitly asks for human"
    script: "Absolutely. Let me get someone for you."
    note: "No argument, no delay, just transfer"
    
  hot_transfer_anger:
    trigger: "High anger detected"
    script: |
      "I can hear this is frustrating. 
       Let me connect you with someone who can help right away."
    note: "Acknowledge emotion, promise immediate help"
    
  warm_transfer_knowledge:
    trigger: "Outside knowledge base"
    script: |
      "I want to make sure you get accurate information. 
       Would you like me to connect you with a specialist?"
    note: "Ask permission, explain why"
    
  warm_transfer_complexity:
    trigger: "Complex edge case"
    script: |
      "That's a specialized area. 
       I can connect you with someone who handles these daily. 
       Would that help?"
    note: "Position human as expert, not AI as failure"
    
  callback_after_hours:
    trigger: "Outside business hours"
    script: |
      "Our team isn't available right now. 
       Can I schedule a callback? 
       What time works best for you tomorrow?"
    note: "Offer specific solution"
    
  security_block:
    trigger: "Prompt injection or compliance issue"
    script: |
      "I cannot help with that request. 
       I'm routing your call to our specialized team."
    note: "Firm but neutral, no explanation"
    
  authentication_required:
    trigger: "Unverified user requests sensitive data"
    script: |
      "I can't access those details until we verify you. 
       Can I get your member ID and date of birth?"
    note: "Start auth workflow, don't transfer"
```

---

## 4.6 SAFETY GUARDRAILS

### Compliance Escalation

```yaml
COMPLIANCE_SAFETY_PATTERNS:

  tipping_off_prevention:
    context: "Financial services, anti-money laundering"
    trigger: 'topic_classifier == "SAR/investigation"'
    action: |
      Agent CANNOT discuss whether an investigation exists.
      Forced escalation to BSA/AML team.
      No confirmation or denial to caller.
    script: |
      "I cannot help with questions about internal reviews. 
       I'm routing your call to the appropriate department."
      
  hipaa_phi_protection:
    context: "Healthcare"
    trigger: 'data_request == "PHI" AND user.auth_status == "unverified"'
    action: |
      Block all PHI disclosure.
      Initiate authentication workflow.
      If auth fails, route to human.
    script: |
      "I need to verify your identity before I can access 
       your health information. This is for your protection."
      
  prompt_injection_defense:
    context: "All domains"
    trigger: 'security_monitor.detect == "prompt_injection"'
    action: |
      Block all tool calls immediately.
      Force escalation to security queue.
      Log incident for review.
    script: |
      "I cannot help with that request. 
       I'm connecting you with our team."
    note: "Never explain what triggered the block"
```

### Transfer Failure Handling

```yaml
TRANSFER_FAILURE_HANDLING:

  no_agents_available:
    detection: "SIP timeout or queue overflow"
    action_1: "Offer callback scheduling"
    action_2: "Create urgent ticket"
    action_3: "Alert operations team"
    script: |
      "I apologize—all our team members are currently helping 
       other customers. Can I schedule a callback within the hour?"
       
  transfer_dropped:
    detection: "Call disconnected during transfer"
    action_1: "Auto-create callback ticket"
    action_2: "Send SMS: 'We got disconnected. Call you back shortly.'"
    action_3: "Alert supervisor"
    
  repeated_transfer_failure:
    detection: 'transfer_failures >= 2'
    action_1: "Email/Slack alert to admin"
    action_2: "Log as critical incident"
    action_3: "Escalate to on-call engineer"
```

---

## PYDANTIC SCHEMAS

```python
from pydantic import BaseModel, Field
from typing import Optional, List, Literal
from enum import Enum

class TransferTrigger(str, Enum):
    HALLUCINATION_RISK = "hallucination_risk"
    ANGER = "anger"
    PROMPT_INJECTION = "prompt_injection"
    EXPLICIT_REQUEST = "explicit_request"
    MISSING_AUTH = "missing_auth"
    OBJECTION_LIMIT = "objection_limit"
    KNOWLEDGE_GAP = "knowledge_gap"
    COMPLIANCE_BLOCK = "compliance_block"

class TransferType(str, Enum):
    REPLY_CONTINUE = "reply_and_continue"
    OFFER_HANDOVER = "offer_handover"
    FORCED_ESCALATION = "forced_escalation"
    CALLBACK_SCHEDULING = "callback_scheduling"

class Priority(str, Enum):
    CRITICAL = "critical"
    URGENT = "urgent"
    STANDARD = "standard"
    CALLBACK = "callback"

class LeadIdentity(BaseModel):
    name: str
    phone: str
    email: Optional[str] = None
    auth_status: bool = False

class ContextPackage(BaseModel):
    """M7 Domain 4: Transfer context package."""
    
    lead_identity: LeadIdentity
    transfer_trigger: TransferTrigger
    conversation_summary: str = Field(..., max_length=500)
    identified_intent: str
    key_metadata: dict = Field(default_factory=dict)
    last_failed_action: Optional[str] = None
    objections_raised: List[str] = Field(default_factory=list)
    sentiment_score: float = Field(ge=-1, le=1, default=0)
    full_transcript_link: Optional[str] = None

class TransferDecision(BaseModel):
    """Transfer routing decision."""
    
    should_transfer: bool
    transfer_type: Optional[TransferType] = None
    priority: Optional[Priority] = None
    queue_name: Optional[str] = None
    script: Optional[str] = None
    context_package: Optional[ContextPackage] = None
```

---

*M7 CONDUCTOR Domain 4 v1.0.0*
*Human Fallback Design — "Transfer quickly when it matters"*

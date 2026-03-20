# M7 CONDUCTOR — DOMAIN 3: POST-CALL AUTOMATION
## Webhooks, Extraction & Workflow Integration

**Version:** 1.0.0  
**Module:** M7 CONDUCTOR (The Execution)  
**Domain:** 3 of 6  
**Lines:** ~800  
**Source:** NotebookLM Voice Architecture Synthesis

---

## DOMAIN OVERVIEW

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    POST-CALL AUTOMATION SCOPE                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  "The backend is the product. The voice is just the interface."            │
│                                                                              │
│  THIS DOMAIN ANSWERS:                                                        │
│  • What data do we extract from calls?                                      │
│  • How do we trigger downstream automations?                                │
│  • What's the n8n/Make workflow pattern?                                    │
│  • How do we handle follow-up sequences?                                    │
│                                                                              │
│  CRITICAL RULE:                                                             │
│  Execute heavy automations POST-CALL, not during.                           │
│  Live tool calls create awkward silences.                                   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3.1 STRUCTURED DATA EXTRACTION

### Call Outcome JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "VoiceCallOutcome",
  "description": "M7 CONDUCTOR: Structured extraction from voice calls",
  "type": "object",
  "properties": {
    "caller_name": {
      "type": "string",
      "description": "Full name of the caller"
    },
    "caller_phone": {
      "type": "string",
      "description": "Phone number for CRM matching"
    },
    "caller_email": {
      "type": ["string", "null"],
      "description": "Email if provided"
    },
    "service_address": {
      "type": ["string", "null"],
      "description": "Physical address for service businesses"
    },
    "issue_type": {
      "type": "string",
      "description": "Primary issue or inquiry category"
    },
    "issue_details": {
      "type": "string",
      "description": "Detailed description of the issue"
    },
    "is_urgent": {
      "type": "boolean",
      "description": "Emergency or time-sensitive flag"
    },
    "qualification_score": {
      "type": "integer",
      "minimum": 1,
      "maximum": 10,
      "description": "Lead quality score 1-10"
    },
    "appointment_confirmed": {
      "type": "boolean",
      "description": "Whether a meeting was booked"
    },
    "appointment_datetime": {
      "type": ["string", "null"],
      "format": "date-time",
      "description": "Scheduled appointment time"
    },
    "objections_raised": {
      "type": "array",
      "items": {"type": "string"},
      "description": "List of objections encountered"
    },
    "next_action": {
      "type": "string",
      "enum": ["follow_up", "transfer", "close_won", "close_lost", "nurture"],
      "description": "Recommended next step"
    },
    "call_summary": {
      "type": "string",
      "maxLength": 500,
      "description": "2-3 sentence summary"
    },
    "sentiment_score": {
      "type": "number",
      "minimum": -1,
      "maximum": 1,
      "description": "Overall sentiment (-1 negative to +1 positive)"
    },
    "custom_fields": {
      "type": "object",
      "description": "Vertical-specific extracted data"
    }
  },
  "required": [
    "caller_name",
    "caller_phone",
    "issue_type",
    "is_urgent",
    "appointment_confirmed",
    "call_summary"
  ]
}
```

### Extraction Rules

```yaml
EXTRACTION_TIMING:

  rule: "Execute extraction ONLY post-call during call_analyzed webhook"
  
  never_during_call:
    - "Heavy LLM analysis"
    - "CRM writes"
    - "Notification sending"
    - "Complex data parsing"
    
  reason: |
    Running automations during live calls causes:
    - Latency spikes
    - Awkward silences
    - User frustration
    
  exception: |
    Only essential tools during call:
    - check_availability (fast API)
    - book_appointment (essential)
```

### LLM Extraction Prompt

```python
# POST-CALL TRANSCRIPT ANALYSIS PROMPT

EXTRACTION_PROMPT = """
Analyze the entire transcript of the conversation to extract 
structured data for CRM and automation systems.

TRANSCRIPT:
{transcript}

EXTRACTION INSTRUCTIONS:
1. Extract the caller's name and phone number
2. Extract service address if provided
3. Identify the primary issue type from context
4. Assess if the issue is urgent (boolean)
5. Determine if an appointment was successfully booked
6. Extract appointment datetime if booked
7. List any objections the caller raised
8. Calculate a qualification score (1-10)
9. Generate a 2-3 sentence call summary
10. Assess overall sentiment (-1 to +1)

CUSTOM FIELD EXTRACTION ({vertical}):
{custom_extraction_rules}

IMPORTANT:
- If data is not explicitly provided, leave null (do not guess)
- Use exact quotes for issue details when possible
- Qualification score: 1-3 (cold), 4-6 (warm), 7-10 (hot)

OUTPUT FORMAT:
Return valid JSON matching the VoiceCallOutcome schema.
"""

# Vertical-specific custom extraction
VERTICAL_RULES = {
    "legal": """
        - Extract law_type (personal injury, family law, estate, business)
        - Extract case_urgency (statute of limitations concern)
        - Extract opposing_party if mentioned
    """,
    "hvac": """
        - Extract equipment_type (AC, heating, water heater)
        - Extract equipment_age if mentioned
        - Extract last_service_date if mentioned
    """,
    "dental": """
        - Extract procedure_type (cleaning, filling, extraction, etc.)
        - Extract pain_level (1-10 if mentioned)
        - Extract insurance_provider if mentioned
    """,
    "saas": """
        - Extract product_interest
        - Extract current_solution
        - Extract team_size
        - Extract decision_timeline
    """
}
```

### Field Mapping to CRM

```yaml
CRM_FIELD_MAPPING:

  # Standard mappings (most CRMs)
  standard_fields:
    caller_name: "Contact.FullName"
    caller_phone: "Contact.Phone"  # Also used as matching key
    caller_email: "Contact.Email"
    service_address: "Contact.Address"
    issue_type: "Deal.Category OR Contact.Tags"
    call_summary: "Activity.Notes"
    qualification_score: "Lead.Score"
    
  # Platform-specific mappings
  hubspot:
    appointment_confirmed: "Deal.Stage = 'Appointment Set'"
    is_urgent: "Contact.Priority = 'High'"
    sentiment_score: "Contact.hs_lead_status"
    
  salesforce:
    appointment_confirmed: "Opportunity.StageName = 'Meeting Scheduled'"
    is_urgent: "Lead.Rating = 'Hot'"
    call_summary: "Task.Description"
    
  gohighlevel:
    appointment_confirmed: "Opportunity.Pipeline.Stage"
    is_urgent: "Contact.Tags += 'URGENT'"
    custom_fields: "Contact.CustomFields"
    
  pipedrive:
    appointment_confirmed: "Deal.Stage"
    qualification_score: "Lead.Label"
```

---

## 3.2 WEBHOOK EVENT ARCHITECTURE

### Event Definitions

```yaml
WEBHOOK_EVENTS:

  call_started:
    trigger: "Agent answers or initiates call"
    payload:
      - call_id
      - timestamp
      - caller_phone
      - direction (inbound/outbound)
    use_case: "Start live session logging"
    
  call_ended:
    trigger: "Call hangup detected"
    payload:
      - call_id
      - timestamp
      - duration_seconds
      - end_reason (completed, dropped, transferred)
    use_case: "Trigger transcript processing"
    
  call_analyzed:
    trigger: "Post-call transcript processed"
    payload:
      - call_id
      - transcript
      - custom_analysis_data (extracted JSON)
      - recording_url
      - duration_seconds
      - sentiment
    use_case: "Primary automation trigger"
    
  appointment_booked:
    trigger: "Calendar event created during call"
    payload:
      - call_id
      - appointment_datetime
      - calendar_event_id
      - attendees
    use_case: "Confirmation sequence trigger"
    
  transfer_initiated:
    trigger: "Call transferred to human"
    payload:
      - call_id
      - transfer_reason
      - context_summary
      - queue_name
    use_case: "Human notification"
```

### Webhook Handler Implementation

```python
# FASTAPI WEBHOOK HANDLER

from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from typing import Optional, List
import httpx

app = FastAPI()

class CallAnalyzedPayload(BaseModel):
    """Webhook payload for call_analyzed event."""
    
    call_id: str
    call_status: str
    transcript: str
    custom_analysis_data: dict
    recording_url: Optional[str]
    duration_seconds: int
    end_reason: Optional[str]

class WebhookRouter:
    """Route webhooks to appropriate handlers."""
    
    def __init__(self):
        self.n8n_url = "https://n8n.yourdomain.com/webhook"
        self.slack_webhook = "https://hooks.slack.com/services/..."
        
    async def route_call_analyzed(
        self,
        payload: CallAnalyzedPayload
    ):
        """
        Main routing logic for call_analyzed events.
        Implements M7 CONDUCTOR automation patterns.
        """
        data = payload.custom_analysis_data
        
        # Route based on extracted data
        if data.get("is_urgent"):
            await self.trigger_urgent_flow(payload)
            
        if data.get("appointment_confirmed"):
            await self.trigger_booking_flow(payload)
            
        # Always update CRM
        await self.update_crm(payload)
        
        # Always log to analytics
        await self.log_analytics(payload)
        
    async def trigger_urgent_flow(self, payload: CallAnalyzedPayload):
        """Immediate Slack alert for urgent issues."""
        async with httpx.AsyncClient() as client:
            await client.post(
                self.slack_webhook,
                json={
                    "text": f"🚨 URGENT CALL\n"
                            f"Caller: {payload.custom_analysis_data.get('caller_name')}\n"
                            f"Issue: {payload.custom_analysis_data.get('issue_type')}\n"
                            f"Phone: {payload.custom_analysis_data.get('caller_phone')}"
                }
            )
            
    async def trigger_booking_flow(self, payload: CallAnalyzedPayload):
        """Confirmation email and calendar sync."""
        async with httpx.AsyncClient() as client:
            await client.post(
                f"{self.n8n_url}/booking-confirmed",
                json={
                    "call_id": payload.call_id,
                    "caller": payload.custom_analysis_data.get("caller_name"),
                    "email": payload.custom_analysis_data.get("caller_email"),
                    "appointment": payload.custom_analysis_data.get("appointment_datetime"),
                    "summary": payload.custom_analysis_data.get("call_summary")
                }
            )

@app.post("/webhook/call-analyzed")
async def handle_call_analyzed(payload: CallAnalyzedPayload):
    """Primary webhook endpoint."""
    router = WebhookRouter()
    await router.route_call_analyzed(payload)
    return {"status": "processed", "call_id": payload.call_id}
```

---

## 3.3 N8N / MAKE WORKFLOW PATTERNS

### Master Routing Workflow

```yaml
N8N_WORKFLOW_PATTERN:

  name: "Voice Call Post-Processing Master"
  
  nodes:
    1_webhook_trigger:
      type: "Webhook"
      method: "POST"
      path: "/call-analyzed"
      
    2_event_filter:
      type: "IF"
      condition: "{{ $json.event === 'call_analyzed' }}"
      true: "→ Parse JSON"
      false: "→ End"
      
    3_parse_json:
      type: "Set"
      operation: "Extract custom_analysis_data"
      
    4_router:
      type: "Switch"
      branches:
        - condition: "is_urgent == true"
          output: "Urgent Flow"
        - condition: "appointment_confirmed == true"
          output: "Booking Flow"
        - condition: "next_action == 'nurture'"
          output: "Nurture Flow"
        - default: "Standard Flow"

  urgent_flow:
    nodes:
      - type: "Slack"
        action: "Send Message"
        channel: "#urgent-calls"
        message: "🚨 URGENT: {{ caller_name }} - {{ issue_type }}"
        
      - type: "Gmail"
        action: "Send Email"
        to: "{{ dispatch_email }}"
        subject: "URGENT: {{ issue_type }}"
        
  booking_flow:
    nodes:
      - type: "Google Calendar"
        action: "Create Event"
        summary: "Call with {{ caller_name }}"
        datetime: "{{ appointment_datetime }}"
        
      - type: "Gmail"
        action: "Send Email"
        to: "{{ caller_email }}"
        template: "booking_confirmation"
        
      - type: "CRM"
        action: "Update Deal Stage"
        stage: "Appointment Set"
        
  nurture_flow:
    nodes:
      - type: "CRM"
        action: "Add to Sequence"
        sequence: "post_call_nurture"
        
      - type: "Wait"
        duration: "48 hours"
        
      - type: "Gmail"
        action: "Send Follow-up"
        template: "value_add_followup"
```

### Visual Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    N8N POST-CALL WORKFLOW                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  [Webhook Trigger: POST /call-analyzed]                                      │
│                    │                                                         │
│                    ▼                                                         │
│  [Filter: event === 'call_analyzed']                                         │
│                    │                                                         │
│                    ▼                                                         │
│  [Parse JSON: Extract custom_analysis_data]                                  │
│                    │                                                         │
│                    ▼                                                         │
│  [Router / Switch Node]                                                      │
│         │         │         │         │                                      │
│         ▼         ▼         ▼         ▼                                      │
│    ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐                              │
│    │URGENT  │ │BOOKING │ │NURTURE │ │STANDARD│                              │
│    └────────┘ └────────┘ └────────┘ └────────┘                              │
│         │         │         │         │                                      │
│         ▼         ▼         ▼         ▼                                      │
│    [Slack]   [Calendar]  [Sequence] [CRM Log]                               │
│    [Email]   [Email]     [Wait 48h]                                         │
│              [CRM]       [Follow-up]                                        │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3.4 FOLLOW-UP SEQUENCE TRIGGERS

### Trigger Conditions

```yaml
FOLLOW_UP_TRIGGERS:

  positive_engagement:
    condition: "User responds positively to LinkedIn/Email"
    action: "Trigger voice call within 60-120 seconds"
    timing: "Illusion of human workflow timing"
    
  incomplete_booking:
    condition: "User dropped before scheduling"
    action: "Add to nurture + schedule follow-up call"
    timing: "24-48 hours"
    
  no_show:
    condition: "Appointment missed"
    action: "Trigger recovery sequence"
    timing: "1 hour after missed appointment"
    
  post_meeting:
    condition: "Meeting completed"
    action: "Trigger proposal/next steps sequence"
    timing: "Same day"
```

### Timing Implementation

```python
# FOLLOW-UP TIMING WITH HUMAN ILLUSION

import asyncio
from datetime import datetime, timedelta

class FollowUpOrchestrator:
    """
    M7 CONDUCTOR: Follow-up sequence timing.
    Creates illusion of human workflow.
    """
    
    async def trigger_speed_to_lead(
        self,
        lead_data: dict,
        response_type: str
    ):
        """
        Trigger voice call after positive text/email response.
        
        Timing: 60-120 second delay creates human illusion
        """
        
        # Random delay for natural feel
        delay_seconds = random.randint(60, 120)
        
        await asyncio.sleep(delay_seconds)
        
        # Trigger outbound voice call
        await self.initiate_outbound_call(
            phone=lead_data["phone"],
            prompt_payload={
                "lead_name": lead_data["name"],
                "company": lead_data["company"],
                "response_context": response_type,
                "personalization": lead_data.get("semantic_nuggets", [])
            }
        )
    
    async def initiate_outbound_call(
        self,
        phone: str,
        prompt_payload: dict
    ):
        """
        Initiate outbound call via Vapi/Retell API.
        Injects M6 scripts with dynamic variables.
        """
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://api.vapi.ai/call",
                headers={"Authorization": f"Bearer {VAPI_API_KEY}"},
                json={
                    "phoneNumber": phone,
                    "assistantId": ASSISTANT_ID,
                    "metadata": prompt_payload
                }
            )
            
            return response.json()
```

### Dynamic Variable Injection

```python
# OUTBOUND CALL PAYLOAD WITH M5/M6 DATA

def build_outbound_payload(
    lead: dict,
    m5_intel: dict,
    m6_scripts: dict
) -> dict:
    """
    Build outbound call payload with full personalization.
    Combines M5 intelligence with M6 scripts.
    """
    
    return {
        "phoneNumber": lead["phone"],
        "assistantId": ASSISTANT_ID,
        
        # M5 Intelligence injection
        "metadata": {
            "lead_name": lead["name"],
            "company": m5_intel["company_research"]["name"],
            "industry": m5_intel["company_research"]["industry"],
            "pain_point": m5_intel["pain_points"]["primary"],
            "semantic_nuggets": m5_intel.get("semantic_nuggets", []),
            "similar_client": m5_intel.get("case_study_match", {}).get("client"),
            "similar_result": m5_intel.get("case_study_match", {}).get("result"),
        },
        
        # M6 Script selection
        "firstMessage": m6_scripts["opener"].format(
            name=lead["name"],
            similar=m5_intel.get("case_study_match", {}).get("client", "a similar company"),
            result=m5_intel.get("case_study_match", {}).get("result", "great results")
        ),
        
        # Override default prompts with M6 value-drop
        "systemPrompt": m6_scripts["system_prompt"],
        
        # Tool definitions from M6
        "tools": m6_scripts["tools"]
    }
```

---

## 3.5 ESCALATION AUTOMATION

### Trigger to Human Queue

```yaml
ESCALATION_AUTOMATION:

  triggers:
    negative_sentiment:
      condition: "sentiment_score < 0.3 OR anger_detected"
      action: "HOT transfer to human queue"
      notification: "Slack alert to team"
      
    explicit_request:
      condition: "User says 'speak to a real person'"
      action: "IMMEDIATE transfer"
      notification: "None (seamless)"
      
    transfer_failure:
      condition: "call_transfer_failures >= 1"
      action: "Email/Slack alert to admin"
      priority: "Critical"
      
    compliance_block:
      condition: "Unauthenticated user requests PHI/sensitive data"
      action: "Route to authentication workflow"
      fallback: "Force escalation to human support"
```

### Human Notification Workflow

```python
# ESCALATION NOTIFICATION SYSTEM

class EscalationNotifier:
    """
    M7 CONDUCTOR: Human queue notification.
    """
    
    async def notify_escalation(
        self,
        call_id: str,
        reason: str,
        context: dict,
        priority: str = "normal"
    ):
        """
        Notify human agents of escalation.
        """
        
        # Build context summary
        summary = {
            "call_id": call_id,
            "caller": context.get("caller_name"),
            "phone": context.get("caller_phone"),
            "reason": reason,
            "sentiment": context.get("sentiment_score"),
            "conversation_summary": context.get("call_summary"),
            "transcript_link": f"https://dashboard.com/calls/{call_id}",
            "priority": priority
        }
        
        # Route based on priority
        if priority == "critical":
            await self._send_slack_urgent(summary)
            await self._send_sms_oncall(summary)
        elif priority == "high":
            await self._send_slack_urgent(summary)
        else:
            await self._send_slack_queue(summary)
            
    async def _send_slack_urgent(self, summary: dict):
        """Urgent Slack notification with @channel."""
        
        message = {
            "text": f"🚨 ESCALATION REQUIRED @channel",
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"*Caller:* {summary['caller']}\n"
                                f"*Reason:* {summary['reason']}\n"
                                f"*Summary:* {summary['conversation_summary']}"
                    }
                },
                {
                    "type": "actions",
                    "elements": [
                        {
                            "type": "button",
                            "text": {"type": "plain_text", "text": "Accept Call"},
                            "action_id": f"accept_{summary['call_id']}"
                        },
                        {
                            "type": "button",
                            "text": {"type": "plain_text", "text": "View Transcript"},
                            "url": summary["transcript_link"]
                        }
                    ]
                }
            ]
        }
        
        async with httpx.AsyncClient() as client:
            await client.post(SLACK_WEBHOOK_URGENT, json=message)
```

---

## 3.6 COMPLIANCE AUTOMATION (HIPAA/HEALTHCARE)

### PHI Handling Rules

```yaml
HIPAA_COMPLIANCE_AUTOMATION:

  infrastructure:
    - "BAAs executed with ALL vendors in stack"
    - "On-premises or HIPAA-compliant cloud only"
    - "Zero data retention on intermediary AI providers"
    - "Encryption at rest and in transit"
    
  redaction:
    automated: true
    fields_to_redact:
      - "Patient name"
      - "Date of birth"
      - "Medical ID numbers"
      - "SSN"
      - "Address"
    replacement: "[REDACTED]"
    timing: "Before transcript storage"
    
  authentication_gate:
    trigger: "Unauthenticated user requests PHI"
    action: "Block data access"
    workflow: "Route to OTP/KBA authentication"
    script: "I can't access account details until we verify you."
    
  audit_trail:
    every_action: true
    fields:
      - timestamp
      - user_id
      - action_type
      - data_accessed
      - outcome
    storage: "Immutable audit log"
    retention: "7 years minimum"
```

### Healthcare Post-Call Workflow

```yaml
HEALTHCARE_POST_CALL_WORKFLOW:

  name: "HIPAA-Compliant Call Processing"
  
  nodes:
    1_receive_webhook:
      type: "Webhook"
      path: "/healthcare/call-analyzed"
      
    2_redact_phi:
      type: "Code"
      action: "Apply PHI redaction to transcript"
      output: "redacted_transcript"
      
    3_authentication_check:
      type: "IF"
      condition: "caller.verified == true"
      true: "→ Full Processing"
      false: "→ Limited Processing"
      
    4_ehr_sync:
      type: "HTTP"
      method: "POST"
      url: "{{ ehr_api_endpoint }}"
      body: "appointment_data + verified_caller_context"
      note: "Direct-to-EHR with no intermediate storage"
      
    5_audit_log:
      type: "Database"
      action: "INSERT"
      table: "audit_trail"
      fields:
        - timestamp
        - call_id
        - action: "processed_healthcare_call"
        - outcome: "success/failure"
```

---

## PYDANTIC SCHEMAS

```python
from pydantic import BaseModel, Field
from typing import Optional, List, Literal
from datetime import datetime
from enum import Enum

class NextAction(str, Enum):
    FOLLOW_UP = "follow_up"
    TRANSFER = "transfer"
    CLOSE_WON = "close_won"
    CLOSE_LOST = "close_lost"
    NURTURE = "nurture"

class CallOutcome(BaseModel):
    """M7 Domain 3: Structured call extraction."""
    
    caller_name: str = Field(..., description="Full name")
    caller_phone: str = Field(..., description="Phone number")
    caller_email: Optional[str] = None
    service_address: Optional[str] = None
    issue_type: str = Field(..., description="Primary issue category")
    issue_details: Optional[str] = None
    is_urgent: bool = Field(default=False)
    qualification_score: int = Field(ge=1, le=10)
    appointment_confirmed: bool = Field(default=False)
    appointment_datetime: Optional[datetime] = None
    objections_raised: List[str] = Field(default_factory=list)
    next_action: NextAction
    call_summary: str = Field(..., max_length=500)
    sentiment_score: float = Field(ge=-1, le=1)
    custom_fields: dict = Field(default_factory=dict)

class WebhookEvent(BaseModel):
    """Webhook event structure."""
    
    event_type: Literal[
        "call_started",
        "call_ended", 
        "call_analyzed",
        "appointment_booked",
        "transfer_initiated"
    ]
    call_id: str
    timestamp: datetime
    payload: dict

class FollowUpTrigger(BaseModel):
    """Follow-up sequence trigger config."""
    
    trigger_type: str
    delay_seconds: int = Field(ge=0)
    action: str
    payload: dict
```

---

*M7 CONDUCTOR Domain 3 v1.0.0*
*Post-Call Automation — "Where conversations become operations"*

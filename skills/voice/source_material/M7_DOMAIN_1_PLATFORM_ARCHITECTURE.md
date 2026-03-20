# M7 CONDUCTOR — DOMAIN 1: PLATFORM ARCHITECTURE
## Voice System Runtime Configuration

**Version:** 1.0.0  
**Module:** M7 CONDUCTOR (The Execution)  
**Domain:** 1 of 6  
**Lines:** ~850  
**Source:** NotebookLM Voice Architecture Synthesis

---

## DOMAIN OVERVIEW

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    PLATFORM ARCHITECTURE SCOPE                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  THIS DOMAIN ANSWERS:                                                        │
│  • Which voice platform for which use case?                                 │
│  • How do I configure realtime streaming?                                   │
│  • When S2S vs Cascade architecture?                                        │
│  • How to handle interruptions properly?                                    │
│                                                                              │
│  RECEIVES FROM M6:                                                          │
│  • Call scripts and objection branches                                      │
│  • Voice configuration preferences                                          │
│  • Tool integration requirements                                            │
│                                                                              │
│  OUTPUTS TO RUNTIME:                                                        │
│  • Platform connection configs                                              │
│  • WebSocket/WebRTC setup                                                   │
│  • VAD and interruption parameters                                          │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 1.1 ARCHITECTURE DECISION MATRIX

### S2S vs Cascade: When to Use Which

```yaml
ARCHITECTURE_SELECTION:

  NATIVE_S2S:
    description: "Single multimodal model, audio-in → audio-out"
    
    providers:
      - "OpenAI Realtime API"
      - "Gemini 3 Audio / Gemini Live"
      - "Amazon Nova Sonic"
    
    latency: "~300ms (best case)"
    
    best_for:
      - "Raw speed priority"
      - "Natural conversation flow"
      - "Simple Q&A interactions"
      - "Demo/prototype builds"
    
    trade_offs:
      - "Black box reasoning"
      - "Limited tool calling control"
      - "Hard to enforce compliance"
      - "Difficult persona modulation"
    
    decision_rule: |
      IF priority == "speed" 
      AND complexity == "low"
      AND tool_calls == "minimal"
      THEN use_s2s()

  STREAMING_CASCADE:
    description: "STT → LLM → TTS with overlapped processing"
    
    providers:
      - "LiveKit Agents + custom models"
      - "Pipecat framework"
      - "Custom WebSocket orchestration"
    
    latency: "<500ms (optimized)"
    
    best_for:
      - "Production agents"
      - "Complex tool calling"
      - "Custom voice personas"
      - "Strict compliance requirements"
      - "Business logic control"
    
    trade_offs:
      - "Higher complexity"
      - "More infrastructure"
      - "Requires optimization work"
    
    decision_rule: |
      IF tool_calls == "complex"
      OR compliance == "strict"
      OR persona == "custom"
      THEN use_streaming_cascade()

  SEQUENTIAL_CASCADE:
    description: "Traditional STT → wait → LLM → wait → TTS"
    
    latency: "800-2000ms (unacceptable)"
    
    use_only_for:
      - "Async processing"
      - "Prototyping"
      - "Non-real-time analysis"
    
    decision_rule: |
      IF realtime == false
      THEN cascade_acceptable()
      ELSE avoid_sequential()
```

### Decision Flowchart

```
START: Voice Agent Deployment
         │
         ▼
┌────────────────────────┐
│ Tool Calling Required? │
└────────────────────────┘
         │
    ┌────┴────┐
    │         │
   YES       NO
    │         │
    ▼         ▼
┌────────┐  ┌────────────────────┐
│Cascade │  │ Latency < 400ms?   │
│Required│  └────────────────────┘
└────────┘           │
    │           ┌────┴────┐
    │          YES       NO
    │           │         │
    │           ▼         ▼
    │       ┌────────┐  ┌────────┐
    │       │  S2S   │  │Cascade │
    │       │  OK    │  │Required│
    │       └────────┘  └────────┘
    │
    ▼
┌────────────────────────┐
│ Compliance Strict?     │
└────────────────────────┘
         │
    ┌────┴────┐
   YES       NO
    │         │
    ▼         ▼
┌────────┐  ┌────────────────────┐
│Streaming│ │ Custom Persona?    │
│Cascade │  └────────────────────┘
└────────┘           │
                ┌────┴────┐
               YES       NO
                │         │
                ▼         ▼
            ┌────────┐  ┌────────┐
            │Cascade │  │S2S OK  │
            └────────┘  └────────┘
```

---

## 1.2 REALTIME API PATTERNS

### WebSocket Voice Streaming Setup

```python
# CONNECTION: Full-duplex persistent WebSocket
# PURPOSE: Continuous audio chunk transmission

import asyncio
import websockets
import json

class VoiceStreamClient:
    """
    WebSocket client for real-time voice streaming.
    Supports PCM, MP3, OGG, AAC audio formats.
    """
    
    def __init__(self, ws_url: str, audio_format: str = "pcm"):
        self.ws_url = ws_url
        self.audio_format = audio_format
        self.connection = None
        
    async def connect(self):
        """Establish persistent WebSocket connection."""
        self.connection = await websockets.connect(
            self.ws_url,
            ping_interval=20,
            ping_timeout=10
        )
        return self.connection
    
    async def stream_audio(self, audio_chunk: bytes):
        """
        Stream raw audio chunk to server.
        Format: PCM 16-bit, 16kHz mono (recommended)
        """
        if self.connection:
            await self.connection.send(audio_chunk)
    
    async def receive_response(self):
        """Receive synthesized audio response."""
        if self.connection:
            response = await self.connection.recv()
            return response
    
    async def send_interrupt_signal(self):
        """
        Send reset signal on user interruption.
        Halts TTS playback immediately.
        """
        interrupt_msg = json.dumps({
            "type": "interrupt",
            "action": "reset_decoder"
        })
        await self.connection.send(interrupt_msg)
```

### STT Streaming Snippet

```python
# REAL-TIME STT WITH STREAMING TRANSCRIPTION

import asyncio
from typing import AsyncGenerator

async def stream_stt(
    audio_generator: AsyncGenerator[bytes, None],
    ws_url: str,
    language: str = "en-US"
) -> AsyncGenerator[str, None]:
    """
    Stream audio to STT service, yield partial transcripts.
    
    Args:
        audio_generator: Async generator of audio chunks
        ws_url: STT WebSocket endpoint
        language: Target language code
    
    Yields:
        Partial transcripts as they arrive
    """
    async with websockets.connect(ws_url) as ws:
        # Send config
        config = {
            "type": "config",
            "language": language,
            "encoding": "LINEAR16",
            "sample_rate": 16000,
            "interim_results": True
        }
        await ws.send(json.dumps(config))
        
        # Stream audio chunks
        async def send_audio():
            async for chunk in audio_generator:
                await ws.send(chunk)
            # Send end signal
            await ws.send(json.dumps({"type": "end"}))
        
        # Receive transcripts
        async def receive_transcripts():
            async for message in ws:
                data = json.loads(message)
                if data.get("type") == "transcript":
                    yield data.get("text", "")
                    if data.get("is_final"):
                        break
        
        # Run both concurrently
        send_task = asyncio.create_task(send_audio())
        async for transcript in receive_transcripts():
            yield transcript
        await send_task
```

---

## 1.3 PLATFORM-SPECIFIC INTEGRATION

### LiveKit Configuration (WebRTC Transport)

```typescript
// LIVEKIT FRONTEND SETUP
// WebRTC-based, lowest latency option

import { 
  AgentSessionProvider, 
  TokenSource 
} from '@livekit/agents-react';

// Environment Variables Required:
// LIVEKIT_URL=wss://your-project.livekit.cloud
// LIVEKIT_API_KEY=your-api-key
// LIVEKIT_API_SECRET=your-api-secret

interface LiveKitConfig {
  url: string;
  token: string;
  roomName: string;
}

const VoiceAgentRoom: React.FC<LiveKitConfig> = ({ 
  url, 
  token, 
  roomName 
}) => {
  const tokenSource: TokenSource = async () => {
    // Fetch token from your backend
    const response = await fetch('/api/livekit-token', {
      method: 'POST',
      body: JSON.stringify({ roomName })
    });
    return response.json();
  };

  return (
    <AgentSessionProvider
      url={url}
      tokenSource={tokenSource}
      options={{
        audio: true,
        video: false,
        // VAD settings
        vadOptions: {
          silenceThreshold: 200,  // ms
          speechPadding: 50       // ms
        }
      }}
    >
      <VoiceAgentUI />
    </AgentSessionProvider>
  );
};
```

### LiveKit Backend Agent

```python
# LIVEKIT AGENT BACKEND
# Full voice agent with tool calling

from livekit.agents import (
    Agent,
    AgentSession,
    RoomEvent
)
from livekit.agents.voice import VoiceAgent
from livekit.agents.llm import LLMStream

class SalesVoiceAgent(Agent):
    """
    M7 CONDUCTOR: LiveKit deployment configuration.
    Receives scripts from M6 BRIDGE.
    """
    
    def __init__(self, m6_config: dict):
        super().__init__()
        self.scripts = m6_config["call_script"]
        self.tools = m6_config["tool_config"]
        
    async def on_session_started(self, session: AgentSession):
        """Initialize voice agent with M6 configuration."""
        
        # Configure STT
        stt_config = {
            "model": "nova-2",
            "language": "en-US",
            "punctuate": True,
            "interim_results": True
        }
        
        # Configure LLM with M6 scripts
        llm_config = {
            "model": "claude-sonnet-4-20250514",
            "system_prompt": self._build_system_prompt(),
            "temperature": 0.3,  # Low for determinism
            "tools": self._register_tools()
        }
        
        # Configure TTS
        tts_config = {
            "voice": "alloy",
            "speed": 1.0,
            "model": "tts-1-hd"
        }
        
        # Start voice agent
        self.voice_agent = VoiceAgent(
            stt=stt_config,
            llm=llm_config,
            tts=tts_config,
            vad_threshold=200,
            interruption_sensitivity=75
        )
        
        await self.voice_agent.start(session)
    
    def _build_system_prompt(self) -> str:
        """Inject M6 scripts into system prompt."""
        return f"""
You are a sales voice agent following the T.A.P. framework.

OPENER SCRIPT:
{self.scripts['opener']}

VALUE DROP SCRIPT:
{self.scripts['value_drop']}

OBJECTION HANDLING:
{self.scripts['objection_branches']}

RULES:
- Keep responses under 20 seconds spoken
- Use gift energy, not pitch energy
- If objections > 3, execute graceful exit
"""
    
    def _register_tools(self) -> list:
        """Register M6-defined tools."""
        return [
            {
                "name": "check_availability",
                "description": "Check calendar availability",
                "parameters": {...}
            },
            {
                "name": "book_appointment",
                "description": "Book meeting with lead",
                "parameters": {...}
            }
        ]
```

### Retell/Vapi Backend Routing

```python
# RETELL/VAPI WEBHOOK HANDLER
# Post-call data extraction via async webhooks

from fastapi import FastAPI, Request
from pydantic import BaseModel
import httpx

app = FastAPI()

class CallAnalyzedPayload(BaseModel):
    """Retell/Vapi call_analyzed webhook schema."""
    call_id: str
    call_status: str
    transcript: str
    custom_analysis_data: dict
    recording_url: str
    duration_seconds: int

@app.post("/webhook/call-analyzed")
async def handle_call_analyzed(payload: CallAnalyzedPayload):
    """
    Handle post-call webhook from Retell/Vapi.
    Routes to n8n/Make for automation.
    
    Webhook Events:
    - call_started: Initiates live session logging
    - call_ended: Call hangup detected
    - call_analyzed: Transcript processed, ready for routing
    """
    
    # Extract M6-defined variables
    extracted_data = {
        "caller_name": payload.custom_analysis_data.get("caller_name"),
        "caller_phone": payload.custom_analysis_data.get("caller_phone"),
        "service_address": payload.custom_analysis_data.get("service_address"),
        "issue_type": payload.custom_analysis_data.get("issue_type"),
        "is_urgent": payload.custom_analysis_data.get("is_urgent", False),
        "appointment_confirmed": payload.custom_analysis_data.get(
            "appointment_confirmed", False
        ),
        "call_summary": payload.custom_analysis_data.get("call_summary")
    }
    
    # Route to n8n production webhook
    async with httpx.AsyncClient() as client:
        await client.post(
            "https://n8n.yourdomain.com/webhook/call-analyzed",
            json={
                "event": "call_analyzed",
                "call_id": payload.call_id,
                "data": extracted_data,
                "transcript": payload.transcript,
                "duration": payload.duration_seconds
            }
        )
    
    return {"status": "processed"}
```

---

## 1.4 PROVIDER CAPABILITIES MATRIX

### Comparison Table

| Provider | Latency | Complexity | Control | Cost | Best For |
|----------|---------|------------|---------|------|----------|
| **Speechify SIMBA 3.0** | <250ms | Low | Medium | $10/1M chars | Speed-critical apps |
| **ElevenLabs** | 300-500ms | Low | High | $15-30/1M chars | Voice customization |
| **Cartesia** | <300ms | Medium | Medium | Variable | Low-latency streaming |
| **Vapi** | 500-1200ms | Low | Low | Per-minute | Quick deployments |
| **Retell** | 500-1200ms | Low | Medium | Per-minute | Easy webhooks |
| **LiveKit** | <500ms | High | Full | Infrastructure | Enterprise control |
| **Pipecat** | <400ms | High | Full | Self-hosted | Complete ownership |

### Selection Decision Tree

```yaml
PROVIDER_SELECTION:

  quick_launch:
    priority: "Time to market"
    choose: "Vapi OR Retell"
    rationale: "Lowest setup complexity, managed infrastructure"
    
  speed_critical:
    priority: "Sub-300ms latency"
    choose: "Speechify SIMBA OR Cartesia"
    rationale: "Optimized streaming pipelines"
    
  voice_branding:
    priority: "Custom voice persona"
    choose: "ElevenLabs"
    rationale: "Best voice cloning and customization"
    
  enterprise_control:
    priority: "Full infrastructure ownership"
    choose: "LiveKit OR Pipecat"
    rationale: "Complete control over every component"
    
  cost_optimization:
    priority: "High volume, low cost"
    choose: "Speechify ($10/1M) OR Self-hosted"
    rationale: "Best unit economics at scale"
```

---

## 1.5 INTERRUPTION HANDLING

### VAD Configuration Parameters

```yaml
VAD_CONFIGURATION:

  model_delegation:
    description: "Run VAD on CPU to dedicate GPU to STT/LLM"
    recommended_model: "Pipecat Smart Turn"
    cpu_allocation: "Dedicated thread"
    
  pause_detection:
    silence_threshold_ms: 200
    description: "Trigger turn detection after 200ms non-speech"
    
  padding_hack:
    synthetic_silence_ms: 120
    description: |
      Append 120ms synthetic silence to force immediate 
      ASR finalization upon interruption detection.
    total_finalization: "200ms user silence + 120ms padding = 320ms"

  sensitivity_tuning:
    platform: "Retell/Vapi"
    recommended_range: "70-80"
    avoid: "100 (too brittle, stops for background noise)"
    
  thresholds:
    conservative: 60   # Fewer interruptions, more latency
    balanced: 75       # Recommended default
    aggressive: 85     # Quick interruption, may be brittle
    brittle: 100       # Avoid: stops for single words
```

### Barge-In Behavior Implementation

```python
# INTERRUPTION HANDLING LOGIC

class InterruptionHandler:
    """
    Handle user interruptions during TTS playback.
    Implements M7 CONDUCTOR interruption protocol.
    """
    
    def __init__(self, sensitivity: int = 75):
        self.sensitivity = sensitivity
        self.is_speaking = False
        self.speech_buffer = []
        
    async def on_vad_speech_detected(
        self,
        audio_chunk: bytes,
        ws_connection,
        tts_player
    ):
        """
        Handle detected speech during agent TTS.
        
        Execution Logic:
        1. Send reset signal to streaming decoder
        2. Halt TTS audio playback immediately
        3. Prioritize new user speech for STT
        4. Flag interruption for LLM context
        """
        
        if self.is_speaking:
            # 1. Reset streaming decoder
            await ws_connection.send(json.dumps({
                "type": "interrupt",
                "action": "reset_decoder",
                "timestamp": time.time()
            }))
            
            # 2. Halt TTS immediately
            await tts_player.stop()
            self.is_speaking = False
            
            # 3. Buffer user speech for STT priority
            self.speech_buffer.append(audio_chunk)
            
            # 4. Create interruption context flag
            return {
                "interrupted": True,
                "context_flag": "USER_INTERRUPTED_AGENT",
                "partial_response": tts_player.get_spoken_text()
            }
        
        return {"interrupted": False}
    
    def get_llm_context_injection(self) -> str:
        """
        Inject interruption awareness into LLM prompt.
        Helps agent adjust response style.
        """
        return """
[SYSTEM: User interrupted your previous response. 
They may want to:
- Ask a question
- Change topic
- Provide information
- Express disagreement

Acknowledge briefly and address their input.]
"""
```

### Sensitivity Calibration

```yaml
INTERRUPTION_SENSITIVITY_GUIDE:

  too_low (50-60):
    behavior: "Agent ignores most interruptions"
    symptom: "User has to repeat themselves"
    use_case: "Formal announcements, one-way info"
    
  balanced (70-80):
    behavior: "Agent responds to clear interruptions"
    symptom: "Natural conversation flow"
    use_case: "Most voice agents (RECOMMENDED)"
    
  too_high (90-100):
    behavior: "Agent stops at any sound"
    symptom: "Stops for coughs, background noise, 'uh-huh'"
    use_case: "Never (creates choppy experience)"

  calibration_process:
    1. "Start at sensitivity = 75"
    2. "Test with 10 real calls"
    3. "Count false positives (stopped for noise)"
    4. "Count false negatives (ignored valid interruption)"
    5. "Adjust ±5 based on ratio"
    6. "Target: <5% false positives, <10% false negatives"
```

---

## 1.6 AUDIO CODEC CONFIGURATION

### Supported Formats

```yaml
AUDIO_CODECS:

  pcm_16bit:
    format: "Linear PCM"
    sample_rate: 16000
    bit_depth: 16
    channels: 1 (mono)
    use_case: "Lowest latency, raw audio"
    bandwidth: "256 kbps"
    
  opus:
    format: "Opus"
    sample_rate: 48000
    bitrate: "24-64 kbps"
    use_case: "WebRTC default, good compression"
    latency_add: "~10ms"
    
  mp3:
    format: "MP3"
    sample_rate: 44100
    bitrate: "64-128 kbps"
    use_case: "Recording storage"
    latency_add: "~50ms (encoding buffer)"
    
  aac:
    format: "AAC-LC"
    sample_rate: 44100
    bitrate: "64-128 kbps"
    use_case: "iOS/Safari compatibility"
    latency_add: "~30ms"

RECOMMENDATION:
  live_streaming: "PCM 16-bit @ 16kHz (no encoding overhead)"
  webrtc: "Opus @ 48kHz (built-in, excellent)"
  recording: "MP3 @ 44.1kHz (storage efficiency)"
  telephony: "μ-law/A-law @ 8kHz (SIP compatibility)"
```

---

## 1.7 DEPLOYMENT CHECKLIST

### Pre-Launch Verification

```yaml
DEPLOYMENT_CHECKLIST:

  infrastructure:
    - [ ] WebSocket/WebRTC endpoints configured
    - [ ] SSL certificates valid
    - [ ] Load balancer health checks passing
    - [ ] Auto-scaling policies set
    
  voice_pipeline:
    - [ ] STT model selected and tested
    - [ ] LLM endpoint responding <50ms TTFT
    - [ ] TTS voice configured
    - [ ] VAD sensitivity calibrated (70-80)
    
  m6_integration:
    - [ ] Scripts imported from M6 BRIDGE
    - [ ] Objection branches mapped
    - [ ] Guardian 8D thresholds set
    - [ ] Escalation triggers configured
    
  monitoring:
    - [ ] Latency logging enabled
    - [ ] Transcript storage configured
    - [ ] Error alerting active
    - [ ] Cost tracking dashboard
    
  compliance:
    - [ ] Disclosure statement configured
    - [ ] Human fallback tested
    - [ ] Recording consent flow
    - [ ] Data retention policy applied
```

---

## PYDANTIC SCHEMAS

```python
from pydantic import BaseModel, Field
from typing import Optional, Literal
from enum import Enum

class ArchitectureType(str, Enum):
    S2S = "speech_to_speech"
    STREAMING_CASCADE = "streaming_cascade"
    SEQUENTIAL_CASCADE = "sequential_cascade"

class AudioCodec(str, Enum):
    PCM = "pcm_16bit"
    OPUS = "opus"
    MP3 = "mp3"
    AAC = "aac"

class PlatformConfig(BaseModel):
    """M7 Domain 1: Platform configuration schema."""
    
    architecture: ArchitectureType = Field(
        default=ArchitectureType.STREAMING_CASCADE,
        description="Voice processing architecture"
    )
    
    provider: str = Field(
        ...,
        description="Voice platform provider"
    )
    
    ws_url: Optional[str] = Field(
        None,
        description="WebSocket endpoint URL"
    )
    
    audio_codec: AudioCodec = Field(
        default=AudioCodec.PCM,
        description="Audio encoding format"
    )
    
    sample_rate: int = Field(
        default=16000,
        description="Audio sample rate in Hz"
    )
    
    vad_sensitivity: int = Field(
        default=75,
        ge=50,
        le=100,
        description="VAD interruption sensitivity (70-80 recommended)"
    )
    
    silence_threshold_ms: int = Field(
        default=200,
        description="Milliseconds of silence to trigger turn end"
    )
    
    synthetic_padding_ms: int = Field(
        default=120,
        description="Synthetic silence for ASR finalization"
    )

class InterruptionConfig(BaseModel):
    """Interruption handling configuration."""
    
    enabled: bool = True
    sensitivity: int = Field(default=75, ge=50, le=100)
    halt_tts_immediately: bool = True
    inject_context_flag: bool = True
    max_false_positive_rate: float = Field(default=0.05)
    max_false_negative_rate: float = Field(default=0.10)
```

---

*M7 CONDUCTOR Domain 1 v1.0.0*
*Platform Architecture — "Where voice becomes infrastructure"*

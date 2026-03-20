# M7 CONDUCTOR — DOMAIN 2: LATENCY ENGINEERING
## Sub-500ms Voice System Optimization

**Version:** 1.0.0  
**Module:** M7 CONDUCTOR (The Execution)  
**Domain:** 2 of 6  
**Lines:** ~750  
**Source:** NotebookLM Voice Architecture Synthesis

---

## DOMAIN OVERVIEW

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      LATENCY ENGINEERING SCOPE                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  "The caller hears latency before they hear intelligence."                  │
│                                                                              │
│  THIS DOMAIN ANSWERS:                                                        │
│  • What's the latency budget for each component?                            │
│  • How do I optimize RAG for voice?                                         │
│  • Which database for sub-500ms retrieval?                                  │
│  • How to measure and monitor latency?                                      │
│                                                                              │
│  CRITICAL INSIGHT:                                                          │
│  Users notice delays above ~500-800ms in voice conversation.                │
│  Every 100ms matters for perceived naturalness.                             │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2.1 LATENCY BUDGETS & THRESHOLDS

### End-to-End (E2E) Total Budget

```yaml
LATENCY_THRESHOLDS:

  human_like:
    target: "<400ms"
    perception: "Feels like talking to a person"
    achievable_with: "S2S or highly optimized cascade"
    
  conversational:
    target: "<500ms"
    perception: "Natural, responsive"
    achievable_with: "Well-tuned streaming cascade"
    
  tolerable:
    target: "500ms - 1000ms"
    perception: "Noticeable but acceptable"
    achievable_with: "Standard cascade, cloud RAG"
    
  unacceptable:
    target: ">1000ms"
    perception: "Awkward silence, robotic"
    cause: "Sequential cascade, slow RAG, cold starts"
    action: "MUST OPTIMIZE"
```

### Component Breakdown (Target: <500ms E2E)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    LATENCY BUDGET BREAKDOWN                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  COMPONENT          │ TARGET      │ NOTES                                   │
│  ───────────────────┼─────────────┼─────────────────────────────────────    │
│  VAD (Turn Detect)  │ 200ms       │ Silence threshold                       │
│  + Padding          │ +120ms      │ Synthetic silence for finalization      │
│  ───────────────────┼─────────────┼─────────────────────────────────────    │
│  STT (Transcription)│ 25-150ms    │ Depends on model and load               │
│  ───────────────────┼─────────────┼─────────────────────────────────────    │
│  RAG (Retrieval)    │ <350ms      │ CRITICAL: Often the bottleneck          │
│  ───────────────────┼─────────────┼─────────────────────────────────────    │
│  LLM (Inference)    │             │                                         │
│    • TTFT           │ 30-40ms     │ With prefix + KV caching                │
│    • ITL            │ 2-5ms/token │ Inter-token latency                     │
│  ───────────────────┼─────────────┼─────────────────────────────────────    │
│  TTS (Synthesis)    │             │                                         │
│    • TTFB           │ 40-60ms     │ Chunked decoding                        │
│  ───────────────────┼─────────────┼─────────────────────────────────────    │
│  Network Transit    │ 50-200ms    │ Geographic + protocol overhead          │
│  ───────────────────┼─────────────┼─────────────────────────────────────    │
│  TOTAL TARGET       │ <500ms      │ Server-side measurement                 │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘

NOTE: Client-side latency typically ~250ms higher due to:
  • OS audio processing
  • Encoding overhead
  • Telephony/SIP transport (+300-600ms for PSTN)
```

### STT Latency Options

```yaml
STT_LATENCY_BENCHMARKS:

  ultra_fast:
    model: "Nemotron Speech ASR"
    latency: "<25ms"
    context_window: "160ms"
    use_case: "Speed-critical, local deployment"
    
  fast:
    model: "Deepgram Nova-2"
    latency: "50-100ms"
    mode: "Streaming"
    use_case: "Production streaming"
    
  standard:
    model: "Whisper (batched)"
    latency: "90-150ms"
    note: "Under load with 25+ concurrent streams per GPU"
    use_case: "Cost-optimized batch processing"
    
  slow:
    model: "Whisper (sync)"
    latency: "500ms+"
    use_case: "Post-call transcription only"
```

### LLM Latency Optimization

```yaml
LLM_LATENCY_OPTIMIZATION:

  prefix_caching:
    description: "Cache system prompt + few-shot examples"
    ttft_improvement: "50-70% reduction"
    implementation: "Set cache_control on static prompt sections"
    
  kv_caching:
    description: "Reuse key-value attention across turns"
    ttft_improvement: "30-40ms achievable"
    requirement: "Same conversation context"
    
  speculative_decoding:
    description: "Use small model to predict tokens"
    itl_improvement: "2-3x faster"
    implementation: "Model-specific, requires tuning"
    
  streaming_overlap:
    description: "Start TTS before LLM completes"
    benefit: "Hides LLM latency"
    trigger: "Start TTS after ~28 tokens accumulated"

LLM_LATENCY_TARGETS:
  ttft: "30-40ms"
  itl: "2-5ms per token"
  first_sentence: "<200ms"
```

### TTS Latency Optimization

```yaml
TTS_LATENCY_OPTIMIZATION:

  sentence_aware_chunking:
    description: "Don't wait for full response"
    implementation: |
      1. Accumulate ~28 tokens from LLM
      2. Detect sentence boundary
      3. Send chunk to TTS
      4. Stream audio while generating next chunk
    ttfb: "40-60ms (down from ~150ms)"
    
  slice_decoding:
    description: "Decode audio in small frames"
    frame_size: "~3 frames at a time"
    benefit: "Continuous audio stream"
    
  voice_caching:
    description: "Pre-cache common phrases"
    examples:
      - "Thank you for calling"
      - "Let me check that for you"
      - "One moment please"
    latency: "Near-zero for cached phrases"

TTS_LATENCY_TARGETS:
  ttfb: "<60ms"
  continuous_stream: "No gaps between sentences"
```

---

## 2.2 RAG OPTIMIZATION FOR VOICE

### The RAG Bottleneck

```yaml
RAG_LATENCY_REALITY:

  warning: |
    RAG is often the dominant latency bottleneck in voice systems.
    A database that's "fine for chat" may be unusable for live voice.
    
  total_query_breakdown:
    embedding_generation: "~300ms (major contributor)"
    index_search: "<1ms (local) to 1700ms (cloud PG)"
    result_processing: "~10-20ms"
    
  critical_insight: |
    Embedding latency dominates when search is local.
    Cloud databases add network + search overhead.
```

### Configuration Parameters

```yaml
VOICE_RAG_CONFIGURATION:

  vector_limits:
    max_vectors: 100000
    rationale: "Beyond this, local search degrades"
    
  retrieval_settings:
    top_k: 3
    rationale: |
      Balance context density vs LLM TTFT.
      More chunks = more context = slower inference.
      3 chunks typically sufficient for voice.
    
  similarity_thresholds:
    excellent: ">0.8"
    good: "0.6 - 0.8"
    poor: "<0.6"
    action_on_poor: "Trigger fallback script"
    
  chunk_sizing:
    voice_optimized: "256-512 tokens"
    rationale: "Smaller chunks = faster retrieval + focused context"
    avoid: "1000+ token chunks (bloat LLM context)"
```

### Embedding Latency Reduction

```python
# EMBEDDING OPTIMIZATION STRATEGIES

from functools import lru_cache
import hashlib
import numpy as np

class VoiceRAGOptimizer:
    """
    Optimized RAG for sub-350ms voice retrieval.
    """
    
    def __init__(
        self,
        embedding_model: str = "text-embedding-3-small",
        cache_size: int = 1000
    ):
        self.embedding_model = embedding_model
        self.cache_size = cache_size
        self.embedding_cache = {}
        
    def get_cache_key(self, text: str) -> str:
        """Generate deterministic cache key."""
        return hashlib.md5(text.encode()).hexdigest()
    
    async def get_embedding_cached(self, text: str) -> np.ndarray:
        """
        Get embedding with caching.
        
        Cache hit: ~0ms (vs ~300ms generation)
        """
        cache_key = self.get_cache_key(text)
        
        if cache_key in self.embedding_cache:
            return self.embedding_cache[cache_key]
        
        # Generate embedding (~300ms)
        embedding = await self._generate_embedding(text)
        
        # Cache for future queries
        self.embedding_cache[cache_key] = embedding
        
        # Evict oldest if over size
        if len(self.embedding_cache) > self.cache_size:
            oldest_key = next(iter(self.embedding_cache))
            del self.embedding_cache[oldest_key]
        
        return embedding
    
    def precompute_common_queries(self, common_queries: list):
        """
        Pre-cache embeddings for frequent queries.
        Run at startup to eliminate embedding latency.
        """
        for query in common_queries:
            cache_key = self.get_cache_key(query)
            # Warm cache synchronously at startup
            self.embedding_cache[cache_key] = self._generate_embedding_sync(query)
        
        print(f"Pre-cached {len(common_queries)} common queries")
```

### Search Pipeline Optimization

```python
# LOCAL FAISS CONFIGURATION FOR VOICE

import faiss
import numpy as np

class VoiceFAISS:
    """
    FAISS configuration optimized for voice latency.
    Target: <1ms search time.
    """
    
    def __init__(
        self,
        dimension: int = 1536,  # OpenAI embedding dim
        max_vectors: int = 100000
    ):
        self.dimension = dimension
        
        # Use IVF for faster search on larger datasets
        if max_vectors > 10000:
            # IVF with 100 clusters
            quantizer = faiss.IndexFlatL2(dimension)
            self.index = faiss.IndexIVFFlat(
                quantizer, 
                dimension, 
                100,  # nlist (clusters)
                faiss.METRIC_L2
            )
            self.index.nprobe = 10  # Search 10 clusters
        else:
            # Flat index for small datasets (fastest)
            self.index = faiss.IndexFlatL2(dimension)
    
    def search(
        self, 
        query_embedding: np.ndarray, 
        top_k: int = 3
    ) -> tuple:
        """
        Search with voice-optimized parameters.
        
        Returns: (distances, indices)
        Latency: ~0.3ms for <100k vectors
        """
        query = query_embedding.reshape(1, -1).astype('float32')
        distances, indices = self.index.search(query, top_k)
        return distances[0], indices[0]

# Benchmark results:
# Local FAISS: ~0.3ms search
# Total query (embed + search): ~340-350ms
```

---

## 2.3 DATABASE SELECTION

### Voice RAG Provider Benchmarks

```yaml
DATABASE_LATENCY_BENCHMARKS:

  local_faiss:
    total_query_latency: "340-350ms"
    search_latency: "~0.3ms"
    embedding_latency: "~300ms"
    network_latency: "0ms"
    verdict: "BEST for voice"
    max_scale: "<100k vectors"
    
  pinecone_serverless:
    total_query_latency: "~450ms"
    search_latency: "~150ms"
    verdict: "ACCEPTABLE for voice"
    note: "Fastest cloud option"
    
  qdrant_cloud:
    total_query_latency: "800-900ms"
    verdict: "DEGRADES naturalness"
    use_case: "Chat only, not voice"
    
  supabase_pgvector:
    total_query_latency: "1700ms+"
    search_latency: "~1700ms"
    verdict: "UNACCEPTABLE for voice"
    note: "Search alone exceeds total budget"
    use_case: "Async text chat only"
```

### Database Selection Decision Tree

```python
def select_voice_database(
    vector_count: int,
    latency_priority: str,
    multi_tenant: bool,
    infrastructure_control: str
) -> str:
    """
    M7 CONDUCTOR: Database selection for voice RAG.
    
    Returns recommended database provider.
    """
    
    # Rule 1: Small dataset + latency critical
    if vector_count < 100000 and latency_priority == "critical":
        return "LOCAL_FAISS"
        # Rationale: Fastest, no network dependency
    
    # Rule 2: Large dataset or multi-tenant
    if vector_count > 100000 or multi_tenant:
        return "PINECONE"
        # Rationale: Scalable, acceptable latency
    
    # Rule 3: Full control required
    if infrastructure_control == "full":
        return "LOCAL_FAISS"
        # Rationale: No external dependencies
    
    # Rule 4: ABORT conditions
    if latency_priority == "critical":
        # Never use these for voice
        blocked = ["SUPABASE", "PGVECTOR", "QDRANT_CLOUD"]
        return f"AVOID: {blocked}"
    
    # Default
    return "LOCAL_FAISS"

# Decision matrix summary:
DECISION_MATRIX = """
┌────────────────────────────────────────────────────────────────┐
│ IF dataset < 100k vectors AND priority == "latency"           │
│   → DEPLOY Local FAISS / In-memory store                      │
│                                                                │
│ IF dataset > 100k vectors OR multi-tenant scaling required    │
│   → DEPLOY Pinecone                                           │
│                                                                │
│ IF database == "PG Vector / Supabase"                         │
│   → ABORT voice RAG deployment                                │
│   → Use only for async text chat                              │
└────────────────────────────────────────────────────────────────┘
"""
```

---

## 2.4 FAILURE MODE HANDLING

### Timeout & Fallback Configuration

```yaml
FAILURE_HANDLING:

  timeout_triggers:
    rag_timeout:
      threshold_ms: 500
      action: "terminate_search()"
      fallback: "Use cached response or skip RAG"
      
    llm_timeout:
      threshold_ms: 2000
      action: "abort_generation()"
      fallback: "Use templated response"
      
    tts_timeout:
      threshold_ms: 1000
      action: "skip_audio()"
      fallback: "Text fallback if supported"

  low_confidence_triggers:
    similarity_threshold:
      threshold: 0.6
      condition: "max_similarity_score < 0.6"
      action: "execute_fallback()"
      
  fallback_scripts:
    no_rag_match: |
      "I don't have that exact information in front of me. 
       Let me connect you to a specialist who can help."
       
    llm_timeout: |
      "One moment while I look that up for you."
      
    general_error: |
      "I'm having a bit of trouble with that. 
       Would you mind if I transfer you to someone who can help?"
```

### Graceful Degradation Pattern

```python
# VOICE RAG WITH GRACEFUL DEGRADATION

import asyncio
from typing import Optional

class VoiceRAGWithFallback:
    """
    RAG with sub-500ms timeout and graceful fallback.
    """
    
    def __init__(
        self,
        rag_timeout_ms: int = 500,
        min_similarity: float = 0.6
    ):
        self.rag_timeout_ms = rag_timeout_ms
        self.min_similarity = min_similarity
        self.fallback_responses = {
            "timeout": "I don't have that exact clause in front of me, "
                       "let me connect you to a specialist.",
            "low_confidence": "I want to make sure I give you accurate info. "
                              "Let me transfer you to someone who can help.",
            "error": "I'm having trouble accessing that information. "
                     "Would you like me to connect you with a team member?"
        }
    
    async def query_with_fallback(
        self,
        query: str,
        context: dict
    ) -> dict:
        """
        Execute RAG query with timeout and fallback.
        
        Returns:
            {
                "success": bool,
                "response": str,
                "source": "rag" | "fallback",
                "latency_ms": int
            }
        """
        start_time = asyncio.get_event_loop().time()
        
        try:
            # Execute RAG with timeout
            result = await asyncio.wait_for(
                self._execute_rag(query),
                timeout=self.rag_timeout_ms / 1000
            )
            
            latency = (asyncio.get_event_loop().time() - start_time) * 1000
            
            # Check confidence
            if result["max_similarity"] < self.min_similarity:
                return {
                    "success": False,
                    "response": self.fallback_responses["low_confidence"],
                    "source": "fallback",
                    "latency_ms": latency,
                    "reason": "low_confidence"
                }
            
            return {
                "success": True,
                "response": result["answer"],
                "source": "rag",
                "latency_ms": latency,
                "chunks_used": result["chunks"]
            }
            
        except asyncio.TimeoutError:
            latency = (asyncio.get_event_loop().time() - start_time) * 1000
            return {
                "success": False,
                "response": self.fallback_responses["timeout"],
                "source": "fallback",
                "latency_ms": latency,
                "reason": "timeout"
            }
            
        except Exception as e:
            return {
                "success": False,
                "response": self.fallback_responses["error"],
                "source": "fallback",
                "reason": str(e)
            }
```

---

## 2.5 MEASUREMENT & MONITORING

### Server-Side Logging

```python
# LATENCY MEASUREMENT PROTOCOL

import time
import logging
from dataclasses import dataclass
from typing import Optional

@dataclass
class LatencyMetrics:
    """Voice pipeline latency measurements."""
    
    vad_ms: float = 0.0
    stt_ms: float = 0.0
    rag_ms: float = 0.0
    llm_ttft_ms: float = 0.0
    llm_total_ms: float = 0.0
    tts_ttfb_ms: float = 0.0
    tts_total_ms: float = 0.0
    network_ms: float = 0.0
    
    @property
    def server_total_ms(self) -> float:
        """Total server-side latency."""
        return (
            self.stt_ms + 
            self.rag_ms + 
            self.llm_ttft_ms + 
            self.tts_ttfb_ms
        )
    
    @property
    def estimated_client_ms(self) -> float:
        """Estimated client-perceived latency."""
        # Client typically +250ms due to OS audio processing
        return self.server_total_ms + 250
    
    def is_acceptable(self) -> bool:
        """Check if latency meets voice threshold."""
        return self.server_total_ms < 500
    
    def get_bottleneck(self) -> str:
        """Identify the slowest component."""
        components = {
            "stt": self.stt_ms,
            "rag": self.rag_ms,
            "llm": self.llm_ttft_ms,
            "tts": self.tts_ttfb_ms
        }
        return max(components, key=components.get)

class LatencyLogger:
    """Log latency metrics for analysis."""
    
    def __init__(self):
        self.logger = logging.getLogger("voice_latency")
        
    def log_turn(self, metrics: LatencyMetrics, call_id: str):
        """Log single conversation turn metrics."""
        self.logger.info(
            f"LATENCY call={call_id} "
            f"server={metrics.server_total_ms:.1f}ms "
            f"stt={metrics.stt_ms:.1f}ms "
            f"rag={metrics.rag_ms:.1f}ms "
            f"llm={metrics.llm_ttft_ms:.1f}ms "
            f"tts={metrics.tts_ttfb_ms:.1f}ms "
            f"bottleneck={metrics.get_bottleneck()} "
            f"acceptable={metrics.is_acceptable()}"
        )
```

### Client-Side Measurement

```yaml
CLIENT_SIDE_MEASUREMENT:

  method: "Audio waveform analysis"
  
  steps:
    1. "Record raw call audio"
    2. "Load in audio editor (Audacity, etc.)"
    3. "Find end of user speech waveform"
    4. "Find start of agent speech waveform"
    5. "Measure gap in milliseconds"
    
  expected_delta: |
    Client-side latency typically ~250ms higher than server-side
    due to:
    - OS audio processing
    - Encoding/decoding
    - Network transport
    
  telephony_overhead:
    sip_pstn: "+300-600ms"
    webrtc: "+50-100ms"
    
  target_client_perceived:
    excellent: "<500ms"
    acceptable: "<750ms"
    poor: ">1000ms"
```

---

## 2.6 OPTIMIZATION PLAYBOOK

### Quick Wins (Implement First)

```yaml
OPTIMIZATION_QUICK_WINS:

  1_embedding_caching:
    impact: "300ms → 0ms for repeated queries"
    effort: "Low"
    implementation: "LRU cache on embedding function"
    
  2_local_vector_store:
    impact: "1700ms → 350ms total RAG"
    effort: "Medium"
    implementation: "Replace cloud DB with local FAISS"
    
  3_llm_prefix_caching:
    impact: "TTFT 100ms → 40ms"
    effort: "Low"
    implementation: "Cache system prompt tokens"
    
  4_tts_chunking:
    impact: "TTFB 150ms → 60ms"
    effort: "Medium"
    implementation: "Stream after 28 tokens"
    
  5_vad_tuning:
    impact: "Reduce false finalization"
    effort: "Low"
    implementation: "Set silence threshold to 200ms"
```

### Advanced Optimizations

```yaml
ADVANCED_OPTIMIZATIONS:

  speculative_decoding:
    description: "Use small model to predict tokens"
    impact: "2-3x faster ITL"
    complexity: "High"
    
  voice_caching:
    description: "Pre-generate common phrases"
    impact: "Near-zero TTS for cached"
    complexity: "Medium"
    
  edge_deployment:
    description: "Run inference at edge locations"
    impact: "Reduce network latency 50-150ms"
    complexity: "High"
    
  model_distillation:
    description: "Use smaller fine-tuned model"
    impact: "Faster inference, same quality"
    complexity: "Very High"
```

---

## PYDANTIC SCHEMAS

```python
from pydantic import BaseModel, Field
from typing import Optional, Literal

class LatencyBudget(BaseModel):
    """M7 Domain 2: Latency budget configuration."""
    
    target_e2e_ms: int = Field(
        default=500,
        description="End-to-end latency target"
    )
    
    vad_threshold_ms: int = Field(
        default=200,
        description="VAD silence detection threshold"
    )
    
    stt_budget_ms: int = Field(
        default=100,
        description="STT latency budget"
    )
    
    rag_budget_ms: int = Field(
        default=350,
        description="RAG retrieval budget"
    )
    
    rag_timeout_ms: int = Field(
        default=500,
        description="RAG timeout before fallback"
    )
    
    llm_ttft_budget_ms: int = Field(
        default=50,
        description="LLM time to first token budget"
    )
    
    tts_ttfb_budget_ms: int = Field(
        default=60,
        description="TTS time to first byte budget"
    )

class RAGConfig(BaseModel):
    """Voice RAG configuration."""
    
    database: Literal["faiss", "pinecone", "qdrant", "supabase"] = Field(
        default="faiss",
        description="Vector database provider"
    )
    
    max_vectors: int = Field(
        default=100000,
        description="Maximum vectors for local store"
    )
    
    top_k: int = Field(
        default=3,
        ge=1,
        le=10,
        description="Number of chunks to retrieve"
    )
    
    similarity_threshold: float = Field(
        default=0.6,
        ge=0.0,
        le=1.0,
        description="Minimum similarity score"
    )
    
    enable_caching: bool = Field(
        default=True,
        description="Enable embedding cache"
    )
    
    cache_size: int = Field(
        default=1000,
        description="Number of embeddings to cache"
    )

class LatencyAlert(BaseModel):
    """Latency alert configuration."""
    
    component: str
    threshold_ms: int
    current_ms: float
    exceeded: bool
    action: str
```

---

*M7 CONDUCTOR Domain 2 v1.0.0*
*Latency Engineering — "Every millisecond is heard"*

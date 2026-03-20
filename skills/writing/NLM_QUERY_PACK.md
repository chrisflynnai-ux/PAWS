# Writing Family — NLM Query Pack

## Notebook Setup
Load these source files into a dedicated NotebookLM notebook called "WRITING MASTERY":
- All files from `skills/writing/source_material/` (9 files)
- voice_dna.json, business.json, icp.json (from source_material)
- Any migrated writing skills from the archive

---

## Primary Queries (Run in order)

### Q1: Writing System Architecture
```
What is the complete writing system architecture across these documents?
Identify every distinct skill, agent role, and workflow mentioned.
For each one, extract: name, purpose, inputs, outputs, and relationships to other skills.
Specifically identify: orchestrator agent, research agent, and any specialist writers.
Present as a structured list.
```

### Q2: Voice DNA and Persona Patterns
```
Extract the complete voice DNA system from these documents.
Include:
- Voice characteristics and their definitions
- How voice is measured or scored
- Voice adaptation rules (how voice changes by context, audience, or channel)
- The structure of voice_dna.json
- Any templates or rubrics for voice consistency
Present as structured data.
```

### Q3: Golden Writing Patterns
```
Extract every reusable writing pattern, framework, or heuristic mentioned.
For each pattern:
- Pattern name
- When to use it
- How it works (2-3 sentences)
- Which type of writing it applies to (copy, content, scripts, emails, etc.)
- Evidence of effectiveness
Classify each as: HEURISTIC, SPEC, PATTERN, or FAILURE_MODE
```

### Q4: Writing Workflow and Agent Coordination
```
How does the multi-agent writing workflow operate?
Extract:
- The orchestrator's role and decision logic
- The research agent's role and outputs
- How research feeds into writing
- How writing is reviewed and refined
- The handoff sequence between agents
- Any quality gates or checkpoints
```

### Q5: ICP and Business Context Integration
```
How do the icp.json and business.json files integrate with the writing system?
Extract:
- What fields are in each file
- How they influence writing decisions (tone, angle, offer framing)
- How they map to the voice DNA system
- Any rules for adapting writing to different audience segments
```

---

## Secondary Queries

### Q6: Skill Structure Recommendation
```
Based on everything in this notebook, recommend a clean XSkill family structure for writing.
For each recommended skill:
- Name and ID
- Purpose (one sentence)
- Phase type: exploratory, compositional, executional, or resonant
- Key inputs and outputs
- Dependencies on other skills
- Whether it should be standalone or a sub-skill
```

### Q7: Experience Bank Seeds
```
Extract 10-15 tactical experience records from these documents:
{
  "scenario": "...",
  "trigger": "...",
  "action_taken": "...",
  "failure_mode": "...",
  "recovery_tactic": "...",
  "outcome": "success|partial|failure",
  "tags": [...]
}
Focus on writing-specific tactical insights — what works, what fails, what to watch for.
```

### Q8: Cross-Family Connections
```
How does the writing system connect to:
- Copy skills (sales pages, VSLs, advertorials)
- Content skills (blog posts, articles, social)
- Email skills (sequences, nurture tracks)
- Video/script skills (VSL scripts, content scripts)
Identify shared patterns, shared sub-skills, and handoff points between families.
```

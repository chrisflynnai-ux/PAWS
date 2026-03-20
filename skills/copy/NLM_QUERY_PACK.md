# Copy Family — NLM Query Pack

## Notebook Setup
Load these source files into a dedicated NotebookLM notebook called "COPY MASTERY":
- All files from `skills/copy/source_material/` (25 files)
- The 6 migrated skill.md files from `skills/copy/*/skill.md`
- RESONANCE_CONSTITUTION.xml (from source_material)
- CONVERSION_CORE_PATTERNS.yaml (from source_material)
- ORCHESTRATOR_CORE.yaml (from source_material)

---

## Primary Queries (Run in order)

### Q1: Core Copy Architecture
```
What is the complete copy skill architecture across these documents?
Identify every distinct skill, sub-skill, and workflow mentioned.
For each one, extract: name, purpose, inputs, outputs, and which other skills it depends on or delegates to.
Present as a structured list, not prose.
```

### Q2: Golden Patterns Extraction
```
Extract every reusable pattern, framework, or heuristic mentioned across these documents.
For each pattern, provide:
- Pattern name
- When to use it (trigger condition)
- How it works (2-3 sentences max)
- Which skill it belongs to
- Evidence of effectiveness (if mentioned)
Classify each as: HEURISTIC, SPEC, PATTERN, or FAILURE_MODE
```

### Q3: Failure Modes and Recovery
```
What are all the failure modes, anti-patterns, and common mistakes documented across these copy skills?
For each failure:
- Name it
- Describe how to detect it
- Describe the recovery tactic
- Rate severity: low / medium / high / critical
- Which skill is most affected
```

### Q4: Voice and Resonance Patterns
```
Extract all voice, tone, resonance, and persuasion patterns from these documents.
Include:
- Voice DNA elements (if present)
- Neuro-resonance dimensions (if referenced)
- 7S/7F chain patterns (if referenced)
- Convection model elements (if referenced)
- Any scoring rubrics for copy quality
Present as structured data, not narrative.
```

### Q5: Conversion Core Patterns Deep Dive
```
Analyze the CONVERSION_CORE_PATTERNS.yaml and ORCHESTRATOR_CORE.yaml files specifically.
Extract:
- Every named pattern with its definition
- The orchestration logic (what calls what, in what order)
- How these patterns map to the individual copy skills
- Any scoring weights or thresholds mentioned
```

---

## Secondary Queries (Run after primary)

### Q6: Skill Gaps and Redundancies
```
Based on everything in this notebook:
- Which copy capabilities are covered by multiple overlapping skills? (redundancy)
- Which copy capabilities are mentioned but have no dedicated skill? (gaps)
- Which skills should be merged vs kept separate?
- Recommend a clean, non-redundant skill family structure.
```

### Q7: Experience Bank Seeds
```
From all the tactical guidance, tips, warnings, and learned behaviors in these documents,
extract 10-15 experience records in this format:
{
  "scenario": "...",
  "trigger": "...",
  "action_taken": "...",
  "failure_mode": "...",
  "recovery_tactic": "...",
  "outcome": "success|partial|failure",
  "tags": [...]
}
Focus on actionable tactical insights, not general advice.
```

### Q8: Sub-Skill Candidates
```
Which procedures or workflows mentioned across these documents are:
1. Used by multiple parent skills
2. Have clear inputs and outputs
3. Could be extracted as standalone sub-skills or xScripts

For each candidate, describe: name, what it does, which skills use it, and whether it should be a sub-skill (procedural) or xScript (deterministic/automated).
```

# PAWS — Personal & Professional Agentic Workstations

A portable, composable agentic workstation powered by XSkill — structured skill libraries with experience-driven learning.

## What Is This?

PAWS transforms AI agents from prompt-following tools into skill-aware, memory-enabled collaborators. It combines:

- **XSkill Engine** — Markdown-based skill specs compiled to machine manifests with tactical experience banks
- **Multi-Model Routing** — Claude (brain), Codex (hands), Gemini (eyes), with worker models for bulk tasks
- **4-Layer Memory** — Ephemeral state → Obsidian vault → ThreadEx graph → Experience bank
- **Plugin Packaging** — Skill families as portable, installable units

## Architecture

```
PAWS (Harness)
  └── SUPERMIND (Agentic OS + Human UI)
       └── XSkill (Skill Engine)
            ├── skill.md          — human-authored source of truth
            ├── manifest.json     — compiled machine manifest
            └── experiences.jsonl — tactical learning layer
```

## Status

🚧 Active development — Phase 1: Schema lock + migration pipeline

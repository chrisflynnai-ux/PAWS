# PAWS — Personal & Professional Agentic Workstations

## Workspace
- **Canonical path**: `C:\DEV\SUPERMIND`
- **Repo**: https://github.com/chrisflynnai-ux/PAWS
- **Branch**: main

## Architecture
- **PAWS** = The Harness (portable agentic workstation)
- **SUPERMIND** = Agentic OS + human frontend
- **XSkill** = Skill engine (skill.md + manifest.json + experiences.jsonl)
- **COSM** = Knowledge Hubs & Collectives (future distribution layer)

## Model Routing
| Role | Model | Tasks |
|------|-------|-------|
| Orchestrator | Codex Opus/Sonnet | Doctrine, schema, architecture, review |
| Build Engine | Codex 5.4 | Migration, refactors, validators, tests |
| Eyes/Design | Gemini | Visual QA, dashboard UI, screenshot audit |
| Workers | Kimi K2.5 / Minimax 2.7 / GLM 5 | Research, docs, bulk generation |

## Source of Truth
- `skill.md` is the human-authored canonical spec
- `manifest.json` is the compiled machine artifact (derived, never hand-edited)
- `experiences.jsonl` is the tactical learning layer (separate from skill spec)
- No dual editable source of truth between Markdown and JSON

## Migration Pipeline
```
XML → AST → skill.md → manifest.json → Experience Bank → validation → evals
```

## Memory Architecture
- **L1**: SESSION_STATE.json (ephemeral task state)
- **L2**: Obsidian vault (human-searchable knowledge)
- **L3**: ThreadEx graph.db (structural memory, skill relations)
- **L4**: experiences.jsonl (tactical patterns per skill)

## Vault-First Rule (MANDATORY)
Before any web search, repo clone, or external research — search the Obsidian vault and ThreadEx first. The answer is almost always already documented.

## Key Directories
```
skills/           ← XSkill packages (skill.md + manifest.json + experiences.jsonl)
tools/            ← Pipeline tools (migrator, validator, drift-detector)
.agents/          ← Agent configs and routing
.threadex/        ← Memory layer (graph.db, expertise, mastery)
.Codex/          ← Codex config and schemas
docs/             ← Architecture and plans
memory/           ← SESSION_STATE.json, MEMORY.md
dashboard/        ← Mission Control fork (future)
```

## Locked Decisions
1. Codex is orchestrator for all refactors
2. Codex is the build/migration engine
3. Markdown is canonical human-authored skill spec
4. manifest.json is compiled machine artifact
5. experiences.jsonl is separate tactical learning layer
6. Pilot one skill family before scaling migration
7. No OpenClaw dependency — Codex is the harness
8. Git sync to GitHub (local-first, cloud-ready later)

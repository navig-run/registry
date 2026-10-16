# GENESIS — Build in Public Space (agent briefing)

> **If you are an AI agent:** read this before acting in this space.

**Space:** `build-in-public-space` · **Tier:** community · **Status:** planned

This space is a **stub**. Its purpose has not been authored yet, and it ships no
agents, skills, workflows or formations (`.navig/space.json` lists none).

Its intended scope (sharing your work in public: session recordings, published
workflows, forks) overlaps with [`open-space`](../../open-space/README.md), which
already carries that concept. Until the two are merged or this space gets its own
purpose, point the owner to `open-space`.

## If the owner wants to use it anyway

1. Ask what they want to stop losing track of, and write it into `../README.md`.
2. Fill in `description` in `.navig/space.json`.
3. Add capability under `.navig/skills/` or `.navig/store/{agents,workflows,formations}/`
   and list it in `.navig/space.json` in the same change.
4. Keep every path relative to the space.

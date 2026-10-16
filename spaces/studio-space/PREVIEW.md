# NAVIG Studio Space

**Music production command center — from first beat to final master.**

---

## What It Is

A production-grade NAVIG space for managing every stage of the music production lifecycle — session tracking, mixing, mastering, sample management, and release distribution. Works with any DAW on **Windows, Linux, and macOS**. Fork it, point it at your projects folder, and start producing.

---

## Key Features

- **10 cross-platform skills** — BPM detection, key detection, loudness metering, stem export, format conversion, metadata tagging, distributor upload, session backup, sample cataloging, DAW project scanning
- **5 specialized agents** — producer (creative lead), mix-engineer (levels & EQ), sound-designer (samples & synthesis), release-manager (distribution), session-planner (scheduling)
- **6 automated workflows** — track production, release cycle, morning studio check, weekly review, sample harvest, session prep
- **8 production prompts** — new track brief, mix review, master checklist, release prep, genre analysis, collab brief, catalog report, sound design brief
- **Full wiki starter kit** — production workflow, mixing guide, mastering reference, release checklist, genre palette, agent guide

---

## Usage Example

```bash
# Activate the space
navig space use studio-space

# Scan all DAW projects in your sessions folder
navig skill run daw-project-scan --path ~/Music/Sessions

# Check loudness compliance before release
navig skill run loudness-check --file master.wav --standard streaming

# Hand a production request to the specialists
navig formation run "Take the new track from rough mix to a streaming-ready master"
```

---

## Quick Install

```bash
navig space install github:navig-run/registry/spaces/studio-space
navig space use studio-space
```

# Changelog — NAVIG Studio Space

All notable changes to the `studio` space will be documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [1.0.0] — 2026-04-05

### Added

**Agents**
- `producer` — Creative direction and session orchestration lead
- `mix-engineer` — Mixing, levels, EQ, spatial placement
- `sound-designer` — Sample creation, synthesis, sound palette
- `release-manager` — Distribution, metadata, platform compliance
- `session-planner` — Calendar, deadlines, session prep

**Formations**
- `track-production` — Full single-track production pipeline
- `release-pipeline` — From final master to distribution
- `sample-lab` — Sample discovery, processing, cataloging
- `mastering-suite` — Final mix QC and master delivery
- `collab-session` — Multi-artist session coordination

**Skills**
- `bpm-detect` — Detect tempo from audio files
- `key-detect` — Detect musical key from audio files
- `loudness-check` — LUFS metering against streaming/broadcast standards
- `stem-export` — Export individual stems from multi-track session
- `format-convert` — Convert between WAV, FLAC, MP3, AAC, OGG
- `metadata-tag` — Write ID3/Vorbis metadata to audio files
- `upload-distro` — Prepare and validate distributor upload packages
- `backup-session` — Incremental session backup with version tracking
- `sample-catalog` — Scan, tag, and index sample libraries
- `daw-project-scan` — Discover and index DAW project files

**Workflows**
- `track-production` — End-to-end single track pipeline
- `release-cycle` — Master → metadata → upload → verify
- `morning-studio` — Daily session status and inbox check (cron)
- `weekly-review` — Weekly production metrics and backlog review
- `sample-harvest` — Batch catalog and organize new samples
- `session-prep` — Pre-session setup and asset verification

**Prompts**
- 8 production prompt templates covering all workflow stages

**Wiki**
- Production workflow guide, mixing reference, mastering standards, release checklist

**Infrastructure**
- Full `.navig/` configuration layer
- Cross-platform skills (Windows, Linux, macOS)
- Memory layer with space context, goals, known issues
- Inbox routing with 5 channels

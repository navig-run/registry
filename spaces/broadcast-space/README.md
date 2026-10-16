# 🎙️ Broadcast Space

> Podcast & Live Streaming Command Center — professional audio content production, distribution, and growth.

## Structure

```
broadcast-space/
├── space.manifest.json      # Store manifest
├── package.json             # Scripts and metadata
├── GENESIS.md               # Origin story
├── README.md                # This file
├── PREVIEW.md               # Store listing
├── CHANGELOG.md             # Version history
├── LICENSE                  # MIT
├── .gitignore
└── .navig/
    ├── space.json           # Canonical manifest
    ├── space.config.json    # Runtime config
    ├── space.manifest.json  # Internal paths
    ├── config.yaml          # Domain settings
    ├── context.md           # Space context
    ├── memory/              # Persistent memory (*.example.json seeds)
    ├── inbox/               # Message routing (routes.example.yaml)
    ├── store/
    │   ├── agents/          # 5 agents
    │   ├── formations/      # 5 formations
    │   ├── workflows/       # 6 workflows
    │   ├── prompts/         # 8 prompt templates
    │   └── mcp/             # Audio tool declarations (ffmpeg, whisper)
    ├── skills/              # 10 skills
    ├── wiki/                # 7 knowledge pages
    ├── ops/                 # Runbooks
    ├── plans/               # Phase tracking
    ├── episodes/            # Episode storage
    ├── guests/              # Guest profiles
    ├── assets/              # Cover art, intros, outros
    └── exports/             # Rendered episodes and clips
```

## Agents

| Agent | Role | Inbox |
|-------|------|-------|
| host | Show Host & Creative Lead | #episodes |
| sound-engineer | Audio Engineer | #audio |
| show-planner | Content Planner & Researcher | #planning |
| publisher | Distribution & RSS Manager | #publishing |
| community-manager | Audience & Guest Relations | #community |

## Skills

| Skill | Category | Purpose |
|-------|----------|---------|
| audio-record | recording | Configure and start recording sessions |
| audio-edit | editing | Edit audio files (trim, splice, crossfade) |
| noise-reduce | editing | Remove background noise from recordings |
| loudness-normalize | mastering | Normalize loudness to -16 LUFS (podcast standard) |
| rss-generate | distribution | Generate and validate RSS podcast feeds |
| show-notes-write | content | Generate show notes from transcript |
| transcript-generate | content | Transcribe audio to text with timestamps |
| guest-research | research | Research potential guests and prepare briefs |
| episode-schedule | publishing | Schedule episodes across platforms |
| clip-extract | editing | Extract highlight clips from episodes |

## Quick Start

```bash
# Produce an episode (topic prep → record → edit → master → notes → transcript)
navig flow run episode-production

# Book a guest
navig flow run guest-pipeline

# Go live
navig flow run live-show

# Plan the week
navig flow run weekly-planning
```

Each workflow asks its agents for the details (topic, guest, platform) as it runs; add
`--dry-run` to preview the steps first.

## First run

Memory ships as examples: copy `.navig/memory/*.example.json` to `*.json` and
`.navig/inbox/routes.example.yaml` to `routes.yaml` (see the README in each folder).

## Requirements

- **ffmpeg** — Audio processing and conversion
- **yt-dlp** — Media download and extraction (optional)
- **whisper** — AI transcription (optional, for transcript-generate)

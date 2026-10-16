# Clips Space

> Short-form video factory for TikTok, Instagram Reels, and YouTube Shorts.

## Structure

```
clips-space/
├── space.manifest.json       # Space metadata
├── package.json              # NAVIG scripts
├── GENESIS.md                # Origin story
├── README.md                 # This file
├── PREVIEW.md                # Store listing
├── CHANGELOG.md              # Version history
├── LICENSE                   # MIT
├── clips/                    # Short-form video files
├── hooks/                    # Hook scripts and templates
├── trends/                   # Trend reports and captures
├── scripts/                  # Automation scripts
├── tests/                    # Validation tests
├── docs/                     # Documentation
├── .navig/
│   ├── space.json            # Canonical manifest (NAVIG reads this first)
│   ├── space.config.json     # Legacy runtime config
│   ├── space.manifest.json   # Internal paths
│   ├── config.yaml           # Settings
│   ├── context.md            # Purpose and scope
│   ├── memory/               # State and context (*.example.json seeds)
│   ├── inbox/                # Task routing (routes.example.yaml)
│   ├── store/
│   │   ├── agents/           # 5 AI agents
│   │   ├── formations/       # 5 team formations
│   │   ├── workflows/        # 5 automated workflows
│   │   ├── prompts/          # 8 prompt templates
│   │   └── mcp/              # Tool configurations
│   ├── skills/               # 10 platform skills
│   ├── wiki/                 # Knowledge base
│   ├── ops/                  # Procedures
│   └── plans/                # Phase tracking
```

## Agents

| Agent | Role | Formation |
|-------|------|-----------|
| clip-director | Creative Lead | clip-factory |
| hook-writer | Hook Specialist | clip-factory |
| clip-editor | Video Editor | clip-factory |
| trend-scout | Trend Analyst | trend-ride |
| distributor | Multi-Platform Publisher | batch-schedule |

## Skills

| Skill | Category |
|-------|----------|
| trend-scan | analytics |
| hook-score | content |
| clip-trim | editing |
| caption-generate | content |
| sound-match | audio |
| multi-post | publishing |
| analytics-aggregate | analytics |
| hashtag-optimize | seo |
| format-adapt | editing |
| batch-export | editing |

## Quick Start

```bash
navig space install github:navig-run/registry/spaces/clips-space
navig space use clips-space
# first run: copy the memory and inbox examples (see .navig/memory/README.md)
navig formation run "Make a clip about 5 productivity hacks for TikTok, Reels and Shorts"
navig formation run "Ride this trend: <trend URL>"
```

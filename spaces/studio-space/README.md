# Studio Space

> Music production command center — from first beat to final master.

Part of the [NAVIG registry](https://github.com/navig-run/registry) space collection.

## Overview

Studio Space gives independent producers, beatmakers, and audio engineers a structured command layer over the entire music production lifecycle. Track sessions, manage mixes, enforce mastering standards, organize samples, and coordinate releases — all from one space.

## Structure

```
studio-space/
├── space.manifest.json          # Store/registry manifest
├── package.json                 # npm-style config with navig scripts
├── GENESIS.md                   # Origin story and design rationale
├── PREVIEW.md                   # Marketplace preview card
├── CHANGELOG.md                 # Version history
├── LICENSE                      # MIT
├── .navig/
│   ├── space.json               # Canonical manifest (NAVIG reads this first)
│   ├── space.config.json        # Legacy runtime configuration
│   ├── space.manifest.json      # Internal paths and lists
│   ├── config.yaml              # Space settings
│   ├── context.md               # Space context summary
│   ├── skills/                  # 10 cross-platform skills
│   ├── store/
│   │   ├── agents/              # 5 specialized agents
│   │   ├── formations/          # 5 formation configs
│   │   ├── workflows/           # 6 automated workflows
│   │   ├── prompts/             # 8 production prompts
│   │   └── mcp/                 # MCP tool config
│   ├── wiki/                    # 7 wiki pages
│   ├── memory/                  # Context, goals, issues (*.example.json seeds)
│   ├── inbox/                   # Routing rules (routes.example.yaml)
│   ├── plans/                   # Phase tracking
│   └── ops/                     # Operational docs
├── releases/                    # Release staging area
├── samples/                     # Sample library root
├── sessions/                    # DAW session projects
├── screenshots/                 # Store screenshots
├── scripts/                     # Utility scripts
├── tests/                       # Validation tests
└── docs/                        # Extended documentation
```

## Quick Start

```bash
# Install and activate
navig space install github:navig-run/registry/spaces/studio-space
navig space use studio-space

# First run: seed memory and inbox routing from the shipped examples
#   (see .navig/memory/README.md and .navig/inbox/README.md)

# Discover DAW projects
navig skill run daw-project-scan --path ~/Music/Sessions

# Run a request across the production specialists
navig formation run "Plan a session for the new track: 124 BPM, A minor, house"
```

The workflows in `.navig/store/workflows/` (`morning-studio`, `track-production`,
`release-cycle`, …) are step-by-step playbooks the agents follow. Ask the producer to run
one ("run the morning-studio routine"); they are not standalone CLI commands.

## Agents

| Agent | Role | Formation |
|-------|------|-----------|
| `producer` | Creative direction, arrangement, orchestration | track-production |
| `mix-engineer` | Levels, EQ, compression, spatial placement | mastering-suite |
| `sound-designer` | Samples, synthesis, sound palette curation | sample-lab |
| `release-manager` | Distribution, metadata, compliance | release-pipeline |
| `session-planner` | Calendar, deadlines, session prep | collab-session |

## Skills

| Skill | Category | Description |
|-------|----------|-------------|
| `bpm-detect` | analysis | Detect tempo from audio files |
| `key-detect` | analysis | Detect musical key from audio |
| `loudness-check` | mastering | LUFS metering against standards |
| `stem-export` | production | Export stems from multi-track |
| `format-convert` | delivery | Convert between audio formats |
| `metadata-tag` | delivery | Write ID3/Vorbis metadata |
| `upload-distro` | release | Prepare distributor packages |
| `backup-session` | ops | Incremental session backup |
| `sample-catalog` | library | Scan, tag, index samples |
| `daw-project-scan` | discovery | Find and index DAW projects |

## License

MIT — see [LICENSE](LICENSE).

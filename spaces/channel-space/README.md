# Channel Space

> AI-powered YouTube creator command center.

## Features

- 🎬 5 specialised agents (showrunner, scriptwriter, editor, growth-analyst, art-director)
- 📊 10 skills (SEO audit, thumbnail scoring, analytics, title generation, and more)
- 🔄 6 automated workflows (video production, weekly review, SEO refresh, and more)
- 📝 8 structured prompts (video brief, script outline, thumbnail brief, and more)
- 📚 Wiki knowledge base with creator guides

## Quick Start

```bash
# Install and activate the space
navig space install github:navig-run/registry/spaces/channel-space
navig space use channel-space

# First run: seed memory and inbox routing from the shipped examples
#   (see .navig/memory/README.md and .navig/inbox/README.md)

# Hand a request to the specialists
navig formation run "Plan next week's video on Docker basics: script outline, title and thumbnail brief"
```

The workflows in `.navig/store/workflows/` (`video-production`, `morning-channel`,
`weekly-review`, …) are playbooks the agents follow. Ask the showrunner to run one by
name; they are not standalone CLI commands.

## Structure

```
channel-space/
├── .navig/
│   ├── config.yaml
│   ├── context.md
│   ├── inbox/           (routes.example.yaml)
│   ├── memory/          (*.example.json seeds)
│   ├── ops/
│   ├── plans/
│   ├── skills/          (10 skills)
│   ├── space.json       (canonical manifest)
│   ├── space.config.json
│   ├── space.manifest.json
│   ├── state/
│   ├── store/
│   │   ├── agents/      (5 agents)
│   │   ├── formations/  (5 formations)
│   │   ├── mcp/
│   │   ├── prompts/     (8 prompts)
│   │   └── workflows/   (6 workflows)
│   └── wiki/            (7 pages)
├── CHANGELOG.md
├── content/
├── GENESIS.md
├── LICENSE
├── package.json
├── PREVIEW.md
├── README.md
├── screenshots/
├── scripts/
├── space.manifest.json
├── tests/
└── thumbnails/
```

## Agents

| Agent | Role | Formation |
|-------|------|-----------|
| showrunner | Creative Director | video-production |
| scriptwriter | Content Writer | content-planning |
| editor | Post-Production Lead | video-production |
| growth-analyst | Data Analyst | channel-growth |
| art-director | Visual Designer | thumbnail-lab |

## Skills

| Skill | Category |
|-------|----------|
| seo-audit | analytics |
| thumbnail-score | design |
| analytics-pull | analytics |
| title-generator | content |
| description-writer | content |
| tag-optimizer | seo |
| schedule-publish | publishing |
| retention-analysis | analytics |
| competitor-scan | research |
| hook-analyzer | content |

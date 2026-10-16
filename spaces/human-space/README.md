# Human Space — v2.0.0

> Your self, managed like a system. Health, habits, learning, journal, and administrative life — all in one place.

A personal life management space powered by **5 agents**, **5 formations**, **9 skills**, **5 workflows**, **8 prompts**, and **7 wiki pages**.

---

## Agent Roster

| Agent | Role |
|-------|------|
| `daily-planner` | Morning routine, priorities, journal, weekly retro |
| `wellness-tracker` | Health metrics, mood, sleep, body composition |
| `habit-coach` | Habit design (Atomic Habits), streaks, portfolio |
| `growth-tracker` | Learning, books, courses, skill development |
| `bureau-manager` | Documents, renewals, subscriptions, appointments |

## Formations

| Formation | Trigger | Lead Agent |
|-----------|---------|------------|
| `morning-routine` | Daily 07:00 | daily-planner |
| `health-ops` | Weekly Sunday | wellness-tracker |
| `evening-reflection` | Daily 21:00 | daily-planner |
| `growth-ops` | Monthly 1st | growth-tracker |
| `bureau-ops` | Monthly 1st | bureau-manager |

---

## Structure

```
human-space/
  README.md                 ← this file
  PREVIEW.md                ← quick stats
  CHANGELOG.md              ← version history
  LICENSE                   ← MIT
  package.json              ← space metadata
  space.manifest.json       ← space identity (legacy shape)
  .gitignore
  .navig/
    space.json              ← canonical manifest
    config.yaml             ← space configuration
    context.md              ← domain context + principles
    profile.json            ← identity profile
    inbox/routes.example.yaml ← inbox routing (copy to routes.yaml)
    memory/                 ← *.example.json seeds (copy to <name>.json on first use)
    plans/                  ← CURRENT_PHASE.md, DEV_PLAN.md
    store/
      agents/               ← 5 agent definitions
      formations/           ← 5 formation definitions
      workflows/            ← 5 workflow definitions
      prompts/              ← 8 prompt templates
      mcp/                  ← MCP configurations
    skills/                 ← 9 skill definitions
    wiki/                   ← 7 wiki pages
  spaces/                   ← local data areas used by the agents
    health/                 ← metrics.csv, fitness logs
    growth/                 ← habits.csv, learning.csv, journal/, retros/, books/
    bureau/                 ← renewals.csv, subscriptions, appointments
  docs/                     ← reference docs
```

---

## Local data areas and related spaces

The three folders under `spaces/` are plain data folders that Human Space's own agents
read and write — they are not nested spaces. Document scans (IDs, medical, insurance)
never live there: they go in the encrypted cabinet (`navig cabinet add`).

For a deeper setup in one area, install the matching standalone space next to this one:

| Area | Standalone space | Purpose |
|------|------------------|---------|
| `spaces/health` | `health-space` | Physical and mental health — metrics, protocols, sleep, training |
| `spaces/growth` | `growth-space` | Learning, skill-building, and habit formation |
| `spaces/bureau` | `bureau-space` | Administrative life — deadlines, documents, dossiers |

`research-space` and `social-circle-space` are independent spaces that pair well with
this one; they are not part of it.

---

## Quick Start

```bash
# Morning routine
@daily-planner morning

# Log mood
@wellness-tracker mood --score 7 --notes "good energy"

# Log health metrics
@wellness-tracker log --sleep 7.5 --steps 9000 --mood 7

# Check habit streaks
@habit-coach review --period last-week

# Design a new habit
@habit-coach design --habit "Read 10 pages before sleep"

# Log a book
@growth-tracker log --type book --title "Deep Work" --status started

# Check renewals
@bureau-manager renewals --days-ahead 30

# Evening reflection
@daily-planner evening
```

---

## Wiki

| Page | Topic |
|------|-------|
| [agent-guide](.navig/wiki/agent-guide.md) | All 5 agents with commands |
| [runbooks](.navig/wiki/runbooks.md) | 10 personal operating procedures |
| [habit-science](.navig/wiki/habit-science.md) | Atomic Habits framework |
| [health-metrics-guide](.navig/wiki/health-metrics-guide.md) | What to track and why |
| [growth-framework](.navig/wiki/growth-framework.md) | Learning system |
| [bureau-guide](.navig/wiki/bureau-guide.md) | Administrative life management |

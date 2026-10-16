# Social Circle

> Your entire human network — mapped, searchable, and deeply personal.

Not a CRM. Not a social feed. A **personal relationship layer** — the one place where every person you know exists in one unified, living map.

> **Status: planned.** This space ships its design, configuration and runbooks. The agents,
> packages and graph view described below are not shipped yet. What works today is NAVIG's
> built-in contact book — `navig contacts add | import | list | search | show` — see
> [Quick Start](#quick-start).

---

## What It Does

Social Circle lets you maintain your full personal network across every dimension of your life:

| Dimension | Examples |
|-----------|---------|
| Real life | Close friends, family, neighbors, gym people |
| Work | Colleagues, clients, managers, ex-coworkers |
| Internet | Discord friends, Twitter mutuals, GitHub collaborators, forum regulars |
| Transient | Conference meets, one-time collaborators, warm leads |

You add people. You log how you're connected. You track when you last talked. The space tells you what's going cold and who you should reach out to.

---

## Core Features

### Circles
User-defined relationship buckets. Default set (from `.navig/memory/space-context.example.json`):

- **inner-circle** — deepest, most active
- **family** — always in the graph
- **friends** — real-life friends
- **work** — professional context
- **community** — clubs, events, neighbours
- **online** — digital-first people

Create, rename, merge, or delete circles at any time. One person can belong to multiple circles.

---

### Contacts
Each contact holds:

```
Name           Jane Example
Circles        inner-circle · work
Tags           met at a conference · co-author
Handles        @jane.example (social) · jane-example (code host)
Last contact   2026-01-14 · direct message · discussed a joint project
Strength       ████░ Strong (4/5)
Notes          Writing a paper on agent memory. Introduced me to a colleague.
```

All fields are optional except name. Add what you know.

---

### Interaction Log
Lightweight touchpoint tracking per contact:

```
2026-03-12  call         Caught up after the launch. Moving to a new city.
2026-01-14  message      Discussed the joint project.
2025-11-03  IRL coffee   Met at a conference. Talked open-source strategy.
```

Channels: `IRL` · `call` · `video` · `message` · `email` · `social` · `event` · `letter`

Interaction logging is part of the planned `interaction-log` package (not shipped yet).

---

### Relationship Strength
Auto-calculated from interaction frequency. No manual scoring needed.

| Score | Label | When |
|-------|-------|------|
| ●●●●● | **Deep** | Multiple interactions / 30 days |
| ●●●●○ | **Strong** | Contacted in the last 30 days |
| ●●●○○ | **Warm** | Contacted in the last 90 days |
| ●○○○○ | **Cold** | 90+ days since last interaction (`relationship_cold_after_days` in `.navig/config.yaml`) |
| ○○○○○ | **Dormant** | Never logged |

The planned agent surfaces all Cold and Dormant contacts on demand: "Who have I not talked to in 3 months?"

---

### Visual Graph View
Force-directed node graph. Every contact is a node. Circles define clusters. Edge thickness = relationship strength.

Interactive:
- Click a node → contact detail drawer
- Drag to rearrange clusters
- Filter by circle, tag, or strength
- Highlight mutual connections between contacts

---

### List & Card View
- **List** — sortable table: name, circles, tags, last interaction, strength
- **Card** — grid of contact cards with photo/avatar, circle badges, last-contact indicator

Toggle freely. Both views share the same filter state.

---

### Search & Filter
Full-text search across names, tags, notes, and handles.

Filter combinations:
```
circle:Work AND strength:Cold
tag:"met at" AND last_contact:>2025-01-01
circle:Mentors
handle:github:*
```

---

## Import

| Source | How |
|--------|-----|
| Manual | Type directly or via quick-add form |
| CSV | Any CSV — agent maps columns on import |
| LinkedIn | Export `Connections.csv` from LinkedIn Data → drop in inbox |
| Google Contacts | `.vcf` or Google CSV export |
| Twitter/X | Paste a handle — agent resolves name + bio |
| vCard (`.vcf`) | Standard contact files |

All imports land in `.navig/inbox/` for review before committing to the graph.

---

## Packages (planned — not shipped yet)

| Package | What it does |
|---------|-------------|
| `contact-graph` | Core data model — contacts, circles, connections, strength engine |
| `circle-manager` | Circle CRUD, membership management, merge/split |
| `interaction-log` | Touchpoint logging, channel types, timeline queries |
| `import-bridge` | CSV/VCF/LinkedIn/Google import pipeline with field mapping |
| `relationship-strength` | Frequency-based strength calculator, cold-contact surfacing |

---

## Agent Capabilities (planned)

The planned relationship agents (see `.navig/wiki/agent-guide.md`) are designed to answer:

```
"Who haven't I talked to in 3 months?"
"Add Jane Example — online circle, met in a community chat"
"Log a call with Sam yesterday, we discussed the trip"
"Show me everyone I know at <company>"
"Who introduced me to <name>?"
"My work circle — who's gone cold?"
"Import this LinkedIn CSV and match duplicates"
```

---

## Quick Start

```bash
# Load the space
navig space switch social-circle-space

# Add your first contact (NAVIG's built-in contact book)
navig contacts add --name "Jane Example" --alias jane --space social-circle-space

# Find and inspect contacts
navig contacts search "conference"
navig contacts show jane
navig contacts list --space social-circle-space

# Import an address book (vCard / CSV export), merging duplicates
navig contacts import ~/Downloads/contacts.vcf --space social-circle-space --dry-run
navig contacts import ~/Downloads/contacts.vcf --space social-circle-space
```

---

## Setup

```bash
# Linux / macOS — create optional root symlinks
bash setup-links.sh

# Windows
powershell setup-links.ps1
```

---

*Social Circle — NAVIG OS · personal tier · status: planned · `crossplatform: true`*

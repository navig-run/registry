# Content Strategy Workshop

Editorial calendars, content briefs, brand voice guides, and pipeline planning.

## Getting Started

1. Update `editorial-calendar.csv` with your content backlog
2. Create a brief for any new piece: `@content-strategist brief --topic "<topic>" --audience "<audience>" --goal "<goal>"`
3. Assign briefs to agents or writers
4. Track status in the calendar CSV: Planned → In Progress → In Review → Published

## Folder Structure

```
content-strategy/
├── editorial-calendar.csv      ← Live content calendar
├── content-brief-template.md  ← Template for individual piece briefs
└── README.md
```

## Pipeline Statuses

| Status | Meaning |
|--------|---------|
| Planned | Brief created, not yet assigned |
| In Progress | Draft underway |
| In Review | Submitted for editorial review |
| Approved | Passed editorial-review workflow |
| Published | Live |
| Archived | No longer current |

## Agents

- `@content-strategist` — calendars, briefs, audits, brand voice
- `@tech-writer` — technical content and documentation pieces
- `@editor` — QA and editorial pass

## Workflows

```
navig flow run editorial-review --var file=<draft.md>
navig flow run publish-checklist --var file=<final.md>
```

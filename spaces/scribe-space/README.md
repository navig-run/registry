# scribe-space

> **The writers' space.** Fiction, journalism, screenwriting, technical documentation, and content strategy — all under one NAVIG workspace.

[![NAVIG Space Runtime](https://img.shields.io/badge/runtime-navig--space--2.0-blue)](https://navig.run)
[![Space Type](https://img.shields.io/badge/type-workspace-green)]()
[![Status](https://img.shields.io/badge/status-active-brightgreen)]()

---

## Sub-workspaces

| Folder | Purpose |
|--------|---------|
| [book-writing/](book-writing/) | Long-form fiction and narrative non-fiction |
| [journalism/](journalism/) | News articles, investigations, features |
| [general-writing/](general-writing/) | Essays, personal writing, miscellaneous |
| [screenwriting/](screenwriting/) | Fountain-format film and TV scripts |
| [technical-writing/](technical-writing/) | API docs, guides, SOPs, changelogs |
| [content-strategy/](content-strategy/) | Editorial calendars, briefs, brand voice |

---

## Agents

| Agent | Role | Inbox |
|-------|------|-------|
| `storyteller` | Long-form fiction and narrative | `#fiction` |
| `journalist` | Investigations and articles | `#journalism` |
| `editor` | Structural, line, and copy editing | `#edit` |
| `content-strategist` | Editorial planning and brand voice | `#content` |
| `screenwriter` | Fountain-format scripts | `#screen` |
| `tech-writer` | API docs, guides, SOPs | `#docs` |

---

## Quick Start

### Start a new book project
```
@storyteller outline --genre <genre> --premise "<premise>"
```

### Write a news article
```
@journalist brief --topic "<topic>" --angle "<angle>"
navig flow run first-draft --var type=article --var title="<title>"
```

### Write a screenplay scene
```
@screenwriter scene --location "INT. CAFÉ - DAY" --beat "<beat description>"
```

### Run editorial review
```
navig flow run editorial-review --var file=<draft.md> --var depth=full
```

### Export to PDF
```
export-pdf skill: file=<doc.md> format=pdf   (ask any Scribe agent)
```

---

## Documentation

- [Agent Guide](.navig/wiki/agent-guide.md)
- [Runbooks](.navig/wiki/runbooks.md)
- [Architecture](.navig/wiki/architecture.md)
- [Full Reference](docs/README.md)

---

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

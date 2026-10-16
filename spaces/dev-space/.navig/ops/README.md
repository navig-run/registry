# Dev Space Ops

Operational runbooks and automation procedures for the dev space.

## Relationship to `scripts/`

| Folder | Purpose |
|--------|---------|
| `ops/` | Runbooks, checklists, release procedures, SOP docs |
| `scripts/` | Raw PowerShell/Bash tooling and automation |

---

## Runbook Index

| Runbook | Trigger | Target |
|---------|---------|--------|
| [Code Review](../store/workflows/code-review.yaml) | On PR / on-demand | → workflow |
| [Run Tests](../store/workflows/run-tests.yaml) | On push / on-demand | → workflow |
| [Daily Standup](../store/workflows/daily-standup.yaml) | Daily 09:00 | → workflow |
| [Scaffold Project](../skills/scaffold-project.yaml) | On new project | → skill |
| [Publish Extension](../skills/publish-extension.yaml) | On release | → skill |

---

## Agents

| Agent | Role | Inbox |
|-------|------|-------|
| coder | Scaffolding, authoring, implementation | `#code` |
| debugger | Bug investigation and tracing | `#debug` |
| reviewer | Code review and quality | `#review` |
| scripter | Userscript & extension specialist | `#extensions` |

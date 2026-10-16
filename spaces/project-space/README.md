# Project Space

Own every project from idea to done.
Plan clearly. Track visibly. Unblock fast.

## Quick Start

```bash
# Kick off a new project
navig flow run new-project

# Weekly standup (update all active projects)
navig flow run weekly-standup

# Close a finished project
navig flow run project-close --var project=my-project
```

## Structure

```
projects/
  {slug}/
    project.json     Metadata: status, owner, done-state, dates
    milestones.md    Milestone list with status
    tasks/           Active task files
    blockers.md      Current blockers and next actions
    decisions.md     Key decisions and rationale
    notes/           Research, context, reference
    close.md         Final outcomes (written at close)
```

## Agents

| Agent | What It Does |
|-------|-------------|
| project-planner | Scopes new projects, defines milestones, tracks status |
| task-tracker | Manages individual tasks: priority, status, blockers |
| milestone-keeper | Tracks milestone progress and flags slippage |
| blocker-resolver | Surfaces all open blockers, facilitates resolution |

## Workflows

| Workflow | When |
|----------|------|
| new-project | Starting any new project |
| weekly-standup | Weekly — review all active projects |
| project-close | When a project reaches done-state |

## Inbox Routes

- `#projects` — new project ideas or updates
- `#blockers` — anything blocking progress
- `#tasks` — task updates, completions

Routing rules ship as `.navig/inbox/routes.example.yaml` and memory as
`.navig/memory/*.example.json` — copy them to `routes.yaml` / `*.json` on first run
(see the README in each folder).

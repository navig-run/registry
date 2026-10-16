# Reference

API references, schema definitions, and parameter documentation for devops-space tools.

## Agent API

See [agent-guide](../../.navig/wiki/agent-guide.md) for full invocation examples.

## Skill Parameters

| Skill | Key Parameters |
|-------|---------------|
| `health-probe` | `--url`, `--timeout` |
| `rollback` | `--method`, `--service`, `--version` |
| `alert-triage` | `--alert` |
| `deploy-validate` | `--image`, `--scan` |
| `cert-check` | `--domains` (optional — reads monitoring/domains.txt) |

## Workflow Parameters

| Workflow | Key Parameters |
|----------|---------------|
| `deploy-check` | `--service`, `--version`, `--env` |
| `incident-triage` | `--severity`, `--service`, `--alert-name` |
| `weekly-reliability-review` | _(scheduled; no params)_ |

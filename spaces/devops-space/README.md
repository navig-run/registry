# devops-space

> **The DevOps engineering hub.** CI/CD pipelines, infrastructure-as-code, site reliability engineering, and incident response.

[![NAVIG Space Runtime](https://img.shields.io/badge/runtime-navig--space--2.0-blue)](https://navig.run)
[![Space Type](https://img.shields.io/badge/type-workspace-green)]()
[![Status](https://img.shields.io/badge/status-active-brightgreen)]()

---

## Sub-workspaces

| Folder | Purpose |
|--------|---------|
| [ci-cd/](ci-cd/) | Pipeline templates and workflow definitions |
| [infrastructure-as-code/](infrastructure-as-code/) | Terraform and Ansible starters |
| [monitoring/](monitoring/) | Prometheus rules, Grafana dashboards, domain lists |
| [runbooks/](runbooks/) | Human-readable incident and ops runbooks |

---

## Agents

| Agent | Role | Inbox |
|-------|------|-------|
| `pipeline-engineer` | CI/CD design, diagnosis, optimisation | `#pipeline` |
| `infra-architect` | IaC authoring and review | `#infra` |
| `site-reliability` | SLOs, alerting, reliability reviews | `#sre` |
| `incident-commander` | Incident management and postmortems | `#incidents` |

---

## Quick Start

### First run — seed the space state
The space ships example state only. Copy each example to its live name and edit it:
```
.navig/memory/goals.example.json         → .navig/memory/goals.json
.navig/memory/known-issues.example.json  → .navig/memory/known-issues.json
.navig/memory/space-context.example.json → .navig/memory/space-context.json
.navig/inbox/routes.example.yaml         → .navig/inbox/routes.yaml
```

### Design a CI/CD pipeline
```
@pipeline-engineer design --platform github-actions --language python --deploy kubernetes
```

### Scaffold Terraform infrastructure
```
@infra-architect scaffold --cloud aws --pattern vpc-3tier --env staging --prefix myapp
```

### Run the weekly reliability review
```
navig ask "run the weekly-reliability-review workflow from .navig/store/workflows"
```

Workflows in `.navig/store/workflows/` are playbooks the space's agents follow step by step;
steps marked `manual: true` are done by you.

### Open an incident
```
@incident-commander open --severity high --title "Database connection pool exhausted"
```

### Check certificate expiry
```
navig skill run cert-check --alert-days 30
```

---

## Documentation

- [Agent Guide](.navig/wiki/agent-guide.md)
- [Runbooks](.navig/wiki/runbooks.md)
- [Architecture](.navig/wiki/architecture.md)

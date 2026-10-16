# DevOps Space Architecture

## Design Decisions

| Date | Decision | Rationale |
|------|-----------|-----------|
| 2026-03-11 | Incident Commander is always lead for incident-response formation | Single decision-maker reduces incident chaos |
| 2026-03-11 | Terraform state in remote backend (stub) | Local state is dangerous for team use |
| 2026-03-11 | All deploys gated by health probe | Prevents deploying on top of existing failure |
| 2026-03-11 | Weekly reliability review scheduled Monday 09:00 UTC | Start-of-week prevents toil accumulation |
| 2026-03-11 | cert-check runs in weekly review AND on-demand | Certificates expire silently — double coverage |

## Space Layout

```
devops-space/
├── .navig/                               ← Runtime config, agents, formations, skills
├── ci-cd/                                ← Pipeline templates and workflow files
├── infrastructure-as-code/
│   ├── terraform-starter/                ← Terraform module starter
│   └── ansible-starter/                  ← Ansible playbook starter
├── monitoring/                           ← Prometheus rules, Grafana dashboards
└── runbooks/                             ← Operational runbooks (human-readable)
```

## Alert Severity Levels

| Level | Response Time | Formation | Pager? |
|-------|-------------|-----------|--------|
| Critical | Immediate | incident-response | Yes |
| High | 15 min | incident-response | Yes |
| Medium | 4 h | sre-ops | No |
| Low | Next business day | sre-ops | No |

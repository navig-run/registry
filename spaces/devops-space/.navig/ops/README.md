# Ops — devops-space

Operational reference for the DevOps space.

## Runbook Index

| ID | Runbook | Trigger |
|----|---------|---------|
| RB-001 | Deploy check | Pre-deployment gate |
| RB-002 | Incident triage | Alert received |
| RB-003 | Certificate renewal | cert-check alert |
| RB-004 | Terraform state lock recovery | Failed apply |
| RB-005 | Weekly reliability review | Monday 09:00 |

## Agent Inbox Reference

| Inbox | Agent | Priority |
|-------|-------|----------|
| #pipeline | pipeline-engineer | normal |
| #infra | infra-architect | normal |
| #incidents | incident-commander, site-reliability | **HIGH** |
| #sre | site-reliability | normal |
| #alerts | incident-commander, site-reliability | **HIGH** |

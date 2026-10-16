---
id: deploy-runbook
name: Deploy Runbook
description: Structured pre/post-deploy checklist and rollback plan for any service deployment
category: operations
version: 1.0.0
license: MIT
---

# Deploy Runbook

Use this prompt to produce a step-by-step deploy guide, health checks, and rollback
plan for any service. Fill in the placeholders or let NAVIG infer them from context.

---

## Prompt

```
You are a senior site reliability engineer running a deployment for:

- Service: {{service_name}}
- Environment: {{environment}}   # staging | production | canary
- Change summary: {{change_summary}}
- Deployment method: {{method}}  # helm | docker compose | systemd | direct | k8s

Produce a structured runbook with these sections:

### 1. Pre-Deploy Checklist
- [ ] Confirm current health baseline (include the command to capture it)
- [ ] Verify {{environment}} config is pinned to the correct version
- [ ] Confirm no active incidents affecting dependent services
- [ ] Snapshot current state (DB dump if applicable, tag current image/commit)
- [ ] Notify stakeholders if this is a user-facing change

### 2. Deploy Steps
Numbered, specific shell commands for {{method}}. Include exact syntax, not pseudocode.

### 3. Health Checks
After each critical step, provide the exact command to verify success.
Target indicators: HTTP 200 on /health, expected log lines, DB connectivity.

### 4. Smoke Tests
Three specific end-to-end checks the operator should run within 5 minutes of deploy.

### 5. Rollback Plan
If smoke tests fail or error rate exceeds 1%:
- Exact rollback commands
- Expected time-to-restore
- Who to notify

### 6. Post-Deploy
- [ ] Update deployment log (date, version, operator)
- [ ] Close related tickets / merge PR
- [ ] Schedule follow-up monitoring window

Keep all commands copy-pasteable. Mark any destructive step with ⚠️.
```

---

## Usage

Import the library once (from a clone of this repository), then fill and copy a prompt with `navig prompts use`:

```bash
navig prompts import library/prompts   # once

navig prompts use deploy-runbook \
  --var service_name="api-gateway" \
  --var environment="production" \
  --var change_summary="Upgrade from v2.4 to v2.5 — new rate limiting middleware" \
  --var method="docker compose"
```

Or open it in the NAVIG chat and fill the variables conversationally.

---

## Tips

- Run this prompt **before** every production deployment, not during
- Combine with `navig skill run system-health vitals` to capture baseline automatically
- Save the output to `.navig/plans/deploys/YYYY-MM-DD-<service>.md`

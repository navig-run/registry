# Incident Runbook

## Purpose
Generate a structured incident response runbook for a specific failure mode.
Used by the Incident Commander agent.

## Variables
- `{{INCIDENT_TYPE}}` — e.g. `database-connection-pool-exhausted`, `high-error-rate`, `disk-full`, `memory-leak`
- `{{SERVICE}}` — affected service name
- `{{SEVERITY}}` — `critical`, `high`, `medium`, `low`
- `{{ON_CALL_ROLE}}` — primary on-call role (e.g. `backend-engineer`, `dba`, `sre`)
- `{{ESCALATION_PATH}}` — comma-separated escalation chain

## Prompt

You are an experienced site reliability engineer writing a runbook.

Incident type: {{INCIDENT_TYPE}}
Service: {{SERVICE}}
Severity: {{SEVERITY}}
Primary on-call: {{ON_CALL_ROLE}}
Escalation: {{ESCALATION_PATH}}

Produce a runbook in this structure:

---
# Runbook: {{INCIDENT_TYPE}} — {{SERVICE}}

**Severity:** {{SEVERITY}}
**Last updated:** [DATE]
**Owner:** {{ON_CALL_ROLE}}

## Symptoms
[What the on-call engineer will see: alerts, user reports, dashboards]

## Immediate Triage (first 5 minutes)
1. [Check X]
2. [Run Y]
3. [Confirm Z]

## Diagnosis Steps
[Ordered steps to identify root cause. Each step includes: what to check, expected vs. actual, command or dashboard link]

## Mitigation Options
| Option | Impact | Time to execute | Risk |
|--------|--------|----------------|------|

## Resolution Steps
[Definitive fix steps — only execute after mitigation is in place]

## Validation
[How to confirm the incident is resolved]

## Escalation
Escalate to {{ESCALATION_PATH}} if:
- [Condition 1]
- [Condition 2]

## Post-Incident
- [ ] File postmortem within 24h
- [ ] Update this runbook if steps were wrong

---

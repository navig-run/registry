# Alert Triage

## Purpose
Analyse an incoming alert and produce a structured triage report — likely cause,
urgency assessment, and recommended first actions.

## Variables
- `{{ALERT_NAME}}` — name of the alert rule
- `{{ALERT_BODY}}` — full alert message or Prometheus/Datadog alert payload (JSON or plain text)
- `{{SERVICE}}` — affected service
- `{{ENVIRONMENT}}` — `prod`, `staging`, `dev`
- `{{TIME}}` — alert trigger time (ISO 8601)

## Prompt

You are an on-call site reliability engineer receiving a production alert.

Alert: {{ALERT_NAME}}
Service: {{SERVICE}}
Environment: {{ENVIRONMENT}}
Time: {{TIME}}
Alert body:
```
{{ALERT_BODY}}
```

Produce a triage report:

---
## Alert Triage — {{ALERT_NAME}}

**Service:** {{SERVICE}} | **Environment:** {{ENVIRONMENT}} | **Time:** {{TIME}}

### Immediate Assessment
- **Urgency:** [P1 / P2 / P3 / P4] — explain why
- **User impact:** [None / Degraded / Partial outage / Full outage]
- **Likely cause:** [Most probable root cause based on alert content]

### First 3 Actions
1.
2.
3.

### Relevant Runbooks
- [Link or name of applicable runbook]

### Escalate if
- [Condition that requires escalation]

### Can this wait until business hours?
[Yes / No — reasoning]

---

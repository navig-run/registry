# Incident Response

## Purpose
Structured incident triage and resolution prompt. Walk through a reproducible
incident response process: detect, scope, contain, mitigate, and document.
Ensures every incident produces a written record in the space wiki/memory.

## Variables
- `{{INCIDENT_TITLE}}` — Short description: e.g. "GPU overheating on homelab-01"
- `{{DETECTED_BY}}` — Who/what detected the incident: agent name, user, or monitoring alert
- `{{DETECTED_AT}}` — ISO timestamp
- `{{AFFECTED_HOSTS}}` — Comma-separated list of affected IPs or hostnames
- `{{INITIAL_SYMPTOMS}}` — What was observed when incident was detected

## Prompt

You are NAVIG Sentinel managing an active incident in the homelab space.

**Incident**: `{{INCIDENT_TITLE}}`
**Detected by**: `{{DETECTED_BY}}` at `{{DETECTED_AT}}`
**Affected hosts**: `{{AFFECTED_HOSTS}}`
**Initial symptoms**: `{{INITIAL_SYMPTOMS}}`

Execute the response playbook in sequence:

---

### T+0 — Immediate Triage (target: < 5 minutes)
1. Confirm the incident is real (rule out false positive)
2. Classify severity:
   - 🔴 **P1 Critical** — data loss risk, system down, security breach
   - 🟠 **P2 High** — significant degradation, hardware at risk
   - 🟡 **P3 Medium** — performance issue, recoverable without urgency
   - 🟢 **P4 Low** — minor issue, can be scheduled
3. State: is this incident currently active or resolved?
4. Identify blast radius: how many hosts/services are affected?

---

### T+5 — Scoping
Run targeted diagnostics on `{{AFFECTED_HOSTS}}`:
- `diagnose-host` prompt (quick depth) on each host
- `port-audit` if network/security incident
- `gpu-health` if thermal/hardware incident
- Check space memory for prior occurrences of this symptom

---

### T+15 — Containment
State specific containment actions taken or recommended. For example:
- Isolate host from network (if security incident)
- Throttle workload on overheating GPU
- Kill rogue process
- Block offending IP at firewall

---

### T+30 — Mitigation
Describe root cause (confirmed or hypothesised) and mitigation steps applied.
If root cause unknown: list top 3 hypotheses ranked by probability.

---

### T+60 — Resolution Check
Confirm: are metrics back to normal? Is the system stable?
List any residual risk still present.

---

### Post-Incident Documentation
Produce a structured incident record:

```yaml
incident_id: "INC-<YYYYMMDD>-<SEQ>"
title: "{{INCIDENT_TITLE}}"
severity: P?
detected_at: "{{DETECTED_AT}}"
detected_by: "{{DETECTED_BY}}"
affected_hosts: [{{AFFECTED_HOSTS}}]
timeline:
  - time: "T+0"
    action: "..."
  - time: "T+..."
    action: "..."
root_cause: "..."
resolution: "..."
prevention: "..."
resolved_at: "<ISO_TIMESTAMP>"
documented_by: "sentinel"
```

Write this record to `.navig/memory/known-issues.json` (append to incidents array).
Update `runbooks.md` if a new runbook pattern was identified.

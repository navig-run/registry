# Security Brief

## Purpose
Generate a concise, human-readable security situation report for the homelab space.
Synthesises port audit, process investigation, authentication logs, and network scan
into a single actionable brief — suitable for daily review or incident awareness.

## Variables
- `{{PORT_AUDIT_DATA}}` — Output from `port-audit` skill (JSON/text)
- `{{PROCESS_DATA}}` — Output from `process-investigate` skill
- `{{AUTH_LOG_SNIPPET}}` — Last 50 lines of auth log (or Windows Security Event log)
- `{{SCAN_DATE}}` — ISO timestamp of when data was collected
- `{{SCOPE}}` — Hosts covered: `all` or comma-separated IPs

## Prompt

You are NAVIG Sentinel producing the daily security brief for the homelab space.

Data collected: `{{SCAN_DATE}}` | Scope: `{{SCOPE}}`

**Port Audit Data:**
```
{{PORT_AUDIT_DATA}}
```

**Suspicious Process Data:**
```
{{PROCESS_DATA}}
```

**Auth Log Snippet:**
```
{{AUTH_LOG_SNIPPET}}
```

Produce a security brief in the following structure:

### 🟢/🟡/🔴 Overall Security Posture
One sentence verdict with colour indicator. Choose:
- 🟢 **Clean** — no significant findings
- 🟡 **Monitor** — anomalies present, not yet confirmed threats
- 🔴 **Action Required** — confirmed or strongly suspected security event

### Open Ports Summary
Table of all open ports found across scope. Flag with:
- ⚠️ **Unnecessary** — standard service that should be closed in this environment
- 🚨 **High Risk** — telnet (23), FTP (21), RDP (3389) exposed externally, SMB (445) exposed
- ✅ **Expected** — port is documented and expected

### Process Anomalies
List any processes flagged as suspicious:
- Unknown executables in temp directories
- Processes with unusually high CPU/RAM
- Network connections to unexpected external IPs
- Processes running as root/SYSTEM unexpectedly

### Authentication Events
- Failed login attempts: count, source IPs, targeted accounts
- Successful logins from unexpected IPs or times
- Any privilege escalation events

### Threat Assessment
Rate each finding: **Low / Medium / High / Critical**
For each High/Critical: provide recommended immediate action.

### Recommended Actions (Prioritised)
Numbered list, most urgent first. Be specific: which host, which port/process/account.

### Next Brief
Schedule: recommend when to re-run this brief based on current posture.

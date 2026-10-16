# Weekly Ops Review

## Purpose
Comprehensive weekly infrastructure review. Aggregates agent reports, summarises
the week's incidents, hardware trending, security posture, and config changes.
Produces a dated wiki entry ready to archive in the space's operational history.

## Variables
- `{{WEEK_ENDING}}` — ISO date of the Sunday ending this review week
- `{{INCIDENTS_THIS_WEEK}}` — Count and titles (from known-issues.json)
- `{{HARDWARE_REPORT}}` — Output from `hardware-report` prompt
- `{{SECURITY_BRIEF}}` — Output from `security-brief` prompt
- `{{DEVICE_CHANGES}}` — Devices added/removed/modified this week
- `{{CONFIG_CHANGES}}` — Config sync changes from Archivist log

## Prompt

You are NAVIG compiling the weekly operations review for the homelab space.

**Week ending**: `{{WEEK_ENDING}}`

Use the provided data to produce a comprehensive weekly report.

---

### 📊 Week at a Glance
Produce a one-table dashboard:

| Category | Metric | Status |
|---|---|---|
| Incidents | `{{INCIDENTS_THIS_WEEK}}` | 🟢/🟡/🔴 |
| Hardware Alerts | count | 🟢/🟡/🔴 |
| Security Findings | count | 🟢/🟡/🔴 |
| Devices Online | X / Y registered | 🟢/🟡/🔴 |
| Config Drift | files changed | 🟢/🟡/🔴 |
| Disk Health | all SMART pass? | 🟢/🔴 |

---

### 🚨 Incidents This Week
For each incident in `{{INCIDENTS_THIS_WEEK}}`:
- ID, title, severity, resolution status, time-to-resolve

If zero incidents: "✅ No incidents this week."

---

### 🖥️ Hardware Health Summary
Summarise from `{{HARDWARE_REPORT}}`:
- Any hosts with degraded hardware
- GPU or disk components approaching end-of-life
- Trending metrics (GPU temps rising week-over-week?)

---

### 🔒 Security Posture
Summarise from `{{SECURITY_BRIEF}}`:
- Open findings from the week
- Any ports newly opened or closed
- Authentication anomalies

---

### 🗂️ Configuration Changes
Summarise from `{{CONFIG_CHANGES}}`:
- Dotfiles modified on which hosts
- New packages installed
- Any unexpected config drift flagged

---

### 📦 Device Registry Changes
List from `{{DEVICE_CHANGES}}`:
- Devices added (name, IP, role)
- Devices removed or status changed
- Devices that went offline unexpectedly

---

### ✅ Completed This Week
List of completed tasks, resolved incidents, and shipped improvements.

---

### 📋 Next Week Priorities
Top 5 items for next week based on this review. Be specific: which host, which agent, which action.

---

### 📁 Archive Entry
Produce the final summary block to write as a wiki entry:

**File**: `.navig/wiki/history/ops-review-{{WEEK_ENDING}}.md`
**Content**: This full report, formatted as a dated wiki page.

Instruct Archivist to write this entry.

---

### Checklist Completion
Confirm all items reviewed:
- [ ] All registered hosts checked for online status
- [ ] Hardware health data is <24h old
- [ ] Security brief data is <24h old  
- [ ] All open P1/P2 incidents formally resolved or escalated
- [ ] Device registry matches physical reality
- [ ] Next week's priorities documented

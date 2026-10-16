# Weekly IoT Review

## Purpose
Comprehensive weekly review of the smart-home mesh. Aggregates agent reports and
summarises the week's device changes, telemetry trends, firmware posture, security
findings, and automation health. Produces a dated wiki entry for the operational history.

## Variables
- `{{WEEK_ENDING}}` — ISO date of the Sunday ending this review week
- `{{DEVICE_CHANGES}}` — Devices added/removed/changed this week
- `{{TELEMETRY_TREND}}` — Energy + battery trend from `sensor` snapshots
- `{{FIRMWARE_STATUS}}` — Output from the firmware audit
- `{{SECURITY_BRIEF}}` — Output from `security-segmentation-brief`
- `{{AUTOMATION_STATUS}}` — Output from the automation review
- `{{INCIDENTS_THIS_WEEK}}` — Count and titles from `known-issues.json`

## Prompt

You are NAVIG compiling the weekly IoT review for the iot space.

**Week ending**: `{{WEEK_ENDING}}`

Use the provided data to produce a comprehensive weekly report.

---

### 📊 Week at a Glance
Produce a one-table dashboard:

| Category | Metric | Status |
|---|---|---|
| Incidents | `{{INCIDENTS_THIS_WEEK}}` | 🟢/🟡/🔴 |
| Devices Online | X / Y registered | 🟢/🟡/🔴 |
| Low Batteries | count | 🟢/🟡/🔴 |
| Firmware Drift | devices behind | 🟢/🟡/🔴 |
| Security Findings | count | 🟢/🟡/🔴 |
| Segmentation | isolation holding? | 🟢/🔴 |
| Automations | passing dry-run? | 🟢/🟡/🔴 |

---

### 🚨 Incidents This Week
For each incident in `{{INCIDENTS_THIS_WEEK}}`: ID, title, severity, resolution status,
time-to-resolve. If zero: "✅ No incidents this week."

---

### 📦 Device Registry Changes
From `{{DEVICE_CHANGES}}`:
- Devices added (name, protocol, type, location)
- Devices removed or status changed
- Devices that went offline unexpectedly (exclude sleepy Zigbee)

---

### 🔋 Telemetry & Energy Trend
Summarise from `{{TELEMETRY_TREND}}`:
- Total energy for the week vs previous week
- Batteries approaching replacement (predicted date)
- Any device with abnormal readings or offline gaps

---

### 🔧 Firmware Posture
Summarise from `{{FIRMWARE_STATUS}}`:
- Devices behind the latest release
- CVE exposure and whether an OTA rollout is scheduled

---

### 🔒 Security Posture
Summarise from `{{SECURITY_BRIEF}}`:
- Segmentation status, any default-credential findings, rogue devices

---

### 🤖 Automation Health
Summarise from `{{AUTOMATION_STATUS}}`:
- Entity drift (orphans / unexposed), scenes that failed dry-run, new automations added

---

### ✅ Completed This Week
Completed tasks, resolved incidents, shipped automations.

---

### 📋 Next Week Priorities
Top 5 items. Be specific: which device, which agent, which action.

---

### 📁 Archive Entry
**File**: `.navig/wiki/history/iot-review-{{WEEK_ENDING}}.md`
**Content**: this full report, formatted as a dated wiki page. Instruct the space to write it.

---

### Checklist Completion
- [ ] All registered devices checked for online status
- [ ] Telemetry data is <24h old
- [ ] Firmware audit is <7d old
- [ ] Security brief is <24h old
- [ ] All open P1/P2 incidents resolved or escalated
- [ ] Device registry matches physical reality
- [ ] Next week's priorities documented

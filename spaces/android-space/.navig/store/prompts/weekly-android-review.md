# Weekly Android Review

## Purpose
Comprehensive weekly review of the Android fleet. Aggregates agent reports,
summarizes the week's device changes, battery/storage trends, security-patch drift,
privacy findings, and backup status. Produces a dated wiki entry ready to archive.

## Variables
- `{{WEEK_ENDING}}` — ISO date of the Sunday ending this review week
- `{{FLEET_REPORT}}` — Output from the latest `fleet-audit` / `device-inventory`
- `{{BACKUP_STATUS}}` — Result from the week's `nightly-backup` runs
- `{{PRIVACY_FINDINGS}}` — Output from `permission-audit` / `debloat-sweep`
- `{{DEVICE_CHANGES}}` — Devices added/removed/reassigned this week

## Prompt

You are NAVIG compiling the weekly Android review for the android space.

**Week ending**: `{{WEEK_ENDING}}`

Use the provided data to produce a comprehensive weekly report.

---

### 📊 Week at a Glance

| Category | Metric | Status |
|---|---|---|
| Devices online | X / Y registered | 🟢/🟡/🔴 |
| Security patch drift | # devices behind | 🟢/🟡/🔴 |
| Battery health alerts | count | 🟢/🟡/🔴 |
| Privacy findings | over-privileged apps | 🟢/🟡/🔴 |
| Backups | all verified? | 🟢/🔴 |
| Storage | any device >90% full? | 🟢/🟡/🔴 |

---

### 📱 Fleet Status
Summarize from `{{FLEET_REPORT}}`:
- Devices online vs. registered; any that went offline.
- Android versions and security-patch levels — flag anything more than 2 patch cycles behind.
- Storage headroom per device; flag anything under 10% free.

---

### 🔋 Battery & Health Trends
- Devices with degraded battery health or high temperature.
- Any device trending worse week-over-week.

---

### 🔒 Privacy & Debloat
Summarize from `{{PRIVACY_FINDINGS}}`:
- New over-privileged apps this week.
- Bloat removed (and anything restored).
- Highest-priority revoke recommendation.

---

### 💾 Backup Status
Summarize from `{{BACKUP_STATUS}}`:
- Which devices backed up and verified successfully.
- Any failed or truncated backup — this is a 🔴 until resolved.
- Media byte counts vs. previous week.

---

### 📦 Device Registry Changes
From `{{DEVICE_CHANGES}}`:
- Devices added (name, model, role).
- Devices removed, reassigned, or retired.

---

### ✅ Completed This Week
Resolved issues, debloat passes, migrations, shipped improvements.

---

### 📋 Next Week Priorities
Top 5 items — be specific: which device, which agent, which action.

---

### 📁 Archive Entry
Produce the final summary block to write as a wiki entry:
**File**: `.navig/wiki/history/android-review-{{WEEK_ENDING}}.md`
Instruct Pixel to write this entry.

### Checklist
- [ ] All registered devices checked for online status
- [ ] Security-patch drift assessed
- [ ] Battery health data <24h old
- [ ] All backups for the week verified
- [ ] Privacy findings triaged
- [ ] Device registry matches physical reality
- [ ] Next week's priorities documented

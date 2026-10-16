---
id: morning-briefing
name: Morning Briefing
description: Concise morning ops status — systems, network, containers, and one actionable priority
category: productivity
version: 1.1.0
license: MIT
---

# Morning Briefing

Kick off each work session with a fast, data-driven status check. When bound to a space,
NAVIG auto-collects skill data before running this prompt.

---

## Prompt

```
You are a concise ops analyst. The operator is starting a new work session.

--- Available data (inject if present) ---
System vitals: {{system_health_vitals}}   # from: navig skill run system-health vitals --json
Network scan: {{network_scan}}            # from: navig skill run network-scan scan --json
Docker status: {{docker_ps}}             # from: navig skill run docker-ops ps --all --json
Open tasks: {{open_tasks}}               # optional: paste from your task manager

--- Briefing format ---

Generate a morning briefing in exactly this structure:

### 🖥 System
One sentence covering CPU, memory, disk. Flag anything above 85% in **bold**.

### 🌐 Network
New or unexpected devices since yesterday? Any host that was up and is now down?
If no scan data: state that and offer to run one.

### 🐳 Containers
Any stopped, unhealthy, or restarting containers? If all healthy: "All containers healthy."

### ✅ Top Priority
Single most important action to take right now based on the data above.
One sentence. Specific. Actionable.

---
Keep the entire briefing under 200 words. End with:
*"Ready. What shall we tackle first?"*

If any data source is unavailable, note it and offer to collect it.
```

---

## Usage

Import the library once (from a clone of this repository), then fill and copy a prompt with `navig prompts use`:

```bash
navig prompts import library/prompts   # once

# Data-rich: pre-collect skill output and inject
VITALS=$(navig skill run system-health vitals --json)
DOCKER=$(navig skill run docker-ops ps --all --json)

navig prompts use morning-briefing \
  --var system_health_vitals="$VITALS" \
  --var docker_ps="$DOCKER"
```

Or simply open NAVIG chat in the morning — if you have a space active with `system-health`
and `docker-ops` bound, NAVIG collects the data automatically before running the briefing.

---

## Automate It

Schedule to run at startup or at a fixed time:

```bash
navig cron add morning-briefing "0 8 * * 1-5" "navig prompts use morning-briefing --no-copy"   # Mon-Fri 8 AM
```

Output will be delivered to your configured notification channel.

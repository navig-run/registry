# Workstation — NAVIG Space Example

A general-purpose space for a local developer workstation or homelab node. Provides
ambient system monitoring, network awareness, Docker oversight, and a daily briefing.

---

## What's included

**Formation:** `homelab-node`

| Agent | Role |
|-------|------|
| **Homelab Ops** | Hands-on exec agent — Docker, files, system commands |
| **Security Guardian** | Passive sentinel — monitors for suspicious activity 24/7 |
| **Daily Chronicler** | 8 PM digest — summarises the day and recommends tomorrow's priority |

**Skills:** `system-health` · `network-scan` · `docker-ops` · `security-audit`  
**Prompts:** `morning-briefing` · `weekly-review`

---

## Quickstart

```bash
# 1. Copy into your home config
cp space.json ~/.navig/spaces/workstation/space.json

# 2. Activate
navig space use workstation

# 3. Morning check-in
navig prompts use morning-briefing

# 4. On-demand health check
navig skill run system-health vitals
navig skill run network-scan scan
```

---

## Configuration

Edit `space.json` to customise:

| Field | Purpose |
|-------|---------|
| `context.os` | `linux` · `mac` · `windows` — affects command templates |
| `vault_keys.telegram_bot_token` | Enable alert and briefing delivery to Telegram |

```bash
navig vault set telegram_bot_token YOUR_TOKEN
```

---

## Legacy note

`space.manifest.json` is the original format from v1.x. The canonical format is
`space.json` with `"kind": "space"` (used by this directory).

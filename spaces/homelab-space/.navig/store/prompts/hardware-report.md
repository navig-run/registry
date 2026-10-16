# Hardware Report

## Purpose
Produce a structured hardware health summary for all registered hosts in the space.
Uses data collected by the `pulse` agent via `gpu-health` and `hardware-inventory` skills.
Suitable for weekly review, pre-workload capacity checks, or post-incident analysis.

## Variables
- `{{HARDWARE_DATA}}` — JSON output from `hardware-inventory` skill across all hosts
- `{{GPU_DATA}}` — JSON output from `gpu-health` skill
- `{{SMART_DATA}}` — SMART disk data (from `smartctl -a` or equivalent)
- `{{REPORT_DATE}}` — ISO date
- `{{HOSTS}}` — List of hostnames/IPs covered

## Prompt

You are NAVIG Pulse generating the hardware health report for the homelab space.

Report date: `{{REPORT_DATE}}` | Hosts: `{{HOSTS}}`

**Hardware Inventory Data:**
```json
{{HARDWARE_DATA}}
```

**GPU Health Data:**
```json
{{GPU_DATA}}
```

**Disk SMART Data:**
```
{{SMART_DATA}}
```

Produce the following report:

### Hardware Roster
| Host | CPU | Cores | RAM | GPU | Primary Storage |
|---|---|---|---|---|---|
(populate from inventory data)

### GPU Health Summary
| Host | GPU Model | Utilisation | VRAM Used | Temp °C | Status |
|---|---|---|---|---|---|
Flag: 🟡 Warning (>80°C / >90% VRAM) | 🔴 Critical (>85°C / errors) | ✅ Healthy

### Disk Health Summary
| Host | Drive | Model | Size | SMART Status | Reallocated Sectors | Hours |
|---|---|---|---|---|---|---|
Flag: 🔴 SMART FAILED or reallocated_sectors > 10 | 🟡 Pre-fail attributes | ✅ Passed

### Thermal Overview
| Host | CPU Temp | GPU Temp | Fan Status | Verdict |
|---|---|---|---|---|

### Memory Pressure
| Host | Total RAM | Used | Free | Swap Used | Verdict |
|---|---|---|---|---|---|
Flag hosts where available RAM < 10% or swap > 50%.

### Capacity Summary
Overall capacity narrative: what headroom exists, what is at risk, what needs upgrading.

### Action Items
List hardware-related actions with priority:
- 🔴 Immediate: hardware approaching failure or already degraded
- 🟡 Soon: components above comfortable thresholds
- 🟢 Scheduled: routine replacements or upgrades to plan

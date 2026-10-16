# Homelab Ops

Operational runbooks and automation scripts for the homelab. This folder mirrors the intent of `scripts/` but focuses on **runbooks** (decision-tree procedures) rather than raw tooling.

## Relationship to `scripts/`

| Folder | Purpose |
|--------|---------|
| `ops/` | Runbooks, checklists, incident procedures, SOP docs |
| `scripts/` | Raw PowerShell/Bash helper tooling |

Cross-reference: runbooks here link out to the scripts they invoke.

---

## Runbook Index

| Runbook | Trigger | Status |
|---------|---------|--------|
| [Onboard Device](../../docs/runbooks/README.md) | New hardware joins network | → `scripts/` + `.navig/store/workflows/onboard-device.yaml` |
| [Incident Response](../store/prompts/incident-response.md) | Service/host failure | → `.navig/store/prompts/incident-response.md` |
| [Morning Sweep](../store/workflows/morning-sweep.yaml) | Daily 08:00 | → workflow |
| [Nightly Sync](../store/workflows/nightly-sync.yaml) | Daily 23:00 | → workflow |
| [Weekly Review](../store/workflows/weekly-review.yaml) | Monday | → workflow |
| [Deep Audit](../store/workflows/deep-audit.yaml) | On-demand | → workflow |
| [Cable Map Update](../store/workflows/cable-map-update.yaml) | After physical changes | → workflow |

---

## Agents & Formations

Homelab agents are defined in `.navig/store/agents/`. Active formation for most ops: `network-ops`.

```
atlas      → Infrastructure cartographer
sentinel   → Security and anomaly watcher
wrench     → Maintenance automator
herald     → Cross-platform command translator
archivist  → Config and knowledge keeper
pulse      → Hardware health monitor
```

---

## Quick Links

- **Device registry:** `.navig/memory/device-registry.json`
- **Network topology:** `.navig/wiki/network-topology.md`
- **Cable log:** `.navig/wiki/cable-log.md`
- **Known issues:** `.navig/memory/known-issues.json`
- **Skills:** `.navig/skills/` (11 automation skills)

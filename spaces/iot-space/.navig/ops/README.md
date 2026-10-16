# IoT Ops

Operational runbooks and automation for the smart-home mesh. This folder mirrors the intent of `scripts/` but focuses on **runbooks** (decision-tree procedures) rather than raw tooling.

## Relationship to `scripts/`

| Folder | Purpose |
|--------|---------|
| `ops/` | Runbooks, checklists, incident procedures, SOP docs |
| `scripts/` | Raw PowerShell/Bash tooling — discovery helpers, MQTT dumps |

Cross-reference: runbooks here link out to the scripts they invoke.

---

## Runbook Index

| Runbook | Trigger | Status |
|---------|---------|--------|
| [Device Onboarding](../wiki/runbooks.md) | New device joins the mesh | → `.navig/store/workflows/device-onboard.yaml` |
| [Firmware Rollout](../store/prompts/firmware-update-plan.md) | Version drift / CVE | → `.navig/store/prompts/firmware-update-plan.md` |
| [Morning Mesh Sweep](../store/workflows/morning-mesh-sweep.yaml) | Daily 07:00 | → workflow |
| [Nightly Telemetry Sync](../store/workflows/nightly-telemetry-sync.yaml) | Daily 01:00 | → workflow |
| [Security Review](../store/workflows/security-review.yaml) | Sunday 03:00 | → workflow |
| [Firmware Audit](../store/workflows/firmware-audit.yaml) | On-demand | → workflow |
| [Automation Review](../store/workflows/automation-review.yaml) | On-demand | → workflow |

---

## Agents & Formations

IoT agents are defined in `.navig/store/agents/`. Active formation for most ops: `discovery-sweep`.

```
beacon   → Device discovery cartographer
broker   → Message bus operator
warden   → Security and segmentation watcher
flux     → Firmware and OTA manager
automa   → Automation and scene orchestrator
sensor   → Telemetry and health monitor
```

---

## Quick Links

- **Device registry:** `.navig/memory/device-registry.json`
- **MQTT topics:** `.navig/wiki/mqtt-topics.md`
- **Segmentation:** `.navig/wiki/segmentation.md`
- **Known issues:** `.navig/memory/known-issues.json`
- **Skills:** `.navig/skills/` (12 automation skills)

# Android Ops

Operational runbooks and automation for the Android device fleet. This folder mirrors the intent of `scripts/` but focuses on **runbooks** (decision-tree procedures) rather than raw tooling.

## Relationship to `scripts/`

| Folder | Purpose |
|--------|---------|
| `ops/` | Runbooks, checklists, incident procedures, SOP docs |
| `scripts/` | Raw PowerShell/Bash tooling — pairing helpers, batch debloat runners |

Cross-reference: runbooks here link out to the scripts they invoke.

---

## Runbook Index

| Runbook | Trigger | Status |
|---------|---------|--------|
| [Onboard Device](../../docs/runbooks/README.md) | New device joins the fleet | → `scripts/` + `.navig/store/workflows/new-device-onboard.yaml` |
| [Diagnose ADB](../store/prompts/diagnose-adb.md) | Device won't connect / unauthorized | → `.navig/store/prompts/diagnose-adb.md` |
| [Morning Device Check](../store/workflows/morning-device-check.yaml) | Daily 08:00 | → workflow |
| [Nightly Backup](../store/workflows/nightly-backup.yaml) | Daily 02:00 | → workflow |
| [Debloat Sweep](../store/workflows/debloat-sweep.yaml) | On-demand | → workflow |
| [Fleet Audit](../store/workflows/fleet-audit.yaml) | On-demand | → workflow |
| [App Update Check](../store/workflows/app-update-check.yaml) | Weekly Mon 09:00 | → workflow |

---

## Agents & Formations

Android agents are defined in `.navig/store/agents/`. Active formation for most ops: `device-bridge`.

```
pixel      → Device cartographer / fleet inventory
bridge     → ADB bridge operator
installer  → App & APK operator
scrub      → Privacy & debloat warden
mirror     → Screen & control operator
keeper     → Backup & restore archivist
```

---

## Quick Links

- **Device registry:** `.navig/memory/device-registry.json` (copy from `device-registry.example.json`)
- **ADB / wireless-debug guide:** `.navig/wiki/adb-guide.md`
- **Debloat catalog:** `.navig/wiki/debloat-catalog.md`
- **Known issues:** `.navig/memory/known-issues.json` (copy from `known-issues.example.json`)
- **Skills:** `.navig/skills/` (12 automation skills)

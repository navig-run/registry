# Current Phase

> Last updated: 2026-07-10

## Active Goal

Bootstrap the android space and bring the first device online — connect over ADB, run the first fleet inventory, and populate the device registry with real data.

## In Progress

_Nothing in progress._

## Completed

- [x] Canonical space structure bootstrapped (`docs/`, `scripts/`, `tests/`, `tools/`)
- [x] 12 skills authored (adb-connect, device-inventory, apk-install, apk-extract, app-debloat, permission-audit, screen-mirror, logcat-capture, battery-report, file-transfer, wireless-debug, app-backup)
- [x] 6 agents + 5 formations defined
- [x] 6 workflows scheduled (morning-device-check, new-device-onboard, debloat-sweep, nightly-backup, app-update-check, fleet-audit)
- [x] 8 prompts authored
- [x] Tool packs created: `tools/platform-tools/pack.yaml` (adb + fastboot), `tools/scrcpy/pack.yaml`
- [x] Registered all skills/agents/formations/packages in the manifests

## Action Items

- [ ] **Install Android SDK Platform-Tools** from the Android developer site and confirm `adb version`
- [ ] **Install scrcpy** from its official release and confirm `scrcpy --version`
- [ ] **Confirm adb_path / scrcpy_path** in `.navig/config.yaml` match the real install locations
- [ ] **Connect the first device** — enable USB debugging, run `navig skill run adb-connect`, accept the RSA prompt
- [ ] **Run the first inventory** — `navig skill run device-inventory` and replace the example registry entries
- [ ] **Populate `debloat-catalog.md`** with safe-to-remove packages for your device OEMs
- [ ] **Enable wireless debugging** on the daily-driver so it's reachable without a cable

## Blocked

_Nothing blocked._

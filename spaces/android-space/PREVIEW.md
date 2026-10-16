# NAVIG Android Space

**Command hub for every Android device you own or manage.**

---

## What It Is

A production-grade NAVIG space for managing Android devices — phones, tablets, TV boxes —
from a single desktop on **Windows, Linux, or macOS**. ADB bridge, app & APK ops, fleet
inventory, reversible debloat, screen mirroring, and backup/restore, all wired up. Fork it,
connect a device, and you're operational in under 10 minutes.

---

## Key Features

- **12 ADB / scrcpy skills** — connect, inventory, install/extract APKs, debloat, permission audit, screen mirror, logcat, battery report, file transfer, wireless debug, backup
- **6 specialized agents** — pixel (fleet), bridge (adb), installer (apps), scrub (privacy), mirror (screen), keeper (backup)
- **6 automated workflows** — morning device check, new-device onboard, debloat sweep, nightly backup, app-update check, fleet audit
- **8 production prompts** — onboard device, debloat plan, diagnose adb, permission review, backup strategy, phone migration, logcat triage, weekly review
- **Safe by default** — debloat is reversible (`pm disable-user`), never touches `/system`, never needs root; fastboot writes are blocked by policy

---

## Usage Example

```bash
# Activate the space
navig space use android

# Connect a device (accept the RSA prompt on-screen)
navig skill run adb-connect

# Inventory the fleet
navig skill run device-inventory

# Full morning check (connect + inventory + battery + offline alert)
navig ask "run the morning-device-check workflow"

# Mirror and control the screen
navig skill run screen-mirror
```

---

**Platform**: Windows · Linux · macOS
**Category**: Mobile · Android · Devices
**Version**: 1.0.0
**License**: MIT

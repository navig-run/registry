# Scripts

Automation scripts for Android device operations.

## Contents

| Script | Purpose | Notes |
|--------|---------|-------|
| [pair-wireless.ps1](pair-wireless.ps1) | Interactive Android 11+ wireless-debugging pairing helper | Prompts for pair host/port + code, then connects on the debug port |
| [batch-debloat.ps1](batch-debloat.ps1) | Catalog-driven batch debloat runner | Dry-run by default. Reads a package list, disables each via `pm disable-user --user 0` |

## Wireless Pairing

`pair-wireless.ps1` walks the Android 11+ flow:
1. On the device: Developer options → Wireless debugging → **Pair device with pairing code**.
2. Enter the shown `IP:pairPort` and the 6-digit code when prompted.
3. The script runs `adb pair`, then `adb connect` on the debug port, and lists devices.

Works for the legacy tcpip path too (pass `-Tcpip` with a USB-connected device).

## Batch Debloat

`batch-debloat.ps1` disables a list of packages **reversibly** for user 0:
- Reads packages from `-PackageFile` (one per line) or a comma-separated `-Packages`.
- **Dry-run by default** — prints the exact commands; pass `-Execute` to actually run them.
- Only use packages you've vetted against `.navig/wiki/debloat-catalog.md`.
- Restore anything with `pm enable <pkg>` or `cmd package install-existing <pkg>`.

## Naming Convention

`<verb>-<noun>.<ext>` — e.g. `pair-wireless.ps1`, `batch-debloat.ps1`, `pull-media.sh`

## Script Header Template

```powershell
# PURPOSE:       <one-line description>
# USAGE:         .\<script-name>.ps1 [args]
# PREREQUISITES: <tools required, e.g. adb on PATH>
# REQUIRES:      <elevated | none>
```

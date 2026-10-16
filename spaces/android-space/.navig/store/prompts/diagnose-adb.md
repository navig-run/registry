# Diagnose ADB

## Purpose
Structured troubleshooting for a device that won't connect, shows `unauthorized`,
`offline`, or `no devices/emulators found`. Surfaces the most likely cause fast and
gives the exact fix command.

## Variables
- `{{SYMPTOM}}` — `not-detected`, `unauthorized`, `offline`, `wifi-drops`, or `multiple-devices`
- `{{OS}}` — Host OS: `windows`, `linux`, or `macos`
- `{{TRANSPORT}}` — `usb` or `wifi`

## Prompt

You are NAVIG Bridge diagnosing an ADB connectivity problem.
Symptom: `{{SYMPTOM}}` · Host: `{{OS}}` · Transport: `{{TRANSPORT}}`.

Work the checklist in order. Stop at the first fix that resolves the symptom.

### 1. Server sanity
```
adb kill-server && adb start-server
adb devices -l
```
If the device now shows `device`, you're done.

### 2. `unauthorized`
- Cause: the RSA fingerprint hasn't been accepted on the device.
- Fix: unlock the device, watch for the "Allow USB debugging?" dialog, tick
  "Always allow from this computer", tap Allow.
- If no dialog appears: toggle Developer options → USB debugging OFF then ON, and
  revoke USB debugging authorizations, then replug.

### 3. `not-detected` (no devices)
- Confirm **USB debugging** is enabled (Developer options).
- Confirm the cable is a **data** cable, not charge-only. Try another port/cable.
- Windows: check Device Manager for a missing/yellow ADB driver; install the OEM or
  Google USB driver. Confirm the USB mode on the phone is **File Transfer (MTP)**, not
  "Charging only".
- Linux: check `lsusb`; add a udev rule for the vendor ID if the device is present in
  `lsusb` but not `adb devices`.

### 4. `offline`
- Usually a stale daemon or a device that rebooted mid-session.
- Fix: `adb kill-server && adb start-server`, then replug. If wireless, `adb disconnect`
  then `adb connect <ip>:<port>` again.

### 5. `wifi-drops`
- The device left tcpip mode (reboot or Wi-Fi sleep).
- Re-run `wireless-debug --method tcpip` over USB, or re-`adb pair` on Android 11+.
- Ensure Wi-Fi "keep on during sleep" and that host + device share the same subnet.

### 6. `multiple-devices`
- Every command must target a serial: `adb -s <serial> <cmd>`.
- List serials with `adb devices -l` and pass `--serial` to skills.

### 7. Assessment
Summarize: most likely cause, the exact command that fixes it, and whether it worked.
Overall: 🟢 Connected / 🟡 Intermittent / 🔴 Still failing (with next escalation).

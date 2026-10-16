# ADB & Wireless Debugging Cheatsheet

**Space**: `android`
**Last Updated**: 2026-07-10
**Maintained by**: Bridge

> Quick reference for the ADB commands the skills wrap. Everything here is what `adb-connect`,
> `wireless-debug`, and `screen-mirror` run under the hood.

---

## Enable USB Debugging (one-time, on the device)

1. Settings → About phone → tap **Build number** 7 times to unlock Developer options.
2. Settings → System → **Developer options** → enable **USB debugging**.
3. Plug in over USB, set USB mode to **File Transfer (MTP)**, accept the RSA prompt.

---

## Core Commands

| Task | Command |
|---|---|
| List devices | `adb devices -l` |
| Restart daemon | `adb kill-server && adb start-server` |
| Target one device | `adb -s <serial> <cmd>` |
| Device state | `adb get-state` |
| Read a property | `adb shell getprop ro.build.version.release` |
| Open a shell | `adb shell` |
| Reboot | `adb reboot` |

---

## Wireless Debugging

### Path A — legacy tcpip (needs USB once)
```
adb tcpip 5555                     # switch the USB device to tcpip mode
adb shell ip route | grep wlan0    # find the device IP
adb connect 192.168.1.42:5555      # connect over Wi-Fi (now unplug USB)
```

### Path B — Android 11+ pairing (no cable)
```
# On device: Developer options → Wireless debugging → Pair device with pairing code
adb pair 192.168.1.42:37105        # host:pairPort  → enter the 6-digit code
adb connect 192.168.1.42:37000     # host:debugPort (the other number shown)
```

**Gotchas**: the device drops tcpip mode on reboot or Wi-Fi sleep — re-run the pairing/tcpip
step. Host and device must be on the same subnet. Enable "keep Wi-Fi on during sleep".

---

## Apps & Packages

| Task | Command |
|---|---|
| List third-party apps | `adb shell pm list packages -3` |
| List disabled apps | `adb shell pm list packages -d` |
| Install (keep data, grant) | `adb install -r -g app.apk` |
| Install split bundle | `adb install-multiple base.apk split_*.apk` |
| Find an app's APK path | `adb shell pm path com.example.app` |
| Uninstall (keep data) | `adb shell pm uninstall -k --user 0 com.example.app` |
| Disable (reversible) | `adb shell pm disable-user --user 0 com.example.app` |
| Restore disabled | `adb shell cmd package install-existing com.example.app` |
| Grant permission | `adb shell pm grant <pkg> android.permission.CAMERA` |

---

## Screen & Input

| Task | Command |
|---|---|
| Mirror + control | `scrcpy --max-size 1024 --video-bit-rate 8M` |
| View-only mirror | `scrcpy --no-control` |
| Screenshot | `adb exec-out screencap -p > shot.png` |
| Screen record | `adb shell screenrecord /sdcard/rec.mp4` then `adb pull` |
| Tap | `adb shell input tap 540 1200` |
| Swipe | `adb shell input swipe 300 1000 300 300` |
| Type text | `adb shell input text "hello"` |
| Key event (home) | `adb shell input keyevent KEYCODE_HOME` |

---

## Files, Logs, Health

| Task | Command |
|---|---|
| Pull a file | `adb pull /sdcard/file .` |
| Push a file | `adb push file /sdcard/` |
| Storage free | `adb shell df -h /data` |
| Battery | `adb shell dumpsys battery` |
| Logcat (errors) | `adb logcat *:E` |
| Clear log buffer | `adb logcat -c` |
| Full bugreport | `adb bugreport report.zip` |

---

## Danger Zone (fastboot — opt-in, high risk)

`fastboot` writes are **blocked by default** in the MCP policy. Bootloader unlocking and
firmware flashing can brick a device and void warranty — never run these without explicit
operator intent and a recovery plan.

```
adb reboot bootloader              # enter fastboot
fastboot devices                   # confirm the device
fastboot flashing unlock           # DANGEROUS — wipes the device
```

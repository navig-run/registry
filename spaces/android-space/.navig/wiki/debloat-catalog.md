# Debloat Catalog — Safe-to-Remove Packages

**Space**: `android`
**Last Updated**: 2026-07-10
**Maintained by**: Scrub

> The vetted list of packages `app-debloat` is allowed to disable without confirmation.
> Everything here is removed with a **reversible** per-user command
> (`pm disable-user --user 0` or `pm uninstall -k --user 0`) — nothing touches `/system`,
> nothing needs root, everything is restorable. **When in doubt, disable — don't uninstall.**
>
> ⚠️ **Never** disable telephony, IMS/RCS, SetupWizard, the package installer, the system
> UI, the launcher of last resort, or the store you actually use. Those are in the
> 🔴 Do-Not-Touch list at the bottom.

---

## How to use

```bash
# 1. See what's on a device
navig skill run app-debloat --action list

# 2. Dry-run a disable (safe — shows the command only)
navig skill run app-debloat --package <pkg>

# 3. Actually disable it
navig skill run app-debloat --package <pkg> --dry_run false

# 4. Restore anytime
navig skill run app-debloat --package <pkg> --action restore --dry_run false
```

---

## 🟢 Cross-OEM common bloat (usually safe)

| Package | What it is |
|---|---|
| `com.facebook.appmanager` | Preinstalled Facebook app manager |
| `com.facebook.system` | Facebook system stub |
| `com.facebook.services` | Facebook background services |
| `com.google.android.apps.tachyon` | Google Meet (Duo) — remove if unused |
| `com.google.android.videos` | Google TV / Play Movies |
| `com.google.android.play.games` | Play Games — remove if unused |

---

## 🟢 Samsung (One UI)

| Package | What it is |
|---|---|
| `com.samsung.android.bixby.agent` | Bixby voice assistant |
| `com.samsung.android.app.spage` | Bixby Home / Samsung Free page |
| `com.samsung.android.game.gamehome` | Game Launcher |
| `com.samsung.android.scloud` | Samsung Cloud (if you use Google backup) |
| `com.samsung.android.app.tips` | Samsung Tips |
| `com.samsung.android.aremoji` | AR Emoji |

---

## 🟢 Xiaomi (MIUI / HyperOS)

| Package | What it is |
|---|---|
| `com.miui.analytics` | MIUI analytics / telemetry |
| `com.miui.msa.global` | MIUI System Ads (MSA) |
| `com.xiaomi.mipicks` | GetApps store (if unused) |
| `com.miui.videoplayer` | Mi Video |
| `com.mi.globalbrowser` | Mi Browser |

---

## 🟢 OnePlus / Oppo (OxygenOS / ColorOS)

| Package | What it is |
|---|---|
| `com.heytap.market` | App Market (if unused) |
| `com.oneplus.brickmode` | Zen Mode |
| `com.coloros.gamespace` | Game Space |

---

## 🔴 Do NOT Touch (disabling these can brick or soft-lock the device)

| Package pattern | Why |
|---|---|
| `com.android.phone`, `com.android.server.telecom` | Telephony / calling |
| `com.android.ims`, `*.rcs*` | VoLTE / VoWiFi / RCS messaging |
| `com.google.android.setupwizard`, `com.android.provision` | First-boot setup |
| `com.android.packageinstaller`, `com.google.android.packageinstaller` | Installs apps |
| `com.android.systemui` | The entire system UI |
| `com.android.vending` | Play Store (if you use it) |
| `*.launcher*` (your active launcher) | Home screen |
| `com.google.android.gms`, `com.google.android.gsf` | Play Services / framework |

---

## Adding to this catalog

Only add a package after you have **confirmed on a test device** that disabling it does not
break calling, messaging, notifications, or boot. Record the OEM and the observed effect.
An unverified entry does not belong here.

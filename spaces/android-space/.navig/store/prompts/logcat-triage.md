# Logcat Triage

## Purpose
Turn a raw `adb logcat` dump into a clear triage: what crashed, why, which app/PID,
and the next diagnostic step. Cuts through the noise to the signal.

## Variables
- `{{DEVICE_SERIAL}}` — Target device serial
- `{{PACKAGE}}` — App package under investigation (blank = whole device)
- `{{ISSUE}}` — What's wrong: `crash`, `anr`, `battery-drain`, `network`, or `unknown`

## Prompt

You are NAVIG Bridge triaging logcat for `{{DEVICE_SERIAL}}`
(app: `{{PACKAGE}}`, issue: `{{ISSUE}}`).

### 1. Capture
Run `logcat-capture` scoped appropriately:
- For a crash/ANR: `--priority E` (and `--package {{PACKAGE}}` if known).
- Reproduce the issue once with `--clear_first true` so the buffer is clean.

### 2. Find the Signal
Scan the capture for, in priority order:
- **`FATAL EXCEPTION`** / `AndroidRuntime` → a crash. Grab the exception class, message,
  and the top 5 stack frames.
- **`ANR in`** → an Application Not Responding. Note the component and the "Reason".
- **`E ActivityManager`**, `Force finishing`, `Process ... has died` → lifecycle failures.
- **`OutOfMemoryError`**, `lowmemorykiller` → memory pressure.
- **`W`/`E` from the target package's tag** → app-specific errors.

### 3. Attribute
Resolve the offending PID to a package (`adb shell ps -A | grep <pid>` or `pidof`).
State clearly: which app, which component (Activity/Service/BroadcastReceiver).

### 4. Diagnosis
Explain in plain language what happened and the most likely root cause. Distinguish:
- App bug (exception in app code)
- OS/permission issue (SecurityException, missing permission)
- Resource issue (OOM, ANR from main-thread work)
- Environmental (network timeout, missing file, storage full)

### 5. Next Step
Give the single most useful next action:
- Re-run with a wider filter, grant a missing permission, clear app data, reinstall,
  or capture a `bugreport` for a deeper dive.

### Output
A short structured report: **Symptom → Evidence (log lines) → Attribution → Root cause → Next step**.
Put long raw log excerpts in a collapsible `<details>` block.

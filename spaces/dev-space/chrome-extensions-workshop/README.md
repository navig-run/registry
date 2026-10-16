# Chrome Extensions Workshop

A ready-to-go workspace for building, loading, and publishing Chrome/Firefox
Manifest V3 browser extensions.

---

## What Is a Manifest V3 Extension?

Manifest V3 (MV3) is the current Chrome/Edge extension architecture. It replaces
the persistent background page from MV2 with an event-driven **service worker**
that wakes up on demand. This makes extensions dramatically lighter but introduces
new patterns you need to understand.

---

## Quick Start — Load Locally in 2 Minutes

1. Edit `manifest.json` with your extension's name and permissions.
2. Open Chrome → `chrome://extensions`
3. Enable **Developer mode** (top-right toggle)
4. Click **Load unpacked** → select this `chrome-extensions-workshop/` folder
5. Your extension is now running. Edit files and click **↻ (reload)** in the extensions page to apply changes.

---

## MV3 Architecture

```
chrome-extensions-workshop/
├── manifest.json     ← Required. Declares everything the extension can do.
├── background.js     ← Service worker. Runs in the background, wakes on events.
├── content.js        ← Injected into matching web pages.
└── popup/
    ├── popup.html    ← UI shown when user clicks the extension icon.
    ├── popup.js      ← Popup logic.
    └── popup.css     ← Popup styles.
```

### How the Pieces Communicate

```
Popup ──── chrome.runtime.sendMessage ────► Background (service worker)
                                              │
Content ── chrome.runtime.sendMessage ────►  │
                                              │
Background ─ chrome.tabs.sendMessage ────► Content
```

All message passing is **async** and uses `chrome.runtime.sendMessage` /
`chrome.tabs.sendMessage` with `onMessage` listeners.

---

## Permissions Model

Only request permissions you actually use. The fewer permissions, the easier
CWS review and the more trust users give your extension.

| Permission | Use Case |
|-----------|----------|
| `activeTab` | Access the current tab URL/content on user gesture |
| `tabs` | Read/manipulate tabs beyond the active one |
| `storage` | Persist data with `chrome.storage.local` or `chrome.storage.sync` |
| `scripting` | Inject scripts into pages programmatically (MV3 replacement for `tabs.executeScript`) |
| `notifications` | Show desktop notifications |
| `alarms` | Schedule periodic background tasks |

**Never** request `<all_urls>` unless absolutely necessary — reviewers flag it.

---

## Service Worker Lifecycle

Service workers in MV3 are **not persistent**. They terminate after ~30 seconds
of inactivity and restart on the next event. Key implications:

- **Don't store state in global variables between events** — use `chrome.storage`.
- **Don't use long-running setInterval** — use `chrome.alarms` instead.
- **chrome.runtime.onInstalled** runs once on install/update — good for initial setup.

---

## CSP (Content Security Policy)

MV3 enforces a strict CSP. You cannot use:
- `eval()` or `new Function()` with dynamic strings — **never use `'unsafe-eval'`**
- Inline `<script>` tags in HTML pages — always load scripts via `<script src="...">` and `defer`
- Remote scripts — all JS must be bundled or in your extension package

---

## Common Errors and Fixes

| Error | Cause | Fix |
|-------|-------|-----|
| `Could not establish connection. Receiving end does not exist.` | Content script not yet injected on target tab | Check `@match` / `content_scripts.matches` in manifest |
| `Service worker registration failed` | Syntax error in `background.js` | Check service worker console (Extensions page → Inspect views: service worker) |
| `Refused to load script ... violates CSP` | Remote or inline script | Move all JS into bundled files |
| `Extension popup closes immediately` | Unhandled promise rejection in popup.js | Wrap async calls in try/catch |

---

## How to Debug

| Component | Open console via |
|-----------|-----------------|
| Popup | Right-click extension icon → Inspect Popup |
| Service worker | `chrome://extensions` → Inspect views: service worker |
| Content script | F12 on the target page → Console tab |

---

## Files in This Folder

| File | Description |
|------|-------------|
| `manifest.json` | Annotated MV3 manifest template |
| `background.js` | Service worker with message listener skeleton |
| `content.js` | Content script with messaging example |
| `popup/popup.html` | Popup UI (no inline scripts) |
| `popup/popup.js` | Popup logic |
| `popup/popup.css` | Popup styles |

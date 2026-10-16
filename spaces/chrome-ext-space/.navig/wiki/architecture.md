# Chrome Extension Architecture

Reference document covering the anatomy of Chrome extensions for reverse engineering and development.

---

## Manifest Versions

| Version | Status | Notes |
|---------|--------|-------|
| MV2 | Deprecated (enforcement 2024+) | Background pages, broad `webRequest` blocking |
| MV3 | Current | Background service workers, declarativeNetRequest, stricter CSP |

---

## Extension Component Map

```
extension/
├── manifest.json              ← Root definition (ALWAYS start here)
├── background/
│   ├── service_worker.js      ← MV3: persistent-less, event-driven
│   └── background.js          ← MV2: persistent background page
├── content_scripts/
│   └── *.js                   ← Injected into web pages per match pattern
├── popup/
│   ├── popup.html
│   └── popup.js               ← Runs in extension context, not page context
├── options/
│   ├── options.html
│   └── options.js
├── devtools/
│   ├── devtools.html
│   └── devtools.js            ← Access to chrome.devtools APIs
└── _locales/                  ← i18n message files
```

---

## manifest.json — Key Fields (RE Checklist)

```json
{
  "manifest_version": 3,
  "name": "...",
  "version": "...",
  "permissions": [],            // ← AUDIT: what APIs does it claim?
  "optional_permissions": [],   // ← Can be requested at runtime
  "host_permissions": [],       // ← URL patterns it can access
  "background": {
    "service_worker": "..."     // MV3
  },
  "content_scripts": [          // ← When/where scripts are injected
    {
      "matches": [],            // ← URL patterns
      "js": [],
      "run_at": "document_idle",
      "all_frames": false
    }
  ],
  "web_accessible_resources": [],  // ← Resources accessible from web pages
  "content_security_policy": {},   // ← CSP for extension pages
  "externally_connectable": {},    // ← Which sites can message the extension
  "storage": {}
}
```

---

## Execution Contexts

| Context | Access | Notes |
|---------|--------|-------|
| Service worker / background | Full Chrome APIs | No DOM access |
| Content script | Limited Chrome APIs + page DOM | Isolated JS world |
| Popup / Options page | Full Chrome APIs | Has DOM, short-lived |
| DevTools page | `chrome.devtools.*` | Inspected window access |
| Web page | None (extension APIs not available) | Communicates via `postMessage` |

---

## Message Passing (RE Focus)

```
Web page ←→ Content Script: window.postMessage / CustomEvent
Content Script ←→ Background: chrome.runtime.sendMessage / onMessage
Popup ←→ Background: chrome.runtime.sendMessage / chrome.tabs.sendMessage
External sites ←→ Extension: chrome.runtime.sendMessage (if externally_connectable)
```

---

## High-Risk Permission Patterns

| Permission | Risk |
|-----------|------|
| `<all_urls>` / `*://*/*` | Can read/modify all web pages |
| `webRequest` + `<all_urls>` | Can intercept all HTTP traffic |
| `declarativeNetRequest` | Can block/redirect requests |
| `tabs` | Can read all tab URLs and titles |
| `cookies` | Can read/write cookies for any site |
| `storage` | Data persistence (check for sensitive data) |
| `nativeMessaging` | Communicates with native host apps |
| `debugger` | Attaches to browser debugger |
| `clipboardRead` | Reads clipboard contents |
| `identity` | OAuth token access |

---

## CSP Gotchas (MV3)

- `script-src 'self'` — only bundled scripts allowed (no CDN, no `eval`)
- `'unsafe-eval'` in CSP → red flag for obfuscated/dynamic code
- `object-src 'none'` — required in MV3
- External script sources in CSP → flag for analysis

# Chrome Extension API — Quick Reference

Key Chrome APIs for reverse engineering, analysis, and development.

---

## Runtime & Messaging

| API | Description |
|-----|-------------|
| `chrome.runtime.sendMessage(msg, cb)` | Send message from content/popup → background |
| `chrome.runtime.onMessage.addListener(fn)` | Receive messages |
| `chrome.tabs.sendMessage(tabId, msg, cb)` | Send message background → content script |
| `chrome.runtime.connect(info)` | Open a persistent message channel (port) |
| `chrome.runtime.id` | Extension ID |
| `chrome.runtime.getURL(path)` | Get full URL to an extension resource |

---

## Tabs

| API | Permission | Description |
|-----|-----------|-------------|
| `chrome.tabs.query(query, cb)` | `tabs` | Find tabs matching criteria |
| `chrome.tabs.get(tabId, cb)` | `tabs` | Get tab info (URL, title) |
| `chrome.tabs.create(props, cb)` | (none) | Open new tab |
| `chrome.tabs.executeScript(tabId, details)` | MV2 only | Inject script (MV3: `scripting`) |
| `chrome.scripting.executeScript(injection)` | `scripting` | MV3 script injection |

---

## Storage

| API | Scope | Notes |
|-----|-------|-------|
| `chrome.storage.local` | Device-local | Up to 10MB (MV3) |
| `chrome.storage.sync` | Cloud-synced | ~100KB limit |
| `chrome.storage.session` | Session-only | Cleared on browser close |
| `chrome.storage.managed` | Admin-controlled | Read-only |

**RE note:** dump storage with `chrome.storage.local.get(null, console.log)` in DevTools console (from extension context).

---

## Network / Requests

| API | Permission | Description |
|-----|-----------|-------------|
| `chrome.webRequest.onBeforeRequest` | `webRequest` + host | MV2: intercept requests |
| `chrome.declarativeNetRequest` | `declarativeNetRequest` | MV3: rule-based blocking/redirect |
| `fetch()` in service worker | `host_permissions` | Standard fetch with extension privileges |

---

## Identity & Auth

| API | Permission | Description |
|-----|-----------|-------------|
| `chrome.identity.getAuthToken` | `identity` | Get OAuth2 token for signed-in user |
| `chrome.identity.launchWebAuthFlow` | `identity` | OAuth2 flow for external providers |

---

## Cookies

| API | Permission | Description |
|-----|-----------|-------------|
| `chrome.cookies.getAll(details, cb)` | `cookies` + host | Get all cookies for a domain |
| `chrome.cookies.set(details, cb)` | `cookies` + host | Set a cookie |
| `chrome.cookies.remove(details, cb)` | `cookies` + host | Delete a cookie |

---

## Notifications & UI

| API | Permission |
|-----|-----------|
| `chrome.notifications.create()` | `notifications` |
| `chrome.action.setBadgeText()` | (none) |
| `chrome.contextMenus.create()` | `contextMenus` |

---

## Alarms (background scheduling)

```js
chrome.alarms.create('name', { periodInMinutes: 1 });
chrome.alarms.onAlarm.addListener(alarm => { ... });
```

---

## Useful DevTools Snippets (RE)

```js
// From extension background — list all storage
chrome.storage.local.get(null, console.log);

// From extension background — get all cookies for a domain
chrome.cookies.getAll({ domain: 'example.com' }, console.log);

// From extension background — inspect all tabs
chrome.tabs.query({}, tabs => tabs.forEach(t => console.log(t.url, t.title)));

// From content script — check extension context
console.log(chrome.runtime.id);
```

---

## Permissions Reference (Risk Ranking)

| Risk | Permissions |
|------|------------|
| 🔴 Critical | `<all_urls>`, `debugger`, `nativeMessaging` |
| 🟠 High | `webRequest` + host, `cookies`, `tabs`, `history` |
| 🟡 Medium | `storage`, `scripting`, `declarativeNetRequest`, `identity` |
| 🟢 Low | `notifications`, `contextMenus`, `alarms`, `action` |

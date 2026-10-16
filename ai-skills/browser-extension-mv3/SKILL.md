---
name: browser-extension-mv3
description: >
  Recognizes and works inside a Manifest V3 browser extension for Chrome/Edge — a static
  `manifest.json` with `"manifest_version": 3`, an ephemeral service-worker background,
  isolated content scripts, and popup/options pages. Fires on a repo containing a
  `manifest.json` with `manifest_version: 3` (keys like `background.service_worker`,
  `content_scripts`, `action`, `permissions`, `host_permissions`). Use when the user says
  "the Dock extension", "load the extension", "my content script change didn't apply",
  "the service worker lost its state", "add a permission", "reach the page's variables",
  or "message the background from the popup". Covers the manifest contract, the
  load-unpacked dev loop, the three-context split (worker / content / page), messaging,
  and the build step. In navig this is Dock (`apps/dock/extension`) — the browser
  companion that talks to the local daemon. Read-only recognition + workflow guidance;
  suggested build/reload steps touch build output only.
category: frontend
tags: [browser-extension, manifest-v3, chrome, edge, service-worker, content-script]
safety: safe
---

# Manifest V3 browser extensions (navig Dock)

An ephemeral service worker, content scripts locked in an isolated world, and a `manifest.json` that
is the whole contract. This skill recognizes an MV3 extension and keeps you on the right side of its
three execution contexts. navig's example is **Dock** (`apps/dock/extension`) — the browser companion
that talks to the local daemon.

## Recognize it

- A **`manifest.json`** with **`"manifest_version": 3`**.
- Keys such as `background.service_worker`, `content_scripts`, `action` (toolbar popup),
  `options_page`/`options_ui`, `permissions`, `host_permissions`, `commands`,
  `web_accessible_resources`, `content_security_policy`.
- A build step: sometimes Vite (`@crxjs/vite-plugin`) or webpack — **Dock uses a custom Node build**
  (`scripts/build.js` with terser + clean-css) that emits `dist/`.
- No bundler at all? The extension folder itself (plain JS/HTML/CSS next to `manifest.json`) is the
  loadable artifact.

Dock's manifest at a glance: `background/service-worker.js` (`type: module`), one content script over
`<all_urls>` at `document_end`, `permissions: [storage, activeTab, tabs, scripting, contextMenus,
alarms]`, `host_permissions` including **`http://localhost:8789/*`** (the local gateway), a `popup`,
an `options_page`, keyboard `commands`, and a lens/apps SDK exposed via `web_accessible_resources`.

## Run it

```powershell
# Dock (custom Node build):
npm install
npm run dev            # scripts/watch.js — rebuild on change
npm run build          # dev build → dist/ (the folder you load)
npm run build:prod     # minified production build
npm run package        # zip dist/ for the store
npm run dev:browser    # launch a browser with the unpacked extension (add :edge for Edge)
```

**Load unpacked (Chrome/Edge):**

1. Open `chrome://extensions` (or `edge://extensions`).
2. Toggle **Developer mode** (top-right).
3. **Load unpacked** → select **`dist/`** (bundled) or the extension root (plain).
4. After edits: click **Reload** on the card. Manifest or service-worker changes *require* a card
   reload; content-script changes also need the **target page refreshed**.

## Three contexts — never confuse them

| Context | Where it runs | Sees | Key limits |
|---------|---------------|------|-----------|
| **Service worker** (`background.service_worker`) | extension, headless | no DOM | **event-driven, can die anytime** — hold no long-lived memory, persist to `chrome.storage`; register listeners at top level so they survive restart |
| **Content script** (`content_scripts` / `chrome.scripting`) | inside the page | the page DOM | **isolated world** — cannot read the page's JS globals; only a slim `chrome.*` surface (messaging + storage) |
| **Popup / options** | extension page | its own DOM | full `chrome.*` access |

**Messaging bridges them:** `chrome.runtime.sendMessage` / `onMessage` between popup ⇄ worker;
`chrome.tabs.sendMessage` to reach a content script. UI ↔ worker ↔ page communicate only through
messages — there is no shared memory.

## Manifest is the contract

A new content script, `command`, icon, permission, or web-exposed file must be declared in
`manifest.json` or it does not exist at runtime. Keep permissions least-privilege: `permissions`
(API access) and `host_permissions` (which sites) are separate, and MV3 prefers `activeTab` +
`chrome.scripting` over a broad host grant. Files the page must load (Dock's lens/app SDK) go in
`web_accessible_resources`.

## Traps

- **The service worker is not persistent.** MV3 killed background pages — any variable in the worker
  can vanish between events. Persist to `chrome.storage.local`/`session`; re-register `onMessage` /
  `onAlarm` listeners at the top level, never inside an async callback.
- **Content scripts can't touch the page's JS.** Isolated world: you see the DOM, not the site's
  `window` globals. To reach page-world variables, inject a `<script>` into the page and talk via
  `window.postMessage` / DOM events.
- **Reload discipline is the #1 "my change didn't work."** Manifest/worker edit → card **Reload**;
  content-script edit → **also refresh the page**. With `@crxjs`, HMR reloads scripts for you but a
  manifest change may still need a manual card reload.
- **Extension CSP is strict** — no remote scripts, no `eval`, no inline handlers on extension pages.
  Bundle everything locally (Dock's `content_security_policy.extension_pages` enforces `script-src
  'self'`).
- **MV2 patterns are dead** — no `background.scripts`/persistent page, `browser_action` → `action`,
  blocking `webRequest` → `declarativeNetRequest`. Don't port MV2 snippets verbatim.
- **navig-specific: the shared page-bar contract.** Dock's on-page bar coordinates with a sibling
  extension's bar through a `data-webbar-*` DOM contract (tri-state auto-position) so the two don't
  overlap. Don't hardcode a position or assume Dock owns the page edge — honor the shared attributes.
- **navig-specific: gateway reachability.** Dock's live features call the local daemon at
  `http://localhost:8789` (a declared `host_permission`). If integration goes dead, confirm the daemon
  is running and the host grant is still in the manifest before touching extension code.

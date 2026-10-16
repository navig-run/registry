# Userscripts Workshop

A ready-to-go workspace for authoring, testing, and publishing Greasemonkey,
Tampermonkey, and Violentmonkey userscripts.

---

## What Is a Userscript?

A userscript is a JavaScript file that runs in your browser on specific websites,
letting you add features, remove annoyances, or automate actions — without touching
the site's own source code. Userscript managers (Tampermonkey, Greasemonkey,
Violentmonkey) inject these scripts after page load based on `@match` patterns
in the metadata block.

---

## Quick Start

1. Install [Tampermonkey](https://www.tampermonkey.net/) in Chrome/Edge, or
   [Greasemonkey](https://addons.mozilla.org/en-US/firefox/addon/greasemonkey/)
   in Firefox, or [Violentmonkey](https://violentmonkey.github.io/) for either.
2. Open the extension dashboard → **New Script** (or drag a `.user.js` file in).
3. Copy `starter-script.user.js` and customise the metadata block and `init()` body.
4. Save — the extension will auto-install it and run it on matching URLs.

---

## Metadata Block Reference

Every userscript starts with a `==UserScript==` block. Key fields:

| Field | Required | Description |
|-------|----------|-------------|
| `@name` | Yes | Display name shown in the manager dashboard |
| `@namespace` | Yes | Unique identifier (conventionally your domain or GitHub URL) |
| `@version` | Yes | Semantic version (e.g. `1.0.0`) |
| `@description` | Yes | One-line description |
| `@author` | Recommended | Your name or handle |
| `@match` | Yes | URL pattern(s) where the script runs |
| `@include` | Optional | Glob-style match (less precise, legacy) |
| `@exclude` | Optional | URL pattern(s) where the script must not run |
| `@grant` | Yes | `none` or specific `GM_*` permissions the script needs |
| `@run-at` | Optional | `document-start`, `document-end` (default), `document-idle` |
| `@noframes` | Optional | Prevents script running inside `<iframe>` elements |
| `@require` | Optional | External JS library to load before the script |
| `@resource` | Optional | Named external resource (CSS, JSON, image) |

### `@match` Pattern Syntax

| Pattern | Matches |
|---------|---------|
| `https://example.com/*` | All pages on example.com over HTTPS |
| `*://example.com/*` | All pages on example.com over any protocol |
| `https://*.example.com/*` | All subdomains of example.com |
| `https://example.com/path/*` | Pages under a specific path |

### `@grant` Permissions

Only request what you actually use:

| Permission | What it grants |
|-----------|----------------|
| `none` | No special access (default sandboxed mode) |
| `GM_getValue` / `GM_setValue` | Persistent storage across page loads |
| `GM_xmlhttpRequest` | Cross-origin HTTP requests |
| `GM_addStyle` | Inject CSS into the page |
| `GM_notification` | Browser desktop notifications |
| `GM_setClipboard` | Write to clipboard |
| `unsafeWindow` | Access to the page's global `window` object |

---

## File Naming Convention

- Userscript files: `<name>.user.js` — the `.user.js` suffix triggers auto-install in all managers.
- One script per file. Shared utilities → `lib/<util-name>.js` + `@require`.

---

## Workflow: Edit → Test → Publish

1. **Edit** `starter-script.user.js` or create a new `.user.js`
2. **Save** — Tampermonkey auto-reloads on next page load
3. **Test** on the target URL — open browser DevTools Console for errors
4. **Debug** — run `@debugger trace "<ERROR>"` in NAVIG for AI-assisted diagnosis
5. **Publish** — upload to [Greasy Fork](https://greasyfork.org) or share as a `.user.js` file

---

## Files in This Folder

| File | Description |
|------|-------------|
| `starter-script.user.js` | Full annotated starter template ready to customise |

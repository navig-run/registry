# Scaffold Chrome Extension

## Purpose
Generate a complete Manifest V3 Chrome extension skeleton with annotated source
files ready for local loading and iterative development.

## Variables
- `{{EXT_NAME}}` — Extension display name
- `{{DESCRIPTION}}` — One-line description
- `{{PERMISSIONS}}` — Required permissions (e.g. `tabs, storage, activeTab`)
- `{{CONTENT_SCRIPT_MATCH}}` — URL pattern for content script (or `none`)
- `{{HAS_POPUP}}` — `true` or `false`

## Prompt

You are NAVIG Scripter. Generate a complete Manifest V3 Chrome extension for:

- **Name**: `{{EXT_NAME}}`
- **Description**: `{{DESCRIPTION}}`
- **Permissions**: `{{PERMISSIONS}}`
- **Content script match**: `{{CONTENT_SCRIPT_MATCH}}`
- **Has popup**: `{{HAS_POPUP}}`

Produce the following files:

### 1. `manifest.json`
MV3 manifest with all required fields. Annotate every non-obvious field with a
JSON comment (use `"_comment_field": "..."` pattern adjacent to the field).
Include only the permissions actually needed. Explain each permission choice.

### 2. `background.js` (service worker)
- `chrome.runtime.onInstalled` listener
- Message listener skeleton (`chrome.runtime.onMessage`)
- Annotated with comments explaining the service worker lifecycle

### 3. `content.js` (if match is not `none`)
- Wraps in IIFE
- Shows how to send a message to background
- Observes DOM mutations if needed
- Annotated with comments

### 4. `popup/popup.html` + `popup/popup.js` + `popup/popup.css` (if HAS_POPUP is true)
- Minimal working popup with a button that sends a message to background
- Strict CSP-compliant (no inline scripts, no `unsafe-eval`)
- Clean CSS

### 5. After the code block, provide:
- How to load the extension locally (Chrome developer mode, Load unpacked)
- How to open the browser console for background service worker vs popup
- Common first-time errors and their fixes

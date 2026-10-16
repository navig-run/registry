# Scaffold Userscript

## Purpose
Generate a complete, ready-to-install Greasemonkey/Tampermonkey userscript with
correct metadata block, scoped permissions, and annotated implementation skeleton.

## Variables
- `{{SCRIPT_NAME}}` — Display name of the userscript
- `{{TARGET_URL}}` — URL pattern to match (e.g. `https://example.com/*`)
- `{{DESCRIPTION}}` — One-line description of what the script does
- `{{GRANTS}}` — Comma-separated list of required GM_ permissions (e.g. `GM_getValue, GM_setValue`)

## Prompt

You are NAVIG Scripter. Generate a complete Greasemonkey userscript for the following spec:

- **Name**: `{{SCRIPT_NAME}}`
- **Match pattern**: `{{TARGET_URL}}`
- **Description**: `{{DESCRIPTION}}`
- **Required grants**: `{{GRANTS}}`

Output a single `.user.js` file with:

### 1. Metadata Block
Complete `==UserScript==` header including:
- `@name`, `@namespace`, `@version`, `@description`, `@author`
- `@match` — use the provided pattern; add `@include` fallback if needed
- `@grant` — only the permissions this script actually needs
- `@run-at` — `document-end` unless DOM needs to be available earlier
- `@noframes` if the script should not run in iframes

### 2. Implementation Skeleton
```javascript
(function () {
  'use strict';
  // Your code here — annotated with comments explaining each section
})();
```

Include:
- Config object at the top for easy customisation
- A main `init()` function
- Event listener wiring (`DOMContentLoaded` or MutationObserver if needed)
- Error handling with `try/catch`
- At least one `GM_` API call if grants were requested (show correct usage)

### 3. Usage Notes
After the code, include a markdown comment block explaining:
- How to install in Tampermonkey / Greasemonkey
- What the script does and where it runs
- Any manual config steps required

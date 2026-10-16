# Dev Space — Runbooks

Quick-reference procedures for common development tasks.

---

## Scaffold a New Userscript

1. `@scripter scaffold userscript --match <URL_PATTERN> --name <SCRIPT_NAME>`
2. Edit `userscripts-workshop/<SCRIPT_NAME>.user.js` — fill in your logic
3. In browser: open Tampermonkey → Dashboard → Import from file
4. Test on target URL; check browser console for errors
5. If broken: `@debugger trace <ERROR_MESSAGE>`

---

## Scaffold a New Chrome Extension

1. `@scripter build extension --name <EXT_NAME>`
2. Fill in `chrome-extensions-workshop/manifest.json` permissions
3. Chrome: `chrome://extensions` → Enable Developer Mode → Load unpacked
4. Navigate to target URL; test popup and content script
5. Open service worker console: Extensions page → Inspect views: service worker

---

## Run a Code Review

1. `navig ask "run the code-review workflow with target=<FILE_PATH>"`
2. Read the report in `#review`
3. Address all `CRITICAL` and `WARNING` findings
4. Re-run: `navig ask "run the code-review workflow with target=<FILE_PATH>"`

---

## Debug a Failing Skill

1. Run skill: `navig skill run <SKILL_ID>`
2. Check output for error message
3. `@debugger trace "<ERROR_MESSAGE>"`
4. Apply the recommended fix
5. Re-run skill to verify

---

## Run Tests

```bash
navig ask "run the run-tests workflow"
```

Or target a specific file:
```bash
navig skill run run-tests --target tests/test-code-lint.js
```

---

## Publish Extension Locally

1. `navig skill run publish-extension --mode local`
2. Load unpacked from `dist/` in Chrome developer mode
3. Verify all features work in production URL
4. For CWS: `navig skill run publish-extension --mode cws` (requires credentials)

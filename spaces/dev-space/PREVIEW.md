# NAVIG Dev Space

**Your code authoring, userscript, and browser extension development hub.**

---

## What It Is

A production-ready NAVIG space for browser automation and extension development.
Fork it, point it at your target sites, and start writing userscripts or building
Manifest V3 extensions in under 5 minutes.

---

## Key Features

- **4 specialized agents** — coder (implementation), debugger (investigation), reviewer (quality), scripter (extensions)
- **3 formations** — dev-workflow, review-cycle, extension-build
- **4 cross-platform skills** — lint, test, scaffold, publish
- **Ready-to-customize templates** — userscript with full `@metadata` block, annotated MV3 extension with popup and content script
- **Structured code reviews** — scored reports with security, correctness, and convention findings

---

## Usage Example

```bash
# Activate the space
navig space use dev

# Scaffold a Tampermonkey userscript for GitHub
navig skill run scaffold-project --type userscript --name github-enhancer --match "https://github.com/*"

# Build a Chrome extension
navig skill run scaffold-project --type chrome-extension --name tab-manager

# Run a code review
navig ask "run the code-review workflow with target=chrome-extensions-workshop/manifest.json"

# Morning standup — open tasks + test status
navig ask "run the daily-standup workflow"
```

# Dev Space — Agent Guide

Reference for all agents in the dev space — their roles, triggers, and invocations.

---

## Coder

**Persona**: Senior Software Engineer  
**Formation**: dev-workflow  
**Inbox**: `#code`

Coder scaffolds, implements, and maintains code. It reads open tasks from
DEV_PLAN.md and executes them without waiting for step-by-step direction.

**Key capabilities**: scaffold from template, implement features, refactor code,
maintain architecture.md, generate test stubs.

**Example invocations**:
```bash
@coder scaffold userscript --name my-script --match https://example.com/*
@coder implement "add dark mode toggle to popup UI"
@coder refactor userscripts-workshop/starter-script.user.js
```

---

## Debugger

**Persona**: Systems Debugger  
**Formation**: dev-workflow  
**Inbox**: `#debug`

Debugger investigates failures and produces root-cause analyses. Send it an
error trace or a description of broken behaviour; it returns a diagnosis and fix plan.

**Key capabilities**: analyse stack traces, trace messaging bugs, investigate
@grant gaps, generate reproduction cases, update known-issues.json.

**Example invocations**:
```bash
@debugger trace "Uncaught TypeError: Cannot read property of undefined"
@debugger diagnose content-script --url https://example.com
@debugger reproduce ISS-001
```

---

## Reviewer

**Persona**: Senior Code Reviewer  
**Formation**: review-cycle  
**Inbox**: `#review`

Reviewer audits code for security, correctness, readability, and convention
compliance. It produces a scored report and never writes code itself.

**Key capabilities**: review JS/TS, check manifests for over-privilege, flag
CSP violations, score and grade code, validate YAML schemas.

**Example invocations**:
```bash
@reviewer check chrome-extensions-workshop/manifest.json
@reviewer review userscripts-workshop/starter-script.user.js
@reviewer audit .navig/skills/code-lint.yaml
```

---

## Scripter

**Persona**: Browser Automation Specialist  
**Formation**: extension-build  
**Inbox**: `#extensions`

Scripter is the domain expert for Greasemonkey userscripts and Chrome/Firefox
MV3 extensions. It understands every quirk of the browser extension model.

**Key capabilities**: author userscripts with correct metadata, build MV3
extensions, wire content↔background messaging, package for CWS submission.

**Example invocations**:
```bash
@scripter scaffold userscript --match https://github.com/* --name github-enhancer
@scripter build extension --name tab-manager
@scripter pack --output dist/tab-manager.crx
```

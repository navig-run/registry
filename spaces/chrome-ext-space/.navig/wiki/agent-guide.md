# Agent Guide — Chrome Extension Space

How to use each agent in this space effectively.

---

## `reverser` — Execution Flow Tracer

**Best for:** Understanding how an extension actually behaves at runtime.

**Typical prompts:**
- `"Trace the execution flow starting from the service worker in extensions-lab/my-ext/"`
- `"De-obfuscate this content script and explain what it does: [paste code]"`
- `"Map all message passing channels in this extension"`
- `"What does this background script do when a tab is updated?"`

**What it produces:**
- Annotated script with inline comments
- Execution flow diagram (text-based)
- List of all `chrome` API calls found

---

## `analyzer` — Manifest & Architecture Parser

**Best for:** First pass analysis, permission mapping, component inventory.

**Typical prompts:**
- `"Analyze the manifest.json in extensions-lab/my-ext/"`
- `"Map all content script injection points and their match patterns"`
- `"List all permissions and explain what each one allows"`
- `"What web_accessible_resources are exposed and why might that matter?"`

**What it produces:**
- Permission inventory table
- Component diagram (background + content scripts + popup + comms)
- `findings.md` draft with manifest analysis section

---

## `coder` — Extension Developer

**Best for:** Building new extensions, writing clean MV3 code, refactoring.

**Typical prompts:**
- `"Scaffold a MV3 extension that intercepts all requests to ad domains and logs them"`
- `"Write a content script that highlights all forms on the page"`
- `"Refactor this MV2 background page to a MV3 service worker"`
- `"Create an options page for configuring a domain blocklist"`

**What it produces:**
- Full extension scaffold (manifest + scripts + HTML)
- Inline documented code
- Local load instructions

---

## `auditor` — Security Reviewer

**Best for:** Security assessment of a third-party extension before installing it.

**Typical prompts:**
- `"Audit the extension in extensions-lab/my-ext/ for security issues"`
- `"Does this extension have any over-privileged permissions?"`
- `"Check this content script for XSS or data exfiltration risks"`
- `"Rate the risk level of this extension and explain the reasoning"`

**What it produces:**
- Risk rating: LOW / MEDIUM / HIGH / CRITICAL
- Finding table: issue, location, severity, recommendation
- Summary paragraph suitable for a security report

---

## Formation Quick Reference

| Formation | Use When |
|-----------|---------|
| `analyze-workflow` | Starting a new extension analysis; default mode |
| `dev-workflow` | Building or refactoring an extension |
| `audit-cycle` | Security review of a third-party extension |

---
space: chrome-ext
version: 1.0.0
created: 2026-04-19
owner: operator
---

# Chrome Extension Space — Context

## Purpose

Chrome extension reverse engineering, static analysis, security auditing, and development workspace.
A focused environment for unpacking real-world extensions, understanding their architecture, auditing
their security posture, and building new Manifest V3 extensions from scratch.

## Scope

- **Reverse engineering** — unpack `.crx`/`.zip` artifacts, trace background service workers and
  content script injection, de-obfuscate bundled JavaScript, map inter-component messaging
- **Static analysis** — parse `manifest.json` (MV2 & MV3), enumerate declared permissions vs used
  permissions, map `web_accessible_resources`, `content_security_policy`, and host permissions
- **Security auditing** — identify over-privileged extensions, potential exfiltration via
  `fetch`/XHR from content scripts, `chrome.storage` abuse, `executeScript` injection vectors,
  and unsafe `eval` usage
- **Development** — scaffold new MV3 extensions, implement background service workers, popup UIs,
  devtools panels, options pages, and content scripts; package and load-test locally

## Active Agents

reverser · analyzer · coder · auditor

## Active Formations

analyze-workflow · dev-workflow · audit-cycle

## Key Paths

- Space root: `spaces/chrome-ext-space`
- Config: `.navig/config.yaml`
- Memory: `.navig/memory/`
- Wiki: `.navig/wiki/`
- Extension drop zone: `extensions-lab/`
- Analysis template: `extensions-lab/_template/`

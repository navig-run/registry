# GENESIS — Chrome Extension Space

## Why This Exists

Chrome extensions are complex, opaque artifacts. Reverse engineering one means unpacking manifests, tracing background service workers, reading obfuscated content scripts, mapping permission scopes, and hunting network calls — all at once.

Without a dedicated space: analysis notes scatter, findings get lost, and every RE session starts from scratch.

This space is the lab: drop an extension in, tear it apart, understand it, build on it — with agents that know the Chrome architecture deeply.

## What It Does

Chrome Extension Space is the workspace for everything Chrome extension related:

- **Reverse engineering** — unpack `.crx`/`.zip` artifacts, trace script execution flow, de-obfuscate content scripts
- **Static analysis** — parse `manifest.json` (MV2 & MV3), map permissions, CSP rules, host patterns, and message-passing channels
- **Security auditing** — identify over-privileged extensions, exfiltration vectors, XSS via `executeScript`, and storage abuse
- **Development** — scaffold new extensions from scratch, implement Manifest V3 service workers, popup UIs, and devtools panels

## Core Agents

| Agent | Role |
|-------|------|
| `reverser` | Unpacks, de-obfuscates, and traces extension execution flow |
| `analyzer` | Parses manifests, maps permissions, build component graphs |
| `coder` | Authors new extensions, content scripts, and background workers |
| `auditor` | Security review — permissions, CSP, network, data exposure |

## Primary Formations

- **`analyze-workflow`** — RE mode: unpack → inspect → map → document findings
- **`dev-workflow`** — Build mode: scaffold → implement → test → package
- **`audit-cycle`** — Security gate: permissions → CSP → network audit → risk report

## Origin

Built to give reverse engineers and extension developers a structured workspace where every extension analysis is reproducible, findings are organized, and new extensions are built on a solid architectural understanding.

---
*Space ID: `chrome-ext` · Runtime: `navig-space-2` · Tier: work*

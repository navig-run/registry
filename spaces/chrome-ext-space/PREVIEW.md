# Chrome Extension Space — Preview

## One-Liner

> Tear apart any Chrome extension, map its attack surface, and build your own — all in one structured workspace.

---

## What You Get

- **`extensions-lab/`** — dedicated drop zone for downloaded extensions with a structured analysis template
- **`reverser` agent** — traces execution flow, de-obfuscates scripts, maps background ↔ content script messaging
- **`analyzer` agent** — parses manifests, permission graphs, CSP policies, web-accessible resources
- **`auditor` agent** — produces security risk reports: over-privilege, data exfiltration, injection vectors
- **`coder` agent** — scaffolds Manifest V3 extensions from a description

## Typical Session

```
# 1. Drop extension into lab
cp my-extension.zip extensions-lab/

# 2. Activate space
navig space use chrome-ext

# 3. Unpack (see docs/runbooks/unpack-crx.md)
# 4. Start analysis
navig ask "analyze the manifest.json in extensions-lab/my-extension/"
```

## Install

```bash
navig space install github:navig-run/registry/spaces/chrome-ext-space
```

> Status: **planned**. The agents listed above are a design; today the space ships the
> `extensions-lab/` template, the Chrome API reference and the unpack runbook.

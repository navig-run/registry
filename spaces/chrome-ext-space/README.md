# Chrome Extension Space

> Reverse engineering, analysis, security auditing, and development workspace for Chrome extensions.

---

## What This Space Is For

| Activity | What You Do Here |
|----------|-----------------|
| **Reverse Engineering** | Unpack `.crx`/`.zip` artifacts, trace scripts, de-obfuscate |
| **Static Analysis** | Parse `manifest.json`, map permissions, CSP, host patterns |
| **Security Auditing** | Permission abuse, exfiltration vectors, storage inspection |
| **Development** | Build new MV3 extensions from scratch |

---

## Folder Map

```
chrome-ext-space/
├── extensions-lab/          ← DROP DOWNLOADED EXTENSIONS HERE FOR ANALYSIS
│   ├── README.md            ← Analysis instructions and naming conventions
│   └── _template/           ← Copy this folder for each extension you analyze
│       ├── NOTES.md         ← Free-form analysis scratch pad
│       ├── manifest.json    ← Copy of the extension's manifest.json
│       └── findings.md      ← Structured findings report
│
├── docs/
│   ├── reference/
│   │   └── chrome-apis.md   ← Key Chrome Extension API reference
│   └── runbooks/
│       └── unpack-crx.md   ← How to unpack a .crx file (Windows)
│
├── scripts/                 ← Automation: unpack, diff, audit helpers
│
├── .navig/
│   ├── space.config.json    ← Space definition (agents, formations, workflows)
│   ├── config.yaml          ← Runtime config
│   ├── context.md           ← Agent context document
│   ├── plans/               ← Active phase, roadmap
│   ├── wiki/                ← Space wiki (architecture, agent guide, runbooks)
│   └── store/               ← Agents, formations, prompts, workflows
│
├── GENESIS.md               ← Why this space exists
├── PREVIEW.md               ← Quick start
└── space.manifest.json      ← Deployment manifest
```

---

## Quick Start — Analyzing an Extension

1. Download a Chrome extension as a `.crx` or `.zip`
2. Drop it into `extensions-lab/`
3. Follow the instructions in `extensions-lab/README.md` to unpack
4. Copy `extensions-lab/_template/` to a new folder named after the extension
5. Start with `manifest.json` — paste the extension's manifest there
6. Fill in `findings.md` as you explore

---

## Quick Start — Building an Extension

1. Activate this space: `navig space use chrome-ext`
2. Ask the `coder` agent to scaffold: `navig ask "scaffold a MV3 extension that ..."`
3. Use `analyze-workflow` for inspection, `dev-workflow` for building

---

## Space Info

- **Space ID:** `chrome-ext`
- **Tier:** `work`
- **Runtime:** `navig-space-2`
- **Agents:** `reverser` · `analyzer` · `coder` · `auditor`
- **Formations:** `analyze-workflow` · `dev-workflow` · `audit-cycle`

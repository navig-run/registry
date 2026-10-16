# Extensions Lab

**This is the drop zone for Chrome extensions you want to analyze.**

---

## How to Use

### 1. Drop your extension here
- Download a `.crx` or `.zip` from the Chrome Web Store (use a CRX downloader tool)
- Place the file in this folder

### 2. Unpack it
See `docs/runbooks/unpack-crx.md` for step-by-step unpack instructions.

Unpack into a subfolder named after the extension:
```
extensions-lab/
└── my-extension-name/
    ├── manifest.json
    ├── background.js / service_worker.js
    ├── content_scripts/
    └── ...
```

### 3. Copy the analysis template
```powershell
# PowerShell
Copy-Item -Recurse extensions-lab\_template extensions-lab\my-extension-name-analysis
```

### 4. Start analysis
- Copy the extension's `manifest.json` into your analysis folder
- Fill in `NOTES.md` and `findings.md` as you explore
- Ask the `analyzer` or `auditor` agent for help

---

## Naming Convention

| What | Convention |
|------|-----------|
| Unpacked extension folder | `<extension-name>-<version>/` e.g. `grammarly-14.1109.0/` |
| Analysis folder | `<extension-name>-analysis/` e.g. `grammarly-analysis/` |
| Raw download files | `<extension-name>-<version>.crx` or `.zip` |

---

## .gitignore Note

Add this folder to `.gitignore` if you are analyzing proprietary or private extensions:
```
extensions-lab/*/
!extensions-lab/_template/
!extensions-lab/README.md
```

---

## Current Extensions Under Analysis

_(add entries here as you work)_

| Extension | Version | Status | Risk |
|-----------|---------|--------|------|
| _(none yet)_ | — | — | — |

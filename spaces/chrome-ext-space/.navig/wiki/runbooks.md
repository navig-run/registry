# Runbooks — Chrome Extension Space

> This space is **planned**: the analyzer / reverser / auditor / coder agents and their
> formations are a design, not yet shipped. The runbooks below work today with plain
> `navig ask` and standard tools.

---

## Runbook 1: Analyze a Downloaded Extension

**Goal:** Go from a raw `.crx` or `.zip` download to a structured findings report.

### Steps

1. **Unpack the extension**
   - See `docs/runbooks/unpack-crx.md` for platform-specific instructions
   - Unpack into `extensions-lab/<extension-name>/`

2. **Copy the analysis template**
   ```
   cp -r extensions-lab/_template/ extensions-lab/<extension-name>-analysis/
   ```

3. **Copy `manifest.json`**
   ```
   cp extensions-lab/<extension-name>/manifest.json \
      extensions-lab/<extension-name>-analysis/manifest.json
   ```

4. **First-pass: manifest analysis**
   - Run: `navig ask "Analyze manifest.json in extensions-lab/<extension-name>-analysis/"`
   - Paste results into `findings.md` → **Section: Manifest Analysis**

5. **Trace execution flow**
   - Run: `navig ask "Trace execution flow in extensions-lab/<extension-name>/"`
   - Add results to `findings.md` → **Section: Execution Flow**

6. **Security audit (if needed)**
   - Run: `navig ask "Audit extensions-lab/<extension-name>/ for security issues"`
   - Add results to `findings.md` → **Section: Security Findings**

7. **Document in `NOTES.md`** — add your own observations, questions, next steps

---

## Runbook 2: Scaffold a New MV3 Extension

**Goal:** Create a working MV3 extension from a description.

### Steps

1. Run: `navig ask "Scaffold a MV3 Chrome extension that [describe what it does]"`
2. The agent will output a folder structure — save to `scripts/` or a new workspace folder
3. Load in Chrome: `chrome://extensions/` → **Load unpacked** → select the folder
4. Test, iterate

---

## Runbook 3: Diff Two Versions of an Extension

**Goal:** Understand what changed between two versions (new permissions, new scripts).

### Steps

1. Unpack both versions:
   ```
   extensions-lab/my-ext-v1.0/
   extensions-lab/my-ext-v2.0/
   ```
2. Diff manifests:
   ```powershell
   # PowerShell
   Compare-Object (Get-Content extensions-lab\my-ext-v1.0\manifest.json) `
                  (Get-Content extensions-lab\my-ext-v2.0\manifest.json)
   ```
   Or use VS Code diff: right-click file → **Select for Compare**, then right-click other → **Compare with Selected**

3. Diff all JS files:
   ```powershell
   git diff --no-index extensions-lab\my-ext-v1.0\ extensions-lab\my-ext-v2.0\
   ```

4. Ask analyzer: `navig ask "Compare the permissions changes between v1 and v2 of my-ext"`

---

## Runbook 4: Check an Extension Before Installing

**Quick security check — 5 minutes.**

1. Download extension as `.zip` (from Chrome Web Store source or CRX Viewer)
2. Unpack into `extensions-lab/<name>/`
3. Run: `navig ask "Quick security check: rate the risk of extensions-lab/<name>/"`
4. If HIGH/CRITICAL → read `findings.md` before deciding to install

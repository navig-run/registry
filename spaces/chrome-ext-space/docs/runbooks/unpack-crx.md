# Runbook: Unpack a Chrome Extension (.crx / .zip)

Chrome extensions distributed as `.crx` files are ZIP archives with a custom header.
This runbook covers unpacking them on Windows, Linux, and macOS.

---

## Method 1 — Rename to .zip and unzip (simplest)

A `.crx` file is a ZIP archive with a small binary header prepended.
For MV3 extensions (modern), a simple rename usually works:

```powershell
# PowerShell (Windows)
Rename-Item my-extension.crx my-extension.zip
Expand-Archive -Path my-extension.zip -DestinationPath extensions-lab\my-extension\
```

> **If Expand-Archive fails** with "The archive entry was compressed using an unsupported compression method" — use Method 2.

---

## Method 2 — Skip the CRX header, extract the ZIP payload

CRX3 format has a variable-length header before the ZIP payload. Use Python to strip it:

```python
# strip_crx.py  (save and run from repo root)
import sys, struct, zipfile, io

crx_path = sys.argv[1]   # input .crx
out_dir   = sys.argv[2]  # output directory

with open(crx_path, 'rb') as f:
    magic = f.read(4)
    assert magic == b'Cr24', "Not a CRX3 file"
    version = struct.unpack('<I', f.read(4))[0]
    assert version == 3, f"Unexpected CRX version: {version}"
    header_len = struct.unpack('<I', f.read(4))[0]
    f.read(header_len)   # skip protobuf header
    zip_data = f.read()

with zipfile.ZipFile(io.BytesIO(zip_data)) as zf:
    zf.extractall(out_dir)

print(f"Extracted to {out_dir}")
```

```powershell
# Run it
python scripts\strip_crx.py extensions-lab\my-extension.crx extensions-lab\my-extension\
```

---

## Method 3 — Download directly as unpacked from Chrome Web Store

Use the **CRX Viewer** browser extension or online tools:

- **crxviewer.robwu.nl** — paste CWS URL, download as ZIP
- **Chrome Web Store Downloader** browser extension — downloads `.crx` directly

Then unzip with `Expand-Archive`.

---

## Method 4 — Load in Chrome and copy from profile (Windows)

1. Install the extension from Chrome Web Store normally
2. Navigate to: `%LOCALAPPDATA%\Google\Chrome\User Data\Default\Extensions\`
3. Find the folder matching the extension ID
4. Copy the version subfolder to `extensions-lab\`

```powershell
# Find by extension ID (from chrome://extensions/)
$extId = "cfhdojbkjhnklbpkdaibdccddilifddb"   # example
$src = "$env:LOCALAPPDATA\Google\Chrome\User Data\Default\Extensions\$extId"
Get-ChildItem $src   # shows version folders
Copy-Item -Recurse "$src\1.0.0_0" "extensions-lab\my-extension\"
```

---

## After Unpacking — Verify

```powershell
# Check you have a manifest.json
Test-Path extensions-lab\my-extension\manifest.json

# Quick peek at the manifest
Get-Content extensions-lab\my-extension\manifest.json | ConvertFrom-Json | Select-Object name, version, manifest_version, permissions
```

---

## Folder Convention

After unpacking, your `extensions-lab/` should look like:

```
extensions-lab/
├── grammarly-14.1109.0/         ← unpacked extension
│   ├── manifest.json
│   ├── background.js
│   └── ...
└── grammarly-analysis/          ← your analysis folder (copy of _template/)
    ├── manifest.json            ← copied from above
    ├── NOTES.md
    └── findings.md
```

# Scripts — Chrome Extension Space

Automation scripts for extension analysis and development workflows.

## Planned Scripts

| Script | Description | Status |
|--------|-------------|--------|
| `strip_crx.py` | Strip CRX3 header and extract ZIP payload | _(see docs/runbooks/unpack-crx.md)_ |
| `audit_manifest.py` | Parse manifest.json and emit a permissions risk report | planned |
| `diff_extensions.py` | Diff two unpacked extension versions | planned |
| `scaffold_mv3.py` | Scaffold a new MV3 extension from a YAML spec | planned |

## Usage

Copy `strip_crx.py` from `docs/runbooks/unpack-crx.md` and save it here for reuse:

```powershell
python scripts\strip_crx.py extensions-lab\my-ext.crx extensions-lab\my-ext\
```

# Memory

This folder holds the space's working state. It ships with **examples only** — your own
data never comes from the registry.

On first use, copy each `<name>.example.json` to `<name>.json` and edit it:

```bash
for f in .navig/memory/*.example.json; do cp -n "$f" "${f%.example.json}.json"; done
```

```powershell
Get-ChildItem .navig/memory/*.example.json | ForEach-Object {
  $dst = $_.FullName -replace '\.example\.json$', '.json'
  if (-not (Test-Path $dst)) { Copy-Item $_.FullName $dst }
}
```

Skills and agents read and write the plain `<name>.json` files. Keep them out of version
control if the space folder is a git repository.

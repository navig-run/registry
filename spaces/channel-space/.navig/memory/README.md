# Memory

Long-lived context for this space. The agents read and write the live file names
(`goals.json`, `known-issues.json`, `space-context.json`); this folder ships only
`*.example.json` seeds so an install never inherits someone else's state.

First run — copy each example to its live name:

```sh
cd .navig/memory
for f in *.example.json; do [ -e "${f%.example.json}.json" ] || cp "$f" "${f%.example.json}.json"; done
```

```powershell
Get-ChildItem .navig/memory/*.example.json | ForEach-Object {
  $live = $_.FullName -replace '\.example\.json$', '.json'
  if (-not (Test-Path $live)) { Copy-Item $_.FullName $live }
}
```

The live files are private (`.gitignore` keeps them out of version control); edit them
freely in your copy of `channel-space`.

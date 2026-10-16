# Formation — safe-migration

Relocate data across drives/homes without ever losing it.

```
inspector  →  mover                         →  inspector
size/probe    copy → VERIFY → trash → log      re-verify dest, report reclaimed
```

1. **inspector** — size the source (`robocopy /L`), detect long paths / ACL risks.
2. **mover** —
   - cross-volume **robocopy** the tree (exclude regenerable dirs if "source only");
   - **VERIFY** dest file-count/bytes ≥ source (re-search the whole dest — items get
     re-categorized);
   - move the **original → `<drive>:\.trash`** (instant rename) and append `restore-log.tsv`
     with `migrated_to` + `verified=yes`;
   - long paths → purge via `\\?\` / robocopy `/MIR` `/B`.
3. **inspector** — confirm, report reclaimed GB. **Empty trash only on explicit confirmation.**

**Default agent:** mover. **Invariant:** the original is never gone until the copy is proven.

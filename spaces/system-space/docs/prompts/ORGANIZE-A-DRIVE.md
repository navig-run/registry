# Prompt — Organize a drive / folder by purpose

**Parameters:** `SOURCE` (folder to organize), `DEST` (clean tree root), `DOMAIN` (what kind
of content — code/media/docs/mixed).

## STEP 0 — Investigate (read-only)
- `system.ps1 inventory SOURCE` · `size SOURCE` · `broken SOURCE` · `dupes SOURCE`.
- List top-level + one level deep; note hostile filenames, long paths, repos.

## STEP 1 — Design the tree (by PURPOSE)
- Buckets = what things *do/are*, not extension/language. Keep a language/type tag for INDEX.
- Reserve `_review-yours` (operator's own), `_duplicates`, `misc`.

## STEP 2 — Classify (size + keyword, guarded)
- Use **size** to surface SFX/clips/samples/broken (small) vs full files (large).
- Keyword-match for obvious types, **but guard false-positives** (real content uses the
  same words). Present borderline items; don't auto-move them.

## STEP 3 — File it (dry-run → apply)
- `tools/classify-by-purpose.ps1 -Source SOURCE -Dest DEST` (dry-run), review, then `-Apply`.
- **Copy** (leave source); exclude `node_modules`/deps; emit `INDEX.md` (name|purpose|type|source).

## STEP 4 — Verify & report
- Count filed vs source; confirm nothing lost. Report bucket counts. Park dups, flag broken.
- Hand heavy media steps to the **media** sub-space.

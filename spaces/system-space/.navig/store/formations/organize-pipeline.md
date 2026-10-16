# Formation — organize-pipeline

Turn a sprawling folder/drive into a clean, indexed tree.

```
inspector  →  organizer  →  (converter)  →  mover
inventory      classify       convert         file + index
size/dupes     by purpose     formats         (copy, dry-run)
broken         + size         if needed       INDEX.md + verify
```

1. **inspector** — read-only: counts, size distribution (smallest-first), dupes, broken.
2. **organizer** — classify by purpose + size; build the destination plan; guard keyword
   false-positives; route operator's own code to `_review-yours`, dups to `_duplicates`.
3. **converter** *(optional)* — normalize formats (archives/docs/images; A/V → media).
4. **mover** — copy into the tree (dry-run → apply), emit `INDEX.md`, verify by count.

**Default agent:** organizer. **Outputs:** clean tree + INDEX manifest + nothing lost.

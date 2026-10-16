# Prompt — Reclaim disk space (safely)

**Parameters:** `DRIVE` or `TARGET` (folder/trash to reclaim).

## STEP 0 — Find the fat
- `system.ps1 size TARGET`; rank biggest second-level dirs (`robocopy /L /BYTES`).
- `broken TARGET` (0-byte + truncated) · `dupes TARGET`.

## STEP 1 — Prove redundancy
- For each big/removable item, confirm a **verified** copy exists elsewhere (count/bytes).
- Audit `.trash` against `restore-log.tsv`: every item's `migrated_to` must exist & match.
  Orphans (`migrated_to = -`) are either intentional junk or must be **organized out first**.

## STEP 2 — Reclaim
- Broken/0-byte/dupes → remove (confirm; they're dead). 
- Long-path trees → `system.ps1 purge <path> -Apply` (`\\?\` / robocopy `/MIR` `/B`).
- Empty trash → `system.ps1 reclaim <drive>:\.trash -Apply` — **only after explicit OK**;
  keep `restore-log.tsv`.

## STEP 3 — Report
- Free space before/after; GB reclaimed; what was kept recoverable. Never report success
  while any orphan lived only in the deleted set.

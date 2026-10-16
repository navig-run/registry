# Prompt — Safely migrate data to a new home

**Parameters:** `SOURCE`, `DEST`, `SOURCE_ONLY?` (exclude node_modules/deps).

## STEP 0 — Investigate
- `system.ps1 size SOURCE` (fast). Detect long paths (>260) and ACL risks. Check DEST free space.

## STEP 1 — Copy
- `robocopy SOURCE DEST /E /R:0 /W:0 /MT:16` (+ `/XD node_modules .git vendor dist` if SOURCE_ONLY).
- For long-path trees use the long-path runbook; expect a few deep cache files to skip (fine).

## STEP 2 — VERIFY (the step that prevents loss)
- Compare **file count / bytes** DEST ≥ SOURCE. Re-search the whole DEST tree (items may be
  re-categorized). Do **not** proceed on "folder exists".

## STEP 3 — Trash the original (recoverable)
- `system.ps1 trash SOURCE -Reason migrated -Apply` → `<drive>:\.trash` + `restore-log.tsv`
  with `migrated_to=DEST`, `verified=yes`. (Or `system.ps1 migrate SOURCE -To DEST -Apply`
  does STEP 1–3.)

## STEP 4 — Report
- "copied N/N ✓, original → trash (recoverable)". **Emptying trash is a separate, confirmed step.**

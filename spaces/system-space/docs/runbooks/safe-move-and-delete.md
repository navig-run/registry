# Runbook — Safe move & delete (never lose data)

The rule that saved a multi-TB migration: **copy → verify → trash → (later) empty.**

## 1. Move a project/folder to a new home
```
1. robocopy <src> <dst> /E /R:0 /W:0 /MT:16   (exclude node_modules/.git/vendor if it's "source only")
2. VERIFY: file count (or bytes) on <dst> >= <src>.  Never trust "the folder exists".
3. Move the ORIGINAL to <drive>:\.trash\<name>   (instant same-volume rename)
4. Append to <drive>:\.trash\restore-log.tsv:
     when | item | original_path | trash_path | migrated_to=<dst> | reason | verified=yes
```
`system.ps1 migrate <src> -To <dst> -Apply` does all four.

## 2. The restore-log is the source of truth
Every trashed item has a row. To audit "can I empty .trash?":
- For each item, confirm `migrated_to` exists **with matching count** (items get
  re-categorized after logging — search the whole dest tree, not just the logged path).
- Items with `migrated_to = -` are **orphans**: they live ONLY in trash. Either they're
  intentional junk (0-byte, caches) → fine to drop, or they must be **organized out first**.

## 3. Emptying trash (the only irreversible step)
- Only after every item is proven redundant (on another drive / verified backup).
- It's the slow part: millions of small files + long-path trees. Use `system.ps1 reclaim`
  (robocopy /MIR + \\?\ for long paths; `/B` for ACL-locked files). Keep `restore-log.tsv`.
- **Confirm with the operator first.** Report reclaimed GB after.

## 4. What "broken" means (delete candidates, not data)
- **0-byte** files = failed downloads. **<40KB "songs"** = truncated stubs. Both are dead;
  removing them loses nothing — but say so and get the OK (they may be a re-download list).

## Anti-patterns (these bit us)
- ✗ Trashing before the copy is verified complete.
- ✗ Declaring `.trash` "safe to empty" while orphans live only there.
- ✗ `rm -rf` on a long-path tree (hangs/partial). Use the purge runbook.
- ✗ Killing `robocopy` globally while another copy runs — it kills them all.

# Runbook — Organize a drive/folder by purpose

Turn a sprawling dump into a clean, indexed tree — without misfiling or losing anything.

## 1. Inventory (read-only)
```
system.ps1 inventory <path>     # counts, dirs, GB, zero-byte
system.ps1 size <path>          # fast bytes/files for huge trees
system.ps1 broken <path>        # 0-byte + truncated stubs
system.ps1 dupes <path>         # duplicates by size+hash
```

## 2. Classify by PURPOSE (not just extension/language)
For reference/inspiration libraries, file by **what it does** (scraping, ai-llm, web,
desktop, automation…) with a language tag in `INDEX.md`. Purpose beats language: language
folders create many near-empty buckets, and you search by "how did someone build X".

## 3. Use SIZE to catch what filenames hide
- SFX / voice clips / samples are **small** (<300 KB); songs/full files are MB.
- Sort smallest-first to surface clips, voice-messages, broken stubs, 0-byte dead files.
- This finds non-music (SFX, ASMR, TikTok rips, soundscapes, audiobooks) that keyword
  scans miss — and that keyword scans *false-positive* on (music says "chant", "mantra",
  "432hz", "legion", "1 hour"). **Always guard keyword hits against false positives.**

## 4. File it (dry-run → apply), build the manifest
```
tools/classify-by-purpose.ps1 -Source <path> -Dest <dest>          # dry-run plan first
tools/classify-by-purpose.ps1 -Source <path> -Dest <dest> -Apply   # copy + write _manifest.tsv
# then build INDEX.md from the manifest: name | purpose | type/lang | source
```
- Copy (don't move) from a still-live source; route the operator's OWN code to `_review-yours`.
- Park exact duplicates in `_duplicates`; drop pure junk after confirmation.

## 5. Verify & report
Count moved vs source; nothing lost. Report the new shelf counts and reclaimed space.

> Heavy media steps (transcode/OCR/A-V/image convert) → hand to a dedicated media space or tool.

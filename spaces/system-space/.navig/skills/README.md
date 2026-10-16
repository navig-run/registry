# System skills (planned)

Packaged navig skills for this space are **planned, not yet shipped**. Today every
capability is reached through the engine `bin/system.ps1` (dry-run by default; add
`-Apply`) and `tools/classify-by-purpose.ps1`:

| Planned skill | Does | Available today |
|---|---|---|
| **fs-inventory** | Read-only scans: counts, size distribution, dupes, broken/0-byte | `system.ps1 inventory`, `size`, `broken`, `dupes` |
| **file-organize** | Classify by purpose/type/size, file into a clean tree, build `INDEX.md` | `tools/classify-by-purpose.ps1` |
| **safe-move** | Move/migrate: same-vol rename or cross-vol robocopy → verify → trash original + log | `system.ps1 move`, `migrate`, `trash` |
| **long-path-ops** | Delete >260-char trees (`\\?\` / robocopy `/MIR` `/B`) | `system.ps1 purge` |
| **dedupe** | Find & resolve duplicate files (size+hash); park dups in `_duplicates` | `system.ps1 dupes` (report only) |
| **bulk-rename** | Pattern/regex rename with `-LiteralPath`, dry-run preview | — |
| **convert** | Archives (7z), documents (pandoc), images (magick) | — |
| **cleanup** | Remove 0-byte/broken/junk; reclaim space; empty trash (confirmed) | `system.ps1 broken`, `reclaim` |

**Doctrine for every skill:** never hard-delete · verify by count/bytes · same-volume rename ·
`-LiteralPath` always · classify by purpose **and** size · guard keyword false-positives.

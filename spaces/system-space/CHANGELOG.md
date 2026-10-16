# Changelog — System space

## [Unreleased]
### Changed
- Space id is now `system-space`; author `navig-run`.
- Manifests list only shipped content: the 8 planned skills and 2 workflows are tracked
  as planned, and the nested media sub-space claim was dropped.
- Docs use placeholder paths instead of real machine paths.

## [1.0.0] — 2026-06-24
### Added
- Initial **System** space: OS & filesystem operator.
- Operating doctrine (`.navig/context.md`) distilled from real production work:
  multi-TB drive migration, long-path backup purge, lock-breaking, size-based
  library classification.
- Engine `bin/system.ps1` + `bin/System-Common.ps1` (inventory/size/broken/dupes/move/
  migrate/trash/purge/reclaim).
- Runbooks: safe-move-and-delete, long-path-operations, organize-a-drive.
- Reference: `docs/reference/windows-filesystem.md`.
- Agents (inspector/organizer/mover/converter), formations, prompts.

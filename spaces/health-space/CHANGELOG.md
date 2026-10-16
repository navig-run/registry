# Health Space — Changelog

## [Unreleased] — registry publish

### Changed
- Added `.navig/space.json` (canonical manifest) and an MIT `LICENSE` (NAVIG contributors).
- Author/owner set to `navig-run`; space id aligned to the folder name in every manifest.
- Seed state ships as examples: `.navig/memory/*.example.json` (see `.navig/memory/README.md`) and `.navig/inbox/routes.example.yaml`.
- `.gitignore` keeps runtime memory, inbox and state out of version control.
- Added a `.gitignore` protecting health data (inbox/, out/, scans, memory, state).
- README reframed as a standalone space. Status → planned: no agents, skills or workflows ship yet.

## v1.0.0 — 2026-03-17

### Added
- Initial space structure
- Physical tracking schema
- Mental health signal model

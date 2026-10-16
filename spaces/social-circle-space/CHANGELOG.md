# Social Circle Space — Changelog

## [Unreleased] — registry publish

### Changed
- Added `.navig/space.json` (canonical manifest) and an MIT `LICENSE` (NAVIG contributors).
- Author/owner set to `navig-run`; space id aligned to the folder name in every manifest.
- Seed state ships as examples: `.navig/memory/*.example.json` (see `.navig/memory/README.md`) and `.navig/inbox/routes.example.yaml`.
- `.gitignore` keeps runtime memory, inbox and state out of version control.
- Status → planned: agents, packages and the graph view are not shipped. Quick start uses the real `navig contacts` commands.
- Default circles and the cold threshold unified (6 circles, 90 days); sample people replaced with neutral examples.

## v1.0.0 — 2026-03-17
### Added
- Initial space structure
- Contact graph schema
- Circle management system
- Interaction log pattern

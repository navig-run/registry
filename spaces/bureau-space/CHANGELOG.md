# Bureau Space — Changelog

## [Unreleased] — registry publish

### Changed
- Added `.navig/space.json` (canonical manifest) and an MIT `LICENSE` (NAVIG contributors).
- Author/owner set to `navig-run`; space id aligned to the folder name in every manifest.
- Seed state ships as examples: `.navig/memory/*.example.json` (see `.navig/memory/README.md`) and `.navig/inbox/routes.example.yaml`.
- `.gitignore` keeps runtime memory, inbox and state out of version control.
- Removed personal to-dos from the plans; de-duplicated pasted text; fixed the profile and folder references.
- Status → planned: the agents in the wiki guide are not shipped yet (filing works via `navig paperwork` / `navig cabinet`).

## v1.0.0 — 2026-03-17

### Added
- Initial space structure
- Document vault schema
- Deadline tracking pattern
- Dossier management workflow

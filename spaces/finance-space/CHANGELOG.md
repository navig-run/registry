# Changelog

## [Unreleased] — registry publish

### Changed
- Added `.navig/space.json` (canonical manifest) and an MIT `LICENSE` (NAVIG contributors).
- Author/owner set to `navig-run`; space id aligned to the folder name in every manifest.
- Seed state ships as examples: `.navig/memory/*.example.json` (see `.navig/memory/README.md`) and `.navig/inbox/routes.example.yaml`.
- `.gitignore` keeps runtime memory, inbox and state out of version control.
- Inbox routes rewritten in the schema the inbox loader reads; added `budgets/` and `goals/` templates.
- Doc fixes: weekly-spending day, sample tax year, retired `navig flow run` replaced by agent invocations.

## [1.0.0] — 2026-03-18

### Added
- Initial space structure with 4 agents, 3 formations, 4 skills, 3 workflows
- Budget tracking pipeline: import → categorize → variance analysis
- Monthly close workflow with savings update
- Tax prep checklist workflow
- Investment tracker with portfolio holdings model
- Savings goals data model with milestone alerts
- Weekly spending pace report
- Document archive structure organized by tax year

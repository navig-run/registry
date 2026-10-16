# Changelog — scribe-space

All notable changes to this space follow [Keep a Changelog](https://keepachangelog.com/) format.

## [Unreleased]

## [1.0.1] — 2026-10-16

### Fixed
- Skills take parameters from environment variables instead of pasting `{{...}}` into
  Python/shell code; `outline-draft` is one cross-platform step (it only had Windows steps).
- Workflows call skills with `skill:` steps; docs no longer reference the non-existent
  `navig skills run`.
- `config.yaml` points `skills_dir` at `.navig/skills/`; broken ops links fixed.
- Memory and inbox ship as `*.example.*` seeds; canonical manifest `.navig/space.json`.

### Removed
- Placeholder `screenshots/`, `scripts/`, `tests/` and `.github/` tooling.

## [1.0.0] — 2026-03-11

### Added
- Initial space scaffold with full NAVIG Space Runtime 2.0 schema
- 6 agents: storyteller, journalist, editor, content-strategist, screenwriter, tech-writer
- 4 formations: fiction-workshop, journalism-workflow, content-pipeline, production-draft
- 5 skills: word-count, grammar-check, outline-draft, export-pdf, readability-score
- 3 workflows: first-draft, editorial-review, publish-checklist
- 6 prompts: outline-chapter, interview-brief, scene-breakdown, api-doc-template, editorial-calendar, brand-voice-guide
- MCP config with LanguageTool, textstat, Pandoc, afterwriting, workspace-fs
- 6 sub-workspaces: book-writing, journalism, general-writing, screenwriting, technical-writing, content-strategy
- Wiki: README, architecture, agent-guide, runbooks

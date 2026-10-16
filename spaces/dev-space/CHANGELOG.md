# Changelog — NAVIG Dev Space

All notable changes to the `dev` space will be documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [1.0.0] — 2026-03-11

### Added

**Space scaffold**
- Initial space structure from the canonical NAVIG space template
- 4 agents: `coder`, `debugger`, `reviewer`, `scripter`
- 3 formations: `dev-workflow`, `review-cycle`, `extension-build`
- 4 skills: `code-lint`, `run-tests`, `scaffold-project`, `publish-extension`
- 3 workflows: `daily-standup`, `code-review`, `run-tests`
- 4 prompts: `scaffold-userscript`, `scaffold-extension`, `debug-session`, `code-review`

**Sub-workspaces**
- `userscripts-workshop/` — Greasemonkey/Tampermonkey starter with full metadata block
- `chrome-extensions-workshop/` — Manifest V3 extension skeleton with annotated files

**Wiki**
- `architecture.md` — Space design and layout reference
- `agent-guide.md` — Per-agent role, triggers, and invocation guide
- `runbooks.md` — Quick-reference runbooks for common dev tasks

# Changelog

## [Unreleased] — registry publish

### Changed
- Added `.navig/space.json` (canonical manifest) and an MIT `LICENSE` (NAVIG contributors).
- Author/owner set to `navig-run`; space id aligned to the folder name in every manifest.
- Seed state ships as examples: `.navig/memory/*.example.json` (see `.navig/memory/README.md`) and `.navig/inbox/routes.example.yaml`.
- `.gitignore` keeps runtime memory, inbox and state out of version control.
- Removed machine-specific backup paths, duplicated pasted blocks, `.github/` tooling and empty placeholder READMEs.
- README/GENESIS/manifests now describe what ships: `spaces/{health,growth,bureau}` are local data folders, not nested spaces.
- Skill scripts read parameters from `NAVIG_PARAM_*` environment variables instead of templating them into code; log-mood CSV column fix.

## [2.0.0] — 2026-03-12 (major upgrade)

### Added — Agents
- `growth-tracker` — Learning goals, books, courses, skill development
- `bureau-manager` — Documents, renewals, subscriptions, appointments

### Added — Formations
- `evening-reflection` — Daily wind-down, gratitude, journal, tomorrow intention
- `growth-ops` — Monthly learning review, quarterly deep review
- `bureau-ops` — Monthly renewal checks, subscription cost summary

### Added — Skills (7 new)
- `log-mood` — Mood and energy tracking
- `journal-entry` — Structured daily journal entries
- `track-learning` — Books, courses, articles logging
- `generate-habit-design` — Atomic Habits framework design
- `body-metrics-report` — Body metrics analysis over configurable period
- `renewal-check` — Upcoming renewal alerts with overdue detection
- `sleep-analysis` — Sleep consistency scoring and deficit detection

### Added — Workflows (3 new)
- `evening-reflection` — End-of-day wind-down workflow
- `monthly-growth-review` — Monthly learning and growth review
- `quarterly-life-review` — Quarterly all-domains life review

### Added — Prompts (6 new)
- `evening-reflection.md` — Evening reflection guide
- `monthly-growth-review.md` — Monthly growth review
- `quarterly-life-review.md` — Quarterly life review
- `habit-design.md` — Habit design using Atomic Habits framework
- `journal-entry.md` — Daily journal guide
- `goal-setting.md` — SMART goal setting

### Added — Wiki (4 new)
- `habit-science.md` — Atomic Habits framework reference
- `health-metrics-guide.md` — What to track, why, and how to interpret
- `growth-framework.md` — Learning system, book notes, reviews
- `bureau-guide.md` — Administrative life management guide

### Added — Domain Directories
- `spaces/health/` — Health subspace with README
- `spaces/growth/` — Growth subspace with README (journal/, retros/, books/)
- `spaces/bureau/` — Bureau subspace with README (ids/, subscriptions/, insurance/)

### Enhanced — Agents (3 rewrites)
- `daily-planner` — Added journal capability, mood check, quarterly review
- `wellness-tracker` — Added mood tracking, HRV, sleep analysis, body composition
- `habit-coach` — Added habit stacking, environment design, max 5 portfolio, monthly review

### Enhanced — Formations (2 rewrites)
- `morning-routine` — Added wellness-tracker, log-mood skill, mood threshold
- `health-ops` — Added habit-coach, mood/HRV triggers, 4 new skills

### Enhanced — Skills (2 rewrites)
- `log-health-metric` — Added mood_1_10 and HRV columns
- `check-habit-streak` — Added trend analysis, period filtering, streak calculation

### Enhanced — Workflows (2 rewrites)
- `daily-planning` — Added mood check, renewal glance, journal seed steps
- `weekly-health-review` — Added sleep analysis, body report, mood trend, habit review

### Enhanced — Prompts (2 rewrites)
- `daily-planning.md` — Added mood, habit streaks, renewal alerts, journal seed
- `weekly-retro.md` — Added health summary, habit adherence, learning log

### Enhanced — Wiki (3 rewrites)
- `README.md` — Full index with 5 agents, 5 formations, data files reference
- `agent-guide.md` — All 5 agents with full command examples
- `runbooks.md` — Expanded from 4 to 10 runbooks

### Enhanced — Config
- `config.yaml` — Added health metrics, journal, growth, bureau, inbox sections
- `context.md` — Expanded to 6 domains, 7 principles, 5-agent roster
- `space.manifest.json` — Updated to v2.0.0 with counts and paths
- `goals.json` — Expanded to 8 goals
- `known-issues.json` — Expanded to 4 issues
- `space-context.json` — Added mood, HRV, journal, bureau fields
- `inbox/routes.yaml` — Added #journal and #bureau channels with SLA

### Enhanced — Root Files
- `README.md` — Full v2.0.0 rewrite with agent roster, structure tree, quick start
- `PREVIEW.md` — Updated counts and highlights
- `package.json` — Bumped to 2.0.0 with metadata
- `.gitignore` — Extended for bureau, learning, and editor patterns

## [1.1.0] — 2026-03-11 (additive upgrade)

### Added
- `.navig/config.yaml`, `.navig/context.md`, `.navig/profile.json`
- `.navig/inbox/routes.yaml`
- `.navig/memory/goals.json`, `known-issues.json`, `space-context.json`
- `.navig/plans/CURRENT_PHASE.md`, `DEV_PLAN.md`
- `.navig/store/agents/` — `daily-planner`, `wellness-tracker`, `habit-coach`
- `.navig/store/formations/` — `morning-routine`, `health-ops`
- `.navig/store/mcp/workstation.mcp.json`
- `.navig/store/prompts/` — `daily-planning`, `weekly-retro`
- `.navig/store/workflows/` — `daily-planning`, `weekly-health-review`
- `.navig/wiki/` — README, agent-guide, runbooks
- `skills/log-health-metric.yaml`, `skills/check-habit-streak.yaml`
- `.github/instructions/` — MASTER.instructions.md, plugin-sdk.instructions.md
- `CHANGELOG.md`, `PREVIEW.md`, `package.json`, `LICENSE`, `.gitignore`
- `screenshots/SCREENSHOTS.md`, `tests/README.md`, `scripts/README.md`

### Preserved (unchanged)
- `README.md`, `space.manifest.json` (at root)
- `.navig/space-config.json`, `.navig/local-persona-override.json`
- `.navig/ops/README.md`
- All existing subspace structure under `spaces/`

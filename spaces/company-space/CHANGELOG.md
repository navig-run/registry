# Changelog

## [2.0.1] — 2026-10-16 (registry cleanup)

### Fixed
- Skills read their parameters from environment variables and company settings from
  `.navig/config.yaml` instead of pasting `{{...}}` placeholders into Python code.
- `triage-inbox` scans `.navig/inbox/` and no longer crashes when the folder is missing.
- Subspaces now match disk: `ops` and `projects` (the five standalone spaces are listed
  under "Pairs well with" instead).
- Memory and inbox ship as `*.example.*` seeds; canonical manifest `.navig/space.json`.

### Removed
- Empty `screenshots/`, `scripts/`, `tests/` placeholders, `.github/` tooling and the
  runtime `.navig/local-persona-override.json`.

## [2.0.0] — 2026-04-06 (Major Restructure — Full Business OS)

### Added — Agents (3 new)
- `chief` — Strategic Director, budget approval, OKRs, conflict arbitration
- `controller` — Finance & Compliance, invoicing, tax monitoring
- `sales` — Client Relations & Growth, lead qualification, outreach

### Added — Formations (4 new)
- `revenue-pipeline` — Quote → Invoice → Payment cycle
- `client-lifecycle` — Prospect → Client → Retention management
- `financial-review` — Monthly/quarterly financial analysis
- `strategic-planning` — OKRs, budget allocation, positioning

### Added — Skills (9 new)
- `generate-invoice` — Compliant invoicing with configurable numbering
- `generate-quote` — Professional quotes with acceptance block
- `expense-log` — Multi-category expense tracking
- `lead-qualify` — Scoring algorithm with priority routing
- `revenue-report` — Period-based revenue analysis with threshold alerts
- `expense-report` — Category/vendor/payment method breakdowns
- `tax-summary` — Quarterly tax prep and threshold monitoring
- `contract-draft` — Service contracts with configurable jurisdiction
- `meeting-minutes` — Structured minutes with action items

### Added — Workflows (5 new)
- `monthly-financial-close` — 7-step monthly close process
- `quarterly-review` — 8-step strategic review with OKR setting
- `lead-intake` — On-demand lead processing and routing
- `invoice-cycle` — 9-step quote-to-payment pipeline
- `tax-deadline-prep` — Tax declaration preparation (quarterly cron)

### Added — Prompts (6 new)
- `invoice-template` — Compliant invoice generation
- `quote-template` — Professional quote generation
- `client-outreach` — Multi-language client outreach drafting
- `proposal-brief` — Service proposal creation
- `monthly-report` — Monthly operations/financial report
- `quarterly-review` — Comprehensive quarterly business review

### Added — Wiki (4 new pages)
- `business-compliance-guide` — Legal and fiscal regime reference
- `invoicing-guide` — Numbering, compliance, billing cycle
- `client-management` — Pipeline, segments, lifecycle stages
- `financial-calendar` — Tax dates, deadlines, annual obligations

### Added — Domain Directories
- `clients/`, `contracts/`, `leads/`, `meetings/`
- `finance/invoices/`, `finance/quotes/`, `finance/expenses/`, `finance/tax/`, `finance/reports/`
- `reports/`

### Enhanced — Agents (2 rewritten to v2.0.0)
- `ops-manager` — Added meeting coordination, compliance monitoring, vendor management
- `project-lead` — Added budget burn tracking, scope change impact, profitability analysis

### Enhanced — Formations (1 rewritten)
- `company-ops` — Now includes all 5 agents, 10 skills, 6 workflows, 6 channels

### Enhanced — Skills (1 rewritten)
- `triage-inbox` — Auto-categorization with 5 domain keywords, priority scoring, SLA

### Enhanced — Workflows (1 rewritten)
- `weekly-ops-review` — Expanded from 4 to 8 steps (financial snapshot, invoice check, lead summary)

### Enhanced — Prompts (2 enhanced)
- `decision-log` — Added financial impact, reversibility, approved_by fields
- `project-kickoff` — Added budget, client, contract ref, billing schedule

### Enhanced — Wiki (3 rewritten)
- `README` — Full index with all domains, agents, formations, skills, workflows
- `agent-guide` — All 5 agents with invocation patterns and restrictions
- `runbooks` — Expanded from 3 to 8 runbooks

### Enhanced — Config
- `config.yaml` — Full business config (identity, finance, 21 expense categories, segments)
- `space-context.json` — Populated with business data (use {{VARIABLE}} placeholders)
- `context.md` — 6 domains, 5 agents, financial regime, 7 principles
- `space.manifest.json` — v2.0.0, 17 domain paths, accurate counts
- `space-config.json` — 5 widgets (revenue, pipeline, invoices, deadlines, expenses)
- `inbox/routes.yaml` — 6 channels with SLA and routing rules
- `goals.json` — 7 goals (4 new financial/compliance goals)
- `known-issues.json` — 4 issues resolved, 1 mitigated

### Updated — Root Files
- `README.md` — Complete rewrite reflecting v2.0.0 structure
- `PREVIEW.md` — Updated counts and capabilities
- `package.json` — Bumped to 2.0.0, added metadata
- `.gitignore` — Added financial and client data patterns

## [1.1.0] — 2026-03-11 (additive upgrade)

### Added
- `.navig/config.yaml` — space runtime config
- `.navig/context.md` — company context and guiding principles
- `.navig/profile.json` — `company_space` profile
- `.navig/inbox/routes.yaml` — channel routing rules
- `.navig/memory/goals.json`, `known-issues.json`, `space-context.json`
- `.navig/plans/CURRENT_PHASE.md`, `DEV_PLAN.md`
- `.navig/store/agents/` — `ops-manager`, `project-lead`
- `.navig/store/formations/` — `company-ops`
- `.navig/store/mcp/workstation.mcp.json`
- `.navig/store/prompts/` — `project-kickoff`, `decision-log`
- `.navig/store/workflows/weekly-ops-review.yaml`
- `.navig/wiki/` — README, agent-guide, runbooks
- `skills/triage-inbox.yaml`
- `.github/instructions/` — MASTER.instructions.md, plugin-sdk.instructions.md
- `CHANGELOG.md`, `PREVIEW.md`, `package.json`, `LICENSE`, `.gitignore`
- `screenshots/SCREENSHOTS.md`, `tests/README.md`, `scripts/README.md`

### Preserved (unchanged)
- `README.md`, `ops/README.md`
- `.navig/space-config.json`, `.navig/space.manifest.json`, `.navig/local-persona-override.json`
- All existing subspace structure under `spaces/`

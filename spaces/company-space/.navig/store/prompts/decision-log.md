# Decision Log Prompt

## Purpose
Create a structured Architecture/Business Decision Record (ADR) for logging significant decisions.
Includes financial impact assessment and reversibility analysis.

## Variables
- `{{DECISION_TITLE}}` — Short title of the decision
- `{{CONTEXT}}` — Background: what problem or situation prompted this decision
- `{{OPTIONS}}` — Options considered (comma-separated)
- `{{CHOSEN}}` — The option chosen
- `{{RATIONALE}}` — Why this option was chosen
- `{{PROJECT}}` — Project or area this decision pertains to
- `{{FINANCIAL_IMPACT}}` — Estimated cost/revenue impact (optional)
- `{{REVERSIBILITY}}` — Easy / Moderate / Difficult / Irreversible
- `{{APPROVED_BY}}` — Who approved: chief / controller / ops-manager / auto

## Prompt

You are a technical writer creating a structured decision record for {{COMPANY_NAME}}.

**Decision**: {{DECISION_TITLE}}
**Project/Area**: {{PROJECT}}
**Context**: {{CONTEXT}}
**Options considered**: {{OPTIONS}}
**Chosen**: {{CHOSEN}}
**Rationale**: {{RATIONALE}}
**Financial Impact**: {{FINANCIAL_IMPACT}}
**Reversibility**: {{REVERSIBILITY}}
**Approved by**: {{APPROVED_BY}}
**Date**: {{TODAY}}

Format as a standard ADR with sections:
1. **Status** — Proposed / Accepted / Superseded
2. **Context** — Why this decision was needed
3. **Options Considered** — Brief pros/cons for each option
4. **Decision** — What was decided
5. **Rationale** — Why this option
6. **Financial Impact** — One-time cost, recurring cost, revenue impact, ROI estimate
7. **Reversibility** — How easy to reverse, what it would cost, dependencies
8. **Consequences** — Positive and negative outcomes expected
9. **References** — Any linked docs, issues, or prior ADRs

Save-ready for `docs/decisions/ADR-{{NNN}}-{{DECISION_TITLE}}.md`.

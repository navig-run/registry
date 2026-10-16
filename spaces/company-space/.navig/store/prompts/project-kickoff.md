# Project Kickoff Prompt

## Purpose
Generate a complete project spec with milestones, done criteria, budget, client context,
risks, and ADR log entry for a new project.

## Variables
- `{{PROJECT_NAME}}` — Name of the project
- `{{GOAL}}` — One-sentence project goal
- `{{DEADLINE}}` — Target completion date (YYYY-MM-DD)
- `{{STAKEHOLDERS}}` — Comma-separated stakeholder list
- `{{CONSTRAINTS}}` — Key constraints (budget, time, tech)
- `{{BUDGET}}` — Total project budget
- `{{CLIENT}}` — Client name (or "internal" for internal projects)
- `{{CONTRACT_REF}}` — Contract reference if applicable
- `{{SERVICE_LINES}}` — Service lines involved (comma-separated)

## Prompt

You are a project lead at {{COMPANY_NAME}} creating a project specification document.

**Project**: {{PROJECT_NAME}}
**Goal**: {{GOAL}}
**Deadline**: {{DEADLINE}}
**Budget**: {{BUDGET}} {{CURRENCY}}
**Client**: {{CLIENT}}
**Contract**: {{CONTRACT_REF}}
**Service Lines**: {{SERVICE_LINES}}
**Stakeholders**: {{STAKEHOLDERS}}
**Constraints**: {{CONSTRAINTS}}

Generate:

1. **Project Summary** — 3 sentences: what, why, success criteria
2. **Client Context** — Who the client is, their goals, relationship history
3. **Done Criteria** — 3–5 measurable conditions that mean "done"
4. **Milestones** — 4–6 milestones with dates working back from {{DEADLINE}}
5. **Budget Breakdown** — Allocation by phase/milestone, buffer percentage
6. **Risks** — Top 3 risks with likelihood (H/M/L), impact (H/M/L), financial exposure, and mitigation
7. **Initial ADR** — Architecture/approach decision record: what approach was chosen and why
8. **Open Questions** — 3–5 questions that must be answered before work starts
9. **Billing Schedule** — When invoices will be generated (aligned with milestones)

Format as markdown, save-ready for `.navig/plans/briefs/{{PROJECT_NAME}}/spec.md`.

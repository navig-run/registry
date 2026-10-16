# Runbooks

> Standard operating procedures for recurring business scenarios.
> Each runbook has a trigger condition, responsible agent, and step-by-step process.

---

## RB-001 — Inbox Backlog Processing

**When**: Inbox items accumulate >48 hours unactioned
**Agent**: ops-manager
**Channel**: #ops

```
1. @ops-manager triage --inbox company
2. Auto-categorize by domain keywords (finance/sales/projects/strategic/ops)
3. Assign priority: high (>48h or "urgent"/"critical" keyword), medium, low
4. Route to responsible agent per inbox/routes.yaml:
   - Financial → controller (#finance)
   - Sales/leads → sales (#sales)
   - Projects → project-lead (#projects)
   - Strategic → chief (#strategic)
   - Ops/general → ops-manager (#ops)
5. Items requiring decisions → create ADR draft in docs/decisions/
6. Archive processed items
7. Report: items triaged, overdue count, routing summary
```

## RB-002 — New Project Kickoff

**When**: New project approved to start (budget + done criteria defined)
**Agent**: project-lead
**Channel**: #projects

```
1. Confirm prerequisites: budget defined, done criteria set, client identified
2. @project-lead kickoff --project "<NAME>" --budget <AMOUNT> --client "<CLIENT>"
3. Use project-kickoff prompt to generate spec
4. Review: done criteria measurable? Budget breakdown realistic? Timeline feasible?
5. Save spec to .navig/plans/briefs/<name>/spec.md
6. Create initial ADR for architecture/approach decision
7. Notify #projects + #ops
8. If client project: notify sales for billing schedule coordination
```

## RB-003 — Decision Recording (ADR)

**When**: A significant decision has been made or needs to be made
**Agent**: ops-manager (creates) + chief (approves if financial impact)
**Channel**: #ops → #strategic (if financial)

```
1. Use decision-log prompt with all variables
2. @ops-manager create-adr --decision "<TITLE>" --project "<PROJECT>"
3. Fill: context, options, rationale, financial impact, reversibility
4. If high financial impact: route to chief for approval
5. Save to docs/decisions/ADR-NNN-<title>.md
6. Link ADR from relevant project spec
7. Update goals.json decision log hygiene goal
```

## RB-004 — Invoice Generation

**When**: Service delivered or milestone reached per contract
**Agent**: controller
**Channel**: #finance

```
1. Verify: project/milestone complete, client accepts deliverable
2. @controller generate-invoice --client "<CLIENT>" --amount <AMOUNT>
3. Determine next sequential number: scan finance/invoices/
4. Use invoice-template prompt with all required fields
5. Save to finance/invoices/{{INVOICE_PREFIX}}-YYYY-NNN.md
6. Send to client (email / client portal)
7. Set payment tracking: due date = +30 days
8. Schedule follow-up reminders: 30d, 45d (escalate chief), 60d (formal notice)
```

## RB-005 — New Lead Processing

**When**: New inquiry or prospect identified
**Agent**: sales
**Channel**: #sales

```
1. @sales qualify-lead --name "<NAME>" --company "<COMPANY>" --budget "<RANGE>"
2. Score lead using lead-qualify skill:
   - Base 5 + timeline bonus (0-2) + budget bonus (0-2) + source bonus (0-1)
   - Priority: ≥8 high, ≥5 medium, <5 low
3. Check existing client records in clients/
4. If existing client: add to client record, route to account manager
5. Create lead record in leads/LEAD-<DATE>-<slug>.md
6. Route by priority:
   - High (≥8): immediate proposal, notify chief + sales
   - Medium (5-7): schedule intro call, sales follow-up in 48h
   - Low (<5): add to nurture list, monthly check-in
7. If high-budget: notify chief
```

## RB-006 — Monthly Financial Close

**When**: 1st business day of each month
**Agent**: controller
**Channel**: #finance → #strategic

```
1. @controller revenue-report --period <YYYY-MM>
2. @controller expense-report --period <YYYY-MM>
3. Reconcile: all invoices match payments, all expenses categorized
4. Calculate P&L: Revenue - Expenses - Tax ({{TAX_RATE}})
5. Check tax thresholds: YTD revenue vs {{TAX_THRESHOLD_1}} and {{TAX_THRESHOLD_2}}
6. Alert if either >80%
7. Use monthly-report prompt to compile full report
8. Save to reports/monthly/YYYY-MM-report.md
9. Notify controller + chief
```

## RB-007 — Tax Declaration Prep

**When**: 20th of quarter-end months (Mar, Jun, Sep, Dec)
**Agent**: controller
**Channel**: #finance

```
1. @controller tax-summary --quarter <Q>
2. Pull all invoices for quarter
3. Validate: sequential numbering intact, no gaps
4. Sum quarterly revenue
5. Calculate tax contribution: revenue × {{TAX_RATE}}
6. Pull all expenses for quarter — verify categorized + receipts attached
7. Check tax threshold projection for remaining year
8. Prepare declaration summary
9. Save to finance/tax/TAX-YYYY-QN.md
10. Notify controller (action: submit declaration)
11. Notify chief (info: quarterly tax summary)
```

## RB-008 — Client Offboarding / Project Closure

**When**: Project completed and final invoice paid
**Agent**: ops-manager + project-lead
**Channel**: #ops → #projects

```
1. @project-lead retro --project "<PROJECT>"
2. Confirm: all deliverables accepted, all invoices paid, no open issues
3. Archive project files (move to completed/)
4. Update client record with:
   - Project summary and outcome
   - Total billed and paid
   - Satisfaction notes
   - Re-engagement opportunity date
5. @ops-manager update-records --project "<PROJECT>" --status "completed"
6. If client relationship ongoing: hand back to sales for retention / upsell
7. Update project progress in space-context.json
8. Create final ADR if significant decisions were made
```

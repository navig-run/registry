# Monthly Report Prompt

## Purpose
Generate a comprehensive monthly operations and financial report.
Combines financial data, project status, client pipeline, and operational metrics.

## Variables
- `{{MONTH}}` — Report month (YYYY-MM)
- `{{REVENUE_TOTAL}}` — Total revenue for the month
- `{{EXPENSE_TOTAL}}` — Total expenses for the month
- `{{INVOICES_ISSUED}}` — Number of invoices issued
- `{{INVOICES_PAID}}` — Number of invoices paid
- `{{INVOICES_OVERDUE}}` — Number of overdue invoices (>30 days)
- `{{ACTIVE_PROJECTS}}` — List of active projects with status %
- `{{LEADS_NEW}}` — New leads this month
- `{{LEADS_CONVERTED}}` — Leads converted to clients
- `{{KEY_EVENTS}}` — Notable events, wins, or issues (comma-separated)
- `{{THRESHOLD_1_YTD_PERCENT}}` — YTD revenue as % of first tax threshold
- `{{THRESHOLD_2_YTD_PERCENT}}` — YTD revenue as % of second tax threshold (if applicable)

## Prompt

You are the ops-manager at {{COMPANY_NAME}} preparing the monthly operations report.
This report is reviewed by the chief (strategic director) and controller (finance).

**Reporting Period**: {{MONTH}}

Generate a structured monthly report:

1. **Executive Summary** — 3-4 sentences: month in review, key numbers, outlook
2. **Financial Overview**
   - Revenue: {{REVENUE_TOTAL}} {{CURRENCY}}
   - Expenses: {{EXPENSE_TOTAL}} {{CURRENCY}}
   - Net: (calculated)
   - Tax contribution estimate ({{TAX_RATE}} of revenue)
   - Threshold 1 status: {{THRESHOLD_1_YTD_PERCENT}}%
   - Threshold 2 status: {{THRESHOLD_2_YTD_PERCENT}}%
   - ⚠️ Flag if either >80%
3. **Invoicing Status**
   - Issued: {{INVOICES_ISSUED}} | Paid: {{INVOICES_PAID}} | Overdue: {{INVOICES_OVERDUE}}
   - List overdue invoices with amounts and days overdue
   - Action items for collection
4. **Project Status**
   {{ACTIVE_PROJECTS}}
   - For each: name, progress %, on-track/at-risk/delayed, key milestone this month
5. **Client Pipeline**
   - New leads: {{LEADS_NEW}}
   - Converted: {{LEADS_CONVERTED}}
   - Pipeline value estimate
   - Top prospects
6. **Key Events & Decisions**
   {{KEY_EVENTS}}
   - Wins, losses, new contracts, completed projects
7. **Operational Metrics**
   - Inbox health (items triaged vs backlog)
   - Meeting count
   - Decision records created
8. **Next Month Outlook**
   - Expected revenue (signed contracts + pipeline)
   - Key deadlines (tax filings, client deliveries)
   - Action items carried forward
9. **Appendix** — Links to source data (invoice folder, expense reports)

**Tone**: Factual, concise. Numbers first, narrative second.
Use tables for financial data. Use bullet lists for status items.

Format as markdown, save-ready for `reports/monthly/{{MONTH}}-report.md`.

# Quarterly Review Prompt

## Purpose
Generate a comprehensive quarterly business review.
Strategic-level analysis covering financials, OKRs, client portfolio, market positioning,
and forward planning.

## Variables
- `{{QUARTER}}` — Quarter identifier (e.g., 2025-Q2)
- `{{REVENUE_Q}}` — Quarterly revenue
- `{{EXPENSE_Q}}` — Quarterly expenses
- `{{REVENUE_YTD}}` — Year-to-date revenue
- `{{CLIENTS_ACTIVE}}` — Number of active clients
- `{{CLIENTS_NEW}}` — New clients acquired this quarter
- `{{CLIENTS_CHURNED}}` — Clients lost this quarter
- `{{PROJECTS_COMPLETED}}` — Projects completed this quarter
- `{{PROJECTS_ACTIVE}}` — Currently active projects
- `{{OKR_STATUS}}` — Current OKR progress summary
- `{{THRESHOLD_1_YTD_PERCENT}}` — YTD revenue as % of first tax threshold
- `{{THRESHOLD_2_YTD_PERCENT}}` — YTD revenue as % of second tax threshold
- `{{TAX_PAID}}` — Tax contributions paid this quarter
- `{{KEY_WINS}}` — Notable achievements (comma-separated)
- `{{KEY_CHALLENGES}}` — Major challenges encountered (comma-separated)

## Prompt

You are the chief (strategic director) of {{COMPANY_NAME}} conducting the quarterly review.
This is the most important recurring strategic document. It drives planning for the next quarter.

**Quarter**: {{QUARTER}}

Generate a comprehensive quarterly review:

## Part 1: Financial Performance

1. **Revenue Analysis**
   - Quarterly revenue: {{REVENUE_Q}} {{CURRENCY}}
   - YTD revenue: {{REVENUE_YTD}} {{CURRENCY}}
   - Revenue by service line (breakdown %)
   - Revenue by client (top 5)
   - Comparison to previous quarter (trend)
2. **Expense Analysis**
   - Quarterly expenses: {{EXPENSE_Q}} {{CURRENCY}}
   - Top expense categories
   - Expense ratio (expenses / revenue %)
3. **Profitability**
   - Gross margin
   - Net after tax ({{TAX_RATE}}): calculated
   - Tax paid: {{TAX_PAID}} {{CURRENCY}}
4. **Compliance Status**
   - Threshold 1: {{THRESHOLD_1_YTD_PERCENT}}%
   - Threshold 2: {{THRESHOLD_2_YTD_PERCENT}}%
   - ⚠️ Projections: will thresholds be hit by year-end?
   - Action required if >80%

## Part 2: Client Portfolio

5. **Client Health**
   - Active: {{CLIENTS_ACTIVE}} | New: {{CLIENTS_NEW}} | Churned: {{CLIENTS_CHURNED}}
   - Net client growth
   - Client satisfaction signals
6. **Pipeline Health**
   - Leads in pipeline
   - Pipeline value
   - Conversion rate this quarter
   - Top 3 prospects for next quarter

## Part 3: Delivery & Operations

7. **Project Performance**
   - Completed: {{PROJECTS_COMPLETED}} | Active: {{PROJECTS_ACTIVE}}
   - On-time delivery rate
   - Budget adherence
   - Profitability per project (where data available)
8. **Operational Efficiency**
   - Average response time (inbox/leads)
   - Decision velocity (ADRs created/resolved)
   - Process improvements implemented

## Part 4: Strategy

9. **OKR Review**
   {{OKR_STATUS}}
   - Score each objective (0.0–1.0)
   - What worked / what didn't
   - Carry-forward items
10. **Wins & Challenges**
    - Wins: {{KEY_WINS}}
    - Challenges: {{KEY_CHALLENGES}}
    - Lessons learned
11. **Market & Competitive Landscape**
    - Industry trends affecting the business
    - Competitive positioning changes
    - New opportunities identified
12. **Next Quarter Plan**
    - Draft OKRs (3 objectives, 3 key results each)
    - Revenue target
    - Key initiatives
    - Resource allocation
    - Risk mitigation

## Part 5: Decisions Required

13. **Open Decisions** — Items requiring resolution before next quarter
    - Pricing adjustments
    - Service line expansion/contraction
    - Tool/infrastructure changes
    - Hiring or subcontracting needs

**Tone**: Strategic, data-driven. Lead with numbers, follow with insight.
Use tables for financial comparisons. Use chart descriptions where visuals would help.

Format as markdown, save-ready for `reports/quarterly/{{QUARTER}}-review.md`.

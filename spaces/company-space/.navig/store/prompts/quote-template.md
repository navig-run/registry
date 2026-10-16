# Quote Template Prompt

## Purpose
Generate a professional quote / estimate for services.
Uses sequential {{QUOTE_PREFIX}}-YYYY-NNN numbering. Valid 30 days by default.

## Variables
- `{{QUOTE_NUMBER}}` — Sequential number {{QUOTE_PREFIX}}-YYYY-NNN (auto-generated from last quote)
- `{{CLIENT_NAME}}` — Full legal name of the client
- `{{CLIENT_ADDRESS}}` — Client address
- `{{CLIENT_CONTACT}}` — Contact person name and email
- `{{ISSUE_DATE}}` — Quote issue date (YYYY-MM-DD)
- `{{VALID_UNTIL}}` — Expiry date (default: +30 days)
- `{{PROJECT_NAME}}` — Project or engagement name
- `{{SERVICE_LINES}}` — Services offered (line items)
- `{{AMOUNTS}}` — Amount per line item
- `{{TOTAL}}` — Total quoted amount
- `{{TIMELINE}}` — Estimated delivery timeline
- `{{PAYMENT_SCHEDULE}}` — Payment milestones (e.g., 30% upfront, 70% on delivery)
- `{{NOTES}}` — Special conditions or notes (optional)

## Prompt

You are the sales agent of {{COMPANY_NAME}} creating a professional quote.

**Quote N°**: {{QUOTE_NUMBER}}
**Date**: {{ISSUE_DATE}}
**Valid Until**: {{VALID_UNTIL}}
**Project**: {{PROJECT_NAME}}

**From**:
{{COMPANY_NAME}} — {{OWNER_NAME}}
{{COMPANY_TYPE}}
ID: {{COMPANY_ID}}
{{COMPANY_ADDRESS}}
Email: {{COMPANY_EMAIL}} — Tel: {{COMPANY_PHONE}}

**To**:
{{CLIENT_NAME}}
{{CLIENT_ADDRESS}}
Contact: {{CLIENT_CONTACT}}

Generate a formatted quote with:

1. **Header** — Company name, quote number, dates, validity period
2. **Parties** — Sender and Client blocks
3. **Project Description** — Brief project overview and objectives
4. **Line Items Table** — Description | Qty | Unit Price | Total
5. **Total** — Total amount in {{CURRENCY}}
6. **Legal Mention** — Tax compliance statement for {{JURISDICTION}}
7. **Timeline** — Estimated start date, milestones, delivery
8. **Payment Schedule** — {{PAYMENT_SCHEDULE}}
9. **General Terms**:
   - Quote validity: 30 days
   - Payment terms: bank transfer
   - Late payment penalties per applicable law
   - Intellectual property: transfers upon final delivery and full payment
10. **Acceptance Block**:
    ```
    Accepted and agreed — Date: ___________

    Client name and signature:

    ___________________________________
    ```
11. **Notes** — {{NOTES}}

Format as markdown, save-ready for `finance/quotes/{{QUOTE_NUMBER}}.md`.

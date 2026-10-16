# Invoice Template Prompt

## Purpose
Generate a compliant invoice for services rendered.
Follows sequential {{INVOICE_PREFIX}}-YYYY-NNN numbering.

## Variables
- `{{INVOICE_NUMBER}}` — Sequential number {{INVOICE_PREFIX}}-YYYY-NNN (auto-generated from last invoice)
- `{{CLIENT_NAME}}` — Full legal name of the client
- `{{CLIENT_ADDRESS}}` — Client address (street, postal code, city, country)
- `{{CLIENT_ID}}` — Client business registration number (if applicable)
- `{{ISSUE_DATE}}` — Invoice issue date (YYYY-MM-DD)
- `{{DUE_DATE}}` — Payment due date (default: +30 days from issue)
- `{{SERVICE_LINES}}` — Services rendered (line items)
- `{{AMOUNTS}}` — Amount per line item
- `{{TOTAL}}` — Total amount
- `{{QUOTE_REF}}` — Related quote reference (optional)
- `{{PROJECT_REF}}` — Project name or reference (optional)
- `{{NOTES}}` — Additional notes (optional)

## Prompt

You are the finance controller of {{COMPANY_NAME}} generating a professional invoice.

**Invoice Number**: {{INVOICE_NUMBER}}
**Date**: {{ISSUE_DATE}}
**Due Date**: {{DUE_DATE}}
**Quote Reference**: {{QUOTE_REF}}
**Project**: {{PROJECT_REF}}

**From**:
{{COMPANY_NAME}} — {{OWNER_NAME}}
{{COMPANY_TYPE}}
ID: {{COMPANY_ID}}
{{COMPANY_ADDRESS}}
Email: {{COMPANY_EMAIL}} — Tel: {{COMPANY_PHONE}}

**To**:
{{CLIENT_NAME}}
{{CLIENT_ADDRESS}}
ID: {{CLIENT_ID}}

**Services**:
{{SERVICE_LINES}} — {{AMOUNTS}}

**Total**: {{TOTAL}} {{CURRENCY}}

Generate a formatted invoice with:

1. **Header** — Company logo area, invoice number, dates
2. **Parties** — Sender and Client blocks with all legal details
3. **Line Items Table** — Description | Qty | Unit Price | Total
4. **Total** — Total amount (add tax line if applicable per jurisdiction)
5. **Legal Mentions** — Required compliance statements for {{JURISDICTION}}
6. **Payment Terms** — Payment due within 30 days of issue date
7. **Payment Methods** — Bank transfer (details on file)
8. **Late Payment** — Late payment penalties per applicable law
9. **Notes** — {{NOTES}}

## Compliance Checklist
- [ ] Sequential numbering (no gaps allowed)
- [ ] Sender identification complete
- [ ] Client identification complete
- [ ] Legal compliance mentions present
- [ ] Late payment terms present
- [ ] Issue date and due date present
- [ ] Service description clear and detailed

Format as markdown, save-ready for `finance/invoices/{{INVOICE_NUMBER}}.md`.

# Invoicing Guide

> Complete reference for invoice and quote generation, numbering, compliance,
> and the full billing cycle from quote to payment.

---

## Numbering Systems

### Invoices — {{INVOICE_PREFIX}}-YYYY-NNN

| Field | Rule |
|-------|------|
| **Prefix** | `{{INVOICE_PREFIX}}` |
| **Year** | 4-digit year |
| **Sequence** | 3-digit zero-padded, starting at 001 each year |
| **Example** | {{INVOICE_PREFIX}}-2025-001, {{INVOICE_PREFIX}}-2025-002 |
| **Reset** | Counter resets on January 1st |
| **Gaps** | Absolutely forbidden. If cancelled → issue credit note |

### Quotes — {{QUOTE_PREFIX}}-YYYY-NNN

| Field | Rule |
|-------|------|
| **Prefix** | `{{QUOTE_PREFIX}}` |
| **Year** | 4-digit year |
| **Sequence** | 3-digit zero-padded, starting at 001 each year |
| **Example** | {{QUOTE_PREFIX}}-2025-001, {{QUOTE_PREFIX}}-2025-002 |
| **Validity** | 30 days from issue date (default) |

### Expenses — {{EXPENSE_PREFIX}}-YYYY-NNN

| Field | Rule |
|-------|------|
| **Prefix** | `{{EXPENSE_PREFIX}}` |
| **Year** | 4-digit year |
| **Sequence** | 3-digit zero-padded |
| **Example** | {{EXPENSE_PREFIX}}-2025-001, {{EXPENSE_PREFIX}}-2025-002 |

---

## Invoice Compliance Checklist

Before issuing ANY invoice, verify all mandatory fields:

- [ ] **Invoice number** — {{INVOICE_PREFIX}}-YYYY-NNN, sequential from last issued
- [ ] **Issue date**
- [ ] **Due date** — Default: +30 calendar days from issue date
- [ ] **Sender block** — {{COMPANY_NAME}}, {{OWNER_NAME}}, {{COMPANY_ID}}, full address
- [ ] **Client block** — Full legal name, address, registration number (if B2B)
- [ ] **Service description** — Clear, detailed description of work performed
- [ ] **Line items** — Description, quantity, unit price, line total
- [ ] **Total** — Sum of all line items
- [ ] **Tax compliance statement** — Per jurisdiction requirements
- [ ] **Late payment penalties** — Per applicable law
- [ ] **Payment method** — Bank transfer or as configured

---

## Quote Compliance Checklist

- [ ] **Quote number** — {{QUOTE_PREFIX}}-YYYY-NNN, sequential
- [ ] **Issue date**
- [ ] **Validity** — 30 days or custom period
- [ ] **Sender block** — Full company details + registration ID
- [ ] **Client block** — Name, company, address
- [ ] **Project description** — What will be delivered
- [ ] **Line items** — Services, quantities, unit prices
- [ ] **Total**
- [ ] **Tax compliance statement**
- [ ] **Payment schedule** — E.g., 30% upfront, 70% on delivery
- [ ] **General terms** — Payment terms, IP transfer, penalties
- [ ] **Acceptance block** — Signature + date space

---

## Billing Cycle Workflow

```
1. QUALIFY (sales)
   └── Lead scored, budget confirmed, services identified

2. QUOTE (sales + controller)
   └── {{QUOTE_PREFIX}}-YYYY-NNN generated and sent to client
   └── Valid 30 days

3. ACCEPTANCE (client)
   └── Client signs acceptance
   └── Quote becomes binding contract

4. DELIVERY (project-lead)
   └── Work performed per spec
   └── Milestones tracked

5. INVOICE (controller)
   └── {{INVOICE_PREFIX}}-YYYY-NNN generated per milestone/completion
   └── Sent to client
   └── Payment tracking starts

6. PAYMENT TRACKING (controller)
   └── Due: +30 days from invoice date
   └── Monitor payment receipt

7. REMINDERS (controller → chief)
   └── +30 days: First reminder (friendly)
   └── +45 days: Second reminder (formal), escalate to chief
   └── +60 days: Formal demand

8. CLOSE (controller)
   └── Payment received → mark invoice as paid
   └── Update revenue records
```

---

## Service Lines & Pricing

Configure your service lines in `config.yaml` under `services`. Typical structure:

| Service | Description | Typical Engagement |
|---------|-------------|-------------------|
| *Your service 1* | Description | Project-based or retainer |
| *Your service 2* | Description | Project-based or retainer |
| *Your service 3* | Description | One-off or monthly |

---

## Credit Notes

When an invoice needs correction:

1. **Never modify** an issued invoice
2. Issue a credit note referencing the original invoice
3. Reference: "Credit note for invoice {{INVOICE_PREFIX}}-YYYY-NNN dated [date]"
4. Issue replacement invoice if needed

---

## Revenue Tracking

All invoices contribute to YTD revenue tracked against:
- Tax Threshold 1: {{TAX_THRESHOLD_1}} (alert at 80%)
- Tax Threshold 2: {{TAX_THRESHOLD_2}} (alert at 80%)

Track revenue on both invoice date and payment date for accurate reporting.

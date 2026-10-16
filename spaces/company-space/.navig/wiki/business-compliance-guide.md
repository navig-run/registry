# Business Compliance Guide

> Reference for legal and fiscal obligations under the company's business registration.
> Customize all {{VARIABLE}} placeholders to match your jurisdiction and entity type.

---

## Legal Identity

| Field | Value |
|-------|-------|
| **Entity** | {{COMPANY_NAME}} — {{OWNER_NAME}} |
| **Type** | {{COMPANY_TYPE}} |
| **Registration ID** | {{COMPANY_ID}} |
| **Address** | {{COMPANY_ADDRESS}} |
| **Founded** | {{FOUNDED_YEAR}} |

---

## Tax Regime Rules

### Revenue Thresholds

| Threshold | Amount | Impact |
|-----------|--------|--------|
| **Tax Threshold 1** | {{TAX_THRESHOLD_1}} | Below: simplified tax regime. Above: must register for full tax |
| **Tax Threshold 2** | {{TAX_THRESHOLD_2}} | Below: small business regime. Above: must switch to standard regime |

**Critical**: Monitor YTD revenue monthly. Alert at >80% of either threshold.

### Tax Contributions

| Parameter | Value |
|-----------|-------|
| **Rate** | {{TAX_RATE}} on revenue |
| **Declaration** | Per jurisdiction schedule (quarterly or monthly) |
| **Calculation** | Total period revenue × {{TAX_RATE}} = contribution due |

---

## Invoicing Obligations

### Mandatory Invoice Fields

Every invoice MUST contain:

1. ✅ Invoice number — sequential, chronological, no gaps ({{INVOICE_PREFIX}}-YYYY-NNN)
2. ✅ Invoice date
3. ✅ Seller identification — name, registration ID, address
4. ✅ Buyer identification — name/company, address
5. ✅ Service description — detailed enough to identify what was delivered
6. ✅ Quantity and unit price
7. ✅ Total amount
8. ✅ Tax compliance statement (per jurisdiction)
9. ✅ Payment terms — deadline (default: 30 days from invoice date)
10. ✅ Late payment penalties per applicable law

### Numbering Rules

- **Format**: `{{INVOICE_PREFIX}}-YYYY-NNN` (e.g., {{INVOICE_PREFIX}}-2025-001)
- **Sequential**: Numbers must follow in chronological order
- **No gaps**: Never skip a number. If cancelled, issue credit note
- **Per year**: Counter resets on January 1st

### Quote Requirements

- **Format**: `{{QUOTE_PREFIX}}-YYYY-NNN`
- **Validity**: 30 days (default)
- **Acceptance**: Client signs acceptance with date
- **Binding**: Once signed, quote becomes a binding contract

---

## Document Retention

| Document Type | Retention Period |
|---------------|-----------------|
| Invoices (issued) | Per jurisdiction (typically 7-10 years) |
| Invoices (received) | Per jurisdiction (typically 7-10 years) |
| Quotes | Same as invoices |
| Expense receipts | Same as invoices |
| Contracts | Per jurisdiction after end of contract |
| Tax declarations | Per jurisdiction (typically 6-7 years) |
| Bank statements | Per jurisdiction |

**Rule**: Never delete financial documents. Archive after active period.

---

## Late Payment Rules

### Penalties

- **Rate**: Per jurisdiction (typically statutory interest rate × multiplier)
- **When**: Applied from day after due date
- **No notice required**: Penalties are due automatically in most jurisdictions

### Collection Timeline

| Day | Action |
|-----|--------|
| Due date | Payment expected |
| +1 day | Late penalties start accruing |
| +7 days | Friendly reminder (email) |
| +30 days | Formal reminder |
| +45 days | Escalate to chief, send formal letter |
| +60 days | Formal demand |
| +90 days | Consider legal action |

---

## Annual Obligations

| When | Obligation |
|------|-----------|
| **Start of Year** | Confirm business status, declare previous year revenue |
| **Quarterly** | Tax declaration + payment |
| **Tax Season** | Annual income tax declaration |
| **Ongoing** | Maintain revenue ledger |
| **Ongoing** | Maintain purchase/expense ledger |

---

## Expense Categories (21)

| # | Category | Examples |
|---|----------|----------|
| 1 | `domain-hosting` | Domain renewals, hosting, CDN |
| 2 | `software-licenses` | Development tools, design tools |
| 3 | `hardware` | Computer equipment, peripherals |
| 4 | `office-supplies` | Paper, pens, office materials |
| 5 | `professional-services` | Accountant, legal counsel |
| 6 | `marketing-advertising` | Ads, campaigns |
| 7 | `travel-transport` | Travel, fuel, parking |
| 8 | `meals-entertainment` | Client lunches, team meals |
| 9 | `telecommunications` | Phone, internet |
| 10 | `insurance` | Professional liability |
| 11 | `training-education` | Courses, certifications, books |
| 12 | `subscriptions-saas` | SaaS tools, monitoring |
| 13 | `banking-fees` | Bank charges, transfer fees |
| 14 | `coworking` | Workspace rental |
| 15 | `printing` | Business cards, brochures |
| 16 | `shipping` | Postal, courier |
| 17 | `subcontracting` | Freelancer payments |
| 18 | `networking-events` | Conferences, meetups |
| 19 | `legal-fees` | Contract review, trademark |
| 20 | `taxes-contributions` | Business taxes, social contributions |
| 21 | `miscellaneous` | Uncategorized (minimize use) |

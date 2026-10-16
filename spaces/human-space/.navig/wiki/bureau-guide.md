# Bureau Guide

## What is Bureau?

Bureau is the administrative life management domain — the unsexy but essential paperwork, renewals, subscriptions, and appointments that keep life running smoothly.

## Categories

| Category | Examples |
|----------|----------|
| **id** | Passport, driver's licence, national ID, residence permit |
| **subscription** | Streaming services, software, gym, memberships |
| **insurance** | Health, car, home, life, travel |
| **medical** | Doctor checkups, dental, eye exams, vaccinations |
| **tax** | Annual filing deadlines, quarterly estimates, documents needed |
| **vehicle** | Registration, inspection, insurance renewal, maintenance |
| **housing** | Lease renewal, utilities, maintenance contracts |
| **other** | Warranties, certificates, professional licences |

## Data File

All renewals tracked in `spaces/bureau/renewals.csv`:
```
item,category,due_date,cost,auto_renew,notes
Passport,id,2028-06-15,,no,Check 6 months before expiry
Netflix,subscription,2026-02-01,15.99,yes,Monthly billing
```

## Where the documents themselves live

The **scans and PDFs** — passport, ID card, residence permit, insurance policies, medical
records, vehicle papers — go in the encrypted cabinet, not in this space:

```bash
navig cabinet add passport-scan.pdf --category identity --expires 2031-05-01
navig cabinet add ~/Scans/insurance/ --category insurance
navig cabinet search "policy number"      # finds words inside the scans
navig cabinet expiring --within 60         # documents due for renewal
```

Everything in the cabinet is encrypted (file, title, tags and the OCR text), searchable
by content, and restorable anywhere from one backup (`navig cabinet backup`). This space
keeps only what you work with day to day:

```
spaces/bureau/
  renewals.csv          # Subscriptions, appointments, anything without a document
  subscriptions/        # Subscription details (no scans of IDs or policies)
  tax/                  # Working notes for filings
```

Incoming paper mail (tax office, health insurer, utilities, local authorities…) is filed with `navig paperwork scan
<folder> --space human-space --profile personal`; any ID or medical document it finds is
encrypted into the cabinet by `navig paperwork handoff --yes`.

## Security Rules

- **Scans never live in this space.** `navig cabinet add` them; the originals can then be
  deleted. The `.gitignore` still excludes the old scan folders (`spaces/bureau/ids/`,
  `medical/`, `insurance/`, `vehicle/`, `spaces/health/records/`) as a backstop.
- **Back the cabinet up** to a second drive: `navig cabinet backup -o <file>`. A cabinet
  locked to this computer does not survive a reinstall.
- Keep physical originals in a safe location.

## Workflows

### Monthly Renewal Check (1st of month)
```
@bureau-manager renewals --days-ahead 60
```
Shows all items due within next 60 days + any overdue.

### Subscription Cost Report
```
@bureau-manager subscriptions --action cost-report
```
Summarises total monthly/annual subscription spend.

### Document Inventory
```
navig cabinet list                    # every stored document
navig cabinet expiring --within 180   # IDs and policies due soon (6-month travel buffer)
```
Lists all stored documents, their categories and expiry dates.

## Alert Configuration

Default alert window: **30 days** before due date.

Configured in `config.yaml`:
```yaml
bureau:
  renewal_alert_days: 30
```

Items marked `auto_renew: yes` are flagged differently (informational, not urgent).

## Common Runbooks

- **RB-009**: Monthly bureau check
- **RB-010**: Quarterly life review (includes bureau status)

## Tips

1. **Enter renewals when you get them.** Don't wait — add to CSV immediately.
2. **Check monthly.** The bureau-ops formation runs on the 1st, but spot-check anytime.
3. **Review subscriptions quarterly.** Cancel what you don't use.
4. **Keep 6-month buffer on IDs.** Many countries require 6+ months validity for travel —
   give every ID an `--expires` date in the cabinet and `navig cabinet expiring` does the rest.
5. **Digital receipts > paper.** Scan, then `navig cabinet add` — searchable by the words
   inside, impossible to lose with a backup.

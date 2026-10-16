# Bureau Subspace

Administrative life — documents, subscriptions, appointments, renewals.

## Structure

```
bureau/
  subscriptions/    ← active subscriptions and their renewal dates
  appointments/     ← upcoming appointments
  insurance/        ← claims in progress (the policy documents go in `navig cabinet`)
  banking/          ← banking references (account info — no credentials!)
  housing/          ← lease, utilities, housing documents
  renewals.csv      ← master renewal tracker
```

## Renewals CSV Format

```csv
item,category,expires,renewed,alert_days,notes
Passport,identity_documents,2028-06-15,,30,
Netflix,subscriptions,2025-02-01,auto,7,Monthly auto-renew
Car insurance,insurance,2025-12-01,,60,Annual renewal
```

## Owner

`bureau-manager` agent via `bureau-ops` formation.

## Rules

- **Scans live in the encrypted cabinet, not here** — `navig cabinet add <file> --category identity|insurance|vehicle --expires <date>`
- **Never store credentials** — no passwords, PINs, or access codes in this directory (`navig vault`)
- Store only references, dates, and document metadata
- Sensitive files: use `.private.md` extension (excluded by `.gitignore`)

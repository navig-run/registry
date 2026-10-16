# Social Circle — Inbox Docs

Drop files here to import contacts or log interactions.

## Supported file types

| File | Processed as |
|------|-------------|
| `*.csv` | Generic contact import — agent maps columns |
| `Connections.csv` | LinkedIn export — auto-detected |
| `*.vcf` / `*.vcard` | vCard contacts |
| `handles.txt` | Twitter/X handles (one per line) |
| `*.md` / `*.txt` | Meeting notes — agent extracts names + interactions |

## How to process

```bash
# Preview an address-book import (nothing is written)
navig contacts import .navig/inbox/contacts.vcf --space social-circle-space --dry-run

# Import it, merging duplicates into one contact per person
navig contacts import .navig/inbox/contacts.vcf --space social-circle-space

# See every merge the import applied (each one can be undone)
navig contacts merges
```

## Field mapping for CSV

If your CSV has non-standard column names, the agent will prompt you to map them.  
You can also create a `field-map.yaml` in this folder to save a mapping for reuse:

```yaml
# field-map.yaml
mappings:
  "Full Name": name
  "Email Address": email
  "Connected On": first_contact_date
  "Company": tags
```

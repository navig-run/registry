# Residence Space

> Your home, systematically managed. Room-by-room inventory, medication tracking, and maintenance scheduling so nothing is lost, expired, or overdue.

## What This Space Does

| Domain | What it tracks |
|--------|---------------|
| **Inventory** | Every item in every room — category, condition, quantity, storage location |
| **Pharmacy** | All household medications — person, dosage, expiry, stock level |
| **Maintenance** | All maintenance tasks — scheduled, in-progress, completed, recurring |

## Agents

| Agent | Role |
|-------|------|
| `housekeeper` | Household inventory manager |
| `medic` | Medication tracker and expiry monitor |
| `steward` | Maintenance scheduler and history keeper |
| `organizer` | Declutter analysis and categorization |

## Quick Start

```bash
# Register your first room
navig skill run log-item --room kitchen --name "Coffee maker" --category appliance --qty 1 --condition good

# Activate the default household formation
navig formation run household-ops

# Check medication expiry
navig skill run check-expiry --days 90

# Run the weekly review
@housekeeper run weekly-home-review   # steps: .navig/store/workflows/weekly-home-review.yaml
```

## Formations

| Formation | Purpose | Default? |
|-----------|---------|---------|
| `household-ops` | General home management | ✅ Yes |
| `medical-watch` | Medication monitoring | No |
| `maintenance-crew` | Maintenance scheduling | No |

## Skills

| Skill | Usage |
|-------|-------|
| `log-item` | Add inventory item |
| `track-medication` | Add/update medication record |
| `check-expiry` | Scan medications for expiry |
| `inventory-export` | Export room or full inventory to Markdown/CSV/JSON |

## Workflows

| Workflow | Schedule | Purpose |
|----------|---------|---------|
| `weekly-home-review` | Mon 09:00 | Overview of maintenance, medications, gaps |
| `medication-expiry-check` | Daily 08:00 | Alert on expiring items |
| `monthly-inventory-audit` | 1st of month | Full home audit + export |

---

_Part of the NAVIG Registry spaces library — `navig-space-2` runtime._

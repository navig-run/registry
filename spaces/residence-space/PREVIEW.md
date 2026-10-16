# Residence Space — Preview

**Runtime:** navig-space-2  
**Default formation:** household-ops  
**Accent:** #D4A76A (warm amber)  
**Tone:** Calm housekeeper — domestic, systematic, reliable

---

## What's in the box

**4 agents** · **3 formations** · **4 skills** · **3 workflows** · **4 prompts**

### Agents
- `housekeeper` — room-based inventory management
- `medic` — medication tracking and expiry monitoring  
- `steward` — maintenance scheduling and service records
- `organizer` — declutter analysis and categorization

### Formations
- `household-ops` (default) — housekeeper + organizer
- `medical-watch` — medic-led, medication-specific operations
- `maintenance-crew` — steward-led, maintenance scheduling

### Skills
- `log-item` — add household item (room, category, condition, qty, location)
- `track-medication` — add/update medication (person, dosage, expiry, stock)
- `check-expiry` — scan medication log, alert on expiry within N days
- `inventory-export` — export full or filtered inventory to Markdown/CSV/JSON

### Workflows
- `weekly-home-review` — Mon 09:00: maintenance due + medication expiry + gaps
- `medication-expiry-check` — Daily 08:00: expiry scan with critical/warning alerts
- `monthly-inventory-audit` — 1st of month: full export + declutter analysis + cost summary

---

## Demo

```bash
# Log an item
navig skill run log-item --room bathroom --name "Towels (x4)" --category other --qty 4 --condition good

# Add a medication
navig skill run track-medication --name "Ibuprofen 400mg" --person self --expiry 2027-06 --room bathroom --qty 24

# Check what expires in 30 days
navig skill run check-expiry --days 30

# Run the weekly review
@housekeeper run weekly-home-review   # steps: .navig/store/workflows/weekly-home-review.yaml
```

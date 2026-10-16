# Room Inventory

## Purpose
Produce a complete, formatted inventory of a specific room. Used for insurance
documentation, move planning, or post-audit organization.

## Variables
- `{{ROOM}}` — Room name
- `{{INVENTORY}}` — Inventory items for this room (JSON array)
- `{{FORMAT}}` — Output: `table | list | insurance | moving`

## Prompt

You are NAVIG Housekeeper. Generate a {{FORMAT}} inventory report for: **{{ROOM}}**

**Room Items:**
```json
{{INVENTORY}}
```

Produce the inventory report in the requested format:

### Table Format
Markdown table with columns: Item | Category | Quantity | Condition | Location | Notes

### List Format
Grouped by category. Each item: name, quantity, condition, location note.

### Insurance Format
Structured list suitable for an insurance inventory claim:
- Item description (brand, model if known)
- Estimated replacement value (if known, otherwise note "value unknown")
- Condition
- Quantity

### Moving Format
Pre-move checklist: all items to pack, organized by category.
Flag: fragile / oversized / requires special packing.

---
For each item with `condition: unknown`, add a note: **[NEEDS VERIFICATION]**
For each item with `condition: poor` or `condition: broken`, add: **[ACTION REQUIRED]**

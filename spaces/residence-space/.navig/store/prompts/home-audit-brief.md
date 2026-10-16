# Home Audit Brief

## Purpose
Generate a structured audit of a room or the entire home. Surfaces item counts,
condition distribution, unknown items, maintenance issues, and declutter opportunities.

## Variables
- `{{ROOM}}` — Room to audit, or `all` for the whole home
- `{{INVENTORY}}` — Inventory JSON for the room (paste or reference)
- `{{MAINTENANCE}}` — Open maintenance tasks for this room
- `{{FOCUS}}` — Audit focus: `condition | declutter | maintenance | full`

## Prompt

You are NAVIG Housekeeper. Run a structured home audit for: **{{ROOM}}**

Focus: **{{FOCUS}}**

**Inventory Data:**
```json
{{INVENTORY}}
```

**Open Maintenance Tasks:**
```
{{MAINTENANCE}}
```

Produce a structured audit report:

### 1. Inventory Summary
- Total items, active vs removed
- Category breakdown (top 5 categories by count)
- Condition distribution: new / good / fair / poor / broken / unknown

### 2. Items Needing Attention
List any items with:
- `condition: poor` or `condition: broken`
- `condition: unknown` (needs verification)
- Quantity = 0 or missing

### 3. Maintenance Review
Summarize open tasks by priority: high / medium / low / overdue

### 4. Declutter Recommendations
Identify candidates for: **donate | store | discard | relocate**
Provide specific rationale for each recommendation.

### 5. Actions Required
List 3–5 specific, actionable next steps for the operator. Be direct.

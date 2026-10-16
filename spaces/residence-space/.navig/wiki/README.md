# Residence Space Wiki

Knowledge base for residence-space.

## Contents

- [Agent Guide](agent-guide.md)
- [Runbooks](runbooks.md)

## Room Registry

Rooms are tracked in `memory/room-registry.json` with:
- Room name and type
- Inventory items (linked to household inventory)
- Maintenance history
- Special notes

## Maintenance Priority Levels

| Level | Meaning | Response |
|-------|---------|---------|
| `urgent` | Safety risk or active damage | Fix within 24h |
| `high` | Significant inconvenience | Fix within 1 week |
| `medium` | Normal maintenance | Fix within 1 month |
| `low` | Cosmetic or optional | Schedule when convenient |

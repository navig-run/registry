# Travel Space

Turn any trip idea into a well-planned, well-documented adventure.
Handles everything from rough estimate to debrief.

## Quick Start

```bash
# Create a new trip
@trip-planner new   # follows .navig/store/workflows/new-trip.yaml

# Check pre-departure checklist
@document-keeper run pre-departure --trip tokyo-2026

# Debrief after returning
@trip-planner run trip-debrief --trip tokyo-2026
```

## Structure

```
trips/
  {slug}/
    trip.json        Trip metadata: dates, destination, budget, status
    itinerary.md     Day-by-day plan
    budget.json      Estimated vs actual costs
    bookings/        Flight, hotel, activity confirmations
    documents/       Visa, insurance, tickets (local copies)
    notes/           Research, recommendations, on-trip notes
    debrief.md       Post-trip retrospective
```

## Agents

| Agent | What It Does |
|-------|-------------|
| trip-planner | Creates and manages trip structure, cost estimates |
| itinerary-builder | Builds day-by-day schedule, suggests activities |
| budget-watcher | Tracks bookings vs budget, flags overruns |
| document-keeper | Manages trip documents, pre-departure checklist |

## Workflows

| Workflow | When |
|----------|------|
| new-trip | When you decide on a destination |
| pre-departure | 1–7 days before travel |
| trip-debrief | Within 48 hours of returning |

## Inbox Routes

- `#trip-ideas` — rough idea, not yet committed
- `#active-trip` — current or upcoming confirmed trip
- `#bookings` — confirmation numbers, itinerary PDFs

## Status

**Planned.** The agents, formations and workflows ship and can be used today. The packaged
skills the workflows were designed around (trip cost estimate, day plan, flight check,
packing list) are not shipped yet — those steps are done by the agents directly.

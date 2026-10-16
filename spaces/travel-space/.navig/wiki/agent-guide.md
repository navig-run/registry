# Agent Guide — Travel Space

## trip-planner

Creates and manages trip structure. The first agent to talk to for any new trip.

```
@trip-planner new --destination tokyo --dates 2026-11-01/14 --budget 4000
@trip-planner status --trip tokyo-2026
@trip-planner estimate --destination lisbon --duration 10 --style mid-range
```

## itinerary-builder

Builds day-by-day plans. Add activities and let it organize them.

```
@itinerary-builder plan --trip tokyo-2026 --style culture-food
@itinerary-builder add --trip tokyo-2026 --day 3 --activity "teamLab Planets"
@itinerary-builder export --trip tokyo-2026
```

## budget-watcher

Tracks every booking commitment against the budget.

```
@budget-watcher add --trip tokyo-2026 --item flight-rt --cost 890 --confirmed
@budget-watcher summary --trip tokyo-2026
@budget-watcher reconcile --trip tokyo-2026
```

## document-keeper

All documents, all checklists. Run before every departure.

```
@document-keeper checklist --trip tokyo-2026
@document-keeper confirm --trip tokyo-2026 --doc travel-insurance
@document-keeper status --trip tokyo-2026
```

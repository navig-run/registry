# Runbooks — Travel Space

## New Trip

1. Decide on destination and rough dates
2. Ask `@trip-planner new` — it follows `.navig/store/workflows/new-trip.yaml`
3. Answer: destination / dates / budget target / trip type
4. Start researching and booking

## Add a Booking

1. Get confirmation from vendor
2. Save confirmation PDF to `trips/{slug}/bookings/`
3. Log cost: `@budget-watcher add --trip {slug} --item flights --cost 890 --confirmed`

## Before You Leave

Run 24–48 hours before departure:
```
@document-keeper run pre-departure --trip {slug}   # steps: .navig/store/workflows/pre-departure.yaml
```
Resolve any ❌ items before leaving.

## When You Return

Within 48 hours:
```
@trip-planner run trip-debrief --trip {slug}   # steps: .navig/store/workflows/trip-debrief.yaml
```

# Travel Space — Ops

## Pre-Trip Protocol

1. Trip created with: destination, dates, estimated budget
2. Major bookings confirmed: flights, accommodation
3. Documents checked: passport validity, visa requirements
4. Pre-departure checklist run 24–48 hours before departure
5. Emergency contacts and important addresses accessible offline

## Active Trip Protocol

- All booking confirmations stored in trips/{slug}/bookings/
- Document copies in trips/{slug}/documents/ — exported from the cabinet for the trip
  (`navig cabinet export <id> -o trips/{slug}/documents/`); the originals stay encrypted in
  `navig cabinet`, and the export folder is gitignored. Delete the copies after the trip.
- Debrief scheduled immediately upon return booking

## Post-Trip Protocol

1. Debrief written within 48 hours of return
2. Actual vs estimated budget reconciled
3. Receipts/confirmations archived
4. Photos indexed in notes if applicable
5. Trip moved to completed/ within one week

## Document Expiry Monitoring

Check annually — `navig cabinet expiring --within 365` lists every dated document:
- Passport valid for 6+ months beyond planned travel dates
- Visa requirements for upcoming destinations
- Travel insurance active for all bookings

## Budget Alert Levels

- 80%: Yellow — review remaining discretionary budget
- 90%: Orange — notify budget-watcher
- 100%: Red — trip has exceeded budget, log reason

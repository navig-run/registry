# Deploy Space — Ops

## Log a Deploy
1. Post deploy event to `#deploys` inbox
2. Include: version, service, author, timestamp, status
3. Attach diff summary if available

## Investigate a Rollback
1. Check `#rollbacks` inbox for recent events
2. Query deploy log for the prior stable version
3. Compare diffs to identify breaking change

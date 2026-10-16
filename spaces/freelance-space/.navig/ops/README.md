# Freelance Space — Ops

## Ops Procedures

### New Client Onboarding
1. Create client profile in `clients/`
2. Define rate and project scope
3. Set up time tracking for project
4. Create project folder in `projects/`

### Monthly Billing Run
1. Activate `billing-cycle` formation
2. Export time logs for the month
3. Generate invoices for all billable work
4. Log sent invoices in `invoices/`
5. Flag any overdue invoices for follow-up

### Overdue Invoice Protocol
1. billing-officer flags invoice as overdue (14+ days past due — `alert_thresholds.overdue_days` in `billing-cycle`)
2. Send payment reminder to client
3. Log communication in client record
4. Escalate to `strategist` if >60 days

## Formation Quick-Start
- **Daily**: Check `#invoices` inbox for payment confirmations
- **Weekly**: `client-ops` for project status review
- **Monthly**: `billing-cycle` for full billing run

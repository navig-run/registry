# Freelance Space — Runbooks

## Monthly Billing Run

**Formation:** `billing-cycle`  
**Frequency:** 28th of each month (the `monthly-billing-run` schedule)

### Steps
1. Export time logs for the current month
2. Review for any missing time entries
3. Generate invoices for all billable work
4. Send invoices to clients
5. Update invoice status in `invoices/`
6. Flag any accounts with overdue balance

---

## New Project Intake

**Trigger:** New project agreed with client

### Steps
1. Define scope, deliverables, and timeline
2. Agree rate (hourly vs fixed vs retainer)
3. Create project record in `projects/`
4. Set up time tracking
5. Send kickoff confirmation to client

---

## Client Health Check

**Trigger:** Monthly strategy review

### Steps
1. Review each active client relationship
2. Flag any at-risk relationships
3. Review project delivery quality and client satisfaction
4. strategist assesses revenue concentration risk

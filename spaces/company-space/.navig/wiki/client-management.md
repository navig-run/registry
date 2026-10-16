# Client Management Guide

> Pipeline management, client segments, lifecycle stages, and relationship protocols.

---

## Client Lifecycle Stages

```
PROSPECT → LEAD → QUALIFIED → PROPOSAL → NEGOTIATION → CLIENT → ACTIVE → RETENTION → RE-ENGAGE
                                                          │
                                                          └─→ CHURNED (if lost)
```

### Stage Definitions

| Stage | Owner | Description | Exit Criteria |
|-------|-------|-------------|---------------|
| **Prospect** | sales | Identified but not yet contacted | First contact made |
| **Lead** | sales | Initial contact, interest expressed | Qualification complete |
| **Qualified** | sales | Scored ≥5, budget/timeline confirmed | Proposal requested or offered |
| **Proposal** | sales + controller | Proposal sent, awaiting response | Proposal accepted or rejected |
| **Negotiation** | sales + chief | Terms being discussed | Agreement reached |
| **Client** | ops-manager | Contract signed, onboarding in progress | Project kickoff complete |
| **Active** | project-lead | Active project(s) underway | All projects delivered |
| **Retention** | sales | No active project, maintaining relationship | New project or re-engagement |
| **Re-Engage** | sales | >90 days since last interaction | Contact made, moves to Lead/Qualified |
| **Churned** | sales | Client explicitly left or >12 months inactive | Re-engagement attempt quarterly |

---

## Lead Qualification Scoring

### Scoring Algorithm

```
Base Score: 5

+ Timeline Bonus:
  - "Urgent / this week"    → +2
  - "This month"            → +1.5
  - "This quarter"          → +1
  - "No rush"               → +0

+ Budget Bonus:
  - High budget             → +2
  - Medium budget           → +1
  - Low budget              → +0.5
  - Unknown                 → +0

+ Source Bonus:
  - Referral                → +1
  - Returning client        → +1
  - Portfolio/website       → +0.5
  - Cold inbound            → +0
```

### Priority Mapping

| Score | Priority | Action |
|-------|----------|--------|
| ≥ 8 | **High** | Immediate proposal, notify chief + sales, respond within 24h |
| 5 — 7 | **Medium** | Schedule intro call, follow up within 48h |
| < 5 | **Low** | Add to nurture list, monthly check-in, content marketing |

---

## Client Segments

Configure your segments in `config.yaml` under `client_segments`. Common segments include:

### Primary Segments

| Segment | Description |
|---------|-------------|
| `sme-tech` | Small/medium tech companies |
| `creative-agencies` | Design studios, marketing agencies |
| `ecommerce` | Online retail and marketplaces |
| `saas-companies` | SaaS product companies |
| `non-profits` | NGOs, associations, foundations |
| `healthcare` | Clinics, health tech, wellness |
| `education` | Schools, e-learning platforms |
| `real-estate` | Property management, agents |
| `hospitality` | Hotels, restaurants, tourism |
| `professional-services` | Law firms, consultancies, accounting |

Add industry-specific segments as needed for your market.

---

## Client Record Structure

Each client in `clients/` has a markdown file:

```markdown
# Client: [Company Name]

## Contact
- **Name**: [Contact Person]
- **Email**: [email]
- **Phone**: [phone]
- **Role**: [their role]
- **Language**: [preferred language]

## Company
- **Industry**: [segment]
- **Size**: solo / small / medium / large
- **Location**: [city, country]
- **Website**: [url]

## Relationship
- **First Contact**: YYYY-MM-DD
- **Source**: referral / portfolio / cold / event / [other]
- **Status**: prospect / lead / qualified / client / active / retention / churned
- **Score**: [qualification score]

## Projects
| Project | Status | Budget | Dates |
|---------|--------|--------|-------|
| ... | ... | ... | ... |

## Financial
- **Total Billed**: [amount]
- **Total Paid**: [amount]
- **Outstanding**: [amount]
- **Payment History**: [on-time / late / mixed]

## Notes
- [Interaction history, preferences, constraints]
```

---

## Outreach Protocols

### Outreach Types

| Type | When | Template |
|------|------|----------|
| Cold intro | New prospect identified | client-outreach prompt (cold-intro) |
| Follow-up | After initial contact, no response in 7 days | client-outreach prompt (follow-up) |
| Re-engagement | >90 days since last contact | client-outreach prompt (re-engagement) |
| Referral ask | Good relationship, project complete | client-outreach prompt (referral-ask) |
| Upsell | Active client, adjacent service opportunity | client-outreach prompt (upsell) |
| Thank you | After payment, project completion, referral | client-outreach prompt (thank-you) |

### Communication Cadence

| Client Stage | Frequency | Channel |
|--------------|-----------|---------|
| Active project | As needed (usually weekly) | Email / call |
| Retention (no project) | Monthly check-in | Email |
| Churned | Quarterly attempt | Email |
| Lead (high) | Within 24h, then every 48h | Email / call |
| Lead (medium) | Within 48h, then weekly | Email |
| Lead (low) | Monthly newsletter | Email |

---

## Contracts

### Contract Types

| Type | Use Case |
|------|----------|
| Service agreement | General service contract |
| NDA | Confidentiality |
| Freelance/subcontracting | Subcontracting |
| Retainer | Ongoing monthly services |
| Project-based | One-off project |

### Contract Essentials
- **Governing law**: Per {{JURISDICTION}}
- **IP transfer**: On final delivery AND full payment
- **Signature**: Acceptance + date, name, signature

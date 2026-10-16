# Proposal Brief Prompt

## Purpose
Create a polished service proposal for prospective or existing clients.
Aligned with configured service lines and positioning.

## Variables
- `{{PROPOSAL_TITLE}}` — Title of the proposal
- `{{CLIENT_NAME}}` — Client name
- `{{CLIENT_COMPANY}}` — Client company name
- `{{CLIENT_SEGMENT}}` — Industry segment
- `{{PROJECT_SUMMARY}}` — 2-3 sentence overview of what the client needs
- `{{SERVICE_LINES}}` — Which services apply (comma-separated)
- `{{TIMELINE}}` — Proposed timeline (weeks/months)
- `{{BUDGET_RANGE}}` — Estimated budget range
- `{{COMPETITIVE_EDGE}}` — What makes {{COMPANY_NAME}} the right choice
- `{{LANGUAGE}}` — Output language (default: en)

## Prompt

You are the sales agent at {{COMPANY_NAME}} preparing a client proposal.

**Proposal**: {{PROPOSAL_TITLE}}
**Client**: {{CLIENT_NAME}} ({{CLIENT_COMPANY}})
**Segment**: {{CLIENT_SEGMENT}}
**Need**: {{PROJECT_SUMMARY}}
**Services**: {{SERVICE_LINES}}
**Timeline**: {{TIMELINE}}
**Budget Range**: {{BUDGET_RANGE}} {{CURRENCY}}
**Language**: {{LANGUAGE}}

Generate a structured proposal:

1. **Cover** — Proposal title, date, prepared for [client], prepared by {{COMPANY_NAME}}
2. **Executive Summary** — 3-4 sentences: their need, our solution, expected outcome
3. **About {{COMPANY_NAME}}** — 1 paragraph: experience, approach, capabilities
4. **Understanding Your Needs** — Reflect back what they need (shows we listened)
5. **Proposed Solution** — Break down by service line:
   - What we'll deliver
   - Approach / methodology
   - Tools & technologies (where relevant)
6. **Timeline & Milestones** — Phase breakdown with deliverables per phase
7. **Investment** — Budget breakdown by phase. Note tax compliance for {{JURISDICTION}}
8. **Why {{COMPANY_NAME}}** — {{COMPETITIVE_EDGE}} + 2-3 differentiators
9. **Team** — Who will work on this (agents/roles)
10. **Next Steps** — Clear path forward:
    - Review and feedback
    - Formal quote upon agreement
    - Contract signing
    - Kickoff date
11. **Contact** —
    {{OWNER_NAME}}
    {{COMPANY_NAME}}
    {{COMPANY_EMAIL}} | {{COMPANY_PHONE}}
    {{COMPANY_WEBSITE}}

**Style**: Professional but human. No jargon. Focus on outcomes over features.
Keep it under 2 pages equivalent in markdown.

Format as markdown, save-ready for `leads/{{CLIENT_COMPANY}}/proposal-{{DATE}}.md`.

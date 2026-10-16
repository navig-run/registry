---
name: business-plan
description: >
  Scans the current project — code, docs, manifests, git history, assets — and produces a
  professional, investor-grade business plan grounded in what the project actually is, never
  invented. Use when the user says "build a business plan", "make/find a business plan", "scan my
  project for a business plan", "what's the business case", "what's this worth", or wants a strategic
  plan derived from a codebase. Writes `BUSINESS-PLAN.md` (mutating — one file). Runs FIRST in the
  pair; hand off to the `monetization` skill afterward for the revenue/pricing half. Has four modes —
  Investigate, Adapt, Evolve, Upgrade.
category: business
tags: [business-plan, strategy, product, market, fundraising]
safety: safe
---

# business-plan — evidence-grounded plan generator

Turn a real project into a credible, decision-ready business plan. You **investigate** the actual
artifacts (never invent the product), **adapt** the plan to the project's type and stage, **evolve**
it across iterations, and **upgrade** it with external research. This is **part 1 of 2** — run
`monetization` afterward for the revenue/pricing half.

The Operator standard applies: reliability over cleverness. A plan that overstates traction is worse
than no plan. Cite everything; label every guess.

## Prime directive — evidence over imagination

Your knowledge of *this specific project* comes only from its files. **Every factual claim about the
product, stack, audience, or traction must trace to a scanned artifact** (`claim → file:line`).

- ✅ "Targets operators of live infrastructure — README markets an 'agent that runs your servers' and
  ships SSH/DB/deploy verbs (`core/navig/commands/host.py`)."
- ❌ "Targets enterprise IT departments." (no evidence in the repo)
- **Label every assumption `[ASSUMPTION]`** and list it in the Assumptions Ledger. No silent
  invention. Market/industry numbers come from retrieval (Upgrade), never memory.
- Separate *what exists* (code/docs present) from *what is planned* (TODOs, roadmap, empty dirs).

## The four modes

| Mode | Trigger | What it does |
|------|---------|--------------|
| **Investigate** | default / "scan" | Read the project end-to-end; build an evidence ledger of facts. |
| **Adapt** | always, after Investigate | Classify **type** + **stage** + **market**, then reshape the template to fit. |
| **Evolve** | "update/refine/v2 the plan"; plan already exists | Re-scan deltas (git log, new files), bump version, refine weak sections, re-validate assumptions. |
| **Upgrade** | "research/benchmark/validate", or low-confidence sections | Pull external market data (TAM, competitors, trends) via WebSearch/WebFetch or the `deep-research` skill; replace `[ASSUMPTION]`s with cited facts. |

Default flow: **Investigate → Adapt → draft → (offer) Upgrade → write file.** Re-runs enter **Evolve**.

## Phase 1 — INVESTIGATE (scan, cheap → deep)

Work this checklist; capture each hit as a `claim → file:line` pair.

```
Investigate:
- [ ] Identity & pitch    (README, docs landing, package.json/pyproject description, .navig/plans/VISION.md)
- [ ] What it does         (entry points, CLI verbs, routes, features, screenshots/)
- [ ] Tech & assets        (manifests, infra, deps, integrations, services/)
- [ ] Audience signals     (docs tone, terminology, install steps, target platform)
- [ ] Stage & traction     (git log age/cadence, CHANGELOG, versions, tests, TODOs)
- [ ] Existing $ signals    (Stripe/payments, pricing pages, licence, "pro"/tier code) → note for monetization
- [ ] Competitor clues      (comparisons in docs, named alternatives, category words)
- [ ] Gaps                 (what's missing / empty / stubbed)
```

1. **Docs first** — `README*`, `docs/`, `CHANGELOG*`, `.navig/plans/*`, `LICENSE`. These carry intent.
2. **Manifests** — `package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`, extension manifests. Name, scripts, deps, description.
3. **Surface area** — entry points, command/route definitions, `skills/`, feature folders. What can it *do*?
4. **History** — `git log --stat -n 40`, tags, `CHANGELOG`. Age + cadence = stage signal.
5. **Visuals** — `screenshots/`, `assets/`, demo links. Polish = stage signal.
6. For large repos, dispatch the **Explore** agent in parallel to map subsystems; you keep the conclusions.

Output of this phase = the **Evidence Ledger** you cite throughout.

## Phase 2 — ADAPT (classify, then tailor)

Pick the closest **type** and **stage**; they change which sections matter.

| Type | Plan emphasis |
|------|--------------|
| SaaS / web app | TAM/SAM/SOM, retention, CAC/LTV, GTM motion |
| CLI / dev tool / library | Adoption funnel, OSS↔commercial line, ecosystem, DX moat |
| Browser extension / userscript | Store distribution, install→active conversion, platform-policy risk |
| Marketplace / two-sided | Liquidity, take-rate, cold-start, supply vs demand |
| Infra / self-hosted / agent platform | Self-host vs managed, tiered entitlement, support revenue, community |
| Content / media | Audience growth, sponsorship/subscription, distribution |
| Agency / services | Utilisation, pipeline, productisation path |

| Stage | Evidence cue | Posture |
|-------|-------------|---------|
| Idea / pre-code | empty dirs, sparse README | Hypothesis-led; heavy `[ASSUMPTION]`; validation roadmap |
| MVP / prototype | working core, few tests, young git | Problem/solution fit; early GTM experiments |
| Launched | docs, screenshots, releases | Traction framing; growth + unit economics |
| Revenue / scaling | payments code, tiers, user data | Optimisation, expansion, defensibility |

State the chosen type/stage at the top of the plan with the evidence that justified it. (Example: a
navig-shaped repo reads as *infra / agent platform · launched*, with a Free/Plus/Max/Enterprise tier
model and a marketplace already in `services/api`.)

## Phase 3 — DRAFT

Write **`BUSINESS-PLAN.md`** in the project root (or `docs/BUSINESS-PLAN.md` if a `docs/` folder
exists). **Omit or compress sections that don't fit** rather than padding with filler.

```
# Business Plan — <Project Name>
> Version: vX.Y · Generated: <date> · Type: <…> · Stage: <…> · Confidence: <H/M/L>

1. Executive Summary   — one-pager: what, who, why now, the ask. Write LAST.
2. Problem             — the pain, who has it, current alternatives & why they fall short.
3. Solution / Product  — what it does today (cite features) vs roadmap.
4. Market              — TAM / SAM / SOM with method shown; trends. [Upgrade for real #s]
5. Customers & Personas— 1–3 personas grounded in audience signals; their jobs-to-be-done.
6. Competition         — named alternatives, table, your wedge. [Upgrade]
7. Unique Value & Moat — tech, data, network, brand, switching cost, distribution.
8. Go-To-Market        — channels, motion (PLG/sales/community), launch sequence, funnel.
9. Business Model      — value→money in one paragraph → full detail in MONETIZATION.md.
10. Operations & Tech  — stack (cite), infra, key dependencies & their risks.
11. Team & Roles       — who/what's needed; gaps (cite contributors/git if solo).
12. Roadmap            — 30/60/90 + 12-month, tied to provable checkpoints.
13. Financial Outlook  — high-level only (detailed model → MONETIZATION.md).
14. Risks & Mitigations— top 5–7, each likelihood × impact × mitigation.
15. KPIs               — the 3–5 numbers that prove this is working.
16. Assumptions Ledger — every [ASSUMPTION] + how to validate + confidence.
17. Evidence Appendix  — claim → file:line citations from Investigate.
```

Writing standards: **specific, quantified, falsifiable** ("convert 8% of installs to weekly-active in
90 days," not "grow users"); **method visible** for every number; tables over paragraphs; **honest** —
name the biggest weakness in Risks; **self-contained** — a reader who has never seen the repo
understands the business.

## Phase 4 — UPGRADE (offer, or run on request)

When sections 4/6 rest on `[ASSUMPTION]`s, or the user asks to validate/benchmark: use
**WebSearch/WebFetch** for market size, competitor set, and category trends — **cite every external
claim** (source + date). For deep validation, invoke the **`deep-research`** skill with a focused
question. Replace resolved `[ASSUMPTION]`s with cited facts; keep the rest flagged. Prefer retrieval
over memory for any market number.

## Phase 5 — EVOLVE (re-runs)

If `BUSINESS-PLAN.md` exists: read it, read `git log` since its `Generated` date and any changed
files. Bump `Version` (minor = refinement, major = pivot/stage change); keep a bottom `## Changelog`.
Re-validate the ledger — promote validated assumptions, kill disproven ones, flag stale market data.
Strengthen the weakest-confidence sections first; leave stable, well-cited sections alone.

## Quality gate (before done)

- [ ] Type + Stage stated and justified with evidence.
- [ ] Every product/traction claim cites a file (Evidence Appendix populated).
- [ ] Every market/competitor number is cited (Upgrade) or tagged `[ASSUMPTION]`.
- [ ] Risks names the real #1 threat, not a soft one.
- [ ] KPIs are 3–5, specific, measurable.
- [ ] Executive Summary written last and stands alone.
- [ ] File written; user told the path + offered the `monetization` handoff.

## Handoff

> "Business plan written to `<path>`. Run `monetization` next to turn this into a pricing & revenue
> model — it reads this plan as its input."

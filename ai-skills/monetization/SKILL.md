---
name: monetization
description: >
  Turns a project plus its business plan into a professional, data-grounded monetization & pricing
  strategy — revenue-model selection, pricing tiers, unit economics (CAC/LTV/margin/payback), revenue
  projections, billing infrastructure, and a pricing-experiment roadmap. Runs SECOND: reads
  `BUSINESS-PLAN.md` first and aligns to it — run the `business-plan` skill before this. Use when the
  user says "how do I monetize/price this", "build a monetization/pricing plan", "revenue model for my
  project", "what should I charge", or "make money from this". Writes `MONETIZATION.md` (mutating —
  one file). Has four modes — Investigate, Adapt, Evolve, Upgrade.
category: business
tags: [monetization, pricing, revenue, unit-economics, billing]
safety: safe
---

# monetization — pricing & revenue strategy generator

Produce **part 2 of 2**: how the project makes money. This skill **reads the business plan first**
(sequence matters), **investigates** real cost/payment signals, **adapts** the revenue model to the
project type, **evolves** pricing as data arrives, and **upgrades** with competitor-pricing research.
Same evidence discipline as `business-plan`: model choices justified by facts, every number's method
shown. Commit to numbers — a pricing plan that only gives ranges hasn't decided anything.

## Precondition — read the plan (the sequence)

1. Look for **`BUSINESS-PLAN.md`** (root) or **`docs/BUSINESS-PLAN.md`**. Read it fully — it defines
   product, type, stage, personas, market, and KPIs this strategy must align to.
2. **If it's missing:** tell the user "Run `business-plan` first — monetization builds on it," and
   offer a fast Investigate pass to draft both. Do not invent the business context.

## Prime directive — pricing must be grounded

- **Model choice traces to project reality** — audience, cost structure, what alternatives charge.
- **Every financial figure shows its method** (assumptions → arithmetic → result). No magic numbers.
- **Competitor/market pricing comes from retrieval** (Upgrade), never memory — pricing dates fast.
- Unproven inputs are tagged `[ASSUMPTION]` and carried into the Assumptions Ledger with a test.

## The four modes

| Mode | Trigger | What it does |
|------|---------|--------------|
| **Investigate** | default | Scan for monetization signals: payment code, tiers, cost drivers, willingness-to-pay. |
| **Adapt** | always | Match revenue model(s) to the **type/stage** from the plan; reject ill-fitting ones with reasons. |
| **Evolve** | "update pricing"; file exists; new data | Fold in real metrics, bump version, retune tiers, log the experiment outcome. |
| **Upgrade** | "benchmark/research pricing" | Pull competitor price points & packaging via WebSearch/WebFetch or `deep-research`; replace `[ASSUMPTION]`s. |

## Phase 1 — INVESTIGATE (monetization signals)

```
Investigate:
- [ ] Existing $ infra      (Stripe/Paddle/LemonSqueezy/PayPal SDKs, webhooks, checkout, licence keys)
- [ ] Tiering signals       ("pro"/"premium"/feature flags, paywalls, quota/limit code, entitlements)
- [ ] Cost drivers          (compute/API/LLM calls, storage, bandwidth, per-seat infra → marginal cost)
- [ ] Distribution channel  (store/web/CLI/extension → which billing rails & fees apply)
- [ ] Audience WTP           (prosumer vs hobbyist vs enterprise tone; B2B vs B2C from the plan)
- [ ] Free/OSS boundary      (licence; give-away vs paid — the open-core line)
- [ ] Current revenue        (if any) and what is already charged
```

Pull product, personas, market, stage, and KPIs from the business plan rather than re-deriving them.
(Example: a navig-shaped repo already encodes a **Free / Plus / Max / Enterprise** tier ladder and a
marketplace with a take-rate in `services/api` — read the existing model before proposing a new one.)

## Phase 2 — ADAPT (select the revenue model)

Score candidates against the project; pick 1 primary (+ optional secondary), and **say why the
rejected ones don't fit.**

| Model | Fits when | Watch out for |
|-------|-----------|---------------|
| Subscription (SaaS) | recurring value, ongoing cost to serve | churn; must show continuous value |
| Usage / metered | cost scales with use (API/LLM/compute) | bill shock; needs caps/alerts |
| Freemium / open-core | low marginal cost, viral/PLG, big top-funnel | free-rider cost; conversion is everything; where's the paid line |
| One-time / perpetual licence | desktop/CLI/tool, low ongoing cost | no recurring revenue; needs v2 upgrades |
| Tiered entitlement | one credential unlocks graded capability | tier design; upgrade friction |
| Marketplace take-rate | two-sided, you broker transactions | liquidity first; take-rate sensitivity |
| Maintenance / support contract | self-hosted, infra, B2B reliance | sales-led; scoping; founder time |
| Services / done-for-you | early, custom, high-touch | doesn't scale; bridge to product |
| Ads / sponsorship | large audience, content/media | needs scale; UX tradeoff |
| Store IAP | extension/mobile/store-distributed | 15–30% platform fee & policy risk |

Decision output: **chosen model + one-paragraph rationale grounded in Investigate + plan facts.**

## Phase 3 — DRAFT

Write **`MONETIZATION.md`** (root, or `docs/` if it exists):

```
# Monetization Plan — <Project Name>
> Version: vX.Y · Generated: <date> · Reads: BUSINESS-PLAN.md vX.Y · Confidence: <H/M/L>

1. Revenue Model        — chosen model(s) + rationale; rejected models w/ reasons.
2. Packaging & Tiers    — tier table: name · who it's for · key features/limits · price.
                          Anchor 3 tiers (good/better/best) unless the type says otherwise.
3. Price Points         — specific numbers + WHY (value metric, anchoring, $9/$19/$49 logic,
                          annual discount, regional pricing). Name the value metric you bill on.
4. Unit Economics       — per customer: price, gross margin, CAC, LTV, LTV:CAC, payback months.
                          SHOW THE MATH. Mark each input cited / [ASSUMPTION].
5. Revenue Projections  — Conservative / Base / Aggressive over 12mo (36mo if scaling).
                          State the funnel behind each (traffic→signup→paid→churn).
6. Billing & Payments   — provider, one-time vs recurring, trials, dunning, taxes, refunds,
                          build vs buy. Reuse any $ infra found in Investigate.
7. Conversion Levers    — activation, free→paid triggers, paywall placement, time-to-value.
8. Expansion Revenue    — upsell / cross-sell / seat & usage expansion / add-ons. (NRR target.)
9. Retention & Churn    — why people leave, save flows, annual incentives, churn target.
10. Pricing Experiments — backlog of A/B tests: hypothesis · metric · expected lift, ranked.
11. KPIs Dashboard      — MRR/ARR, ARPU, conversion %, churn %, LTV:CAC, payback, NRR + targets.
12. 30/60/90 + 12-Month — instrument → price → launch → optimise.
13. Risks & Mitigations — pricing / billing / platform-fee / concentration risks + mitigations.
14. Assumptions Ledger  — every [ASSUMPTION] + how to validate + confidence.
```

Standards: **concrete prices**, not ranges only; **bill on a value metric** that grows with customer
value (seats, usage, projects) — name it; show **sensitivity** (how revenue moves if conversion or
churn shifts ±2pp); respect **platform fees** in margin math (Stripe ~2.9%+30¢; app/extension stores
15–30%); **align to the plan** — pricing serves the personas, stage, and KPIs in `BUSINESS-PLAN.md`.

## Phase 4 — UPGRADE (benchmark real prices)

Use **WebSearch/WebFetch** for **current** competitor price points, tier structures, and packaging —
**cite source + date** (never quote pricing from memory). For a thorough sweep, invoke
**`deep-research`**. Replace `[ASSUMPTION]` price inputs with benchmarked figures; raise confidence;
note what's still unverified.

## Phase 5 — EVOLVE (re-runs)

If `MONETIZATION.md` exists: read it and the latest `BUSINESS-PLAN.md` (stay in sync — note if the
plan moved ahead). Fold in any **real metrics** the user provides (actual conversion, churn, ARPU) —
they outrank assumptions. Retune tiers/prices; record the change and its trigger in a bottom
`## Changelog` and the Experiments log (hypothesis → result → decision). Bump Version; re-flag stale
competitor pricing for re-Upgrade.

## Quality gate (before done)

- [ ] Business plan was read (or its absence handled) and this plan aligns to it.
- [ ] Primary revenue model chosen WITH rationale; alternatives rejected with reasons.
- [ ] Tier table has concrete prices and a named value metric.
- [ ] Unit economics show the math; LTV:CAC and payback computed; inputs cited or flagged.
- [ ] Projections list their funnel assumptions and a ±sensitivity.
- [ ] Platform/payment fees reflected in margins.
- [ ] KPIs have targets; experiments backlog is ranked.
- [ ] File written; user told the path.

## Handoff

> "Monetization plan written to `<path>`, aligned to `BUSINESS-PLAN.md`. Re-run in Evolve mode once
> you have real conversion/churn numbers, or in Upgrade mode to benchmark live competitor pricing."

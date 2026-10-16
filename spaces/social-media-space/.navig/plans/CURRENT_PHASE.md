# Current Phase: Brand Setup & Pipeline Activation

**Phase**: 1 — Foundation: Brand Onboarding & First Content Pipeline
**Started**: 2026-03-18
**Status**: active

## Objectives

- [ ] Onboard at least one brand: copy `brands/_template/`, fill voice.json + accounts.json + guidelines.md
- [ ] Update `active_brands` in `.navig/memory/space-context.json`
- [ ] Create first 5 post drafts using `@post-writer draft`
- [ ] Complete first brand-guardian voice review
- [ ] Populate first week's scheduling queue
- [ ] Run first analytics baseline (even if empty — sets the baseline)

## Definition of Success for Phase 1

✅ At least 1 brand fully configured (voice.json, accounts.json, guidelines.md complete)
✅ 5 approved drafts in `content/scheduled/`
✅ Weekly content rhythm running (Monday analytics → Wednesday drafts → Friday scheduling)
✅ No draft shipped with voice score < 7

## Next Actions

1. `cp -r brands/_template brands/{your-brand}` — onboard your first brand
2. `@content-strategist brief --brand {your-brand} --kickoff` — generate first content brief
3. `@post-writer draft --brand {your-brand} --platform linkedin --topic "Introduction"` — first post

## Risks

- **Brand voice too vague** — if voice.json has insufficient detail, brand-guardian scores will be unreliable; invest time in voice.json
- **Over-scheduling before finding rhythm** — start with 3 posts/week/platform; scale after 4 weeks of data

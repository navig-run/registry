# Empire Space — Runbooks

## Monthly Empire Review

**Formation:** `portfolio-ops` + `venture-review`  
**Duration:** 2-3 hours  
**Frequency:** First week of month

### Steps
1. Pull revenue summary for previous month
2. Review each venture status (update stage if changed)
3. Log any strategic decisions made
4. Rate and archive accumulated market signals
5. Set priorities for the coming month

---

## New Venture Intake

**Trigger:** New venture opportunity identified

### Steps
1. Create venture profile in `ventures/`
2. Add it to `.navig/memory/ventures.json` (`id`, `name`, initial stage `idea`) — the
   `advance-stage` skill moves it along the pipeline from there
3. Brief venture-scout with opportunity context
4. Log initial decision to proceed with exploration

---

## Market Signal Assessment

**Trigger:** Significant market event or competitive move

### Steps
1. Log signal with date, source, and description
2. market-analyst rates: significance (1-10), urgency (1-10)
3. portfolio-commander reviews and decides: monitor / respond / act
4. Log decision with context

---
id: weekly-review
name: Weekly Review
description: Structured end-of-week review — wins, blockers, key decisions, and next-week priorities
category: productivity
version: 1.0.0
license: MIT
---

# Weekly Review

Run every Friday (or end of your sprint cycle) to close the week cleanly and set up
the next one. Works best when combined with `navig skill run git-ops summary` to
pull in actual commit data automatically.

---

## Prompt

```
You are a ruthlessly effective executive coach. Guide the operator through a 30-minute
structured weekly review.

--- Context ---
Week ending: {{week_ending_date}}
Focus areas this week: {{focus_areas}}    # comma-separated, e.g. "API v2, hiring, docs"
Git summary (optional): {{git_summary}}   # output of `navig skill run git-ops summary`
Notable events (optional): {{events}}     # anything significant not in git

--- Review Protocol ---

### 1. Energy Check (1 min)
Rate your energy this week 1–10 and state the single biggest drain and the single biggest
energiser. Do not over-explain — one sentence each.

### 2. Wins (5 min)
List three things that moved forward this week. For each:
- What shipped / was completed
- Why it matters
- Who/what enabled it (to reinforce the pattern)

### 3. Blockers & Carry-Overs (5 min)
List items that didn't complete. For each:
- Item
- Root cause of blockage (honest assessment)
- Decision: Drop / Defer / Escalate / Decompose

### 4. Key Decisions Made (3 min)
List up to three significant decisions made this week and the reasoning behind them.
Record these — future-you will thank present-you.

### 5. Learnings (3 min)
One technical insight and one process/people insight from this week.

### 6. Next Week Priorities (10 min)
Top 3 outcomes for next week — not tasks, outcomes. For each:
- Outcome (what done looks like)
- First action (the single next physical step)
- Blocking dependencies to resolve first

### 7. System Maintenance (3 min)
- Inbox zero? If not: triage now
- Any docs or plans that need updating?
- Calendar / schedule conflicts to address?

Close with one sentence: "Next week is a win if _______________."
```

---

## Usage

Import the library once (from a clone of this repository), then fill and copy a prompt with `navig prompts use`:

```bash
navig prompts import library/prompts   # once

# Auto-populate git summary
GIT_SUMMARY=$(navig skill run git-ops summary --json)

navig prompts use weekly-review \
  --var week_ending_date="$(Get-Date -Format 'yyyy-MM-dd')" \
  --var focus_areas="API v2, onboarding docs" \
  --var git_summary="$GIT_SUMMARY"
```

Or run it in NAVIG chat on Friday afternoon with context attached.

---

## Tips

- Schedule a recurring 30-min block: `navig cron add weekly-review "0 16 * * 5" "navig prompts use weekly-review --no-copy"`
- Save each review to `.navig/plans/reviews/YYYY-WXX.md` for quarterly trend analysis
- Pair with `morning-briefing` on Mondays to close the loop: last week's next-week priorities become this week's focus areas

# Social Media Space — Ops

## Weekly Content Ops Rhythm

### Monday — Analytics Review
```
[ ] @analytics-watcher report --period last-7-days (all active brands)
[ ] Identify top-performing posts from last week
[ ] Note patterns: which pillars, hooks, times performed best
[ ] Feed learnings into this week's content brief
```

### Tuesday — Strategy & Planning
```
[ ] @content-strategist calendar --week current (for each brand)
[ ] Fill any gaps in the 7-day forward calendar
[ ] Greenlight or adjust ideas based on Monday analytics
[ ] Brief post-writer with this week's angles
```

### Wednesday–Friday — Production
```
[ ] @post-writer draft (per scheduled brief)
[ ] @brand-guardian review (auto-triggered on draft commit)
[ ] Approve, revise, or reject each draft
[ ] @scheduler queue (approved drafts → scheduled queue)
```

### Saturday — Queue Audit
```
[ ] Review content/scheduled/ — all slots filled for next 7 days?
[ ] Spot-check voice consistency on 3 random upcoming posts
[ ] Verify hook scores — nothing below 6 in the queue
```

---

## Brand Onboarding Protocol

```
1. cp -r brands/_template brands/{new-slug}
2. Edit brands/{new-slug}/voice.json — fill ALL fields
3. Edit brands/{new-slug}/accounts.json — add platform accounts
4. Write brands/{new-slug}/guidelines.md — content pillars, forbidden topics, target audience
5. Add {new-slug} to .navig/memory/space-context.json active_brands[]
6. @content-strategist brief --brand {new-slug} --kickoff
7. First content review: @brand-guardian audit --brand {new-slug}
```

---

## Emergency Procedures

### Take Down a Post
```
1. @scheduler dequeue --brand {slug} --post-id {id}
2. If already published: record in content/published/{brand}/{id}.json with status: "retracted"
3. Log incident in .navig/plans/
```

### Brand Voice Drift Detected
```
1. @brand-guardian audit --brand {slug} --period last-30-days
2. Review low-scoring posts: what pattern of deviation?
3. Update brands/{slug}/voice.json with clarified rules
4. Re-review last 2 weeks of drafts against updated voice
```

### Engagement Crash
```
1. @analytics-watcher anomaly --brand {slug}
2. Pull last 30 days: @analytics-watcher trends --brand {slug} --metric engagement --weeks 4
3. Check: was posting frequency maintained? Were hook scores high?
4. @content-strategist pivot-brief --brand {slug} (adjust content mix)
```

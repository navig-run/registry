# Runbooks

Standard operating procedures for common and critical scenarios.

---

## RB-001 — Onboard a New Brand

**Time:** ~15 minutes
**When:** Adding a brand to this space for the first time

**Steps:**

1. Create the brand directory:
   ```
   mkdir brands/{slug}
   ```

2. Copy the template files:
   ```
   cp brands/_template/voice.json brands/{slug}/voice.json
   cp brands/_template/accounts.json brands/{slug}/accounts.json
   cp brands/_template/guidelines.md brands/{slug}/guidelines.md
   ```

3. Fill in `voice.json` — every field matters:
   - `personality`: 3-5 adjectives (these drive post-writer behavior)
   - `tone`: `casual` / `professional` / `authoritative` / `friendly`
   - `avoid[]`: words and phrases that are off-brand
   - `must_feel[]`: emotions the reader should feel after every post
   - `min_body_chars`: minimum post body length for this brand

4. Fill in `accounts.json` — one entry per active account

5. Write `guidelines.md` — target audience, content pillars, visual style

6. Add brand slug to `active_brands` in `.navig/memory/space-context.json`

7. Create analytics directories:
   ```
   mkdir -p analytics/{slug}/{YYYY-MM}
   echo "date,platform,post_id,post_slug,impressions,likes,comments,shares,clicks,saves,reach,hook_score" > analytics/{slug}/{YYYY-MM}/engagement.csv
   echo "[]" > analytics/{slug}/hashtags.json
   ```

8. Test voice check: `@brand-guardian audit --brand {slug}`

9. Run first content brief: `@content-strategist brief --brand {slug} --topic intro`

**Done when:** First draft written, voice-checked, and approved.

---

## RB-002 — Weekly Content Production Cycle

**Time:** ~2 hours across the week
**When:** Every Monday–Friday

| Day | Action |
|-----|--------|
| Mon 8 AM | Analytics weekly report auto-runs (#analytics) |
| Mon 9 AM | Weekly content plan auto-runs (#strategy) |
| Mon–Wed | Write drafts based on briefs (#drafts) |
| Wed–Thu | Brand guardian reviews drafts (#review) |
| Thu | Approved posts scheduled for next week (#schedule) |
| Fri | Queue audit — verify 5+ posts ready per active brand |

**Manual trigger:** `navig flow run weekly-content-plan`

---

## RB-003 — Emergency Post Removal

**When:** A published or scheduled post needs to come down immediately

**Steps:**

1. If not yet published, dequeue from schedule:
   ```
   @scheduler dequeue --brand {slug} --post {post-id}
   ```

2. Move draft to archive:
   ```
   mv content/scheduled/{brand}/{file}.json content/published/{brand}/RETRACTED-{file}.json
   ```

3. If already published via platform API:
   - Delete from platform manually or via API
   - Log the incident: `echo "{timestamp},{brand},{post-slug},retracted,{reason}" >> analytics/{brand}/incidents.log`

4. Brief content-strategist on what replacement content (if any) is needed:
   ```
   @content-strategist brief --brand {slug} --topic "replacement for retracted post"
   ```

---

## RB-004 — Voice Drift Recovery

**When:** Multiple consecutive posts are scoring 5-6, brand guardian keeps rejecting

**Symptoms:** voice_score average dropping, rejections increasing, post-writer output feels generic

**Steps:**

1. Audit last 5 published posts:
   ```
   @brand-guardian audit --brand {slug} --last 5
   ```

2. Review `brands/{slug}/voice.json` — have the avoid/must_feel arrays become too restrictive or too vague?

3. Update `voice.json` with clearer examples if needed (add `example_posts` entries)

4. Brief post-writer with a specific tone recalibration note:
   ```
   @post-writer draft --brand {slug} --platform linkedin --brief "..." --note "Recalibration: focus on {must_feel[0]} more than anything else"
   ```

5. Run voice check on the recalibrated draft

6. If score ≥ 7, the new draft becomes the reference for post-writer resets

---

## RB-005 — Engagement Crash Response

**When:** Analytics shows ≥30% drop in engagement for a brand over 7 days

**Trigger:** analytics-watcher auto-escalates this to #viral as an anomaly flag

**Steps:**

1. Get detailed breakdown:
   ```
   @analytics-watcher anomalies --brand {slug} --threshold 30
   ```

2. Identify: is the drop platform-specific, pillar-specific, or universal?

3. Platform-specific drop: check if posting time or format changed recently
   - Adjust `posting_frequencies` in space-context.json if needed

4. Pillar-specific drop: rest that pillar for 2 weeks, shift to better-performing pillars

5. Universal drop: run voice audit `@brand-guardian audit --brand {slug} --last 10` — may indicate voice drift

6. Post recovery in `.navig/plans/briefs/recovery-{brand}-{week}.md` with adjusted strategy

7. Monitor closely for 2 weeks — flag if crash continues

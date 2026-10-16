# Simulation Space — Runbooks

## Weekly Simulation Review

**Formation:** `habit-sim`  
**Frequency:** Sunday

### Steps
1. Review all habit runs for the week
2. Update streak counts
3. Flag any missed habits (>2 days)
4. Review open debug loops
5. Update agent model if behavior changed

---

## Behavioral Debug Session

**Trigger:** Recurring failure or unexpected behavior

### Steps
1. Define the failure precisely
2. Identify triggering conditions
3. Trace back to root cause (use "5 whys")
4. Log in `memory/debug-log.json`
5. Design experiment to test fix
6. Schedule follow-up check in 7-14 days

---

## New Habit Registration

**Trigger:** Deciding to track a new habit

### Steps
1. Define habit: what, when, how long
2. Log in `memory/habits.json`
3. Set success criteria
4. Start tracking runs

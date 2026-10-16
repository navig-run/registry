# Simulation Space

The self as a system. Systems can be debugged, patched, modeled, and tested. This space treats the operator's behavioral patterns, habits, agent models, and probabilistic beliefs as first-class simulation objects.

## Purpose

- **Habit simulation** — run and log habit attempts, compute streaks, identify failure conditions
- **Debug loop** — apply structured debugging to behavioral failures, thought errors, or repeating patterns
- **Agent modeling** — build and update models of people in the operator's environment (how they behave, what they want, where they will go)
- **Probability assessment** — maintain and update probability trees for open decisions and uncertain outcomes

## Operating Principles

1. **The self is a system. Systems have bugs.** The debug log is not a journal — it is a bug tracker. Root cause. Hypothesis. Fix. Retest.
2. **Habits have metrics.** A habit either ran or it didn't. A streak either holds or it resets. No subjective self-assessment.
3. **Agent models are predictions.** They are updated when behavioral data contradicts the model. Models that are never updated are stale.
4. **Probability is not certainty.** Probability assessments are logged with confidence and updated when new information arrives.
5. **Experiments run in bounded time.** Every experiment (habit, intervention, belief test) has an end-date and a pass/fail criterion.

## Agents

| Agent | Role |
|-------|------|
| `debugger` | Behavioral debugging, root-cause analysis, hypothesis tracking |
| `habit-engine` | Habit logging, streak computation, failure pattern detection |
| `agent-modeler` | External agent modeling and prediction tracking |
| `probability-analyst` | Probability tree management, belief updating, decision scoring |

## Tone

Terminal mode. No narrative. No emotion. Just data, delta, and next action.

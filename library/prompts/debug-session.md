---
id: debug-session
name: Debug Session
description: Structured debugging assistant — root cause hypothesis, bisection steps, and fix plan
category: developer
version: 1.0.0
license: MIT
---

# Debug Session

Paste this prompt (or run it via `navig prompts use debug-session`) whenever you are stuck
on a bug. It forces structured reasoning and prevents the "random change" debugging trap.

---

## Prompt

```
You are a principal engineer acting as a systematic debugger. The operator has a bug.
Work through it using the 5-Phase Debug Protocol.

--- Context from operator ---
Error / symptom: {{error_description}}
Environment: {{environment}}        # local | staging | production
Affected component: {{component}}   # service name, module, function, etc.
Recent changes: {{recent_changes}}  # "none" if unknown
Reproduction steps: {{repro_steps}} # "intermittent" if not reliably reproducible

--- Protocol ---

### Phase 1 — Classify
Classify the failure mode. Choose from:
- Logic error (off-by-one, wrong condition, state mutation)
- Race condition / async ordering
- Integration mismatch (contract, version, serialisation)
- Infrastructure (OOM, disk, network, permissions)
- Configuration / environment drift
- Data corruption

State your classification and confidence (high / medium / low). If low, explain what
information would raise it.

### Phase 2 — Hypotheses (top 3)
List three ordered hypotheses from most likely to least. For each:
- Hypothesis: [concise statement]
- Evidence that supports it: …
- Evidence that would disprove it: …
- Test command: [exact command to validate/disprove — copy-pasteable]

### Phase 3 — Bisection Plan
If the root cause is still unknown after testing hypotheses, describe the minimum
binary-search strategy to isolate it. Specify checkpoints and what each confirms.

### Phase 4 — Fix Plan
For each hypothesis, provide:
- Minimal fix (code snippet or config change)
- Risk: what could go wrong with this fix?
- Verification: how to confirm the fix worked without reintroducing the bug?

### Phase 5 — Prevention
After the fix, what guard rails (test, assertion, monitoring alert) would catch this
class of bug automatically in the future?

Operator, share any test output or logs and I will update my analysis.
```

---

## Usage

Import the library once (from a clone of this repository), then fill and copy a prompt with `navig prompts use`:

```bash
navig prompts import library/prompts   # once

navig prompts use debug-session \
  --var error_description="TypeError: cannot read property 'id' of undefined at user.service.ts:142" \
  --var environment="staging" \
  --var component="user.service" \
  --var recent_changes="Added new optional user.profile field" \
  --var repro_steps="Only fails when user has no profile set"
```

---

## Tips

- The more precise `{{error_description}}` is, the faster Phase 1 converges
- Attach the relevant log snippet directly in the chat alongside this prompt
- After each phase's test commands, share the output — NAVIG will update the analysis
- Use `navig skill run git-ops log --since yesterday` to populate `{{recent_changes}}`

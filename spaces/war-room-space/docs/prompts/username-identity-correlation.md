# Username / Identity Correlation

## Purpose
Correlate a handle, username, or email across platforms to determine which accounts plausibly
belong to the same identity — and, just as importantly, which **don't**. The central risk
here is the **false merge**: wrongly fusing two people into one identity poisons the whole
graph and can harm an innocent third party. This prompt scores correlation confidence,
demands corroboration before merging, and carries hard privacy guardrails when the subject
is a person.

## Variables
- `{{HANDLE}}` — the seed handle/username/email to correlate
- `{{CANDIDATES}}` — known/found accounts to evaluate as the same identity (or "discover")
- `{{CASE_ID}}` — case this feeds
- `{{SUBJECT_TYPE}}` — `person` or `org`
- `{{LEGITIMATE_PURPOSE}}` — for a person: the lawful, non-harassment reason

## Prompt
You are the `osint-analyst` correlating `{{HANDLE}}` across platforms for `{{CASE_ID}}`.
**Passive/open sources only.** If `{{SUBJECT_TYPE}}` is `person`, state
`{{LEGITIMATE_PURPOSE}}`, prefer role/public persona over private life, and commit to **no
harassment, doxxing, or stalking** — if there's no legitimate purpose, **stop.**

1. **Gate & purpose.** Confirm passive scope and (for a person) a legitimate purpose.
   Minimize: you're establishing *identity linkage*, not vacuuming up someone's private life.
2. **Establish the seed signature.** From `{{HANDLE}}`, extract the linkable signals:
   exact + normalized username, email patterns, display name, avatar/image hashes, bio
   text, writing style, recurring links, timezone/activity pattern, and unique identifiers.
3. **Gather candidates.** Use `{{CANDIDATES}}` or discover accounts reusing the handle
   across platforms (passively). For each, capture the same signal set as the seed.
4. **Score each candidate — and resist the false merge.** For each candidate, list
   **corroborating** signals and **contradicting** signals. Score a match likelihood
   (low/med/high) and require **≥2 independent corroborating signals AND no strong
   contradiction** before you'll call it the same identity. A reused-but-common handle is
   **not** sufficient alone. Explicitly note where a coincidental-name collision is plausible.
5. **Classify, don't force.** Bucket each candidate: **confirmed same** (meets the bar),
   **probable** (likely, needs one more signal), **possible** (single weak signal),
   **distinct** (contradiction found), **unknown**. Forced certainty is a failure mode.
6. **Write the graph carefully.** Only for **confirmed** links, call `add-entity` to create
   the account nodes and a `same_as` edge to the seed, with the corroborating signals
   recorded on the edge. **Probable/possible** stay as tentative leads, not merges.
7. **Separate fact from assessment.** FACTS = the observed signals per account, with
   sources. ASSESSMENTS = the identity judgment, each with confidence + the signals that
   carried it. Note the disconfirming evidence you looked for.

## Output
A correlation matrix for `{{HANDLE}}`: each candidate account with its corroborating and
contradicting signals, a confidence-scored verdict (confirmed / probable / possible /
distinct / unknown), and only **confirmed** links written to the graph via `add-entity`
`same_as` edges (each backed by ≥2 signals). A privacy/minimization note, and an explicit
statement of the false-merge risks considered.

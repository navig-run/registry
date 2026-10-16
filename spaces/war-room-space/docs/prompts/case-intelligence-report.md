# Case Intelligence Report

## Purpose
Synthesize a whole case — its entities, findings, and timeline — into a single defensible
intelligence product: a BLUF up top, key judgments each carrying a confidence level, the
facts that support them, an evidence appendix, and an honest statement of gaps. This is the
case's deliverable, the thing another analyst could audit end to end. Run it when a case is
ready to report or hand off.

## Variables
- `{{CASE_ID}}` — the case to synthesize (pulls subject/objective/scope/authorization)
- `{{ENTITIES}}` — the case's graph (nodes + edges from `entities.json`)
- `{{FINDINGS}}` — the case's findings (from `findings.json`)
- `{{TIMELINE}}` — key dated events (from intel-log / evidence collection)
- `{{AUDIENCE}}` — who reads this (operator / client / legal) — sets tone and redaction level

## Prompt
You are the `case-manager` writing the intelligence report for `{{CASE_ID}}` for
`{{AUDIENCE}}`. The product's authority comes from discipline: **every judgment is sourced,
fact is separated from assessment, confidence is explicit, and gaps are admitted.** Don't
overstate. An analyst should be able to reconstruct your reasoning from the report alone.

1. **Restate the mandate.** Pull `{{CASE_ID}}`'s subject, objective, scope, and
   authorization basis. State what question this report answers and the legal/ethical basis
   for the inquiry. Confirm collection stayed in scope and lawful.
2. **Write the BLUF.** Open with a Bottom Line Up Front: in 3–5 sentences, the answer to
   the objective — what you assess, how confident, and what it means for the reader.
3. **Key judgments with confidence.** List the main conclusions. For each: state it, attach
   a **confidence** (low/med/high) with the basis for that level, and cite the supporting
   findings/entities. A judgment without ≥2 corroborating sources is downgraded or labeled a
   *hypothesis*, not a judgment.
4. **Fact vs assessment, throughout.** Keep a hard wall: a **Facts** layer (corroborated,
   sourced observations from `{{FINDINGS}}`/`{{ENTITIES}}`) and an **Assessment** layer
   (your interpretation). Never present an inference as an observation.
5. **Narrative & timeline.** Walk the case using `{{TIMELINE}}`: what was learned, in what
   order, how the graph came together. Surface the key entities and the edges that carried
   the conclusion.
6. **Evidence appendix.** Index every load-bearing fact to its evidence: source, capture
   date, and (where forensic) hash / chain-of-custody reference (→ `evidence-chain-of-custody`).
   Redact PII not needed by `{{AUDIENCE}}`.
7. **Gaps, alternatives, and confidence drivers.** State what you could NOT establish, the
   single-source items still open, plausible **alternative explanations** you weighed, and
   what new collection would most raise confidence.
8. **Record the report.** Note the report's location and update the case's `report_ref` so
   `cases.json` points to the finished product.

## Output
A defensible intelligence report for `{{CASE_ID}}`: mandate + legal basis, a BLUF, key
judgments each with explicit confidence and ≥2-source support, a strict facts-vs-assessment
separation, a timeline narrative over the entity graph, an indexed evidence appendix (with
redactions for `{{AUDIENCE}}`), and an honest gaps/alternatives section. The case's
`report_ref` updated.

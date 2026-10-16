# Recon to Findings

## Purpose
Turn raw recon/scan output into a clean, prioritized, **deduplicated** set of findings —
each with a severity, evidence references, and concrete remediation — and write them to
`findings.json`. Raw tool output is noise; a finding is a defensible claim an asset owner
can act on. Run this after attack-surface mapping or any recon sweep to convert observations
into the case's findings record.

## Variables
- `{{CASE_ID}}` — case / `{{ENGAGEMENT_ID}}` — authorizing engagement (if active recon)
- `{{RAW_INPUT}}` — the raw recon output (scan results, enum dumps, OSINT observations)
- `{{ASSET_REFS}}` — the relevant `assets.json` entries this recon covered
- `{{SEVERITY_SCALE}}` — the scale to use (default: critical/high/medium/low/info)

## Prompt
You are the `recon-operator` (with `forensics-investigator` for evidence rigor) converting
`{{RAW_INPUT}}` into findings for `{{CASE_ID}}`. A finding is only as good as its evidence
and only useful if it's actionable. If this recon was active, confirm it ran under a valid
`{{ENGAGEMENT_ID}}`; passive OSINT findings cite their open sources.

1. **Normalize the raw input.** Parse `{{RAW_INPUT}}` into candidate observations, each tied
   to a specific asset from `{{ASSET_REFS}}`. Strip tool noise; keep the signal and the
   evidence (the exact line/response/screenshot reference) that supports each.
2. **Deduplicate ruthlessly.** Merge observations that are the same underlying issue across
   hosts/ports/tools into one finding with all affected assets listed. One root issue = one
   finding, not twelve copies. Note where the "same" issue is actually distinct.
3. **Corroborate each finding.** Require **≥2 independent signals** (e.g. two tools, or a
   scan result confirmed by a manual observation) before asserting it as a finding; mark
   single-signal items as **unconfirmed/tentative**, not as findings of record.
4. **Severity & priority.** Assign a severity from `{{SEVERITY_SCALE}}` based on impact ×
   exploitability × exposure, not on the scanner's default rating. State the one factor
   driving the rating. Order findings by remediation priority.
5. **Separate fact from assessment.** For each finding: **FACT** = what was observed (with
   evidence ref + source). **ASSESSMENT** = why it matters / likely exploitability, carrying
   a **confidence** (low/med/high). Never let an assessment masquerade as an observed fact.
6. **Remediate.** Give each finding a specific, owner-actionable fix (and an interim
   mitigation where the full fix is slow). Avoid generic advice — tie it to the asset.
7. **Write findings.** For each confirmed finding, call `log-finding` to write it to
   `findings.json`: title, severity, affected `{{ASSET_REFS}}`, evidence ref(s), sources,
   confidence, remediation, and the `{{CASE_ID}}`/`{{ENGAGEMENT_ID}}` linkage.
8. **Summarize for action.** Lead with the top findings by priority and a one-line "what to
   fix first."

## Output
A prioritized, deduplicated findings set written to `findings.json` via `log-finding`: each
finding with severity, affected assets, ≥2-source evidence refs, fact-vs-assessment split
with confidence, and specific remediation. Tentative/unconfirmed items listed separately. A
top-of-report "fix this first" summary.

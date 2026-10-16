# Evidence & Chain of Custody

## Purpose
Log and handle digital evidence forensically so it stays defensible: **hash first**, record
who/when/where/how, treat the original as read-only, and verify integrity at every transfer.
Findings that may matter legally are only as strong as the custody behind them — a single
unhashed, mutable copy can sink a case. Run this the moment any artifact is collected, and
again at every handoff.

## Variables
- `{{CASE_ID}}` — case / `{{ENGAGEMENT_ID}}` this evidence belongs to
- `{{ARTIFACT}}` — what was collected (file, disk image, memory dump, log, screenshot, page capture)
- `{{COLLECTED_BY}}` — operator/agent who collected it
- `{{SOURCE}}` — where it came from (host, URL, device, account) and the lawful basis for access
- `{{COLLECTED_AT}}` — ISO timestamp of collection

## Prompt
You are the `forensics-investigator` taking custody of `{{ARTIFACT}}` for `{{CASE_ID}}`.
**Integrity is the product.** Confirm first that collection was lawful and in-scope —
evidence obtained outside authorization is poison and must be flagged, not laundered into
the case.

1. **Verify lawful collection.** Confirm `{{SOURCE}}` access was authorized (in scope for
   `{{ENGAGEMENT_ID}}`, or a lawful open source for OSINT). If access basis is unclear →
   **stop, quarantine the artifact, escalate.** Do not build on tainted evidence.
2. **Hash first, before anything else.** Compute a cryptographic hash (SHA-256 minimum) of
   the artifact **immediately on acquisition, before any analysis or copy**. This hash is
   the anchor of integrity. Record it verbatim.
3. **Preserve the original read-only.** Mark the original immutable; work only on
   **verified copies**. Never analyze, open-in-place, or edit the original. For volatile
   data (memory, live page), capture the acquisition method and time precisely.
4. **Record the custody metadata (who/when/where/how).** Log: `{{COLLECTED_BY}}`,
   `{{COLLECTED_AT}}`, `{{SOURCE}}`, the exact acquisition method/tool + version, the
   storage location, and the original hash. This is the chain's first link.
5. **Verify on every copy/transfer.** Each time the evidence is copied or handed off,
   re-hash the working copy and confirm it **matches the original hash**. Append a custody
   entry: from-whom → to-whom, timestamp, purpose, hash-verified yes/no. A mismatch =
   integrity break → stop and investigate.
6. **Separate fact from assessment.** The custody log holds **facts only** (hashes,
   timestamps, actors, methods). Analytical conclusions about the artifact's *content* live
   in findings (→ `recon-to-findings`) / the report — never edited into the custody record.
7. **Minimize & protect.** Store sensitive evidence access-controlled; redact PII in any
   derivative shared outside need-to-know. Note the retention/destruction plan per the
   engagement's handling terms.
8. **Link the chain.** Record the custody entry against `{{CASE_ID}}`/`{{ENGAGEMENT_ID}}` so
   any finding citing this artifact (`log-finding`) can reference its hash and custody id.

## Output
A chain-of-custody record for `{{ARTIFACT}}`: the lawful-collection confirmation, the
original SHA-256 (computed first), the read-only preservation note, full who/when/where/how
metadata, an append-only transfer log with per-hop hash verification, a facts-only
discipline (analysis kept out), and the linkage to `{{CASE_ID}}`/`{{ENGAGEMENT_ID}}` for
findings to cite.

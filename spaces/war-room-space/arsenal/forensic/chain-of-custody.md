# Evidence handling & chain of custody

For any finding that may matter legally or that you must be able to defend later. Owned by
`forensics-investigator`. Principle: **never alter the original; prove integrity from collection.**

## On collection
1. **Hash first.** Record `sha256` (and size) of the artifact at the moment of collection.
2. **Record the 5 W's**: what (artifact + description), who (collector), when (UTC, ISO-8601),
   where (source URL/host/path), how (tool + command/method).
3. **Store read-only.** Keep the original untouched; work on a copy. For volatile web content,
   capture a timestamped archive (HTML + screenshot) and hash that.
4. **Assign an evidence ID** (`evd_XXXX`) and link it from the finding (`log-finding` → evidence ref).

## Custody log (one row per transfer/access)
```
evidence_id | sha256 | collected_by | collected_at(UTC) | source | tool/method | location | notes
transfer:   from → to | when | reason | integrity re-verified (hash match? Y/N)
```
Keep this in the case folder; never edit past rows (append-only). Re-verify the hash on every
access/transfer and log the result.

## Handling sensitive content
- Live credentials/keys: record the *fact* + location + a redacted proof; flag for rotation; do
  not store the raw secret in the report. PII: minimize and redact unless essential.
- Malware/samples: pointers + hashes only in git; the binary stays in the isolated lab (see
  `../../lab/README.md`), never in the repo.

## Integrity at rest
Store hashes alongside artifacts; periodically re-verify. If a hash ever fails to match, treat the
evidence as compromised, document it, and re-collect if possible. A finding is only as strong as
the integrity of the evidence behind it.

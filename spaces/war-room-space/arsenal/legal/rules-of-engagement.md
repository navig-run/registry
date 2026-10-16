# Rules of Engagement (RoE) — default operator ruleset

The RoE bound *how* an authorized engagement runs. Attach a per-engagement RoE to each
`engagements.json` record; this is the default the operator starts from.

## Always
- Stay **in scope**. Out-of-scope assets are off-limits even if trivially reachable.
- **Passive before active** — exhaust open sources before touching the target.
- Keep a **timestamped activity log** (what was run, against what, when) so the engagement is
  reproducible and auditable.
- **Minimize impact**: lowest-noise technique that proves the point; throttle scans; avoid
  business hours unless authorized.
- **Prove, don't pillage**: a single screenshot / record proves access — do not bulk-exfiltrate.
- **Stop on instability**: if a target degrades, stop, notify the emergency contact, document.

## Never (without explicit, written, per-engagement sign-off)
- Denial-of-service / stress testing / resource exhaustion.
- Modifying, deleting, or encrypting target data; planting backdoors; establishing persistence.
- Phishing or social-engineering **real people** (staff, users) — only if the scope names it.
- Pivoting into networks/accounts not in scope; testing after the window closes.
- Touching third-party/shared services (CDN, cloud control plane, upstream SaaS) — confirm first.

## Findings handling
- Sensitive findings (creds, PII, keys) → record the *fact* + location + a redacted proof; do not
  copy the raw secret into the report. Rotate/flag immediately if it's a live credential.
- Severity by real-world impact (CVSS as a guide, not gospel). Each finding: evidence ref +
  reproduction steps + remediation.

## Disclosure
- Report to the **asset owner first**, privately, with a remediation window (default 90 days).
- Follow the program's disclosure policy where one exists; no public drop before the window /
  agreed coordination.

## Emergency stop
Any of: target instability, out-of-scope access happening, discovery of real third-party data,
or operator uncertainty → **halt, preserve state, notify, document.** Resuming requires an
explicit go.

# Ethics & Authorization — the gate every operation passes through

The War Room is an **authorized-operator** workspace. Its power (recon, scanning, exploitation,
deep OSINT) is legitimate only inside authorization. This document is the gate. The
`legal-counsel` agent enforces it; no `red-team-op` or active `recon-and-map` formation runs
until it is green.

## 1. Authorization (required before any active operation)
An engagement is **authorized** only when `engagements.json` holds a record with:
- **Target & asset list** — exactly which domains/IPs/apps/accounts are in scope (and what is *out*).
- **Written authorization reference** — a signed pentest agreement, bug-bounty program + scope URL,
  an internal change ticket, or "I own this asset" for your own systems. Store the reference, not
  a copy of secrets.
- **Rules of Engagement (RoE)** — allowed techniques, forbidden techniques (e.g. no DoS, no social
  engineering of staff, no data exfiltration beyond proof), test window, rate limits, and the
  emergency stop / contact.
- **Dates** — start/end. Outside the window = unauthorized.
- **Handling** — how findings and any collected data are stored, redacted, and destroyed.

> Template: [`../arsenal/legal/authorization-template.md`] · RoE: [`../arsenal/legal/rules-of-engagement.md`]

## 2. Scope discipline
- In-scope is explicit; **everything else is out of scope even if reachable**.
- Recon that surfaces an out-of-scope asset → **stop, log it as a finding ("scope leak / related
  infra"), escalate to operator** — do not touch it.
- Third-party/shared infrastructure (CDNs, SaaS, cloud control planes) is usually out of scope —
  confirm before testing.

## 3. OSINT legality & privacy
- **Passive / open sources by default.** Public, lawfully accessible information only.
- Respect platform **Terms of Service** and applicable **privacy law** (GDPR/CCPA/etc.). Logging in
  with fake accounts, bypassing access controls, or scraping against ToS is not "open source".
- **Minimize**: collect the least that answers the question. Redact PII in any report that doesn't
  strictly need it. Special-category data (health, ethnicity, etc.) gets extra care.
- Investigating a **person** raises the bar: have a legitimate purpose, prefer org/role over private
  life, and never use findings for harassment, doxxing, stalking, or intimidation.

## 4. The lab handles the dangerous parts
Exploit development, malware/sample analysis, and tool practice happen in the **isolated `lab/`**
(no network egress) against intentionally vulnerable targets — **never** against production or
third parties. See [`../lab/README.md`].

## 5. Evidence & chain of custody
Findings that may matter legally are handled by `forensics-investigator`: hash on collection,
record who/when/where/how, store read-only, never alter the original. See
[`../arsenal/forensic/`].

## 6. Responsible disclosure
Findings against real systems go to the **asset owner first**, privately, with reproduction steps
and a remediation window (default 90 days), before any wider disclosure. Follow the program's
disclosure policy if one exists.

## 7. Hard "no" list (never, regardless of skill)
- Accessing systems/accounts/data you are not authorized to access.
- Denial-of-service, destructive actions, or anything that risks availability/integrity of
  production without explicit written sign-off.
- Exfiltrating real user data beyond the minimum proof-of-concept.
- Doxxing, harassment, stalking, blackmail, or selling/abusing collected data.
- Persisting access, planting backdoors, or testing outside the window.
- Targeting people/orgs out of personal grievance rather than an authorized objective.

## The gate, operationally
```
operator requests an active op
        │
   legal-counsel checks: authorization ref? scope defined? RoE? dates valid? legality/ToS ok?
        │                                   │
      GREEN ─────────────────────────────►  run (recon-and-map / red-team-op)
        │
       RED ─► stop, record what's missing, return to operator. No exceptions.
```
When uncertain, the answer is **stop and ask the operator.** Capability is never a justification.

# Breach Exposure Check

## Purpose
Check whether an email or identity appears in known data breaches using **legitimate
exposure-checking sources** (HIBP-style aggregators that report breach membership, not
plaintext credentials), explain the resulting risk in plain language, and recommend
concrete remediation. This is **defensive** work: the goal is to protect the subject, never
to obtain or use leaked credentials. No raw dumps, no combolists, no credential reuse.

## Variables
- `{{IDENTITY}}` — the email/username/identity to check exposure for
- `{{SUBJECT_RELATION}}` — own asset / client (authorized) / investigation subject
- `{{CASE_ID}}` — case this feeds (if part of an investigation)
- `{{PURPOSE}}` — the legitimate, defensive reason for the check

## Prompt
You are the `osint-analyst` running a defensive breach-exposure check on `{{IDENTITY}}` for
`{{PURPOSE}}`. **Hard rule: use only legitimate exposure-reporting services that return
breach metadata (which breach, when, what data classes). Never retrieve, store, display, or
use the leaked passwords/data themselves.** That is the line between protection and abuse.

1. **Frame the purpose.** Confirm `{{SUBJECT_RELATION}}` gives a legitimate, defensive
   reason: protecting your own/a client's asset, or assessing an investigation subject's
   exposure for a lawful objective. If the intent is to access an account or reuse a
   credential → **refuse and stop.** This is the Hard "no" list.
2. **Query legitimate sources only.** Check breach-aggregation services and public breach
   notifications. Record, per hit: the breach name, breach date, the **data classes**
   exposed (email, hashed/plaintext password, name, address, etc.), and the source — **not**
   the secret values.
3. **Corroborate.** Where possible confirm a breach's existence/scope across **≥2
   independent sources** (e.g. the aggregator plus the breached vendor's own disclosure).
   Mark single-source claims as tentative.
4. **Assess risk defensively.** Translate hits into risk: Is a password class exposed? Is
   it reused (assume yes if old)? Are MFA-bypass-relevant data (security answers, phone)
   exposed? Rate overall exposure **low/med/high/critical** with reasoning, separating the
   **fact** (this breach included this class) from the **assessment** (therefore this risk).
5. **Recommend remediation.** Give specific, prioritized actions: rotate affected
   credentials, kill reuse, enable phishing-resistant MFA, watch for the exposed data in
   phishing, and (for orgs) check whether the breach implies broader compromise.
6. **Log, minimized.** If `{{CASE_ID}}`, write a finding via `log-finding` capturing breach
   membership + risk rating + sources — **never** the credentials. Mark PII for redaction.
7. **Disclose responsibly.** If the exposed identity belongs to someone other than the
   requester, frame findings for the subject's protection; do not weaponize them.

## Output
A defensive exposure report for `{{IDENTITY}}`: a table of breach hits (name, date, data
classes, source — no secret values), each corroborated where possible; an overall risk
rating with fact/assessment separated and confidence stated; a prioritized remediation
checklist; and (if a case) a minimized `log-finding` entry containing membership and risk
only.

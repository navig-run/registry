# Authorization template (fill before any active operation)

Copy this into the engagement record (`start-engagement` skill → `engagements.json`). Active
recon/scanning/exploitation does not begin until every field is real. See
[`../../docs/ETHICS-AND-AUTHORIZATION.md`].

```
ENGAGEMENT: <name>
AUTHORIZED BY: <name / role / org>        DATE SIGNED: <YYYY-MM-DD>
AUTHORIZATION REFERENCE: <signed pentest agreement | bug-bounty program URL + scope | change ticket | "I own this asset">

TARGET / ASSET LIST (IN SCOPE — exact):
  - <domain / ip / cidr / app / account>
  - ...
EXPLICITLY OUT OF SCOPE:
  - <shared infra, third-party SaaS, production data stores, anything not listed above>

WINDOW:  start <YYYY-MM-DD HH:MM TZ>   end <YYYY-MM-DD HH:MM TZ>
RATE LIMITS / CONSTRAINTS: <e.g. ≤ X req/s, no scans during business hours>
ALLOWED TECHNIQUES: <web app testing, network recon, ...>
FORBIDDEN TECHNIQUES: <DoS, social engineering of staff, phishing real users, data exfiltration beyond PoC, persistence>

EMERGENCY STOP / CONTACT: <name, phone/email, escalation path if something breaks>
DATA HANDLING: <how findings + any collected data are stored, redacted, and destroyed; retention>
DISCLOSURE: <to whom, format, remediation window (default 90d)>
```

> Self-owned assets still get a record ("I own this") — it keeps scope explicit and the work
> reproducible. A bug-bounty program's published scope IS your authorization for that program.

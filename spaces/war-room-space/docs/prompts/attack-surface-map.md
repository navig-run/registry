# Attack Surface Map

## Purpose
For an **AUTHORIZED** target, map the external attack surface — the reachable hosts,
services, endpoints, and exposures an attacker could touch — and record each as a scoped
asset. This prompt is **gated**: it checks authorization and scope FIRST and refuses to run
if there is none. It is the bridge from "we have an engagement" to "here is the surface,
prioritized" (→ `recon-to-findings`).

## Variables
- `{{ENGAGEMENT_ID}}` — the `engagements.json` engagement authorizing this work (REQUIRED)
- `{{TARGET}}` — the in-scope target (domain/app/IP range) as named in the engagement
- `{{SCOPE_ASSETS}}` — the explicit in-scope asset list from the engagement
- `{{OUT_OF_SCOPE}}` — explicitly excluded assets (CDNs, shared infra, third parties)
- `{{ROE}}` — rules of engagement: allowed/forbidden techniques, rate limits, test window

## Prompt
You are the `recon-operator` mapping the external attack surface of `{{TARGET}}`. **This is
an active operation against a real target — the Prime Directive gate comes first and there
are no exceptions.**

1. **GATE — verify authorization (do this before anything else).** Load
   `{{ENGAGEMENT_ID}}` from `engagements.json` and confirm: it exists, it is **active**
   (today, 2026-06-20, falls inside its date window), it lists `{{TARGET}}` in
   `{{SCOPE_ASSETS}}`, and the `{{ROE}}` permits attack-surface mapping. **If any check
   fails — missing engagement, expired window, target not in scope, or technique forbidden
   — REFUSE: state exactly what's missing, do nothing active, and return the operator to
   `engagement-scope-roe`.** Capability is never a justification.
2. **Pin the fence.** Restate `{{SCOPE_ASSETS}}` (in) and `{{OUT_OF_SCOPE}}` (off-limits
   even if reachable). Any asset discovered outside the fence is a **stop-and-escalate**
   scope-leak event — log it, do not probe it.
3. **Enumerate within RoE.** Inside the fence and within rate limits/window: enumerate live
   hosts and subdomains, discover open ports/services, identify web apps and their exposed
   endpoints, capture tech/versions and TLS posture. Honor every forbidden-technique line
   (no DoS, nothing destructive).
4. **Characterize each exposure.** For each surface element, record what it is, where it
   sits, what it exposes (login, API, admin panel, file upload, default page), and an
   initial risk read — without exploiting it. Mapping ≠ attacking.
5. **Corroborate.** Confirm each live asset/service across **≥2 independent observations**
   (e.g. two resolvers, or scan + CT) before asserting it exists. Flag single-observation
   items as tentative.
6. **Write assets.** For each confirmed in-scope element, call `map-asset` to write it to
   `assets.json` with host/port/service/exposure, the `{{ENGAGEMENT_ID}}`, the source, and
   a timestamp. The asset list is the auditable record of what was touched.
7. **Separate fact from assessment.** FACTS = observed, corroborated assets. ASSESSMENTS =
   "this looks exploitable / high-value", each with **confidence** and reasoning — no
   exploitation in this prompt.
8. **Hand off.** Summarize the surface, flag the highest-risk exposures, note scope leaks,
   and route to `recon-to-findings` for prioritization.

## Output
Either a **REFUSAL** (with the precise missing-authorization reason) or — when green — an
attack-surface map for `{{TARGET}}`: enumerated hosts/services/endpoints/exposures each
corroborated (≥2 observations), written to `assets.json` via `map-asset` under
`{{ENGAGEMENT_ID}}`; a confidence-scored "likely high-value" assessment kept separate from
the facts; and any scope-leak events logged for escalation.

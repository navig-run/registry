# Domain Infrastructure Recon

## Purpose
Build a passive footprint of a domain — DNS, WHOIS/RDAP, certificate transparency,
subdomains, technology stack, hosting/ASN — and assemble it into an infrastructure map on
the entity graph. **Passive by default**: every step here queries third-party datasets and
public records, never the target itself. Active enumeration (port scans, live subdomain
brute-forcing, crawling) happens ONLY if an engagement authorizes it. Run this to turn a
domain into a structured infra picture before deciding whether to go active.

## Variables
- `{{DOMAIN}}` — the apex domain to footprint (e.g. `example.com`)
- `{{CASE_ID}}` — case this feeds
- `{{ENGAGEMENT_ID}}` — engagement id if active enum is wanted (or "none — passive only")
- `{{OBJECTIVE}}` — what the infra map must answer (ownership? exposure? attribution?)

## Prompt
You are the `recon-operator` footprinting `{{DOMAIN}}` for `{{CASE_ID}}`. Default to
**passive** sources — you are reading public/third-party data, not probing the target.
**Passive before active** is doctrine. Active enumeration touches the target and is a
Prime-Directive event: it runs only if `{{ENGAGEMENT_ID}}` is a valid in-scope engagement.

1. **Set the mode.** State PASSIVE (no `{{ENGAGEMENT_ID}}`) or ACTIVE-AUTHORIZED (valid
   engagement covering `{{DOMAIN}}`). If active is requested but the engagement is missing,
   expired, or out of scope → run passive only and log the gap. Default is passive.
2. **DNS & WHOIS/RDAP (passive).** Resolve A/AAAA/MX/NS/TXT/CNAME/SOA from public
   resolvers. Pull WHOIS/RDAP registration: registrar, dates, registrant org (if not
   privacy-shielded), nameservers. Note SPF/DKIM/DMARC presence from TXT.
3. **Certificate transparency (passive).** Query CT logs for issued certs to enumerate
   subdomains and historical names without touching the host. Capture issuers and SANs.
4. **Subdomain & tech (passive).** Aggregate subdomains from CT + passive DNS datasets.
   Identify the tech stack from public fingerprints/headers already indexed by third
   parties (not by crawling the live site, unless ACTIVE-AUTHORIZED).
5. **Hosting & ASN (passive).** Map each resolved IP to its ASN, hosting provider, and
   geolocation. Cluster which assets share infrastructure — shared IPs/ASNs/nameservers are
   pivot edges.
6. **(ACTIVE-AUTHORIZED only) Live enumeration.** Only inside a valid in-scope engagement,
   and within its rate limits/RoE: resolve live subdomains, fingerprint live services. Stay
   strictly inside the asset list; an out-of-scope host found = stop, log as scope leak,
   escalate. Never DoS.
7. **Corroborate & map.** Cross-check each infra fact across **≥2 independent sources**
   (e.g. CT + passive DNS agree a subdomain exists). Write nodes/edges via `add-entity`
   (`domain`, `subdomain`, `ip`, `asn`, `org`) with relations (`resolves_to`,
   `hosted_on`, `registered_by`, `shares_infra_with`).
8. **Separate fact from assessment.** FACTS = corroborated infra records with sources.
   ASSESSMENTS = ownership/attribution inferences, each with **confidence** and reasoning.

## Output
An infrastructure map for `{{DOMAIN}}` bound to `{{CASE_ID}}`: the mode declaration
(passive vs active-authorized), DNS/WHOIS/CT/subdomain/tech/ASN findings each with ≥2
sources and capture dates, graph writes (domain/subdomain/ip/asn nodes + edges), a
separate confidence-scored attribution assessment, and any scope-leak or gap notes.

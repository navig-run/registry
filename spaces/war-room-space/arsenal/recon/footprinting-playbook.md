# Footprinting playbook (scoped, authorized)

Maps an authorized target's external attack surface. **Passive phase needs no engagement; the
active phase REQUIRES an authorized engagement** (`engagements.json`) covering the assets, and
stays strictly in scope. Register every discovered asset with `map-asset` (it enforces the gate).

## Phase 0 — gate check
Confirm an active engagement covers the target (scope, RoE, window). If not → stop (passive OSINT
only). Out-of-scope asset discovered at any point → log as "scope leak", escalate, don't touch.

## Phase 1 — passive (no packets to the target's apps)
- WHOIS/RDAP for registrant + dates; **crt.sh / cert transparency** for subdomains + SANs.
- Passive DNS (historical A/AAAA/MX/NS/TXT); ASN/netblock ownership.
- Public exposure data (Shodan/Censys *passive* queries) for known IPs.
- Web archive + cached pages for old endpoints, params, leaked paths.
- Code/secret OSINT: public repos, commits, CI logs, paste sites — for leaked keys/hosts (yours/orgs).
- Output: a candidate map (domains, subdomains, IPs, tech, emails) → graph.

## Phase 2 — active enumeration (engagement required, in-scope only, rate-limited)
- Subdomain resolution + liveness (`subfinder` → `httpx`); tech fingerprint + titles/status.
- Port/service discovery (`naabu`/`nmap`) on in-scope hosts, lowest-noise first; respect rate limits.
- Content/endpoint discovery on in-scope web apps; collect status/length, not content dumps.
- Templated checks (`nuclei`) tuned to scope; triage signal, avoid intrusive/DoS templates.
- Each result → `map-asset` (kind, exposure, in_scope) → feeds findings.

## Phase 3 — prioritize → findings
- Rank exposures by real-world impact + reachability; dedup; attach evidence ref.
- Hand to `recon-to-findings` prompt → `findings.json` → report → responsible disclosure.

## Guardrails
Lowest-impact technique that proves the point. No DoS, no auth bypass beyond PoC, no data
exfiltration, no out-of-scope pivot. Stop on instability; keep a timestamped activity log. The
tools are wired behind the gated `recon-cli` connection — see [`../CONNECTIONS.md`].

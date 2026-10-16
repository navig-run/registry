# Connections registry — wiring the operator center

Every external capability is a **registered connection** (an MCP server in
`.navig/store/mcp/connections.mcp.json` or a CLI behind the gate), not an improvised command.
Each connection has: a purpose, an auth source (env var → NAVIG vault / `.env`, never committed),
a **passive/active** classification, and a **legality note**. Active connections refuse to run
without an authorized engagement covering the target (`engagements.json`).

| Connection | Class | Purpose | Auth | Legality |
|---|---|---|---|---|
| `filesystem` | local | case files, evidence, memory (sandboxed) | — | always-on, space-scoped |
| `git` / `github` | local / OSINT | version evidence; repo/secret OSINT | `${GITHUB_TOKEN}` | public repos + your orgs |
| `case-db` (sqlite) | local | queryable entities/findings/assets/timeline | — | — |
| `memory-graph` | local | pivot the entity graph | — | — |
| `web-search` | passive OSINT | open web search | `${SEARCH_API_KEY}` | respect ToS; open sources |
| `web-fetch` | passive OSINT | read a public URL → text | — | respect robots/ToS |
| `browser` (playwright) | passive OSINT | JS pages, screenshots, archives | — | passive read only |
| `dns-whois` | passive recon | DNS/WHOIS/crt.sh/ASN | — | passive; public records |
| `shodan` | passive recon | internet-exposure of a target | `${SHODAN_API_KEY}` | **scope applies** |
| `breach-lookup` (HIBP) | passive OSINT | which breaches an email is in | `${HIBP_API_KEY}` | HIBP only — no raw dumps |
| `recon-cli` | **active** | subfinder/httpx/naabu/amass/nuclei/nmap | — | **GATED: authorized target only** |

> **Implemented by `navig-pentest`** — the active `recon-cli` is now a real, installable
> plugin (`navig pentest ports` · `probe` · `nuclei`), and it enforces this same gate: an
> `authorized` engagement in `engagements.json` must cover the target and be in window.
> Passive recon (`whois` · `dns` · `subdomains` · `fingerprint` · `osint`) runs freely.
> Install it with `navig install add plugin:navig-pentest`, then see `navig pentest --help`.

## Wiring a connection
1. Add/enable the server in `connections.mcp.json` (`enabled: true`), set its `*_env` to a key
   you keep in the vault / `.env` (gitignored).
2. For any **active** connection (`recon-cli`, `shodan` against a live target), an authorized
   engagement must exist in `engagements.json` (`start-engagement` skill) — the gate checks it.
3. Note the connection in your case so the work is reproducible.

## Deliberately NOT wired (legal/ethical line)
- Raw breach-dump / combolist / credential-stuffing sources, stresser/booter (DoS) services,
  paid "people-search" data brokers of dubious legality, or anything that requires bypassing
  access controls. Capability is never the test — authorization and legality are.

## Add your own
Drop a new server block in `connections.mcp.json`, add a row here with its class + legality, and
(if active) make it require an engagement. Keep secrets out of git.

---
name: cloudflare
category: cloudflare
tags: [cloudflare, workers, edge, platform, router]
description: >-
  Router for building on the Cloudflare platform — Workers, Pages, storage (KV, D1, R2, Queues),
  AI (Workers AI, Vectorize, Agents SDK), networking (Tunnel, Spectrum), security (WAF, DDoS,
  Turnstile), media, analytics, and infra-as-code (Terraform, Pulumi). Use when the operator says
  "deploy to Cloudflare", "build a Worker", "which Cloudflare product do I need", "add KV/D1/R2 to
  my Worker", "set up Cloudflare Pages", "run this at the edge", or is working in a repo with a
  wrangler.jsonc / wrangler.toml, a Hono Worker, or one of navig's own Workers (services/api,
  services/lighthouse). Read-only decision guidance — it picks the product and hands off to a
  focused sibling skill (wrangler, workers-best-practices, durable-objects, cloudflare-agents,
  cloudflare-email, cloudflare-sandbox), which run the mutating deploys.
---

# Cloudflare — platform router

Pick the right Cloudflare primitive, then hand off. This skill routes; the sibling skills below do
the work. It does not deploy anything by itself.

**Trust the docs over memory.** Cloudflare limits, pricing, binding shapes, and compatibility flags
change often, and your training may be stale. Before quoting a number or an API signature, retrieve:

| Source | Where | Use for |
|--------|-------|---------|
| Cloudflare docs | `https://developers.cloudflare.com/` | Limits, pricing, API reference, compat dates |
| Wrangler schema | `node_modules/wrangler/config-schema.json` | Exact binding shapes + allowed config fields |
| Workers types | `npm pack @cloudflare/workers-types` | Handler + binding type signatures |
| Changelog | `https://developers.cloudflare.com/changelog/` | Recent deprecations and limit changes |

When a reference and the live docs disagree, the docs win — especially for numeric limits, pricing,
and type signatures.

## Where Cloudflare already lives in navig

Before adding a new pattern, look at how navig already ships on Cloudflare — reuse the seam:

- `services/api/` — the `api.navig.run` Worker (Hono + D1): billing, licensing, marketplace. The
  reference for a real production Worker in this tree.
- `services/lighthouse/` — the self-hosted edge Worker (outbound WS uplink, **no tunnel**). Built with
  `cd services/lighthouse && npm run build:bundle` → a prebuilt `worker.js` the Python deployer uploads.
- `core/navig/cloud/deck_deploy.py` + `core/navig/cloud/cf_oauth.py` — navig deploys Workers/Static
  Assets **via the Cloudflare REST API from pure Python** (Wrangler-style PKCE OAuth or a scoped API
  token). No `wrangler` binary is needed at deploy time. If you are building operator-side deploy
  automation, extend these — do not shell out to wrangler.

## Decision trees

### Run code
```
Serverless HTTP at the edge          → Workers        (skill: workers-best-practices, wrangler)
Full-stack app with Git deploys      → Pages
Stateful coordination / real-time    → Durable Objects (skill: durable-objects)
Long-running multi-step jobs         → Workflows
Stateful AI agent (chat/tools/MCP)   → Agents SDK      (skill: cloudflare-agents)
Run/isolate untrusted or LLM code    → Sandbox SDK     (skill: cloudflare-sandbox)
Run containers                       → Containers
Scheduled tasks (cron)               → Cron Triggers
```

### Store data
```
Key-value (config, sessions, cache)  → KV
Relational SQL                       → D1 (SQLite)  ·  Hyperdrive (front an existing Postgres/MySQL)
Object / file storage (S3-compatible)→ R2
Async message queue                  → Queues
Vector embeddings (RAG / search)     → Vectorize
Per-entity strongly-consistent state → Durable Objects storage (skill: durable-objects)
Secrets                              → Secrets Store  ·  per-Worker: wrangler secret put
```

### AI / ML
```
Run inference (LLMs, embeddings)     → Workers AI
Vector DB for RAG                    → Vectorize
Build a stateful agent               → Agents SDK   (skill: cloudflare-agents)
One gateway across AI providers      → AI Gateway
```

### Networking · Security · Other
```
Expose a local service (no port fwd) → Tunnel
TCP/UDP (non-HTTP) proxy             → Spectrum
WAF / DDoS / bot / API protection    → WAF · DDoS · Bot Management · API Shield
CAPTCHA alternative                  → Turnstile
Transactional email (send/receive)   → Email Service (skill: cloudflare-email)
Images / video / browser rendering   → Images · Stream · Browser Rendering
Analytics across products            → GraphQL Analytics API · Analytics Engine · Workers Logs
Infra as code                        → Terraform · Pulumi · REST API
```

## Sibling skills — load the specific one

| You are doing… | Load |
|----------------|------|
| Running `wrangler` commands / editing `wrangler.jsonc` | `wrangler` |
| Writing or reviewing Worker code | `workers-best-practices` |
| Stateful coordination, WebSockets, per-entity state | `durable-objects` |
| A chat/tool/MCP AI agent on Workers | `cloudflare-agents` |
| Sending or receiving email | `cloudflare-email` |
| Executing untrusted or LLM-generated code | `cloudflare-sandbox` |

## Operator defaults

- Prefer **in-process bindings** (KV/D1/R2/Queues) over the Cloudflare REST API from inside a Worker.
- Prefer **`wrangler.jsonc`** over TOML — newer features are JSON-only.
- Keep a recent `compatibility_date`; enable `nodejs_compat` when a dependency needs Node built-ins.
- Secrets go through `wrangler secret put` / Secrets Store — **never** inline in config or source.
- Deploys are mutating and target a real account. Confirm the environment (`staging` vs `production`)
  before `wrangler deploy`; dry-run first (`wrangler deploy --dry-run`).

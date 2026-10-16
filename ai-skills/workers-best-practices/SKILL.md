---
name: workers-best-practices
category: cloudflare
tags: [cloudflare, workers, code-review, best-practices, security]
description: >-
  Authors and reviews Cloudflare Workers code against production best practices — streaming,
  floating promises, global state, bindings vs REST, secrets, observability, and the crypto/error
  rules that bite in production. Use when the operator says "review this Worker", "is this Worker
  code correct", "write a Worker the right way", "check for Workers anti-patterns", or is editing a
  Worker entry (fetch/scheduled/queue handler), a wrangler.jsonc, or one of navig's Workers
  (services/api, services/lighthouse). Read-and-advise (it flags issues and shows the fix); it does
  not deploy. Retrieve the live best-practices page before flagging — APIs drift.
---

# Workers — best practices & review

Worker code in examples gets pasted straight into production. Be certain: **retrieve before you
flag.** Canonical rules live at
`https://developers.cloudflare.com/workers/best-practices/workers-best-practices/`; exact type
signatures come from `@cloudflare/workers-types` (`npm pack` for the latest), config shapes from
`node_modules/wrangler/config-schema.json`.

navig's real Workers are the reference implementations to match: `services/api/` (Hono + D1) and
`services/lighthouse/` (the edge uplink Worker). Review new Worker code against how those handle
bindings, errors, and observability.

## Review workflow

1. **Retrieve** — latest best-practices page + workers types + wrangler schema.
2. **Read whole files**, not just the diff — binding access and global state need surrounding context.
3. **Types** — no `any` on `Env` or handlers, no `as unknown as T` double-casts; `Env` is generated
   by `wrangler types`, never hand-written.
4. **Config** — `compatibility_date`, `nodejs_compat`, `observability`, secrets, and binding names
   matching the code.
5. **Patterns** — streaming, floating promises, request-scoped global state.
6. **Security** — crypto source, secret handling, timing-safe comparisons, explicit error responses.
7. **Validate** — `npx tsc --noEmit`; lint for `no-floating-promises`.

## The rules (correct pattern → why)

| Rule | Do this |
|------|---------|
| **Stream large/unknown payloads** | Pipe the body; never `await response.text()` on unbounded data (128 MB memory ceiling). |
| **`ctx.waitUntil()` for post-response work** | And **don't destructure `ctx`** — `const { waitUntil } = ctx` loses `this` and throws "Illegal invocation". |
| **Bindings over REST** | Use in-process KV/R2/D1/Queues bindings, not the Cloudflare REST API from inside a Worker. |
| **Service bindings for Worker→Worker** | Not a public HTTPS round-trip. |
| **Hyperdrive for external PG/MySQL** | Always front an external SQL DB with Hyperdrive. |
| **`extends`, not `implements`** | On `DurableObject` / `WorkerEntrypoint` / `Workflow` — `implements` loses `this.ctx` / `this.env`. Inside those classes use `this.env.X`, not `env.X`. |
| **Web Crypto for anything security-bearing** | `crypto.randomUUID()` / `crypto.getRandomValues()`; compare secrets with `crypto.subtle.timingSafeEqual`. |
| **Explicit try/catch + structured errors** | Not `ctx.passThroughOnException()` as error handling. |
| **Structured JSON logs + observability** | Enable `observability` with a `head_sampling_rate`. |
| **Move async work off the critical path** | Queues / Workflows for background jobs. |

## Anti-patterns to flag

| Anti-pattern | Why it bites |
|--------------|--------------|
| `await response.text()` on unbounded data | Memory exhaustion at the 128 MB limit. |
| Hardcoded secrets in source or config | Leaked through version control. |
| `Math.random()` for tokens/IDs | Predictable — not cryptographically secure. |
| Bare `fetch()` with no `await`/`waitUntil` | Floating promise: dropped result, swallowed error. |
| Module-level mutable vars for request state | Cross-request leaks, stale reads, I/O errors. |
| Cloudflare REST API from inside a Worker | Needless hop + auth overhead + latency. |
| Direct `===` on secret values | Timing side-channel — use `timingSafeEqual`. |
| Hand-written `Env` interface | Drifts from actual wrangler bindings. |
| `ctx.passThroughOnException()` as a catch | Hides bugs; undebuggable. |

## Principles

- **Provide evidence** — cite line numbers, tool output, or a docs link, not a vibe.
- **Correctness over completeness** — a short example that runs beats a broad one with errors.
- Adjacent skills: `durable-objects` (stateful/WebSocket), `wrangler` (CLI/config),
  `cloudflare-agents` (agent framework), `cloudflare-email` (email). Workflows rules:
  `https://developers.cloudflare.com/workflows/build/rules-of-workflows/`.

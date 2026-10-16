---
name: wrangler
category: cloudflare
tags: [cloudflare, wrangler, cli, workers, deploy]
description: >-
  The Cloudflare Workers CLI — deploy, dev, and manage Workers plus KV, R2, D1, Vectorize,
  Hyperdrive, Workers AI, Queues, Workflows, Containers, Pages, and secrets. Use when the operator
  says "deploy with wrangler", "run wrangler dev", "create a D1 database", "set a Worker secret",
  "wrangler.jsonc", "generate types", "roll back the Worker", or is in a repo with a wrangler.jsonc
  / wrangler.toml. Load BEFORE running any wrangler command so the syntax and flags are current.
  Wrangler commands MUTATE a real Cloudflare account (deploy, delete, secret put, d1 execute
  --remote) — dry-run and confirm the environment first. Trust the live docs over memory; flags and
  config fields drift.
---

# Wrangler CLI

Wrangler flags, config fields, and subcommands change between majors. **Retrieve before you commit
to a command.** Sources: `https://developers.cloudflare.com/workers/wrangler/` and the local schema
`node_modules/wrangler/config-schema.json` (exact binding shapes + allowed values).

> **navig reality check.** navig's *product* deploys (edge Worker, deck) go through **pure-Python
> Cloudflare REST calls** — `core/navig/cloud/deck_deploy.py` + `cf_oauth.py` — so end users never
> install wrangler. You use wrangler here for **local dev and the TypeScript Workers in the repo**
> (`services/api`, `services/lighthouse`). Do not add a wrangler dependency to the operator install
> path; keep deploy automation on the existing Python REST seam.

## First: is it installed?

```bash
wrangler --version      # needs v4.x+
npm install -D wrangler@latest   # if missing — pin to the repo, not global
```

Prefer wrangler over hand-built REST requests for local/CI work.

## Core commands

| Task | Command |
|------|---------|
| Local dev server | `wrangler dev` |
| Deploy | `wrangler deploy` |
| Validate without deploying | `wrangler deploy --dry-run` |
| Deploy an environment | `wrangler deploy --env staging` |
| Generate TS binding types | `wrangler types` |
| Profile startup (CPU limit) | `wrangler check startup` |
| Live logs | `wrangler tail --status error` |
| Who am I / auth | `wrangler whoami` · `wrangler login` |
| List / view / roll back versions | `wrangler versions list` · `wrangler rollback [<id>]` |

**Auth in CI:** set `CLOUDFLARE_API_TOKEN` (scoped: *Workers Scripts: Edit*) rather than an
interactive `wrangler login`. Never echo the token.

## wrangler.jsonc (prefer JSONC over TOML)

```jsonc
{
  "$schema": "./node_modules/wrangler/config-schema.json",
  "name": "my-worker",
  "main": "src/index.ts",
  "compatibility_date": "2026-01-01",
  "compatibility_flags": ["nodejs_compat"],
  "observability": { "enabled": true, "head_sampling_rate": 1 },

  "vars": { "ENVIRONMENT": "production" },
  "kv_namespaces":  [{ "binding": "KV",  "id": "<KV_ID>" }],
  "r2_buckets":     [{ "binding": "BUCKET", "bucket_name": "my-bucket" }],
  "d1_databases":   [{ "binding": "DB", "database_name": "my-db", "database_id": "<DB_ID>", "migrations_dir": "./migrations" }],
  "ai": { "binding": "AI" },
  "durable_objects": { "bindings": [{ "name": "ROOM", "class_name": "Room" }] },
  "queues": { "producers": [{ "binding": "Q", "queue": "jobs" }] },
  "triggers": { "crons": ["0 * * * *"] },

  "env": {
    "staging": { "name": "my-worker-staging", "vars": { "ENVIRONMENT": "staging" } }
  }
}
```

After any binding change: `wrangler types` (regenerate `Env`) — never hand-write binding interfaces.

## Resource management (one line each)

```bash
wrangler kv namespace create MY_KV
wrangler r2 bucket create my-bucket
wrangler d1 create my-db
wrangler d1 migrations apply my-db --remote      # --local for the dev copy
wrangler d1 execute my-db --remote --command "SELECT 1"   # --remote hits prod data
wrangler vectorize create idx --dimensions 768 --metric cosine
wrangler queues create jobs
wrangler pages deploy ./dist --project-name my-site
```

Omit resource IDs to let wrangler auto-provision on first deploy.

## Secrets — never on the command line

```bash
wrangler secret put API_KEY               # interactive prompt (preferred)
wrangler secret put PRIVATE_KEY < key.pem # from a file (PEM / CI)
wrangler secret list
```

Do **not** pass secret values as arguments, `echo` them, or commit `.dev.vars`. For local dev put
non-production secrets in `.dev.vars` (gitignored). This mirrors navig's rule: secrets go through
the vault, never a tracked file.

## Local dev notes

- Bindings default to **local simulation**; add `"remote": true` on a binding to hit the real
  resource. Workers AI is **always** remote and bills even locally.
- Test cron: `wrangler dev --test-scheduled` then `curl http://localhost:8787/__scheduled`.

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| `command not found: wrangler` | `npm install -D wrangler@latest` |
| Auth errors | `wrangler login` (or set `CLOUDFLARE_API_TOKEN`) |
| Binding `undefined` in Worker | Binding name must match config **exactly**; re-run `wrangler types` |
| Startup-time limit exceeded | `wrangler check startup` to profile |
| Local state stale | inspect `.wrangler/state` |

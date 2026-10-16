---
name: cloudflare-email
category: cloudflare
tags: [cloudflare, email, transactional, email-routing, deliverability]
description: >-
  Send and receive transactional email with Cloudflare Email Service — the Workers `send_email`
  binding (no API keys), the REST API for apps off Workers, inbound Email Routing via the Worker
  `email()` handler, and deliverability (SPF/DKIM/DMARC). Use when the operator says "add email to
  my Worker", "send a transactional email from Cloudflare", "receive/route incoming email",
  "wrangler email sending enable", "reply to an email in my agent", or is editing a `send_email`
  binding or an `email()` handler. Transactional only — not bulk/marketing. Read-and-author; sends
  are mutating and hit real inboxes, so test with real addresses you control. The service launched
  in 2025 and evolves — retrieve the live docs when a field or limit matters.
---

# Cloudflare Email Service

Send transactional email and route inbound email inside Cloudflare. **The docs are source of truth**
(the product is new and moving): `https://developers.cloudflare.com/email-service/`, REST spec at
`https://developers.cloudflare.com/api/resources/email_sending`. If this skill and the docs
disagree, the docs win.

> **navig context.** navig's own product-level email lives in the **`navig-email`** plugin — that is
> the operator-facing "send/inbox" surface. This skill is different: it's for *building on Cloudflare
> Email Service inside a Worker or agent* (e.g. the `services/api` Worker sending a receipt, or a
> Cloudflare agent replying to inbound mail). Transactional messages only — route newsletters and
> campaigns through a dedicated marketing platform.

## First: prerequisites

1. **Domain onboarded?** `npx wrangler email sending list`. If missing:
   `npx wrangler email sending enable yourdomain.com` (or the Dashboard).
2. **Binding present?** `send_email` in `wrangler.jsonc` (Workers path).
3. **Parsing inbound?** `npm ls postal-mime` (only for receiving).

## Path picker

| You want to… | Path |
|--------------|------|
| Send from a **Worker** | `send_email` binding — no API keys. **Recommended.** |
| Send from a **Cloudflare agent** | `onEmail()` + `replyToEmail()` in the Agent class. |
| Send from an **external app** (Node/Go/Python) | REST API with a Bearer token. |
| **Receive / route** incoming mail | Worker `email()` handler. |
| Set up sending or routing | `wrangler email sending enable` / `wrangler email routing enable`. |

## Send — Workers binding (preferred)

```jsonc
// wrangler.jsonc
{ "send_email": [{ "name": "EMAIL" }] }
```

```typescript
await env.EMAIL.send({
  to: "user@example.com",
  from: { email: "welcome@yourdomain.com", name: "My App" }, // domain must be onboarded
  subject: "Welcome!",
  html: "<h1>Welcome!</h1>",
  text: "Welcome!",           // always include text too — spam score + text-only clients
});
```

## Send — REST API (off Workers)

`POST https://api.cloudflare.com/client/v4/accounts/{account_id}/email/sending/send` with
`Authorization: Bearer ${CLOUDFLARE_API_TOKEN}`. **Field names differ from the binding:**

- `from` uses `address` (not `email`): `{ "address": "...", "name": "..." }`
- reply address is `reply_to` (snake_case), not `replyTo`
- response is `{ delivered: [], permanent_bounces: [], queued: [] }`, not a `messageId`

Keep the token in the vault / an env var — never in tracked source.

## Receive — Worker `email()` handler

```typescript
export default {
  async email(message, env, ctx) {
    // The raw stream is single-use — buffer it ONCE, then reuse:
    const raw = await new Response(message.raw).arrayBuffer();
    // parse with postal-mime, then forward/reply/store
    await message.forward("team@yourdomain.com"); // destination must be verified
  },
};
```

## Common mistakes

| Mistake | Fix |
|---------|-----|
| No `send_email` binding | Add `"send_email": [{ "name": "EMAIL" }]` — it's a binding, not an API key. |
| Sending from an unverified domain | `wrangler email sending enable yourdomain.com` first. |
| Reading `message.raw` twice | Single-use stream — buffer once (`await new Response(message.raw).arrayBuffer()`). |
| HTML only, no `text` | Always send both `html` and `text`. |
| `email` vs `address` in `from` | Binding: `{ email, name }`. REST: `{ address, name }`. |
| `replyTo` in REST | REST uses `reply_to` (snake_case). |
| Forwarding to an unverified address | `wrangler email routing addresses create user@gmail.com`. |
| Testing with fake addresses | Bounces hurt reputation — use real addresses you control. |
| Hardcoded API token | Env var / secret, never in source. |
| Using it for bulk/marketing | Transactional only — use a marketing platform for campaigns. |

## Deliverability (when in doubt, retrieve)

Authenticate the sending domain (SPF, DKIM, DMARC), keep `text` + `html`, honor bounces and
suppressions. Full guidance: `https://developers.cloudflare.com/email-service/`. Adjacent skills:
`wrangler` (email setup commands), `cloudflare-agents` (agent email handling),
`workers-best-practices`.

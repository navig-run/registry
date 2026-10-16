---
name: web-perf
description: >
  Audits real web-page performance with the Chrome DevTools MCP server — records a load
  trace, reads Core Web Vitals (LCP, INP, CLS) plus FCP/TBT/TTFB/Speed Index, and hunts
  render-blocking resources, late network chains, layout-shift culprits, weak caching, and
  accessibility gaps, then maps fixes back to the codebase. Use when the user says "audit
  the page speed", "why is the deck slow to load", "profile the site", "improve the
  Lighthouse score", "what's hurting LCP/CLS/INP", or "make the landing page faster".
  Requires the `chrome-devtools` MCP server to be configured (the skill checks first and
  stops with the config snippet if it's missing). Prefer live retrieval over memory for
  any specific threshold number. navig surfaces to point it at: the deck (`apps/deck`,
  static export) and the marketing site (www). Read-only measurement — it drives a browser
  and reads the codebase; it never changes files unless you then apply a fix.
category: performance
tags: [performance, web-vitals, lighthouse, chrome-devtools, mcp, accessibility]
safety: safe
---

# Web performance audit (Chrome DevTools MCP)

Measure first, recommend only what the trace proves. This skill drives the **`chrome-devtools`** MCP
server to record a real page load, then reads the numbers and the code behind them. Thresholds and
tooling drift — **prefer live retrieval over memory** for any specific number you cite.

The full tool table, phased workflow, insight names, and threshold table live in
[`references/devtools-mcp.md`](references/devtools-mcp.md). This page is the router and the
house rules.

## Step 0 — verify the MCP server (do this first)

Try calling `navigate_page` or `performance_start_trace`. If they aren't available, **stop** — the
`chrome-devtools` MCP server isn't configured. Ask the user to add it:

```json
"chrome-devtools": { "type": "local", "command": ["npx", "-y", "chrome-devtools-mcp@latest"] }
```

## The audit, in five phases

Track it as a checklist:

```
- [ ] 1. Trace       — navigate + record a cold load (reload: true)
- [ ] 2. Web Vitals  — LCP / INP / CLS breakdowns, CLS culprits
- [ ] 3. Network     — render-blocking, late chains, caching, oversized payloads
- [ ] 4. A11y        — accessibility-tree snapshot, contrast, names, focus
- [ ] 5. Code        — framework/bundler + tree-shaking/compression (skip for third-party sites)
```

Retrieval sources when you need current numbers: web.dev/articles/vitals (vitals thresholds),
developer.chrome.com/docs/devtools/performance (tooling), the Lighthouse scoring page (weights).
See the references file for the per-metric good / needs-improvement / poor bands.

## House rules — be assertive, quantify, prioritize

- **Verify, then state definitively.** Confirm a resource is unused (zero requests to that origin)
  before recommending removal; confirm a claim against the network log or DOM, then say it plainly.
- **Quantify impact.** Use the estimated savings the insight reports. Don't recommend a change with
  0ms impact — note it and move on.
- **Be specific.** "Convert `hero.png` (450 KB) to WebP and set explicit width/height" beats "optimize
  images."
- **Prioritize ruthlessly.** A page at 200ms LCP and 0 CLS is already excellent — say so and stop. Rank
  findings High / Medium / Low by measured effect.
- **Don't weaken the target to score.** No suppressing a real regression, no gaming a metric that
  hides a genuine UX cost.

## navig surfaces

- **The deck (`apps/deck`)** ships as a **static export** on Cloudflare Workers Static Assets, so it
  starts with edge-served static HTML/JS and strong cache headers — LCP is usually dominated by the JS
  bundle and first data call to the daemon, and CLS by late-mounting panels. Audit the exported build,
  not `next dev` (dev has no minification/caching and will lie about prod).
- **The marketing site (www)** is a public, first-impression surface — LCP (hero image/font), CLS
  (web-font swap, un-sized media), and cache headers are the usual wins.

## Output format

1. **Core Web Vitals summary** — a table: metric · value · rating (good / needs-improvement / poor).
2. **Top issues** — prioritized (High/Medium/Low) with the measured impact for each.
3. **Recommendations** — specific, actionable, with the concrete file/config change.
4. **Codebase findings** — framework + bundler detected and the optimization openings (omit if you had
   no codebase access).

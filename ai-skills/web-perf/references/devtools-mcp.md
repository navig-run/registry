# Chrome DevTools MCP — tools, workflow, thresholds

Deep reference for the `web-perf` skill. Tool names and metric bands change across Chrome
versions — treat these as a map, and confirm current numbers via live retrieval
(web.dev/articles/vitals, the Lighthouse scoring page) before quoting them as fact.

## Tool cheat-sheet

| Task | Tool call |
|------|-----------|
| Load a page | `navigate_page(url: "…")` |
| Record a cold load | `performance_start_trace(autoStop: true, reload: true)` |
| Analyze one insight | `performance_analyze_insight(insightSetId: "…", insightName: "…")` |
| List requests | `list_network_requests(resourceTypes: ["Script","Stylesheet","Document","Font","Image"])` |
| One request's detail | `get_network_request(reqid: <id>)` |
| Accessibility tree | `take_snapshot(verbose: true)` |

## Phase 1 — trace

1. `navigate_page(url: "<target>")`.
2. `performance_start_trace(autoStop: true, reload: true)` — `reload: true` captures cold-load metrics.
3. Wait for completion, then read the result. If the trace is empty, re-confirm the page loaded with
   `navigate_page` first. If an insight name doesn't resolve, inspect the trace response for the
   `insightSetId` and the list of available insights (names vary by version).

## Phase 2 — Core Web Vitals

Pull each metric with `performance_analyze_insight`. Common insight names:

| Metric | Insight name | Look for |
|--------|--------------|----------|
| LCP | `LCPBreakdown` | TTFB vs resource-load vs render-delay split |
| CLS | `CLSCulprits` | shift sources: unsized images, injected/late content, font swaps |
| Render blocking | `RenderBlocking` | CSS/JS blocking first paint |
| Document latency | `DocumentLatency` | slow server response |
| Network dep graph | `NetworkRequestsDepGraph` | request chains delaying critical resources |

**Threshold bands (good / needs-improvement / poor) — verify current values before quoting:**

| Metric | Good | Needs improvement | Poor |
|--------|------|-------------------|------|
| TTFB | < 800ms | < 1.8s | > 1.8s |
| FCP | < 1.8s | < 3s | > 3s |
| LCP | < 2.5s | < 4s | > 4s |
| INP | < 200ms | < 500ms | > 500ms |
| TBT | < 200ms | < 600ms | > 600ms |
| CLS | < 0.1 | < 0.25 | > 0.25 |
| Speed Index | < 3.4s | < 5.8s | > 5.8s |

## Phase 3 — network

`list_network_requests(...)`, then look for:

1. **Render-blocking** — JS/CSS in `<head>` without `async`/`defer`/`media`.
2. **Late chains** — resources discovered only after another finishes (CSS `@import`, JS-loaded fonts).
3. **Missing preloads** — critical fonts/hero image/key scripts not preloaded.
4. **Weak caching** — missing/short `Cache-Control`, no `ETag`/`Last-Modified`.
5. **Oversized payloads** — uncompressed or bloated JS/CSS bundles.
6. **Unused preconnect** — if flagged, confirm: zero requests to that origin ⇒ definitively remove; if
   requests exist but loaded late, the preconnect may still help.

## Phase 4 — accessibility

`take_snapshot(verbose: true)`, then flag: missing/duplicate ARIA IDs; contrast below WCAG AA
(4.5:1 normal text, 3:1 large); focus traps or missing focus indicators; interactive elements with no
accessible name.

## Phase 5 — codebase (skip for third-party sites)

Detect the stack and the optimization openings:

- **Framework/bundler** — `next.config.*` (Next), `vite.config.*` (Vite), `webpack.config.*`,
  `rollup.config.*`, `astro.config.*`, `svelte.config.*`; plus `package.json` deps + build scripts.
- **Tree-shaking / dead code** — production mode on; `sideEffects` set; watch for barrel-file re-exports
  and whole-library imports (lodash, moment).
- **Unused JS/CSS** — CSS-in-JS vs extracted CSS; Tailwind `content` globs / PurgeCSS; dynamic vs eager
  imports.
- **Polyfills** — `@babel/preset-env` targets + `useBuiltIns`; oversized `core-js`; overly broad
  `browserslist`.
- **Compression/minification** — terser/esbuild/swc; gzip/brotli at build or edge; production source
  maps external or off.

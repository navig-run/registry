// ==UserScript==
// @name         GitHub full width
// @namespace    https://navig.run/community
// @navig-id     github-full-width
// @version      1.0.0
// @description  Lets code, diffs and pull requests use the whole window instead of a fixed column.
// @author       navig-run
// @homepage     https://github.com/navig-run/registry/tree/main/lenses/github-full-width
// @downloadURL  https://raw.githubusercontent.com/navig-run/registry/main/lenses/github-full-width/lens.user.js
// @match        https://github.com/*
// @run-at       document-start
// @grant        GM_addStyle
// ==/UserScript==

// Widens the page containers GitHub caps at ~1280px. Pages GitHub renders full-width
// already are unchanged; CSS only, so a redesign makes the Lens a no-op, never a break.
GM_addStyle(`
  .container-xl,
  .container-lg,
  .application-main .container-xl,
  .Layout-main .container-lg,
  .repository-content .container-xl,
  div[data-target="react-app.reactRoot"] .container-xl {
    max-width: none !important;
  }
  .pull-request-tab-content .container-xl,
  .js-diff-progressive-container {
    max-width: none !important;
  }
`)

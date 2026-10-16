// ==UserScript==
// @name         YouTube without Shorts
// @namespace    https://navig.run/community
// @navig-id     youtube-hide-shorts
// @version      1.0.0
// @description  Hides Shorts shelves, the Shorts tab and Shorts in search and subscriptions.
// @author       navig-run
// @homepage     https://github.com/navig-run/registry/tree/main/lenses/youtube-hide-shorts
// @downloadURL  https://raw.githubusercontent.com/navig-run/registry/main/lenses/youtube-hide-shorts/lens.user.js
// @match        *://www.youtube.com/*
// @match        *://m.youtube.com/*
// @run-at       document-start
// @grant        GM_addStyle
// ==/UserScript==

// CSS only: the page keeps working even when YouTube renames a component — the rule
// just stops matching. Nothing is clicked, removed from the DOM, or sent anywhere.
GM_addStyle(`
  ytd-reel-shelf-renderer,
  ytd-rich-shelf-renderer[is-shorts],
  ytd-rich-section-renderer:has(ytd-rich-shelf-renderer[is-shorts]),
  grid-shelf-view-model:has(a[href^="/shorts/"]),
  ytd-video-renderer:has(a[href^="/shorts/"]),
  ytd-grid-video-renderer:has(a[href^="/shorts/"]),
  ytd-guide-entry-renderer:has(a[title="Shorts"]),
  ytd-mini-guide-entry-renderer[aria-label="Shorts"],
  yt-tab-shape[tab-title="Shorts"],
  ytm-reel-shelf-renderer,
  ytm-pivot-bar-item-renderer:has(.pivot-shorts) {
    display: none !important;
  }
`)

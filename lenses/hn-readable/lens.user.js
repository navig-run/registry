// ==UserScript==
// @name         Readable Hacker News
// @namespace    https://navig.run/community
// @navig-id     hn-readable
// @version      1.0.0
// @description  Larger text, a comfortable reading width and roomier comment threads on Hacker News.
// @author       navig-run
// @homepage     https://github.com/navig-run/registry/tree/main/lenses/hn-readable
// @downloadURL  https://raw.githubusercontent.com/navig-run/registry/main/lenses/hn-readable/lens.user.js
// @match        https://news.ycombinator.com/*
// @run-at       document-start
// @grant        GM_addStyle
// ==/UserScript==

GM_addStyle(`
  #hnmain {
    width: min(960px, 100%) !important;
  }
  body, td, .title, .comment, .commtext {
    font-size: 15px !important;
    line-height: 1.55 !important;
  }
  .subtext, .subline, .comhead {
    font-size: 12px !important;
  }
  .comment {
    max-width: 72ch;
  }
  td.default {
    padding-bottom: 6px;
  }
`)

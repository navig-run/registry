// ==UserScript==
// @name         Wikipedia reading width
// @namespace    https://navig.run/community
// @navig-id     wikipedia-reading
// @version      1.0.0
// @description  Keeps article text at a comfortable line length with a little more line spacing.
// @author       navig-run
// @homepage     https://github.com/navig-run/registry/tree/main/lenses/wikipedia-reading
// @downloadURL  https://raw.githubusercontent.com/navig-run/registry/main/lenses/wikipedia-reading/lens.user.js
// @match        https://*.wikipedia.org/wiki/*
// @run-at       document-start
// @grant        GM_addStyle
// ==/UserScript==

// Only the article body: navigation, tables and infoboxes keep Wikipedia's own layout.
// Article text sits directly in .mw-parser-output on older pages and inside <section>
// on current ones, so both are covered.
GM_addStyle(`
  #mw-content-text .mw-parser-output > p,
  #mw-content-text .mw-parser-output > ul,
  #mw-content-text .mw-parser-output > ol,
  #mw-content-text .mw-parser-output > blockquote,
  #mw-content-text .mw-parser-output > section > p,
  #mw-content-text .mw-parser-output > section > ul,
  #mw-content-text .mw-parser-output > section > ol,
  #mw-content-text .mw-parser-output > section > blockquote {
    max-width: 75ch;
    line-height: 1.7;
  }
`)

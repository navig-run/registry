// ==UserScript==
// @name         Starter Userscript
// @namespace    https://github.com/your-username/userscripts
// @version      1.0.0
// @description  Replace this with what your script does in one sentence.
// @author       Your Name
// @match        https://example.com/*
// @match        https://www.example.com/*
// @exclude      https://example.com/excluded-path/*
// @grant        GM_getValue
// @grant        GM_setValue
// @grant        GM_addStyle
// @run-at       document-end
// @noframes
// ==/UserScript==

(function () {
  'use strict';

  // ─────────────────────────────────────────────
  // CONFIG — Edit these values to customise behaviour
  // ─────────────────────────────────────────────
  const CONFIG = {
    enabled: GM_getValue('enabled', true), // persist on/off state across sessions
    highlightColor: '#ffeb3b',              // yellow — change to any CSS color
    debug: false,                           // set true to log verbose output
  };

  // ─────────────────────────────────────────────
  // STYLES — Injected CSS (GM_addStyle required in @grant)
  // ─────────────────────────────────────────────
  GM_addStyle(`
    .my-script-highlight {
      background-color: ${CONFIG.highlightColor} !important;
      outline: 2px solid orange !important;
    }
    .my-script-badge {
      font-size: 11px;
      padding: 2px 6px;
      background: #333;
      color: #fff;
      border-radius: 3px;
      margin-left: 4px;
    }
  `);

  // ─────────────────────────────────────────────
  // UTILITIES
  // ─────────────────────────────────────────────

  /**
   * Log to console only when debug mode is on.
   * @param {...any} args
   */
  function log(...args) {
    if (CONFIG.debug) console.log('[StarterScript]', ...args);
  }

  /**
   * Wait for a DOM element matching `selector` to appear.
   * Resolves once found; rejects after `timeout` ms.
   * @param {string} selector
   * @param {number} [timeout=5000]
   * @returns {Promise<Element>}
   */
  function waitForElement(selector, timeout = 5000) {
    return new Promise((resolve, reject) => {
      const el = document.querySelector(selector);
      if (el) return resolve(el);

      const observer = new MutationObserver(() => {
        const found = document.querySelector(selector);
        if (found) {
          observer.disconnect();
          resolve(found);
        }
      });

      observer.observe(document.body, { childList: true, subtree: true });
      setTimeout(() => {
        observer.disconnect();
        reject(new Error(`Timeout waiting for: ${selector}`));
      }, timeout);
    });
  }

  // ─────────────────────────────────────────────
  // MAIN LOGIC
  // Replace the body of init() with your actual script logic.
  // ─────────────────────────────────────────────

  async function init() {
    if (!CONFIG.enabled) {
      log('Script disabled via GM_getValue — exiting.');
      return;
    }

    log('Script running on', window.location.href);

    try {
      // Example: wait for a heading and highlight it
      const heading = await waitForElement('h1');
      heading.classList.add('my-script-highlight');

      const badge = document.createElement('span');
      badge.className = 'my-script-badge';
      badge.textContent = '✓ script active';
      heading.appendChild(badge);

      log('Applied highlight to', heading.textContent.trim());
    } catch (err) {
      console.error('[StarterScript] Error:', err.message);
    }
  }

  // ─────────────────────────────────────────────
  // ENTRY POINT
  // DOMContentLoaded already fired when @run-at is document-end.
  // If you need document-start, remove the readyState check.
  // ─────────────────────────────────────────────
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();

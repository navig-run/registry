// content.js — Injected into pages matching manifest.json content_scripts.matches
// This runs in the context of the web page (not the extension).
// DOM APIs are available. chrome.* APIs are limited to those that work in content scripts.

(function () {
  'use strict';

  // Prevent double-injection if the script is somehow loaded twice
  if (window.__starterExtensionLoaded) return;
  window.__starterExtensionLoaded = true;

  console.log('[Content] Starter Extension content script active on', window.location.href);

  // ─────────────────────────────────────────────
  // COMMUNICATE WITH BACKGROUND
  // Send a message to background.js and handle the response.
  // ─────────────────────────────────────────────
  chrome.runtime.sendMessage({ action: 'getStatus' }, (response) => {
    if (chrome.runtime.lastError) {
      // Background service worker may not yet be running — this is normal on first load.
      console.warn('[Content] Could not reach background:', chrome.runtime.lastError.message);
      return;
    }
    console.log('[Content] Status from background:', response);

    if (response?.enabled) {
      init();
    } else {
      console.log('[Content] Extension disabled — skipping init.');
    }
  });

  // ─────────────────────────────────────────────
  // LISTEN FOR MESSAGES FROM BACKGROUND OR POPUP
  // ─────────────────────────────────────────────
  chrome.runtime.onMessage.addListener((message, _sender, sendResponse) => {
    if (message.action === 'pageDone') {
      console.log('[Content] Received pageDone signal from background.');
      sendResponse({ status: 'acknowledged' });
    }
  });

  // ─────────────────────────────────────────────
  // MAIN LOGIC — Replace with your implementation
  // ─────────────────────────────────────────────
  function init() {
    console.log('[Content] Initialising features on page...');

    // Example: highlight the first heading on the page
    const h1 = document.querySelector('h1');
    if (h1) {
      h1.style.outline = '3px solid #4285f4';
      h1.title = 'Highlighted by Starter Extension';
    }
  }

})();

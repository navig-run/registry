// background.js — MV3 Service Worker
// This file runs as a service worker: it is NOT persistent.
// It wakes up on Chrome events and terminates after ~30s of inactivity.
// DO NOT store state in module-level variables between events — use chrome.storage.

// ─────────────────────────────────────────────
// INSTALL / UPDATE
// Runs once when the extension is first installed or updated.
// ─────────────────────────────────────────────
chrome.runtime.onInstalled.addListener((details) => {
  console.log('[Background] onInstalled:', details.reason);

  if (details.reason === 'install') {
    // First-time setup: set default storage values
    chrome.storage.local.set({ enabled: true, installDate: Date.now() });
    console.log('[Background] First install — defaults written to storage.');
  }

  if (details.reason === 'update') {
    console.log('[Background] Updated from version', details.previousVersion);
  }
});

// ─────────────────────────────────────────────
// MESSAGE LISTENER
// Receives messages from content.js or popup.js via chrome.runtime.sendMessage.
// ─────────────────────────────────────────────
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  console.log('[Background] Message received:', message, 'from tab:', sender.tab?.id);

  // Always return true if you intend to respond asynchronously.
  if (message.action === 'getStatus') {
    chrome.storage.local.get('enabled', (data) => {
      sendResponse({ status: 'ok', enabled: data.enabled });
    });
    return true; // keeps the channel open for the async response
  }

  if (message.action === 'toggle') {
    chrome.storage.local.get('enabled', (data) => {
      const newValue = !data.enabled;
      chrome.storage.local.set({ enabled: newValue }, () => {
        sendResponse({ enabled: newValue });
      });
    });
    return true;
  }

  // Unhandled message — respond with an error so the sender doesn't hang
  sendResponse({ error: 'Unknown action: ' + message.action });
});

// ─────────────────────────────────────────────
// TAB EVENTS (optional — remove if not needed)
// ─────────────────────────────────────────────
chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
  if (changeInfo.status === 'complete' && tab.url?.startsWith('https://example.com')) {
    console.log('[Background] Target page loaded in tab', tabId);
    // Example: send a message to the content script in this tab
    // chrome.tabs.sendMessage(tabId, { action: 'pageDone' });
  }
});

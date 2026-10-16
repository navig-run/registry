// popup.js — Runs in the popup context (separate from content and background).
// Can use chrome.runtime.sendMessage to talk to background.js.
// Cannot directly access page DOM — use content.js for that.

document.addEventListener('DOMContentLoaded', () => {
  const statusBadge = document.getElementById('status-badge');
  const toggleBtn   = document.getElementById('toggle-btn');
  const message     = document.getElementById('message');

  // ─────────────────────────────────────────────
  // LOAD INITIAL STATE from background
  // ─────────────────────────────────────────────
  chrome.runtime.sendMessage({ action: 'getStatus' }, (response) => {
    if (chrome.runtime.lastError) {
      setStatus(false, 'Could not reach background: ' + chrome.runtime.lastError.message);
      return;
    }
    setStatus(response.enabled);
    toggleBtn.disabled = false;
  });

  // ─────────────────────────────────────────────
  // TOGGLE BUTTON
  // ─────────────────────────────────────────────
  toggleBtn.addEventListener('click', () => {
    toggleBtn.disabled = true;
    message.textContent = '';

    chrome.runtime.sendMessage({ action: 'toggle' }, (response) => {
      if (chrome.runtime.lastError) {
        message.textContent = 'Error: ' + chrome.runtime.lastError.message;
        toggleBtn.disabled = false;
        return;
      }
      setStatus(response.enabled, response.enabled ? 'Enabled.' : 'Disabled.');
      toggleBtn.disabled = false;
    });
  });

  // ─────────────────────────────────────────────
  // HELPERS
  // ─────────────────────────────────────────────

  /**
   * Update badge and optional message text.
   * @param {boolean} enabled
   * @param {string} [msg]
   */
  function setStatus(enabled, msg = '') {
    statusBadge.textContent = enabled ? 'Active' : 'Disabled';
    statusBadge.className = 'badge ' + (enabled ? 'badge--active' : 'badge--inactive');
    if (msg) message.textContent = msg;
  }
});

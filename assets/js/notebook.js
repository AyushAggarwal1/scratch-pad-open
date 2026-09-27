/* Progressive enhancements. All document links work without JavaScript. */
(function () {
  'use strict';

  var lightCSS = 'just-the-docs-default.css';
  var darkCSS = 'just-the-docs-scratchpad-dark.css';
  var themeLink = document.querySelector('link[href*="' + lightCSS + '"], link[href*="' + darkCSS + '"]');
  var preference = window.matchMedia('(prefers-color-scheme: dark)');

  function savedTheme() {
    try { return localStorage.getItem('osn-scheme'); } catch (error) { return null; }
  }

  function isDark() {
    return themeLink && themeLink.href.indexOf(darkCSS) !== -1;
  }

  function refreshThemeButtons() {
    document.querySelectorAll('.js-scheme-toggle').forEach(function (button) {
      button.classList.toggle('is-dark', isDark());
      button.setAttribute('aria-pressed', String(Boolean(isDark())));
      button.setAttribute('aria-label', 'Switch to ' + (isDark() ? 'light' : 'dark') + ' mode');
    });
  }

  function setTheme(mode, persist) {
    if (!themeLink) return;
    themeLink.href = themeLink.href.replace(isDark() ? darkCSS : lightCSS, mode === 'dark' ? darkCSS : lightCSS);
    document.querySelector('meta[name="theme-color"]').content = mode === 'dark' ? '#181a19' : '#faf9f6';
    if (persist) {
      try { localStorage.setItem('osn-scheme', mode); } catch (error) { /* Private storage is optional. */ }
    }
    refreshThemeButtons();
  }

  document.querySelectorAll('.js-scheme-toggle').forEach(function (button) {
    button.addEventListener('click', function () { setTheme(isDark() ? 'light' : 'dark', true); });
  });
  refreshThemeButtons();
  preference.addEventListener('change', function (event) {
    if (!savedTheme()) setTheme(event.matches ? 'dark' : 'light', false);
  });
  window.addEventListener('storage', function (event) {
    if (event.key === 'osn-scheme' || event.key === null) {
      setTheme(savedTheme() || (preference.matches ? 'dark' : 'light'), false);
    }
  });

  var searchWrap = document.querySelector('.search-input-wrap');
  if (searchWrap) searchWrap.dataset.shortcut = /Mac|iPhone|iPad/.test(navigator.platform) ? '⌘ K' : 'Ctrl K';
  // The pinned theme listens for keyup; input also covers paste and mobile keyboards.
  var searchInput = document.getElementById('search-input');
  if (searchInput) searchInput.addEventListener('input', function () {
    searchInput.dispatchEvent(new Event('keyup', { bubbles: true }));
  });

  var library = document.querySelector('[data-topic-library]');
  if (!library) return;

  var cards = Array.from(library.querySelectorAll('[data-topic-card]'));
  var queryInput = library.querySelector('[data-topic-query]');
  var buttons = Array.from(library.querySelectorAll('[data-filter]'));
  var category = 'all';
  var searchText = cards.map(function (card) { return card.textContent.toLowerCase(); });

  function filterTopics() {
    var terms = queryInput.value.trim().toLowerCase().split(/\s+/).filter(Boolean);
    var visible = 0;
    cards.forEach(function (card, index) {
      var matches = (category === 'all' || card.dataset.category === category) && terms.every(function (term) {
        return searchText[index].indexOf(term) !== -1;
      });
      card.hidden = !matches;
      if (matches) visible += 1;
    });
    buttons.forEach(function (button) {
      var active = button.dataset.filter === category;
      button.classList.toggle('is-active', active);
      button.setAttribute('aria-pressed', String(active));
    });
    library.querySelector('[data-topic-count]').textContent = visible + ' of ' + cards.length + ' topics';
    library.querySelector('[data-topic-empty]').hidden = visible !== 0;
  }

  buttons.forEach(function (button) {
    button.addEventListener('click', function () { category = button.dataset.filter; filterTopics(); });
  });
  queryInput.addEventListener('input', filterTopics);
  library.querySelector('[data-filter-reset]').addEventListener('click', function () {
    queryInput.value = '';
    category = 'all';
    filterTopics();
    queryInput.focus();
  });
  library.querySelector('[data-library-controls]').hidden = false;
  filterTopics();
})();

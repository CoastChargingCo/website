(function () {
  var FADE = 0.35;

  function ensurePlay(video) {
    video.muted = true;
    video.setAttribute('muted', '');
    video.setAttribute('playsinline', '');
    var attempt = video.play();
    if (attempt && typeof attempt.catch === 'function') {
      attempt.catch(function () {});
    }
  }

  function bind(video) {
    if (!video || video.dataset.loopFadeBound) return;
    video.dataset.loopFadeBound = '1';
    video.style.opacity = '1';

    ensurePlay(video);

    video.addEventListener('loadeddata', function () {
      ensurePlay(video);
    });

    video.addEventListener('timeupdate', function () {
      if (video.paused || video.readyState < 2) {
        video.style.opacity = '1';
        return;
      }

      var duration = video.duration;
      if (!duration || !isFinite(duration) || duration < FADE * 2) {
        video.style.opacity = '1';
        return;
      }

      var time = video.currentTime;
      var opacity = 1;

      // Fade only near the loop seam to soften the cut, not at every start.
      if (duration - time < FADE) {
        opacity = Math.max(0.72, (duration - time) / FADE);
      }

      video.style.opacity = String(opacity);
    });
  }

  function bindAll() {
    document.querySelectorAll('video[data-loop-fade]').forEach(bind);
  }

  function init() {
    bindAll();

    // dc-runtime mounts the page with React after DOMContentLoaded.
    var observer = new MutationObserver(function () {
      bindAll();
    });
    observer.observe(document.documentElement, { childList: true, subtree: true });

    window.addEventListener('load', bindAll);
    setTimeout(bindAll, 250);
    setTimeout(bindAll, 1000);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();

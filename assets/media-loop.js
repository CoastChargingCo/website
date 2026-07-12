(function () {
  var FADE = 0.45;

  function bind(video) {
    if (!video || video.dataset.loopFadeBound) return;
    video.dataset.loopFadeBound = '1';
    video.muted = true;

    video.addEventListener('timeupdate', function () {
      var duration = video.duration;
      if (!duration || !isFinite(duration) || duration < FADE * 2) return;

      var time = video.currentTime;
      var opacity = 1;

      if (time < FADE) {
        opacity = time / FADE;
      } else if (duration - time < FADE) {
        opacity = (duration - time) / FADE;
      }

      video.style.opacity = String(opacity);
    });
  }

  function init() {
    document.querySelectorAll('video[data-loop-fade]').forEach(bind);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();

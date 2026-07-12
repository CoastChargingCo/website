(function () {
  function bind(video) {
    if (!video || video.dataset.loopBound) return;
    video.dataset.loopBound = '1';

    video.muted = true;
    video.setAttribute('muted', '');
    video.setAttribute('playsinline', '');
    video.loop = true;
    video.style.opacity = '1';

    function play() {
      var attempt = video.play();
      if (attempt && typeof attempt.catch === 'function') {
        attempt.catch(function () {});
      }
    }

    play();

    video.addEventListener('loadeddata', play);

    video.addEventListener('ended', function () {
      video.currentTime = 0;
      play();
    });
  }

  function bindAll() {
    document.querySelectorAll('video[data-loop-fade]').forEach(bind);
  }

  function init() {
    bindAll();

    var observer = new MutationObserver(bindAll);
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

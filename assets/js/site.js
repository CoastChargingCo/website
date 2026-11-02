// Coast Charging Co · small page helpers. The page works without this file;
// it only adds the phone menu toggle and keeps the community video looping.
(function () {
  // Phone menu
  var nav = document.querySelector('.site-nav');
  var toggle = nav && nav.querySelector('.site-nav__toggle');
  if (nav && toggle) {
    function setOpen(open) {
      nav.classList.toggle('is-open', open);
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    }
    toggle.addEventListener('click', function () {
      setOpen(!nav.classList.contains('is-open'));
    });
    nav.querySelectorAll('.site-nav__links a').forEach(function (link) {
      link.addEventListener('click', function () { setOpen(false); });
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('is-open')) { setOpen(false); toggle.focus(); }
    });
  }

  // Community video: muted autoplay loop, paused for people who prefer reduced motion
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.querySelectorAll('video[data-loop]').forEach(function (video) {
    video.muted = true;
    if (reduce) { video.removeAttribute('autoplay'); video.pause(); return; }
    var p = video.play();
    if (p && p.catch) p.catch(function () {});
  });
})();

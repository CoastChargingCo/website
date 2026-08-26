(function () {
  var checkbox = document.getElementById("site-nav-open");
  if (!checkbox) return;
  document.querySelectorAll(".site-nav-actions a").forEach(function (link) {
    link.addEventListener("click", function () {
      checkbox.checked = false;
    });
  });
})();

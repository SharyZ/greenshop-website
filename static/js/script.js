(function () {
  const menuBtn = document.getElementById('menu-btn');
  const menu = document.getElementById('menu');

  menuBtn.addEventListener('click', function (e) {
    menu.classList.toggle('hidden');
  });
})();

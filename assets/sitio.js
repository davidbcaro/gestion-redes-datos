/* Buscador del sitio. Funciona con el indice embebido en cada pagina
   (window.INDICE) y tambien filtra tarjetas de la pagina actual. */
(function () {
  'use strict';

  function normalizar(texto) {
    return (texto || '')
      .toLowerCase()
      .normalize('NFD')
      .replace(/[\u0300-\u036f]/g, '');
  }

  /* Buscador global: lista resultados de todo el programa. */
  var campo = document.getElementById('buscador-global');
  var lista = document.getElementById('resultados');

  if (campo && lista && window.INDICE) {
    var items = window.INDICE.map(function (i) {
      return { dato: i, clave: normalizar(i.t + ' ' + i.d) };
    });

    var pintar = function () {
      var q = normalizar(campo.value.trim());
      lista.innerHTML = '';
      if (q.length < 2) return;

      var hallados = items.filter(function (i) { return i.clave.indexOf(q) !== -1; }).slice(0, 12);

      if (!hallados.length) {
        lista.innerHTML = '<li class="vacio">Sin resultados para &laquo;' +
          campo.value.replace(/[<>&]/g, '') + '&raquo;</li>';
        return;
      }

      hallados.forEach(function (i) {
        var li = document.createElement('li');
        var a = document.createElement('a');
        a.href = i.dato.u;
        if (i.dato.n) { a.target = '_blank'; a.rel = 'noopener'; }
        a.innerHTML = '<span class="etiqueta-tipo">' + i.dato.k + '</span>' +
          '<span class="que"></span><span class="donde"></span>';
        a.querySelector('.que').textContent = i.dato.t;
        a.querySelector('.donde').textContent = i.dato.d;
        li.appendChild(a);
        lista.appendChild(li);
      });
    };

    campo.addEventListener('input', pintar);
    campo.addEventListener('search', pintar);
    document.addEventListener('keydown', function (ev) {
      if (ev.key === 'Escape' && document.activeElement === campo) {
        campo.value = '';
        pintar();
        campo.blur();
      }
    });
  }

  /* Filtro dentro de una pagina de fase: oculta tarjetas que no coinciden. */
  var filtro = document.getElementById('filtro');
  if (filtro) {
    var tarjetas = [].slice.call(document.querySelectorAll('[data-buscable]'));
    var bloques = [].slice.call(document.querySelectorAll('[data-bloque]'));

    filtro.addEventListener('input', function () {
      var q = normalizar(filtro.value.trim());
      tarjetas.forEach(function (t) {
        var coincide = !q || normalizar(t.getAttribute('data-buscable')).indexOf(q) !== -1;
        t.classList.toggle('oculto', !coincide);
      });
      bloques.forEach(function (b) {
        var visibles = b.querySelectorAll('[data-buscable]:not(.oculto)').length;
        b.classList.toggle('oculto', visibles === 0);
      });
    });
  }
})();

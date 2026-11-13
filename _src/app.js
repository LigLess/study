(function(){
  var $ = function(s, r){ return (r||document).querySelector(s); };
  var $$ = function(s, r){ return Array.prototype.slice.call((r||document).querySelectorAll(s)); };
  var body = document.body;

  /* ---- reveal on scroll ---- */
  var revs = $$('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function(es){
      es.forEach(function(e){ if (e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } });
    }, {rootMargin:'0px 0px -8% 0px'});
    revs.forEach(function(el){ io.observe(el); });
  } else revs.forEach(function(el){ el.classList.add('in'); });

  /* ---- progress bar + toc spy ---- */
  var bar = $('.progress i');
  var chs = $$('.chapter');
  var subs = $$('.ch-body h3[id]');
  var tocCh = {}; $$('.toc-ch').forEach(function(a){ tocCh[a.dataset.ch] = a; });
  var tocSub = {}; $$('.toc ol a').forEach(function(a){ tocSub[a.getAttribute('href').slice(1)] = a; });
  var curCh = null, curSub = null, ticking = false;
  function spy(){
    ticking = false;
    var h = document.documentElement, max = h.scrollHeight - innerHeight;
    if (bar) bar.style.transform = 'scaleX(' + (max > 0 ? Math.min(1, scrollY / max) : 0) + ')';
    var line = 140, c = null, s = null;
    for (var i = 0; i < chs.length; i++) { if (chs[i].getBoundingClientRect().top - line < 0) c = chs[i]; else break; }
    for (var j = 0; j < subs.length; j++) { if (subs[j].getBoundingClientRect().top - line < 0) s = subs[j]; else break; }
    if (c !== curCh) {
      if (curCh && tocCh[curCh.id]) { tocCh[curCh.id].classList.remove('on'); tocCh[curCh.id].parentNode.classList.remove('open'); }
      curCh = c;
      if (c && tocCh[c.id]) { tocCh[c.id].classList.add('on'); tocCh[c.id].parentNode.classList.add('open'); }
    }
    if (s !== curSub) {
      if (curSub && tocSub[curSub.id]) tocSub[curSub.id].classList.remove('on');
      curSub = s;
      if (s && tocSub[s.id] && c && c.contains(s)) tocSub[s.id].classList.add('on');
    }
  }
  addEventListener('scroll', function(){ if (!ticking){ ticking = true; requestAnimationFrame(spy); } }, {passive:true});
  spy();

  /* ---- mobile toc ---- */
  var tg = $('.toc-toggle');
  if (tg) tg.addEventListener('click', function(){
    var open = body.classList.toggle('toc-open'); tg.setAttribute('aria-expanded', open);
  });
  $$('.toc a').forEach(function(a){ a.addEventListener('click', function(){ body.classList.remove('toc-open'); if (tg) tg.setAttribute('aria-expanded', false); }); });

  /* ---- quiz ---- */
  document.addEventListener('click', function(e){
    var b = e.target.closest && e.target.closest('.opt');
    if (!b) return;
    var q = b.closest('.q'); if (q.classList.contains('done')) return;
    var ans = +q.dataset.ans, pick = +b.dataset.i;
    q.classList.add('done');
    $$('.opt', q).forEach(function(o){ if (+o.dataset.i === ans) o.classList.add('right'); });
    if (pick !== ans) b.classList.add('wrong');
  });
  $$('.q').forEach(function(q){
    var t = document.createElement('button'); t.type = 'button'; t.className = 'ans-toggle'; t.textContent = '정답만 보기';
    t.addEventListener('click', function(){
      q.classList.add('done'); $$('.opt', q).forEach(function(o){ if (+o.dataset.i === +q.dataset.ans) o.classList.add('right'); });
      t.remove();
    });
    q.appendChild(t);
  });

  /* ---- PDF (print) ---- */
  var modal = $('#pdfModal'), lastFocus = null;
  function openModal(){ lastFocus = document.activeElement; modal.hidden = false; $('#doPrint').focus(); }
  function closeModal(){ modal.hidden = true; if (lastFocus) lastFocus.focus(); }
  $$('.open-pdf').forEach(function(b){ b.addEventListener('click', openModal); });
  $$('[data-close]', modal).forEach(function(b){ b.addEventListener('click', closeModal); });
  addEventListener('keydown', function(e){ if (e.key === 'Escape' && !modal.hidden) closeModal(); });
  $$('[data-all]', modal).forEach(function(b){ b.addEventListener('click', function(){
    var v = b.dataset.all === '1'; $$('.pick input', modal).forEach(function(i){ i.checked = v; });
  }); });

  var cover = $('.pc-list');
  function fillCover(ids){
    cover.innerHTML = '';
    chs.forEach(function(c){
      if (ids && ids.indexOf(c.id) < 0) return;
      var li = document.createElement('li'), g = c.dataset.group;
      li.innerHTML = (g ? '<span>' + g + '</span>' : '') + c.dataset.title;
      cover.appendChild(li);
    });
  }
  function printChapters(ids, withAns){
    if (!ids.length) { alert('저장할 단원을 하나 이상 고르세요.'); return; }
    var all = ids.length === chs.length;
    chs.forEach(function(c){ c.classList.toggle('pr', ids.indexOf(c.id) > -1); });
    body.classList.toggle('pick-mode', !all);
    body.classList.toggle('no-ans', !withAns);
    fillCover(ids);
    revs.forEach(function(el){ el.classList.add('in'); });
    var t = document.title;
    if (!all && ids.length === 1) document.title = t.replace(' 교본', '') + ' - ' + $('#' + ids[0]).dataset.title;
    modal.hidden = true;
    setTimeout(function(){
      window.print();
      setTimeout(function(){ document.title = t; }, 500);
    }, 60);
  }
  $('#doPrint').addEventListener('click', function(){
    var ids = $$('.pick input:checked', modal).map(function(i){ return i.value; });
    printChapters(ids, $('#optAns').checked);
  });
  $$('.ch-pdf').forEach(function(b){ b.addEventListener('click', function(){ printChapters([b.dataset.ch], true); }); });
  addEventListener('afterprint', function(){
    body.classList.remove('pick-mode', 'no-ans'); chs.forEach(function(c){ c.classList.remove('pr'); });
    fillCover(null);
  });
  addEventListener('beforeprint', function(){ revs.forEach(function(el){ el.classList.add('in'); }); });
  /* 브라우저 메뉴(Ctrl+P)로 바로 인쇄해도 표지 목록이 채워지도록 */
  fillCover(null);

  /* figures: run once when visible */
  window.__onSeen = function(el, fn){
    if (!el) return;
    if (!('IntersectionObserver' in window)) { fn(); return; }
    var o = new IntersectionObserver(function(es){ es.forEach(function(e){ if (e.isIntersecting){ o.disconnect(); fn(); } }); }, {threshold:.35});
    o.observe(el);
  };
})();

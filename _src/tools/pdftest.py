import sys, pathlib
from playwright.sync_api import sync_playwright
src = pathlib.Path(sys.argv[1]).resolve(); out = pathlib.Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
chs = sys.argv[3].split(",") if len(sys.argv) > 3 else None
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width":1280,"height":900})
    pg.goto(src.as_uri()); pg.wait_for_timeout(1200)
    if chs:
        pg.evaluate("""ids => { const chs=[...document.querySelectorAll('.chapter')];
          chs.forEach(c=>c.classList.toggle('pr', ids.includes(c.id)));
          document.body.classList.add('pick-mode');
          const cov=document.querySelector('.pc-list'); cov.innerHTML='';
          chs.filter(c=>ids.includes(c.id)).forEach(c=>{const li=document.createElement('li'); li.innerHTML='<span>'+c.dataset.group+'</span>'+c.dataset.title; cov.appendChild(li);});
          document.querySelectorAll('.reveal').forEach(e=>e.classList.add('in')); }""", chs)
    else:
        pg.evaluate("document.querySelectorAll('.reveal').forEach(e=>e.classList.add('in'))")
    pg.emulate_media(media="print")
    name = (sys.argv[3].replace(",", "_") if chs else "full")
    pg.pdf(path=str(out / f"{name}.pdf"), prefer_css_page_size=True, print_background=True)
    b.close()
print("done")

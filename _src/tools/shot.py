import sys, pathlib
from playwright.sync_api import sync_playwright
src = pathlib.Path(sys.argv[1]).resolve(); out = pathlib.Path(sys.argv[2]); out.mkdir(exist_ok=True, parents=True)
targets = sys.argv[3:] if len(sys.argv) > 3 else []
with sync_playwright() as p:
    b = p.chromium.launch()
    for w, h, name in [(1440, 900, "pc"), (390, 844, "mo")]:
        pg = b.new_page(viewport={"width": w, "height": h}); errs = []
        pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
        pg.goto(src.as_uri()); pg.wait_for_timeout(3200)
        pg.screenshot(path=str(out / f"{name}_top.png"))
        for t in targets:
            pg.evaluate(f"document.querySelector('{t}').scrollIntoView({{block:'start'}})"); pg.wait_for_timeout(2600)
            pg.screenshot(path=str(out / f"{name}_{t.strip('#.').replace(' ','_')}.png"))
        print(name, "errors:", errs[:5])
        pg.close()
    b.close()

#!/usr/bin/env python3
"""교본 빌드: content/*.md + figs.py -> dist/*.html"""
import re, html, pathlib, datetime
import markdown
from figs import FIGS, FIG_JS, FIG_CSS, hero_term

ROOT = pathlib.Path(__file__).parent
DIST = ROOT / "dist"
DIST.mkdir(exist_ok=True)

from guides import GUIDES, GROUPS

CIRCLE = "①②③④⑤"

def inline(md_text):
    out = markdown.markdown(md_text, extensions=["tables", "fenced_code"])
    if out.startswith("<p>") and out.endswith("</p>") and out.count("<p>") == 1:
        out = out[3:-4]
    return out

def render_quiz(lines):
    """Q. 질문 / 1) 보기 / > 정답 2 | 해설"""
    qs, cur = [], None
    for ln in lines:
        if ln.startswith("Q."):
            if cur: qs.append(cur)
            cur = {"q": [ln[2:].strip()], "opts": [], "ans": None, "exp": ""}
        elif cur is None:
            continue
        elif re.match(r"^[1-5]\) ", ln):
            cur["opts"].append(ln[3:].strip())
        elif ln.startswith("> 정답"):
            m = re.match(r"> 정답\s*([1-5])\s*\|\s*(.*)", ln)
            cur["ans"], cur["exp"] = int(m.group(1)), m.group(2).strip()
        elif cur["opts"] and cur["ans"] is not None:
            cur["exp"] += "\n" + ln
        elif not cur["opts"]:
            cur["q"].append(ln)
    if cur: qs.append(cur)
    h = ['<ol class="quiz">']
    for q in qs:
        assert q["ans"], q
        h.append('<li class="q" data-ans="%d"><div class="q-text">%s</div><ol class="opts">' %
                 (q["ans"], markdown.markdown("\n".join(q["q"]), extensions=["fenced_code", "tables"])))
        for i, o in enumerate(q["opts"], 1):
            h.append('<li><button type="button" class="opt" data-i="%d"><span class="n">%s</span><span>%s</span></button></li>' %
                     (i, CIRCLE[i-1], inline(o)))
        h.append('</ol><div class="ans"><p><b>정답 %s</b> %s</p></div></li>' %
                 (CIRCLE[q["ans"]-1], inline(q["exp"].strip())))
    h.append('</ol>')
    return "\n".join(h)

BOX_NAMES = {"tip": "핵심 정리", "exam": "시험 포인트", "warn": "헷갈리기 쉬운 것", "ex": "예시"}

def preprocess(body):
    out, i, L = [], 0, body.split("\n")
    while i < len(L):
        ln = L[i]
        m = re.match(r"^:::(\w+)\s*(.*)$", ln)
        if m and m.group(1) != "":
            kind, arg = m.group(1), m.group(2).strip()
            if kind == "fig":
                out.append('\n<div data-fig="%s"></div>\n' % arg)
                i += 1; continue
            block = []; i += 1
            while i < len(L) and L[i].strip() != ":::":
                block.append(L[i]); i += 1
            i += 1
            if kind == "quiz":
                out.append("\n" + render_quiz(block) + "\n")
            else:
                title = arg or BOX_NAMES.get(kind, "")
                out.append('\n<aside class="box box-%s" markdown="1">\n<p class="box-t">%s</p>\n\n%s\n\n</aside>\n' %
                           (kind, html.escape(title), "\n".join(block)))
            continue
        out.append(ln); i += 1
    return "\n".join(out)

def slugify(t, n):
    return "s%d" % n

def build(g):
    src = (ROOT / "content" / g["file"]).read_text(encoding="utf-8")
    def inc(m):
        return (ROOT / "content" / "shared" / (m.group(1) + ".md")).read_text(encoding="utf-8")
    for _ in range(3):
        src = re.sub(r"^@@include (\S+)\s*$", inc, src, flags=re.M)
    # chapters split by '# '
    parts = re.split(r"^# ([^\n]+ \| [^\n]+)$", src, flags=re.M)
    chapters = []
    for k in range(1, len(parts), 2):
        head, body = parts[k].strip(), parts[k+1]
        group, _, title = head.partition(" | ")
        if not title: title, group = group, ""
        chapters.append((group.strip(), title.strip(), body))
    toc, secs, sec_n = [], [], 0
    for ci, (group, title, body) in enumerate(chapters):
        cid = "ch%d" % ci
        md = markdown.Markdown(extensions=["tables", "fenced_code", "md_in_html", "attr_list", "sane_lists"])
        body_html = md.convert(preprocess(body))
        # figures
        def fig_sub(m):
            key = m.group(1)
            return FIGS[key]
        body_html = re.sub(r'<div data-fig="([\w-]+)"></div>', fig_sub, body_html)
        body_html = body_html.replace("\\|", "|")
        # 표 감싸기: 짧은 표는 페이지 경계에서 통째로 넘김
        def tbl_sub(m):
            t = m.group(0)
            keep = " keep" if t.count("<tr") <= 14 else ""
            return f'<div class="tw{keep}">{t}</div>'
        body_html = re.sub(r"<table>.*?</table>", tbl_sub, body_html, flags=re.S)
        # 소제목(h4)과 바로 뒤 블록을 한 덩어리로 묶어 제목만 페이지 끝에 남는 것 방지
        body_html = re.sub(r"(<h4>.*?</h4>)\s*(<p>.*?</p>)", r'<div class="keep">\1\n\2</div>', body_html, flags=re.S)
        # h2 ids for toc
        subs = []
        def h2_sub(m):
            nonlocal sec_n
            sec_n += 1
            sid = "s%d" % sec_n
            subs.append((sid, re.sub("<[^>]+>", "", m.group(1))))
            return '<h3 id="%s">%s</h3>' % (sid, m.group(1))
        # markdown '##' -> h3 visually (h2 is chapter), '###' -> h4
        body_html = re.sub(r"<h3>(.*?)</h3>", r"<h4>\1</h4>", body_html)
        body_html = re.sub(r"<h2>(.*?)</h2>", h2_sub, body_html)
        toc.append((cid, group, title, subs))
        secs.append(f'''
<section class="chapter" id="{cid}" data-title="{html.escape(title)}" data-group="{html.escape(group)}">
  <header class="ch-head reveal">
    <p class="ch-group">{html.escape(group)}</p>
    <h2>{html.escape(title)}</h2>
    <button type="button" class="ch-pdf" data-ch="{cid}"><svg viewBox="0 0 16 16" aria-hidden="true"><path d="M4 1.5h5.5L12.5 4.5V14.5h-8.5z M9.5 1.5v3h3 M6 9.5l2 2 2-2 M8 6.5v5"/></svg>이 장만 PDF로</button>
  </header>
  <div class="ch-body">
{body_html}
  </div>
</section>''')
    # TOC html
    t = []
    last_group = None
    for cid, group, title, subs in toc:
        if group != last_group and group:
            pass
        t.append(f'<li><a href="#{cid}" class="toc-ch" data-ch="{cid}"><span class="toc-g">{html.escape(group)}</span>{html.escape(title)}</a>')
        if subs:
            t.append('<ol>' + "".join(f'<li><a href="#{sid}">{html.escape(st)}</a></li>' for sid, st in subs) + '</ol>')
        t.append('</li>')
    toc_html = "\n".join(t)
    # modal chapter list
    pick = "\n".join(
        f'<label class="pick"><input type="checkbox" value="{cid}" checked><span class="pick-g">{html.escape(group)}</span><span class="pick-t">{html.escape(title)}</span></label>'
        for cid, group, title, _ in toc)
    nav = '<a href="index.html">전체 교본 목록</a>' 
    tpl = (ROOT / "template.html").read_text(encoding="utf-8")
    css = (ROOT / "style.css").read_text(encoding="utf-8") + FIG_CSS
    js = (ROOT / "app.js").read_text(encoding="utf-8")
    page = (tpl.replace("{{CSS}}", css).replace("{{JS}}", js + "\n" + "\n".join(FIG_JS.values()))
            .replace("{{ACCENT}}", g["accent"]).replace("{{ACCENT2}}", g["accent2"]).replace("{{ACCENT_INK}}", g["accent_ink"])
            .replace("{{NAME}}", g["name"]).replace("{{FULL}}", g["full"]).replace("{{TAG}}", g["tag"])
            .replace("{{SLUG}}", g["slug"]).replace("{{NAV}}", nav).replace("{{TOC}}", toc_html)
            .replace("{{PICK}}", pick).replace("{{CHAPTERS}}", "\n".join(secs))
            .replace("{{HERO_FIG}}", FIGS.get("hero-" + g["slug"]) or hero_term(g["hero"], g.get("prompt", "")))
            .replace("{{NCH}}", str(len(toc))).replace("{{NSEC}}", str(sum(len(s) for *_, s in toc)))
            .replace("{{NQ}}", str(sum(len(re.findall(r'class="q"', s)) for s in secs)))
            .replace("{{DATE}}", "2026년 11월"))
    (DIST / f'{g["slug"]}.html').write_text(page, encoding="utf-8")
    print(g["slug"], len(toc), "chapters", len(page)//1024, "KB")

if __name__ == "__main__":
    for g in GUIDES:
        if not (ROOT / "content" / g["file"]).exists():
            print("SKIP (아직 없음):", g["slug"]); continue
        build(g)
    idx = (ROOT / "index_tpl.html").read_text(encoding="utf-8")
    rows = []
    for gname, gdesc in GROUPS:
        rows.append(f'<section class="grp in"><h2>{gname}</h2><p class="gd">{gdesc}</p><ol>')
        for x in [x for x in GUIDES if x["group"] == gname]:
            rows.append(f'''<li><a class="row" href="{x["slug"]}.html">
      <span class="sw" style="background:{x["accent"]}">{x["short"]}</span>
      <span><h3>{x["full"]}</h3><p>{x["desc"]}</p></span>
      <span class="go">읽기<svg viewBox="0 0 24 24"><path d="M4 12h15M13 6l6 6-6 6"/></svg></span></a></li>''')
        rows.append('</ol></section>')
    idx = idx.replace("{{ROWS}}", "\n".join(rows)).replace("{{N}}", str(len(GUIDES)))
    (DIST / "index.html").write_text(idx, encoding="utf-8")

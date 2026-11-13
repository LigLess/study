#!/usr/bin/env python3
import re, sys, pathlib
from playwright.sync_api import sync_playwright
src = pathlib.Path(sys.argv[1]).resolve()
out = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else "shots"); out.mkdir(exist_ok=True)
html = src.read_text(encoding="utf-8"); fails, warns = [], []
css = " ".join(re.findall(r"<style[^>]*>(.*?)</style>", html, re.S | re.I)) + " " + " ".join(re.findall(r'style="([^"]*)"', html))
rules = [
 (r"(linear|radial|conic)-gradient", "그라데이션 사용 (사진 위 글자용 어두운 스크림만 예외)", "W"),
 (r"background-clip\s*:\s*text", "그라데이션 글자", "F"),
 (r"backdrop-filter", "유리(블러) 패널", "W"),
 (r"#(7c3aed|8b5cf6|a855f7|6366f1|4f46e5|9333ea|a78bfa|c084fc|818cf8)\b", "AI 단골 보라/인디고 색", "F"),
 (r"text-transform\s*:\s*uppercase", "대문자+자간 라벨(아이브로우) 의심", "W"),
 (r"transition\s*:\s*all", "transition: all (속성 지정 필요)", "F"),
 (r"scale\(0\)", "scale(0)에서 등장 (0.95 이상 + opacity)", "F"),
 (r"ease-in[^-]", "ease-in 사용 (UI는 ease-out)", "W"),
 (r"border-left\s*:\s*[2-9]px", "굵은 왼쪽 색 테두리 카드", "W")]
for pat, msg, lvl in rules:
    if re.search(pat, css, re.I): (fails if lvl == "F" else warns).append(msg)
text_only = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", html, flags=re.S | re.I)
if re.search("[\U0001F300-\U0001FAFF☀-➿]", text_only): fails.append("이모지 사용 (아이콘은 SVG로)")
if not re.search(r"prefers-reduced-motion", html): fails.append("prefers-reduced-motion 대응 없음")
if not re.search(r"word-break\s*:\s*keep-all", css): warns.append("한글 word-break: keep-all 없음")
if len(re.findall(r'class="[^"]*\bcard\b', html)) >= 6: warns.append("동일 카드 6개 이상 반복 — 카드 나열 구조 의심")
JS = r"""() => { const r = {overflow: document.documentElement.scrollWidth > innerWidth + 1, long: [], small: 0, moving: 0, fonts: new Set()};
 document.querySelectorAll('h1,h2,h3').forEach(h => { const cs = getComputedStyle(h); const lh = parseFloat(cs.lineHeight) || parseFloat(cs.fontSize)*1.2;
   const lines = Math.round(h.getBoundingClientRect().height / lh); if (lines > 2 && h.offsetParent) r.long.push(h.tagName+' '+lines+'줄: '+h.textContent.trim().slice(0,30)); });
 document.querySelectorAll('p,li,td').forEach(e => { if (e.offsetParent && e.textContent.trim().length > 20 && parseFloat(getComputedStyle(e).fontSize) < 14) r.small++; });
 document.querySelectorAll('*').forEach(e => { const cs = getComputedStyle(e);
   if (cs.animationName !== 'none' || cs.transitionProperty.includes('transform') || cs.transitionProperty.includes('opacity')) r.moving++;
   r.fonts.add(cs.fontFamily.split(',')[0].trim()); });
 r.fonts = [...r.fonts]; return r; }"""
with sync_playwright() as p:
    b = p.chromium.launch()
    for w, h, name in [(1440, 900, "pc"), (390, 844, "mobile")]:
        pg = b.new_page(viewport={"width": w, "height": h}); errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.goto(src.as_uri()); pg.wait_for_timeout(1500)
        pg.evaluate("window.scrollTo(0, document.body.scrollHeight)"); pg.wait_for_timeout(800)
        pg.evaluate("window.scrollTo(0, 0)"); pg.wait_for_timeout(400)
        m = pg.evaluate(JS)
        pg.screenshot(path=str(out / f"{name}_top.png"))
        if m["overflow"]: fails.append(f"[{name}] 가로 스크롤 발생")
        for l in m["long"]: warns.append(f"[{name}] 제목 3줄 이상 → {l}")
        if m["small"]: warns.append(f"[{name}] 14px 미만 본문 {m['small']}곳")
        if errs: fails.append(f"[{name}] 스크립트 오류: {errs[0][:120]}")
        if name == "pc":
            if m["moving"] < 6: warns.append(f"움직이는 요소 {m['moving']}개 — 모션 설명 부족")
            if len([f for f in m["fonts"] if f]) > 4: warns.append(f"글꼴 종류 과다: {m['fonts']}")
        pg.close()
    b.close()
print("FAIL:" if fails else "FAIL: 없음"); [print("  -", f) for f in fails]
print("WARN:" if warns else "WARN: 없음"); [print("  -", w) for w in warns]

# -*- coding: utf-8 -*-
"""교본에 들어가는 설명용 그림(SVG/HTML)과 동작 스크립트"""
import random

random.seed(7)

# ---------- ADsP hero: 산점도 + 회귀선 ----------
_pts = []
for i in range(26):
    x = 70 + i * 15.5 + random.uniform(-6, 6)
    y = 318 - (x - 60) * 0.55 + random.uniform(-38, 38)
    _pts.append((round(x, 1), round(y, 1)))
_circ = "".join(
    f'<circle class="pt" cx="{x}" cy="{y}" r="5.5" style="animation-delay:{120 + i*45}ms"/>' for i, (x, y) in enumerate(_pts))
_resid = "".join(
    f'<line class="rs" x1="{x}" y1="{y}" x2="{x}" y2="{round(318-(x-60)*0.55,1)}" style="animation-delay:{1900 + i*30}ms"/>'
    for i, (x, y) in enumerate(_pts) if i % 3 == 0)
HERO_ADSP = f'''<svg viewBox="0 0 520 380" class="hero-svg anim" role="img" aria-label="점들이 찍히고 그 사이를 지나는 회귀선이 그려지는 산점도">
<g stroke="rgba(255,255,255,.35)" stroke-width="1"><line x1="50" y1="340" x2="500" y2="340"/><line x1="50" y1="20" x2="50" y2="340"/></g>
<g stroke="rgba(255,255,255,.12)" stroke-width="1">{''.join(f'<line x1="50" y1="{y}" x2="500" y2="{y}"/>' for y in (100,180,260))}</g>
<g fill="#fff">{_circ}</g>
<g stroke="#fff" stroke-width="1.2" stroke-dasharray="3 3" opacity=".7">{_resid}</g>
<line class="reg" x1="60" y1="318" x2="490" y2="81.5" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<text x="330" y="66" fill="#fff" font-size="20" font-weight="600" class="eq">ŷ = β₀ + β₁x</text>
<text x="500" y="364" fill="rgba(255,255,255,.75)" font-size="14" text-anchor="end">광고비 x</text>
<text x="56" y="16" fill="rgba(255,255,255,.75)" font-size="14">매출 y</text>
</svg>'''

# ---------- DIKW ----------
DIKW = '''<figure class="fig anim" id="fig-dikw">
<svg viewBox="0 0 700 340" role="img" aria-label="DIKW 피라미드: 아래부터 데이터, 정보, 지식, 지혜">
<g class="lay" style="--d:0ms"><polygon points="65,245 335,245 380,320 20,320" fill="var(--accent)" fill-opacity=".22"/><text x="200" y="290" text-anchor="middle" font-size="19" font-weight="700" fill="var(--text)">Data 데이터</text></g>
<g class="lay" style="--d:220ms"><polygon points="110,170 290,170 335,245 65,245" fill="var(--accent)" fill-opacity=".45"/><text x="200" y="215" text-anchor="middle" font-size="19" font-weight="700" fill="var(--text)">Information 정보</text></g>
<g class="lay" style="--d:440ms"><polygon points="155,95 245,95 290,170 110,170" fill="var(--accent)" fill-opacity=".75"/><text x="200" y="146" text-anchor="middle" font-size="15" font-weight="700" fill="#fff">Knowledge 지식</text></g>
<g class="lay" style="--d:660ms"><polygon points="200,20 245,95 155,95" fill="var(--accent)"/><text x="200" y="84" text-anchor="middle" font-size="13" font-weight="700" fill="#fff">Wisdom</text></g>
<g font-size="15" fill="var(--text)">
<g class="lay" style="--d:120ms"><text x="410" y="278" font-weight="700">가공 전 사실</text><text x="410" y="300" fill="var(--text-2)">A마트 볼펜 100원, B마트 200원</text></g>
<g class="lay" style="--d:340ms"><text x="410" y="203" font-weight="700">패턴·의미를 찾은 것</text><text x="410" y="225" fill="var(--text-2)">A마트 볼펜이 더 싸다</text></g>
<g class="lay" style="--d:560ms"><text x="410" y="128" font-weight="700">정보를 내 것으로 체계화</text><text x="410" y="150" fill="var(--text-2)">볼펜은 A마트에서 사야겠다</text></g>
<g class="lay" style="--d:780ms"><text x="410" y="53" font-weight="700">근본 원리로 새 상황에 적용</text><text x="410" y="75" fill="var(--text-2)">A마트는 다른 상품도 쌀 것이다</text></g>
</g>
<g stroke="var(--line)" stroke-width="1"><line x1="372" y1="283" x2="398" y2="283"/><line x1="327" y1="208" x2="398" y2="208"/><line x1="282" y1="133" x2="398" y2="133"/><line x1="234" y1="58" x2="398" y2="58"/></g>
</svg>
<figcaption>아래층이 쌓여야 위층이 생긴다. 시험에는 "A마트가 더 싸다"처럼 예시 문장을 주고 어느 층인지 고르는 문제가 자주 나온다.</figcaption>
</figure>'''

# ---------- CRISP-DM ----------
_ph = [("업무 이해", 320, 52), ("데이터 이해", 452, 128), ("데이터 준비", 452, 272),
       ("모델링", 320, 348), ("평가", 188, 272), ("전개", 188, 128)]
_phg = "".join(
    f'<g class="ph" data-i="{i}"><rect x="{x-66}" y="{y-22}" width="132" height="44" rx="22"/><text x="{x}" y="{y+6}" text-anchor="middle">{i+1}. {n}</text></g>'
    for i, (n, x, y) in enumerate(_ph))
CRISP = f'''<figure class="fig" id="fig-crisp">
<svg viewBox="0 0 640 400" role="img" aria-label="CRISP-DM 6단계 순환 구조">
<circle cx="320" cy="200" r="150" fill="none" stroke="var(--line)" stroke-width="2" stroke-dasharray="4 6"/>
<g class="orbit" style="transform-origin:320px 200px"><circle cx="320" cy="50" r="7" fill="var(--accent)"/></g>
<text x="320" y="194" text-anchor="middle" font-size="22" font-weight="800" fill="var(--text)">데이터</text>
<text x="320" y="220" text-anchor="middle" font-size="14" fill="var(--text-2)" class="crisp-desc">단계를 오가며 반복</text>
<g class="phs" font-size="16" font-weight="700">{_phg}</g>
<g stroke="var(--accent)" stroke-width="1.6" fill="none" marker-end="url(#ah)" opacity=".8">
<path d="M388 60 q40 10 54 40"/><path d="M430 104 q-30 -20 -46 -40" stroke-dasharray="3 3"/>
<path d="M470 300 q-20 40 -86 52" /><path d="M370 330 q50 -14 70 -40" stroke-dasharray="3 3"/>
</g>
<defs><marker id="ah" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L8 4L0 8z" fill="var(--accent)"/></marker></defs>
</svg>
<figcaption>점선 화살표가 피드백(되돌아가기) 구간이다. 업무 이해 ↔ 데이터 이해, 데이터 준비 ↔ 모델링은 서로 오가며 반복한다. 평가에서 목표를 달성하지 못하면 업무 이해로 돌아간다.</figcaption>
</figure>'''

# ---------- 혼동행렬 계산기 ----------
CM = '''<figure class="fig" id="fig-cm">
<div class="cm">
 <div class="cm-grid">
  <span></span><b class="cm-h">예측 Positive</b><b class="cm-h">예측 Negative</b>
  <b class="cm-h cm-v">실제 Positive</b>
  <label class="cm-c tp">TP<input type="number" min="0" value="40" data-k="tp"></label>
  <label class="cm-c fn">FN<input type="number" min="0" value="10" data-k="fn"></label>
  <b class="cm-h cm-v">실제 Negative</b>
  <label class="cm-c fp">FP<input type="number" min="0" value="5" data-k="fp"></label>
  <label class="cm-c tn">TN<input type="number" min="0" value="45" data-k="tn"></label>
 </div>
 <dl class="cm-out">
  <div><dt>정확도 Accuracy</dt><dd data-o="acc"></dd><p>(TP+TN) / 전체</p></div>
  <div><dt>정밀도 Precision</dt><dd data-o="pre"></dd><p>TP / (TP+FP)</p></div>
  <div><dt>재현율·민감도 Recall</dt><dd data-o="rec"></dd><p>TP / (TP+FN)</p></div>
  <div><dt>특이도 Specificity</dt><dd data-o="spe"></dd><p>TN / (TN+FP)</p></div>
  <div><dt>F1 점수</dt><dd data-o="f1"></dd><p>2·P·R / (P+R)</p></div>
  <div><dt>FPR (1 − 특이도)</dt><dd data-o="fpr"></dd><p>FP / (FP+TN) · ROC의 x축</p></div>
 </dl>
</div>
<figcaption>네 칸의 숫자를 바꿔 보면 지표가 바로 다시 계산된다. 시험에서는 표를 주고 정밀도·재현율·특이도를 계산하게 한다. 분모가 무엇인지(예측 기준인지, 실제 기준인지)가 핵심이다.</figcaption>
</figure>'''

# ---------- SQLD hero ----------
_emp = [("7369", "SMITH", "20"), ("7499", "ALLEN", "30"), ("7566", "JONES", "20"), ("7839", "KING", "10")]
_dept = [("10", "ACCOUNTING"), ("20", "RESEARCH"), ("30", "SALES")]
def _tbl(x, y, title, cols, rows, widths, cls):
    s = [f'<g transform="translate({x},{y})"><text x="0" y="-12" fill="rgba(255,255,255,.8)" font-size="15" font-weight="600">{title}</text>']
    tw = sum(widths)
    s.append(f'<rect x="0" y="0" width="{tw}" height="34" fill="rgba(255,255,255,.16)"/>')
    cx = 0
    for c, w in zip(cols, widths):
        s.append(f'<text x="{cx+12}" y="22" fill="#fff" font-size="14" font-weight="700">{c}</text>'); cx += w
    for r, row in enumerate(rows):
        ry = 34 + r * 36
        s.append(f'<g class="{cls}" data-r="{r}"><rect x="0" y="{ry}" width="{tw}" height="36" fill="transparent"/>')
        cx = 0
        for v, w in zip(row, widths):
            s.append(f'<text x="{cx+12}" y="{ry+23}" fill="#fff" font-size="14" font-family="ui-monospace,Consolas,monospace">{v}</text>'); cx += w
        s.append('</g>')
        s.append(f'<line x1="0" y1="{ry+36}" x2="{tw}" y2="{ry+36}" stroke="rgba(255,255,255,.22)"/>')
    s.append('</g>')
    return "".join(s)
HERO_SQLD = f'''<svg viewBox="0 0 560 330" class="hero-svg" id="hero-sqld" role="img" aria-label="EMP 테이블의 부서번호가 DEPT 테이블의 같은 부서번호 행과 차례로 연결되는 조인 그림">
{_tbl(10, 60, "EMP", ["EMPNO","ENAME","DEPTNO"], _emp, [70, 84, 76], "er")}
{_tbl(340, 78, "DEPT", ["DEPTNO","DNAME"], _dept, [76, 132], "dr")}
<path class="jl" d="" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round"/>
<text x="10" y="318" fill="#fff" font-size="16" font-family="ui-monospace,Consolas,monospace" class="jsql">ON E.DEPTNO = D.DEPTNO</text>
</svg>'''

ORDER = '''<figure class="fig" id="fig-order">
<div class="ord">
 <div class="ord-col"><p class="ord-h">작성 순서</p>
  <ol class="ord-w"><li data-s="5">SELECT</li><li data-s="1">FROM</li><li data-s="2">WHERE</li><li data-s="3">GROUP BY</li><li data-s="4">HAVING</li><li data-s="6">ORDER BY</li></ol></div>
 <div class="ord-col"><p class="ord-h">실행 순서</p>
  <ol class="ord-x"><li data-s="1"><b>FROM</b><span>테이블을 가져온다</span></li><li data-s="2"><b>WHERE</b><span>행을 거른다</span></li><li data-s="3"><b>GROUP BY</b><span>그룹으로 묶는다</span></li><li data-s="4"><b>HAVING</b><span>그룹을 거른다</span></li><li data-s="5"><b>SELECT</b><span>보여줄 칼럼을 고른다</span></li><li data-s="6"><b>ORDER BY</b><span>정렬한다</span></li></ol></div>
</div>
<figcaption>SELECT는 맨 위에 쓰지만 다섯 번째로 실행된다. 그래서 SELECT에서 붙인 별칭(alias)은 WHERE·GROUP BY에서 쓸 수 없고, 마지막인 ORDER BY에서만 쓸 수 있다.</figcaption>
</figure>'''

JOIN = '''<figure class="fig" id="fig-join">
<div class="fig-ctrl" role="group" aria-label="조인 종류">
 <button type="button" class="chip" data-j="inner" aria-pressed="true">INNER</button>
 <button type="button" class="chip" data-j="left" aria-pressed="false">LEFT OUTER</button>
 <button type="button" class="chip" data-j="right" aria-pressed="false">RIGHT OUTER</button>
 <button type="button" class="chip" data-j="full" aria-pressed="false">FULL OUTER</button>
 <button type="button" class="chip" data-j="cross" aria-pressed="false">CROSS</button>
</div>
<pre class="j-sql"><code></code></pre>
<div class="j-wrap">
 <div><p class="j-t">EMP</p><table class="j-a small"><thead><tr><th>ENAME</th><th>DEPTNO</th></tr></thead><tbody></tbody></table></div>
 <div><p class="j-t">DEPT</p><table class="j-b small"><thead><tr><th>DEPTNO</th><th>DNAME</th></tr></thead><tbody></tbody></table></div>
 <div class="j-res"><p class="j-t">결과 <span class="j-n"></span></p><table class="j-r small"><thead><tr><th>ENAME</th><th>E.DEPTNO</th><th>D.DEPTNO</th><th>DNAME</th></tr></thead><tbody></tbody></table></div>
</div>
<figcaption>버튼을 바꿔 보면 결과 행이 달라진다. 짝이 없는 행은 OUTER 쪽에서만 살아남고, 반대편 칼럼은 NULL로 채워진다. CROSS JOIN은 4 × 3 = 12행이다.</figcaption>
</figure>'''

# ---------- Linux ----------
HERO_LINUX = '''<div class="term hero-term" id="heroTerm" aria-label="터미널 예시"><span class="d">student@rocky:~</span></div>'''

BOOT = '''<figure class="fig" id="fig-boot">
<ol class="boot">
 <li data-i="0"><b>펌웨어</b><span>BIOS/UEFI</span></li>
 <li data-i="1"><b>부트로더</b><span>GRUB2</span></li>
 <li data-i="2"><b>커널</b><span>vmlinuz + initramfs</span></li>
 <li data-i="3"><b>systemd</b><span>PID 1</span></li>
 <li data-i="4"><b>target</b><span>multi-user / graphical</span></li>
 <li data-i="5"><b>로그인</b><span>getty · GDM</span></li>
</ol>
<div class="boot-bar"><i></i></div>
<p class="boot-desc" aria-live="polite"></p>
<figcaption>전원을 켜면 위 순서로 제어권이 넘어간다. 각 단계에서 무엇을 하는지가 시험에 나온다.</figcaption>
</figure>'''

CHMOD = '''<figure class="fig" id="fig-chmod">
<div class="perm">
 <div class="perm-grid">
  <span></span><b>r 읽기 (4)</b><b>w 쓰기 (2)</b><b>x 실행 (1)</b>
  <b class="perm-who">소유자 u</b><button type="button" data-b="256" aria-pressed="true">r</button><button type="button" data-b="128" aria-pressed="true">w</button><button type="button" data-b="64" aria-pressed="true">x</button>
  <b class="perm-who">그룹 g</b><button type="button" data-b="32" aria-pressed="true">r</button><button type="button" data-b="16" aria-pressed="false">w</button><button type="button" data-b="8" aria-pressed="true">x</button>
  <b class="perm-who">기타 o</b><button type="button" data-b="4" aria-pressed="false">r</button><button type="button" data-b="2" aria-pressed="false">w</button><button type="button" data-b="1" aria-pressed="false">x</button>
 </div>
 <div class="perm-out">
  <label>8진수로 입력<input type="text" inputmode="numeric" maxlength="3" value="750" class="perm-num" aria-label="8진수 권한"></label>
  <div class="term perm-term"></div>
 </div>
</div>
<figcaption>칸을 눌러 권한을 켜고 끄거나, 숫자 세 자리를 직접 입력해 보자. r=4, w=2, x=1을 더한 값이 한 자리가 된다.</figcaption>
</figure>'''

FIGS = {
    "hero-adsp": HERO_ADSP, "dikw": DIKW, "crisp": CRISP, "cm": CM,
    "hero-sqld": HERO_SQLD, "order": ORDER, "join": JOIN,
    "hero-linux": HERO_LINUX, "boot": BOOT, "chmod": CHMOD,
}

FIG_CSS = r'''
/* hero svg animations */
.hero-svg .pt{opacity:0;transform-box:fill-box;transform-origin:center;animation:ptIn 420ms var(--ease-out) forwards}
@keyframes ptIn{from{opacity:0;transform:scale(.6)}to{opacity:.95;transform:none}}
.hero-svg .reg{stroke-dasharray:500;stroke-dashoffset:500;animation:draw 1100ms var(--ease-io) 1400ms forwards}
.hero-svg .rs{opacity:0;animation:fadeIn 300ms var(--ease-out) forwards}
.hero-svg .eq{opacity:0;animation:fadeIn 500ms var(--ease-out) 2300ms forwards}
@keyframes draw{to{stroke-dashoffset:0}}
@keyframes fadeIn{to{opacity:1}}
#hero-sqld .er rect,#hero-sqld .dr rect{transition:fill 260ms var(--ease-out)}
#hero-sqld .on rect{fill:rgba(255,255,255,.2)}
#hero-sqld .jl{transition:opacity 200ms var(--ease-out)}
.hero-term{min-height:300px;font-size:15px;background:#0b0f12}
.hero-term .cur{display:inline-block;width:.6em;height:1.1em;background:#7ee2a8;vertical-align:-.15em;animation:blink 1s steps(1) infinite}
@keyframes blink{50%{opacity:0}}

/* DIKW */
.js #fig-dikw:not(.play) .lay{opacity:0}
#fig-dikw.play .lay{animation:rise 620ms var(--ease-out) both;animation-delay:var(--d)}
@keyframes rise{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}

/* CRISP */
#fig-crisp .ph rect{fill:#fff;stroke:var(--line);stroke-width:1.5;transition:fill 300ms var(--ease-out),stroke 300ms var(--ease-out)}
#fig-crisp .ph text{fill:var(--text);transition:fill 300ms var(--ease-out)}
#fig-crisp .ph.on rect{fill:var(--accent);stroke:var(--accent)}
#fig-crisp .ph.on text{fill:#fff}
#fig-crisp .orbit{transition:transform 900ms var(--ease-io)}

/* CM */
.cm{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:28px;align-items:start}
.cm-grid{display:grid;grid-template-columns:auto 1fr 1fr;gap:6px;font-size:14px}
.cm-h{font-weight:600;color:var(--text-2);text-align:center;align-self:end;padding-bottom:2px}
.cm-v{writing-mode:horizontal-tb;text-align:right;align-self:center;padding-right:6px}
.cm-c{display:flex;flex-direction:column;gap:4px;padding:12px;border-radius:4px;font-weight:700;font-size:14px;background:#fff;border:1px solid var(--line)}
.cm-c.tp,.cm-c.tn{background:var(--accent-2);border-color:transparent}
.cm-c input{font:inherit;font-size:24px;font-weight:700;width:100%;border:0;background:transparent;padding:0;color:var(--text);font-variant-numeric:tabular-nums}
.cm-c input:focus{outline:none}
.cm-c:focus-within{outline:2px solid var(--accent);outline-offset:1px}
.cm-out{display:grid;grid-template-columns:1fr 1fr;gap:14px 18px;margin:0}
.cm-out div{margin:0}
.cm-out dt{font-size:13.5px;color:var(--text-2)}
.cm-out dd{margin:0;font-size:26px;font-weight:700;font-variant-numeric:tabular-nums;letter-spacing:-.01em;line-height:1.25}
.cm-out p{margin:0 !important;font-size:14px;color:var(--text-2)}

/* ORDER */
.ord{display:grid;grid-template-columns:1fr 1.4fr;gap:28px}
.ord-h{font-size:14px;color:var(--text-2);margin:0 0 8px !important;font-weight:600}
.ord ol{list-style:none;padding:0 !important;margin:0 !important;display:grid;gap:6px}
.ord li{margin:0;padding:10px 14px;background:#fff;border:1px solid var(--line);border-radius:4px;font-family:var(--mono);font-size:15px;
  transition:background-color 260ms var(--ease-out),color 260ms var(--ease-out),border-color 260ms var(--ease-out),transform 260ms var(--ease-out)}
.ord-x li{display:flex;justify-content:space-between;gap:12px}
.ord-x li span{font-family:var(--font);color:var(--text-2);font-size:14px}
.ord-x li::before{content:attr(data-s);font-family:var(--font);font-weight:700;color:var(--accent);margin-right:-4px;min-width:1.2em}
.ord-x li b{flex:1}
.ord li.on{background:var(--accent);border-color:var(--accent);color:#fff;transform:translateX(4px)}
.ord li.on span,.ord-x li.on::before{color:#fff}
.ord li.done{border-color:var(--accent)}

/* JOIN */
.j-sql{margin-bottom:16px}
.j-wrap{display:grid;grid-template-columns:.8fr .8fr 1.4fr;gap:16px;align-items:start}
.j-t{font-size:14px;font-weight:700;margin:0 0 6px !important}
.j-n{color:var(--accent);font-weight:600;margin-left:6px}
.j-wrap table{font-size:13.5px;background:#fff}
.j-wrap th,.j-wrap td{padding:6px 8px;font-family:var(--mono);white-space:nowrap}
.j-wrap tr.m td{background:var(--accent-2)}
.j-wrap td.nul{color:var(--text-2);font-style:italic}
.j-r tbody tr{animation:rowIn 260ms var(--ease-out) both}
@keyframes rowIn{from{opacity:0;transform:translateY(6px)}}

/* BOOT */
.boot{list-style:none;padding:0 !important;margin:0 0 14px !important;display:grid;grid-template-columns:repeat(6,1fr);gap:6px}
.boot li{margin:0;padding:12px 10px;background:#fff;border:1px solid var(--line);border-radius:4px;display:flex;flex-direction:column;
  transition:background-color 300ms var(--ease-out),color 300ms var(--ease-out),border-color 300ms var(--ease-out)}
.boot b{font-size:15px}
.boot span{font-size:12.5px;color:var(--text-2);line-height:1.4;margin-top:2px}
.boot li.on{background:var(--accent);border-color:var(--accent);color:#fff}
.boot li.on span{color:rgba(255,255,255,.85)}
.boot li.done{border-color:var(--accent)}
.boot-bar{height:4px;background:var(--surface-2);border-radius:2px;overflow:hidden}
.boot-bar i{display:block;height:100%;background:var(--accent);transform-origin:0 50%;transform:scaleX(0);transition:transform 900ms var(--ease-io)}
.boot-desc{min-height:3.4em;margin:14px 0 0 !important;font-size:15.5px}

/* CHMOD */
.perm{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:24px;align-items:start}
.perm-grid{display:grid;grid-template-columns:auto repeat(3,1fr);gap:6px;font-size:13.5px;align-items:center}
.perm-grid>b{color:var(--text-2);font-weight:600;text-align:center}
.perm-grid>b.perm-who{text-align:right;padding-right:6px;color:var(--text)}
.perm-grid button{font:inherit;font-family:var(--mono);font-size:20px;font-weight:700;height:52px;border-radius:4px;border:1px solid var(--line);background:#fff;color:var(--text-2);cursor:pointer;
  transition:background-color 160ms var(--ease-out),color 160ms var(--ease-out),transform 140ms var(--ease-out)}
.perm-grid button:active{transform:scale(.96)}
.perm-grid button[aria-pressed="true"]{background:var(--accent);border-color:var(--accent);color:#fff}
.perm-grid button[aria-pressed="false"]{text-decoration:line-through;text-decoration-thickness:1px}
.perm-out label{display:flex;flex-direction:column;font-size:13.5px;color:var(--text-2);gap:4px;margin-bottom:10px}
.perm-num{font:inherit;font-family:var(--mono);font-size:30px;font-weight:700;width:5em;padding:4px 10px;border:1px solid var(--line);border-radius:4px;color:var(--text);letter-spacing:.08em}
.perm-term{font-size:13.5px;min-height:7.5em}

@media (max-width:720px){
  .cm,.perm,.ord{grid-template-columns:1fr}
  .j-wrap{grid-template-columns:1fr 1fr}
  .j-res{grid-column:1/-1;overflow-x:auto}
  .boot{grid-template-columns:repeat(3,1fr)}
}
@media print{
  .hero-term{display:none}
  #fig-dikw .lay{opacity:1 !important}
  #fig-crisp .orbit{display:none}
  #fig-crisp .ph rect{fill:#fff !important;stroke:var(--accent) !important}
  #fig-crisp .ph text{fill:var(--text) !important}
  .ord li.on,.boot li.on{background:#fff !important;color:var(--text) !important;border-color:var(--accent) !important;transform:none}
  .ord li.on span,.boot li.on span{color:var(--text-2) !important}
  .ord-x li.on::before{color:var(--accent) !important}
  .boot-bar,.boot-desc{display:none}
  .boot{grid-template-columns:repeat(6,1fr)}
  .perm-grid button{height:9mm;font-size:12pt}
  .cm-c input{font-size:14pt}
  .j-wrap{grid-template-columns:.8fr .8fr 1.4fr}
}
'''

FIG_JS = {
"adsp": r'''
(function(){
  var d = document.getElementById('fig-dikw'); __onSeen(d, function(){ d.classList.add('play'); });
  var c = document.getElementById('fig-crisp');
  if (c) {
    var ph = c.querySelectorAll('.ph'), orb = c.querySelector('.orbit'), desc = c.querySelector('.crisp-desc');
    var tx = ['비즈니스 목표 → 분석 목표','데이터 수집·품질 확인','정제·통합·변환 (가장 오래 걸림)','기법 선택·모델 작성','목표 달성 여부 판단','배포·모니터링·보고서'];
    var n = -1, timer = null;
    function step(){ n++; var i = n % 6; ph.forEach(function(p){ p.classList.toggle('on', +p.dataset.i === i); });
      orb.style.transform = 'rotate(' + (n*60) + 'deg)'; desc.textContent = tx[i]; }
    __onSeen(c, function(){ step(); timer = setInterval(step, 1800); });
  }
  var m = document.getElementById('fig-cm');
  if (m) {
    var ins = m.querySelectorAll('input'), out = {};
    m.querySelectorAll('[data-o]').forEach(function(e){ out[e.dataset.o] = e; });
    function f(x){ return isFinite(x) ? (x*100).toFixed(1) + '%' : '—'; }
    function calc(){ var v = {}; ins.forEach(function(i){ v[i.dataset.k] = Math.max(0, +i.value || 0); });
      var all = v.tp+v.fn+v.fp+v.tn, P = v.tp/(v.tp+v.fp), R = v.tp/(v.tp+v.fn);
      out.acc.textContent = f((v.tp+v.tn)/all); out.pre.textContent = f(P); out.rec.textContent = f(R);
      out.spe.textContent = f(v.tn/(v.tn+v.fp)); out.f1.textContent = isFinite(2*P*R/(P+R)) ? (2*P*R/(P+R)).toFixed(3) : '—';
      out.fpr.textContent = f(v.fp/(v.fp+v.tn)); }
    ins.forEach(function(i){ i.addEventListener('input', calc); }); calc();
  }
})();
''',
"sqld": r'''
(function(){
  /* hero: 조인 행 연결 애니메이션 */
  var h = document.getElementById('hero-sqld');
  if (h) {
    var er = h.querySelectorAll('.er'), dr = h.querySelectorAll('.dr'), jl = h.querySelector('.jl');
    var map = [1, 2, 1, 0], k = 0; // EMP행 -> DEPT행 인덱스 (20,30,20,10)
    function yE(r){ return 60 + 34 + r*36 + 18; } function yD(r){ return 78 + 34 + r*36 + 18; }
    function tick(){
      er.forEach(function(g){ g.classList.remove('on'); }); dr.forEach(function(g){ g.classList.remove('on'); });
      var r = k % 4, d = map[r]; er[r].classList.add('on'); dr[d].classList.add('on');
      jl.setAttribute('d', 'M240 ' + yE(r) + ' C290 ' + yE(r) + ' 290 ' + yD(d) + ' 340 ' + yD(d)); k++;
    }
    if (!matchMedia('(prefers-reduced-motion: reduce)').matches) { tick(); setInterval(tick, 1500); } else tick();
  }
  /* 실행 순서 */
  var o = document.getElementById('fig-order');
  if (o) {
    var w = o.querySelectorAll('li'), s = 0;
    function st(){ s = s % 6 + 1; w.forEach(function(li){ var n = +li.dataset.s; li.classList.toggle('on', n === s); li.classList.toggle('done', n < s); }); }
    __onSeen(o, function(){ st(); setInterval(st, 1400); });
  }
  /* 조인 시각화 */
  var j = document.getElementById('fig-join');
  if (j) {
    var A = [['SMITH',20],['ALLEN',30],['KING',10],['SCOTT',null]];
    var B = [[10,'ACCOUNTING'],[20,'RESEARCH'],[40,'OPERATIONS']];
    var SQL = {
      inner:'SELECT E.ENAME, E.DEPTNO, D.DEPTNO, D.DNAME\n  FROM EMP E INNER JOIN DEPT D\n    ON E.DEPTNO = D.DEPTNO;',
      left:'SELECT E.ENAME, E.DEPTNO, D.DEPTNO, D.DNAME\n  FROM EMP E LEFT OUTER JOIN DEPT D\n    ON E.DEPTNO = D.DEPTNO;',
      right:'SELECT E.ENAME, E.DEPTNO, D.DEPTNO, D.DNAME\n  FROM EMP E RIGHT OUTER JOIN DEPT D\n    ON E.DEPTNO = D.DEPTNO;',
      full:'SELECT E.ENAME, E.DEPTNO, D.DEPTNO, D.DNAME\n  FROM EMP E FULL OUTER JOIN DEPT D\n    ON E.DEPTNO = D.DEPTNO;',
      cross:'SELECT E.ENAME, E.DEPTNO, D.DEPTNO, D.DNAME\n  FROM EMP E CROSS JOIN DEPT D;'
    };
    function cell(v){ return v === null ? '<td class="nul">NULL</td>' : '<td>' + v + '</td>'; }
    function run(t){
      var res = [], ma = {}, mb = {};
      if (t === 'cross') { A.forEach(function(a){ B.forEach(function(b){ res.push([a[0],a[1],b[0],b[1]]); }); }); }
      else {
        A.forEach(function(a, i){ B.forEach(function(b, k){ if (a[1] !== null && a[1] === b[0]) { res.push([a[0],a[1],b[0],b[1]]); ma[i]=1; mb[k]=1; } }); });
        if (t === 'left' || t === 'full') A.forEach(function(a, i){ if (!ma[i]) res.push([a[0],a[1],null,null]); });
        if (t === 'right' || t === 'full') B.forEach(function(b, k){ if (!mb[k]) res.push([null,null,b[0],b[1]]); });
      }
      j.querySelector('.j-a tbody').innerHTML = A.map(function(a,i){ return '<tr' + (ma[i]||t==='cross' ? ' class="m"' : '') + '>' + cell(a[0]) + cell(a[1]) + '</tr>'; }).join('');
      j.querySelector('.j-b tbody').innerHTML = B.map(function(b,k){ return '<tr' + (mb[k]||t==='cross' ? ' class="m"' : '') + '>' + cell(b[0]) + cell(b[1]) + '</tr>'; }).join('');
      j.querySelector('.j-r tbody').innerHTML = res.map(function(r,i){ return '<tr style="animation-delay:' + (i*35) + 'ms">' + r.map(cell).join('') + '</tr>'; }).join('');
      j.querySelector('.j-n').textContent = res.length + '행';
      j.querySelector('.j-sql code').textContent = SQL[t];
    }
    j.querySelectorAll('.chip').forEach(function(b){ b.addEventListener('click', function(){
      j.querySelectorAll('.chip').forEach(function(x){ x.setAttribute('aria-pressed', x === b); }); run(b.dataset.j); }); });
    run('inner');
  }
})();
''',
"linux": r'''
(function(){
  /* hero terminal typing */
  var t = document.getElementById('heroTerm');
  if (t) {
    var S = [
      ['$ ', 'whoami', 'student'],
      ['$ ', 'pwd', '/home/student'],
      ['$ ', 'ls -l report.txt', '-rw-r--r--. 1 student student 2048 Nov  7 16:00 report.txt'],
      ['$ ', 'chmod 640 report.txt', ''],
      ['$ ', 'ls -l report.txt', '-rw-r-----. 1 student student 2048 Nov  7 16:00 report.txt'],
      ['$ ', 'ps -ef | grep sshd | head -1', 'root      1024     1  0 09:12 ?   00:00:00 /usr/sbin/sshd -D']
    ];
    var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
    var html = '<span class="d">[student@rocky ~]</span>';
    function esc(s){ return s.replace(/&/g,'&amp;').replace(/</g,'&lt;'); }
    if (reduce) { S.forEach(function(s){ html += '\n<span class="p">' + s[0] + '</span>' + esc(s[1]) + (s[2] ? '\n' + esc(s[2]) : ''); }); t.innerHTML = html; }
    else {
      var ln = 0, ci = 0;
      function frame(){
        if (ln >= S.length) { t.innerHTML = html + '\n<span class="p">$ </span><span class="cur"></span>'; return; }
        var s = S[ln];
        if (ci <= s[1].length) {
          t.innerHTML = html + '\n<span class="p">' + s[0] + '</span>' + esc(s[1].slice(0, ci)) + '<span class="cur"></span>';
          ci++; setTimeout(frame, 38 + Math.random()*50);
        } else {
          html += '\n<span class="p">' + s[0] + '</span>' + esc(s[1]) + (s[2] ? '\n' + esc(s[2]) : '');
          ln++; ci = 0; t.innerHTML = html; setTimeout(frame, 520);
        }
      }
      setTimeout(frame, 500);
    }
  }
  /* boot */
  var b = document.getElementById('fig-boot');
  if (b) {
    var steps = b.querySelectorAll('li'), bar = b.querySelector('.boot-bar i'), dsc = b.querySelector('.boot-desc');
    var D = ['전원이 들어오면 메인보드 펌웨어(BIOS 또는 UEFI)가 POST(하드웨어 자가 진단)를 하고, 부팅 장치에서 부트로더를 찾는다.',
             '부트로더 GRUB2가 메뉴를 보여주고, 선택한 커널 이미지와 initramfs를 메모리에 올린다. 설정은 /boot/grub2/grub.cfg.',
             '커널이 하드웨어를 초기화하고 루트 파일 시스템을 마운트한다. initramfs는 그 전에 필요한 임시 드라이버 묶음이다.',
             '커널이 첫 프로세스 systemd를 실행한다. PID는 1번이고, 이후 모든 프로세스의 조상이 된다.',
             'systemd가 기본 target(예전의 런레벨)에 필요한 서비스들을 띄운다. 기본값 확인은 systemctl get-default.',
             '텍스트 로그인(getty) 또는 그래픽 로그인(GDM) 화면이 뜬다. 로그인하면 셸이 시작된다.'];
    var i = -1;
    function go(){ i = (i + 1) % 6; steps.forEach(function(e){ var n = +e.dataset.i; e.classList.toggle('on', n === i); e.classList.toggle('done', n < i); });
      bar.style.transform = 'scaleX(' + ((i + 1) / 6) + ')'; dsc.textContent = (i + 1) + '단계 · ' + D[i]; }
    __onSeen(b, function(){ go(); setInterval(go, 2600); });
  }
  /* chmod */
  var p = document.getElementById('fig-chmod');
  if (p) {
    var bt = p.querySelectorAll('.perm-grid button'), num = p.querySelector('.perm-num'), term = p.querySelector('.perm-term');
    function val(){ var v = 0; bt.forEach(function(x){ if (x.getAttribute('aria-pressed') === 'true') v += +x.dataset.b; }); return v; }
    function sym(v){ var s = 'rwxrwxrwx', o = '-'; for (var k = 0; k < 9; k++) o += (v & (256 >> k)) ? s[k] : '-'; return o; }
    function show(v, fromNum){
      var oc = v.toString(8); while (oc.length < 3) oc = '0' + oc;
      if (!fromNum) num.value = oc;
      bt.forEach(function(x){ x.setAttribute('aria-pressed', (v & +x.dataset.b) ? 'true' : 'false'); });
      var u = 'ugo', parts = [];
      for (var k = 0; k < 3; k++) { var seg = sym(v).slice(1 + k*3, 4 + k*3).replace(/-/g, ''); parts.push(u[k] + '=' + seg); }
      term.innerHTML = '<span class="p">$ </span>chmod ' + oc + ' report.txt\n<span class="d"># 같은 뜻</span>\n<span class="p">$ </span>chmod ' + parts.join(',') + ' report.txt\n<span class="p">$ </span>ls -l report.txt\n' + sym(v) + '. 1 student student 2048 report.txt';
    }
    bt.forEach(function(x){ x.addEventListener('click', function(){ x.setAttribute('aria-pressed', x.getAttribute('aria-pressed') !== 'true'); show(val()); }); });
    num.addEventListener('input', function(){ var s = num.value.replace(/[^0-7]/g, ''); num.value = s; if (s.length === 3) show(parseInt(s, 8), true); });
    show(val());
  }
})();
'''
}

# ================= 추가 그림 (9권 확장) =================
import json as _json

def hero_term(lines, prompt):
    """lines: [[prompt, command, output], ...]"""
    data = _json.dumps(lines, ensure_ascii=False).replace("'", "&#39;")
    return f'<div class="term hero-term gen-term" data-prompt="{prompt}" data-lines=\'{data}\' aria-label="실행 예시"><span class="d">{prompt}</span></div>'

SUBNET = '''<figure class="fig" id="fig-subnet">
<div class="sn">
 <div class="sn-in">
  <label>IP 주소<input type="text" class="sn-ip" value="192.168.10.70" inputmode="decimal" aria-label="IP 주소"></label>
  <label>프리픽스 /<input type="number" class="sn-px" value="26" min="0" max="32" aria-label="프리픽스 길이"></label>
 </div>
 <div class="sn-bits" aria-hidden="true"></div>
 <dl class="sn-out">
  <div><dt>서브넷 마스크</dt><dd data-o="mask"></dd></div>
  <div><dt>네트워크 주소</dt><dd data-o="net"></dd></div>
  <div><dt>브로드캐스트 주소</dt><dd data-o="bc"></dd></div>
  <div><dt>사용 가능 범위</dt><dd data-o="range"></dd></div>
  <div><dt>호스트 수</dt><dd data-o="hosts"></dd></div>
  <div><dt>클래스 · 종류</dt><dd data-o="cls"></dd></div>
 </dl>
</div>
<figcaption>IP와 프리픽스를 바꿔 보자. 위 32칸에서 진한 칸이 네트워크 부분, 옅은 칸이 호스트 부분이다. 호스트 부분이 전부 0이면 네트워크 주소, 전부 1이면 브로드캐스트 주소라서 호스트 수는 2^(호스트 비트) − 2다.</figcaption>
</figure>'''

TCP3 = '''<figure class="fig" id="fig-tcp3">
<svg viewBox="0 0 640 330" role="img" aria-label="TCP 3방향 핸드셰이크와 4방향 종료">
<text x="110" y="28" text-anchor="middle" font-size="16" font-weight="700" fill="var(--text)">클라이언트</text>
<text x="530" y="28" text-anchor="middle" font-size="16" font-weight="700" fill="var(--text)">서버</text>
<line x1="110" y1="40" x2="110" y2="320" stroke="var(--line)" stroke-width="2"/>
<line x1="530" y1="40" x2="530" y2="320" stroke="var(--line)" stroke-width="2"/>
<defs><marker id="ta" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L8 4L0 8z" fill="var(--accent)"/></marker></defs>
<g class="tm" style="--d:0ms"><line x1="112" y1="60" x2="526" y2="100" stroke="var(--accent)" stroke-width="2" marker-end="url(#ta)"/><text x="320" y="70" text-anchor="middle" font-size="14" fill="var(--text)">① SYN  seq=100</text></g>
<g class="tm" style="--d:700ms"><line x1="528" y1="110" x2="114" y2="150" stroke="var(--accent)" stroke-width="2" marker-end="url(#ta)"/><text x="320" y="120" text-anchor="middle" font-size="14" fill="var(--text)">② SYN + ACK  seq=300, ack=101</text></g>
<g class="tm" style="--d:1400ms"><line x1="112" y1="160" x2="526" y2="200" stroke="var(--accent)" stroke-width="2" marker-end="url(#ta)"/><text x="320" y="170" text-anchor="middle" font-size="14" fill="var(--text)">③ ACK  ack=301</text></g>
<g class="tm" style="--d:2100ms"><rect x="20" y="215" width="600" height="30" rx="4" fill="var(--accent-2)"/><text x="320" y="235" text-anchor="middle" font-size="14" font-weight="700" fill="var(--text)">ESTABLISHED — 데이터 송수신</text></g>
<g class="tm" style="--d:2800ms" font-size="12.5" fill="var(--text-2)"><text x="20" y="62">SYN_SENT</text><text x="545" y="112">SYN_RECEIVED</text><text x="20" y="152">ESTABLISHED</text><text x="545" y="202">ESTABLISHED</text></g>
<g class="tm" style="--d:3400ms" font-size="13" fill="var(--text)"><text x="320" y="275" text-anchor="middle">종료는 4단계: FIN → ACK → FIN → ACK</text><text x="320" y="300" text-anchor="middle" fill="var(--text-2)">먼저 끊은 쪽은 TIME_WAIT 상태로 잠시 기다린다</text></g>
</svg>
<figcaption>연결할 때 세 번 주고받는다. 상대의 순서번호(seq)에 1을 더해 확인번호(ack)로 돌려주는 것이 핵심이다. SYN만 잔뜩 보내고 ③을 보내지 않는 공격이 SYN 플러딩이다.</figcaption>
</figure>'''

PAGING = '''<figure class="fig" id="fig-paging">
<div class="fig-ctrl" role="group" aria-label="페이지 교체 알고리즘">
 <button type="button" class="chip" data-a="FIFO" aria-pressed="true">FIFO</button>
 <button type="button" class="chip" data-a="LRU" aria-pressed="false">LRU</button>
 <button type="button" class="chip" data-a="OPT" aria-pressed="false">OPT</button>
 <label class="pg-in">참조열 <input type="text" class="pg-ref" value="1 2 3 1 4 5 2 1 2 3" aria-label="페이지 참조열"></label>
 <label class="pg-in">프레임 <input type="number" class="pg-fr" value="3" min="1" max="6" aria-label="프레임 수"></label>
</div>
<div class="pg-wrap"><table class="pg small"><tbody></tbody></table></div>
<p class="pg-sum"></p>
<figcaption>알고리즘이나 참조열을 바꾸면 표가 다시 계산된다. 진한 칸이 페이지 부재(fault)가 난 순간이다. FIFO는 가장 먼저 들어온 페이지를, LRU는 가장 오래 쓰지 않은 페이지를, OPT는 앞으로 가장 늦게 쓸 페이지를 내보낸다.</figcaption>
</figure>'''

FIGS.update({"subnet": SUBNET, "tcp3": TCP3, "paging": PAGING})

FIG_CSS += r'''
/* SUBNET */
.sn-in{display:flex;gap:14px;flex-wrap:wrap;margin-bottom:14px}
.sn-in label,.pg-in{display:flex;flex-direction:column;font-size:13.5px;color:var(--text-2);gap:4px}
.sn-in input,.pg-in input{font:inherit;font-family:var(--mono);font-size:18px;padding:6px 10px;border:1px solid var(--line);border-radius:4px;color:var(--text);background:#fff}
.sn-ip{width:11em}.sn-px{width:5em}
.sn-bits{display:grid;grid-template-columns:repeat(32,1fr);gap:2px;margin-bottom:16px}
.sn-bits i{height:26px;border-radius:2px;background:var(--surface-2);font-style:normal;font-family:var(--mono);font-size:11px;display:grid;place-items:center;color:var(--text-2);
  transition:background-color 200ms var(--ease-out),color 200ms var(--ease-out)}
.sn-bits i.n{background:var(--accent);color:#fff}
.sn-bits i.g{margin-right:5px}
.sn-out{display:grid;grid-template-columns:repeat(3,1fr);gap:12px 18px;margin:0}
.sn-out div{margin:0}.sn-out dt{font-size:13.5px;color:var(--text-2)}
.sn-out dd{margin:0;font-family:var(--mono);font-size:17px;font-weight:700;font-variant-numeric:tabular-nums}
/* TCP3 */
.js #fig-tcp3:not(.play) .tm{opacity:0}
#fig-tcp3.play .tm{animation:rise 520ms var(--ease-out) both;animation-delay:var(--d)}
/* PAGING */
.pg-in{flex-direction:row;align-items:center;margin-left:8px}
.pg-in input{font-size:14px;padding:4px 8px}
.pg-ref{width:14em}.pg-fr{width:4em}
.pg-wrap{overflow-x:auto}
.pg td,.pg th{text-align:center;font-family:var(--mono);padding:6px 8px;min-width:34px;border:1px solid var(--line)}
.pg th{background:#fff}
.pg td.f{background:var(--accent);color:#fff;font-weight:700}
.pg td.h{background:#fff}
.pg-sum{margin:12px 0 0 !important;font-weight:600}
@media (max-width:720px){ .sn-out{grid-template-columns:1fr 1fr} .sn-bits i{font-size:0;height:18px} }
@media print{ .js #fig-tcp3 .tm{opacity:1 !important} .sn-in input,.pg-in input{border-color:#d6dce2} }
'''

FIG_JS["common"] = r'''
(function(){
  /* 범용 터미널 히어로 */
  document.querySelectorAll('.gen-term').forEach(function(t){
    var S; try { S = JSON.parse(t.dataset.lines); } catch(e) { return; }
    var P = t.dataset.prompt || '';
    function esc(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;'); }
    var html = '<span class="d">' + esc(P) + '</span>';
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) {
      S.forEach(function(s){ html += '\n<span class="p">' + esc(s[0]) + '</span>' + esc(s[1]) + (s[2] ? '\n' + esc(s[2]) : ''); }); t.innerHTML = html; return;
    }
    var ln = 0, ci = 0;
    function frame(){
      if (ln >= S.length) { t.innerHTML = html + '\n<span class="cur"></span>'; return; }
      var s = S[ln];
      if (ci <= s[1].length) { t.innerHTML = html + '\n<span class="p">' + esc(s[0]) + '</span>' + esc(s[1].slice(0, ci)) + '<span class="cur"></span>'; ci++; setTimeout(frame, 30 + Math.random()*40); }
      else { html += '\n<span class="p">' + esc(s[0]) + '</span>' + esc(s[1]) + (s[2] ? '\n' + esc(s[2]) : ''); ln++; ci = 0; t.innerHTML = html; setTimeout(frame, 450); }
    }
    setTimeout(frame, 500);
  });
  /* 서브넷 계산기 */
  var sn = document.getElementById('fig-subnet');
  if (sn) {
    var ip = sn.querySelector('.sn-ip'), px = sn.querySelector('.sn-px'), bits = sn.querySelector('.sn-bits'), o = {};
    sn.querySelectorAll('[data-o]').forEach(function(e){ o[e.dataset.o] = e; });
    for (var i = 0; i < 32; i++) { var b = document.createElement('i'); if (i % 8 === 7 && i < 31) b.className = 'g'; bits.appendChild(b); }
    var cells = bits.querySelectorAll('i');
    function toS(n){ return [n>>>24, (n>>>16)&255, (n>>>8)&255, n&255].join('.'); }
    function calc(){
      var p = ip.value.trim().split('.').map(Number), k = Math.max(0, Math.min(32, parseInt(px.value, 10) || 0));
      if (p.length !== 4 || p.some(function(x){ return isNaN(x) || x < 0 || x > 255; })) { o.mask.textContent = '올바른 IP를 입력'; return; }
      var n = ((p[0]<<24)>>>0) + (p[1]<<16) + (p[2]<<8) + p[3];
      var m = k === 0 ? 0 : (0xFFFFFFFF << (32 - k)) >>> 0;
      var net = (n & m) >>> 0, bc = (net | (~m >>> 0)) >>> 0;
      cells.forEach(function(c, i){ c.textContent = (n >>> (31 - i)) & 1; c.classList.toggle('n', i < k); });
      o.mask.textContent = toS(m); o.net.textContent = toS(net); o.bc.textContent = toS(bc);
      var h = k >= 31 ? (k === 32 ? 1 : 2) : Math.pow(2, 32 - k) - 2;
      o.range.textContent = k >= 31 ? toS(net) + ' ~ ' + toS(bc) : toS(net + 1) + ' ~ ' + toS(bc - 1);
      o.hosts.textContent = h.toLocaleString() + '개';
      var c = p[0] < 128 ? 'A' : p[0] < 192 ? 'B' : p[0] < 224 ? 'C' : p[0] < 240 ? 'D' : 'E';
      var priv = p[0] === 10 || (p[0] === 172 && p[1] >= 16 && p[1] <= 31) || (p[0] === 192 && p[1] === 168);
      o.cls.textContent = c + '클래스 · ' + (p[0] === 127 ? '루프백' : priv ? '사설' : '공인');
    }
    ip.addEventListener('input', calc); px.addEventListener('input', calc); calc();
  }
  /* TCP 3-way */
  var tc = document.getElementById('fig-tcp3'); if (tc) __onSeen(tc, function(){ tc.classList.add('play'); });
  /* 페이지 교체 */
  var pg = document.getElementById('fig-paging');
  if (pg) {
    var alg = 'FIFO', ref = pg.querySelector('.pg-ref'), fr = pg.querySelector('.pg-fr'), tb = pg.querySelector('tbody'), sum = pg.querySelector('.pg-sum');
    function run(){
      var R = ref.value.trim().split(/[\s,]+/).filter(Boolean), F = Math.max(1, Math.min(6, +fr.value || 3));
      var mem = [], cols = [], faults = 0, last = {}, order = [];
      R.forEach(function(r, t){
        var hit = mem.indexOf(r) > -1;
        if (!hit) {
          faults++;
          if (mem.length < F) { mem.push(r); order.push(r); }
          else {
            var victim;
            if (alg === 'FIFO') victim = order.shift();
            else if (alg === 'LRU') { victim = mem.slice().sort(function(a, b){ return last[a] - last[b]; })[0]; }
            else { var far = -1; mem.forEach(function(m){ var nx = R.indexOf(m, t + 1); if (nx === -1) nx = 1e9; if (nx > far) { far = nx; victim = m; } }); }
            mem[mem.indexOf(victim)] = r;
            if (alg === 'FIFO') order.push(r);
          }
        }
        last[r] = t; cols.push({r: r, m: mem.slice(), f: !hit});
      });
      var h = '<tr><th>참조</th>' + cols.map(function(c){ return '<th>' + c.r + '</th>'; }).join('') + '</tr>';
      for (var i = 0; i < F; i++) h += '<tr><th>프레임' + (i + 1) + '</th>' + cols.map(function(c){ var v = c.m[i]; return '<td class="' + (c.f && v === c.r ? 'f' : 'h') + '">' + (v === undefined ? '' : v) + '</td>'; }).join('') + '</tr>';
      tb.innerHTML = h; sum.textContent = alg + ' · 페이지 부재 ' + faults + '회 / 참조 ' + R.length + '회';
    }
    pg.querySelectorAll('.chip').forEach(function(b){ b.addEventListener('click', function(){ pg.querySelectorAll('.chip').forEach(function(x){ x.setAttribute('aria-pressed', x === b); }); alg = b.dataset.a; run(); }); });
    ref.addEventListener('input', run); fr.addEventListener('input', run); run();
  }
})();
'''

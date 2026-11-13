# 교본 원본 (빌드용)

이 폴더는 사이트에 노출되지 않는다 (밑줄로 시작하는 폴더는 GitHub Pages가 게시하지 않음).

## 수정 → 반영 절차

1. 내용 수정: `content/<slug>.md` (공통 단원은 `content/shared/*.md`)
2. 책 목록·색·소개 문구: `guides.py`
3. 빌드: `_src`에서 `python3 build.py` (markdown 패키지 필요) → `_src/dist/*.html` 생성
4. `dist`의 html을 저장소 루트로 복사 후 커밋·푸시 → 1~2분 뒤 ligless.github.io/study 반영
5. `dist/`는 커밋하지 않는다

## 규칙

- 사이트는 학생에게도 공개된다. 멘토·상담·학원 관점 표현을 넣지 않는다
- 요청받은 부분만 수정하고 디자인(색·레이아웃·여백)은 임의로 바꾸지 않는다
- 표 안의 백틱 코드에 `|`가 들어가면 `\|`로 쓴다
- `shinguide.html`은 별도 파일이므로 건드리지 않는다
- 점검 도구: `tools/check_html.py`, `tools/shot.py`, `tools/pdftest.py` (Playwright)

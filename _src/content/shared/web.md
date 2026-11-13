## 웹의 구조

브라우저(클라이언트)가 **HTTP** 요청을 보내면 웹 서버가 HTML·CSS·JS 파일을 응답한다. 동적인 처리는 **WAS**(Tomcat 등)가 서버 프로그램(Java, Python 등)을 실행해 결과를 만든다.

| 기술 | 역할 |
|---|---|
| HTML | 문서의 **구조**와 내용 |
| CSS | **모양**(색, 크기, 배치) |
| JavaScript | **동작**(클릭 반응, 데이터 요청) |

| HTTP 메서드 | 용도 |
|---|---|
| GET | 조회. 데이터가 URL에 노출 |
| POST | 생성·전송. 데이터가 본문에 담김 |
| PUT / PATCH | 전체 수정 / 일부 수정 |
| DELETE | 삭제 |

| 상태 코드 | 의미 |
|---|---|
| 200 | 성공 |
| 301 / 302 | 영구 / 임시 이동 |
| 400 | 잘못된 요청 |
| 401 / 403 | 인증 필요 / 권한 없음 |
| 404 | 찾을 수 없음 |
| 500 | 서버 내부 오류 |

**URL 구조**: `https://www.example.com:443/board/list?page=2#top` → 프로토콜 / 호스트 / 포트 / 경로 / 쿼리 스트링 / 프래그먼트.

## HTML

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>제목</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1>가장 큰 제목</h1>
  <p>문단 <strong>강조</strong> <a href="https://example.com">링크</a></p>
  <img src="logo.png" alt="로고">
  <ul><li>순서 없는 목록</li></ul>
  <ol><li>순서 있는 목록</li></ol>
  <table>
    <tr><th>이름</th><th>점수</th></tr>
    <tr><td>김</td><td>90</td></tr>
  </table>
  <form action="/login" method="post">
    <input type="text" name="id" placeholder="아이디">
    <input type="password" name="pw">
    <input type="checkbox"> <input type="radio">
    <select><option>선택</option></select>
    <textarea></textarea>
    <button type="submit">로그인</button>
  </form>
  <script src="app.js"></script>
</body>
</html>
```

| 태그 | 의미 |
|---|---|
| `<h1>`~`<h6>` | 제목 (h1이 가장 큼) |
| `<p>`, `<br>`, `<hr>` | 문단, 줄바꿈, 가로줄 |
| `<a href>` | 링크 |
| `<img src alt>` | 이미지 (alt: 대체 텍스트, 접근성) |
| `<div>` / `<span>` | 블록 영역 / 인라인 영역 |
| 시맨틱 태그 | `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>` — 의미를 가진 구조 |
| `<table>`, `<tr>`, `<th>`, `<td>` | 표, 행, 제목 칸, 데이터 칸. 병합은 `colspan`, `rowspan` |

**블록 요소**(div, p, h1 — 한 줄 전체 차지)와 **인라인 요소**(span, a, img — 내용만큼만).

## CSS

```css
/* 선택자 { 속성: 값; } */
h1 { color: #222; font-size: 32px; }
.box { width: 200px; padding: 10px; margin: 20px; border: 1px solid #ccc; }   /* class */
#header { background: #f5f5f5; }                                               /* id */
ul li { list-style: none; }          /* 후손 선택자 */
ul > li { }                          /* 자식 선택자 */
a:hover { text-decoration: underline; }   /* 가상 클래스 */
.row { display: flex; justify-content: space-between; align-items: center; }
```

| 선택자 | 의미 | 우선순위 |
|---|---|---|
| `*` | 전체 | 가장 낮음 |
| `태그` | 태그 이름 | |
| `.class` | 클래스 (여러 요소) | |
| `#id` | 아이디 (문서에 하나) | |
| `style=""` | 인라인 스타일 | |
| `!important` | 강제 | 가장 높음 |

**박스 모델**: 안쪽부터 **content → padding → border → margin**.

| 속성 | 설명 |
|---|---|
| `display` | block, inline, inline-block, none, flex, grid |
| `position` | static(기본), relative(자기 위치 기준), absolute(가장 가까운 위치 지정 조상 기준), fixed(화면 기준), sticky |
| `float` | 좌우로 띄워 배치 |
| `@media` | 화면 크기별 스타일 (반응형 웹) |

## JavaScript

```javascript
let count = 0;                 // 변경 가능 변수
const PI = 3.14;               // 상수
var old = 1;                   // 예전 방식 (함수 스코프)

function add(a, b) { return a + b; }
const mul = (a, b) => a * b;   // 화살표 함수

const arr = [3, 1, 2];
arr.push(4);                   // [3, 1, 2, 4]
console.log(arr.length, arr.map(x => x * 2), arr.filter(x => x > 1));

const user = { name: "Kim", age: 20 };
console.log(user.name, user["age"]);

console.log(1 + "2", "3" * 2, 5 == "5", 5 === "5");   // "12" 6 true false

document.querySelector("#btn").addEventListener("click", () => {
  document.querySelector("#out").textContent = "클릭!";
});
```

- `==`는 값만 비교(형 변환), `===`는 값과 타입 모두 비교
- **DOM**: HTML 문서를 객체 트리로 표현한 것. `document.getElementById`, `querySelector`로 접근
- 이벤트: `click`, `submit`, `keydown`, `load`, `change`, `mouseover`
- **AJAX**: 페이지 새로고침 없이 서버와 비동기 통신 (`fetch`, `XMLHttpRequest`)
- **JSON**: `{"name": "Kim", "age": 20}` — 자바스크립트 객체 표기 기반 데이터 형식. `JSON.parse`, `JSON.stringify`

### 기타 웹 기술

| 기술 | 설명 |
|---|---|
| 웹 표준 | W3C가 정한 표준을 지켜 어떤 브라우저에서도 같게 |
| 웹 접근성 | 장애인·고령자도 이용 가능하게 (alt 속성, 키보드 조작, 명도 대비) |
| 반응형 웹 | 화면 크기에 맞춰 레이아웃 자동 조정 (미디어 쿼리) |
| 쿠키 / 세션 | 클라이언트에 저장 / 서버에 저장하는 상태 정보 |
| 프레임워크 | React, Vue(프론트엔드), Spring, Django, Express(백엔드) |

:::quiz
Q. 웹 문서의 구조를 정의하는 언어는?
1) CSS
2) HTML
3) JavaScript
4) JSON
> 정답 2 | HTML은 구조, CSS는 모양, JavaScript는 동작.

Q. CSS 박스 모델에서 안쪽부터 바깥쪽 순서로 옳은 것은?
1) content → border → padding → margin
2) content → padding → border → margin
3) margin → border → padding → content
4) padding → content → border → margin
> 정답 2 | 내용 → 안쪽 여백 → 테두리 → 바깥 여백.

Q. CSS 선택자 중 우선순위가 가장 높은 것은? (!important 제외)
1) 태그 선택자
2) 클래스 선택자
3) 아이디 선택자
4) 인라인 스타일
> 정답 4 | 인라인 > 아이디 > 클래스 > 태그.

Q. JavaScript에서 `5 === "5"`의 결과는?
1) true
2) false
3) 5
4) 오류
> 정답 2 | ===는 타입까지 비교한다. ==는 true.

Q. 이미지를 볼 수 없는 사용자를 위해 대체 텍스트를 제공하는 속성은?
1) src
2) href
3) alt
4) title
> 정답 3 | alt 속성은 웹 접근성의 기본이다.

Q. HTTP 상태 코드 404의 의미는?
1) 성공
2) 권한 없음
3) 요청한 자원을 찾을 수 없음
4) 서버 내부 오류
> 정답 3 | 404 Not Found.

Q. 페이지 전체를 새로고침하지 않고 서버와 비동기적으로 데이터를 주고받는 기술은?
1) AJAX
2) DOM
3) CSS
4) SOAP
> 정답 1 | Asynchronous JavaScript and XML.
:::

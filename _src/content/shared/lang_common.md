## 프로그래밍 언어의 분류

| 분류 | 특징 | 대표 언어 |
|---|---|---|
| 절차적(구조적) 언어 | 순서대로 명령을 실행. 순차·선택·반복 3가지 구조로 작성. 함수 단위 | C, Pascal, FORTRAN, COBOL |
| 객체지향 언어 | 데이터와 기능을 객체로 묶어 설계. 캡슐화·상속·다형성 | Java, C++, C#, Python, Smalltalk |
| 스크립트 언어 | 컴파일 없이 인터프리터로 바로 실행. 서버 측(PHP, Python), 클라이언트 측(JavaScript) | Python, JavaScript, PHP, Perl, Ruby, Shell |
| 선언형 언어 | "어떻게"가 아니라 "무엇을" 원하는지 기술. 함수형(LISP, Haskell), 논리형(Prolog), 질의어(SQL) | SQL, HTML, LISP, Prolog |

| 실행 방식 | 설명 |
|---|---|
| 컴파일러 | 전체 소스를 기계어(목적 코드)로 한 번에 번역 후 실행. 실행 빠름. C, C++ |
| 인터프리터 | 한 줄씩 번역하며 바로 실행. 실행 느리지만 수정·디버깅이 쉬움. Python, JavaScript |
| 혼합(바이트코드) | 컴파일해서 중간 코드(바이트코드)를 만들고 가상 머신이 실행. Java(JVM) |

번역 과정: 소스 코드 → **컴파일러** → 목적 코드 → **링커**(라이브러리 연결) → 실행 파일 → **로더**(메모리 적재) → 실행. 전처리기(`#include`, `#define`)는 컴파일 전에 동작한다.

## 데이터 타입과 변수

| 구분 | C | Java | Python |
|---|---|---|---|
| 정수 | `char`(1B), `short`(2B), `int`(4B), `long`(4/8B) | `byte`(1B), `short`(2B), `int`(4B), `long`(8B) | `int` (크기 제한 없음) |
| 실수 | `float`(4B), `double`(8B) | `float`(4B), `double`(8B) | `float` |
| 문자 | `char`(1B, 아스키) | `char`(2B, 유니코드) | 문자열 `str`만 존재 |
| 논리 | 없음 (0은 거짓, 나머지 참) | `boolean` (true/false) | `bool` (True/False) |
| 문자열 | 문자 배열 `char s[10]` | `String` (클래스) | `str` |

**변수 이름 규칙** (공통): 영문자·숫자·밑줄(`_`) 사용, **숫자로 시작 불가**, 공백·특수문자 불가, 예약어 불가, 대소문자 구분. Java는 `$`도 허용.

- **상수**: 값을 바꿀 수 없음. C `const int A = 5;` / `#define A 5`, Java `final int A = 5;`
- **형 변환**: 자동(묵시적) 변환은 작은 타입 → 큰 타입. 강제(명시적) 변환은 `(int)3.7` → 3 (소수점 버림)

## 연산자

| 우선순위 | 연산자 | 결합 방향 |
|---|---|---|
| 1 (높음) | `()` `[]` `.` `->` 후위 `++` `--` | → |
| 2 | 단항: `!` `~` 전위 `++` `--` `+` `-` `(형변환)` `sizeof` | ← |
| 3 | 산술: `*` `/` `%` | → |
| 4 | 산술: `+` `-` | → |
| 5 | 시프트: `<<` `>>` | → |
| 6 | 관계: `<` `<=` `>` `>=` | → |
| 7 | 관계: `==` `!=` | → |
| 8 | 비트: `&` → `^` → `\|` | → |
| 9 | 논리: `&&` → `\|\|` | → |
| 10 | 조건(삼항): `조건 ? 참 : 거짓` | ← |
| 11 (낮음) | 대입: `=` `+=` `-=` `*=` 등 | ← |

외우는 순서: **단항 → 산술 → 시프트 → 관계 → 비트 → 논리 → 조건 → 대입** ("단산시관비논조대").

:::exam 자주 나오는 연산
- 정수끼리 나누면 몫만 남는다: `7 / 2` = 3 (Python은 `7 // 2` = 3, `7 / 2` = 3.5)
- `%`는 나머지: `7 % 3` = 1, `-7 % 3`은 C·Java에서 −1, Python에서 2
- 전위 `++a`는 증가 후 사용, 후위 `a++`는 사용 후 증가
- 비트 연산: `5 & 3` = 1 (101 & 011 = 001), `5 | 3` = 7, `5 ^ 3` = 6, `~5` = −6, `5 << 1` = 10, `5 >> 1` = 2
- 단락 평가: `A && B`에서 A가 거짓이면 B는 실행하지 않는다. `A || B`에서 A가 참이면 B는 실행하지 않는다
:::

## 제어문 공통

| 구조 | 형태 |
|---|---|
| 선택 | `if`, `if-else`, `else if`, `switch-case` (C·Java: `break` 없으면 아래 case로 계속 실행 — fall through) |
| 반복 | `for`, `while`(조건 먼저 검사), `do-while`(최소 1번 실행 후 검사) |
| 분기 | `break`(반복 탈출), `continue`(다음 반복으로), `return`, `goto` |

## 라이브러리와 예외 처리

**라이브러리**는 자주 쓰는 함수·클래스를 모아 둔 것이다.

| 언어 | 표준 라이브러리 예 |
|---|---|
| C | `stdio.h`(입출력: printf, scanf), `stdlib.h`(malloc, free, atoi, rand), `string.h`(strlen, strcpy, strcmp, strcat), `math.h`(sqrt, pow), `time.h` |
| Java | `java.lang`(자동 import: String, Math, System), `java.util`(List, ArrayList, HashMap, Scanner), `java.io`(파일 입출력), `java.net` |
| Python | 내장 함수(print, len, range, input), `math`, `random`, `datetime`, `os`, `sys`, `re` |

**예외(Exception)**는 실행 중 발생하는 오류다. Java·Python은 예외 처리 구문을 제공한다.

```java
try {
    int x = 10 / 0;                    // ArithmeticException
} catch (ArithmeticException e) {
    System.out.println("0으로 나눌 수 없음");
} finally {
    System.out.println("항상 실행");
}
```

```python
try:
    x = int("abc")                     # ValueError
except ValueError as e:
    print("숫자가 아님")
else:
    print("예외가 없을 때만 실행")
finally:
    print("항상 실행")
```

| 대표 예외 (Java) | 원인 |
|---|---|
| `ArithmeticException` | 0으로 나눔 |
| `NullPointerException` | null 객체 참조 |
| `ArrayIndexOutOfBoundsException` | 배열 범위 초과 |
| `NumberFormatException` | 숫자로 바꿀 수 없는 문자열 |
| `ClassCastException` | 잘못된 형 변환 |
| `FileNotFoundException`, `IOException` | 파일 없음, 입출력 오류 (**검사 예외** — 반드시 처리) |

:::quiz
Q. C 언어에서 `int a = 7, b = 2; printf("%d", a / b * b + a % b);`의 출력은?
1) 6
2) 7
3) 8
4) 3
> 정답 2 | 7 / 2 = 3, 3 * 2 = 6, 7 % 2 = 1, 6 + 1 = 7. 몫 × 나누는 수 + 나머지 = 원래 수.

Q. 다음 연산자 중 우선순위가 가장 높은 것은?
1) `&&`
2) `==`
3) `+`
4) `=`
> 정답 3 | 산술 → 관계 → 논리 → 대입 순이다.

Q. 소스 코드 전체를 한 번에 번역하여 목적 코드를 만드는 번역기는?
1) 인터프리터
2) 컴파일러
3) 어셈블러
4) 링커
> 정답 2 | 인터프리터는 한 줄씩 번역·실행한다. 링커는 목적 코드와 라이브러리를 연결한다.

Q. `5 ^ 3`(비트 XOR)의 결과는?
1) 1
2) 6
3) 7
4) 125
> 정답 2 | 101 XOR 011 = 110 = 6. 같으면 0, 다르면 1.

Q. 다음 중 변수 이름으로 사용할 수 없는 것은? (C 언어)
1) _count
2) total2
3) 2total
4) sumValue
> 정답 3 | 숫자로 시작할 수 없다.

Q. 반복문 중 조건과 상관없이 최소 한 번은 실행되는 것은?
1) for
2) while
3) do-while
4) foreach
> 정답 3 | do-while은 본문을 먼저 실행하고 조건을 검사한다.
:::

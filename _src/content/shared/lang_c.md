## C 언어 기본 구조와 입출력

```c
#include <stdio.h>          // 전처리기: 표준 입출력 헤더 포함

int main(void) {            // 프로그램 시작점
    int age = 20;
    printf("나이: %d\n", age);
    return 0;               // 0 = 정상 종료
}
```

| 서식 지정자 | 의미 | 예 |
|---|---|---|
| `%d` | 10진 정수 | `printf("%d", 10)` → 10 |
| `%f` | 실수 (기본 소수점 6자리) | `printf("%f", 3.14)` → 3.140000 |
| `%.2f` | 소수점 2자리 | 3.14 |
| `%c` | 문자 1개 | `printf("%c", 65)` → A |
| `%s` | 문자열 | `printf("%s", "hi")` |
| `%o` / `%x` | 8진수 / 16진수 | `printf("%o %x", 10, 255)` → 12 ff |
| `%5d` / `%-5d` | 5칸 오른쪽 / 왼쪽 정렬 | |
| `%p` | 포인터 주소 | |

이스케이프 문자: `\n` 줄바꿈, `\t` 탭, `\\` 역슬래시, `\"` 큰따옴표, `\0` 널 문자(문자열 끝).

입력: `scanf("%d", &a);` — 변수 앞에 주소 연산자 `&`. 문자열(배열)은 이름 자체가 주소라 `&` 없이 `scanf("%s", str);`

## 제어문 따라가기

```c
int i, sum = 0;
for (i = 1; i <= 10; i++) {
    if (i % 2 == 0) continue;   // 짝수는 건너뜀
    if (i > 7) break;           // 7보다 크면 탈출
    sum += i;
}
printf("%d %d", i, sum);        // 9 16
```

i = 1, 3, 5, 7을 더해 sum = 16. i = 8은 짝수라 continue, i = 9에서 break → i는 9.

```c
int n = 2;
switch (n) {
    case 1: printf("A");
    case 2: printf("B");
    case 3: printf("C"); break;
    default: printf("D");
}
// 출력: BC  (case 2부터 break를 만날 때까지 실행)
```

## 배열과 문자열

```c
int a[5] = {10, 20, 30};     // 나머지 a[3], a[4]는 0
int b[] = {1, 2, 3, 4};      // 크기 4로 자동 결정
int m[2][3] = {{1,2,3},{4,5,6}};  // m[1][2] = 6
char s[] = "KOREA";          // 크기 6 (마지막 '\0' 포함)
printf("%d %d", sizeof(s), (int)strlen(s));   // 6 5
```

| 문자열 함수 (`string.h`) | 기능 |
|---|---|
| `strlen(s)` | 길이 (`\0` 제외) |
| `strcpy(d, s)` | s를 d에 복사 |
| `strcat(d, s)` | d 뒤에 s를 붙임 |
| `strcmp(a, b)` | 같으면 0, a가 사전순으로 앞이면 음수 |

## 포인터

**포인터**는 메모리 주소를 저장하는 변수다.

```c
int a = 10;
int *p = &a;        // p에 a의 주소 저장
printf("%d\n", *p); // 10  (* : p가 가리키는 곳의 값)
*p = 20;            // a를 20으로 바꿈
printf("%d\n", a);  // 20
```

### 배열과 포인터

배열 이름은 첫 원소의 주소다. `arr[i]` ≡ `*(arr + i)`

```c
int arr[] = {10, 20, 30, 40};
int *p = arr;
printf("%d\n", *(p + 2));   // 30
printf("%d\n", *p + 2);     // 12  (*p 먼저 = 10, 그다음 +2)
p++;
printf("%d\n", *p);         // 20
```

```c
char *s = "HELLO";
printf("%c %s\n", *(s + 1), s + 2);   // E LLO
```

### 함수와 포인터: 값 전달 vs 주소 전달

```c
void swap1(int x, int y) { int t = x; x = y; y = t; }     // 값 복사 → 원본 안 바뀜
void swap2(int *x, int *y) { int t = *x; *x = *y; *y = t; } // 주소 전달 → 원본 바뀜

int main(void) {
    int a = 1, b = 2;
    swap1(a, b); printf("%d %d\n", a, b);   // 1 2
    swap2(&a, &b); printf("%d %d\n", a, b); // 2 1
    return 0;
}
```

### 2차원 배열과 포인터

```c
int m[2][3] = {{1,2,3},{4,5,6}};
printf("%d\n", *(*(m + 1) + 2));  // 6  = m[1][2]
printf("%d\n", **m);              // 1  = m[0][0]
```

## 구조체

```c
struct Student {
    char name[10];
    int score;
};

int main(void) {
    struct Student s[2] = {{"Kim", 90}, {"Lee", 80}};
    struct Student *p = s;
    printf("%s %d\n", p->name, p->score);     // Kim 90   (-> : 포인터로 멤버 접근)
    printf("%d\n", (p + 1)->score);           // 80
    printf("%d\n", s[1].score + p->score);    // 170
    return 0;
}
```

## 재귀 함수

```c
int fact(int n) {
    if (n <= 1) return 1;
    return n * fact(n - 1);
}
int fib(int n) {
    if (n <= 1) return n;
    return fib(n - 1) + fib(n - 2);
}
// fact(5) = 120,  fib(6) = 8  (0 1 1 2 3 5 8)
```

## static 변수와 메모리 영역

```c
void count(void) {
    static int c = 0;   // 프로그램 끝날 때까지 값 유지, 초기화는 한 번만
    int d = 0;          // 호출할 때마다 새로 0
    c++; d++;
    printf("%d %d ", c, d);
}
// count(); count(); count();  →  1 1 2 1 3 1
```

| 영역 | 저장 대상 |
|---|---|
| 코드(텍스트) | 실행할 기계어 코드 |
| 데이터 | 전역 변수, static 변수 |
| 힙 | `malloc`으로 동적 할당한 메모리 (`free`로 해제) |
| 스택 | 지역 변수, 매개변수, 함수 호출 정보 |

:::tip 코드 문제 푸는 법
1. 변수표를 그린다 (변수 이름을 가로로 적고, 값이 바뀔 때마다 아래에 새 값을 적는다).
2. 반복문은 한 바퀴씩 표에 적는다. 머릿속으로만 돌리면 반드시 틀린다.
3. 출력 형식(`%d` 뒤 공백, `\n`)까지 그대로 적는다. 실기는 띄어쓰기 하나 틀려도 오답이다.
:::

:::quiz
Q. 다음 C 코드의 출력은?

```c
int a = 5, b;
b = a++ + ++a;
printf("%d %d", a, b);
```
1) 6 11
2) 7 11
3) 7 12
4) 6 12
> 정답 3 | a++는 5를 쓰고 a = 6, ++a는 a = 7로 만든 뒤 7을 쓴다. b = 5 + 7 = 12, a = 7. (한 식에서 같은 변수를 두 번 증감하는 것은 C 표준상 정의되지 않은 동작이지만, 시험에서는 왼쪽부터 순서대로 계산한다.)

Q. 다음 코드의 출력은?

```c
int arr[] = {3, 6, 9, 12};
int *p = arr + 1;
printf("%d", *p + *(p + 2));
```
1) 15
2) 18
3) 21
4) 9
> 정답 2 | p는 arr[1] = 6을 가리킨다. *(p + 2)는 arr[3] = 12. 6 + 12 = 18.

Q. 다음 코드의 출력은?

```c
int i, s = 0;
for (i = 0; i < 5; i++) {
    if (i == 3) break;
    s += i;
}
printf("%d", s);
```
1) 3
2) 6
3) 10
4) 0
> 정답 1 | i = 0, 1, 2를 더해 3. i = 3에서 탈출.

Q. `char s[] = "ABC";`일 때 `sizeof(s)`의 값은?
1) 2
2) 3
3) 4
4) 8
> 정답 3 | 문자열 끝의 널 문자 `\0`까지 4바이트.

Q. 구조체 포인터 p로 멤버 score에 접근하는 올바른 표현은?
1) p.score
2) p->score
3) *p.score
4) &p.score
> 정답 2 | 포인터는 `->` 또는 `(*p).score`를 쓴다. `*p.score`는 우선순위 때문에 `*(p.score)`로 해석되어 오류.

Q. 다음 재귀 함수에서 f(4)의 값은?

```c
int f(int n) { if (n == 0) return 0; return n + f(n - 1); }
```
1) 4
2) 6
3) 10
4) 24
> 정답 3 | 4 + 3 + 2 + 1 + 0 = 10.

Q. 다음 코드의 출력은?

```c
int x = 3;
switch (x) {
    case 1: x += 1;
    case 3: x += 3;
    case 5: x += 5;
    default: x += 10;
}
printf("%d", x);
```
1) 6
2) 11
3) 21
4) 3
> 정답 3 | case 3부터 break가 없어 끝까지 실행: 3 + 3 + 5 + 10 = 21.
:::

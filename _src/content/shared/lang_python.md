## Python 기본 문법

- 들여쓰기로 블록을 구분한다 (중괄호 없음). 보통 공백 4칸
- 변수 선언 시 타입을 쓰지 않는다 (동적 타입)
- 주석은 `#`, 여러 줄 문자열은 `"""..."""`

```python
print("A", "B", sep="-", end="!\n")   # A-B!
print(7 / 2, 7 // 2, 7 % 2, 2 ** 10)  # 3.5 3 1 1024
print("ab" * 3)                       # ababab
print(type(3), type(3.0), type("3"))  # <class 'int'> <class 'float'> <class 'str'>
x = int(input("숫자: "))               # input은 항상 문자열을 돌려줌
```

## 자료형

| 자료형 | 예 | 순서 | 변경 | 중복 |
|---|---|---|---|---|
| 리스트 `list` | `[1, 2, 3]` | O | O | O |
| 튜플 `tuple` | `(1, 2, 3)` | O | X | O |
| 세트 `set` | `{1, 2, 3}` | X | O | X |
| 딕셔너리 `dict` | `{"a": 1, "b": 2}` | O (3.7+) | O | 키 중복 X |
| 문자열 `str` | `"abc"` | O | X | O |

### 인덱싱과 슬라이싱

```python
s = "PYTHON"
print(s[0], s[-1])      # P N
print(s[1:4])           # YTH   (1 이상 4 미만)
print(s[:2], s[3:])     # PY HON
print(s[::2])           # PTO   (2칸씩)
print(s[::-1])          # NOHTYP (뒤집기)

a = [10, 20, 30, 40, 50]
print(a[-2:])           # [40, 50]
print(a[1:4:2])         # [20, 40]
```

### 리스트 메서드

```python
a = [3, 1, 2]
a.append(5)        # [3, 1, 2, 5]      끝에 추가
a.insert(1, 9)     # [3, 9, 1, 2, 5]   1번 위치에 삽입
a.remove(9)        # [3, 1, 2, 5]      값 9 삭제 (첫 번째 것)
x = a.pop()        # x = 5, a = [3, 1, 2]
a.extend([7, 8])   # [3, 1, 2, 7, 8]
a.sort()           # [1, 2, 3, 7, 8]   원본 정렬
a.reverse()        # [8, 7, 3, 2, 1]
print(a.index(3), a.count(1), len(a))   # 2 1 5
b = sorted(a)      # 원본은 그대로, 정렬된 새 리스트
```

### 딕셔너리와 세트

```python
d = {"kim": 90, "lee": 80}
d["park"] = 70
print(d.get("choi", 0))         # 0 (없으면 기본값)
for k, v in d.items():
    print(k, v)
print(list(d.keys()))           # ['kim', 'lee', 'park']

s1 = {1, 2, 3}; s2 = {2, 3, 4}
print(s1 & s2, s1 | s2, s1 - s2)   # {2, 3} {1, 2, 3, 4} {1}
```

## 제어문과 반복

```python
for i in range(5):            print(i, end=" ")   # 0 1 2 3 4
for i in range(1, 10, 3):     print(i, end=" ")   # 1 4 7
for i in range(5, 0, -2):     print(i, end=" ")   # 5 3 1

for idx, val in enumerate(["a", "b"]):   # 0 a / 1 b
    print(idx, val)
for a, b in zip([1, 2], ["x", "y"]):     # 1 x / 2 y
    print(a, b)

n = 0
while n < 3:
    n += 1
else:
    print("반복이 break 없이 끝나면 실행")   # while/for-else
```

### 컴프리헨션

```python
sq = [x * x for x in range(1, 6)]            # [1, 4, 9, 16, 25]
ev = [x for x in range(10) if x % 2 == 0]    # [0, 2, 4, 6, 8]
dic = {x: len(x) for x in ["a", "bb"]}       # {'a': 1, 'bb': 2}
```

## 함수

```python
def add(a, b=10):            # b는 기본값 10
    return a + b
print(add(1), add(1, 2))     # 11 3

def total(*args):            # 가변 인자 → 튜플
    return sum(args)
print(total(1, 2, 3))        # 6

def info(**kw):              # 키워드 가변 인자 → 딕셔너리
    return kw
print(info(a=1, b=2))        # {'a': 1, 'b': 2}

f = lambda x, y: x * y       # 익명 함수
print(f(3, 4))               # 12
print(list(map(lambda x: x * 2, [1, 2, 3])))      # [2, 4, 6]
print(list(filter(lambda x: x > 1, [1, 2, 3])))   # [2, 3]
```

:::warn 가변 객체 공유
```python
a = [1, 2, 3]
b = a          # 같은 리스트를 가리킴
b.append(4)
print(a)       # [1, 2, 3, 4]  ← a도 바뀜
c = a[:]       # 복사본 (또는 a.copy())
```
:::

## 클래스

```python
class Animal:
    count = 0                       # 클래스 변수
    def __init__(self, name):       # 생성자
        self.name = name            # 인스턴스 변수
        Animal.count += 1
    def speak(self):
        return "..."

class Dog(Animal):                  # 상속
    def speak(self):                # 오버라이딩
        return self.name + ": 멍멍"

d = Dog("바둑이")
print(d.speak(), Animal.count)      # 바둑이: 멍멍 1
print(isinstance(d, Animal))        # True
```

## 문자열 메서드

```python
s = " Hello World "
print(s.strip())               # 'Hello World'  양쪽 공백 제거
print(s.split())               # ['Hello', 'World']
print("-".join(["a", "b"]))    # a-b
print("abc".upper(), "ABC".lower())
print("hello".replace("l", "L"))   # heLLo
print("hello".find("l"), "hello".count("l"))   # 2 2
print(f"{3.14159:.2f}", "{}+{}".format(1, 2))   # 3.14 1+2
```

:::quiz
Q. 다음 Python 코드의 출력은?

```python
a = [1, 2, 3, 4, 5]
print(a[1:4][::-1])
```
1) [2, 3, 4]
2) [4, 3, 2]
3) [5, 4, 3]
4) [4, 3, 2, 1]
> 정답 2 | a[1:4] = [2, 3, 4], 뒤집으면 [4, 3, 2].

Q. 다음 코드의 출력은?

```python
print(17 // 5, 17 % 5, 2 ** 3)
```
1) 3.4 2 6
2) 3 2 8
3) 3 2 6
4) 4 2 8
> 정답 2 | //는 몫, %는 나머지, **는 거듭제곱.

Q. 순서가 없고 중복을 허용하지 않는 Python 자료형은?
1) list
2) tuple
3) set
4) str
> 정답 3 | set이다.

Q. 다음 코드의 출력은?

```python
x = [1, 2]
y = x
y.append(3)
print(len(x))
```
1) 2
2) 3
3) 1
4) 오류
> 정답 2 | y와 x는 같은 리스트를 가리키므로 x도 길이 3.

Q. 다음 코드의 출력은?

```python
r = [i * 2 for i in range(5) if i % 2 == 1]
print(r)
```
1) [2, 6]
2) [1, 3]
3) [0, 4, 8]
4) [2, 4, 6]
> 정답 1 | i = 1, 3만 조건을 만족하고 2배 하면 [2, 6].

Q. 다음 코드의 출력은?

```python
d = {"a": 1, "b": 2}
d["a"] += 10
print(sum(d.values()))
```
1) 3
2) 12
3) 13
4) 오류
> 정답 3 | a = 11, b = 2, 합 13.

Q. `"banana".count("a") + "banana".find("n")`의 값은?
1) 3
2) 5
3) 6
4) 4
> 정답 2 | count("a") = 3, find("n") = 2 (첫 위치). 3 + 2 = 5.
:::

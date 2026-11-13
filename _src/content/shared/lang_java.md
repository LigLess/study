## Java 기본 구조

```java
public class Main {                          // 파일 이름은 public 클래스 이름과 같아야 함 (Main.java)
    public static void main(String[] args) { // 프로그램 시작점
        int a = 10;
        System.out.println("a = " + a);      // 줄바꿈 출력
        System.out.print("no newline ");     // 줄바꿈 없음
        System.out.printf("%d %.1f%n", 3, 2.5); // 서식 출력
    }
}
```

- 문자열 + 숫자 = 문자열: `"a" + 1 + 2` → `"a12"`, `1 + 2 + "a"` → `"3a"` (왼쪽부터 계산)
- `char` + 정수 = 정수: `'A' + 1` → 66, `(char)('A' + 1)` → 'B'
- 정수 나눗셈: `7 / 2` → 3, `7.0 / 2` → 3.5

## 객체지향의 핵심 개념

| 개념 | 설명 |
|---|---|
| 클래스 (Class) | 객체를 만들기 위한 설계도. 속성(필드)과 기능(메서드) |
| 객체 (Object) / 인스턴스 | 클래스로 만든 실체. `new`로 생성 |
| 캡슐화 (Encapsulation) | 데이터와 메서드를 묶고, 내부를 숨김(정보 은닉). `private` 필드 + `getter/setter` |
| 상속 (Inheritance) | 부모 클래스의 속성·메서드를 자식이 물려받음. `extends`. Java는 **단일 상속**만 |
| 다형성 (Polymorphism) | 같은 이름의 메서드가 객체에 따라 다르게 동작. 오버라이딩·오버로딩 |
| 추상화 (Abstraction) | 공통 특징만 뽑아 표현. 추상 클래스, 인터페이스 |

| 구분 | 오버로딩 (Overloading) | 오버라이딩 (Overriding) |
|---|---|---|
| 의미 | 같은 클래스에서 **이름은 같고 매개변수가 다른** 메서드 여러 개 | 부모 메서드를 자식이 **같은 형태로 재정의** |
| 조건 | 매개변수 개수·타입·순서가 달라야 함 (반환형만 다르면 안 됨) | 이름·매개변수·반환형이 같아야 함 |

### 접근 제어자

| 제어자 | 같은 클래스 | 같은 패키지 | 자식 클래스 | 전체 |
|---|---|---|---|---|
| `public` | O | O | O | O |
| `protected` | O | O | O | |
| (default) | O | O | | |
| `private` | O | | | |

## 클래스와 생성자

```java
class Car {
    private String name;
    private int speed;
    static int count = 0;           // 클래스 변수: 모든 객체가 공유

    Car(String name) {              // 생성자: 클래스 이름과 같고 반환형 없음
        this(name, 0);              // 다른 생성자 호출
    }
    Car(String name, int speed) {
        this.name = name;           // this: 자기 자신 객체
        this.speed = speed;
        count++;
    }
    void accel(int v) { speed += v; }
    int getSpeed() { return speed; }
}

public class Main {
    public static void main(String[] args) {
        Car a = new Car("A");
        Car b = new Car("B", 30);
        a.accel(10); b.accel(10);
        System.out.println(a.getSpeed() + " " + b.getSpeed() + " " + Car.count);  // 10 40 2
    }
}
```

## 상속과 오버라이딩 — 출력 문제의 핵심

```java
class Parent {
    int x = 10;
    Parent() { System.out.print("P "); }
    void show() { System.out.print("Parent "); }
    static void st() { System.out.print("PS "); }
}
class Child extends Parent {
    int x = 20;
    Child() { super(); System.out.print("C "); }  // super(): 부모 생성자 (생략해도 자동 호출)
    @Override
    void show() { System.out.print("Child "); }
    static void st() { System.out.print("CS "); }
}
public class Main {
    public static void main(String[] args) {
        Parent p = new Child();   // 출력: P C   (부모 생성자 → 자식 생성자)
        p.show();                 // Child   (오버라이딩된 메서드는 실제 객체 기준)
        System.out.print(p.x + " ");  // 10   (필드는 선언된 변수 타입 기준)
        p.st();                   // PS      (static 메서드는 변수 타입 기준)
    }
}
// 전체 출력: P C Child 10 PS
```

:::exam 업캐스팅 규칙 3줄
`Parent p = new Child();`일 때
1. **메서드**(인스턴스): 실제 객체(Child)의 오버라이딩된 메서드가 실행된다 — 동적 바인딩
2. **필드**: 변수 타입(Parent)의 필드가 사용된다
3. **static 메서드**: 변수 타입(Parent)의 것이 실행된다
:::

## 추상 클래스와 인터페이스

| 구분 | 추상 클래스 (abstract class) | 인터페이스 (interface) |
|---|---|---|
| 키워드 | `abstract class`, 자식은 `extends` | `interface`, 구현은 `implements` |
| 객체 생성 | 불가 | 불가 |
| 내용 | 일반 메서드 + 추상 메서드, 필드 | 추상 메서드, 상수(`public static final`), default·static 메서드 |
| 다중 | 단일 상속만 | **여러 개 구현 가능** |

```java
interface Shape { double area(); }
class Circle implements Shape {
    double r; Circle(double r) { this.r = r; }
    public double area() { return 3.14 * r * r; }
}
abstract class Animal {
    abstract String sound();
    void speak() { System.out.println(sound()); }
}
class Dog extends Animal { String sound() { return "멍멍"; } }
```

## 배열, 문자열, 컬렉션

```java
int[] a = {5, 3, 8};
int[][] m = new int[2][3];          // 모두 0으로 초기화
System.out.println(a.length);       // 3 (배열은 length 속성)

String s = "Hello";
System.out.println(s.length());     // 5 (문자열은 length() 메서드)
System.out.println(s.charAt(1));    // e
System.out.println(s.substring(1, 3)); // el  (1 이상 3 미만)
System.out.println(s.indexOf("l")); // 2
System.out.println(s.toUpperCase());// HELLO

String x = "java", y = "java", z = new String("java");
System.out.println(x == y);         // true  (같은 문자열 상수 풀)
System.out.println(x == z);         // false (다른 객체 주소)
System.out.println(x.equals(z));    // true  (내용 비교)
```

| 컬렉션 | 특징 |
|---|---|
| `ArrayList` | 순서 있음, 중복 허용, 인덱스 접근 |
| `LinkedList` | 순서 있음, 삽입·삭제 빠름 |
| `HashSet` | 중복 불가, 순서 없음 |
| `HashMap` | 키-값 쌍, 키 중복 불가 |

## 예외와 스레드 (개념)

- `try` → 예외 발생 시 해당 `catch` → `finally`는 항상 실행
- `throw`: 예외를 직접 발생, `throws`: 메서드 선언부에서 예외를 호출한 쪽으로 넘김
- **스레드**: `Thread` 클래스 상속 또는 `Runnable` 인터페이스 구현 후 `start()` 호출 (`run()`을 직접 부르면 새 스레드가 아님)

:::quiz
Q. 다음 Java 코드의 출력은?

```java
System.out.println(1 + 2 + "3" + 4 + 5);
```
1) 15
2) 3345
3) 12345
4) 339
> 정답 2 | 왼쪽부터: 1 + 2 = 3, 3 + "3" = "33", "33" + 4 = "334", "3345".

Q. 다음 코드의 출력은?

```java
class A { void f() { System.out.print("A"); } }
class B extends A { void f() { System.out.print("B"); } }
public class Main {
    public static void main(String[] args) {
        A obj = new B();
        obj.f();
    }
}
```
1) A
2) B
3) AB
4) 컴파일 오류
> 정답 2 | 오버라이딩된 메서드는 실제 객체(B)를 기준으로 실행된다.

Q. 같은 클래스 안에서 메서드 이름은 같지만 매개변수의 개수나 타입을 다르게 정의하는 것은?
1) 오버라이딩
2) 오버로딩
3) 캡슐화
4) 추상화
> 정답 2 | 오버로딩이다. 오버라이딩은 상속 관계에서 재정의.

Q. 다음 중 Java에서 여러 개를 동시에 구현할 수 있는 것은?
1) class
2) abstract class
3) interface
4) final class
> 정답 3 | 클래스 상속은 단일 상속만, 인터페이스는 다중 구현이 가능하다.

Q. 다음 코드의 출력은?

```java
String a = "hi";
String b = new String("hi");
System.out.print((a == b) + " " + a.equals(b));
```
1) true true
2) false true
3) true false
4) false false
> 정답 2 | ==는 주소 비교, equals는 내용 비교.

Q. 다음 코드의 출력은?

```java
class P { P() { System.out.print("1"); } }
class C extends P { C() { System.out.print("2"); } }
public class Main { public static void main(String[] args) { new C(); new C(); } }
```
1) 12
2) 1212
3) 22
4) 2121
> 정답 2 | 자식 객체를 만들 때마다 부모 생성자가 먼저 실행된다.

Q. 접근 제어자 중 같은 클래스에서만 접근할 수 있는 것은?
1) public
2) protected
3) default
4) private
> 정답 4 | private은 클래스 내부에서만 접근할 수 있다.
:::

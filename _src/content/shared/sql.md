## SQL의 분류

| 분류 | 명령어 | 용도 |
|---|---|---|
| DDL (정의어) | CREATE, ALTER, DROP, TRUNCATE, RENAME | 테이블·뷰·인덱스 등 구조 정의 |
| DML (조작어) | SELECT, INSERT, UPDATE, DELETE | 데이터 조회·조작 |
| DCL (제어어) | GRANT, REVOKE (+ COMMIT, ROLLBACK, SAVEPOINT를 DCL로 분류하기도) | 권한·트랜잭션 제어 |
| TCL | COMMIT, ROLLBACK, SAVEPOINT | 트랜잭션 제어 |

## DDL

```sql
CREATE TABLE 학생 (
    학번   CHAR(8)     PRIMARY KEY,
    이름   VARCHAR(20) NOT NULL,
    학과   VARCHAR(20),
    학년   INT         CHECK (학년 BETWEEN 1 AND 4),
    이메일 VARCHAR(50) UNIQUE,
    지도교수 CHAR(5),
    FOREIGN KEY (지도교수) REFERENCES 교수(교수번호)
        ON DELETE SET NULL ON UPDATE CASCADE
);

ALTER TABLE 학생 ADD 연락처 VARCHAR(15);        -- 열 추가
ALTER TABLE 학생 MODIFY 이름 VARCHAR(30);       -- 열 변경 (DBMS마다 ALTER COLUMN)
ALTER TABLE 학생 DROP COLUMN 연락처;            -- 열 삭제

DROP TABLE 학생 CASCADE;    -- 참조하는 객체까지 함께 삭제
DROP TABLE 학생 RESTRICT;   -- 참조하는 객체가 있으면 삭제 거부

CREATE VIEW 3학년 AS SELECT 학번, 이름 FROM 학생 WHERE 학년 = 3;
CREATE INDEX idx_이름 ON 학생(이름);
CREATE UNIQUE INDEX idx_mail ON 학생(이메일);
```

| 참조 옵션 | 부모 행 삭제·변경 시 자식 행 |
|---|---|
| CASCADE | 함께 삭제·변경 |
| SET NULL | NULL로 |
| SET DEFAULT | 기본값으로 |
| RESTRICT / NO ACTION | 자식이 있으면 거부 |

| 삭제 명령 비교 | DROP | TRUNCATE | DELETE |
|---|---|---|---|
| 분류 | DDL | DDL | DML |
| 대상 | 구조 + 데이터 | 데이터 전체 (구조 유지) | 조건에 맞는 행 |
| 롤백 | 불가 | 불가 | 가능 |

## DML: 조회 (SELECT)

```sql
SELECT [DISTINCT] 열 [AS 별칭]
  FROM 테이블
 WHERE 조건
 GROUP BY 열
HAVING 그룹 조건
 ORDER BY 열 [ASC | DESC];
```

:::fig order

| 조건 연산자 | 예 |
|---|---|
| 비교 | `학년 >= 3`, `학과 <> '경영'` |
| BETWEEN | `점수 BETWEEN 80 AND 90` (양 끝 포함) |
| IN | `학과 IN ('컴공', '전자')` |
| LIKE | `이름 LIKE '김%'` (김으로 시작), `'_수%'` (두 번째 글자가 수) |
| IS NULL | `이메일 IS NULL` (`= NULL`은 틀림) |
| AND, OR, NOT | NOT → AND → OR 순으로 처리 |

```sql
-- 학과별 평균 점수가 80 이상인 학과, 평균 내림차순
SELECT 학과, COUNT(*) AS 인원, AVG(점수) AS 평균
  FROM 성적
 WHERE 학년 >= 2
 GROUP BY 학과
HAVING AVG(점수) >= 80
 ORDER BY 평균 DESC;
```

| 집계 함수 | 설명 |
|---|---|
| COUNT(*) | 행 수 (NULL 포함) |
| COUNT(열) | NULL이 아닌 값의 수 |
| SUM, AVG, MAX, MIN | NULL 제외하고 계산 |
| STDDEV, VARIANCE | 표준편차, 분산 |

## 조인

:::fig join

```sql
-- 내부 조인 (동등 조인)
SELECT S.이름, D.학과명
  FROM 학생 S INNER JOIN 학과 D ON S.학과코드 = D.학과코드;
-- 같은 의미: FROM 학생 S, 학과 D WHERE S.학과코드 = D.학과코드

-- 자연 조인: 같은 이름의 열로 자동 조인, 중복 열은 하나만
SELECT * FROM 학생 NATURAL JOIN 학과;

-- 외부 조인: 짝이 없어도 왼쪽(학생)은 모두 출력
SELECT S.이름, D.학과명
  FROM 학생 S LEFT OUTER JOIN 학과 D ON S.학과코드 = D.학과코드;

-- 셀프 조인: 같은 테이블끼리
SELECT A.이름 AS 사원, B.이름 AS 상사
  FROM 사원 A JOIN 사원 B ON A.상사번호 = B.사원번호;

-- 교차 조인: 모든 조합 (행 수 = 곱)
SELECT * FROM 학생 CROSS JOIN 과목;
```

| 조인 종류 | 결과 |
|---|---|
| 동등 조인 (Equi Join) | `=` 조건으로 결합 |
| 비동등 조인 (Non-Equi) | `>`, `BETWEEN` 등으로 결합 |
| 자연 조인 (Natural) | 동등 조인 결과에서 중복 열 제거 |
| 외부 조인 (Outer) | LEFT, RIGHT, FULL. 짝 없는 행도 NULL로 포함 |
| 세타 조인 (Theta) | 비교 연산자(=, <, > …)를 사용한 조인의 총칭 |

## 서브쿼리와 집합 연산

```sql
-- 단일 행 서브쿼리
SELECT 이름 FROM 학생 WHERE 점수 > (SELECT AVG(점수) FROM 학생);

-- 다중 행 서브쿼리
SELECT 이름 FROM 학생 WHERE 학과코드 IN (SELECT 학과코드 FROM 학과 WHERE 건물 = '공학관');
SELECT 이름 FROM 학생 WHERE 점수 > ALL (SELECT 점수 FROM 학생 WHERE 학과 = '경영');  -- 최댓값보다 큼
SELECT 이름 FROM 학생 WHERE 점수 > ANY (SELECT 점수 FROM 학생 WHERE 학과 = '경영');  -- 최솟값보다 큼

-- 상관 서브쿼리 + EXISTS
SELECT D.학과명 FROM 학과 D
 WHERE EXISTS (SELECT 1 FROM 학생 S WHERE S.학과코드 = D.학과코드);
```

| 집합 연산자 | 의미 |
|---|---|
| UNION | 합집합, 중복 제거 |
| UNION ALL | 합집합, 중복 포함 |
| INTERSECT | 교집합 |
| EXCEPT (MINUS) | 차집합 |

## DML: 삽입·수정·삭제

```sql
INSERT INTO 학생 (학번, 이름, 학과, 학년) VALUES ('20260001', '홍길동', '컴공', 1);
INSERT INTO 졸업생 SELECT * FROM 학생 WHERE 학년 = 4;      -- 서브쿼리로 여러 행

UPDATE 학생 SET 학년 = 학년 + 1 WHERE 학과 = '컴공';
DELETE FROM 학생 WHERE 학번 = '20260001';
```

:::warn 시험에 자주 나오는 문법 함정
- `UPDATE 테이블 **SET** 열 = 값` — SET 빠뜨리기
- `DELETE **FROM** 테이블` — 표준 SQL은 FROM 필요
- `INSERT INTO 테이블(열) **VALUES** (값)` — VALUES 철자
- 문자열은 작은따옴표 `'홍길동'`, 숫자는 따옴표 없이
- WHERE 없는 UPDATE·DELETE는 **모든 행**에 적용
:::

## DCL과 TCL

```sql
GRANT SELECT, INSERT ON 학생 TO kim;                    -- 권한 부여
GRANT ALL ON 학생 TO lee WITH GRANT OPTION;             -- 받은 권한을 남에게 줄 수 있음
REVOKE INSERT ON 학생 FROM kim;                         -- 권한 회수
REVOKE ALL ON 학생 FROM lee CASCADE;                    -- lee가 준 권한까지 연쇄 회수

COMMIT;                -- 확정
SAVEPOINT A;           -- 저장점
ROLLBACK TO A;         -- 저장점까지 취소
ROLLBACK;              -- 마지막 COMMIT 이후 전체 취소
```

## 절차형 SQL

| 종류 | 설명 |
|---|---|
| 프로시저 (Procedure) | 일련의 SQL 작업을 묶어 저장. `EXECUTE`(CALL)로 호출. 반환값 없음(출력 매개변수 가능) |
| 사용자 정의 함수 (Function) | 결과 값을 **반드시 RETURN**. SQL 문 안에서 호출 가능 |
| 트리거 (Trigger) | 삽입·갱신·삭제 같은 **이벤트가 발생하면 자동 실행**. 트리거 안에서는 **DCL(COMMIT, ROLLBACK) 사용 불가** |
| 커서 (Cursor) | 쿼리 결과 행을 하나씩 처리하기 위한 포인터. 선언(DECLARE) → OPEN → FETCH → CLOSE |

```sql
CREATE OR REPLACE PROCEDURE 학년올리기 (p_학과 IN VARCHAR2)
IS
BEGIN
    UPDATE 학생 SET 학년 = 학년 + 1 WHERE 학과 = p_학과;
    COMMIT;
EXCEPTION
    WHEN OTHERS THEN ROLLBACK;
END;

CREATE OR REPLACE TRIGGER trg_로그
AFTER INSERT ON 학생
FOR EACH ROW
BEGIN
    INSERT INTO 로그 VALUES (:NEW.학번, SYSDATE);
END;
```

| 쿼리 성능 | 설명 |
|---|---|
| 옵티마이저 | SQL 실행 계획을 세움. 규칙 기반(RBO), 비용 기반(CBO) |
| 힌트 (Hint) | 옵티마이저에게 실행 방법을 지시 |
| 실행 계획 (Explain Plan) | 쿼리가 어떤 순서·방법으로 실행되는지 확인 |

:::quiz
Q. 다음 중 DDL에 해당하지 않는 것은?
1) CREATE
2) ALTER
3) DROP
4) UPDATE
> 정답 4 | UPDATE는 DML이다.

Q. 학생 테이블에서 이름이 '이'로 시작하는 학생을 조회하는 조건은?
1) 이름 = '이%'
2) 이름 LIKE '이%'
3) 이름 LIKE '%이'
4) 이름 IN '이%'
> 정답 2 | %는 0개 이상 임의 문자. '%이'는 이로 끝나는 이름.

Q. 다음 SQL에서 빈칸에 들어갈 키워드는?

```sql
SELECT 학과, AVG(점수) FROM 성적 GROUP BY 학과 (    ) AVG(점수) >= 80;
```
1) WHERE
2) HAVING
3) ORDER BY
4) ON
> 정답 2 | 그룹에 대한 조건은 HAVING에 쓴다.

Q. 권한을 회수할 때 사용하는 명령은?
1) GRANT
2) REVOKE
3) DELETE
4) ROLLBACK
> 정답 2 | REVOKE ... FROM 사용자.

Q. 이벤트가 발생할 때 자동으로 실행되며, 내부에서 COMMIT·ROLLBACK을 사용할 수 없는 절차형 SQL은?
1) 프로시저
2) 사용자 정의 함수
3) 트리거
4) 커서
> 정답 3 | 트리거다.

Q. 다음 SQL의 실행 결과 행 수는? (학생 5행, 과목 4행)

```sql
SELECT * FROM 학생 CROSS JOIN 과목;
```
1) 4
2) 5
3) 9
4) 20
> 정답 4 | 교차 조인은 5 × 4 = 20행.

Q. 테이블의 구조는 유지하면서 모든 행을 삭제하고, 롤백할 수 없는 명령은?
1) DROP
2) TRUNCATE
3) DELETE
4) ALTER
> 정답 2 | TRUNCATE. DELETE는 롤백 가능, DROP은 구조까지 삭제.

Q. 다음 SQL에서 문법 오류가 있는 부분은?

```sql
UPDATE 학생 학년 = 2 WHERE 학번 = '1001';
```
1) UPDATE 학생
2) 학년 = 2 앞에 SET이 없음
3) WHERE 학번 = '1001'
4) 오류 없음
> 정답 2 | `UPDATE 학생 SET 학년 = 2 ...`가 맞다.
:::

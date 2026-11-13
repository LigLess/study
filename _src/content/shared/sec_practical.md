## 실기는 "쓰는" 시험이다

실기 출제 범위는 필기와 같다. 다른 점은 **보기 없이 직접 쓴다**는 것이다. 주요 항목은 시스템 및 네트워크 보안 특성 파악, 취약점 점검 및 보완, 보안관제 및 대응, 위험분석 및 정보보호 대책 수립 (2027년부터 최신 보안 동향 추가).

| 유형 | 요구 | 준비 방법 |
|---|---|---|
| 단답형 | 용어·명령어·설정값·포트 번호 | 키워드 카드로 반복 암기. 영문 약어와 풀네임 모두 |
| 서술형 | 원리·절차·대응 방안을 문장으로 | 아래 **답안 골격 4가지**로 연습 |
| 실무형 | 로그·패킷·설정 파일·소스 코드를 보고 분석·조치 | 실제 로그 형식을 눈에 익히기 |

## 서술형 답안 골격 4가지

| 골격 | 쓰는 순서 | 예시 문제 |
|---|---|---|
| **원리형** | ① 정의 → ② 동작 원리(단계) → ③ 결과·피해 | "SYN 플러딩의 원리를 설명하시오" |
| **대응형** | ① 원인 → ② 대응 방안 3가지 이상(기술적·관리적) → ③ 설정 예 | "SQL 삽입 대응 방안을 쓰시오" |
| **비교형** | 표 형식으로 기준별 비교 (정의·장점·단점·사용처) | "IDS와 IPS를 비교하시오" |
| **절차형** | 번호를 붙여 단계별 서술 | "침해사고 대응 절차를 쓰시오" |

:::ex 서술형 예시 답안 — SQL 삽입 대응
**원인**: 사용자 입력값을 검증 없이 SQL 문자열에 이어 붙여 쿼리를 만들기 때문.
**대응**
1. **Prepared Statement(바인드 변수)**를 사용해 입력값이 SQL 구문으로 해석되지 않게 한다.
2. 입력값의 길이·형식·허용 문자를 서버 측에서 검증하고, `'`, `--`, `;` 등 특수문자를 필터링한다.
3. DB 계정은 **최소 권한**으로 운영하고, 상세 DB 오류 메시지를 사용자에게 노출하지 않는다.
4. 웹 방화벽(WAF)으로 공격 패턴을 차단한다.
:::

## 실무형 연습: 로그와 설정 읽기

:::ex 리눅스 인증 로그 분석
```text
Nov  7 03:12:01 web sshd[2211]: Failed password for root from 203.0.113.7 port 51022 ssh2
Nov  7 03:12:03 web sshd[2213]: Failed password for root from 203.0.113.7 port 51024 ssh2
Nov  7 03:12:05 web sshd[2215]: Failed password for invalid user admin from 203.0.113.7 port 51026 ssh2
...(같은 IP에서 수백 건)
Nov  7 03:20:44 web sshd[2901]: Accepted password for root from 203.0.113.7 port 52210 ssh2
```
**분석**: 같은 IP에서 짧은 간격으로 로그인 실패가 반복된 뒤 root 로그인이 성공했다 → **무차별 대입(Brute Force) 공격 성공**.
**조치**: ① 해당 IP 차단 (`iptables -A INPUT -s 203.0.113.7 -j DROP`) ② root 비밀번호 즉시 변경 ③ `/etc/ssh/sshd_config`에 `PermitRootLogin no` ④ 비밀번호 대신 키 인증, 로그인 실패 잠금(pam_faillock), fail2ban ⑤ 침입 이후 행위(`last`, `.bash_history`, 새 계정·cron·SetUID 파일) 점검.
:::

:::ex 웹 접근 로그 분석
```text
198.51.100.9 - - [07/Nov/2026:10:01:12] "GET /board/view.php?id=1%27%20or%20%271%27=%271 HTTP/1.1" 200 5123
198.51.100.9 - - [07/Nov/2026:10:01:40] "GET /board/view.php?id=1 union select id,pw from member-- HTTP/1.1" 200 8812
198.51.100.9 - - [07/Nov/2026:10:05:02] "POST /upload.php HTTP/1.1" 200 120
198.51.100.9 - - [07/Nov/2026:10:05:10] "GET /upload/shell.php?cmd=cat%20/etc/passwd HTTP/1.1" 200 1820
```
**분석**: ① `' or '1'='1` → SQL 삽입 시도 ② `union select` → 회원 테이블 탈취 시도 (응답 크기 증가로 성공 추정) ③ 파일 업로드 후 `shell.php?cmd=` → **웹셸** 업로드·명령 실행.
**조치**: Prepared Statement 적용, 업로드 확장자 허용 목록·실행 권한 제거·웹 루트 밖 저장, 웹셸 삭제, 회원 비밀번호 초기화, WAF 정책 추가.
:::

:::ex 방화벽 정책 순서
```text
1  allow  any            → 10.0.0.10  tcp/80
2  deny   203.0.113.0/24 → any        any
3  allow  10.0.1.0/24    → 10.0.0.20  tcp/22
4  deny   any            → any        any
```
**문제점**: 1번 규칙이 먼저 일치하므로 203.0.113.0/24도 웹 서버 80번에 접근할 수 있다. 차단 규칙(2번)을 **1번보다 위로** 올려야 한다. 규칙은 위에서부터 처음 일치한 것이 적용된다.
:::

## 단답형 키워드 점검

:::quiz
Q. 리눅스에서 사용자가 실행한 모든 명령을 기록하며 lastcomm으로 확인하는 로그 파일은?
1) wtmp
2) pacct
3) secure
4) lastlog
> 정답 2 | pacct(프로세스 계정 로그).

Q. 다음 tcpdump 출력이 나타내는 상태로 가장 적절한 것은? (같은 출발지 포트가 계속 바뀌며 반복)

```text
IP 198.51.100.x.40001 > 10.0.0.5.80: Flags [S]
IP 198.51.100.y.40002 > 10.0.0.5.80: Flags [S]
IP 198.51.100.z.40003 > 10.0.0.5.80: Flags [S]
(ACK 없이 SYN만 수천 건)
```
1) ARP 스푸핑
2) SYN 플러딩
3) DNS 증폭
4) 세션 하이재킹
> 정답 2 | SYN만 대량으로 오고 3-way handshake가 완료되지 않는다.

Q. Snort 규칙에서 대소문자를 구분하지 않고 문자열을 검사하게 하는 옵션은?
1) content
2) nocase
3) offset
4) depth
> 정답 2 | nocase.

Q. Apache에서 응답 헤더의 서버 버전 정보를 최소화하는 설정은?
1) ServerTokens Prod
2) Options -Indexes
3) ServerSignature On
4) KeepAlive Off
> 정답 1 | ServerTokens Prod. ServerSignature Off도 함께 설정한다.

Q. 웹 로그에서 `/upload/a.jsp?cmd=whoami` 같은 요청이 보일 때 가장 의심되는 공격은?
1) XSS
2) 웹셸
3) CSRF
4) 디렉터리 리스팅
> 정답 2 | 업로드된 스크립트로 시스템 명령을 실행하는 웹셸이다.

Q. SSH 설정에서 root 계정의 원격 로그인을 막는 항목은?
1) PermitRootLogin no
2) PasswordAuthentication yes
3) Port 2222
4) AllowUsers root
> 정답 1 | `/etc/ssh/sshd_config`의 PermitRootLogin no.
:::

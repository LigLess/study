## 운영체제와 보안의 기본

| 보안 목표 | 의미 |
|---|---|
| 기밀성 | 인가된 사용자만 정보에 접근 |
| 무결성 | 인가된 방법으로만 정보 변경 |
| 가용성 | 필요할 때 언제든 사용 |
| 인증성·책임추적성·부인방지 | 신원 확인, 행위 추적, 행위 부인 불가 |

**운영체제 보안 요소**: 사용자 인증, 접근 통제, 감사(로그), 파일 시스템 보호, 메모리 보호.

**참조 모니터(Reference Monitor)**: 주체(사용자·프로세스)가 객체(파일·자원)에 접근할 때마다 권한을 확인하는 추상 개념. 조건 — **우회 불가**(항상 호출), **변조 불가**, **검증 가능**(작아서 분석 가능). 이를 구현한 것이 **보안 커널**, 보안 기능 전체 집합이 **TCB**(신뢰 컴퓨팅 기반).

### 메모리 보호와 공격

| 공격·보호 | 설명 |
|---|---|
| 버퍼 오버플로 | 버퍼 크기를 넘는 입력으로 복귀 주소를 덮어써 악성 코드 실행. **스택** 버퍼 오버플로, **힙** 버퍼 오버플로 |
| 포맷 스트링 공격 | `printf(input)`처럼 서식 문자열을 사용자 입력 그대로 써서 `%x`, `%n`으로 메모리 읽기·쓰기 |
| 레이스 컨디션 | 임시 파일 생성 시점과 사용 시점 사이를 노려 심볼릭 링크로 바꿔치기 (TOCTOU) |
| 스택 가드 (카나리) | 복귀 주소 앞에 임의 값을 두고 변조를 감지 |
| 스택 실드 | 복귀 주소를 별도 영역에 복사해 두고 비교 |
| **ASLR** | 스택·힙·라이브러리 주소를 실행할 때마다 무작위로 |
| **DEP / NX 비트** | 스택·힙 영역에서 코드 실행 금지 |
| 안전한 함수 | strcpy → **strncpy**, strcat → strncat, gets → **fgets**, sprintf → snprintf |

## 유닉스·리눅스 보안

### 계정과 패스워드

| 파일 | 내용 |
|---|---|
| `/etc/passwd` | `사용자:x:UID:GID:설명:홈:셸` 7필드. 누구나 읽기 가능 |
| `/etc/shadow` | 암호화된 비밀번호와 기간 정보. **root만** 읽기. 권한 400(또는 000) |
| `/etc/group` | 그룹 정보 |
| `/etc/login.defs` | 비밀번호 최소 길이·사용 기간 기본값 |
| `/etc/pam.d/` | PAM(플러그형 인증 모듈) 설정. 비밀번호 복잡도(pam_pwquality), 로그인 실패 잠금(pam_faillock / pam_tally2) |

- UID 0 = root. **root 외에 UID 0인 계정**이 있으면 백도어 의심
- shadow 비밀번호 필드: `$1$` MD5, `$5$` SHA-256, `$6$` **SHA-512**, `$y$` yescrypt. `!`·`*`는 잠긴 계정
- 불필요한 계정의 셸은 `/sbin/nologin` 또는 `/bin/false`

### 파일 권한과 특수 권한

| 권한 | 숫자 | 의미 | 보안 위험 |
|---|---|---|---|
| SetUID | 4000 | 실행하는 동안 **파일 소유자** 권한 (예: passwd) | root 소유 SetUID 파일은 권한 상승 경로 |
| SetGID | 2000 | 실행 중 그룹 소유자 권한 / 디렉터리 그룹 상속 | |
| Sticky Bit | 1000 | 자기 파일만 삭제 가능 (/tmp) | |

```bash
# find / -user root -perm -4000 -type f 2>/dev/null   # root 소유 SetUID 파일 점검
# find / -perm -2 -type f 2>/dev/null                 # 누구나 쓸 수 있는 파일 (world writable)
# chmod 400 /etc/shadow
# umask 022                                           # 새 파일 644, 디렉터리 755
```

### 로그 파일

| 로그 | 내용 | 확인 |
|---|---|---|
| `/var/log/messages` (데비안 `syslog`) | 시스템 전반 로그 | 텍스트 |
| `/var/log/secure` (데비안 `auth.log`) | **인증·로그인·su·sudo** 기록 | 텍스트 |
| **utmp** (`/var/run/utmp`) | **현재 로그인** 사용자 | `w`, `who`, `users` |
| **wtmp** (`/var/log/wtmp`) | **로그인·로그아웃 이력**, 재부팅 | `last` |
| **btmp** (`/var/log/btmp`) | **로그인 실패** 기록 | `lastb` |
| lastlog | 사용자별 **마지막 로그인** | `lastlog` |
| pacct | 사용자가 실행한 **모든 명령** (프로세스 계정) | `lastcomm` |
| `.bash_history` | 사용자 명령 이력 | 텍스트 |
| `/var/log/xferlog` | FTP 파일 전송 | 텍스트 |
| sulog | su 명령 기록 | 텍스트 |
| dmesg | 부팅 시 커널 메시지 | `dmesg` |

**syslog 설정** `/etc/rsyslog.conf`: `facility.priority  action` 형식. 예) `authpriv.*  /var/log/secure`, `*.emerg  *`.
우선순위(높음 → 낮음): **emerg > alert > crit > err > warning > notice > info > debug**.

### 서비스와 접근 통제

| 기능 | 파일·도구 |
|---|---|
| TCP Wrapper | `/etc/hosts.allow` → `/etc/hosts.deny` 순서로 검사. 예) `sshd: 192.168.1.` |
| inetd / xinetd | 슈퍼 데몬 설정 (`/etc/xinetd.d/`) |
| 방화벽 | iptables, firewalld, nftables, ufw |
| 원격 접속 제한 | `/etc/ssh/sshd_config`의 `PermitRootLogin no`, `PasswordAuthentication no` |
| cron 접근 제어 | `/etc/cron.allow`, `/etc/cron.deny` |
| 무결성 검사 | Tripwire, AIDE (파일 해시를 저장해 두고 변조 탐지) |

```bash
# iptables -A INPUT -p tcp --dport 22 -s 10.0.0.0/24 -j ACCEPT
# iptables -A INPUT -p tcp --dport 22 -j DROP
# iptables -L -n --line-numbers
```

iptables 체인: **INPUT**(들어오는), **OUTPUT**(나가는), **FORWARD**(통과하는). 타깃: ACCEPT, DROP(응답 없이 버림), REJECT(거부 응답).

## 윈도우 보안

| 요소 | 설명 |
|---|---|
| **SAM** | 계정·비밀번호 해시(NTLM) 저장 데이터베이스 (`%SystemRoot%\System32\config\SAM`) |
| **LSA** | 로컬 보안 인증. 로그인 검증, 보안 정책, 감사 로그 생성 |
| **SRM** | 보안 참조 모니터. 접근 권한 검사, 액세스 토큰 발급 |
| SID | 계정 고유 식별자. **RID 500 = Administrator**, 501 = Guest, 일반 사용자 1000 이상 |
| 액세스 토큰 | 로그인 시 발급되는 권한 정보 |
| ACL (DACL, SACL) | 객체 접근 권한 목록 / 감사 설정 |
| UAC | 관리자 권한이 필요할 때 사용자에게 확인 |
| BitLocker / EFS | 드라이브 전체 암호화 / 파일 단위 암호화 |
| 레지스트리 | 시스템 설정 DB. HKLM, HKCU, HKCR, HKU, HKCC. 악성코드 자동 실행 위치: `...\CurrentVersion\Run` |

| 이벤트 로그 | 내용 |
|---|---|
| 응용 프로그램 | 프로그램 오류·정보 |
| 보안 | 로그온 성공·실패, 권한 사용, 개체 접근 (감사 정책 설정 필요). 이벤트 ID **4624 로그온 성공, 4625 실패**, 4634 로그오프, 4720 계정 생성 |
| 시스템 | 드라이버·서비스 |

**공유 폴더 보안**: 기본 관리 공유(C$, ADMIN$, IPC$) 제거·제한, `net share`로 확인. **NTFS 권한**이 FAT보다 세밀하다.

## 악성코드

| 종류 | 특징 |
|---|---|
| 바이러스 | 다른 파일에 기생, 숙주 필요. 부트·파일·매크로 바이러스. 1세대 원시형 → 2세대 암호형 → 3세대 은폐형(스텔스) → 4세대 갑옷형(아머드) → 5세대 매크로 |
| 웜 | 스스로 복제해 네트워크로 전파. 숙주 불필요 |
| 트로이 목마 | 정상 프로그램으로 위장. 자기 복제 없음 |
| 백도어 | 인증 없이 접근하는 비밀 통로 |
| 루트킷 | 공격 흔적·악성 프로세스를 숨기는 도구 모음 |
| 랜섬웨어 | 파일 암호화 후 금전 요구 |
| 봇넷 | 감염된 좀비 PC 네트워크, C&C 서버가 명령 |
| 스파이웨어 / 애드웨어 | 정보 수집 / 광고 |
| 파일리스 악성코드 | 파일 없이 메모리·PowerShell·레지스트리에서 동작 |
| 키로거 | 키 입력 탈취 |

**악성코드 분석**: **정적 분석**(실행하지 않고 코드·문자열·헤더 분석, 디스어셈블러 IDA), **동적 분석**(가상 환경·샌드박스에서 실행하며 행위 관찰). 패킹(실행 압축, UPX)을 풀어야 분석이 가능한 경우가 많다.

## 클라우드·가상화·IoT·모바일 보안

| 영역 | 주요 위협·대책 |
|---|---|
| 클라우드 | **책임 공유 모델**(IaaS는 고객 책임이 크고, SaaS로 갈수록 제공자 책임이 커짐), 잘못된 설정, 접근 키 유출, CASB, CSPM |
| 컨테이너 | 취약한 이미지, 권한 상승(privileged 컨테이너), 이미지 스캔, 최소 권한 |
| 가상화 | VM 탈출(VM Escape), 하이퍼바이저 보안 |
| IoT | 기본 비밀번호, 펌웨어 취약점, 미라이(Mirai) 봇넷 |
| 모바일 | 루팅·탈옥, 악성 앱, 앱 위변조. 안드로이드 권한 모델, iOS 샌드박스 |

## 시스템 보안 점검·대응 도구

| 도구 | 용도 |
|---|---|
| Nmap | 포트·서비스·OS 스캐닝 |
| Nessus, OpenVAS | 취약점 스캐너 |
| Tripwire, AIDE | 파일 무결성 점검 |
| tcpdump, Wireshark | 패킷 캡처·분석 |
| Snort, Suricata | 네트워크 IDS/IPS |
| EDR | 단말의 이상 행위 탐지·대응 |
| John the Ripper, Hashcat | 패스워드 크래킹 (점검용) |
| lsof, netstat, ss, ps | 열린 파일·포트·프로세스 확인 |

:::quiz
Q. 리눅스에서 로그인 실패 기록을 저장하며 lastb 명령으로 확인하는 로그는?
1) utmp
2) wtmp
3) btmp
4) lastlog
> 정답 3 | btmp. wtmp는 로그인·로그아웃 이력(last), utmp는 현재 로그인(w, who).

Q. 실행하는 동안 파일 소유자의 권한으로 동작하게 하는 특수 권한은?
1) SetUID
2) SetGID
3) Sticky Bit
4) umask
> 정답 1 | SetUID(4000). root 소유 SetUID 파일은 점검 대상이다.

Q. 프로세스의 스택·힙·라이브러리 주소를 실행할 때마다 무작위로 배치하는 기법은?
1) DEP
2) ASLR
3) 스택 가드
4) 카나리
> 정답 2 | ASLR이다. DEP는 데이터 영역의 코드 실행을 막는다.

Q. 윈도우에서 계정과 비밀번호 해시를 저장하는 데이터베이스는?
1) LSA
2) SAM
3) SRM
4) SID
> 정답 2 | SAM이다.

Q. syslog 우선순위 중 가장 높은 것은?
1) crit
2) alert
3) emerg
4) err
> 정답 3 | emerg > alert > crit > err > warning > notice > info > debug.

Q. 자기 복제 기능이 없고 정상 프로그램으로 위장하는 악성코드는?
1) 바이러스
2) 웜
3) 트로이 목마
4) 봇
> 정답 3 | 트로이 목마는 자기 복제를 하지 않는다.

Q. 참조 모니터가 만족해야 하는 조건이 아닌 것은?
1) 우회 불가
2) 변조 불가
3) 검증 가능
4) 암호화 필수
> 정답 4 | 우회 불가, 변조 불가, 검증 가능.

Q. 윈도우 보안 이벤트 로그에서 로그온 실패를 뜻하는 이벤트 ID는?
1) 4624
2) 4625
3) 4634
4) 4720
> 정답 2 | 4624 성공, 4625 실패, 4634 로그오프, 4720 계정 생성.

Q. TCP Wrapper에서 먼저 검사하는 파일은?
1) /etc/hosts.deny
2) /etc/hosts.allow
3) /etc/inetd.conf
4) /etc/services
> 정답 2 | hosts.allow를 먼저 보고, 없으면 hosts.deny를 본다.

Q. 클라우드 책임 공유 모델에서 고객의 보안 책임이 가장 큰 서비스 모델은?
1) SaaS
2) PaaS
3) IaaS
4) 모두 같다
> 정답 3 | IaaS는 OS부터 고객이 관리한다.
:::

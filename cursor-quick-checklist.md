# Cursor 환경 복제 빠른 체크리스트

## 📥 백업 (기존 계정에서)

### 자동 백업 (추천)
```powershell
cd "c:\Users\sharp\OneDrive\문서\gitLocal\report"
.\cursor-backup.ps1
```

### 수동 백업
- [ ] `%APPDATA%\Cursor\User\settings.json` 복사
- [ ] `%APPDATA%\Cursor\User\keybindings.json` 복사
- [ ] 확장 프로그램 목록 내보내기: `code --list-extensions > extensions-list.txt`
- [ ] `C:\Users\sharp\.cursor\skills-cursor\` 폴더 복사
- [ ] 프로젝트 `.cursor\rules\` 폴더 복사
- [ ] `%APPDATA%\Cursor\User\globalStorage\` 복사

---

## 📤 복원 (새 계정에서)

### 자동 복원 (추천)
```powershell
.\cursor-restore.ps1 -BackupPath ".\cursor-backup-20260306-123456"
```

### 수동 복원
- [ ] settings.json → `%APPDATA%\Cursor\User\`
- [ ] keybindings.json → `%APPDATA%\Cursor\User\`
- [ ] 확장 프로그램 설치: `Get-Content extensions-list.txt | ForEach-Object { code --install-extension $_ }`
- [ ] skills-cursor → `C:\Users\새계정\.cursor\skills-cursor\`
- [ ] project-cursor-rules → 프로젝트 폴더
- [ ] globalStorage → `%APPDATA%\Cursor\User\`

---

## ✅ 복원 후 확인사항

- [ ] Cursor 재시작
- [ ] 테마/폰트 확인
- [ ] 키바인딩 작동 (Ctrl+I)
- [ ] 확장 프로그램 활성화
- [ ] Python 경로 수정 (필요시)
- [ ] Git 사용자 정보 설정
- [ ] SSH 서버 주소 확인
- [ ] Cursor Rules 인식 확인
- [ ] Agent Skills 사용 가능 확인
- [ ] MCP 서버 연결 확인

---

## 🛠️ 추가 설정

### Git 설정
```powershell
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Python 경로 (settings.json에서 수정)
```json
"python.defaultInterpreterPath": "새경로/python3.11.exe"
```

### SSH 서버 (settings.json에서 수정)
```json
"remote.SSH.remotePlatform": {
    "서버주소": "linux"
}
```

---

## 📂 주요 파일 경로

### Windows
```
설정: %APPDATA%\Cursor\User\
스킬: C:\Users\계정명\.cursor\skills-cursor\
규칙: 프로젝트\.cursor\rules\
MCP: %APPDATA%\Cursor\User\globalStorage\
```

### PowerShell 변수
```powershell
$env:APPDATA\Cursor\User\
$env:USERPROFILE\.cursor\
$env:LOCALAPPDATA\Programs\Cursor\
```

---

## 🔧 문제 해결

### 설정이 적용 안 됨
→ Cursor 완전 종료 후 재시작 (작업 관리자 확인)

### 확장 프로그램 설치 실패
→ 인터넷 연결 확인, 개별 재설치

### Skills 인식 안 됨
→ 경로 확인, Cursor 재시작

### MCP 서버 연결 안 됨
→ MCP 서버 재설치 또는 설정 재확인

---

## 📞 백업/복원 스크립트 옵션

### 백업 옵션
```powershell
# 기본 백업
.\cursor-backup.ps1

# 특정 경로에 백업
.\cursor-backup.ps1 -BackupPath "D:\Backups\cursor-20260306"
```

### 복원 옵션
```powershell
# 전체 복원
.\cursor-restore.ps1 -BackupPath ".\cursor-backup-20260306-123456"

# 확장 프로그램 제외
.\cursor-restore.ps1 -BackupPath "경로" -SkipExtensions

# MCP 설정 제외
.\cursor-restore.ps1 -BackupPath "경로" -SkipMCP

# 확장 프로그램과 MCP 모두 제외
.\cursor-restore.ps1 -BackupPath "경로" -SkipExtensions -SkipMCP
```

---

## 📋 백업 항목 상세

### 1. settings.json (602 bytes)
- 자동 저장 설정
- SSH 원격 플랫폼
- Python 경로
- Copilot 설정
- Git 설정

### 2. keybindings.json (356 bytes)
- Ctrl+I: Composer 에이전트 모드
- Ctrl+Alt+S: 사이드바 토글

### 3. 확장 프로그램 (20개)
- GitHub Copilot
- Python 지원
- Jupyter Notebook
- Remote SSH
- C/C++ 지원
- CMake 지원
- ROS 지원
- 한국어 언어팩

### 4. Agent Skills (5개)
- create-rule
- create-skill
- create-subagent
- migrate-to-skills
- update-cursor-settings

### 5. Cursor Rules (44개 파일)
- 프로젝트별 규칙
- 컨텍스트 기반 워크플로우
- PDF 변환 가이드

### 6. MCP 서버 (5개)
- Sequential Thinking
- Notion
- context7-mcp
- playwright
- desktop-commander

---

## 💾 정기 백업 자동화

### Windows 작업 스케줄러
```powershell
$trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Sunday -At 2am
$action = New-ScheduledTaskAction -Execute "PowerShell.exe" -Argument "-File `"C:\경로\cursor-backup.ps1`""
Register-ScheduledTask -TaskName "Cursor Weekly Backup" -Trigger $trigger -Action $action
```

### OneDrive 동기화
```powershell
# 설정을 OneDrive로 이동
Move-Item -Path "$env:APPDATA\Cursor\User\settings.json" -Destination "$env:OneDrive\CursorSettings\"

# 심볼릭 링크 생성
New-Item -ItemType SymbolicLink -Path "$env:APPDATA\Cursor\User\settings.json" -Target "$env:OneDrive\CursorSettings\settings.json"
```

---

## 📝 백업 권장 주기

- **설정 파일**: 변경 시마다
- **확장 프로그램**: 새로 설치 시
- **Skills/Rules**: 생성/수정 시
- **전체 백업**: 주 1회 또는 월 1회

---

## 🚨 중요 참고사항

1. **계정명 차이**: 새 계정의 사용자명이 다를 수 있음
2. **Python 경로**: 환경에 맞게 수정 필요
3. **SSH 서버**: 접근 가능한 서버인지 확인
4. **Git 설정**: 별도로 구성 필요
5. **라이센스**: Copilot 등 유료 확장은 재인증 필요

---

**마지막 업데이트**: 2026-03-06  
**버전**: 1.0  
**작성자**: sharp

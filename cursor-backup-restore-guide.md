# Cursor 완전 복제 가이드

새로운 계정에서 현재 Cursor 환경을 동일하게 세팅하는 방법입니다.

## 📋 백업할 항목 요약

1. **설정 파일** (settings.json, keybindings.json)
2. **확장 프로그램** (20개)
3. **Cursor Rules** (44개 파일)
4. **Agent Skills** (5개 스킬)
5. **MCP 서버 설정**
6. **워크스페이스 설정**

---

## 🔧 단계 1: 기존 계정에서 백업 실행

### 방법 A: 자동 백업 스크립트 사용 (추천)

아래 백업 스크립트를 실행하면 모든 파일을 한 번에 백업합니다:

```powershell
# PowerShell에서 실행
.\cursor-backup.ps1
```

백업 완료 후 생성되는 폴더: `cursor-backup-YYYYMMDD-HHMMSS`

### 방법 B: 수동 백업

각 항목을 개별적으로 복사하려면 아래 체크리스트를 따르세요.

---

## 📦 백업 체크리스트 (수동)

### 1. 설정 파일 백업 ✅

**위치**: `C:\Users\sharp\AppData\Roaming\Cursor\User\`

복사할 파일:
- ✅ `settings.json` (602 bytes)
- ✅ `keybindings.json` (356 bytes)

**현재 주요 설정**:
- 자동 저장: afterDelay
- SSH 원격 플랫폼 설정
- Python 기본 인터프리터 경로
- GitHub Copilot 활성화
- Git 자동 커밋 활성화

---

### 2. 확장 프로그램 목록 백업 ✅

**설치된 확장 프로그램 (20개)**:

```
github.copilot
github.copilot-chat
mechatroner.rainbow-csv
ms-ceintl.vscode-language-pack-ko
ms-iot.vscode-ros
ms-python.debugpy
ms-python.python
ms-python.vscode-pylance
ms-python.vscode-python-envs
ms-toolsai.jupyter
ms-toolsai.jupyter-keymap
ms-toolsai.jupyter-renderers
ms-toolsai.vscode-jupyter-cell-tags
ms-toolsai.vscode-jupyter-slideshow
ms-vscode-remote.remote-ssh
ms-vscode-remote.remote-ssh-edit
ms-vscode.cmake-tools
ms-vscode.cpptools
ms-vscode.remote-explorer
twxs.cmake
```

**백업 방법**:
```powershell
code --list-extensions > extensions-list.txt
```

---

### 3. Cursor Rules 백업 ✅

**위치**: 프로젝트 내 `.cursor/rules/` 폴더

총 44개의 규칙 파일이 있습니다:

**주요 규칙 파일**:
- `001-project-rules.mdc` - 프로젝트 기본 규칙
- `1001-context-plan.mdc` - 계획 단계 규칙
- `1002-context-act.mdc` - 실행 단계 규칙
- `1003-context-reflect.mdc` - 회고 단계 규칙
- `1004-context-test.mdc` - 테스트 단계 규칙
- `004-project-workflow.mdc` - 워크플로우 규칙
- `pdf-to-md-guide.mdc` - PDF 변환 가이드

**백업 방법**:
```powershell
# 프로젝트 폴더 전체를 백업하면 자동으로 포함됩니다
# 또는 개별 복사:
Copy-Item -Path "프로젝트경로\.cursor" -Destination "백업경로\.cursor" -Recurse
```

---

### 4. Agent Skills 백업 ✅

**위치**: `C:\Users\sharp\.cursor\skills-cursor\`

**설치된 스킬 (5개)**:
1. `create-rule` - Cursor 규칙 생성
2. `create-skill` - Agent Skill 생성
3. `create-subagent` - 서브에이전트 생성
4. `migrate-to-skills` - 스킬 마이그레이션
5. `update-cursor-settings` - Cursor 설정 업데이트

**백업 방법**:
```powershell
Copy-Item -Path "C:\Users\sharp\.cursor\skills-cursor" -Destination "백업경로\skills-cursor" -Recurse
```

---

### 5. MCP 서버 설정 백업 ✅

**위치**: `C:\Users\sharp\AppData\Roaming\Cursor\User\globalStorage\`

**현재 활성 MCP 서버**:
- Sequential Thinking
- Notion
- context7-mcp (라이브러리 문서 조회)
- playwright (브라우저 자동화)
- desktop-commander (데스크톱 제어)

**백업 방법**:
```powershell
Copy-Item -Path "$env:APPDATA\Cursor\User\globalStorage" -Destination "백업경로\globalStorage" -Recurse
```

---

### 6. 워크스페이스 설정 백업 ✅

프로젝트 폴더 자체를 백업하면 다음이 포함됩니다:
- `.cursor/` 폴더
- `.vscode/` 폴더 (있는 경우)
- 프로젝트별 설정

---

## 🚀 단계 2: 새 계정에 복원 실행

### 방법 A: 자동 복원 스크립트 사용 (추천)

```powershell
# PowerShell에서 실행 (백업 폴더 경로 지정)
.\cursor-restore.ps1 -BackupPath ".\cursor-backup-20260306-123456"
```

### 방법 B: 수동 복원

아래 체크리스트를 따라 순서대로 복원하세요.

---

## 📥 복원 체크리스트 (수동)

### 1단계: Cursor 설치 확인 ✅
- 새 계정에 Cursor가 설치되어 있는지 확인
- 설치 안 되어 있으면 [cursor.sh](https://cursor.sh) 에서 다운로드

### 2단계: 설정 파일 복원 ✅

```powershell
# settings.json 복사
Copy-Item -Path "백업경로\settings.json" -Destination "$env:APPDATA\Cursor\User\settings.json" -Force

# keybindings.json 복사
Copy-Item -Path "백업경로\keybindings.json" -Destination "$env:APPDATA\Cursor\User\keybindings.json" -Force
```

### 3단계: 확장 프로그램 설치 ✅

```powershell
# extensions-list.txt 파일에서 한 번에 설치
Get-Content extensions-list.txt | ForEach-Object { code --install-extension $_ }
```

또는 개별 설치:
```powershell
code --install-extension github.copilot
code --install-extension github.copilot-chat
code --install-extension mechatroner.rainbow-csv
# ... (나머지 확장 프로그램)
```

### 4단계: Agent Skills 복원 ✅

```powershell
# Skills 폴더 생성 및 복사
New-Item -Path "C:\Users\새계정\.cursor\skills-cursor" -ItemType Directory -Force
Copy-Item -Path "백업경로\skills-cursor\*" -Destination "C:\Users\새계정\.cursor\skills-cursor" -Recurse -Force
```

### 5단계: MCP 서버 설정 복원 ✅

```powershell
# globalStorage 복사
Copy-Item -Path "백업경로\globalStorage\*" -Destination "$env:APPDATA\Cursor\User\globalStorage" -Recurse -Force
```

### 6단계: 프로젝트 및 Rules 복원 ✅

```powershell
# 프로젝트 폴더 전체 복사 (Git 저장소 포함)
Copy-Item -Path "원본프로젝트경로" -Destination "새위치" -Recurse
```

또는 Git Clone:
```bash
git clone <repository-url>
# .cursor/rules 폴더는 자동으로 포함됨
```

### 7단계: Cursor 재시작 ✅

모든 복원이 완료되면 Cursor를 재시작하여 설정을 적용합니다.

---

## ✅ 확인 체크리스트

복원 후 다음 항목들이 제대로 작동하는지 확인하세요:

- [ ] 에디터 테마와 폰트가 동일한가?
- [ ] 키보드 단축키가 작동하는가? (Ctrl+I로 에이전트 모드)
- [ ] 확장 프로그램이 모두 설치되었는가?
- [ ] Python 인터프리터가 설정되었는가?
- [ ] GitHub Copilot이 작동하는가?
- [ ] SSH 원격 연결 설정이 있는가?
- [ ] Cursor Rules가 프로젝트에서 인식되는가?
- [ ] Agent Skills가 사용 가능한가?
- [ ] MCP 서버가 연결되는가?

---

## 🔍 주요 파일 경로 참조

### Windows 경로

```
설정 파일: C:\Users\계정명\AppData\Roaming\Cursor\User\
Skills: C:\Users\계정명\.cursor\skills-cursor\
프로젝트 Rules: 프로젝트경로\.cursor\rules\
MCP 설정: C:\Users\계정명\AppData\Roaming\Cursor\User\globalStorage\
```

### 환경 변수 사용

```powershell
$env:APPDATA\Cursor\User\         # 설정 파일
$env:USERPROFILE\.cursor\         # Skills 폴더
```

---

## 💡 추가 팁

### 정기 백업 자동화

작업 스케줄러를 사용하여 자동 백업 설정:

```powershell
# 매주 일요일 자동 백업
$trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Sunday -At 2am
$action = New-ScheduledTaskAction -Execute "PowerShell.exe" -Argument "백업경로\cursor-backup.ps1"
Register-ScheduledTask -TaskName "Cursor Weekly Backup" -Trigger $trigger -Action $action
```

### Git으로 설정 관리

설정 파일을 Git으로 버전 관리하면 더욱 편리합니다:

```bash
# 설정 저장소 생성
cd C:\Users\sharp\AppData\Roaming\Cursor\User
git init
git add settings.json keybindings.json
git commit -m "Initial cursor settings"
git remote add origin <your-repo-url>
git push -u origin main
```

### 여러 PC 간 동기화

OneDrive 또는 Google Drive에 설정을 저장하고 심볼릭 링크 사용:

```powershell
# 설정 파일을 OneDrive로 이동
Move-Item -Path "$env:APPDATA\Cursor\User\settings.json" -Destination "$env:OneDrive\CursorSettings\settings.json"

# 심볼릭 링크 생성
New-Item -ItemType SymbolicLink -Path "$env:APPDATA\Cursor\User\settings.json" -Target "$env:OneDrive\CursorSettings\settings.json"
```

---

## 🆘 문제 해결

### 문제: 설정이 적용되지 않음
**해결**: Cursor를 완전히 종료하고 재시작 (작업 관리자에서도 확인)

### 문제: 확장 프로그램 설치 실패
**해결**: 인터넷 연결 확인 후 개별적으로 재설치

### 문제: MCP 서버 연결 안 됨
**해결**: MCP 서버 재설치 또는 설정 파일 재확인

### 문제: Skills가 인식되지 않음
**해결**: 경로가 올바른지 확인, Cursor 재시작

---

## 📞 지원

문제가 계속되면:
1. Cursor 공식 문서 참조
2. Cursor Discord 커뮤니티 문의
3. 백업 파일 무결성 확인

---

**생성일**: 2026-03-06  
**버전**: 1.0  
**적용 계정**: sharp (기준 환경)

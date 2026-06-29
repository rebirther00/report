# Git + Gitea + LFS 개발환경 가이드

이 저장소는 **GitHub와 Gitea 두 원격(remote)** 을 함께 쓰고, 대용량 파일은 **Git LFS로 Gitea에** 저장한다.

## 구조 한눈에 보기

| 위치 | 무엇을 저장 |
|---|---|
| **GitHub** (`origin` fetch) | 코드·md·텍스트 + 대용량 파일의 **LFS 포인터**(몇 줄짜리 텍스트) |
| **Gitea** (`git.kocetismart.kr:3000`) | **실제 대용량 바이너리**(hwpx/pptx/pdf/xlsx/hwp 등)를 Git LFS로 |

- `.lfsconfig`의 `lfs.url`이 Gitea를 가리켜 → **모든 LFS 객체는 항상 Gitea로** 간다.
- `origin`에 push URL 2개(GitHub+Gitea)가 설정돼 → **`git push` 한 번에 양쪽 동기화**.
- `pull`/`fetch`는 GitHub에서 받는다.
- 대용량 파일 추적 규칙은 `.gitattributes`에 정의돼 있다 (hwpx/pptx/pdf/xlsx/hwp/ppt/xls/zip).

> 배경: GitHub 무료는 파일당 100MB 제한이 있어 대용량(예: 199MB hwpx)을 못 올린다. 회사 Gitea 서버로 LFS 처리해 이 문제를 해결했다. **과거의 OneDrive 우회 방식은 폐기**되었다.

---

## 평소 작업 (모든 PC 공통)

대용량 파일도 그냥 평소대로 커밋하면 자동으로 Gitea LFS로 간다.

```bash
git add .
git commit -m "작업 내용"
git push          # → GitHub(포인터) + Gitea(실제 파일) 자동 동기화
git pull          # → GitHub에서 받기 (대용량은 Gitea에서 자동 다운로드)
```

---

## 새 PC에서 처음 받을 때 (clone)

```bash
git lfs install                                    # 1회만
git clone https://github.com/rebirther00/report.git
cd report
# 코드·md·포인터를 받고, 대용량은 Gitea에서 자동 다운로드된다
```

**필요 조건:** 그 PC에 `git-lfs` 설치 + **Gitea 로그인 권한**(회사 계정). Gitea 첫 접속 시 인증 창이 한 번 뜬다.

### 새 PC에서도 push로 양쪽 동기화하려면 (1회 설정)

clone한 PC에서 push까지 하려면 dual-push 설정을 한 번 해준다:

```bash
git remote set-url --add --push origin https://github.com/rebirther00/report.git
git remote set-url --add --push origin http://git.kocetismart.kr:3000/rebirther00/report.git
```

설정 확인: `git remote -v` 에서 `origin ... (push)` 줄이 **2개**면 정상.

---

## 이미 소스가 있는 기존 PC (⚠️ 1회성 강제 동기화 필요)

LFS 전환 시 **히스토리를 재작성(migrate)하고 force-push** 했기 때문에, 그 전에 clone해둔 PC는
로컬 히스토리가 새 원격과 **완전히 갈라진 상태**다. 이 PC에서는 그냥 `git pull` 하면 충돌이 난다.
아래로 **한 번만** 새 히스토리에 맞춘다.

```bash
git lfs install                 # 안 돼 있으면

# ⚠️ 커밋 안 한 작업이 있으면 먼저 백업!
git status
git stash                       # 필요시 임시 보관

git fetch origin
git reset --hard origin/main    # 새 히스토리에 강제로 맞춤 (미커밋 변경 버려짐)
git lfs pull                    # 대용량을 Gitea에서 받기 (자동 안 됐을 때)
```

> 미커밋 작업이 없다면 **폴더 지우고 새로 clone** 하는 게 가장 깔끔하다.
>
> 이 강제 동기화는 **이번 한 번만**이다. 이후엔 평소대로 `git pull` / `git push`.

---

## 대용량 / 제외 파일 규칙

- **LFS로 저장(자동):** `*.hwpx *.hwp *.pptx *.ppt *.pdf *.xlsx *.xls *.zip` → 커밋하면 Gitea LFS로.
- **git에서 제외(`.gitignore`):**
  - 추출 임시물: `**/_*_extract/`, `*_txt.txt`, `*_ocr.txt`, 추출 스크립트
  - 도구 상태: `.bkit/`, `.omc/`
  - 가상환경: `marker-env/`, `mineru-env/`, `__pycache__/`, `*.pyc`, `*.bat`
  - `13. 4극3특/`의 미리보기 이미지·html (`*.png *.jpg *.html`) — 원본 그림이면 별도로 추가

---

## 트러블슈팅

| 증상 | 해결 |
|---|---|
| 대용량 파일이 포인터 텍스트로만 보임 | `git lfs pull` (Gitea 로그인 필요) |
| push 시 GitHub가 100MB 초과로 거부 | 해당 확장자가 `.gitattributes`에 LFS로 등록됐는지 확인 (`git lfs track`) |
| `git pull` 충돌/`unrelated histories` | 위 "기존 PC 1회성 강제 동기화" 절차 수행 |
| Gitea 인증 실패 | 회사 Gitea 계정 권한 확인 |

---

## 백업 / 복원

- 변환 전 상태: 로컬 `backup-pre-lfs` 브랜치 / `pre-lfs-snapshot` 태그 (작업 PC 한정).
- LFS를 다시 일반 파일로 되돌리려면: `git lfs migrate export --include="*.pdf,*.hwpx,..."`.

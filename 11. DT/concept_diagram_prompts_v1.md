# 개념도 작성용 GPT 프롬프트 모음 (v1.1)

> 대상: GPT 5.5 (또는 ChatGPT 이미지 생성)
> 용도: 사업 외부 공유용 개념도 6종
>
> **v1.1 보정 (2026-05-04)** — 사업기획_업무상세화_v1.2와 동기화. *BIM·외부 측량 통합 등 사업화 단계 표현 제거*. TRL 3~5에 맞춰 *TB(테스트베드) 환경 공정 계획* 중심으로 표현 수정.

---

## 사용 가이드

1. 각 프롬프트를 GPT 5.5 이미지 생성 모드에 그대로 붙여넣기
2. 결과가 마음에 안 들면 **"수정 지시"** 섹션의 문구로 후속 요청
3. 한국어 텍스트 라벨 깨짐 방지: 결과물 받은 후 PPT/Visio에서 텍스트만 다시 입력 권장
4. 일관된 스타일 유지: 같은 *색상·폰트 키워드*를 모든 프롬프트에 사용

### 공통 스타일 키워드 (모든 프롬프트에 포함)

```
Style: clean modern infographic, flat 2D design, isometric optional
Color palette: navy blue (#1565C0), orange (#FF9800), green (#43A047), light grey background
Typography: sans-serif, bold headers, minimal text
Aspect ratio: 16:9 widescreen for slides
Background: white or very light grey, no clutter
No: photorealistic rendering, 3D ray tracing, decorative ornaments
```

---

## 1. 전체 개념도 (Overall Concept)

### 목적
사업 전체 비전을 한 장으로 보여주기. *발표 첫 슬라이드*용.

### 핵심 메시지
- 무인 자율 굴착기 = *DT 시뮬 검증 ↔ 실차 검증의 양방향 사이클*
- 가상과 실차의 학습·전이 흐름 (Sim2Real)

### GPT 프롬프트

```
Create a clean modern infographic diagram (16:9 widescreen) titled
"AI 기반 무인 자율 굴착기 디지털 트윈 플랫폼" in Korean.

Layout:
- Left side: a virtual world with a digital twin excavator working on
  a digital construction site (wireframe or transparent style)
- Right side: a real construction site with a real excavator (slightly
  realistic but flat 2D illustration style)
- Center: a glowing data bridge connecting both sides, with bidirectional
  arrows labeled "Sim2Real 전이" (left to right) and "실차 데이터 피드백"
  (right to left)
- Top banner: 4 stage labels in horizontal flow:
  "① 가상 환경 학습" → "② DT 공정 계획·검증" → "③ 실차 자율 작업" → "④ 데이터 피드백"
- Bottom: small icons row with labels
  "디지털 트윈 모델 · 토사 물리 모델 · AI 정책 학습 · Sim2Real 적응 · 안전 레이어"

Style: clean modern infographic, flat 2D design with subtle isometric
  feel for the excavators
Color palette: navy blue (#1565C0) for virtual side, orange (#FF9800)
  for real side, green (#43A047) for the bridge, light grey background
Typography: bold sans-serif Korean headers, minimal English labels
Background: white with subtle grid pattern on the left (virtual) side

Avoid: photorealistic, 3D rendering, cluttered text, decorative elements,
  BIM/blueprint imagery, drone/aerial survey elements (out of scope)
```

### 수정 지시 예시
- "left side 가상 영역의 wireframe을 더 강조해줘"
- "중앙 bridge에 'Sim2Real Transfer' 영문 라벨 추가"
- "전체적으로 텍스트 양을 30% 줄여줘"

---

## 2. DT 플랫폼 모듈 개념도

### 목적
DT 플랫폼이 *어떤 모듈로 구성되며 어떤 입출력을 갖는지* 표현.

### 핵심 메시지
- DT는 단순 시뮬레이터가 아니라 *통합 작업 환경*
- TB 환경 데이터·시나리오 + 실차 데이터 입력 → 시뮬 검증 → 작업 명령 출력

### GPT 프롬프트

```
Create a modular concept diagram (16:9) titled "디지털 트윈 플랫폼 (DT) 구조"
in Korean.

Layout: a central rounded rectangle labeled "DT 통합 플랫폼" containing
6 inner modules arranged in a 2x3 grid:
  Row 1: "가상 작업 환경" | "건설기계 모델 (3종)" | "토사 물리 모델 (3종)"
  Row 2: "도메인별 물리 모델" | "공정 계획·검증" | "DT 성능 시험"

Inputs (left side, with arrows pointing into the platform):
  - "TB 환경 데이터" (icon: testbed/sensor)
  - "작업 시나리오" (icon: task list)
  - "실차 데이터" (icon: excavator silhouette)

Outputs (right side, with arrows pointing out of the platform):
  - "검증된 작업 명령" (icon: gear)
  - "AI 학습 데이터" (icon: database)
  - "성능 검증 보고서" (icon: chart)

Bottom: a thin horizontal bar labeled "통합 미들웨어 · API · 시각화"
representing the foundational layer.

Style: clean modern infographic, flat 2D
Color palette: navy blue (#1565C0) for platform border, light blue
  fills for modules, orange (#FF9800) for input arrows, green (#43A047)
  for output arrows
Background: white
Typography: bold Korean headers, monospace for tech labels

Avoid: 3D effects, decorative shadows, photorealistic icons,
  BIM blueprint imagery, drone aerial survey (out of scope for TRL 3~5)
```

### 수정 지시
- "각 모듈에 작은 아이콘 추가해줘"
- "Inputs 영역에 TB 환경 = testbed 의미 명시 (시험장 인식 데이터)"

---

## 3. AI 모듈 개념도 (Sim2Real 학습 사이클)

### 목적
AI가 *가상에서 학습 → 실차에 적응 → 검증*되는 사이클 시각화.

### 핵심 메시지 (주인공 = AI 정책 모델)
- **AI 정책 모델이 4단계 사이클을 거쳐 진화** (가상 → 전이 → 적응 → 검증)
- 도메인 랜덤화·시스템 식별·미세조정은 *각 단계의 기법*
- **안전 레이어·단계별 시험 캠페인은 보조 요소** (단계 아님 — 사이클 외곽 작은 표기)

### GPT 프롬프트

```
Create a circular pipeline diagram (16:9) titled "AI 학습 및 Sim2Real 적응 사이클"
in Korean.

THE PROTAGONIST: an "AI 정책 모델" icon (stylized neural network or brain
chip) placed prominently at the CENTER of the circle. This is the main
subject — make it visually dominant (large, bold, glowing outline).
The icon should appear to "flow" through the cycle, suggesting evolution
of the same model across stages.

Layout: a circular flow with 4 MAIN STAGES connected by curved arrows,
going clockwise:
  Stage 1 (top): "가상 환경 정책 학습" - icon of brain in virtual/wireframe world
  Stage 2 (right): "Sim2Real 전이" - icon of bridge transferring the model
  Stage 3 (bottom): "실차 도메인 적응" - icon of real excavator + tuning knob
  Stage 4 (left): "실차 검증 (KPI 90%)" - icon of medal/checkmark on real machine

Below each stage label, smaller secondary text showing the key technique
(half-size font, lighter color):
  Stage 1: "도메인 랜덤화 (Domain Randomization)"
  Stage 2: "시스템 식별 (System Identification)"
  Stage 3: "미세조정·잔차 정책 (Fine-tune / Residual Policy)"
  Stage 4: "단계별 시험 캠페인"

AUXILIARY ELEMENTS (small, NOT stages — placed at bottom edge of diagram
as a thin footer strip, clearly subordinate):
  - "🛡 안전 레이어 (Stage 3~4 동안 상시 작동)" - small shield icon
  - "📋 단계별 시험 캠페인 (Stage 4 진행: 4단계 위험도 점진 확대)" - small list icon

These auxiliary items must NOT be drawn inside the cycle or as separate
stages. They are footnote-style small labels showing they are background
support, not main stages.

Style: clean infographic, flat 2D
Color palette: 
  - Stages 1-2 (virtual side): blue tones (#1565C0, #42A5F5)
  - Stages 3-4 (real side): orange tones (#FF9800, #FFB74D)
  - Bridge/transition: green (#43A047)
  - Center AI model: dark navy with glowing accent
  - Auxiliary footer: muted grey (#9E9E9E)
Typography: bold Korean labels for stages, smaller lighter font for techniques,
  smallest grey font for auxiliary items

Avoid: 
  - Promoting safety layer or staged test campaign to be a stage in the cycle
  - 6 stages instead of 4 (must be 4)
  - Central shield diagram (the center is the AI policy model, not a shield)
  - Chaotic arrow crossings or neural network spaghetti
  - Photorealistic AI imagery
```

### 수정 지시
- "Stage 3 아래 '미세조정·잔차 정책' 폰트를 더 작게 — 메인 라벨의 50% 크기"
- "중앙 AI 정책 모델 아이콘을 더 크게, 사이클 전체에서 가장 시선이 가는 요소로"
- "안전 레이어와 단계별 시험 캠페인을 footer에서 더 작게 — 메인의 30% 크기"

---

## 4. 실차 모듈 개념도

### 목적
실차에 어떤 *센서·통신·안전 장치*가 들어가는지, *시험장 구성*은 어떤지 표현.

### 핵심 메시지
- 실차는 *보유*하고 있고, 센서·통신·안전 장치를 *retrofit*
- 4단계 시험 캠페인 (Bench → 평탄 → 다양지형 → 야간/위험)

### GPT 프롬프트

```
Create a technical illustration (16:9) titled "실차 검증 환경 구성" in Korean.

Layout: split into two halves:

LEFT HALF (60% width): "Instrumented Excavator"
- An isometric 2D illustration of an excavator
- Annotation callouts pointing to specific parts:
  - Top of cabin: "5G 안테나 + GPS RTK"
  - Front of cabin: "스테레오 카메라 + LiDAR"
  - Boom: "관절 엔코더"
  - Bucket: "6축 힘/토크 센서"
  - Hydraulic line: "압력 센서"
  - Inside cabin: "Edge Computer + IMU"
  - Side: "비상정지 (E-stop)"

RIGHT HALF (40% width): "4-Stage Test Campaign"
A vertical stacked diagram showing 4 stages from top to bottom:
  Stage 1: "Bench 시험" - icon of excavator on test bench
  Stage 2: "주간 평탄지" - icon of sunny flat ground
  Stage 3: "다양 지형 (토사 3종)" - icon of soil types
  Stage 4: "야간 / 위험지" - icon of moon and warning sign
Each stage has a success rate target on the right (95%, 92%, 90%, 85%).

Style: technical infographic, flat 2D with isometric excavator,
  clean callout lines (no overlapping), professional engineering look
Color palette: orange (#FF9800) primary for excavator, navy blue
  (#1565C0) for callout lines, gradient red-to-blue for the 4 stages
Background: light grey (#FAFAFA) with subtle blueprint grid

Avoid: cluttered annotations, photorealistic excavator render, 3D rays
```

### 수정 지시
- "센서 라벨에 영문 약어 (LiDAR, IMU, RTK) 추가"
- "각 단계의 성공률을 더 큰 폰트로"

---

## 5. KPI 매트릭스 개념도

### 목적
*5개 KPI*와 *16개 항목의 책임 관계*를 한 장으로 시각화. 평가위원 대응용.

### 핵심 메시지
- 모든 KPI에 *주관 책임 항목*이 명확히 매핑됨
- KPI 5개 중 *G2/P4 (전이 90%)* 가 가장 큰 책임 (5개 항목)

### GPT 프롬프트

```
Create a KPI accountability matrix infographic (16:9) titled
"성능 지표(KPI)와 책임 항목 매핑" in Korean.

Layout: a horizontal bubble chart / sankey-style diagram

LEFT COLUMN: 5 vertical bars labeled with KPIs (in Korean):
  1. "G1/P1 거동 일치도 ≥ 90%" - blue bar
  2. "P2 토사 3종 구현" - brown bar
  3. "P3 기계 모델 3종" - orange bar
  4. "G2/P4 무인 작업 90%" - red bar (largest)
  5. "P5 연동 지연 ≤ 100ms" - green bar
  6. "P6 계획 정확도 (제안)" - light green bar (with "협의" tag)

RIGHT COLUMN: 16 small rounded boxes representing items #1 to #15
(with #10 split into #10a and #10b), arranged in a 4x4 grid.
Each box labeled with item number and short name.

CENTER: connecting curved lines (sankey style) from each KPI to its
responsible items, with line thickness proportional to budget.
Use subtle transparency so overlaps are readable.

Bottom: a legend explaining
  "굵은 선 = 주관 책임 (◎)"
  "얇은 선 = 보조 (○)"

Style: data visualization infographic, flat 2D, sankey-inspired
Color palette: each KPI has its own color; items in neutral grey
  with colored borders matching their primary KPI
Typography: bold Korean headers, small Korean labels on items

Avoid: chaotic line crossings, illegible labels, dark backgrounds
```

### 수정 지시
- "G2/P4 라인을 더 굵게 강조"
- "P6는 점선으로 표시 (협의 중 의미)"

---

## 6. (선택) 기관·예산 개념도

### 목적
*5개 기관*과 *48억 예산*을 한 장으로.

### GPT 프롬프트

```
Create a stakeholder/budget allocation infographic (16:9) titled
"컨소시엄 구성 및 예산 분배 (총 48억)" in Korean.

Layout: 5 organizations as colored circles with size proportional to budget

Organizations (with budget):
  - 🟧 주관 (중소·중견 SW): "10.0억 (21%)" - orange circle, largest at top
  - 🟦 공동1 (시뮬·CAE): "12.0억 (25%)" - blue circle, top right
  - 🟩 공동2 (AI 기업): "12.5억 (26%)" - green circle, bottom right
  - 🟪 공동3 (대학·출연연): "4.0억 (8%)" - purple circle, smallest, bottom
  - 🟨 공동4 (제조사·시험기관): "9.5억 (20%)" - yellow circle, bottom left

Each circle labeled with:
  - Organization role (Korean)
  - Budget amount
  - 2-3 key responsibilities

Connecting lines between circles labeled with collaboration topics:
  - 주관 ↔ 공동1: "플랫폼-모델 통합"
  - 공동2 ↔ 공동4: "Sim2Real 적응 ↔ 실차 검증"
  - 공동1 ↔ 공동3: "토사 모델 위탁"

Bottom right: pie chart summary "48억 = 좌 27.5 + 중 8 + 우 12.5"

Style: clean modern infographic, flat 2D with subtle gradients
Color palette: as specified above (orange/blue/green/purple/yellow)
Typography: bold Korean labels, percentage in larger font

Avoid: photorealistic, 3D pie chart, busy backgrounds
```

---

## 후속 작업 시 권장 사항

1. **GPT 5.5 결과를 받은 후, *PPT/Visio에서 텍스트 다시 입력*** — 한글 깨짐 방지
2. **모든 개념도 색상을 통일** — 위 색상 팔레트 사용
3. **결과 저장** — `concept_diagrams/` 폴더 생성하여 정리
4. **버전 관리** — 외부 공유 전 v1, v2 등 버전 명기

---

## 변경 이력

| 버전 | 일자 | 변경 내용 |
|---|---|---|
| v1.0 | 2026-05-04 | 초안 작성 (6종 프롬프트) |
| v1.1 | 2026-05-04 | 사업기획_업무상세화 v1.2 동기화 — *BIM·드론 측량 통합* 표현 제거. *TB 환경·작업 시나리오* 입력으로 변경. "임무 계획" → "공정 계획" 명칭 통일. TRL 3~5 범위에 부합하도록 사업화 단계 표현 회피. |
| v1.2 | 2026-05-04 | **#3 AI 모듈 개념도 재구성** — 6단계(안전/Curriculum 포함) → **4단계 + AI 정책 모델 중심**. 안전 레이어와 Curriculum을 사이클 외부의 보조 footer로 강등. AI 정책 모델을 중앙 protagonist로 부각. |
| v1.3 | 2026-05-04 | **용어 한글화** — "Curriculum 시험"·"Curriculum Deployment" → "단계별 시험 캠페인"으로 통일. 학술 외래어 대신 평가위원·정부 보고용 표준 표현 채택. 영문 학술용어는 괄호 병기 형태로만 남김. |

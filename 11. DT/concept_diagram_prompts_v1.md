# 개념도 작성용 GPT 프롬프트 모음 (v2.0)

> 대상: GPT 5.5 (또는 ChatGPT 이미지 생성)
> 용도: 사업 외부 공유용 개념도 10종
>
> **v1.1 보정 (2026-05-04)** — 사업기획_업무상세화_v1.2와 동기화. *BIM·외부 측량 통합 등 사업화 단계 표현 제거*. TRL 3~5에 맞춰 *TB(테스트베드) 환경 공정 계획* 중심으로 표현 수정.
>
> **v1.4 추가 (2026-05-07)** — **#7 건설기계 DT 모델 구성도 신설** — 굴착기의 다관절 동역학(MBD) 구조 + 도메인 물리(유압·MCV·실린더·ECU) + 토사 반력 + 파라미터 가변 + 정밀도 모드 한 장 통합. 모든 미팅(HDX·심지·평가위원) 공용.
>
> **v1.5 변경 (2026-05-07)** — **#7 스타일 전면 변경** — 굴착기 일러스트 → **순수 블록 다이어그램**(rounded boxes + arrows + legend)으로 재작성. 사용자 요청 *"실제 예시 그리기보다 모듈별 연계와 구성을 심플하게 도식화"* 반영. MBD 솔버를 중심 노드로 하는 control loop + MBD↔토사 양방향 결합 강조.
>
> **v1.6 추가 (2026-05-09)** — **#8 업무 범위 한 장 구조도 신설** — 사업이 *무엇을 만드는지*를 비전공자도 한 장으로 파악하도록 컴포넌트 트리(장비/환경/시나리오/통신/학습) + 16개 항목 번호 + 5개 기관 색상 코드를 결합. 신규 합류자·외부 미팅 첫 장 공용.
>
> **v1.7 추가 (2026-05-09)** — **#9 DT 컴포넌트·연결 한 장 구성도 신설** — #8(업무 범위)과 분리하여 *기술 관점*에서 DT가 무엇으로 만들어지고 어떻게 연결되는지 시각화. 사용자가 빠뜨리기 쉬운 4개 카테고리(센서 모델·정밀도 모드·V&V 검증·Sim2Real 다리)를 명시적으로 부각. 신규 엔지니어 온보딩·기술 검토회의 첫 장.
>
> **v1.8 변경 (2026-05-09)** — **#7~#9에서 *항목 번호·기관 색상·예산·KPI 코드* 일괄 배제** (사용자 요청). #8: 모든 child box 옆 `← #X 🟦` 매핑·LEVEL 3 기관 예산 + KPI 한 줄 요약 띠 제거 / #9: child box 안 `(#5)·(#13)·(P5 ≤100ms)` 등 제거. 두 다이어그램 모두 AVOID 섹션에 *사업 항목 번호·기관 색상·예산·KPI 코드 금지* 명시. 책임·예산은 별도 자료(한장 사업구조도·KPI 매트릭스)로 분리하여 *기술 컴포넌트 범위·연결*에만 시선 집중. 제어기 약어 `VBO·FEH` → 표준 `VCU·ECU·HCU`로 변경.
>
> **v1.9 변경 (2026-05-09)** — **#9를 #9a + #9b로 분리** (사용자 지적: *"기존 #9의 ZONE ④/⑤에 DT 자산이 아닌 실차·학습 인프라가 섞여 있다"*). #9a = *좁은 DT 내부 컴포넌트* (실차 retrofit·실차 데이터·실차 캠페인·안전 레이어 등 외부 요소 제거) / #9b = *DT ↔ 외부 시스템 통합* (DT 중앙, 3방향 외부 — 입력원·AI 학습 인프라·실차 시스템 — 데이터 흐름 화살표). DT 경계가 시각적으로 정직해짐.
>
> **v2.0 변경 (2026-05-09)** — **Sim2Real 전이 배치 정정 + OTA 용어 일괄 제거** (사용자 지적 2건). ① *"Sim2Real 전이"가 Bridge에 있는 이유?"* → 학술적 *Sim2Real 학습 기법*(DR·SysID·DA·Residual)을 ZONE ⑤(학습 코드) + 외부 GPU(#9b)로 이동, ZONE ④에는 *정책 배포 모듈*(weights 전달)만. ② *"국책과제(TRL 3~5)에 OTA는 over-engineering"* → 다이어그램 9곳의 OTA 라벨을 *"정책 배포 (수동·LAN·SD)"*로 일괄 정정. 모델 레지스트리도 *"OTA 배포 준비"* → *"실차 배포 패키지 빌드"*. #9a/#9b 사용 시 주의에 OTA 불필요 + Sim2Real 의미 명시 추가. **사용자 핵심 문서**(사업기획·한장구조도·연계다이어그램)의 OTA 표현은 별도 협의 후 정리 예정.

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

## 7. 건설기계 DT 모델 구성도 (Multi-physics 결합 + 파라미터·정밀도 가변)

### 목적
*건설기계가 DT 안에서 어떻게 구성되어 있는지* 한 장으로 보여주기. **모든 미팅 공용** (HDX·심지·평가위원·CAE 후보 등).

### 핵심 메시지

- **블록 다이어그램 형식** — 굴착기 일러스트 X. 모듈(ECU·MCV·실린더·MBD·토사)과 *연계·환류 화살표*만 표시
- DT는 **MBD(다관절 동역학) 솔버를 중심으로 한 control loop**: ECU → MCV → 실린더 → MBD → (관절 피드백) → ECU
- 버킷이 토사를 만나면 **MBD ↔ 토사 양방향 결합** — 운동 정보가 토사로, 6축 반력이 MBD로 환류
- *같은 모듈 구성에* 파라미터(실린더 보어·유압 압력·관절 길이·토사 종류)를 외부 주입 → 신차·변형 모델 검증
- *같은 모듈 구성에* 정밀도 모드(정밀↔실시간↔도메인 mix)를 외부 적용 → OEM 정밀 검증과 AI 실시간 학습 모두 수용
- → **차별화 ① "파라미터화 + 정밀도 가변 multi-physics 통합 DT"의 모듈 연계 시각화**

### GPT 프롬프트

```
Create a clean SYSTEM BLOCK DIAGRAM (16:9 widescreen) titled
"건설기계 디지털 트윈 모델 구성도" with subtitle
"모듈 결합 · 파라미터 가변 · 정밀도 모드 가변" in Korean.

This is a PURE BLOCK DIAGRAM (rounded rectangles + labeled arrows + legend).
DO NOT illustrate an excavator or any machinery. Visualize ONLY modules
and their connections — like a system architecture or P&ID schematic.

LAYOUT — 3 zones in a single panel:

[ZONE A — LEFT-CENTER (50% width)]
A large rounded panel labeled "건설기계 DT 모델" containing 4 module blocks.
Arrange them like a control loop:

  Top:    [ECU<br/>차량 제어기]
  Middle: [MCV<br/>메인 제어 밸브 (Main Control Valve)]
  Bottom-left: [유압 실린더 ×3<br/>(Hydraulic Cylinders)]
  Center (largest, emphasized): [MBD 솔버<br/>다관절 동역학<br/>(Multi-body Dynamics)]

  Arrows inside Zone A (with style/color per type — see LEGEND below):
    - ECU → MCV : 제어 신호 (dashed green arrow, label "제어 명령")
    - MCV → 유압 실린더 : 유압 흐름 (thick blue arrow, label "유압 압력·유량")
    - 유압 실린더 → MBD : 힘 입력 (orange arrow, label "실린더 힘")
    - MBD → ECU : 관절 상태 피드백 (thin grey arrow, label "관절각·속도 피드백")

[ZONE B — RIGHT-CENTER (30% width)]
A separate rounded panel labeled "환경 (토사)" containing one block:
  [토사 모델<br/>DEM (입자 단위 토사 해석)<br/>+ SPH (점성토)]

  Bidirectional coupling between Zone A's MBD-Bucket and Zone B's 토사:
    - MBD → 토사 : 버킷 위치·속도 (blue arrow, label "버킷 운동")
    - 토사 → MBD : 6축 반력 (THICK red arrow, label "버킷 반력 (6축 힘·토크)<br/>Fx Fy Fz Mx My Mz")
  This bidirectional pair is THE KEY visual — make it visually prominent.

[ZONE C — RIGHT-EDGE / TOP-RIGHT (20% width, two stacked sub-panels)]

  Sub-panel C1 (top): "파라미터 입력"
    A small box with 4 stacked rows showing parameter names + values:
      실린더 보어 = D mm
      유압 압력   = P bar
      관절 길이   = L m
      토사 종류   = {모래·진흙·자갈}
    From this box, dashed orange "fan-out" arrows reach to ALL modules
    in Zone A and Zone B (use thin dashed lines so they don't overwhelm).
    Caption (small): "OEM 신차·변형 모델 검증 (HDX)"

  Sub-panel C2 (bottom): "정밀도 모드"
    A small box with 3 mode tags in a row (one highlighted active):
      [정밀 (OEM)] [실시간 (AI)] [도메인 mix]
    Below, 3 short labels:
      유압 : 고차 / 근사
      토사 : DEM full / ML 근사
      MBD  : full / 단순화
    From this box, dashed green "fan-out" arrows reach to ALL modules
    in Zone A and Zone B.
    Caption (small): "한 모델이 정밀↔실시간 자동 전환"

[LEGEND — bottom strip, full width, small]
Show 5 arrow style swatches with labels:
  ▬▬▬ (thick blue)   = 유압 흐름
  ▬▬▬ (thick red)    = 반력·힘
  ▬▬▬ (thin orange)  = 실린더 힘
  ─ ─ ─ (dashed green) = 제어 신호 / 정밀도 모드 적용
  ─ ─ ─ (dashed orange) = 파라미터 주입
  ───── (thin grey)  = 상태 피드백

STYLE:
- Pure system block diagram (think system architecture / P&ID / Simulink)
- Rounded rectangles with thin colored borders, white fills
- All labels in Korean (with English in parens for industry terms)
- Color palette:
  - Zone A panel border: navy blue (#1565C0)
  - Zone B panel border: brown (#8D6E63)
  - Zone C panel border: dark grey (#616161)
  - MBD module (largest): yellow accent border to emphasize central role
  - Arrow colors per LEGEND
- Background: white, very subtle grid optional
- Typography: bold sans-serif Korean for module names, smaller for sub-labels

AVOID:
- ANY illustration of an excavator, machinery, or 3D objects
- Photorealistic rendering
- Showing 전동 모터, 배터리, 파워트레인 (out of scope per user)
- Showing physical construction site
- Decorative shadows, gradients, ornaments
- Crossing arrows that hurt readability — re-route if needed
```

### 수정 지시 예시

- "버킷 반력 화살표(red, thick)를 더 굵게, *Fx Fy Fz Mx My Mz* 라벨이 잘 보이게"
- "MBD 솔버 박스를 가장 크게, 모든 화살표가 결국 MBD를 거치는 구조 부각"
- "오른쪽 *정밀도 모드* 패널의 3개 모드 중 *정밀 (OEM)* 만 색깔 채워서 활성화 표시"
- "ECU → MCV → 실린더 → MBD 흐름이 *위→아래로 자연스러운 control loop*가 되게 재배치"
- "Zone B의 *MBD ↔ 토사* 양방향 화살표가 시선의 중심에 오도록 강조"
- "파라미터 주입 fan-out 화살표가 너무 많아 복잡하면, 대표 모듈 1~2개에만 그리고 *"전 모듈 적용"* 으로 라벨"

### 사용 시 주의

- 블록 다이어그램은 **A4 1장 또는 PPT 1슬라이드**로 충분 (정보가 모듈로 압축되어 작아도 읽힘)
- HDX 미팅 시: *Zone C1 파라미터 입력*을 짚으며 *"이 값을 바꾸면 모든 모듈 거동이 자동 재계산"* 설명
- 평가위원 발표 시: *MBD 솔버를 중심으로 한 모듈 결합 구조* 강조 — *"단순 시각 시뮬이 아닌 control loop + multi-physics 통합"*
- 심지·CAE 후보 미팅 시: *MBD ↔ 토사 양방향 결합*을 짚으며 *"이 환류가 기술적으로 가장 어려운 부분"*
- GPT 결과가 복잡하면 *수정 지시 6번* (fan-out 화살표 단순화) 적용 권장

---

## 8. 업무 범위 한 장 구조도 (Scope-at-a-Glance)

### 목적

사업이 *무엇을 만드는지·무엇이 그 안에 들어 있는지*를 **30초 안에 비전공자가 이해**하도록. 신규 합류자 온보딩, 외부 미팅 첫 장, 공무원·평가위원 첫 슬라이드 공용.

기존 #1(전체 비전), #2(DT 플랫폼 모듈), #5(KPI 매트릭스)와의 차이:
- #1은 *왜 하는가*, #2는 *DT 내부 구조*, #5는 *KPI 책임*
- **#8은 *전체 업무 범위 = 큰 컴포넌트 5개 × 그 하위 모듈 × 누가 책임지는가*** — 가장 처음 봐야 할 한 장

### 핵심 메시지

- 사업의 업무 범위는 **5개 큰 묶음**으로 분해됨 — ① 장비 모델 ② 작업 환경 ③ 자율공정 ④ 통신·전이 ⑤ 학습·검증
- 각 묶음 안에 *세부 컴포넌트 박스*가 들어가 한 장에서 전체 범위 파악
- **두 기둥 가치**(A: OEM 신제품 / B: 무인 자율 작업)가 *같은 컴포넌트를 공유*함을 우측 상단 라벨로 표시

### GPT 프롬프트

```
Create a clean SCOPE-AT-A-GLANCE infographic (16:9 widescreen) titled
"사업 업무 범위 한 장 구조도" with subtitle
"5개 컴포넌트 묶음으로 본 전체 업무 범위" in Korean.

This is a HIERARCHICAL TREE / GROUPED BOX diagram. Pure shapes + labels;
NO illustration of an excavator or any machinery.

LAYOUT — top-down hierarchy in 3 levels:

[LEVEL 0 — TOP CENTER, full width banner]
  Title block: "AI 기반 무인 자율 굴착기 디지털 트윈 플랫폼"
  Right side of banner: TWO small pillar tags side by side (small font):
    🟢 [기둥 A] OEM 신제품·변형 모델 개발 (정밀 모드)
    🟠 [기둥 B] 무인 자율 작업 AI 전이 (실시간 모드)
  Caption (smaller): "두 기둥이 아래의 같은 컴포넌트 자산을 공유"

[LEVEL 1 — 5 large grouped panels arranged left-to-right horizontally]
Each panel is a rounded rectangle with a thick colored header bar.
Panel header shows the GROUP NAME in large bold; below it is a row of
SMALLER child boxes (Level 2) representing individual research items.

  PANEL ① "건설기계 장비 모델" (header color: navy blue #1565C0)
    Subtitle: "굴착기·로더·1종 — 3종"
    Children (small boxes, 1 row of 5):
      [멀티바디 (MBD)<br/>붐·암·버킷·차체]
      [유압 모델<br/>펌프·MCV·실린더]
      [파워트레인<br/>엔진·트랜스미션]
      [제어기<br/>VCU·ECU·HCU]
      [주행 시스템<br/>트랙·휠·구동]

  PANEL ② "작업 환경" (header color: brown #8D6E63)
    Subtitle: "가상 작업장 + 토사"
    Children (small boxes, 1 row of 4):
      [지면·지형<br/>(DEM/메쉬)]
      [토사 모델 3종<br/>진흙·모래·자갈]
      [날씨·조도·시야]
      [장애물·BIM 객체]

  PANEL ③ "작업 시나리오·자율 공정" (header color: green #43A047)
    Subtitle: "TB 환경 한정 · Unified Planner"
    Children (small boxes, 1 row of 3):
      [작업 시나리오 명세]
      [자율 공정 계획<br/>(터파기·상차)]
      [3개 모드 동작<br/>학습데이터·실차지령·무인실행]

  PANEL ④ "통신·실차 인터페이스" (header color: orange #FF9800)
    Subtitle: "가상 ↔ 실차 다리 (실시간 ms급)"
    Children (small boxes, 1 row of 5):
      [통신·동기화<br/>(실시간 ms급)]
      [Sim2Real 전이<br/>+ 디지털 섀도우]
      [실차 retrofit<br/>센서·통신]
      [실증 시험장<br/>토사 베드]
      [DT 통합 플랫폼 SW<br/>+ 정밀도 모드 관리자]
    (Note: DT 통합 플랫폼 SW 박스를 이 패널 우측에 약간 더 크게 — backbone 역할)

  PANEL ⑤ "학습·검증" (header color: red #E53935)
    Subtitle: "AI 학습 + V&V + 실차 검증"
    Children (small boxes, 1 row of 5):
      [가상 학습 데이터<br/>수집]
      [실차 학습 데이터<br/>수집 ⭐ 사업 fuel]
      [가상 AI 정책 학습<br/>(RL/IL)]
      [Sim2Real 적응<br/>+ 4단계 안전]
      [성능 시험<br/>DT 검증 + 4단계 실차 캠페인]

[LEVEL 2 INSIDE EACH CHILD BOX]
- 첫 줄: 컴포넌트 한글 이름 (bold)
- 둘째 줄(작게): 핵심 키워드 1~2개

[LEVEL 3 — BOTTOM STRIP, full width, thin] (선택)
한 줄 caption만:
  "DT 플랫폼 = 5개 컴포넌트 묶음의 통합 — 두 기둥(OEM 신제품 / 무인 자율 작업)이 같은 자산을 공유"

STYLE:
- Pure block / grouped box infographic — system architecture style
- Rounded rectangles with thin colored borders, soft white/light fills
- All labels in Korean (English in parens for industry terms only)
- Color usage:
  - PANEL header bar: vivid color per panel
  - Child box border: thin grey, white fill, no badges/chips
- Background: white with very subtle grid
- Typography: bold sans-serif Korean for panel headers, regular for items,
  small grey for sub-keywords
- Aspect ratio: 16:9 widescreen for slides

AVOID:
- ANY illustration of an excavator, machinery, construction site, BIM, drone
- Photorealistic rendering, 3D effects, decorative shadows
- Arrows between panels (this is a SCOPE map, not a flow diagram —
  flow is shown in 다른 다이어그램 separately)
- Cluttered text inside child boxes (max 2 lines, no chips/badges)
- Any reference to 사업 항목 번호, 기관 식별 색상, 예산 수치 (이 다이어그램은 *컴포넌트 범위*만 표현)
- Any reference to "사업화·양산·BIM·외부 측량" (out of scope per TRL 3~5)
```

### 수정 지시 예시

- "패널 ④의 *DT 통합 플랫폼 SW* 박스를 가장 크게, *모든 패널 아래로 backbone 띠*가 깔리는 형태로 재배치"
- "각 child box를 더 크게, 멀리서도 컴포넌트 이름이 읽히게"
- "패널별 *행(row) 안에 child box 5개 이상이면 2행*으로 자동 줄바꿈"
- "패널 ⑤의 *실차 학습 데이터*에 ⭐ 강조 — '사업 fuel' 라벨이 한눈에 들어오게"
- "최상단 banner의 *두 기둥 A/B 태그*를 작게 — *제목 무게의 30%*. 본문(컴포넌트)이 주인공"
- "child box 안에 chip·뱃지·색사각형을 절대 넣지 말 것 — 컴포넌트 이름과 키워드만"

### 사용 시 주의

- **첫 페이지 / 표지 다음 페이지** 전용. 디테일 흐름은 다른 다이어그램으로 분리해 후속 슬라이드에 배치
- **신규 합류 연구원·외부 청자**에게는 이 한 장만으로 *"이 사업이 무엇을 만드는지(5개 컴포넌트 묶음)"*가 즉시 전달됨
- HDX·OEM 미팅 시: *PANEL ① 장비 모델*을 짚으며 *"이 5개 하위 모듈이 파라미터화되어 신차·변형 모델로 자동 확장됨(기둥 A)"*
- 심지·SW 주관 후보 미팅 시: *PANEL ④의 DT 통합 플랫폼 SW backbone* + *PANEL ⑤의 학습 인프라*가 SW 주관 영역
- KITECH·대학 미팅 시: *PANEL ② 토사 모델 3종*만 색칠 강조한 변형본 만들기
- GPT 결과가 너무 빽빽하면 *수정 지시 3번* (자동 줄바꿈) 적용
- 한글 깨지면 PPT/Visio에서 텍스트만 다시 입력 (다른 프롬프트와 동일)
- **항목 번호·기관 색상·예산은 의도적으로 배제** — 책임·예산은 별도 자료(한장 사업구조도)로 분리해 *기술 컴포넌트 범위*에 시선이 집중되도록

### 변형 활용

같은 프롬프트의 골격을 유지한 채, *대상 청자별*로 패널 강조 변형:

| 청자 | 강조 패널 | 어떻게 |
|---|---|---|
| HDX·OEM | ① 장비 모델 | 패널 ① 색을 진하게, 나머지 회색 톤 다운 |
| 심지·SW 후보 | ④ 통신·플랫폼 | 패널 ④의 DT 통합 플랫폼 SW box를 배 크기로 |
| KITECH·대학 | ② 작업 환경(토사) | 패널 ②의 *토사 3종* child box를 강조 |
| AI 기업 | ⑤ 학습·검증 | 패널 ⑤만 컬러, ①~④는 그레이스케일 |
| 평가위원 | 전체 균형 | 변형 없이 원본 사용 |

---

## 9a. DT 내부 컴포넌트 한 장 구성도 (좁은 DT — DT 자산만)

### 목적

**기술 관점**에서 *DT 플랫폼 자체가 무엇으로 구성되어 있고, 내부 컴포넌트가 어떻게 연결되는가*를 한 장으로. *DT 외부의 실차·학습 인프라는 명시적으로 제외* — 그 부분은 **#9b** (DT ↔ 외부 시스템 통합)에서 다룸.

청자: 신규 엔지니어 온보딩, 기술 검토회의 첫 장, *"DT 플랫폼의 내부 부품과 연결"*을 보여주고 싶을 때.

기존 다이어그램과의 분업:
- #1 = 비전·사이클 (Sim2Real 사이클 한 장)
- #2 = DT 플랫폼 모듈 (입출력 중심)
- #7 = 건설기계 내부 multi-physics 결합 (모듈 간 control loop)
- #8 = 업무 범위 (5개 컴포넌트 묶음, 연결 흐름 없음)
- **#9a = DT 내부 컴포넌트·연결 (좁은 DT만)** ← 본 섹션
- **#9b = DT ↔ 외부 시스템 통합 (실차·학습 인프라 포함)** ← 다음 섹션

### 핵심 메시지

- **좁은 DT** = sim 엔진이 돌고, 가상 모델이 살아있고, DT 자체 SW가 동작하는 영역만
- 4개 영역으로 구성 — ① 장비 모델 ② 작업 환경 ③ 시나리오·계획 ④ DT 인터페이스 SW (통신·Sim2Real 변환·디지털 섀도우)
- **DT 자산이 아닌 것은 zone 외부에 ⚪ 회색 stub로만 표시** (실차 retrofit·실차 데이터·실차 캠페인·GPU 학습 compute·안전 레이어 등은 #9b에서)
- 사용자 멘탈 모델에서 자주 누락되는 **3개 핵심 DT 카테고리** 부각: ⓐ 센서 모델 (가상) ⓑ 정밀도 모드 관리자 ⓒ Sim2Real 변환기 SW (DT 측)

### GPT 프롬프트

```
Create a clean TECHNICAL COMPONENT & CONNECTION MAP (16:9 widescreen) titled
"디지털 트윈 내부 컴포넌트 · 연결 구성도 (좁은 DT)" with subtitle
"DT 플랫폼 자체의 부품과 연결만 — 외부 시스템(실차·학습 인프라)은 #9b 참조" in Korean.

This is a SYSTEM-LEVEL BLOCK DIAGRAM with directional flow arrows.
Pure shapes + labels + arrows; NO illustration of an excavator or machinery.
SCOPE: only show DT platform internals. External elements (실차 retrofit, 실차
데이터, GPU 학습 compute, 실차 4단계 캠페인, 안전 레이어 실차 측) are deliberately
excluded — they belong in #9b.

LAYOUT — 4 zones (DT-internal only) + boundary stubs for external interfaces:

[ZONE ① — TOP CENTER, narrow band] "작업 시나리오 · 자율 공정 계획 (DT 위 모듈)"
  2 inline boxes (시나리오 명세는 zone 외부 stub로):
    [Unified Planner<br/>(터파기·상차)]  [공정 모드<br/>학습/지령/실행]
  External stub (small grey, above this zone, dashed border):
    ⚪ "외부 입력 — 작업 시나리오 명세 (#9b 참조)"
  Outgoing arrow (downward, label "작업 명령 / 목표 자세") flows into ZONE ②

[ZONE ② — UPPER MIDDLE, LARGEST PANEL] "건설기계 DT 모델 (CORE)"
  Wide rounded panel with thick navy border. Inside, 5 child boxes in one row:
    [멀티바디 (MBD)<br/>강체·관절·구속<br/>붐·암·버킷·차체]
    [유압 모델<br/>펌프·MCV·실린더<br/>로드센싱]
    [파워트레인<br/>엔진·트랜스미션]
    [제어기<br/>VCU·ECU·HCU<br/>CAN-FD]
    [주행 시스템<br/>트랙(스프로킷·롤러)<br/>또는 휠·차축]
  
  Internal control loop arrow (small, inside the panel):
    ECU → MCV → 실린더 → MBD → (관절 피드백) → ECU  
  Label this small inline: "내부 control loop (자세한 결합은 #7 참조)"

[ZONE ③ — LOWER MIDDLE, WIDE PANEL] "작업 환경 (가상)"
  Wide rounded panel with brown border. Inside, 5 child boxes in one row:
    [지면·지형<br/>(DEM·메쉬)]
    [토사 모델 3종<br/>진흙(SPH)·모래·자갈(DEM)]
    [날씨·조도·시야]
    [장애물·BIM 객체]
    [⭐ 센서 모델 (가상)<br/>카메라·LiDAR·IMU<br/>압력·엔코더]
  
  Note: 센서 모델 박스는 노란색 강조 테두리 ("쉽게 빠뜨리는 핵심" 라벨)

  Connection between ZONE ② ↔ ZONE ③ (vertical, bidirectional, prominent):
    ZONE ② → ZONE ③ : "버킷 운동 / 트랙 접지" (blue arrow)
    ZONE ③ → ZONE ② : "지면·토사 6축 반력 / 가상 센서 측정값" (THICK red arrow)
  This bidirectional pair is THE KEY visual coupling — make it visually prominent.

[ZONE ④ — RIGHT SIDE, vertical panel] "DT 인터페이스 SW (외부 시스템 facing)"
  Tall narrow panel with orange border. Inside, 4 child boxes stacked vertically
  (ALL DT-side software — no 실차 hardware):
    [통신 · 동기화 SW<br/>실시간 ms급 (≤ 100ms 목표)]
    [정책 배포 모듈<br/>모델 패키징·버전 관리<br/>수동/LAN/SD (OTA 불필요)]
    [디지털 섀도우<br/>실시간 거울 동기화]
    [데이터 게이트웨이<br/>가상 rollout 출력 / 실차 텔레메트리 입력]
  
  Note: Sim2Real *학습 기법*(DR·SysID·DA·Residual)은 ZONE ⑤ + 외부 GPU에서 실행됨.
        ZONE ④에는 *배포·변환·통신* SW만.
  
  This panel sits to the RIGHT of Zones ② and ③, acting as DT's facing layer
  toward external systems. External counterparts are STUBS (not in this diagram):
    ⚪ "→ 실차 시스템 (#9b)"     (right of this panel, dashed grey arrow out)
    ⚪ "→ AI 학습 인프라 (#9b)"  (right of this panel, dashed grey arrow out)

[ZONE ⑤ — BOTTOM, NARROWED PANEL] "DT 학습·검증 모듈 (코드/알고리즘만)"
  Narrower rounded panel with red border. Inside, 3 child boxes in one row
  (DT-side algorithm modules — actual GPU compute and 실차 캠페인은 #9b):
    [가상 학습 데이터<br/>생성 모듈<br/>(sim rollout + Domain Randomization)]
    [정책 학습 + Sim2Real 학습 기법<br/>RL/IL · DR · DA · Residual 코드<br/>(compute는 외부)]
    [⭐ DT V&V 분석<br/>sim 거동 vs 실측 비교<br/>+ 시스템 식별 보정<br/>(실차 캠페인은 #9b)]
  
  Note: V&V 분석 박스도 노란색 강조 테두리

  Inflows / outflows of ZONE ⑤:
    ZONE ②③ → 가상 데이터 (downward arrow, label "시뮬 실행 → rollout")
    ZONE ④ 데이터 게이트웨이 → 가상 데이터 출력 (right arrow, label "rollout 외부 NAS로")
    ⚪ "← 외부 GPU compute (#9b)"  (dashed arrow into 정책 학습 알고리즘)
    ⚪ "← 실차 측정값 (#9b)"        (dashed arrow into V&V 분석)
    ZONE ⑤ → ZONE ④ : "학습된 정책 (eval / 실차 배포)"  (upward arrow)

[CROSSCUTTING BAND ⓐ — LEFT EDGE, vertical thin strip] "🎚 정밀도 모드 관리자"
  Tall thin vertical band on LEFT edge spanning Zones ②③④⑤.
  Shows 3 mode tags stacked: [정밀(OEM)] [실시간(AI)] [도메인 mix]
  Caption rotated 90° (small): "한 모델 자산이 정밀↔실시간 자동 전환 (전 DT 영역 관통)"
  Use dashed green border to suggest "관통".

(NOTE: 안전 레이어 crosscutting band 제거 — 안전 레이어는 *실차 탑재* 모듈로
 #9b의 실차 시스템에서 다룸. DT 자체는 안전 레이어 *학습/검증*만 수행.)

[BOTTOM LEGEND — full width, ~7% height]
Two rows:
  Row 1 — 화살표 종류 (4 swatches):
    ▬▬▬ 파란 thick     = 가상 운동 / 제어 명령
    ▬▬▬ 빨간 thick      = 가상 반력 / 측정값
    ─ ─ ─ 점선 초록   = 정밀도 모드 적용 (DT 전 영역 관통)
    ─ ─ ─ 점선 회색   = 외부 시스템 인터페이스 (#9b로 연결)

  Row 2 — DT 자산에서 자주 빠뜨리는 3 카테고리 (작은 강조):
    ⭐ 센서 모델 (가상, Zone ③) | ⭐ 정밀도 모드 관리자 (Band ⓐ) |
    ⭐ Sim2Real 변환기 SW (Zone ④, DT 측만)

STYLE:
- Pure technical block diagram — system architecture / P&ID style
- Rounded rectangles with thin colored borders, white/very-light fills
- All labels in Korean (English in parens for industry terms)
- Color usage:
  - Zone ① (시나리오): light green header (#A5D6A7)
  - Zone ② (장비 모델, CORE): navy blue (#1565C0) thick border, largest, central
  - Zone ③ (환경): brown (#8D6E63)
  - Zone ④ (DT 인터페이스 SW): orange (#FF9800)
  - Zone ⑤ (학습·검증 모듈): red (#E53935)
  - Crosscutting band ⓐ: dashed green
  - External stubs (⚪): light grey, dashed border, "외부 → #9b" label
  - Highlighted boxes (⭐ 센서모델·V&V): yellow (#FFC107) thick border
- Background: white with very subtle grid
- Typography: bold sans-serif Korean for zone headers, regular for child boxes,
  small italic for sub-keywords
- Aspect ratio: 16:9 widescreen for slides

AVOID:
- ANY illustration of an excavator, machinery, construction site
- Photorealistic rendering, 3D effects, decorative shadows
- Crossing arrows that hurt readability — re-route around panels
- Cluttered text inside child boxes (max 3 lines per box, NO chips/badges)
- Confusing #9a with #8 — #9a must show ARROWS (flow), not just grouped boxes
- Confusing #9a with #7 — #9a is DT-wide overview, not internal MBD detail
- INCLUDING any 실차 측 elements (실차 retrofit, 실차 데이터 수집, 실차 4단계
  캠페인, 안전 레이어 실차 모듈, GPU 학습 클러스터 자체, NAS 스토리지 자체) —
  these are ALL in #9b. In #9a they appear ONLY as ⚪ external stubs labeled
  "(→ #9b)".
- ANY 사업 항목 번호 (#1~#15), 기관 식별 색상 (🟧🟦🟩🟪🟨), 예산 수치 (X억·X%),
  KPI 코드 (P5·G1/P1·G2/P4 등)
- Reference to BIM 통합·드론 측량·양산 (out of scope per TRL 3~5)
```

### 수정 지시 예시

- "ZONE ② (장비 모델 CORE)를 화면의 *시각적 무게 중심*에 — 다른 영역보다 두 배 크기로"
- "ZONE ②↔③ 사이의 *6축 반력 화살표*를 가장 굵게, 시선이 가장 먼저 가는 요소로"
- "⭐ 표시 박스(가상 센서모델·정밀도모드·Sim2Real 변환기 SW·DT V&V 분석)를 *노란색 강조 테두리* + *작은 ⭐ 아이콘*"
- "Crosscutting band ⓐ(정밀도 모드)를 *왼쪽 edge 전체에 세로 띠*로 — 모든 DT 영역을 관통하는 시각 효과"
- "외부 stub ⚪는 *zone 외부에 작은 점선 박스*로 — 본문(DT 자산)과 시각적으로 명확히 구분, *(→ #9b)* 라벨로 다른 다이어그램 참조"
- "각 child box를 더 크게, *컴포넌트 이름이 멀리서도 한눈에* 들어오게 (chip·뱃지·색사각형은 절대 추가 금지)"

### 사용 시 주의

- **기술 검토회의 첫 슬라이드** 또는 **신규 엔지니어 온보딩 1번 자료** 전용
- 본 다이어그램은 *DT 플랫폼 자체의 부품과 연결*만 보여줌. **실차·학습 인프라·실차 캠페인은 #9b 참조**
- ※ **"Sim2Real 전이"의 학술적 의미**(Domain Randomization·System Identification·Domain Adaptation·Residual Policy 등)는 ZONE ⑤(학습 코드) + 외부 GPU(#9b)에 분산. ZONE ④의 *"정책 배포 모듈"*은 학습 결과의 *전달*만 담당
- ※ **국책과제 TRL 3~5에서는 OTA 인프라 불필요** — 시험장 LAN/SCP/SD 카드 swap 등 간이 수단으로 충분 (full OTA는 fleet 운영 단계에서 필요)
- HDX·OEM 미팅 시: ZONE ②(장비 모델)의 *5개 sub-module*을 짚으며 *"각 sub-module이 OEM 신차 파라미터 입력으로 자동 확장됨(기둥 A — #7과 연계)"*
- KITECH·CAE 후보 미팅 시: ZONE ②↔③의 *bidirectional 6축 반력 결합*을 짚으며 *"이 환류가 multi-physics의 핵심 난도"*
- 심지·SW 주관 후보 미팅 시: ZONE ④(DT 인터페이스 SW) + 좌측 *정밀도 모드 관리자*를 짚으며 *"backbone이 두 기둥 모두 떠받침"*
- AI 기업 미팅 시: ZONE ⑤의 *정책 학습 알고리즘 코드*만 강조 + *"compute·NAS·실차 배포는 #9b에서"* 보충
- 평가위원 발표 시: 본 다이어그램으로 *DT 자체의 정의*를 명확히 한 뒤, #9b로 *외부 통합*까지 보여 줄 것

### 변형 활용

| 청자 | 강조 영역 | 어떻게 |
|---|---|---|
| HDX·OEM | ZONE ② | 장비 모델 panel을 1.5배로, 다른 영역 옅은 톤 |
| KITECH·대학 | ZONE ②↔③ 결합 | 6축 반력 화살표를 두 배 굵기 |
| 심지·SW 후보 | ZONE ④ + Band ⓐ | DT 인터페이스 SW 패널 + 정밀도 모드 띠 강조 |
| AI 기업 | ZONE ⑤ | 정책 학습 알고리즘 강조 + 외부 GPU stub 점선 강조 (#9b 안내) |
| 평가위원 | 전체 + ⭐ 강조 | 변형 없이 원본 + ⭐ 3개 박스 부각 |
| 비기술자 (공무원) | ZONE 라벨만 | 모든 sub-module을 회색으로, ZONE 헤더만 컬러 |

### #7·#9b와의 관계 (셋 다 사용할 때)

- **#7** = *ZONE ② 내부의 control loop를 줌인한 상세도* (한 대의 굴착기 multi-physics 결합)
- **#9a (본 섹션)** = *DT 플랫폼 자체의 4개 영역과 내부 연결* (좁은 DT)
- **#9b (다음 섹션)** = *DT ↔ 외부 시스템(실차·학습 인프라) 통합* (넓은 시스템 맥락)
- 발표 시퀀스: **#1(비전) → #8(업무 범위) → #9a(DT 내부) → #9b(외부 통합) → #2 또는 #7(영역 줌인)** 권장
- *항목 번호·기관·예산·KPI 코드*는 별도 자료(한장 사업구조도·KPI 매트릭스)로 분리. 이 다이어그램은 *기술 컴포넌트와 그 연결*에만 시선이 가도록

---

## 9b. DT ↔ 외부 시스템 통합 한 장 구성도 (시스템 맥락)

### 목적

**시스템 관점**에서 *DT 플랫폼이 어떤 외부 시스템과 어떻게 데이터·정책을 주고받는가*를 한 장으로. **#9a (좁은 DT)**가 답하지 못하는 질문 — *"학습은 어디서 돌고, 실차 데이터는 어디로 가고, 정책은 어떻게 배포되나"* — 을 시각화.

청자: 시스템 통합 명세 회의, IT 인프라 협의(NAS·GPU·정책 배포 방식), 1차년도 인터페이스 합의 회의, *"DT가 시스템 안에서 어떤 위치인가"* 설명.

### 핵심 메시지

- DT 플랫폼은 **3개 외부 시스템과 인터페이스**:
  - ⓐ **외부 입력원** (위) — 작업 시나리오·OEM 도면·토사 실측·실차 보유 사양
  - ⓑ **AI 학습 인프라** (좌) — NAS/데이터레이크·GPU 학습 클러스터·모델 레지스트리 *(별도 머신)*
  - ⓒ **실차 시스템** (우) — 실차 retrofit·실증 시험장·실차 텔레메트리·4단계 시험 캠페인·실차 탑재 안전 레이어
- DT는 *중앙 허브*로서 sim 실행·데이터 생성·디지털 섀도우·정책 평가만 담당
- *학습 compute는 별도 GPU 머신*, *실차 동작은 별도 하드웨어* — DT 외부지만 *DT 데이터에 의존*하는 시스템

### GPT 프롬프트

```
Create a SYSTEM INTEGRATION MAP (16:9 widescreen) titled
"DT ↔ 외부 시스템 통합 구성도" with subtitle
"DT 플랫폼이 외부 입력원·AI 학습 인프라·실차 시스템과 어떻게 연결되는가" in Korean.

This is a HUB-AND-SPOKE system diagram. Pure shapes + labels + arrows;
NO illustration of an excavator or machinery.

LAYOUT — DT in center, 3 external system clusters around it:

[CENTER — LARGE HUB BOX] "DT 플랫폼 (좁은 DT, 상세는 #9a)"
  Single large rounded panel with thick navy border, occupying ~30% center area.
  Inside, show as compact summary (small font, 4 inline labels):
    [장비 모델] [작업 환경] [DT 인터페이스 SW] [학습·검증 모듈]
  Caption (small, italic): "내부 컴포넌트 상세는 #9a 참조"
  This box is the gravity center — all arrows radiate from/to it.

[NORTH — TOP CLUSTER] "외부 입력원 (Static·Setup)"
  3 boxes arranged horizontally above the hub, light grey fills, dashed borders:
    [작업 시나리오 명세<br/>(OEM·시험기관)]
    [OEM 도면·사양<br/>(파라미터 입력)]
    [토사 실측 데이터<br/>(KITECH·대학)]
  Arrow direction: 위 → DT (downward)
  Arrow label: "초기 설정 / 파라미터 주입" (1회성, 사업 1차년도 baseline)
  Use thin solid grey arrows.

[WEST — LEFT CLUSTER] "AI 학습 인프라 (별도 GPU 머신)"
  Vertically stacked panel on the LEFT of the hub, 3 boxes:
    [📦 NAS / 데이터레이크<br/>가상·실차 데이터 통합 저장소<br/>(rollout·텔레메트리·체크포인트)]
    [🖥 GPU 학습 클러스터<br/>RL/IL forward·backward 연산<br/>(Isaac Lab 또는 분산)]
    [📋 모델 레지스트리<br/>정책 weights 버전 관리<br/>실차 배포 패키지 빌드]
  
  Bidirectional arrows between this cluster and DT center:
    DT → NAS  : "rollout / 시뮬 데이터 dump" (blue arrow)
    NAS → GPU : "학습 데이터 로드" (internal arrow within the cluster)
    GPU → 모델 레지스트리 : "체크포인트 저장" (internal arrow)
    모델 레지스트리 → DT : "학습된 정책 (eval)" (green arrow back to center)
    모델 레지스트리 → 실차 (East cluster) : "학습된 정책 배포 (수동·LAN·SD)"
      (long arrow crossing the diagram, dashed orange, prominently labeled)
      Caption (small italic, near arrow): "*국책과제 TRL 3~5 — OTA 인프라 불필요,
      시험장 LAN/SCP/SD swap으로 충분*"

  Caption below this cluster (small, italic):
    "*학습 compute는 DT가 아닌 별도 GPU 머신에서 실행*"

[EAST — RIGHT CLUSTER] "실차 시스템 (실세계 하드웨어 + 시험 인프라)"
  Vertically stacked panel on the RIGHT of the hub, 5 boxes:
    [🚜 실차 retrofit<br/>센서·통신 모듈·E-stop<br/>+ 안전 레이어 (실차 탑재)]
    [🏗 실증 시험장<br/>토사 베드·평탄지·다양 지형]
    [📡 실차 텔레메트리<br/>실차 센서·작업 데이터<br/>NAS로 업로드]
    [🛡 실차 탑재 안전 레이어<br/>L1 기구학 / L2 동력학<br/>L3 이상감지 / L4 페일세이프]
    [🎯 4단계 시험 캠페인<br/>Bench → 평탄 → 다양 → 야간/위험<br/>(KPI 90% 검증)]
  
  Bidirectional arrows between this cluster and DT center:
    DT → 실차 retrofit : "정책 지령 / 실시간 동기" (orange arrow, ms급)
    실차 텔레메트리 → DT : "실차 측정값 (디지털 섀도우 입력)" (THICK red arrow)
    실차 텔레메트리 → NAS (West) : "실차 학습 데이터 (모방학습 fuel ⭐)"
      (long arrow crossing diagram, blue dashed)
    4단계 캠페인 → DT V&V : "실측 ground truth" (red arrow back to center)
    4단계 캠페인 → 외부 산출물 : "KPI 90% 검증 보고서" (right arrow out)

  Caption below this cluster (small, italic):
    "*실차 하드웨어·캠페인은 DT 외부지만 DT 데이터에 의존*"

[SOUTH — BOTTOM, OUTPUTS] "외부 산출물"
  2 boxes at the bottom (light grey, dashed borders):
    [학습된 자율 작업 정책<br/>(실차 배포 완료)]
    [KPI 90% 검증 보고서<br/>(거동 일치도 + 무인 작업 성공률)]
  Inflows from the entire system, label: "사업 성과물"

[BOTTOM LEGEND — full width, ~7% height]
Two rows:
  Row 1 — 화살표 종류 (5 swatches):
    ▬▬▬ 파란     = 시뮬 / 학습 데이터 흐름
    ▬▬▬ 빨간 thick = 실차 측정값 / 반력 / V&V 비교
    ▬▬▬ 주황     = 실시간 동기 (ms급) / 정책 배포 (수동·LAN)
    ▬▬▬ 초록     = 학습된 정책 (eval/배포)
    ─ ─ ─ 점선 회색 = 외부 입력 (1회성·정적)

  Row 2 — DT vs 외부 경계 색상:
    🟦 DT 자산 (채운 색)  |  ⚪ 외부 시스템 (옅은 색·점선·⚠️)
    "DT는 sim·데이터 생성·섀도우·정책 평가만, 학습 compute와 실차 하드웨어는 외부"

STYLE:
- Pure system integration block diagram — hub-and-spoke / cloud architecture style
- Rounded rectangles with thin colored borders
- All labels in Korean (English in parens for industry terms)
- Color usage:
  - DT 중앙 허브: navy blue (#1565C0) thick border, white fill (DT 자산)
  - 외부 입력원 (North): light grey (#ECEFF1) fills, dashed border (외부)
  - AI 학습 인프라 (West): purple (#7B1FA2) borders, light fills (외부 인프라)
  - 실차 시스템 (East): orange (#FF9800) borders, light fills (외부 하드웨어)
  - 외부 산출물 (South): yellow (#FBC02D) accent, dashed (성과물)
  - DT 자산은 *채운 색 + 실선*, 외부는 *옅은 색 + 점선* — 시각적으로 명확히 구분
- Background: white with very subtle grid
- Typography: bold sans-serif Korean for cluster headers, regular for child boxes
- Aspect ratio: 16:9 widescreen for slides

AVOID:
- ANY illustration of an excavator, machinery, GPU rack, server room
- Photorealistic rendering, 3D effects, decorative shadows
- Showing internal DT structure in detail (that's #9a — keep DT center as
  a SUMMARY box only with 4 inline labels)
- Crossing arrows that hurt readability — re-route or use waypoint corners
- Cluttered text inside boxes (max 3 lines per box)
- ANY 사업 항목 번호 (#1~#15), 기관 식별 색상 (🟧🟦🟩🟪🟨), 예산 수치,
  KPI 코드 (P5·G1/P1·G2/P4) — focus on system topology only
- Blurring DT vs 외부 boundary — DT 자산은 *반드시* 채운 색·실선,
  외부는 *반드시* 옅은 색·점선
```

### 수정 지시 예시

- "중앙 DT 허브 박스를 더 크게 — 외부 cluster 박스보다 *시각적으로 무게중심*으로"
- "*모델 레지스트리 → 실차 정책 배포* 화살표를 가장 길고 굵게 — 학습 정책이 실차로 흘러가는 핵심 경로 (TRL 3~5 단계라 수동/LAN/SD 충분, OTA 불필요)"
- "*실차 텔레메트리 → NAS* 화살표를 ⭐로 강조 — 사업 fuel(#13 실차 학습 데이터)의 흐름임을 부각"
- "AI 학습 인프라 cluster 캡션 *'학습 compute는 별도 GPU 머신'*을 더 크게 — 1차년도 인프라 합의 시 핵심 메시지"
- "DT vs 외부 경계 — *채운 색 vs 점선*이 한눈에 구분되게, legend Row 2를 더 강조"
- "북·서·동·남 4방향 cluster 배치를 깨끗한 cross 형태로 — DT가 중심에 있고 외부 시스템이 사방에서 연결"

### 사용 시 주의

- **시스템 통합 명세 회의·IT 인프라 협의·1차년도 인터페이스 합의** 전용
- *#9a (좁은 DT)와 함께 사용*하는 것이 정석. #9a 후 바로 #9b로 *"DT 외부에 무엇이 있고 어떻게 묶이는가"* 설명
- 1차년도 시스템 통합 명세서 작성 시 **3개 인터페이스 합의 우선순위**:
  - ⓐ DT ↔ NAS 데이터 핸드오프 (포맷·schema·주기)
  - ⓑ NAS ↔ GPU ↔ 모델 레지스트리 (학습 인프라 소유·체크포인트 거버넌스)
  - ⓒ DT ↔ 실차 (통신 프로토콜·정책 배포 방식·디지털 섀도우 동기) — *국책과제 TRL 3~5는 OTA 불필요*
- 평가위원 발표 시: 본 다이어그램으로 *"우리 사업이 단순 시뮬이 아닌 *시스템 통합* 사업임"*을 부각
- AI 기업 미팅 시: West cluster (AI 학습 인프라) 색칠 강조한 변형본 — *학습 인프라 소유·운영 책임 명확화*
- OEM·시험기관 미팅 시: East cluster (실차 시스템) 색칠 강조한 변형본 — *retrofit·시험장·캠페인 책임 명확화*

### 변형 활용

| 청자 | 강조 cluster | 어떻게 |
|---|---|---|
| 시스템 통합 회의 | 전체 + 화살표 모두 | 변형 없이 원본 — 모든 인터페이스 보임 |
| AI 기업·SW | West (학습 인프라) | West cluster 진하게, 나머지 옅은 톤 |
| OEM·시험기관 | East (실차 시스템) | East cluster 진하게, 나머지 옅은 톤 |
| KITECH·대학 | North (외부 입력원) | 토사 실측 데이터 흐름 강조 |
| IT 인프라 담당 | NAS·GPU·정책 배포 화살표 | West-East 사이 *학습 데이터·정책 배포* 화살표를 두 배 굵기 |
| 평가위원 | 전체 + DT 중심성 | DT 허브 박스를 1.5배로, 외부 sleeves가 모두 DT에 의존함을 부각 |

### #9a와의 관계

- #9a = *DT 자체의 부품과 내부 연결* (좁은 DT, 4 zones)
- #9b = *DT가 외부와 어떻게 묶이는가* (넓은 시스템, hub-and-spoke)
- 함께 사용 시: #9a로 *"DT는 무엇인가"*를 정의 → #9b로 *"DT가 시스템에서 어떤 위치인가"* 보충
- 둘 다 *항목 번호·기관 색상·예산 미사용* 정책 일관

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
| v1.4 | 2026-05-07 | **#7 건설기계 DT 모델 구성도 신설** — 모든 미팅 공용. 한 장 레이아웃 3-zone 구조: Zone A 굴착기 멀티바디 결합 (유압·MCV·실린더·ECU·revolute joint) / Zone B 버킷-토사 6축 반력 (DEM 입자 + 환류) / Zone C 오른쪽 패널 (C1 파라미터 슬라이더 + 변형 모델 silhouette / C2 정밀도 모드 토글 + 도메인별 fidelity 바). 컬러 팔레트: 굴착기 오렌지 / 유압 블루 / ECU 그린 / 토사 브라운 / 반력 레드. 미팅별 활용 팁 추가. |
| v1.5 | 2026-05-07 | **#7 스타일 전면 재작성** — 굴착기 isometric 일러스트 → **순수 시스템 블록 다이어그램**(rounded boxes + 화살표 + legend). 사용자 요청 *"실제 예시 그리기보다 모듈별 연계와 구성을 심플하게 도식화"* 반영. Zone A: ECU → MCV → 실린더 → MBD → 관절 피드백 control loop / Zone B: MBD ↔ 토사 양방향 결합 (6축 반력 환류) / Zone C: 파라미터·정밀도 fan-out 주입 패널 / 하단 legend (5가지 화살표 종류). |
| v1.6 | 2026-05-09 | **#8 업무 범위 한 장 구조도 신설** — 사용자 요청 *"다른 사람들이 알기 쉽게 업무 범위를 이해하는 한 장"*. 컴포넌트 멘탈 모델(장비/환경/시나리오/통신/학습 5개 묶음)과 16개 항목·5개 기관 색상 코드를 결합한 hierarchical grouped-box 다이어그램. 신규 합류자·외부 미팅 첫 장 공용. 5개 청자별 강조 변형 표 포함. |
| v1.7 | 2026-05-09 | **#9 DT 컴포넌트·연결 한 장 구성도 신설** — 사용자 요청 *"디지털 트윈을 구성하는 컴포넌트와 연결요소를 이해하기 위한 프롬프트"*. #8(업무 범위)과 분리하여 *기술 관점*에서 5개 영역(장비/환경/시나리오/통신·Sim2Real/학습·검증) + 영역 간 5종 흐름 화살표 + 2개 횡단 띠(정밀도 모드·안전 레이어) + ⭐4개 강조 박스(센서모델·정밀도모드·V&V·Sim2Real 다리)를 결합. 신규 엔지니어 온보딩·기술 검토회의 첫 장. 6개 청자별 강조 변형 + #7과의 발표 시퀀스 권장. |
| v1.8 | 2026-05-09 | **#7~#9에서 *항목 번호·기관 색상·예산·KPI 코드* 일괄 배제** — 사용자 요청 *"항목 번호와 기관 색상, 예산등은 배재하고 싶다"*. #7은 이미 깨끗(변경 없음). #8: child box 옆 `← #X 🟦` 매핑·기관 예산·KPI 띠 모두 제거, AVOID에 명시적 금지 추가, child box는 컴포넌트 이름과 키워드만. #9: child box 안 `(#5)·(#13)·(P5 ≤100ms)` 등 제거, AVOID에 명시적 금지 추가. 제어기 약어 `VBO·FEH` → 표준 `VCU·ECU·HCU`로 변경 (HDX 사내 명명 미확인). |
| v1.9 | 2026-05-09 | **#9를 #9a + #9b로 분리** — 사용자 지적 *"기존 #9의 ZONE ④/⑤에 DT 자산이 아닌 실차·학습 인프라가 섞여 있다"*. **#9a = 좁은 DT (DT 자산만)** — ZONE ④에서 실차 retrofit 제거, ZONE ⑤에서 실차 학습 데이터·실차 캠페인·GPU compute 분리, 안전 레이어 crosscutting band 제거(실차 측 모듈이라 #9b로 이전). 외부 요소는 ⚪ stub로만 표시. **#9b 신설 = DT ↔ 외부 시스템 통합** — DT 중앙 허브 + 3방향 외부 cluster (북: 외부 입력원 / 서: AI 학습 인프라 NAS·GPU·모델 레지스트리 / 동: 실차 시스템 retrofit·시험장·텔레메트리·안전 레이어·4단계 캠페인 / 남: 외부 산출물). DT 자산은 채운 색·실선, 외부는 옅은 색·점선으로 시각적 경계 표현. 발표 시퀀스 갱신: #1 → #8 → #9a → #9b → #2/#7. |
| v2.0 | 2026-05-09 | **Sim2Real 배치 정정 + OTA 용어 일괄 제거** — 사용자 지적 2건. ① *"Sim2Real 전이가 왜 Bridge에 있나"* → 학술적 *Sim2Real 학습 기법*(DR·SysID·DA·Residual)은 ZONE ⑤(학습 코드)와 외부 GPU(#9b)에 분산, ZONE ④의 Bridge에는 *정책 배포 모듈*(weights 전달)만 남김. RFP의 모호한 "전이" 라벨이 학술 정의와 다르다는 점 캡션으로 명시. ② *"국책과제 TRL 3~5에 OTA는 배보다 배꼽"* → 다이어그램 9곳의 OTA → *"정책 배포 (수동·LAN·SD)"*로 일괄 정정. 모델 레지스트리도 *"실차 배포 패키지 빌드"*로 변경. 1차년도 합의 안건도 *"DT↔실차 통신·정책 배포 방식"* 으로 갱신. ※ 사용자 핵심 문서(사업기획·한장구조도·연계다이어그램)의 OTA 잔존은 별도 협의 후. |

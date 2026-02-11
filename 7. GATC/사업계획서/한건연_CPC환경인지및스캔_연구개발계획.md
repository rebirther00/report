# 한국건설기계연구원(한건연) CPC 환경 인지 및 현장 스캔 선행 기술 연구개발계획

> **과제명**: 스마트 컨스트럭션 구현을 위한 콘크리트펌프카 자율타설 시스템 개발  
> **한건연 연구 범위**: CPC 환경 인지(장애물 인지) 및 현장 스캔(작업량 추론) 선행 기술 개발  
> **연구 기간**: 2026년 4월 ~ 2028년 12월 (33개월)  
> **작성 기준**: 기존 CPC 단독 자율타설 연구 범위 축소·집중 버전

---

## 1. 연구 범위 재정의 배경

### 1.1 기존 계획의 문제점

기존 CPC 단독 자율타설 계획은 다음과 같은 광범위한 개발 항목을 포함하고 있었다.

- 붐 기구학 모델링 및 좌표 제어
- 작업자 티칭 시스템
- 경로 생성 알고리즘
- 현장 스캔 시스템
- 장애물 인지 안전 시스템
- 콘솔 UI/UX
- 시스템 통합 및 현장 실증

이는 한건연의 투입 가능 인력(연구원 3~4명, 풀타임 환산 약 0.6~0.8명/년) 및 예산 규모를 고려할 때 **33개월 내 모든 항목을 충실히 수행하기 어렵다**고 판단하였다.

### 1.2 집중 영역 선정 근거

CPC 자율타설 시스템의 실현을 위해 가장 기초가 되면서도, **독립적인 선행 기술 개발**이 가능한 두 가지 영역을 선정하였다.

| 영역 | 역할 | 선정 근거 |
|------|------|----------|
| **환경 인지 (안전)** | 붐 전개·운용 시 장애물 인지 | 자율 운용의 **안전 전제 조건**. 장애물 인지 없이 자율타설 불가 |
| **환경 스캔 (작업)** | 타설 현장 3D 스캔 → 필요 작업량 예측 + 달성량 확인 | 자율 경로 생성의 **입력 데이터 기반** + 타설 **품질 관리 기반** |

이 두 영역은 자율타설 시스템의 **필수 선행 기술**이며, 개발 성과물은 향후 기구학 제어, 경로 생성, 자동 타설 모듈과 통합 시 핵심 입력 모듈로 활용된다.

### 1.3 나머지 영역과의 관계

```
[한건연 담당 - 선행 기술]          [주관/타 기관 담당]
                                  
┌─────────────────────┐          ┌──────────────────────┐
│ 환경 인지 (안전)      │───────→│ 붐 제어 안전 연동      │
│ · 장애물 감지/분류     │         │ · 충돌 회피 경로 생성   │
│ · 다중센서 융합        │         │ · 비상정지 연동        │
└─────────────────────┘          └──────────────────────┘
                                  
┌─────────────────────┐          ┌──────────────────────┐
│ 환경 스캔 (작업)      │───────→│ 자율타설 경로 생성      │
│ · 3D 현장 맵 생성     │         │ · 티칭 기반 영역 설정   │
│ · 사전: 필요량 예측   │         │ · 타설 경로 최적화      │
│ · 사후: 달성량 확인   │───────→│ · 잔여 영역 재작업 판단  │
└─────────────────────┘          └──────────────────────┘
```

---

## 2. 시스템 구성

### 2.1 환경 인지 시스템 (장애물 인지)

> **목적**: CPC 붐 전개 및 자동 운전 중 주변 장애물을 실시간 인지하여 안전 사고 방지

#### (1) 다중 센서 융합 구성

| 센서 | 역할 | 특성 | 검지 범위 |
|------|------|------|----------|
| **3D LiDAR** | 주변 장애물 3D 형상 검지 | 고정밀 거리 측정, 날씨 영향 적음 | 중~장거리 (10~100m) |
| **레이더 (Radar)** | 장거리 장애물 검지, 이동체 속도 측정 | 우천·분진·야간 환경에서도 안정적 | 장거리 (50~200m) |
| **카메라 (Vision)** | 장애물 분류·식별 (사람/구조물/장비) | 색상·질감 정보, 객체 인식 AI 연동 | 중거리 (5~50m) |
| **초음파 (Ultrasonic)** | 근접 장애물 최종 확인 | 근거리 고신뢰 감지, 사각지대 보완 | 근거리 (0.3~5m) |

#### (2) 센서 융합 아키텍처

```
[LiDAR 포인트클라우드]──→ ┌──────────────────┐
[Radar 반사파]──────────→ │   센서 융합 엔진    │──→ [장애물 맵]
[카메라 영상]──────────→  │  (Sensor Fusion)   │──→ [위험도 판정]
[초음파 근접 데이터]────→  └──────────────────┘──→ [안전 명령 출력]
                                │
                         시간 동기화 + 좌표 변환
                         (각 센서 → 차량 기준 좌표계)
```

#### (3) 핵심 기능

- **장애물 검출(Detection)**: 다중 센서 데이터에서 장애물 후보 영역 추출
- **장애물 분류(Classification)**: 사람, 타워크레인, 전력선, 구조물, 차량 등 유형 분류
- **장애물 추적(Tracking)**: 이동 장애물의 위치·속도 추적 (칼만 필터 등)
- **위험도 평가(Risk Assessment)**: 붐 동작 경로와 장애물 간 간섭 가능성 판단
- **안전 신호 출력**: 경고(Warning) → 감속(Slow-down) → 정지(Stop) 단계별 출력

### 2.2 환경 스캔 시스템 (작업량 추론)

> **목적**: 타설 전 현장 3D 스캔으로 **필요 작업량(타설 체적)을 예측**하고, 타설 후 재스캔으로 **작업 진행량(달성량)을 확인**하는 시스템

#### (1) 운용 개념: 사전 스캔 → 타설 → 사후 스캔

본 시스템은 **실시간 모니터링이 아닌, 붐 위치 이동(크레인 이동) 전후의 이산적 스캔** 방식으로 운용한다.

```
[운용 시나리오]

① 사전 스캔 (Pre-Pour Scan)
   └─ 붐 전개 후, 타설 전에 엔드호스 부근 센서로 바닥 영역 스캔
   └─ 타설 필요 체적 예측 → 레미콘 투입 계획 기초 데이터

② 타설 작업 수행
   └─ 작업자 또는 시스템이 타설 수행

③ 사후 스캔 (Post-Pour Scan)
   └─ 타설 완료 후, 붐/크레인 위치 이동 전에 동일 영역 재스캔
   └─ 사전 맵과 사후 맵 비교 → 타설 달성량(체적 변화) 산출
   └─ 잔여 작업량 = 목표 체적 - 달성 체적

④ 반복 (다음 영역 이동)
   └─ 붐 이동 후 다음 영역에서 ①부터 반복
```

#### (2) 스캔 센서 구성

| 센서 | 역할 | 탑재 위치 |
|------|------|----------|
| **3D LiDAR** | 바닥면·철근부·타설면 3D 형상 취득 | 붐 선단(엔드호스 부근) |
| **스테레오 카메라** | 질감·색상 정보 보완, 철근/콘크리트면 구분 | 붐 선단(엔드호스 부근) |

#### (3) 작업량 추론 파이프라인

```
[붐 선단 센서]
    │
    ▼
[3D 포인트 클라우드 취득] ← 붐 이동 시 연속 스캔
    │
    ▼
[포인트 클라우드 정합(Registration)] ← ICP/NDT 알고리즘
    │
    ▼
[바닥면 추출 및 영역 분할]
    │
    ├─→ [철근 배근 영역 인식] ← 카메라 AI 보조 분류
    │
    ▼
[3D 환경 맵 생성]
    │
    ├─────────────────────────────────────────┐
    │                                         │
    ▼                                         ▼
[사전 스캔 맵 (Pre-Pour)]            [사후 스캔 맵 (Post-Pour)]
    │                                         │
    ▼                                         ▼
[필요 체적 예측]                      [맵 차분(Differencing)]
    │                                         │
    ▼                                         ▼
[필요 물량 출력]                      [달성량 산출 + 잔여량 계산]
 · 필요 콘크리트(㎥)                   · 타설 달성 체적(㎥)
 · 레미콘 대수 예측                    · 잔여 미타설 체적(㎥)
                                      · 달성률(%)
```

#### (4) 핵심 기능

- **3D 환경 맵 생성**: 붐 이동 중 연속 스캔 → 포인트 클라우드 정합 → 통합 3D 맵
- **바닥면 자동 추출**: 지면/철근부 평면 검출 및 영역 분할
- **기존 구조물 인식**: 기둥, 벽체, 슬래브 개구부 등 비타설 영역 자동 식별
- **사전 스캔: 필요 체적 예측**: 타설 영역 면적 × 설계 두께 → 필요 콘크리트 물량 산출
- **사후 스캔: 달성량 확인**: 타설 전/후 3D 맵 차분 → 실제 타설 체적 산출, 잔여량 계산
- **레미콘 투입 계획 기초 데이터 제공**: 필요량 및 잔여량 기반 레미콘 추가 투입 판단

---

## 3. 연차별 개발 목표 및 내용

### [공동연구개발기관2(한국건설기계연구원)]

---

### 3.1 1차년도 (2026.04 ~ 2026.12, 9개월)

#### ① 개발 목표

**다중 센서 융합 장애물 인지 시스템 설계 및 현장 스캔 센서 선정·기본 알고리즘 설계**

- 환경 인지용 **다중 센서(LiDAR, Radar, Camera, Ultrasonic) 선정** 및 융합 아키텍처 설계
- CPC 붐 환경에서의 **센서 배치 설계** 및 설치 방안 수립
- 장애물 **검출·분류 알고리즘 기본 설계** 및 벤치마크 환경 구축
- 현장 스캔용 **LiDAR + 카메라 센서 선정** 및 3D 맵 생성 기본 알고리즘 설계
- 타설 **작업량 추론(필요량 예측 + 달성량 확인) 알고리즘 개념 설계**

#### ② 개발 내용 및 범위

**(가) 환경 인지 센서 시스템 설계**

- CPC 붐 운용 환경 분석 및 센서 요구사항 정의
  - 붐 전개 높이(50~75m), 회전 반경, 진동 환경 분석
  - 검지 대상 장애물 유형 정의 (작업자, 타워크레인, 전력선, 구조물, 차량 등)
  - 센서별 검지 범위·분해능·갱신 주기 요구사항 도출
- 다중 센서 선정 및 사양 검토
  - 3D LiDAR: 소형·경량, 내진동, IP67 이상, 스캔 각도·해상도 비교
  - 밀리미터파 레이더: 장거리 검지(100m+), 이동체 속도 측정, 우천 내성
  - 산업용 카메라: FHD 이상, WDR, 야간 대응, AI 추론 가능 프레임레이트
  - 초음파 센서: 근거리(5m 이내), 사각지대 보완용, 내분진·내수
- 센서 융합 아키텍처 설계
  - 시간 동기화 방안 (PTP/NTP 기반 센서 간 타임스탬프 동기)
  - 좌표 변환 체계 (각 센서 좌표 → CPC 차량 기준 좌표계)
  - 데이터 버스 및 처리 플랫폼 설계 (ROS2 기반 메시지 프레임워크)
- CPC 붐 장착 위치 및 배치 방안 설계
  - 붐 선단(엔드호스 부근): LiDAR + 카메라 (전방 감시 + 하방 스캔)
  - 붐 중간 링크: 레이더 (측방 장거리 감시)
  - 붐 기부(베이스): 초음파 (근접 장애물 최종 확인)
  - 센서 마운트 방진·방수 설계 검토

**(나) 장애물 검출·분류 알고리즘 기본 설계**

- 장애물 검출 알고리즘 컨셉 설계
  - LiDAR 포인트 클라우드 기반 장애물 클러스터링 (DBSCAN, 유클리드 클러스터링 등)
  - 레이더 반사파 기반 이동체 검출 (CFAR 알고리즘)
  - 카메라 영상 기반 객체 검출 (YOLO/SSD 계열 딥러닝 모델)
- 센서 융합 알고리즘 컨셉 설계
  - Early Fusion vs Late Fusion vs Mid-level Fusion 비교·선정
  - 각 센서 검출 결과의 신뢰도 기반 가중 융합 방안
  - 센서 고장/불량 시 Degraded Mode 운용 설계
- 벤치마크 환경 구축
  - 실내 테스트 환경: 표준 장애물(더미) 배치, 센서 단품 성능 측정
  - 시뮬레이션 환경: Gazebo/CARLA 등 3D 시뮬레이터에서 센서 모델링

**(다) 현장 스캔 센서 선정 및 3D 맵 생성 기본 설계**

- 붐 선단 탑재 스캔 센서 검토 및 선정
  - 소형·경량 3D LiDAR: 무게, 스캔 범위, 해상도, 내환경성 비교
  - 스테레오 카메라: 해상도, 깊이 측정 정확도, 프레임레이트
  - 붐 진동·움직임 환경에서의 센서 안정성 평가 방안
- 3D 포인트 클라우드 처리 기본 알고리즘 설계
  - 포인트 클라우드 전처리: 노이즈 제거, 다운샘플링, 관심 영역 필터링
  - 포인트 클라우드 정합(Registration) 알고리즘 선정 (ICP, NDT, LOAM 등)
  - 바닥면 추출 알고리즘 컨셉 (RANSAC 평면 검출)
- 작업량 추론 알고리즘 개념 설계
  - **사전 스캔(필요량 예측)**: 바닥 면적 × 설계 두께 − 기존 구조물 체적 모델
  - **사후 스캔(달성량 확인)**: 타설 전/후 3D 맵 차분(Differencing) 기반 체적 변화량 산출 개념
  - 운용 시나리오 정의: 사전 스캔 → 타설 → 사후 스캔(크레인 이동 전) → 다음 영역 이동
  - 바닥 면적 계산 방법론 (2D 투영 면적, 3D 메시 면적)
  - 설계 두께 입력 연동 방식

#### ③ 1차년도 대표 그림

**[그림 프롬프트 1: CPC 환경 인지 다중 센서 배치도]**

> 프롬프트: "Technical diagram showing multi-sensor placement on a concrete pump car (CPC) for obstacle detection. Show a concrete pump car with multi-joint boom extended. Sensor positions marked with icons and labels: (1) At boom tip - 3D LiDAR (blue) and industrial camera (green) looking forward and downward; (2) At mid-boom joint - millimeter-wave radar (orange) for long-range side detection; (3) At boom base - ultrasonic sensors (purple) for close-range detection. Around the CPC, show concentric detection zones: ultrasonic zone (0-5m, purple shading), LiDAR+camera zone (5-50m, blue/green shading), radar zone (50-200m, orange shading). Include obstacle examples: worker (near), tower crane (mid), power lines (far). Arrows showing sensor coverage angles. Bottom: sensor fusion data flow from all sensors to fusion engine to safety output. Clean technical illustration, Korean and English labels, white background."

**[그림 프롬프트 2: 현장 스캔 및 작업량 추론 개념도]**

> 프롬프트: "Technical concept diagram for construction site scanning with pre-pour and post-pour comparison. Show a concrete pump car boom with LiDAR and stereo camera at the tip. Two-phase layout: LEFT 'Pre-Pour Scan' - boom scanning downward onto a construction floor with visible rebar grid, point cloud of bare floor, area segmentation (pour zone blue, columns red, walls gray), volume calculation showing floor area × design thickness = required volume with concrete truck estimate. RIGHT 'Post-Pour Scan' - same area after concrete pouring, boom rescanning before crane moves, new point cloud showing concrete surface (higher elevation), 3D map differencing visualization (before vs after overlay with height change in color gradient). Bottom center: comparison dashboard showing 'Required: 5.2m³', 'Achieved: 4.8m³', 'Remaining: 0.4m³', 'Achievement: 92%' with progress bar. Clean technical illustration, Korean labels, white background."

---

### 3.2 2차년도 (2027.01 ~ 2027.12, 12개월)

#### ① 개발 목표

**장애물 인지 핵심 알고리즘 개발 및 3D 환경 맵 기반 작업량 추론 시스템 구현**

- 다중 센서 융합 기반 **장애물 검출·분류·추적 알고리즘** 개발
- 센서 융합 엔진 구현 및 **실시간 장애물 인지 성능** 검증
- LiDAR+카메라 기반 **3D 환경 맵 생성 시스템** 구현
- 바닥면 추출 및 **타설 체적 자동 계산 + 타설 진행량 확인 시스템** 개발
- 실내 환경 및 **CPC 탑재 기초 시험** 수행

#### ② 개발 내용 및 범위

**(가) 장애물 검출·분류·추적 알고리즘 개발**

- LiDAR 기반 장애물 검출 알고리즘 구현
  - 3D 포인트 클라우드 클러스터링 및 바운딩 박스 추출
  - 지면(Ground) 제거 후 장애물 후보 영역 분리
  - 정적/동적 장애물 구분 (프레임 간 비교)
- 카메라 기반 객체 검출·분류 모델 개발
  - 건설현장 특화 학습 데이터셋 구축 (작업자, 크레인, 전력선, 비계, 차량 등)
  - 딥러닝 객체 검출 모델 학습 및 최적화 (YOLO v8/v9 또는 동급)
  - 엣지 디바이스(GPU 임베디드) 추론 최적화 (TensorRT 등)
- 레이더 기반 이동체 검출 알고리즘 구현
  - 밀리미터파 레이더 반사파 처리 및 물체 검출
  - 이동체 속도·방향 추정 (도플러 효과 활용)
- 다중 센서 융합 엔진 구현
  - 센서별 검출 결과 시간·공간 정합
  - 신뢰도 가중 융합 (LiDAR 거리 + 카메라 분류 + 레이더 속도)
  - 융합 결과 기반 장애물 리스트 출력 (ID, 유형, 위치, 속도, 크기)
- 장애물 추적 알고리즘 구현
  - 다중 객체 추적 (Multi-Object Tracking): 칼만 필터 + 헝가리안 매칭
  - 이동 장애물 경로 예측 (단기 궤적 추정)

**(나) 위험도 평가 및 안전 신호 출력 시스템 개발**

- 위험도 평가 로직 구현
  - 붐 동작 예상 경로와 장애물 위치 간 최소 거리 계산
  - 시간 기반 충돌 예측 (TTC: Time-To-Collision)
  - 위험도 레벨 정의: 안전(Safe) → 주의(Caution) → 경고(Warning) → 위험(Danger)
- 안전 신호 출력 인터페이스
  - 경고 단계: 시각/청각 경보 출력
  - 감속 단계: 붐 동작 속도 제한 명령 출력
  - 정지 단계: 즉시 정지 명령 출력
  - 인터페이스 프로토콜: CAN 또는 이더넷 기반 안전 명령 전송

**(다) 3D 환경 맵 생성 시스템 구현**

- 포인트 클라우드 정합 시스템 구현
  - 붐 이동 중 연속 스캔 데이터 정합 (ICP/NDT 알고리즘 구현)
  - IMU 데이터 연동을 통한 초기 자세 추정 보정
  - 점진적 맵 업데이트 (Incremental Mapping)
- 바닥면 추출 및 영역 분할 알고리즘 구현
  - RANSAC 기반 평면 검출 → 바닥면 자동 추출
  - 카메라 영상 AI 보조 분류 (철근 영역 vs 기타)
  - 기존 구조물(기둥, 벽체, 개구부) 자동 식별 및 영역 분리

**(라) 타설 체적 계산 및 진행량 확인 시스템 개발**

- 사전 스캔: 타설 필요 체적 자동 계산
  - 바닥면 3D 메시 → 2D 투영 면적 계산
  - 비타설 영역(기둥, 개구부 등) 자동 공제
  - 면적 × 설계 두께 → 필요 콘크리트 체적 자동 산출
  - 경사면/단차 반영 체적 보정
  - 레미콘 필요 대수 예측 (믹서 용량 고려)
- 사후 스캔: 타설 달성량 확인 시스템
  - 타설 후 동일 영역 재스캔 (붐/크레인 위치 이동 전 수행)
  - 사전 맵과 사후 맵의 3D 차분(Differencing) 알고리즘 구현
  - 표면 높이 변화량 기반 타설 체적 산출
  - 달성률 계산: 달성 체적 / 목표 체적 × 100%
  - 잔여 미타설 영역 및 체적 자동 식별

**(마) 실내 환경 및 CPC 탑재 기초 시험**

- 실내 시험
  - 센서 단품 성능 측정 (검지 범위, 정확도, 응답 속도)
  - 표준 장애물 검출·분류 정확도 평가
  - 3D 맵 생성 정확도 평가 (기준 환경 대비)
- CPC 탑재 기초 시험
  - 센서 CPC 붐 장착 및 진동/움직임 환경 테스트
  - 실외 환경 기본 성능 확인 (날씨, 분진, 조도 변화)

#### ③ 2차년도 대표 그림

**[그림 프롬프트 3: 다중 센서 융합 장애물 인지 시스템 구성도]**

> 프롬프트: "System architecture diagram for multi-sensor fusion obstacle detection on a concrete pump car. Show four sensor input streams at top: (1) 3D LiDAR - point cloud visualization with colored distance; (2) Radar - range-doppler plot showing moving objects; (3) Camera - image frame with bounding box detections (worker in yellow, crane in red, power line in orange); (4) Ultrasonic - proximity bar indicator. All streams flow into central 'Sensor Fusion Engine' box with sub-modules: time synchronization, coordinate transform, confidence-weighted fusion. Output flows to: (a) Obstacle Map - top-down view with colored obstacle positions and tracking trails; (b) Risk Assessment - danger zone visualization with boom trajectory overlay; (c) Safety Command Output - three-level output (Warning → Slow-down → Stop). Side panel shows edge computing unit processing all data in real-time. Clean technical diagram, Korean labels, white background."

**[그림 프롬프트 4: 3D 환경 맵 및 작업량 추론 시스템 구성도]**

> 프롬프트: "Technical system diagram for 3D environment mapping with pre-pour estimation and post-pour achievement verification. Two parallel pipelines: TOP PIPELINE 'Pre-Pour': (1) Scanning - boom tip sensors scanning bare floor with rebar; (2) Point cloud processing and 3D map of rebar floor; (3) Volume estimation - area × thickness = required volume, concrete truck count. BOTTOM PIPELINE 'Post-Pour': (1) Re-scanning same area after concrete pouring (before crane moves); (2) Point cloud processing and 3D map of concrete surface; (3) Map differencing - overlay of pre/post maps with height change detection, achieved volume calculation. CENTER: comparison module receiving both pipelines, outputting dashboard with: required volume, achieved volume, remaining volume, achievement percentage, under-poured area highlights (shown in red on floor plan). Side annotation: 'Scan timing: before crane repositioning'. Clean professional technical diagram, Korean labels, white background."

---

### 3.3 3차년도 (2028.01 ~ 2028.12, 12개월)

#### ① 개발 목표

**장애물 인지 고도화, 작업량 추론(필요량+달성량) 고도화, 현장 실증 시험**

- 장애물 인지 시스템 **고도화** (동적 장애물 추적, 악천후 대응, 센서 고장 대응)
- 작업량 추론 시스템 **정확도 향상**: 필요량 예측 및 달성량 확인 정밀화
- 장애물 인지 정확도 **90% 이상**, 정지 신호 출력 응답시간 **500ms 이내** 달성
- 작업량 추론 오차 **±15% 이내** (필요량 예측 및 달성량 확인 모두) 달성
- CPC 탑재 **현장 실증 시험** 수행

#### ② 개발 내용 및 범위

**(가) 장애물 인지 시스템 고도화**

- 동적 장애물 추적 고도화
  - 다중 이동 장애물 동시 추적 성능 향상 (최대 20개 동시 추적)
  - 장애물 궤적 예측 정확도 향상 (딥러닝 기반 경로 예측)
  - 붐 동작과 장애물 이동의 동시 고려를 통한 충돌 예측 개선
- 악천후·악조건 대응 강화
  - 우천, 분진, 야간, 역광 등 환경 변화에 대한 센서 성능 열화 보상
  - 환경 조건별 센서 신뢰도 동적 조정 (레이더 가중치 증가 등)
  - 눈·비·안개 환경에서의 LiDAR 포인트 클라우드 필터링
- 센서 고장 대응 (Degraded Mode)
  - 개별 센서 고장 시 나머지 센서만으로 운용 가능한 대체 모드
  - 센서 자가 진단(Self-Diagnosis) 및 고장 알림
  - 가용 센서 조합별 성능 저하 수준 정의 및 운용 제한
- 전체 붐 간섭 검사 확장
  - 붐 선단뿐 아니라 전체 링크(모든 관절 구간)에 대한 장애물 간섭 검사
  - 붐 3D 모델과 장애물 맵 간 실시간 간섭 계산

**(나) 작업량 추론 시스템 고도화 (필요량 + 달성량)**

- 3D 맵 생성 정확도 향상
  - 붐 자세 오차 보정을 통한 정합 정확도 향상
  - 고정밀 맵 생성 (포인트 밀도 향상, 해상도 개선)
  - 반복 스캔을 통한 맵 갱신 및 정확도 검증
- 사전 스캔(필요량 예측) 정확도 향상
  - 실제 타설량 대비 추론량 비교·보정 (머신러닝 기반 보정 모델)
  - 철근 배근 높이 차이에 따른 체적 보정
  - 경사면·비정형 바닥의 체적 계산 정밀화
- 사후 스캔(달성량 확인) 고도화
  - 사전/사후 맵 차분 알고리즘 정밀화 (콘크리트 표면 변화 정밀 검출)
  - 미타설 영역·두께 부족 영역 자동 식별 및 시각화
  - 누적 달성량 관리: 영역별·전체 작업 달성률 이력 추적
  - 타설 품질 지표 산출 (두께 균일도, 목표 대비 편차 분포)

**(다) 현장 실증 시험**

- 환경 인지 시스템 실증
  - CPC 붐 운용 환경에서의 장애물 인지 정확도 평가
    - 검출 정확도(Detection Rate): 90% 이상
    - 오검출률(False Positive Rate): 5% 이하
    - 정지 신호 출력 응답시간: 500ms 이내
  - 다양한 장애물 유형별 검출 성능 평가
  - 악천후(우천, 야간) 환경 성능 검증
- 환경 스캔 시스템 실증
  - 3D 맵 생성 정확도 평가 (기준 측량 대비 오차)
  - 사전 스캔: 필요량 예측 정확도 평가 (설계 체적 대비 ±15% 이내)
  - 사후 스캔: 달성량 확인 정확도 평가 (실제 타설 체적 대비 ±15% 이내)
  - 사전/사후 비교 시나리오 실증 (스캔 → 타설 → 재스캔 → 달성률 확인)
  - 다양한 현장 형태(평면, 경사면, 구조물 혼재) 시험
- 연속 운용 안정성 검증
  - 2시간 이상 연속 운용 안정성
  - 센서 열화·오류 발생률 측정
  - 장시간 운용 시 성능 유지 확인

**(라) 시스템 인터페이스 문서화**

- 주관기관 연동 인터페이스 정의서 작성
  - 장애물 인지 결과 출력 데이터 포맷 (장애물 리스트, 위험도, 안전 명령)
  - 작업량 추론 결과 출력 데이터 포맷 (3D 맵, 영역 정보, 필요 체적, 달성 체적, 잔여량)
  - 향후 자율타설 시스템 통합 시 연동 방안 제시

#### ③ 3차년도 대표 그림

**[그림 프롬프트 5: 현장 실증 시험 구성도]**

> 프롬프트: "Field test setup diagram for CPC environment perception and scanning system. Show: (1) Test site with concrete pump car, boom extended, all sensors visible (LiDAR on tip, radar on mid-joint, cameras, ultrasonic at base) with colored detection zones overlaid; (2) Standard obstacle set placed around CPC - human dummy at 3m, scaffolding at 10m, simulated power line at 30m, moving vehicle at 50m; (3) Ground truth measurement setup - total station, reference markers, ground truth obstacle positions; (4) Scanning test area - marked floor zone with rebar, measured reference volume; (5) Data logging station with laptop and analysis displays. Test metrics labels: 'Detection rate ≥90%', 'False positive ≤5%', 'Stop signal response ≤500ms', 'Volume estimation error ≤±15%', 'Continuous operation ≥2hrs'. Weather condition icons showing tests in sun, rain, night. Clean technical illustration, Korean labels, white background."

**[그림 프롬프트 6: 환경 인지 + 현장 스캔 통합 시스템 최종 구성도]**

> 프롬프트: "Complete system overview diagram of CPC environment perception and site scanning system. Top section: CPC with boom showing all sensor positions (LiDAR, Radar, Camera, Ultrasonic) with detection range indicators. Left branch 'Environment Perception (Safety)': sensor fusion pipeline → obstacle detection/classification/tracking → risk assessment → safety command (Warning/Slow-down/Stop) → interface to boom control system. Right branch 'Site Scanning (Work)' with two sub-branches: (A) 'Pre-Pour Scan' → 3D map → required volume estimation → interface to path planning; (B) 'Post-Pour Scan (before crane move)' → 3D map → map differencing vs pre-pour → achieved volume + remaining volume → interface to work management. Center: edge computing unit processing all branches. Bottom: output interface panel showing obstacle map display AND work volume dashboard with 'Required / Achieved / Remaining' progress indicators. Arrows indicating data flow to external systems. Version label 'v1.0 Field-tested'. Clean professional system diagram, Korean labels, white background."

---

## 4. 연구개발성과 성능목표

### 성능지표 1: 장애물 인지 정확도 (검출률)

| 항목 | 내용 |
|------|------|
| **성능지표명** | 장애물 인지 정확도 - 검출률 (Obstacle Detection Rate) |
| **단위** | % (퍼센트) |
| **정의** | 검지 범위 내에 존재하는 장애물 중 시스템이 정상적으로 검출한 비율 (True Positive Rate) |
| **1차년도 목표** | 센서 선정 및 알고리즘 기본 설계 완료, 벤치마크 환경 구축 |
| **2차년도 목표** | 70% 이상 (실내 표준 환경, 다중 센서 융합) |
| **3차년도 목표** | 90% 이상 (CPC 탑재, 실외 실증 환경) |

#### 평가 방법

- **측정 방식**: 표준 장애물 시험
  - 사전 정의된 표준 장애물 세트를 검지 범위 내 다양한 거리·위치에 배치
  - 시스템이 검출한 장애물 수 / 실제 배치된 장애물 수 × 100%
  - 장애물 유형별(사람, 구조물, 차량 등) 개별 검출률도 산출
- **표준 장애물 세트**:
  - 사람 모형 더미 (60cm × 60cm × 180cm)
  - 비계/거푸집 모사 구조물 (1m × 1m × 2m)
  - 전력선 모사 (직경 3cm 와이어, 높이 15m)
  - 이동 차량 모사 (원격 조종 카트 또는 실차)
- **측정 조건**:
  - 2차년도: 실내 표준 환경 (정적 장애물 위주, 조명 제어)
  - 3차년도: 실외 실증 환경 (동적 장애물 포함, 자연 조명, 우천·야간 포함)
  - 검지 거리: 5m, 10m, 30m, 50m 각 거리별 평가
  - 반복: 각 조건 30회 이상 반복, **평균 검출률**이 목표 이내
- **평가 환경**: 한건연 테스트베드 또는 건설현장, CPC 실장비 탑재 상태

---

### 성능지표 2: 타설 작업량 추론 정확도 (필요량 예측 + 달성량 확인)

| 항목 | 내용 |
|------|------|
| **성능지표명** | 타설 작업량 추론 정확도 (Work Volume Estimation & Achievement Accuracy) |
| **단위** | % (퍼센트, 오차율) |
| **정의** | (A) 사전 스캔으로 추론한 타설 필요 체적과 설계 체적 간의 오차율, (B) 사후 스캔으로 산출한 타설 달성 체적과 실제 타설 체적 간의 오차율 |
| **1차년도 목표** | 알고리즘 개념 설계 완료 (필요량 예측 + 달성량 확인 개념 정의) |
| **2차년도 목표** | ±25% 이내 (실내 표준 환경, 필요량 예측 및 달성량 확인 모두) |
| **3차년도 목표** | ±15% 이내 (CPC 탑재, 실외 실증 환경, 필요량 예측 및 달성량 확인 모두) |

#### 평가 방법

- **측정 방식 A - 필요량 예측 정확도**: 기준 체적 비교
  - 사전에 정밀 측량으로 확인된 기준 영역(면적, 깊이)을 사전 스캔
  - 시스템 추론 필요 체적과 설계 기준 체적 비교
  - 오차율 = |추론값 - 기준값| / 기준값 × 100%
- **측정 방식 B - 달성량 확인 정확도**: 사전/사후 맵 차분 비교
  - 기준 영역에 알려진 양의 콘크리트(또는 대체 물질)를 투입
  - 타설 전 사전 스캔 → 투입 → 타설 후 사후 스캔 (크레인 이동 전)
  - 시스템 산출 달성 체적과 실제 투입 체적 비교
  - 오차율 = |산출값 - 실제값| / 실제값 × 100%
- **기준 영역 구성**:
  - 평면 영역: 정사각형(5m × 5m) 바닥면, 균일 두께 200mm
  - 복합 영역: 기둥(비타설 영역) 포함, 단차 포함, 경사면 포함
  - 실제 철근 배근 영역: 실제 건설현장 또는 테스트베드의 철근부
- **측정 조건**:
  - 2차년도: 실내 표준 환경, 단순 형상 영역
  - 3차년도: 실외 실증 환경, 복합 형상 영역 포함, 실제 타설 전후 스캔 포함
  - 반복: 각 영역 유형별 10회 이상 스캔, **평균 오차율** 및 **최대 오차율**이 목표 이내
- **평가 환경**: 한건연 테스트베드 또는 건설현장, CPC 붐 선단 센서 탑재 상태

---

## 5. 연차별 요약표

| 구분 | 1차년도 (9개월) | 2차년도 (12개월) | 3차년도 (12개월) |
|------|----------------|-----------------|-----------------|
| **핵심 목표** | 센서 선정 + 아키텍처 설계 + 기본 알고리즘 설계 | 핵심 알고리즘 개발 + 시스템 구현 + 기초 시험 | 시스템 고도화 + 현장 실증 |
| **환경 인지** | 다중 센서 선정, 융합 아키텍처 설계 | 검출·분류·추적 알고리즘 개발, 융합 엔진 구현 | 고도화 (악천후, 고장 대응), 검출률 90%+ |
| **환경 스캔** | 스캔 센서 선정, 맵 생성·달성량 확인 기본 설계 | 3D 맵 생성, 필요량 예측 + 달성량 확인 구현 | 정확도 향상 (필요량·달성량 모두 ±15%) |
| **시험** | 벤치마크 환경 구축, 시뮬레이션 | 실내 시험 + CPC 탑재 기초 시험 | 현장 실증 시험 |
| **예산** | 2.0억 원 | 1.8억 원 | 2.0억 원 |

---

### 5.1 1차년도 예산: 2.0억원 (2026.04 ~ 2026.12, 9개월)

**주요 연구개발 내용**: 다중 센서 선정 및 융합 아키텍처 설계, 장애물 검출·분류 기본 알고리즘 설계, 현장 스캔 센서 선정, 3D 맵 생성 기본 설계, 벤치마크 환경 구축

**인건비: 8,500만원 (42.5%)**

- 책임연구원 1명 (참여율 25%, 9개월): 1,900만원 — 시스템 총괄, 센서 융합 아키텍처 설계
- 선임연구원 1명 (참여율 40%, 9개월): 3,000만원 — 장애물 인지 알고리즘 설계, 센서 평가
- 연구원 1명 (참여율 30%, 9개월): 2,300만원 — 3D 스캔·맵 생성 알고리즘 설계
- 연구원 1명 (참여율 15%, 9개월): 1,300만원 — 벤치마크 환경 구축, 시뮬레이션 지원

**재료비: 5,000만원 (25.0%)**

- 3D LiDAR 센서 (환경 인지용, 멀티레이어): 1,200만원
- 밀리미터파 레이더 모듈: 600만원
- 산업용 카메라 (AI 추론 대응, 2대): 500만원
- 초음파 센서 모듈 (4채널): 200만원
- 3D LiDAR (스캔용, 소형 경량): 800만원
- 스테레오 카메라 (스캔 보조): 400만원
- 엣지 컴퓨팅 유닛 (GPU 임베디드 PC): 800만원
- 소모품/마운트/케이블/IMU: 500만원

**연구활동비: 2,500만원 (12.5%)**

- 국내출장비 (현장조사, 주관기관 방문): 800만원
- 기술자문회의비: 400만원
- 회의비/세미나: 300만원
- 시험분석비 (센서 벤치마크 테스트): 500만원
- 기술정보수집비: 300만원
- 기타: 200만원

**간접비: 4,000만원 (20.0%)**

| 항목 | 금액(만원) | 비율 |
|------|-----------|------|
| 인건비 | 8,500 | 42.5% |
| 재료비 | 5,000 | 25.0% |
| 연구활동비 | 2,500 | 12.5% |
| 간접비 | 4,000 | 20.0% |
| **합계** | **20,000** | **100%** |

---

### 5.2 2차년도 예산: 1.8억원 (2027.01 ~ 2027.12, 12개월)

**주요 연구개발 내용**: 장애물 검출·분류·추적 알고리즘 개발, 센서 융합 엔진 구현, 3D 환경 맵 생성 시스템 구현, 타설 체적 계산 및 달성량 확인 시스템 개발, CPC 탑재 기초 시험

**인건비: 9,500만원 (52.8%)**

- 책임연구원 1명 (참여율 20%): 2,000만원 — 연구 총괄, 시험 관리
- 선임연구원 1명 (참여율 35%): 3,500만원 — 센서 융합·장애물 인지 핵심 알고리즘 개발
- 연구원 1명 (참여율 25%): 2,500만원 — 3D 맵 생성·작업량 추론 시스템 개발
- 연구원 1명 (참여율 15%): 1,500만원 — 딥러닝 모델 학습·최적화, 시험 지원

**재료비: 2,700만원 (15.0%)**

- 추가 센서 (시험용 교체/예비): 600만원
- 학습 데이터 구축 장비 (라벨링 도구, 데이터 스토리지): 400만원
- GPU 워크스테이션 (딥러닝 학습 전용): 800만원
- CPC 탑재 마운트·브래킷 제작: 400만원
- 소모품/유지보수: 300만원
- SW 라이선스: 200만원

**연구활동비: 2,200만원 (12.2%)**

- 국내출장비 (CPC 탑재 시험): 700만원
- 기술자문회의비: 300만원
- 회의비: 200만원
- 시험분석비 (실내 시험, CPC 기초 시험): 600만원
- 기술정보수집비: 200만원
- 기타: 200만원

**간접비: 3,600만원 (20.0%)**

| 항목 | 금액(만원) | 비율 |
|------|-----------|------|
| 인건비 | 9,500 | 52.8% |
| 재료비 | 2,700 | 15.0% |
| 연구활동비 | 2,200 | 12.2% |
| 간접비 | 3,600 | 20.0% |
| **합계** | **18,000** | **100%** |

---

### 5.3 3차년도 예산: 2.0억원 (2028.01 ~ 2028.12, 12개월)

**주요 연구개발 내용**: 장애물 인지 시스템 고도화, 작업량 추론 정확도 향상, 현장 실증 시험, 시스템 인터페이스 문서화

**인건비: 9,200만원 (46.0%)**

- 책임연구원 1명 (참여율 20%): 2,000만원 — 연구 총괄, 현장 실증 관리
- 선임연구원 1명 (참여율 30%): 3,000만원 — 시스템 고도화/최적화
- 연구원 1명 (참여율 25%): 2,500만원 — 악천후 대응·센서 고장 대응 개발
- 연구원 1명 (참여율 17%): 1,700만원 — 현장 실증 시험·데이터 분석

**재료비: 4,000만원 (20.0%)**

- 센서 교체/유지보수: 600만원
- 현장 실증 시험 장비/자재 (표준 장애물 세트, 기준 영역 구성): 1,200만원
- 측정 장비 (토탈 스테이션 렌탈, RTK-GPS 등): 800만원
- 방수/방진 하우징 개선: 500만원
- 소모품/유지보수: 500만원
- 통신 모듈/케이블: 400만원

**연구활동비: 2,800만원 (14.0%)**

- 국내출장비 (현장 실증 시험): 1,000만원
- 입회시험비: 500만원
- 기술자문회의비: 300만원
- 회의비: 200만원
- 시험분석비 (성능 검증): 400만원
- 기술정보수집비: 200만원
- 기타: 200만원

**간접비: 4,000만원 (20.0%)**

| 항목 | 금액(만원) | 비율 |
|------|-----------|------|
| 인건비 | 9,200 | 46.0% |
| 재료비 | 4,000 | 20.0% |
| 연구활동비 | 2,800 | 14.0% |
| 간접비 | 4,000 | 20.0% |
| **합계** | **20,000** | **100%** |

---

### 5.4 환경 인지 및 현장 스캔 시스템 예산 총괄

| 항목 | 1차년도 | 2차년도 | 3차년도 | **합계** | **비율** |
|------|---------|---------|---------|---------|---------|
| 인건비 | 8,500 | 9,500 | 9,200 | **27,200** | **46.9%** |
| 재료비 | 5,000 | 2,700 | 4,000 | **11,700** | **20.2%** |
| 연구활동비 | 2,500 | 2,200 | 2,800 | **7,500** | **12.9%** |
| 간접비 | 4,000 | 3,600 | 4,000 | **11,600** | **20.0%** |
| **합계** | **20,000** | **18,000** | **20,000** | **58,000** | **100%** |

(단위: 만원)

> **총 예산**: 5억 8,000만원 (5.8억원) / 33개월 (2026.04 ~ 2028.12)  
> **투입 인력**: 연구원 4명 (참여율 15~40%), 풀타임 환산 약 1.0~1.1명/년  
> **간접비**: 전체의 20.0% (11,600만원)  
> **인건비 산정 기준**: 풀타임 1인 연간 1억원 × 참여율 × 연구기간(월)

---

## 6. 용어 정의

| 약어 | 정식 명칭 | 설명 |
|------|----------|------|
| CPC | Concrete Pump Car | 콘크리트 펌프카 |
| DMCR | Distributor Mobile Concrete Robot | 모바일 콘크리트 분배 로봇 |
| LiDAR | Light Detection and Ranging | 레이저 기반 3D 거리 측정 센서 |
| CFAR | Constant False Alarm Rate | 레이더 신호 검출 알고리즘 |
| ICP | Iterative Closest Point | 포인트 클라우드 정합 알고리즘 |
| NDT | Normal Distributions Transform | 포인트 클라우드 정합 알고리즘 |
| LOAM | LiDAR Odometry And Mapping | LiDAR 기반 위치 추정·맵핑 |
| RANSAC | Random Sample Consensus | 로버스트 모델 피팅 알고리즘 |
| DBSCAN | Density-Based Spatial Clustering | 밀도 기반 공간 클러스터링 |
| YOLO | You Only Look Once | 실시간 객체 검출 딥러닝 모델 |
| TTC | Time-To-Collision | 충돌까지 남은 예상 시간 |
| IMU | Inertial Measurement Unit | 관성 측정 장치 |
| PTP | Precision Time Protocol | 정밀 시간 동기화 프로토콜 |
| WDR | Wide Dynamic Range | 광역 다이나믹 레인지 |
| ROI | Region of Interest | 관심 영역 |
| TRL | Technology Readiness Level | 기술 성숙도 수준 |

# Hutter 그룹 굴착기 RL 논문 3편 — §6-5 KPI 인용 정리

> 한건연 AI DT 사업 사업계획서 §6-5 KPI 근거자료
> 작성일: 2026-05-20
> 분석 방법: 서브 에이전트 3개 병렬, 각 논문 본문 정독 후 명시 수치만 추출 (추정 금지)

---

## 0. 분석 대상 3편 개요

| # | 약칭 | 출처 | 핵심 기술 | 비고 |
|---|---|---|---|---|
| 1 | Egli & Hutter 2022 | IEEE RA-L 7(2) | **RL (PPO)** 기반 4관절 trajectory tracking | Menzi Muck M545 (12t) |
| 2 | ExT (Hutter 2025) | — | **GPT-style transformer + RL fine-tuning** | Menzi Muck M545 (12t) |
| 3 | Werner et al. 2026 | arXiv:2605.09465 | **MPC + Hydraulic FF + PID** (RL 아님) | M445 11.5t + CASE250 25t |

> ⚠ 논문 3은 강화학습이 아니라 모델 기반 제어. SOTA 정밀도 근거로는 가장 강력하지만 "RL 학습" KPI 인용처로는 부적합.

---

## 1. 용어 정의 — SOTA

**SOTA** = State-Of-The-Art (최첨단, 최고 수준).
논문에서 "SOTA를 달성했다"는 동일 과제의 기존 모든 보고 성능 중 최고임을 의미. 사업계획서에서는 "~분야 SOTA 대비 동등 이상" 형태로 인용 가능.

---

## 2. 논문별 핵심 수치

### 논문 1: A General Approach (Egli & Hutter, RA-L 2022)

**핵심 contribution**
- 해석적 모델 없이 actuator 신경망 + RL (PPO)로 유압 굴착기 4관절 end-effector 추종 학습
- 추가 튜닝·필터링 없이 실차 pilot stage 밸브에 직접 적용 (sim-to-real 직접 전이)
- 상용 grading controller(Leica iCON) 대비 더 높은 추종 정확도

**보상 함수 (식 (1), p.4)**
```
r_k = max(0, r_k^v + r_k^ω + r_k^Δ + r_k^c)
  r_k^v = 0.05 · exp(-60 · f_c,1 · ||v* - v||²)    # 선형 속도 추종 (w=0.05)
  r_k^ω = 0.02 · exp(-60 · f_c,1 · ||ω* - ω||²)    # 각속도 추종 (w=0.02)
  r_k^Δ = -0.75 · f_c,2 · ||a_k - a_{k-1}||₁        # 입력 변화 패널티 (w=0.75)
  r_k^c = 0.025                                      # 상수 양 보상
```
커리큘럼 계수 `f_c,1`(100 iter), `f_c,2`(200 iter)는 0.1→1.0 선형 증가.

**학습 설정**
- 알고리즘: PPO (Stable Baselines PPO2), MLP 128×128 Tanh
- 시뮬레이터: 자체 (데이터 기반 actuator NN + 직렬 매니퓰레이터)
- **학습 시간: 약 2시간** (RTX 2080s 1장 + Ryzen 9 3950X)
- 실차 데이터 (actuator 모델용): 100분 (100 Hz)
- 실차 deploy 주파수: 100 Hz

**성능 지표 (속도 조건 포함)**

| 시나리오 | 속도 | 평균 위치오차 | 최대 위치오차 | 평균 자세오차 |
|---|---|---|---|---|
| 원형 궤적 (in-air) | **10 cm/s** | **1.7 cm** | 3.9 cm | 0.008 rad |
| 원형 궤적 (in-air) | **15 cm/s** | 2.2 cm | 4.9 cm | 0.010 rad |
| 원형 궤적 (in-air) | **20 cm/s** | 2.8 cm | 6.7 cm | 0.011 rad |
| 토사 grading (in-soil) | **avg 19.8 cm/s** | **2.0 cm** | 3.4 cm | 0.006 rad (0.34°) |
| (이전 SOTA [11]) | 10 cm/s | 7.8 cm | 13.5 cm | — |

→ 이전 SOTA 7.8 cm 대비 **약 4.6배 정밀도 향상**

**상용 시스템(Leica iCON) 대비 (Table VI, z방향)**

| 시나리오 | 학습 정책 | Leica |
|---|---|---|
| Slow (3 joints) | 0.7 cm | 1.6 cm |
| Slow (4 joints) | 0.8 cm | — |
| Fast (3 joints) | 1.2 cm | 1.8 cm |
| Fast (4 joints) | 0.9 cm | — |

---

### 논문 2: ExT — Scalable Autonomous Excavation (Hutter, 2025)

**핵심 contribution**
- 통합 오픈소스 프레임워크: 다양한 expert(RL·script·human teleop) 데모 → GPT-style transformer 사전학습 → SFT/RLFT 신속 적응
- Menzi Muck M545 실차 dig-dump-move 전체 사이클 zero-shot sim-to-real
- 신규 지형·토양·버킷(OOD)에 적은 상호작용으로 적응, 기존 task 망각 최소화

**보상 함수**
- 별도 정의 없음. 선행연구 [5] (Egli et al. 2024)의 보상·종료 조건 사용.
- RLFT 단계 PPO 손실: `L = E[L^CLIP - c1·L^VF + c2·S[π] - β·KL(π‖π0)]`
  - 엔트로피 c2 = 0.0005, KL 페널티 β = 0.02
  - actor lr: 1e-5 → 1e-7 (cosine), critic lr 1e-4, std lr 5e-4

**학습 설정**
- **시뮬레이터: IsaacGym** (GPU 병렬, 한건연 사업의 Algoryx와 다름 — 주의)
- 데모: dig 150k + dump 150k + move 150k + abort 2k (≈ 실세계 30일 분량)
- 데모 생성 시간: **RTX 3090 단일 GPU 2시간 미만**
- Pretrained 모델: GPT decoder-only, 6 layer / 6 head / hidden 640 / K=25 / **25M params**
- RLFT 설정: parallel envs 1,000 / PPO iter 100 / total interactions 600k
- 비교 MLP-PPO: 300 iter × 64k envs = **115.2M interactions** (192배 차이)

**성능 지표 (속도 조건 포함)**

| 항목 | 수치 | 속도 조건 |
|---|---|---|
| GPT-4-Tasks dig 성공률 (sim) | **98.8%** | — |
| Abort & recovery 성공률 | **99.5%** | — |
| Dump 위치 오차 (sim) | 1.0 ± 0.7 cm | EE velocity ≤ 0.2 m/s (= **20 cm/s**) |
| Move 위치 오차 (sim) | 0.5 ± 0.3 cm | EE velocity ≤ 0.2 m/s |
| Dump 위치 오차 (실차, zero-shot) | **3.6 ± 2.5 cm** | EE velocity ≤ 0.2 m/s |
| Move 위치 오차 (실차) | 2.2 ± 1.0 cm | EE velocity ≤ 0.2 m/s |
| **완전 사이클 dig-dump-move** | **사이클 36 s**, 굴착량 **0.96 m³/cycle** (버킷 0.68 m³, fill 141%) | 6 cycles 평균 |
| 실차 dig 위치 오차 | 10.7 ± 3.0 cm | — |
| 실차 dump 위치 오차 | 6.5 ± 2.9 cm | — |
| 주입 노이즈 (sim-to-real) | 제어 지연 ≤ 0.75 s, joint vel 노이즈 ±0.2 rad/s | — |

**OOD 적응 성능 (USP)**
- 지형(RBF→계단), 토양 파라미터, 버킷 기하 3가지 OOD에 대해
- GPT pretrained + RLFT (100 iter × 1k envs = 600k interactions)로 **95~97% 회복**
- MLP-PPO는 같은 budget에서 74.7% → 115.2M interactions까지 늘려야 동급
- **데이터 효율: 1k SFT 데모로 96% 성공 (150k from-scratch는 12%) → 150배 절감**

---

### 논문 3: High Precision Hydraulic Excavator Control (Werner et al., arXiv 2026)

> **⚠ RL이 아님**: MPC + Hydraulic FF + PID hybrid

**핵심 contribution**
- LS(Load Sensing)·NFC(Negative Flow Control) 양 유압 아키텍처 공통 적용 가능한 retrofittable·machine-agnostic 정밀 grading 제어
- NFC 유압의 load-dependent soft 거동 보상 pressure-adaptive 모델
- 실차 2종 (11.5t LS / 25t NFC)에서 **약 20분 캘리브레이션**만으로 cm-level 정밀도

**보상 함수 (MPC stage cost — RL reward 아님)**
- 항: EE forward velocity 추종, vertical velocity ≈0, pitch rate ≈0, EE 높이→목표 plane, blade pitch, 입력 증분 패널티
- **가중치 수치 본문 미명시**

**학습 설정**
- RL 아님 → 학습 시간·GPU·샘플 수 해당 없음
- **캘리브레이션: 약 20분** (조인트별 순차, 벤더 접근 불필요)
- MPC 주파수 10 Hz, horizon N=20, Δt=0.1 s

**정밀도 지표 (속도 조건 포함) — 이 논문의 USP**

| 항목 | 수치 | 속도 조건 |
|---|---|---|
| **CASE250 (25t NFC) RMSE** | **1.8 cm** | **약 0.5 m/s = 50 cm/s** (전문 operator 미세 grading 속도) |
| CASE250 최대 path 편차 | 5 cm | 50 cm/s |
| **M445 (11.5t LS) RMSE** | **1.4 cm** | 50 cm/s |
| M445 최대 path 편차 | 4 cm | 50 cm/s |
| 절삭 깊이 범위 | 2 ~ 40 cm | — |
| Joint velocity 추종 (LS) | ±2 % | — |
| 자세(pitch) 오차 | **본문 미명시** | — |
| 표면 측정 장비 | Leica MS60 Multistation | — |

**Baseline 대비 개선폭**

| 비교 대상 | 비교 수치 | 본 방법 | 개선폭 |
|---|---|---|---|
| 상용 시스템 (Trimble 계열, CASE250 동일 조건) | RMSE 4.7 cm | 1.8 cm | **2.6배** |
| 상용 시스템 최대 편차 | 17 cm | 5 cm | 3.4배 |
| End-to-end RL (저자 사전 실험) | 약 6 cm | 1.8 cm | 약 3.3배 |
| 선행 [31] IK+PI (sim) | 4 cm | 1.8 cm | 2.2배 |
| 선행 [17] light grading | 2.34 cm | 1.4~1.8 cm | 동등 (단, 본 방법은 in-soil deep grading) |

---

## 3. §6-5 KPI 권장값 (속도 조건 명시)

> ⚠ 속도 미명시 시 평가자의 "사실상 정지 상태 아닌가" 공격 가능 — **항상 속도와 정밀도를 쌍으로 명시**

| KPI 항목 | 보수안 | 공격안 | 학술 근거 |
|---|---|---|---|
| 굴착 위치 정밀도 (in-air) | ≤ 5 cm @ 20 cm/s | ≤ 3 cm @ 20 cm/s | 논문 1: 2.8 cm @ 20 cm/s |
| 굴착 위치 정밀도 (실차 dig) | ≤ 12 cm | ≤ 8 cm | 논문 2: 10.7±3.0 cm |
| Dump 위치 정밀도 | ≤ 5 cm @ 20 cm/s | ≤ 4 cm @ 20 cm/s | 논문 2: 3.6±2.5 cm @ ≤20 cm/s |
| 그레이딩 RMSE | ≤ 3 cm @ 50 cm/s | ≤ 2 cm @ 50 cm/s | 논문 3: 1.4~1.8 cm @ 50 cm/s |
| 자세 오차 | ≤ 1.0° | ≤ 0.5° | 논문 1: 0.34° (grading) |
| 사이클 타임 (dig-dump-move) | ≤ 60 s | ≤ 40 s | 논문 2: 36 s |
| 1-cycle 굴착량 | ≥ 0.6 m³ (버킷 0.68 기준) | ≥ 0.9 m³ | 논문 2: 0.96 m³ (fill 141%) |
| 굴착 성공률 | ≥ 90% | ≥ 95% | 논문 2 sim: 98.8%, 실차 — |
| RL 학습 수렴 시간 (단일 task) | ≤ 8 hr | ≤ 4 hr | 논문 1: 2 hr (RTX 2080s) |
| 신규 토양 적응 데이터 | ≤ 5k 데모 | ≤ 1k 데모 | 논문 2: 1k SFT 96% |
| 상용 대비 정밀도 개선 | ≥ 1.5배 | ≥ 2.0배 | 논문 3: 2.6배 |

---

## 4. 인용 시 주의사항 3가지

1. **시뮬레이터 mismatch**
   Hutter 그룹은 IsaacGym (논문 2), 자체 시뮬 (논문 1) 사용. 한건연 사업은 Algoryx. → "Hutter는 IsaacGym에서 X 달성, 본 사업은 Algoryx 기반으로 동등 수준 목표" 식으로 분리 서술 필수.

2. **장비 체급 차이**
   Hutter는 11~25t. 한건연 대상 굴착기 체급이 다르면 cm 수치 직접 인용 불가 — 비율(%)로 환산하거나 "동급 체급 기준" 명시.

3. **논문 3은 RL 아님**
   §6-5에서 "RL 기반 1.8 cm 달성 가능"으로 인용하면 오기. 정확한 표현:
   - "최신 모델기반 제어 SOTA(Werner 2026) 1.8 cm 수준을 본 사업의 RL+hybrid 접근으로 목표"
   - 또는 "RL 단독(저자 사전 실험 약 6 cm) → RL+모델기반 hybrid로 cm-level 도달"

---

## 5. 원본 자료

- `1. A General Approach ... _Hutter.pdf` (Egli & Hutter, RA-L 2022)
- `5. ExT Towards Scalable Autonomous Excavation via.pdf` (Hutter, 2025)
- `High Precision Hydraulic Excavator Control for.pdf` (Werner et al., arXiv:2605.09465, 2026)
- 텍스트 추출본: `paper1.txt`, `paper2.txt`, `paper3.txt` (pdftotext -layout)

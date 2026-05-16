# 공연 기획 제안서 — 이미지 생성 프롬프트 (GPT / DALL·E / Midjourney 공용)

> 사용법: 아래 프롬프트를 GPT(ChatGPT 이미지 생성) 또는 DALL·E 3, Midjourney v6, Sora 등 이미지 생성 모델에 그대로 붙여넣으면 됩니다.
> 모든 프롬프트는 **한글(GPT/한국어 입력)** + **영문(DALL·E·MJ 권장)** 두 버전을 제공합니다.
> 비율은 제안서 용도에 맞춰 표기했습니다: **표지=세로 A4(2:3)**, **포스터=세로(2:3)**, **본문 삽입=가로(16:9 또는 4:3)**.

---

## 0. 공통 비주얼 가이드라인 (Style Bible)

전 이미지에 공통 적용할 톤·매너입니다. 각 프롬프트 끝에 "Style: 아래 공통 톤 적용"이라고 붙이거나, 아래 항목을 풀어 넣어 주세요.

- **컬러 팔레트**: 딥 네이비(#1F3A68), 코발트 블루(#2E5C94), 따뜻한 골드(#E0B265), 아이보리(#F7F2E6), 코랄 핑크(#E89B8C). 클래식의 격조 + 어린이 친화 따뜻함을 동시에.
- **무드**: 마법 같은(magical) · 시네마틱(cinematic) · 가족 친화(family-friendly) · 동심(whimsical) · 음악적(musical) · 고급스러움(elegant)
- **금지 요소**: 디즈니/지브리 스타일의 직접 모사 금지(저작권), 무서운 표정의 동물, 어린이가 울거나 무서워하는 표정, 텍스트 자동 생성(글자는 직접 합성)
- **렌더링 스펙**: 4K 해상도, 영화 같은 라이팅(rim light + soft key light), 책 일러스트 + 콘서트 홀 사진 합성 분위기, 그레인 약간(film grain subtle)

---

## 1. 표지(커버) 메인 비주얼 — A4 세로 (2:3)

### 용도
- 제안서 표지(공연 기획 제안서 1쪽)
- 포스터/리플렛 메인 비주얼로 재사용 가능

### 한글 프롬프트

```
A4 세로 비율(2:3)의 시네마틱한 클래식 음악회 포스터 일러스트.
중앙에는 어두운 콘서트홀 무대 위에서 4K LED 스크린에 거대한 사자 한 마리의 실사 영상이 비치고 있고, 그 앞에서 8~9명의 클래식 챔버 앙상블 단원(바이올린 2, 비올라, 첼로, 콘트라베이스, 플루트, 클라리넷, 타악기, 피아노 일부)이 연주하고 있다.
무대 앞쪽에는 어린이들과 가족 관객들이 야광 응원봉을 들고 있고, 일부는 작은 빛으로 손에서 발광하는 듯한 효과.
무대 위로는 별·음표·작은 동물들의 실루엣(코끼리, 백조, 새, 거북이)이 황금빛 입자처럼 떠올라 마법 같은 분위기를 만든다.
조명: 무대 위에서 따뜻한 골드 스포트라이트가 단원을 비추고, 객석은 부드러운 코발트 블루 톤.
색감: 딥 네이비(#1F3A68) 배경 + 골드(#E0B265) 액센트 + 아이보리(#F7F2E6) 하이라이트.
스타일: 시네마틱 일러스트레이션 + 빛 입자 효과 + 영화 포스터 같은 깊이감.
어린이 친화적이면서도 격조 있는 클래식의 위엄을 동시에 표현.
중앙 상단과 하단에 제목·로고가 들어갈 여백 충분히 확보(텍스트는 비워둘 것).
4K 해상도, 그레인 약간, 동심과 마법감을 강조.
금지: 캐릭터화된 만화 스타일, 디즈니/지브리 직접 모사, 무서운 표정의 동물, 자동 생성된 글자.
```

### 영문 프롬프트 (DALL·E 3 / MJ v6 권장)

```
Cinematic concert poster illustration, A4 vertical (2:3 aspect ratio).
A grand classical chamber ensemble of 8-9 musicians (2 violins, viola, cello, double bass, flute, clarinet, percussion, piano partial) performing on a dark concert hall stage.
Behind them, a massive 4K LED screen displays a hyper-realistic photographic image of a majestic lion.
In the foreground, families and children in the audience hold glowing concert lightsticks; some lightsticks emit soft warm sparkles.
Floating golden particles rise above the stage forming silhouettes of animals — elephant, swan, bird, tortoise — and musical notes, evoking a magical atmosphere.
Lighting: warm gold spotlights on the musicians (rim + key light), audience bathed in soft cobalt blue.
Color palette: deep navy #1F3A68 background, gold #E0B265 accents, ivory #F7F2E6 highlights.
Style: cinematic illustration with light particle effects, movie-poster depth and bokeh.
Mood: family-friendly yet refined and dignified, blending childlike wonder with classical elegance.
Leave clear space at top and bottom for title and logo (no text rendered).
4K resolution, subtle film grain, magical and ceremonial atmosphere.
Avoid: cartoon characters, direct Disney/Ghibli style, scary animal expressions, any rendered text.
--ar 2:3 --style raw --v 6
```

---

## 2. 핵심 차별화 ① — 4K 실사 미디어아트 연출 시각화 (가로 16:9)

### 용도
- 제안서 본문 "5.2 연출 요소" 또는 "7. 무대 및 기술 요구사항"에 삽입
- 음악감독에게 4K 미디어아트의 임팩트를 전달

### 한글 프롬프트

```
가로 16:9 비율의 클로즈업 무대 사진 같은 일러스트.
어두운 콘서트홀, 무대 후면 전체를 덮는 대형 4K LED/프로젝션 스크린.
스크린에는 생상스 「동물의 사육제」 XIII. 백조(The Swan)에 맞춰 실사 같은 백조 한 마리가 잔잔한 호수 위를 우아하게 미끄러지듯 헤엄치는 4K 슬로우 모션 영상이 비친다(물결, 깃털 디테일까지 사실적).
무대 앞에는 첼리스트 한 명이 무대 중앙에 앉아 「백조」를 연주하고 있고, 옆에는 피아니스트가 함께한다.
조명: 무대 전체가 푸른 보랏빛(twilight blue) + 백조 영상의 차가운 흰색 빛이 무대로 흘러나오는 듯한 효과.
관객석은 약간 보이고 흐릿하게 처리(보케).
스타일: 영화 같은 콘서트 다큐멘터리 사진 + 약간의 회화적 터치. 따뜻함과 차가움의 대비.
강조 포인트: "캐릭터 일러스트가 아닌 4K 실사 영상"이라는 차별화를 한눈에 보여줄 것.
4K, 시네마틱, 정적이면서도 깊이감 있는 구도.
```

### 영문 프롬프트

```
Wide cinematic concert stage photograph illustration, 16:9 aspect ratio.
A dark concert hall with a massive 4K LED projection screen filling the entire back of the stage.
The screen shows a hyper-realistic, photographic 4K slow-motion video of a single white swan gliding elegantly across a calm lake — every ripple and feather rendered photorealistically.
In front of the screen, a solo cellist sits center stage performing "The Swan" from Saint-Saëns' "Carnival of the Animals", with a pianist beside her.
Lighting: stage bathed in twilight blue-violet, with cool white light from the swan video spilling onto the performers.
Audience seats partially visible, soft bokeh.
Style: cinematic concert documentary photography with subtle painterly touch, contrast of warm and cold tones.
Key emphasis: the screen shows PHOTOGRAPHIC REAL FOOTAGE, not cartoon illustration — to make the differentiation visually obvious.
4K, cinematic, still yet deep composition.
--ar 16:9 --style raw --v 6
```

---

## 3. 핵심 차별화 ② — 멘티미터 양방향 퀴즈 + 가족 참여 장면 (가로 16:9)

### 용도
- 제안서 본문 "3. 기획 의도" 또는 "8.1 타깃 관객" 부근에 삽입
- 어린이가 끝까지 집중하는 모습을 비주얼로 증명

### 한글 프롬프트

```
가로 16:9 비율의 콘서트홀 객석에서 본 장면.
무대 위에는 챔버 앙상블이 연주 중이고, 무대 중앙 위 스크린에는 멘티미터 퀴즈 화면이 표시되어 있다("이 곡의 동물은 누구일까요? ① 사자 ② 코끼리 ③ 거북이" 같은 객관식 4지선다 인터페이스 — 화면 안의 글자는 실제 글자가 아닌 그래픽 박스로 표현).
객석에는 부모와 어린 자녀들(만 5~10세) 가족 그룹이 여러 줄로 앉아 있고, 어린이들이 스마트폰 또는 부모의 스마트폰을 들고 정답을 입력하며 즐거워하는 표정.
일부 어린이는 야광 응원봉을 무릎 위에 올려둔 상태.
조명: 객석은 멘티미터 화면의 푸른 빛 + 무대 골드 스포트라이트의 따뜻한 잔광. 어린이들의 얼굴이 화면 빛을 받아 밝게 빛난다.
스타일: 다큐멘터리 콘서트 사진. 어린이들의 자연스러운 호기심·집중 표정이 핵심.
4K, 시네마틱, 가족 친화, 따뜻하고 활기찬 분위기.
금지: 어린이가 울거나 무서워하는 표정, 스마트폰 화면에 자동 생성된 글자.
```

### 영문 프롬프트

```
Wide cinematic photograph illustration from the audience view, 16:9 aspect ratio.
On stage, a chamber ensemble performs; above the stage, a large screen displays a Mentimeter-style live quiz interface (multiple-choice boxes — show as graphic shapes only, no actual text).
In the audience, families with young children (ages 5-10) sit in multiple rows. Children hold smartphones (or parents' phones), enthusiastically tapping in their answers with joyful, focused expressions.
Some children have glowing concert lightsticks resting on their laps.
Lighting: audience faces softly illuminated by the cool blue glow of the quiz screen, with warm gold spillover from stage spotlights.
Style: documentary concert photography. The focus is on the children's natural curiosity and deep engagement.
4K, cinematic, family-friendly, warm and lively atmosphere.
Avoid: crying or scared children, any rendered text on screens.
--ar 16:9 --style raw --v 6
```

---

## 4. 핵심 차별화 ③ — 야광 응원봉 피날레 연출 (가로 16:9)

### 용도
- 제안서 본문 "5.2 연출 요소"의 응원봉 항목, 또는 "11. 기대 효과" 부근
- 클래식의 정적 분위기를 깬다는 메시지를 시각적으로

### 한글 프롬프트

```
가로 16:9 비율의 콘서트홀 전체를 위에서 비스듬히 내려다본 와이드 샷.
공연 피날레(또는 앙코르) 장면. 무대에서는 8~9인 챔버 앙상블이 강렬하게 연주 중이고, 무대 후면 스크린에는 「동물의 사육제」 피날레에 맞춰 모든 동물들(사자, 코끼리, 새, 백조, 캥거루, 거북이 등)이 함께 행진하는 4K 실사+살짝 마법적 합성 영상이 비친다.
객석에서는 수백 명의 가족과 어린이들이 동시에 야광 응원봉을 머리 위로 흔들고 있다. 응원봉 색은 다양(파랑·노랑·핑크·초록)하지만 주로 따뜻한 골드와 코랄.
조명: 무대 암전 + 응원봉의 빛만이 객석을 가득 채우는 환상적 장면. 별이 떠 있는 듯한 분위기.
스타일: 마법 같은(magical) 콘서트 포토 + 살짝 일러스트적 합성. K-POP 콘서트 응원봉 장관 + 클래식의 격조.
강조: 클래식 공연인데 마치 별빛이 떠다니는 듯한, 어린이가 평생 기억할 순간.
4K, 시네마틱, 광활하고 따뜻한 감동.
```

### 영문 프롬프트

```
Wide cinematic high-angle shot of a concert hall during the finale, 16:9 aspect ratio.
On stage, an 8-9 piece chamber ensemble performs powerfully; behind them, a large 4K screen shows all the animals from "Carnival of the Animals" (lion, elephant, bird, swan, kangaroo, tortoise, etc.) marching together in a hyper-realistic yet slightly magical composite video.
In the audience, hundreds of families and children simultaneously wave glowing concert lightsticks above their heads. Lightsticks in various colors (blue, yellow, pink, green) but predominantly warm gold and coral.
Lighting: stage in low light, the audience completely filled with the lightstick glow — like floating stars in a night sky.
Style: magical concert photography with a hint of illustration, fusion of K-pop lightstick spectacle with classical music dignity.
Key emphasis: a classical concert that feels like a starfield — a moment a child remembers for a lifetime.
4K, cinematic, expansive and warmly emotional.
--ar 16:9 --style raw --v 6
```

---

## 5. 단체 소개 / 출연진 페이지용 — 챔버 앙상블 사진 (세로 3:4 또는 가로 4:3)

### 용도
- 제안서 본문 "2. 제안 단체 소개" 또는 "6. 출연진"에 임시 비주얼로 사용
- ※ 실제 단원 사진을 확보하면 교체 권장 — 본 이미지는 어디까지나 임시(temp) 비주얼

### 한글 프롬프트

```
4:3 비율의 클래식 챔버 앙상블 그룹 단체 사진 같은 일러스트(가상 인물).
8명의 한국인 클래식 연주자(20~40대, 남녀 혼합, 단정하고 우아한 검은 정장 또는 짙은 네이비 의상)가 콘서트홀 무대 또는 모던한 공연장 로비를 배경으로 모여 있다.
악기: 바이올린 2, 비올라, 첼로, 콘트라베이스, 플루트, 클라리넷, 작은 타악기. 자연스러운 포즈로 악기를 들거나 옆에 둠.
표정: 따뜻하고 자신감 있는 미소. 가족 음악회를 진행하는 단체답게 친근함과 전문성 동시에.
조명: 부드러운 자연광 + 약한 백라이트. 분위기: 격조 있는 클래식 단체의 공식 프로필.
배경: 흐릿한 콘서트홀 또는 회색·아이보리 그라데이션.
스타일: 고급 클래식 단체 공식 사진. 사실적이되 약간의 회화적 미감.
4K, 부드러운 톤, 신뢰감 있는 분위기.
※ 실제 단원 사진 확보 시 교체할 임시 이미지.
```

### 영문 프롬프트

```
4:3 ratio group photo illustration of a fictional Korean classical chamber ensemble.
8 Korean musicians (ages 20-40, mixed gender), wearing elegant black or dark navy formal attire, gathered at a concert hall stage or modern venue lobby.
Instruments: 2 violins, viola, cello, double bass, flute, clarinet, small percussion. Natural poses holding or standing beside their instruments.
Expressions: warm, confident smiles. Combining the friendliness of a family-concert group with the professionalism of a serious ensemble.
Lighting: soft natural daylight with gentle backlight. Mood: refined official portrait of a classical group.
Background: blurred concert hall or gray/ivory gradient.
Style: high-end classical ensemble official photo, photorealistic with a subtle painterly touch.
4K, soft tones, trustworthy atmosphere.
Note: This is a placeholder image; replace with actual member photos when available.
--ar 4:3 --style raw --v 6
```

---

## 6. (선택) 콘셉트 다이어그램 — 차별화 3대 포인트 시각화 (가로 16:9)

### 용도
- 제안서 본문 "1. Executive Summary" 또는 "3. 기획 의도"에 인포그래픽으로 삽입
- 음악감독·기획팀에 "왜 이 단체가 다른가"를 1초 만에 전달

### 한글 프롬프트

```
가로 16:9 비율의 미니멀하고 세련된 인포그래픽 일러스트.
가운데에 큰 동그라미가 있고 그 안에 "동물의 사육제" 콘셉트 심볼(작은 동물 실루엣 + 음표).
가운데에서 세 방향으로 화살표가 뻗어 나가 세 개의 작은 일러스트 패널과 연결된다:
  ① 좌측: 4K 실사 영상이 비치는 LED 스크린 아이콘 + 사자 사진 일부
  ② 중앙 상단: 스마트폰 화면에 멘티미터 객관식 UI 아이콘 + 어린이 손
  ③ 우측: 야광 응원봉 일러스트 + 빛 입자
배경: 깔끔한 아이보리(#F7F2E6) 베이스에 딥 네이비(#1F3A68) 라인 + 골드(#E0B265) 액센트.
스타일: 모던하고 미니멀한 컨설팅 자료 스타일 인포그래픽 + 약간의 일러스트 감성. 종이 위에 인쇄된 듯한 질감.
글자는 자동 생성하지 말 것(레이블 위치만 빈 박스로 표시).
4K, 깨끗하고 프로페셔널하며 격조 있는 분위기.
```

### 영문 프롬프트

```
Minimalist and refined infographic illustration, 16:9 aspect ratio.
A large central circle contains a "Carnival of the Animals" concept symbol (small animal silhouettes + musical notes).
Three arrows extend from the center to three smaller illustrated panels:
  Left: a stylized LED screen icon showing 4K realistic footage with a partial lion image
  Top-center: a smartphone displaying a Mentimeter-style multiple-choice UI with a child's hand reaching toward it
  Right: a glowing concert lightstick with floating light particles
Background: clean ivory (#F7F2E6) base with deep navy (#1F3A68) line work and gold (#E0B265) accents.
Style: modern minimalist consulting-deck infographic with subtle illustration, paper-print texture.
Do not render any text — leave empty boxes for label placement.
4K, clean, professional, dignified.
--ar 16:9 --style raw --v 6
```

---

## 사용 우선순위 (만약 시간이 부족하다면)

1. **필수**: §1 표지 메인 비주얼 (제안서 1쪽 표지)
2. **필수**: §2 4K 실사 미디어아트 (가장 큰 차별화 포인트의 시각화)
3. **강력 권장**: §4 야광 응원봉 피날레 (감동 모먼트, 음악감독 설득력 최고)
4. **권장**: §3 멘티미터 양방향 퀴즈 (어린이 집중도 증명)
5. **선택**: §6 콘셉트 다이어그램 (Executive Summary 인포그래픽)
6. **임시**: §5 챔버 앙상블 단체 사진 (실제 단원 사진 확보 시 교체)

---

## 후처리 / 텍스트 합성 안내

- 모든 프롬프트에서 **자동 글자 생성은 금지**했습니다(이미지 모델은 한국어를 자주 깨뜨림).
- 제목·로고·곡명 등 텍스트는 **PowerPoint, Canva, Figma, Photoshop 등에서 직접 합성**해 주세요.
- 표지(§1)의 경우 상·하단 여백을 비워두도록 프롬프트에 명시했으니, 그 자리에 한글 제목과 단체명을 얹으시면 됩니다.

---

## 부록: 빠른 GPT 사용 팁

- ChatGPT(유료 GPT-4o 또는 GPT-5)의 이미지 생성 기능에 위 프롬프트 한글 버전을 그대로 붙여넣으면 됩니다.
- 결과가 마음에 들지 않으면 "이 이미지에서 ○○만 더 강조/약하게/색상 변경해서 다시"로 후속 지시를 주면 됩니다.
- 동일 컨셉으로 여러 베리에이션을 받고 싶다면 마지막에 "다른 구도로 한 번 더, 같은 스타일 유지"라고 추가하세요.
- 영문 프롬프트는 DALL·E 3(Bing Image Creator 포함) / Midjourney v6 / Stable Diffusion(SDXL) 등에서 더 안정적인 결과를 줍니다.

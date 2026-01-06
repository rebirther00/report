# -*- coding: utf-8 -*-
import os
import sys

# PyMuPDF 설치 확인
try:
    import fitz
except ImportError:
    os.system('pip install pymupdf')
    import fitz

def read_pdf(pdf_path, max_chars=None):
    """PDF 파일을 읽어 텍스트 반환"""
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        if max_chars:
            return text[:max_chars]
        return text
    except Exception as e:
        return f"Error reading {pdf_path}: {str(e)}"

# PDF 파일 목록
pdf_files = [
    ("ref_docs/260106_할일 및 자료/9.첨단제조_자율 작업형 건설기계 통합 제어기 평가기술 개발 및 적합성 평가 기반 조성(3)_수요조사서.pdf", "수요조사서"),
    ("ref_docs/260106_할일 및 자료/[한국건설기계연구원]2026년 신규사업 아이템_건설기계제어기평가기술_250731.pdf", "신규사업아이템"),
    ("ref_docs/260105_진행계획 및 자료/01_최승준_2025_기반구축_수요조사_설명자료_기능안전_v2f.pdf", "기반구축_수요조사_설명자료"),
    ("ref_docs/260105_진행계획 및 자료/(250321)선진시장_안전규제대응_현황.pdf", "안전규제대응_현황"),
]

# 각 PDF 읽기 및 저장
for pdf_path, name in pdf_files:
    if os.path.exists(pdf_path):
        print(f"\n{'='*80}")
        print(f"📄 {name}")
        print(f"파일: {pdf_path}")
        print('='*80)
        text = read_pdf(pdf_path)
        print(text[:20000] if len(text) > 20000 else text)
        print(f"\n[총 {len(text)} 문자]")
    else:
        print(f"파일 없음: {pdf_path}")

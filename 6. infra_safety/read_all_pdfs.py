# -*- coding: utf-8 -*-
import fitz
import os

base_path = r'C:\Users\sharp\OneDrive\문서\gitLocal\report\6. infra_safety'
output_dir = os.path.join(base_path, 'extracted_texts')
os.makedirs(output_dir, exist_ok=True)

pdf_files = [
    (r'ref_docs\260106_할일 및 자료\9.첨단제조_자율 작업형 건설기계 통합 제어기 평가기술 개발 및 적합성 평가 기반 조성(3)_수요조사서.pdf', '01_수요조사서'),
    (r'ref_docs\260106_할일 및 자료\[한국건설기계연구원]2026년 신규사업 아이템_건설기계제어기평가기술_250731.pdf', '02_신규사업아이템'),
    (r'ref_docs\260105_진행계획 및 자료\01_최승준_2025_기반구축_수요조사_설명자료_기능안전_v2f.pdf', '03_기반구축_설명자료'),
    (r'ref_docs\260105_진행계획 및 자료\(250321)선진시장_안전규제대응_현황.pdf', '04_안전규제대응'),
    (r'ref_docs\260106_할일 및 자료\(백종희)전북도_과기위기획보고서(제출용)_24.11.12(1차완료)(오탈자수정).pdf', '05_전북도_과기위기획보고서'),
]

for pdf_rel_path, name in pdf_files:
    pdf_path = os.path.join(base_path, pdf_rel_path)
    output_file = os.path.join(output_dir, f'{name}.txt')
    
    if os.path.exists(pdf_path):
        try:
            doc = fitz.open(pdf_path)
            text = ''
            for page in doc:
                text += page.get_text()
            doc.close()
            
            # UTF-8로 파일 저장
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"FILE: {name}\n")
                f.write(f"PATH: {pdf_rel_path}\n")
                f.write("="*80 + "\n\n")
                f.write(text)
            
            print(f"Saved: {output_file} ({len(text)} chars)")
        except Exception as e:
            print(f"Error processing {name}: {e}")
    else:
        print(f"File not found: {pdf_path}")

print(f"\nAll files saved to: {output_dir}")

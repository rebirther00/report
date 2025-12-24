# -*- coding: utf-8 -*-
import pdfplumber
import sys
import io
import os

# UTF-8 출력 설정
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

base_path = r"c:\Users\sharp\OneDrive\문서\gitLocal\report\4. mining_add\ref_docs"

# PDF 파일들 정의
pdf_files = [
    {
        "name": "1번_건설기계_농기계_전동화",
        "path": os.path.join(base_path, "1. (기획보고서) 건설기계-농기계 전동화 핵심기술 개발 사업-취합(251218)-회의결과메모_최종.pdf"),
        "pages": list(range(61, 67))  # p62~66 (0-indexed: 61~66)
    },
    {
        "name": "2번_선박용_CO2_포집시스템",
        "path": os.path.join(base_path, "2. [format](기획보고서) 선박용 CO2 포집시스템 기술개발 및 실증사업.pdf"),
        "pages": list(range(56, 59))  # p57~58 (0-indexed: 56~58)
    },
    {
        "name": "3번_광산용_초대형_건설기계",
        "path": os.path.join(base_path, "3. 251224_(기획보고서) 광산용 초대형 건설기계 기술개발사업_V46.pdf"),
        "pages": list(range(0, 60))  # 처음부터 p60까지 (내용 파악용)
    }
]

output_dir = os.path.join(base_path, "extracted")
os.makedirs(output_dir, exist_ok=True)

for pdf_info in pdf_files:
    print(f"\n{'='*80}")
    print(f"Processing: {pdf_info['name']}")
    print(f"{'='*80}")
    
    output_path = os.path.join(output_dir, f"{pdf_info['name']}_extracted.txt")
    
    try:
        with pdfplumber.open(pdf_info['path']) as pdf:
            total_pages = len(pdf.pages)
            print(f"Total pages: {total_pages}")
            
            all_text = []
            
            for page_num in pdf_info['pages']:
                if page_num < total_pages:
                    page = pdf.pages[page_num]
                    text = page.extract_text()
                    if text:
                        all_text.append(f"\n{'='*80}\nPage {page_num+1}\n{'='*80}\n{text}\n")
                        print(f"Page {page_num+1}: {len(text)} characters extracted")
                    else:
                        all_text.append(f"\n{'='*80}\nPage {page_num+1}\n{'='*80}\n[No text found]\n")
                        print(f"Page {page_num+1}: No text found")
            
            full_text = "".join(all_text)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(full_text)
            
            print(f"\n✓ Saved to: {output_path}")
                
    except Exception as e:
        print(f"Error processing {pdf_info['name']}: {e}")
        import traceback
        traceback.print_exc()

print("\n\n" + "="*80)
print("All PDFs processed!")
print("="*80)


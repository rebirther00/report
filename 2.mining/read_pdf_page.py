# -*- coding: utf-8 -*-
import pdfplumber
import sys
import io

# UTF-8 출력 설정
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 6번 파일 읽기
pdf_path_6 = r"c:\Users\sharp\OneDrive\문서\gitLocal\report\2.mining\ref_docs\6.[format](기획보고서) 선박용 CO2 포집시스템 기술개발 및 실증사업.pdf"
output_path_6 = r"c:\Users\sharp\OneDrive\문서\gitLocal\report\2.mining\ref_docs\6_extracted_text.txt"

print(f"Reading PDF 6: {pdf_path_6}")
print("=" * 80)

try:
    with pdfplumber.open(pdf_path_6) as pdf:
        total_pages = len(pdf.pages)
        print(f"Total pages: {total_pages}\n")
        
        # p45 주변 페이지 읽기 (40-50페이지)
        start_page = max(0, 39)  # 0-indexed, so page 40 = index 39
        end_page = min(total_pages, 50)  # page 50 = index 49
        
        all_text = []
        
        for i in range(start_page, end_page):
            page = pdf.pages[i]
            text = page.extract_text()
            if text:
                all_text.append(f"\n{'='*80}\nPage {i+1}\n{'='*80}\n{text}\n")
                print(f"Page {i+1}: {len(text)} characters extracted")
            else:
                all_text.append(f"\n{'='*80}\nPage {i+1}\n{'='*80}\n[No text found]\n")
        
        # 파일로 저장
        full_text = "".join(all_text)
        with open(output_path_6, 'w', encoding='utf-8') as f:
            f.write(full_text)
        
        print(f"\n✓ Text extracted and saved to: {output_path_6}")
        print(f"Pages {start_page+1}-{end_page}: {len(full_text)} characters")
            
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()

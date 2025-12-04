# -*- coding: utf-8 -*-
import pdfplumber
import sys
import io

# UTF-8 출력 설정
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

pdf_path = r"c:\Users\sharp\OneDrive\문서\gitLocal\report\2.mining\ref_docs\(approved) [국책] 초대형 마이닝 시장용 광산장비 및 기술개발_v1.pdf"
output_path = r"c:\Users\sharp\OneDrive\문서\gitLocal\report\2.mining\ref_docs\pdf_extracted_text.txt"

print(f"Reading PDF: {pdf_path}")
print("=" * 80)

try:
    with pdfplumber.open(pdf_path) as pdf:
        total_pages = len(pdf.pages)
        print(f"Total pages: {total_pages}\n")
        
        all_text = []
        
        # 모든 페이지 읽기
        for i in range(total_pages):
            page = pdf.pages[i]
            text = page.extract_text()
            if text:
                all_text.append(f"\n{'='*80}\nPage {i+1}\n{'='*80}\n{text}\n")
                print(f"Page {i+1}: {len(text)} characters extracted")
            else:
                all_text.append(f"\n{'='*80}\nPage {i+1}\n{'='*80}\n[No text found]\n")
                print(f"Page {i+1}: No text found")
        
        # 파일로 저장
        full_text = "".join(all_text)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(full_text)
        
        print(f"\n✓ Text extracted and saved to: {output_path}")
        print(f"Total characters: {len(full_text)}")
        
        # 처음 2000자 미리보기
        print("\n" + "="*80)
        print("Preview (first 2000 characters):")
        print("="*80)
        print(full_text[:2000])
            
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()

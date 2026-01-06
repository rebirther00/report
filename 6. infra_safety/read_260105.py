# -*- coding: utf-8 -*-
import fitz
import os
import glob

base_path = r'C:\Users\sharp\OneDrive\문서\gitLocal\report\6. infra_safety'
output_dir = os.path.join(base_path, 'extracted_texts')
os.makedirs(output_dir, exist_ok=True)

# 260105 폴더의 모든 PDF 파일 찾기
pdf_folder = os.path.join(base_path, r"ref_docs\260105_진행계획 및 자료")

print(f"Searching in: {pdf_folder}")
print(f"Folder exists: {os.path.exists(pdf_folder)}")

if os.path.exists(pdf_folder):
    for filename in os.listdir(pdf_folder):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(pdf_folder, filename)
            # 파일명에서 안전한 출력 파일명 생성
            safe_name = filename.replace(' ', '_').replace("'", "").replace(',', '')[:50]
            output_file = os.path.join(output_dir, f'{safe_name}.txt')
            
            try:
                doc = fitz.open(pdf_path)
                text = ''
                for page in doc:
                    text += page.get_text()
                doc.close()
                
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(f"FILE: {filename}\n")
                    f.write(f"PATH: {pdf_path}\n")
                    f.write("="*80 + "\n\n")
                    f.write(text)
                
                print(f"OK: {filename[:40]}... ({len(text)} chars)")
            except Exception as e:
                print(f"ERROR: {filename[:40]}... - {e}")
else:
    print("Folder not found!")

print("\nDone!")

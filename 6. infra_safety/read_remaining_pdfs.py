# -*- coding: utf-8 -*-
import fitz
import os

base_path = r'C:\Users\sharp\OneDrive\문서\gitLocal\report\6. infra_safety'
output_dir = os.path.join(base_path, 'extracted_texts')
os.makedirs(output_dir, exist_ok=True)

# 나머지 PDF 파일들
pdf_files = [
    # 260105 폴더
    (r"ref_docs\260105_진행계획 및 자료\'26_'28 산기반 로드맵(안)_최종안내.pdf", "06_산기반_로드맵"),
    (r"ref_docs\260105_진행계획 및 자료\0430(1조간)산업기술정책과, '26년 산업·에너지 R&D 예산안 및 장비 도입계획 검토.pdf", "07_산업기술정책과_예산"),
    
    # 슈어소프트테크 - 미래기술검증솔루션
    (r"ref_docs\260106_할일 및 자료\슈어소프트테크_2025_미래기술검증솔루션(VISTA, DCAT, SIMVA, AUTOSIM, ARCHON Z)\슈어소프트테크_2025_VISTA.pdf", "08_슈어소프트_VISTA"),
    (r"ref_docs\260106_할일 및 자료\슈어소프트테크_2025_미래기술검증솔루션(VISTA, DCAT, SIMVA, AUTOSIM, ARCHON Z)\슈어소프트테크_2025_DCAT.pdf", "09_슈어소프트_DCAT"),
    (r"ref_docs\260106_할일 및 자료\슈어소프트테크_2025_미래기술검증솔루션(VISTA, DCAT, SIMVA, AUTOSIM, ARCHON Z)\슈어소프트테크_2025_SIMVA.pdf", "10_슈어소프트_SIMVA"),
    (r"ref_docs\260106_할일 및 자료\슈어소프트테크_2025_미래기술검증솔루션(VISTA, DCAT, SIMVA, AUTOSIM, ARCHON Z)\슈어소프트테크_2025_AUTOSIM.pdf", "11_슈어소프트_AUTOSIM"),
    (r"ref_docs\260106_할일 및 자료\슈어소프트테크_2025_미래기술검증솔루션(VISTA, DCAT, SIMVA, AUTOSIM, ARCHON Z)\슈어소프트테크_2025_ARCHON Z.pdf", "12_슈어소프트_ARCHON_Z"),
    
    # 슈어소프트테크 - 시스템검증솔루션
    (r"ref_docs\260106_할일 및 자료\슈어소프트테크_2025_시스템검증솔루션(FIT, PROV, AESOP, AUTORACT)\슈어소프트테크_2025_FIT.pdf", "13_슈어소프트_FIT"),
    (r"ref_docs\260106_할일 및 자료\슈어소프트테크_2025_시스템검증솔루션(FIT, PROV, AESOP, AUTORACT)\슈어소프트테크_2025_PROV.pdf", "14_슈어소프트_PROV"),
    (r"ref_docs\260106_할일 및 자료\슈어소프트테크_2025_시스템검증솔루션(FIT, PROV, AESOP, AUTORACT)\슈어소프트테크_2025_AESOP.pdf", "15_슈어소프트_AESOP"),
    (r"ref_docs\260106_할일 및 자료\슈어소프트테크_2025_시스템검증솔루션(FIT, PROV, AESOP, AUTORACT)\슈어소프트테크_2025_AUTORACT.pdf", "16_슈어소프트_AUTORACT"),
    
    # 슈어소프트테크 - 코드검증솔루션
    (r"ref_docs\260106_할일 및 자료\슈어소프트테크_2025_코드검증솔루션(STATIC, CT, COVER, VPES, V-SPICE)\슈어소프트테크_2025_STATIC.pdf", "17_슈어소프트_STATIC"),
    (r"ref_docs\260106_할일 및 자료\슈어소프트테크_2025_코드검증솔루션(STATIC, CT, COVER, VPES, V-SPICE)\슈어소프트테크_2025_CT.pdf", "18_슈어소프트_CT"),
    (r"ref_docs\260106_할일 및 자료\슈어소프트테크_2025_코드검증솔루션(STATIC, CT, COVER, VPES, V-SPICE)\슈어소프트테크_2025_COVER Cloud.pdf", "19_슈어소프트_COVER_Cloud"),
    (r"ref_docs\260106_할일 및 자료\슈어소프트테크_2025_코드검증솔루션(STATIC, CT, COVER, VPES, V-SPICE)\슈어소프트테크_2025_COVER Enterprise, Standalone.pdf", "20_슈어소프트_COVER_Enterprise"),
    (r"ref_docs\260106_할일 및 자료\슈어소프트테크_2025_코드검증솔루션(STATIC, CT, COVER, VPES, V-SPICE)\슈어소프트테크_2025_V-SPICE.pdf", "21_슈어소프트_V-SPICE"),
    (r"ref_docs\260106_할일 및 자료\슈어소프트테크_2025_코드검증솔루션(STATIC, CT, COVER, VPES, V-SPICE)\슈어소프트테크_2025_VPES.pdf", "22_슈어소프트_VPES"),
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
            
            print(f"OK: {name} ({len(text)} chars)")
        except Exception as e:
            print(f"ERROR: {name} - {e}")
    else:
        print(f"NOT FOUND: {pdf_path}")

print(f"\nAll files saved to: {output_dir}")

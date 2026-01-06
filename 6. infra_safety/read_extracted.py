# -*- coding: utf-8 -*-
import os
import sys

# stdout을 UTF-8로 설정
sys.stdout.reconfigure(encoding='utf-8')

base_path = r'C:\Users\sharp\OneDrive\문서\gitLocal\report\6. infra_safety\extracted_texts'

# 모든 txt 파일 읽기
for filename in os.listdir(base_path):
    if filename.endswith('.txt'):
        filepath = os.path.join(base_path, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 새로 추출된 파일만 출력 (로드맵, 산업기술정책과)
            if '로드맵' in filename or '산업기술정책과' in filename:
                print(f"\n{'='*80}")
                print(f"FILE: {filename}")
                print(f"SIZE: {len(content)} chars")
                print('='*80)
                print(content[:8000])
                print("\n... (truncated) ...")
        except Exception as e:
            print(f"ERROR reading {filename}: {e}")

print("\n\nDone!")

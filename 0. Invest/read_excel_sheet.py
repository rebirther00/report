# -*- coding: utf-8 -*-
"""
Excel 파일에서 '2. 종목현황' 시트의 C6:O45 범위 읽기
"""
import pandas as pd
import sys
import io

# 콘솔 출력 인코딩 설정
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

file_path = r"0. Invest/.cursor/reference/서대리투자기록시트_Ver3.0(2025년).xlsx"

# C6:O45 범위 읽기
df = pd.read_excel(
    file_path, 
    sheet_name="2. 종목현황",
    usecols="C:O",      # C~O열 선택
    skiprows=5,          # 처음 5행 스킵 (6행부터 읽기)
    nrows=40             # 40행 읽기 (6~45행)
)

# 결과 출력
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

print("=" * 80)
print("[2. 종목현황 시트 (C6:O45)]")
print("=" * 80)
print(df.to_string(index=False))
print("=" * 80)
print(f"총 {len(df)}개 행, {len(df.columns)}개 열")


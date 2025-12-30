# -*- coding: utf-8 -*-
"""
Google Sheets에서 '2. 종목현황' 시트 다운로드 및 읽기
포트폴리오 상담용 데이터 추출
"""
import requests
import pandas as pd
import io
import sys

# 콘솔 출력 인코딩 설정
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Google Sheets 정보
SHEET_ID = "1aYFV5Ym8GXfoIj5w22ZuuazxGRQsfriJgI2g3yG2FZM"
EXPORT_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=xlsx"

print("=" * 80)
print("[Google Sheets 다운로드 중...]")
print("=" * 80)

try:
    # Google Sheets 다운로드
    response = requests.get(EXPORT_URL)
    response.raise_for_status()
    
    # 메모리에서 Excel 파일 읽기
    excel_data = io.BytesIO(response.content)
    
    # 시트 목록 확인
    xl = pd.ExcelFile(excel_data)
    print(f"[시트 목록]: {xl.sheet_names}")
    print("=" * 80)
    
    # '2. 종목현황' 시트 읽기
    # C6:O45 범위 (이전과 동일하게)
    df = pd.read_excel(
        excel_data,
        sheet_name="2. 종목현황",
        usecols="C:O",      # C~O열 선택
        skiprows=5,          # 처음 5행 스킵 (6행부터 읽기)
        nrows=40             # 40행 읽기 (6~45행)
    )
    
    # NaN 행 제거 (빈 행 정리)
    df_clean = df.dropna(how='all')
    
    # 결과 출력
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 20)
    
    print("[2. 종목현황 시트 - 포트폴리오 데이터]")
    print("=" * 80)
    print(df_clean.to_string(index=False))
    print("=" * 80)
    print(f"총 {len(df_clean)}개 종목")
    
    # 포트폴리오 요약 정보 계산 시도
    print("\n[포트폴리오 요약]")
    print("-" * 40)
    
except requests.exceptions.RequestException as e:
    print(f"[오류] Google Sheets 다운로드 실패: {e}")
    print("시트가 공개 설정되어 있는지 확인해주세요.")
except Exception as e:
    print(f"[오류] 데이터 처리 중 오류 발생: {e}")


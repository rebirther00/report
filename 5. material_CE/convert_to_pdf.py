# -*- coding: utf-8 -*-
"""
마크다운 파일을 PDF로 변환하는 스크립트
"""
import subprocess
import sys
import os

def install_package(package):
    """패키지 설치"""
    subprocess.check_call([sys.executable, "-m", "pip", "install", package, "-q"])

def convert_md_to_pdf():
    """마크다운을 PDF로 변환"""
    # 필요한 패키지 설치
    try:
        import markdown
    except ImportError:
        install_package("markdown")
        import markdown
    
    try:
        from weasyprint import HTML, CSS
    except ImportError:
        install_package("weasyprint")
        from weasyprint import HTML, CSS
    
    # 현재 스크립트 디렉토리
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 변환할 파일 목록
    files = [
        "기획보고서_복합소재_AI_고소작업차.md",
        "기획보고서_복합소재_AI_경량화_굴착기_v2.md"
    ]
    
    # CSS 스타일
    css_style = """
    @page {
        size: A4;
        margin: 2cm;
    }
    body {
        font-family: 'Malgun Gothic', 'Apple SD Gothic Neo', sans-serif;
        font-size: 11pt;
        line-height: 1.6;
        color: #333;
    }
    h1 {
        font-size: 22pt;
        color: #1a1a1a;
        border-bottom: 2px solid #333;
        padding-bottom: 10px;
        margin-top: 30px;
    }
    h2 {
        font-size: 16pt;
        color: #2c3e50;
        border-bottom: 1px solid #bdc3c7;
        padding-bottom: 5px;
        margin-top: 25px;
    }
    h3 {
        font-size: 14pt;
        color: #34495e;
        margin-top: 20px;
    }
    h4 {
        font-size: 12pt;
        color: #2c3e50;
        margin-top: 15px;
    }
    table {
        width: 100%;
        border-collapse: collapse;
        margin: 15px 0;
        font-size: 10pt;
    }
    th, td {
        border: 1px solid #bdc3c7;
        padding: 8px 10px;
        text-align: left;
    }
    th {
        background-color: #ecf0f1;
        font-weight: bold;
    }
    tr:nth-child(even) {
        background-color: #f9f9f9;
    }
    code {
        background-color: #f4f4f4;
        padding: 2px 6px;
        border-radius: 3px;
        font-family: 'Consolas', 'Courier New', monospace;
        font-size: 9pt;
    }
    pre {
        background-color: #f4f4f4;
        padding: 15px;
        border-radius: 5px;
        overflow-x: auto;
        font-size: 9pt;
        line-height: 1.4;
    }
    pre code {
        background-color: transparent;
        padding: 0;
    }
    blockquote {
        border-left: 4px solid #3498db;
        padding-left: 15px;
        margin-left: 0;
        color: #666;
        font-style: italic;
    }
    ul, ol {
        margin-left: 20px;
    }
    li {
        margin-bottom: 5px;
    }
    hr {
        border: none;
        border-top: 1px solid #bdc3c7;
        margin: 20px 0;
    }
    """
    
    for md_file in files:
        md_path = os.path.join(script_dir, md_file)
        pdf_path = md_path.replace(".md", ".pdf")
        
        if not os.path.exists(md_path):
            print(f"파일을 찾을 수 없습니다: {md_file}")
            continue
        
        print(f"변환 중: {md_file}")
        
        # 마크다운 파일 읽기
        with open(md_path, "r", encoding="utf-8") as f:
            md_content = f.read()
        
        # 마크다운을 HTML로 변환
        html_content = markdown.markdown(
            md_content,
            extensions=['tables', 'fenced_code', 'toc']
        )
        
        # HTML 문서 생성
        full_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>{md_file}</title>
        </head>
        <body>
            {html_content}
        </body>
        </html>
        """
        
        # PDF로 변환
        try:
            HTML(string=full_html).write_pdf(
                pdf_path,
                stylesheets=[CSS(string=css_style)]
            )
            print(f"✅ 변환 완료: {os.path.basename(pdf_path)}")
        except Exception as e:
            print(f"❌ 변환 실패: {md_file} - {e}")

if __name__ == "__main__":
    convert_md_to_pdf()

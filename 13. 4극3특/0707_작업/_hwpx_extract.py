# -*- coding: utf-8 -*-
"""hwpx -> text 추출. 표는 | 셀 | 셀 | 형태, 메모(hp:memogroup)도 별도 덤프."""
import sys, zipfile, re
import xml.etree.ElementTree as ET

def local(tag):
    return tag.split('}')[-1]

def children(e, name):
    return [c for c in e if local(c.tag) == name]

def render_p(p, out, depth=0):
    buf = []
    def flush():
        s = ''.join(buf).strip()
        if s:
            out.append('  ' * depth + s)
        buf.clear()
    def walk(e):
        for ch in e:
            t = local(ch.tag)
            if t == 't':
                buf.append(''.join(ch.itertext()))
            elif t == 'tbl':
                flush()
                render_tbl(ch, out, depth)
            elif t == 'p':
                flush()
                render_p(ch, out, depth)
            else:
                walk(ch)
    walk(p)
    flush()

def render_tbl(tbl, out, depth):
    out.append('  ' * depth + '[TABLE]')
    for tr in children(tbl, 'tr'):
        cells = []
        for tc in children(tr, 'tc'):
            cell = []
            for sub in children(tc, 'subList'):
                for p in children(sub, 'p'):
                    render_p(p, cell, 0)
            cells.append(' / '.join(cell))
        out.append('  ' * depth + '| ' + ' | '.join(cells) + ' |')
    out.append('  ' * depth + '[/TABLE]')

def extract(path, outpath):
    z = zipfile.ZipFile(path)
    sections = sorted([n for n in z.namelist() if re.match(r'Contents/section\d+\.xml', n)],
                      key=lambda n: int(re.search(r'(\d+)', n).group(1)))
    out = []
    memos = []
    for sec in sections:
        out.append(f'\n{"="*70}\n=== {sec} ===\n{"="*70}')
        root = ET.fromstring(z.read(sec))
        for p in root:
            t = local(p.tag)
            if t == 'p':
                render_p(p, out, 0)
            elif t == 'tbl':
                render_tbl(p, out, 0)
        # 메모 수집 (memogroup 은 위치 무관 전체 검색)
        for mg in root.iter():
            if local(mg.tag) == 'memogroup':
                for memo in mg:
                    mtxt = []
                    render_p(memo, mtxt, 0)
                    if mtxt:
                        memos.append(f'[{sec}] ' + ' / '.join(mtxt))
    if memos:
        out.append(f'\n{"="*70}\n=== MEMOS ===\n{"="*70}')
        out.extend(memos)
    with open(outpath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out))
    print('done ->', outpath, f'({len(out)} lines, memos={len(memos)})')

if __name__ == '__main__':
    extract(sys.argv[1], sys.argv[2])

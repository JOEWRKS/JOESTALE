# -*- coding: utf-8 -*-
"""collect_examples.py — 문장 독자 결과 표에서 검수자가 **새로 쓴 토막**을 설계서 user_examples에 모은다(T-082).

쓰임: python collect_examples.py design.json "review_out*/문장독자*.md" [--reset]
- 표의 둘째 칸(본문 인용)과 다섯째 칸(고친 문장)을 공백 없이 비교해, 고친 문장에서 원문에 없는 12자 이상 토막만 뽑는다(낱말 하나 바꾼 것은 안 모은다).
  (원문을 그대로 둔 부분까지 모으면 X3가 본문 전체를 잡는다.)
- 뽑은 토막을 design.user_examples에 더한다(중복 제외). 그 뒤 check_text.py의 X3가 본문이 그 토막을 옮겨 적었는지 본다(패턴 58·90·98).
- 패스마다 검수 결과를 받은 직후 돌린다. 설계서 `user_examples`는 손으로 옮기지 않는다. --reset은 기존 목록을 비우고 다시 모은다.
"""
import sys, json, re, glob

WIN = 8      # 원문과 겹침을 보는 창
MIN_FRAG = 12   # 모을 토막의 최소 길이(낱말 하나 바꾼 것은 모으지 않는다 — 문장 단위 옮김만)

def flat(s):
    return re.sub(r'\s+', '', s)

def novel_fragments(orig, fix, n=WIN):
    o, f = flat(orig), flat(fix)
    if len(f) < n:
        return []
    covered = [False] * len(f)
    for i in range(len(f) - n + 1):
        if f[i:i + n] in o:
            for k in range(i, i + n):
                covered[k] = True
    out, run = [], ''
    for ch, c in zip(f, covered):
        if c:
            if len(run) >= MIN_FRAG:
                out.append(run)
            run = ''
        else:
            run += ch
    if len(run) >= MIN_FRAG:
        out.append(run)
    return out

def extract(md):
    out = []
    for line in md.splitlines():
        if not line.startswith('|'):
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) < 5 or cells[0] in ('#', '') or set(cells[0]) <= set('-'):
            continue
        orig, fix = cells[1], cells[4]
        fix = re.sub(r'\(.*?\)', '', fix).replace('<br>', ' ')
        orig = orig.replace('<br>', ' ')
        out += novel_fragments(orig, fix)
    return out

def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    reset = '--reset' in sys.argv
    if len(args) < 2:
        print(__doc__); sys.exit(1)
    dp = args[0]
    files = []
    for pat in args[1:]:
        files += glob.glob(pat)
    d = json.load(open(dp, encoding='utf-8'))
    ex = [] if reset else list(d.get('user_examples') or [])
    seen = set(flat(e) for e in ex)
    added = 0
    for f in sorted(files):
        for piece in extract(open(f, encoding='utf-8').read()):
            if piece not in seen:
                seen.add(piece); ex.append(piece); added += 1
    d['user_examples'] = ex
    json.dump(d, open(dp, 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
    print(f'user_examples {len(ex)} (+{added}) ← {len(files)} files')

if __name__ == '__main__':
    main()

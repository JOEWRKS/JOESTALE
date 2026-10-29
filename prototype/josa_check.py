import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from kiwipiepy import Kiwi
k = Kiwi()
def batchim(ch):
    c = ord(ch)
    return None if not (0xAC00 <= c <= 0xD7A3) else (c - 0xAC00) % 28
P = {'이':1,'가':0,'을':1,'를':0,'은':1,'는':0,'과':1,'와':0,'이랑':1,'랑':0,'으로':1,'로':0,'아':1,'야':0}
pat = re.compile(r'([가-힣]+?)(이랑|으로|이|가|을|를|은|는|과|와|랑|로|아|야)(?=[\s.,!?]|$)')
def flags(text):
    out = []
    for m in pat.finditer(text):
        stem, j = m.group(1), m.group(2)
        b = batchim(stem[-1])
        if b is None: continue
        want = P[j]
        has = 1 if b else 0
        if j == '로' and b == 8: has = 0          # ㄹ받침 + 로
        if j == '으로' and b == 8: has = 1        # 서울으로 -> wrong (flag)
        if want != has:
            # confirm stem is nominal via Kiwi
            toks = k.tokenize(stem)
            if toks and toks[-1].tag[0] in 'NX' or toks[-1].tag in ('SL','SN','NP','NNB'):
                out.append((stem, j))
    return out
tests = ["경첩가 쇳소리를 뱉어냈다.", "바람를 맞으며 뺨이 베였다.", "그녀은 식빵을 집어 들었다.",
         "손톱로 눌렀다. 서울으로 갔다. 창틈으로 밀려든 바람. 칼로 벴다.",
         "문손잡이를 당기자 녹슨 경첩이 쇳소리를 뱉어냈다. 마트 마감 시간이 되자 그녀는 식빵을 집어 들었다."]
for t in tests: print(t, '->', flags(t))

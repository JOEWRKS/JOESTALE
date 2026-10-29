import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from kiwipiepy import Kiwi
k = Kiwi()
pairs = [
 ("낡고 오래된 문이 시끄럽게 열렸다.", "문손잡이를 당기자 녹슨 경첩이 쇳소리를 뱉어냈다."),
 ("매서운 바람이 몹시 차갑게 불었다.", "창틈으로 밀려든 바람이 뺨을 베고 지나갔다. 난로 곁에 둔 물그릇 표면에 살얼음이 덮였다."),
 ("그는 매우 꼼꼼하고 예민한 성격이었다.", "그는 책상 위 연필 세 자루의 끄트머리가 일직선이 되도록 나란히 맞췄다. 지우개 가루 하나 없는 매끄러운 책상 표면을 손끝으로 두 번 쓸어내린 뒤에야 비로소 의자에 등을 기댔다."),
 ("그녀는 지독한 가난에 시달리며 늘 위축되어 있었다.", "마트 마감 시간이 되자 그녀는 반값 할인 스티커가 세 겹으로 덧붙여진 식빵을 집어 들었다. 딱딱해진 빵 가장자리를 손톱으로 꾹 눌러본 뒤, 타인의 시선을 피하듯 카트 맨 밑바닥으로 소리 없이 밀어 넣었다."),
]
def stats(t):
    toks = k.tokenize(t)
    c = {}
    for tk in toks:
        c[tk.tag] = c.get(tk.tag, 0) + 1
    content = sum(v for tg, v in c.items() if tg[0] in 'NVM' and tg != 'VCP' and tg != 'VCN')
    adv = c.get('MAG', 0); adj = c.get('VA', 0) + c.get('MM', 0)
    noun = sum(v for tg, v in c.items() if tg.startswith('NN'))
    verb = c.get('VV', 0)
    return dict(adv=adv, adj=adj, noun=noun, verb=verb, content=content, ratio=round((adv+adj)/max(content,1),2),
                advs=[tk.form for tk in toks if tk.tag=='MAG'], adjs=[tk.form for tk in toks if tk.tag in ('VA','MM')])
for a, b in pairs:
    print("BEFORE:", stats(a)); print("AFTER :", stats(b)); print()

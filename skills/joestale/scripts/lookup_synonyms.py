"""우리말샘 오픈 API로 비슷한말·반대말·상위어·하위어를 조회한다 (Phase 2).

사용: OPENDICT_KEY=<키> python lookup_synonyms.py <단어> [--related-check <단어2>]

- 키는 환경변수 OPENDICT_KEY에서만 읽는다. 파일·기록에 적지 않는다.
- --related-check: 두 단어가 비슷한말/반대말/상하위 관계이면 exit 2 (강제 결합 시드로 부적합).
- 이 스크립트는 키가 없으면 안내만 하고 exit 3. 실제 응답 확인은 ROADMAP P2-1.
API 문서: https://opendict.korean.go.kr/service/openApiInfo
"""
import sys, os, re, json, argparse, urllib.request, urllib.parse
from http.client import IncompleteRead

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

SEARCH = "https://opendict.korean.go.kr/api/search"
VIEW = "https://opendict.korean.go.kr/api/view"
REL_TYPES = {"비슷한말", "반대말", "상위어", "하위어", "참고 어휘"}
# 너무 일반적인 상위어는 "공통 범주" 판정에서 제외(곳·것·사람 등은 거의 모든 명사를 묶는다)
GENERIC_HYPERNYMS = {"곳", "것", "일", "사람", "물건", "물체", "현상", "상태", "행동", "부분", "말", "때", "장소", "물질", "동물", "식물"}

def _get(url, params, tries=3):
    q = urllib.parse.urlencode(params, encoding="utf-8")
    last = None
    for _ in range(tries):   # 서버가 가끔 chunked 응답을 끊는다(IncompleteRead) → 재시도
        try:
            with urllib.request.urlopen(f"{url}?{q}", timeout=20) as r:
                body = r.read().decode("utf-8")
            if body.lstrip().startswith("<"):
                raise RuntimeError("API가 JSON 대신 XML/오류를 반환: " + body[:200])
            return json.loads(body)
        except (IncompleteRead, json.JSONDecodeError, TimeoutError) as e:
            last = e
    raise last

def strip_homograph(w):
    """우리말샘 관계어는 '접철002', '갓-바다001'처럼 동형어 번호·하이픈이 붙는다 → '접철', '갓바다'."""
    return re.sub(r"\d{3}$", "", w or "").replace("-", "")

def search_codes(key, word, limit=10):
    """표제어가 정확히 word인 항목의 sense target_code 목록. num은 10~100만 허용(오류 103)."""
    d = _get(SEARCH, {"key": key, "q": word, "req_type": "json", "num": max(10, limit), "advanced": "y", "target": 1, "method": "exact"})
    items = d.get("channel", {}).get("item", []) or []
    codes = []
    for it in items:
        if it.get("word") != word:
            continue
        for s in it.get("sense", []) or []:
            if s.get("target_code"):
                codes.append((s["target_code"], s.get("definition", "")))
    return codes

def relations(key, word):
    """{관계유형: [단어...]} 와 뜻풀이 목록. view 응답의 senseInfo(dict 또는 list) 안 relation_info만 본다. 없으면 빈 dict."""
    out, defs = {}, []
    for code, definition in search_codes(key, word):
        d = _get(VIEW, {"key": key, "q": code, "method": "target_code", "req_type": "json"})
        item = d.get("channel", {}).get("item", {}) or {}
        senses = item.get("senseInfo") or item.get("sense_info") or []
        if isinstance(senses, dict):
            senses = [senses]
        for s in senses:
            defs.append(s.get("definition", definition))
            for rel in s.get("relation_info") or []:
                out.setdefault(rel.get("type", "?"), set()).add(strip_homograph(rel.get("word")))
    return {k: sorted(v) for k, v in out.items()}, defs

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("word")
    ap.add_argument("--related-check")
    a = ap.parse_args()
    key = os.environ.get("OPENDICT_KEY")
    if not key:
        print(json.dumps({"error": "OPENDICT_KEY 환경변수가 없음. opendict.korean.go.kr에서 인증키 신청 후 설정"}, ensure_ascii=False))
        sys.exit(3)
    rel, defs = relations(key, a.word)
    print(json.dumps({"word": a.word, "senses": len(defs), "definitions": defs[:5], "relations": rel}, ensure_ascii=False, indent=1))
    if a.related_check:
        other = a.related_check.replace("-", "")
        hit = [t for t, ws in rel.items() if t in REL_TYPES and other in ws]
        if not hit:   # 반대 방향도 본다: 상대 단어의 관계어에 이 단어가 있는가
            rel2, _ = relations(key, a.related_check)
            hit = [f"{t}(역방향)" for t, ws in rel2.items() if t in REL_TYPES and a.word.replace("-", "") in ws]
            # 공통 범주(소금/설탕=조미료): 두 단어의 상위어가 겹치면 관계 있음으로 본다 (작가 규칙: 공통분모가 있으면 탈락)
            shared = (set(rel.get("상위어", [])) & set(rel2.get("상위어", []))) - GENERIC_HYPERNYMS
            if shared:
                hit.append("공통 상위어:" + ",".join(sorted(shared)))
        if hit:
            print(json.dumps({"related": True, "types": hit}, ensure_ascii=False))
            sys.exit(2)
        print(json.dumps({"related": False}, ensure_ascii=False))

if __name__ == "__main__":
    main()

"""우리말샘 오픈 API로 비슷한말·반대말·상위어·하위어를 조회한다 (Phase 2).

사용: OPENDICT_KEY=<키> python lookup_synonyms.py <단어> [--related-check <단어2>]

- 키는 환경변수 OPENDICT_KEY에서만 읽는다. 파일·기록에 적지 않는다.
- --related-check: 두 단어가 비슷한말/반대말/상하위 관계이면 exit 2 (강제 결합 시드로 부적합).
- 이 스크립트는 키가 없으면 안내만 하고 exit 3. 실제 응답 확인은 ROADMAP P2-1.
API 문서: https://opendict.korean.go.kr/service/openApiInfo
"""
import sys, os, json, argparse, urllib.request, urllib.parse

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

SEARCH = "https://opendict.korean.go.kr/api/search"
VIEW = "https://opendict.korean.go.kr/api/view"
REL_TYPES = {"비슷한말", "반대말", "상위어", "하위어", "참고 어휘"}

def _get(url, params):
    q = urllib.parse.urlencode(params, encoding="utf-8")
    with urllib.request.urlopen(f"{url}?{q}", timeout=15) as r:
        return json.loads(r.read().decode("utf-8"))

def search_codes(key, word, limit=5):
    d = _get(SEARCH, {"key": key, "q": word, "req_type": "json", "num": limit, "advanced": "y", "target": 1, "method": "exact"})
    items = d.get("channel", {}).get("item", [])
    return [it.get("target_code") for it in items if it.get("target_code")]

def relations(key, word):
    out = {}
    for code in search_codes(key, word):
        d = _get(VIEW, {"key": key, "q": code, "method": "target_code", "req_type": "json"})
        item = d.get("channel", {}).get("item", {})
        senses = item.get("senseInfo", item.get("sense_info", []))
        if isinstance(senses, dict):
            senses = [senses]
        for s in senses:
            for rel in s.get("relation_info", []):
                out.setdefault(rel.get("type", "?"), set()).add(rel.get("word"))
    return {k: sorted(v) for k, v in out.items()}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("word")
    ap.add_argument("--related-check")
    a = ap.parse_args()
    key = os.environ.get("OPENDICT_KEY")
    if not key:
        print(json.dumps({"error": "OPENDICT_KEY 환경변수가 없음. opendict.korean.go.kr에서 인증키 신청 후 설정"}, ensure_ascii=False))
        sys.exit(3)
    rel = relations(key, a.word)
    print(json.dumps({"word": a.word, "relations": rel}, ensure_ascii=False, indent=1))
    if a.related_check:
        hit = [t for t, ws in rel.items() if t in REL_TYPES and a.related_check in ws]
        if hit:
            print(json.dumps({"related": True, "types": hit}, ensure_ascii=False))
            sys.exit(2)
        print(json.dumps({"related": False}, ensure_ascii=False))

if __name__ == "__main__":
    main()

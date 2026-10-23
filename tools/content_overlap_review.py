"""Candidate-only TF-IDF and shared-sentence review, no destructive SEO decisions."""
import argparse,collections,html,json,math,re
from pathlib import Path

def tokens(s):return re.findall(r"[a-z][a-z0-9]+",s.lower())
STOP=set("the and for with that this from your our you are was were have has not can into they their will its these those then than when where which who why how what should could would each only some more also both all any been being them but as at by if in is it of on or to an be do no we so us up".split())
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--audit",required=True);a=ap.parse_args();p=Path(a.audit)
    data=json.loads((p/"page-snapshots.json").read_text(encoding="utf-8"))["pages"]
    docs=[];seen=set()
    for r in data:
        if "evbtms.com" in r["requested"] and "/products/" in r["requested"]:continue
        if r["title"].startswith("News -"):continue
        if "evbtms.com" in r["requested"] and r["requested"] not in [x["url"] for x in json.loads((p/"inventory.json").read_text(encoding="utf-8"))["entries"] if x["type"]=="article"]:continue
        canonical=r["canonical"][0] if r["canonical"] else r["requested"]
        if canonical in seen:continue
        seen.add(canonical);docs.append({"url":canonical,"title":r["h1"][0] if r["h1"] else r["title"],"text":r["body_text"]})
    counters=[collections.Counter(w for w in tokens(d["text"]) if w not in STOP) for d in docs]
    df=collections.Counter(w for c in counters for w in c)
    vectors=[];norms=[]
    for c in counters:
        v={w:(1+math.log(n))*math.log((1+len(docs))/(1+df[w])) for w,n in c.items() if df[w]<len(docs)*.45}
        vectors.append(v);norms.append(math.sqrt(sum(x*x for x in v.values())) or 1)
    rows=[]
    for i,a in enumerate(docs):
        for j,b in enumerate(docs[i+1:],i+1):
            if ("evbtms.com" in a["url"])==("evbtms.com" in b["url"]):continue
            small,large=(vectors[i],vectors[j]) if len(vectors[i])<len(vectors[j]) else (vectors[j],vectors[i])
            score=sum(v*large.get(w,0) for w,v in small.items())/(norms[i]*norms[j])
            if score>.10:rows.append({"a":a["url"],"a_title":a["title"],"b":b["url"],"b_title":b["title"],"tfidf_cosine":round(score,4),"interpretation":"topic-overlap candidate, not proof of duplicate wording or Google cannibalization"})
    rows.sort(key=lambda x:x["tfidf_cosine"],reverse=True)
    # Sentence matches are exact after token normalization. Common boilerplate is filtered by document frequency.
    sentence_docs=collections.defaultdict(set);sentences={}
    for i,d in enumerate(docs):
        for sent in re.split(r"(?<=[.!?])\s+",d["text"]):
            ts=tokens(sent)
            if len(ts)<14 or len(ts)>85:continue
            key=" ".join(ts)
            sentence_docs[key].add(i);sentences[key]=sent
    shared=[]
    for key,ids in sentence_docs.items():
        if len(ids)<2 or len(ids)>5:continue
        sites={"new" if "evbtms.com" in docs[i]["url"] else "old" for i in ids}
        if len(sites)<2:continue
        shared.append({"sentence":sentences[key],"urls":[docs[i]["url"] for i in sorted(ids)],"note":"Exact normalized sentence; may still be a standard definition, not necessarily copied."})
    payload={"method":"TF-IDF across public text with common-site terms excluded; no search-volume/GSC conclusions","documents":len(docs),"pairs":rows[:50],"shared_sentences":shared[:30]}
    (p/"cross-site-overlap-evidence.json").write_text(json.dumps(payload,ensure_ascii=False,indent=2),encoding="utf-8")
    lines=["# 两站正文主题重叠候选","","注意：相似度不是重复率，不是AI检测，也不是谷歌关键词互抢证据。仅用于排定人工核对顺序。","公共文本包含部分页眉页脚，已用词频过滤，仍有误差。没有据此执行删除、301或canonical。","","| New/Old article A | Article B | Topic cosine |","|---|---|---|"]
    for r in rows[:20]:lines.append(f"| [{r['a_title']}]({r['a']}) | [{r['b_title']}]({r['b']}) | {r['tfidf_cosine']} |")
    lines+=["","## 精确归一化句子候选",""]
    for r in shared[:10]:lines.append("- "+r["sentence"]+"\n  Sources: "+" ; ".join(r["urls"]))
    if not shared:lines.append("未发现符合本脚本长度和频次过滤规则的跨站精确句子；不等于不存在改写或复制。")
    (p/"cross-site-overlap-review.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
    print(json.dumps({"documents":len(docs),"topic_candidates":len(rows),"exact_sentence_candidates":len(shared),"top_pairs":rows[:5]},ensure_ascii=False))
if __name__=="__main__":main()

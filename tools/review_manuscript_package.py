"""Offline manuscript consistency checks. Does not perform AI detection."""
import argparse,hashlib,html,json,re
from pathlib import Path

def plain(s):
    s=re.sub(r"</(?:p|h[1-6]|li)>","\n\n",s)
    return re.sub(r"\n{3,}","\n\n",html.unescape(re.sub(r"<[^>]*>","",s))).strip()

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--root",required=True);a=ap.parse_args();root=Path(a.root)
    configs=[
      ("BTMS","REPORTS/three-hour-2026-10-22/DAILY-BTMS-1022-rework-v2.md","REPORTS/detection-1022/DAILY-BTMS-1022-configuration-v2.txt"),
      ("HVCH","REPORTS/three-hour-2026-10-22/DAILY-HVCH-1022-rework-v2.md","REPORTS/detection-1022/DAILY-HVCH-1022-low-voltage-wake-up-v2.txt")]
    rows=[]
    for label,md,txt in configs:
        doc=(root/md).read_text(encoding="utf-8")
        m=re.search(r"```html\n([\s\S]*?)\n```",doc)
        body=m.group(1) if m else ""
        generated=plain(body)
        actual=(root/txt).read_text(encoding="utf-8").strip()
        first=re.search(r"<p>([\s\S]*?)</p>",body)
        intro=plain(first.group(1)) if first else ""
        bans=re.findall(r"\b(?:delve|furthermore|moreover|in conclusion|it is important to note)\b",generated,re.I)
        experiences=re.findall(r"\b(?:we have tested|we have seen|our engineers measured|our customers achieved|we shipped)\b",generated,re.I)
        links=re.findall(r'<a\s+href="([^"]+)"[^>]*>(.*?)</a>',body,re.S)
        rows.append({"article":label,"draft":md,"fixed_text":txt,"word_count_approx":len(generated.split()),"body_h1_count":len(re.findall(r"<h1\b",body,re.I)),"first_sentence_starts_the":bool(re.match(r"the\b",intro,re.I)),"banned_tone_tokens":bans,"unsubstantiated_experience_phrases_flagged":experiences,"links":[{"url":u,"anchor":plain(t)} for u,t in links],"plain_text_matches_html":actual==generated,"normalized_utf8_lf_sha256":hashlib.sha256((generated+"\n").encode()).hexdigest(),"ai_detection":{"ZeroGPT":None,"GPTZero":None,"status":"NOT_TESTED_THIS_VERSION"},"limits":"Automated text checks do not establish technical correctness, natural authorship, AI score, rights, search demand or publication readiness."})
    p=root/"REPORTS/three-hour-2026-10-22/rework-package-qa.json";p.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps(rows,ensure_ascii=False))
if __name__=="__main__":main()

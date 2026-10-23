"""Build local-only review, never publish articles."""
import html,re
from pathlib import Path

root=Path(__file__).resolve().parents[1]
out=root/'REPORTS/three-hour-2026-10-22'
sections=[]
for name,title,picture in [
 ('DAILY-BTMS-1022-rework-v2.md','BTMS配置说明（723词）','assets/btms-configuration-v2-feature.webp'),
 ('DAILY-HVCH-1022-rework-v2.md','HVCH供电与控制取证（931词）','../assets/daily-2026-10-22/hvch-start-up-review-feature.webp')]:
    text=(out/name).read_text(encoding='utf-8')
    match=re.search(r'```html\n([\s\S]*?)\n```',text)
    body=match.group(1)
    sections.append(f'<section><h1>{title}</h1><p class="notice">v2尚未实测AI检测；不套用v1分数。待Peter审核，不发布。落点为现有页面补充候选，不自动新建URL。</p><img src="{picture}" alt="EVLINK article configuration illustration"><article>{body}</article><p><a href="{name}">完整发布包与资料边界</a></p></section>')
page='''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>两篇返工v2审稿</title><style>body{margin:0;background:#f1f5f8;color:#213344;font:17px/1.8 system-ui}main{max-width:960px;margin:auto;padding:24px}section{background:white;padding:30px;margin:20px 0;border-radius:12px}img{width:100%;height:auto}h1,h2{line-height:1.3}a{color:#276fa8}.notice{padding:16px;background:#fff1d2}article{overflow-wrap:anywhere}@media(max-width:500px){main{padding:8px}section{padding:18px}h1{font-size:26px}}</style><main><h1>Codex返工v2 · 待审核</h1><p>旧气流选题重复已撤销。本页仅为本地审稿，不代表网站上线、检测通过或手机端验收。</p>'''+''.join(sections)+'</main></html>'
(out/'peter-review-v2.html').write_text(page,encoding='utf-8')
print(out/'peter-review-v2.html')

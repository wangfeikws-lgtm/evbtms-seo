"""Format supplied T12-W2-05, preserving non-whitespace text."""
from pathlib import Path
import html,re,json
src=Path('C:/Users/Administrator/.codex/attachments/3a7aabf4-9735-4559-9a4a-9dfffac9311f/已粘贴的文本.txt')
out=Path(__file__).resolve().parents[1]/'REPORTS/2026-10-23'
lines=[s.strip() for s in src.read_text(encoding='utf-8-sig').strip().splitlines() if s.strip()];label=lines.pop(0)
heads={'The Battery’s “Second Home”—the Storage Rack','In January, drivers still have to hit the road.','Connectors are put through rigorous tests every day.','A Five-Minute Battery Swap with Two-Hour Aftereffects','Our Recommendations for Technical Specifications','Frequently Asked Questions on This Topic'}
faq={'Do trucks using the battery-swapping model need to be equipped with lower-power onboard heaters?','Can the temperature control at battery swap stations completely replace the vehicle’s onboard battery heating system?','Who should bear the cost of the energy consumed by the battery swap station during preheating?'}
start=lines.index('The temperature control capabilities (heating and cooling) of the battery-swapping station should be sufficient to meet battery-swapping demand during peak hours.')
parts=[]
for i,line in enumerate(lines):
    if i==start:parts.append('<ol>')
    if i==start+5:parts.append('</ol>')
    tag='li' if start<=i<start+5 else 'h2' if line in heads else 'h3' if line in faq else 'p'
    parts.append(f'<{tag}>'+html.escape(line)+f'</{tag}>')
body='\n'.join(parts)+'\n'
norm=lambda s:re.sub(r'\s+','',s)
assert norm(html.unescape(re.sub('<[^>]*>','',body)))==norm(''.join(lines))
(out/'T12-W2-05-peter-body.html').write_text(body,encoding='utf-8')
title='Battery-Swapping Heavy Trucks Need Thermal Management Too'
page='<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+title+'</title><style>body{max-width:920px;margin:30px auto;padding:20px;font:18px/1.8 system-ui;color:#253746}h1,h2,h3{line-height:1.35}h2{margin-top:38px}li{margin:12px 0}</style><h1>'+title+'</h1>'+body+'</html>'
(out/'T12-W2-05-peter-reading.html').write_text(page,encoding='utf-8')
(out/'T12-W2-05-format-check.json').write_text(json.dumps({'body_non_whitespace_matches':True,'removed_internal_label':label,'ai_detection_this_version':'NOT_TESTED','publication':'NOT_PUBLISHED_BY_CODEX'},ensure_ascii=False,indent=2),encoding='utf-8')
print('Formatted complete article; text equality verified.')

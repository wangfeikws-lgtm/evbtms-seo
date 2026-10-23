"""Assemble unchanged source drafts with separate editorial review notes."""
from pathlib import Path
import re,html,json
root=Path(__file__).resolve().parents[1]
reports=root/'REPORTS';out=reports/'2026-10-23';out.mkdir(exist_ok=True)
items=[
('T12-W2-01','重卡15kW与35kW加热器选型','T12-W2-01-15kw-vs-35kw-hvch-sizing-heavy-duty-trucks-publish-package-v2.md','22.6%',[
'审核重点：客户是否需要按电池质量、温升、预热时间和电压选型，而非只比较功率。',
'发布前返工：首句以The开头，违反Peter开头规范；未经证据支持的询盘经历不能写成真实经历。',
'算例应明确全部是假设与理想下限：2,000kg、比热1kJ/(kg·K)、温升20K，对应约11.1kWh；15/35kW除法不能承诺实际45/20分钟。',
'“只取电池或客舱较大负荷”忽略同时需求，不能直接作为通用选型结论。',
'自2021出货、六台35kW/210kW项目、12kg及冗余效果等主张需对应证据；由编辑查来源，不要求Peter凭印象确认。']),
('T12-W2-02','高压加热器IP67与EMC参数核验','T12-W2-02-ip67-emc-high-voltage-heaters-publish-package-v2.md','27.2%',[
'审核重点：文章是否帮助采购索要具体型号对应的防护与EMC资料，而不是把所有产品统称已认证。',
'验收要求：IP67适用条件、EMC报告对象、线束/安装配置与标准版本须区分；具体技术声明由编辑查证后再交最终稿。',
'本次汇编不代表已逐项完成技术来源或全文事实审核；分数只是Muse记录。']),
('T12-W2-03','氢燃料电池客车20kW级供暖选型','T12-W2-03-hydrogen-fuel-cell-bus-heating-20kw-ptc-publish-package-v3.md','24.1%',[
'建议标题：Hydrogen Fuel Cell Bus Heating: How to Evaluate a 20 kW-Class Coolant Heater。删除“成为标准答案”的普适结论。',
'正文中“每个项目首会”“冬奥每辆车”“−7°C研究”“15–25kW负荷”均需明确来源或改成有条件的示例。',
'E系列20–24kW/400–800V与CAN控制建议须分开：既有型号资料中E系列不是CAN型号，不能让读者误认原生支持。',
'燃料电池回路冷却液必须按堆与系统要求，不能笼统要求只用去离子水。',
'需要Peter审核的是选题/表达是否符合业务；以上工程事实由我们返工核实，不让Peter代替技术验证。']),
('T12-W2-04','风暖与液暖总成本比较','T12-W2-04-air-heater-vs-coolant-heater-total-cost-publish-package-v2.md','13.7%',[
'审核重点：是否客观解释现有冷却回路、安装件、维护、供暖对象对总成本的影响。',
'不批准没有报价依据的价格、回本期或节省比例；不能把液暖写成任何项目都更便宜。',
'正式发布前仍须Muse完成全文事实与内链验收；当前只呈现存档版本。']),
('T12-W2-05','换电重卡与换电站热管理','T12-W2-05-battery-swapping-heavy-trucks-thermal-management-publish-package-v2.md','3.5%',[
'审核重点：车辆与换电站如何分配电池温度管理、客舱供暖和接口维护责任。',
'开场夜间换电场景须标为假设，不伪装成真实客户经历；“我们经常对客户说”须有依据。',
'432/513kWh、五分钟换电、约两小时惩罚、十年一次气阻等具体数字没有来源不能当成事实。',
'普通插充车辆冷却回路“终身密封”、低温电池在行驶中必然降温等绝对化表述需返工。',
'低分不代表这些主张正确，不建议照当前版本直接发布。']),
('DAILY-BTMS-1022-v2','5kW BTMS配置差异','three-hour-2026-10-22/DAILY-BTMS-1022-rework-v2.md','尚未检测',[
'审核：是否保留LDC502HA与LDC560HA加热选项差异、5kW型号电压窗口比较。',
'建议用于现有评级文或5kW产品页增补，不再新建重复气流文章；最终落点待确认。',
'不宣称真实气流试验；参数引用内部型号汇总，原始规格修订仍需对应。',
'v2未检测；旧稿69%不适用于此稿。']),
('DAILY-HVCH-1022-v2','HVCH不加热：供电与控制取证','three-hour-2026-10-22/DAILY-HVCH-1022-rework-v2.md','尚未检测',[
'审核：是否采用按具体型号区分控制接口、把请求功率和实际供热证据分开的表达。',
'示例计算不是测量值，不写成客户故障案例，不给非专业人员带电操作指导。',
'优先现有文章补充候选，不自动新建URL；v2未检测，不能套用旧稿62.6%。'])]
sections=[];index=[]
for ident,cn,file,score,notes in items:
    doc=(reports/file).read_text(encoding='utf-8')
    body=re.search(r'```html\s*\n([\s\S]*?)\n```',doc)
    if not body:raise ValueError(file)
    body=body.group(1)
    seo=doc.split('```html')[0]
    first=re.search(r'<p\b[^>]*>([\s\S]*?)</p>',body)
    first_text=html.unescape(re.sub('<[^>]+>','',first.group(1))) if first else ''
    flags='首段以The开头：需按已定规则修改。' if re.match(r'The\b',first_text) else '首段The检查未命中；不代表全文已过审。'
    notes=notes+[flags]
    sections.append(f'<section id="{ident}"><h2>{ident} · {cn}</h2><p class="badge">检测记录：{score}｜本页未重新检测｜未经Peter最终审核不得发布</p><h3>具体审核明细</h3><ul>'+''.join('<li>'+html.escape(n)+'</li>' for n in notes)+f'</ul><p><b>请反馈：</b>保留方向／修改意见／暂缓。技术证据不足项由编辑先补齐，不默认要求Peter背书。</p><details><summary>SEO字段及原稿说明</summary><pre>{html.escape(seo)}</pre></details><h3>完整英文正文（原样汇编，未改写）</h3><article>'+body+f'</article><p><a href="../{html.escape(file)}">原始版本文件</a></p></section>')
    index.append(f'<a href="#{ident}">{ident} {cn}</a>')
page='''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>10月23日逐篇审核明细</title><style>body{font:17px/1.8 system-ui;background:#edf2f6;color:#233548;margin:0}main{max-width:1050px;margin:auto;padding:24px}section{background:white;padding:30px;margin:26px 0;border-radius:12px}h1,h2,h3{line-height:1.35}a{color:#226aa5}nav a{display:block}.badge{background:#fff0c9;padding:14px}article{border-top:2px solid #4789c6;padding-top:20px;overflow-wrap:anywhere}pre{white-space:pre-wrap;overflow-wrap:anywhere;font:14px/1.7 system-ui}li{margin-bottom:10px}@media(max-width:500px){main{padding:8px}section{padding:16px}h2{font-size:24px}}</style><main><h1>10月23日 · 7篇稿件详细审核</h1><p class="badge">这不是可直接发布的合格包。五篇老站稿的检测数字来自Muse存档，事实/技术验收尚有问题；两篇新站v2未检测。修改正文后旧分数失效，需对新版本重测。低AI分数不是实际人工比例，也不是事实正确证明。</p><p>老站：Codex参与初稿，Muse最终重组/检测并负责验收；新站两稿：Codex负责。Peter审业务表达并决定最终发布。以下保留原文，编辑问题单独标注。</p><nav>'''+''.join(index)+'</nav>'+''.join(sections)+'</main></html>'
(out/'peter-detailed-review.html').write_text(page,encoding='utf-8')
assert len(sections)==7
print(json.dumps({'articles':len(sections),'file':str(out/'peter-detailed-review.html'),'source_bodies_unchanged':True},ensure_ascii=False))

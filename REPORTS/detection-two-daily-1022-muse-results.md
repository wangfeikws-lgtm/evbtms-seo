# 两篇当日稿 AI 检测结果（Muse 实测，2026-10-22）

派工：`REPORTS/dispatch-muse-detect-two-daily-articles-2026-10-22.md`。检测对象为 detection-1022/ 内定稿 txt 全文，一次粘贴、不截段、不改字、每工具每篇只测一次。

| 文章 | 输入 | ZeroGPT | GPTZero（仅参考） |
|---|---|---|---|
| BTMS《BTMS Condenser Airflow: An Installation Review Checklist》 | 4,885 字符 / 707 词，sha256 前缀 47d674125a5f287c | **69%**，判定文案 "Your Text is AI/GPT Generated" ❌ 未过线 | "We are highly confident this text was AI generated"；AI 100% / Mixed 0% / Human 0% |
| HVCH《HVCH Not Starting? Check Low-Voltage Supply and Wake-Up》 | 5,106 字符 / 755 词，sha256 前缀 16fb0185dd4b82e3 | **62.6%**，判定文案 "Your Text is AI/GPT Generated" ❌ 未过线 | 补测中（结果后补） |

## 结论（Muse）

- 判定线 ZeroGPT ≤30%：**两篇均未过线**，按门禁不得交付发布。
- 原因与既有实证一致：两篇都是纯流程/清单型稿件，全文无 EVLINK 实测数据、无具体参数演算、无厂家第一人称取舍判断——正是 2026-10-21/22 反复验证过的"无真实数据则高分"模式（同类稿此前三版约 80%）。
- Codex 稿件本身的事实边界是干净的（未编造数据），问题纯粹在文本形态。
- 处理选项（待 Peter 定）：①搁置，等有真实工况数据再织入重写；②Muse 按全文重组法（换切入点、判断前置、节奏打散）试改，改完复测，过线才交。GPTZero 按既定口径仅作参考，不作判定。

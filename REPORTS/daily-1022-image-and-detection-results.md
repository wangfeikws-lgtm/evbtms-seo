# DAILY-1022 特色图与检测状态

负责人：Codex。日期2026-10-22。图片已交付；检测未完成，不可发布。

## 实际图片交付

| 稿件 | 仓库文件 | 尺寸/大小 | Alt |
|---|---|---|---|
| BTMS冷凝器气流 | REPORTS/assets/daily-2026-10-22/btms-condenser-airflow-feature.webp | 1199×675 / 55,286 bytes | EVLINK BTMS product visual with conceptual airflow arrows and an electric truck illustration |
| HVCH低压与唤醒 | REPORTS/assets/daily-2026-10-22/hvch-start-up-review-feature.webp | 1199×675 / 61,158 bytes | EVLINK coolant heater product visual with supply, wake-up and enable review icons |

- 原尺寸PNG同目录保留。采用内置image_gen编辑/合成，后做WebP格式压缩。
- 参考素材分别来自既有system-images/product-btms-source-6087.jpg和outputs/EVLINK-HVCH-All-Models-Native-V4/assets/evlink-hvch-b1.jpg。它们是既有产品视觉素材，不能声称都是实拍照片。
- 已目视核对三风扇柜体、加热器主要结构及英文标题。背景车辆和箭头仅为通用应用示意；不是客户车辆、真实工厂、测试证据或接线图。
- 图片内明确标注Not test data / Not a wiring diagram；不得以BTMS箭头确定真实机型风向。
- 提示词摘要：沿用参考产品外观；白/浅蓝底、品牌蓝绿；BTMS CONDENSER AIRFLOW / Review the Installed Air Path；HVCH START-UP REVIEW / Supply • Wake-Up • Enable；无性能数字、认证及客户声明。工具：内置image_gen，非CLI。

## 检测准确状态

- 本轮新建ZeroGPT浏览器操作超时，未提交全文、未取得结果。ZeroGPT、GPTZero均为NOT TESTED，不写0%、不借用旧稿分数。
- 两个固定检测文本已导出到REPORTS/detection-1022/，不含内部交付备注和SEO字段，包含正文标题、内容、列表和链接锚文本。
- BTMS文本SHA256：47D674125A5F287C3E357E8E79811FD95ED125902256CB950CBF87582B983769。
- HVCH文本SHA256：16FB0185DD4B82E3D96DBF96F30B9A0925AC3C29DDCD2F29392F6F829F50F6D6。
- 分数必须对应上述全文版本；改字后重导出、重测。检测分数不等于作者占比、技术正确或SEO效果。

## 给Muse的最小补测执行包（待领取）

使用现有可控浏览器，分别将上述两个txt全文提交ZeroGPT及GPTZero。不得只测首段或删掉高分段。回填工具、时间、字数、实际分数、报告URL/截图及文本SHA256。ZeroGPT要求<=30%，GPTZero参考；若未达标回传具体结果，Codex继续修订。不得使用付费额度、购买订阅或绕过验证码；若有此依赖明确记录。此单是检测协作请求，不代表Muse已经接受或检测通过。

## 仍然未闭环

实际检测、完整站内去重及目标国家SERP。两篇是已交正文和配图，不是全部门禁通过。若BTMS已有气流选题，先合并既有稿，不另建重复页面。正式发布由Peter审核。

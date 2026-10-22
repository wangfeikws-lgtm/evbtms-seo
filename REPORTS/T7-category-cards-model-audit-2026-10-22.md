# T7 余项①：HVCH 分类页 20 张产品卡——真实型号对应表（待 Peter 确认）

- 页面：https://evbtms.com/products/high-voltage-coolant-heater/
- 实抓日期：2026-10-22（页面 HTML 按 DOM 结构逐卡解析：每卡＝图片＋H3 标题＋链接）
- **更正（2026-10-22 17:05）**：第一版表格误报 7 张卡"无链接"——解析方式有误。复核结论：**20 张卡全部有链接**，其中 7 张指向站内其他路径的系列页（B2/E/Z/H2/H/B4），第一版按路径前缀过滤时漏掉了。图片归属也已按 DOM 顺序修正。

## 现状

- 20 张卡标题只有 3 种且大面积重复："800v 35kw"×8、"600v 30kw"×4、"400v 24kw"×8。
- 链接指向共 12 个型号页，其中 7 个型号页各被 2 张卡共用（多为一张 800V 卡＋一张 600V/400V 卡，疑似同型号不同电压平台版本）——请 Peter 确认是否如此。
- 卡 5 与卡 17 共用同一张图片（画板-1-6.jpg）。

## 对应表（按页面顺序）

| 卡号 | 现在标题 | 卡片链接指向（型号页） | 卡片图片 | 真实型号＋功率/电压（Peter 填） |
|---|---|---|---|---|
| 1 | 800v 35kw | /products/high-voltage-coolant-heater/ev-high-voltage-heating-q-3/ | 画板-1-5.jpg | |
| 2 | 800v 35kw | /products/high-voltage-coolant-heater/qseries/ | 画板-1-2.jpg | |
| 3 | 800v 35kw | /products/high-voltage-coolant-heater/q-series-3/ | 画板-1-3.jpg | |
| 4 | 800v 35kw | /products/high-voltage-coolant-heater/ev-high-voltage-heating-q-4/ | 画板-1-4.jpg | |
| 5 | 800v 35kw | /products/high-voltage-coolant-heater/a5-series/ | 画板-1-6.jpg | |
| 6 | 800v 35kw | /b2-series-high-voltage-coolant-heater/ | 画板-1-8.jpg | |
| 7 | 800v 35kw | /e-series-high-voltage-coolant-heater/ | 画板-1-9.jpg | |
| 8 | 800v 35kw | /z-series-high-voltage-coolant-heater-2/ | 画板-1-10.jpg | |
| 9 | 600v 30kw | /products/high-voltage-coolant-heater/ev-high-voltage-heating-q-3/ | 画板-2-3.jpg | |
| 10 | 600v 30kw | /products/high-voltage-coolant-heater/q-series-3/ | 画板-2-5.jpg | |
| 11 | 600v 30kw | /products/high-voltage-coolant-heater/ev-high-voltage-heating-q-4/ | 画板-2-6.jpg | |
| 12 | 600v 30kw | /products/high-voltage-coolant-heater/qseries/ | 画板-2-13.jpg | |
| 13 | 400v 24kw | /products/high-voltage-coolant-heater/a3-series/ | 画板-1-11.jpg | |
| 14 | 400v 24kw | /h2-series-high-voltage-coolant-heater/ | 画板-1-14.jpg | |
| 15 | 400v 24kw | /h-series-high-voltage-coolant-heater/ | 画板-1-17.jpg | |
| 16 | 400v 24kw | /products/high-voltage-coolant-heater/a4-series/ | 画板-1-18.jpg | |
| 17 | 400v 24kw | /products/high-voltage-coolant-heater/a5-series/ | 画板-1-6.jpg（与卡 5 同图） | |
| 18 | 400v 24kw | /b4-series-high-voltage-coolant-heater/ | 画板-1-19.jpg | |
| 19 | 400v 24kw | /b2-series-high-voltage-coolant-heater/ | 画板-1-21.jpg | |
| 20 | 400v 24kw | /products/high-voltage-coolant-heater/a3-series/ | 画板-1-23.jpg | |

## 共用同一型号页的卡（请重点确认是否为同型号不同电压版本）

- Q-3 页：卡 1（800v 35kw）、卡 9（600v 30kw）
- qseries 页：卡 2（800v 35kw）、卡 12（600v 30kw）
- q-series-3 页：卡 3（800v 35kw）、卡 10（600v 30kw）
- Q-4 页：卡 4（800v 35kw）、卡 11（600v 30kw）
- A5 页：卡 5（800v 35kw）、卡 17（400v 24kw）
- B2 页：卡 6（800v 35kw）、卡 19（400v 24kw）
- A3 页：卡 13（400v 24kw）、卡 20（400v 24kw）

## 已知官方系列口径（供对照，不要据此猜卡片归属）

- A 系列：6–18kW / 400–800V（a3-series 页）
- Q 系列：15–35kW / 400–1100V（q-3 页为 15–35kW）
- E 系列：20–24kW / 400–800V
- H 系列：5–14kW / 400–1000V

## 填写方式

直接在本表最后一列填，或在主聊按"卡3＝XX型号，35kW/800V"的格式逐条回复即可。若某张卡本身就是重复卡、应该删掉，也请注明"卡X 删除"。Muse 拿到确认后逐卡改成唯一型号标题。

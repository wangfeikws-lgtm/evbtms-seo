# 五条产品线询盘入口执行包（草案，未改生产）

目标：客户知道下一步该提供什么，但不因为不知道工程数据而无法提交。只要求联系人及有效回邮渠道；技术字段允许“not yet defined”，不要把整张工程表变成必填表。

## 公开表单实况

- 本轮公开Contact HTML中Phone/WhatsApp的numeric_field已是type=tel，而非number；该历史整改不再重复派发。字段名numeric_field是历史内部名，本轮不建议为了美观改名。
- 页源码含两个fluentform_1实例，可能来自正文和弹窗；不能仅凭源码说有两个可见表单或认定提交失败。请现有执行者在桌面/390px验证各自按钮与标签关联。
- 本轮不提交表单、不读后台询盘、不发送邮件。历史收件证明不等于本轮端到端验收。

## 1 BTMS产品页

位置建议：型号比较与选型说明之后、最终CTA处。先由当前页面执行者对照实况，避免重复模块。

**Heading:** Find the BTMS Configuration for Your Vehicle

**Copy:** Tell us your vehicle type, battery heat load or available pack data, voltage range and expected ambient conditions. If an input is not yet defined, mark it as unknown. Include cooling and heating requirements separately so we can review the configuration rather than just the headline kilowatt rating.

**Button:** Request a BTMS Selection Review

**Target:** https://evbtms.com/contact/

可复制到Message的模板：
Vehicle / application:
Battery heat load or pack information (if available):
Cooling duty / heating duty:
Minimum–maximum supply voltage:
Coolant and flow requirements (if known):
Ambient conditions and operating cycle:
Available drawing or project document:

## 2 HVCH产品页

**Heading:** Match the Heater to the Duty and Interface

**Copy:** Send the requested heating duty, minimum and maximum vehicle voltage, available coolant data and required control method. CAN control, thermostat control and enable inputs are model-specific; we will identify the information needed to review a suitable variant.

**Button:** Discuss a Coolant Heater Specification

**Target:** https://evbtms.com/contact/

模板：Heating purpose (battery / cabin / other); target output; voltage range; initial/target coolant temperature; flow (if known); required control interface; installation drawing.

## 3 矿卡方案页

**Heading:** Define the Truck Duty Before Selecting Components

**Copy:** Share the truck type and gross vehicle mass, battery and voltage information, route duty and operating environment. For braking and thermal review, include descent duration, charging conditions and the cooling or heating functions required. Customer names and confidential drawings are not required for an initial discussion.

**Button:** Discuss a Mining Truck Thermal Project

**Target:** https://evbtms.com/contact/

模板：Truck type/payload; battery capacity and voltage; grade/descent/braking duty; charging power; ambient/altitude; dust/vibration/protection needs; cooling/heating/CAN needs.

## 4 三合一控制器

**Heading:** Check the System Boundary Before Combining Controllers

**Copy:** Describe the compressor, heater and refrigeration-control functions in your project. Include the battery voltage window, low-voltage supply, communication requirements and installation environment. A three-in-one architecture is a configuration decision, not an automatic guarantee of cost or energy savings.

**Button:** Review Controller Integration

**Target:** https://evbtms.com/contact/

模板：Functions to combine; compressor and PTC loads; HV minimum/maximum; LV supply; CAN ownership; mounting/airflow; existing block diagram.

## 5 制动电阻产品页（交Muse统筹，不直接改）

**Heading:** Send the Electrical and Downhill Duty

**Copy:** Provide the DC-bus voltage range, chopper limits, vehicle duty and available cooling conditions. Include braking duration and repetition where possible. We will review the required inputs before discussing a product configuration.

**Button:** Request a Braking Resistor Review

**Target:** https://evbtms.com/contact/

模板：DC bus min/max; chopper limits; truck gross mass and route; braking duration/repetition; available coolant conditions; applicable environment; drawing if shareable.

## 后台与验收要求

1. 与Muse的T13施工包去重；只采用用户批准且当前页面缺失的模块，不另加重复长表。
2. 保留原Contact表单动作和字段映射，不改邮箱、SMTP、插件或站点设置。
3. 按钮可用普通链接；如果以后要预填产品线或追踪来源，应先在现有表单安全支持范围内实现，不伪造GA4已配置。
4. 390px核对CTA可点、标签清楚、电话支持+和空格；键盘能访问提交按钮。
5. 真正端到端通过仍需“前台提交成功→后台条目→邮件通知”，测试需明确标QA且避免重复轰炸收件箱。

当前交付是可直接施工的英文文案与检查方法，不是已经生产上线或提升转化率的证据。

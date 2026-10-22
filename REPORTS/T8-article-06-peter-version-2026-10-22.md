# Sizing Mistakes That Kill Braking Resistors（T8-6，Peter 发布版全文 2026-10-22）

**URL slug:** /braking-resistor-sizing-mistakes/
**SEO Title:** Sizing Mistakes That Kill Braking Resistors | EVLINK
**Meta Description:** Most braking resistors die from missed conditions, not bad math: voltage window, derating, coolant flow. Six sizing mistakes we see on EVs, and the fixes.
**目标关键词:** braking resistor sizing mistakes
**Category:** Guide
**版本说明:** 正文为 Peter 2026-10-22 提供的发布版（他本人内容，Muse 仅统一标题编号、补内链、清单分条、清理公式记法）；取代 Muse 底稿 T8-article-06-sizing-mistakes.md 用于发布。

---

When braking resistors were returned due to damage, we dismantled them for inspection; we had initially assumed this was due to a calculation error, but we often found that the calculations themselves were correct. The application of the formula U²/P was entirely correct (we have described this method in detail in our [Resistor Calculation Guide](/braking-resistor-resistance-calculation/)), and the resistance values were also accurate. What actually caused the equipment to fail were the unrecorded actual operating conditions: the duration of the downhill run was longer than that reported to the supplier; the actual flow rate in the cooling circuit was only half that specified in the design drawings; and, in hot weather and at high altitude, the DC bus voltage remained consistently at the upper limit of the permissible range.

In almost all the failure cases we have analysed, the situation has been broadly similar. The selection of braking resistors involves two calculations and approximately six assumptions. The calculation methods are explained in detail in our comprehensive selection guide; this article focuses on these assumptions—it is precisely these that, unbeknownst to us, render otherwise correct calculations ineffective.

Before listing these issues, one further point requires clarification: errors of this kind rarely occur in isolation; when considered individually during the design review stage, any one of them may appear harmless. For example, if a resistor with a matching rated voltage is selected (and no derating is applied), and the cooling circuit flow rate is only 80 per cent of the requirement, it will indeed still perform the braking function, but its thermal margin will be almost entirely exhausted. Subsequently, should hot weather, longer downhill sections, or air locks in the system following a coolant change occur, these minor errors will compound. The result is that equipment which could have passed a year of testing suffers complete failure in less than a week of actual operation.

## Mistake 1: Directly applying variable frequency drive (VFD) selection tables to configure braking resistors for electric vehicles

Selection tables for industrial variable frequency drives (VFDs) are typically based on operating conditions characterised by 'short braking periods and long periods of inactivity'—that is, a duty cycle of 10% to 40%, ambient room temperature, and a cabinet installation environment with ample space around the resistors. However, when electric lorries are travelling in mountainous terrain, they may be subject to continuous braking under full load for up to 20 minutes. Although these resistors belong to the same series, their thermal life performance differs significantly.

If selection is based directly on the VFD product catalogue, the load model itself is already incorrect before any values are even entered. The equipment may pass bench testing and commissioning, but will age rapidly during actual operation, eventually failing on sections of the route for which it is fundamentally unsuitable. The correct approach is to base the selection on the most demanding continuous braking section of the actual route, using the selection tables in the product catalogue merely as a supplementary reference—and under no circumstances should they be regarded as the sole basis for selection. We have explained the relevant load cycle calculation methods in detail in our article on [How Load Cycles Determine the Size of Braking Resistors](/duty-cycle-braking-resistor-sizing/). The error here is actually simpler: people have completely overlooked this issue.

## Mistake 2: Selecting resistance values based on nominal voltage

The DC bus voltage in commercial electric vehicles is not a fixed value, but rather a voltage range. On a 450–850 V voltage platform, the power dissipated by the same resistor at the upper limit of the voltage range is approximately 3.6 times that at the lower limit—this is because power is proportional to the square of the voltage (P = U²/R). Selecting a resistor based solely on the nominal voltage of 650 V leads to two problems: at high states of charge (SOC), the chopping current and resistor power will exceed the expected design values; whilst at lower voltages, braking power will be insufficient, forcing the controller to rely more heavily on friction braking, and during aggressive energy recovery (regenerative braking), the DC bus voltage may still surge, triggering overvoltage protection.

It is therefore essential to consider both ends of the voltage range, rather than focusing solely on the midpoint. We provide detailed guidance on [how to match resistor values to the DC bus voltage](/matching-braking-resistor-resistance-dc-bus-voltage/), which also explains why the lower limit of the resistor value is typically determined by the chopper (rather than the resistor itself).

## Mistake 3: Ignoring that resistance is a 'dynamic parameter'

Our [HVH-R1402](/products/braking-resistor/) model has a nominal resistance of 2.24 Ω, but this figure is subject to two conditions that are often overlooked by buyers: it is the resistance at 25°C in a cold state, and it is subject to a tolerance range of ±10 per cent. When a resistor is heated, its resistance value drifts; furthermore, the tolerance range means that two devices with exactly the same nominal value may exhibit significant differences in their actual resistance values.

If calculations are based solely on 2.24 Ω, then on a cold winter's morning, a resistor in a cold state with a lower resistance value may generate a chopping current that exceeds your set protection threshold. At best, this will result in a false trip; at worst, it will subject the braking chopper to excessive stress, potentially causing the chopper to fail before the resistor itself. The solution requires no additional cost: calculate the chopping current when the resistance is at its minimum (cold state, nominal value minus tolerance), and calculate the braking power when the resistance is at its maximum (hot state). All it takes is adding two extra rows of calculations to your spreadsheet.

## Mistake 4: Ignoring ambient temperature and altitude

Product ratings are specified under specific test conditions, whereas the actual operating environment of a vehicle differs. For example, a resistor installed beneath a lorry chassis at an ambient temperature of 40°C, or one operating at an altitude of 3,000 metres (where thin air reduces heat dissipation capacity), will have already consumed part of its thermal margin before braking has even commenced. Air-cooled units are particularly affected; liquid-cooled units also suffer a loss of thermal margin—if the coolant is already at a high temperature after passing through the battery circuit during a high-load climb, its cooling efficiency will be significantly reduced.

In practical applications, the problem often manifests in the same way: on the hottest and highest-altitude sections of the route—precisely where braking is most needed—the resistor triggers protection due to overheating. It is therefore essential to derate the design based on the most severe ambient temperatures and altitudes likely to be encountered along the route, and to confirm with the supplier the assumptions on which their rated parameters are based. The rated parameters of the HVH-R1402 are valid for an ambient temperature range of –40 °C to +85 °C. Regardless of which product is procured, the supplier should be required to specify in writing the assumptions on which their rated parameters are based.

## Mistake 5: Insufficient cooling circuit flow

The performance of liquid-cooled resistors depends to a large extent on the cooling circuit system that supplies them. For the HVH-R1402 to maintain a continuous power output of 140 kW for 20 minutes, the coolant flow rate at its DN32 connection must be at least 172 L/min. We have encountered installation cases where the use of a shared pump, excessively long hose runs and two sharp bends resulted in an actual flow rate of only around half the required value. At the time, the problem was attributed to the heater (resistance element), but in fact the heater was not at fault. Even after maintenance of the cooling system, residual air locks (air pockets) in the pipework can silently cause the same damage, and such issues are often even more difficult to detect. Furthermore, confusion between the concepts of 'peak power' and 'continuous power' frequently leads to such misjudgements: as we have clearly stated in our guide on [Continuous Power and Peak Power](/continuous-vs-peak-power-braking-resistor/), the 20-minute rated power actually defines the cooling capacity, rather than imposing a performance limit on the heating element itself.

Please ensure that, once the vehicle has been fully assembled, you measure the actual flow rate directly at the heater connection point, rather than relying solely on the nominal parameters stated on the water pump nameplate. The pipework must be bled after every cooling system maintenance operation. If the measured flow rate fails to meet requirements, please first inspect and optimise the pipework system; do not blindly attribute the fault to the heater.

## Pre-purchase checklist

Before signing the order, please confirm the following six items:

- The most demanding continuous downhill section on the route: length of the descent, gradient, gross vehicle weight, and vehicle speed upon entering the descent
- Busbar voltage range (minimum and maximum values, not the nominal value)
- Chopping current (calculated at the lowest resistance value) and braking power (calculated at the maximum value)
- Derating calculations for the most severe ambient temperatures and altitudes
- Actual measured coolant flow rate at the resistor interface under real-vehicle conditions
- NTC temperature sensors and high-voltage interlock devices have been wired and functionally tested

Please send us these six pieces of data, and we will calculate the appropriate model selection for you.

If you have completed this checklist, please send it to us. Before you place your formal order, we will carry out the selection calculation for you. If the calculation results match our HVH-R1402 model (2.24 Ω, 450–850 V DC, 140 kW continuous power for 20 minutes, IP6K9K protection rating, and having passed 25 validation tests), we can arrange production for you (minimum order quantity of 10 units, with a lead time of one week). Should the calculation results indicate other specifications, we will inform you accordingly to ensure that your final selection does not result in damage to the resistors.

## Frequently Asked Questions

### What is the most common mistake made when selecting braking resistors for electric truck applications?

Directly applying selection tables designed for industrial variable frequency drives (VFDs). Such tables are typically based on the operating assumption of 'short braking periods with long cooling intervals'. However, during a downhill descent lasting up to 20 minutes, a heavy goods vehicle is actually operating under a duty cycle of nearly 100 per cent. Consequently, if resistors are selected based on selection tables designed for a 10 per cent–40 per cent duty cycle, even if their resistance values and peak power ratings appear to meet the requirements, their thermal capacity will be severely inadequate—this often results in the equipment appearing to function normally during commissioning but failing during actual operation.

### Can a resistor still fail even if the resistance value is entirely correct?

Yes, and this is precisely the cause of most failures. Whilst the resistance value determines the peak power and chopping current, resistor failure often stems from thermal management issues: for example, underestimating the duty cycle, insufficient coolant flow, failure to account for derating due to ambient temperature and altitude, or a missing temperature sensor preventing early warning. If the resistance value is correct but the cooling conditions are inadequate, the resistor will still fail; it will simply take longer for the failure to occur.

### What information do you need to provide if you require us to calculate the selection of braking resistors?

A total of six items are required: the DC bus voltage range (minimum and maximum values); the most severe downhill operating conditions (including vehicle mass, gradient, slope length and speed upon entering the slope); the duration of braking on that downhill section; the coolant flow rate your cooling circuit can provide at the resistor; and the most extreme ambient temperatures and altitudes likely to be encountered on that route. Once we have this data, we can calculate the resistance value, continuous power rating and cooling margin, and inform you clearly whether our products are suitable.

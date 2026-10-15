# T8 文章 #1：How to Size a Braking Resistor for an Electric Bus or Truck

- Slug 建议：`how-to-size-braking-resistor-electric-bus-truck`
- SEO Title：How to Size a Braking Resistor for an Electric Bus or Truck | EVLINK
- Meta：Size a braking resistor in three steps: continuous power from weight, grade and speed; resistance matched to your DC bus voltage; duty cycle checked against cooling. Worked example included.
- 配图：
  - Hero：`T8-article-01-assets/media-generation-t8-article01-hero-downhill-tru-0-9e191675-71d1-411c-9816-47f86f7abe04.webp`（Alt：Electric heavy truck descending a long mountain grade at dusk）
  - 剖视：`T8-article-01-assets/media-generation-t8-article01-coolant-loop-cuta-0-882f0a23-8654-4356-b521-b7bf31703d51.webp`（Alt：Cutaway of electric truck chassis showing liquid-cooled braking resistor in the coolant loop）
- 内链：制动电阻产品页 https://evbtms.com/products/braking-resistor/
- 状态：Muse 正文 v1，待 Peter 过目

---

Sizing a braking resistor comes down to three numbers. Get them right and the resistor disappears into the vehicle, doing its job for years. Get one wrong and you find out on a mountain grade, which is the worst possible classroom.

We build liquid-cooled braking resistors for electric commercial vehicles, and we size them with customers every week. Here is the method we actually use.

## Step 1: Continuous braking power

Forget peak power for a moment. The number that sizes the resistor is the power it must dissipate continuously, for the whole descent, not the first ten seconds.

The physics is simple:

**P = m × g × v × grade**

Take an 18-tonne bus holding 30 km/h on a 7% grade:

18,000 kg × 9.81 × 8.33 m/s × 0.07 ≈ 103 kW

That is roughly 100 kW the resistor must turn into heat, nonstop, for as long as the grade lasts. If the descent runs 15 minutes, the resistor sees 100 kW for 15 minutes. There is no averaging it away.

This is where most undersized resistors come from. Someone sizes for the motor's peak regen rating, or for a 60-second stop, and the unit that looked fine on paper overheats twenty minutes into a real descent. Size for the grade, not the brochure.

Our HVH-R1402 series is built around exactly this case: 140 kW continuous for 20 minutes. That covers a fully loaded bus or medium truck on a serious grade with margin left over.

## Step 2: Resistance matched to your bus voltage

Once you know the power, the resistance follows from the DC bus voltage:

**R = U² / P**

At 750 V DC and 103 kW, that gives about 5.5 Ω. In practice you pick a standard winding near the calculated value, then verify the current stays within the chopper and the resistor's limits.

Two things we insist on here. First, resistance is wound to order. There is no universal value, because bus voltages across platforms run from 450 V to 850 V and beyond. Anyone selling you a fixed catalog value without asking your bus voltage is guessing. Second, always check the result against the minimum resistance your brake chopper allows. Too low a resistance draws too much current and the chopper's switching device pays for it.

Our standard winding is 2.24 Ω for 450–850 V DC systems (1000 V DC maximum). Other bus voltages get their own winding on the same platform.

## Step 3: Duty cycle and cooling

Power and resistance tell you the electrical size. Duty cycle tells you the thermal size.

How long is the longest descent, and how much rest does the resistor get between braking events? A city bus doing stop-start all day has a completely different thermal profile from a mining truck crawling down a ramp for forty minutes. The resistor's continuous rating must cover your worst real cycle, not an average day.

Then cooling. A liquid-cooled resistor dumps heat into the vehicle's coolant loop, typically 50% water and 50% glycol. That only works if the loop can carry the heat away. Check the coolant flow and the temperature the loop runs at under load. On our units the interface is DN32, and the design assumes the vehicle's thermal system does its share. If your platform has no proper coolant loop, say so early. An air-cooled unit on a small vehicle is a more honest answer than a liquid-cooled unit with nowhere to send the heat.

## Putting it together: a mountain grade walkthrough

Picture the scenario. A 25-tonne electric truck crests a pass at 90% state of charge and starts down a 12 km, 6% grade. Regen kicks in, the battery fills within minutes, and the battery management system cuts regen to protect the pack. From here down, the braking resistor carries the load the friction brakes cannot safely hold alone.

Run the three steps. Continuous power: 25,000 × 9.81 × 8.33 × 0.06 ≈ 123 kW. Resistance at 800 V bus: 800² / 123,000 ≈ 5.2 Ω, wound to order. Duty: the full descent, roughly 25 minutes at 30 km/h, so the resistor needs a genuine continuous rating past 120 kW, with temperature sensing watching the whole way. Our 140 kW / 20-minute unit fits with margin; a longer or steeper grade would push toward a larger frame or a project-specific winding.

That is the whole method. Three numbers, one honest worst case.

## Where the resistor lives in the vehicle

The resistor is not a standalone box bolted wherever it fits. On a liquid-cooled design it sits in the coolant loop alongside the battery and drive system, with its own temperature sensor and an interlock loop back to the vehicle controller. If the sensor reads too hot or the interlock opens, the system knows before the driver does.

We ship every unit with NTC temperature sensing and an HVIL interlock as standard. A resistor without them is a liability, not a product. When you evaluate any supplier, ask whether those are included or optional. The answer tells you a lot.

## The mistakes we see most

Three, in order of frequency. Sizing for peak power instead of continuous, which we covered. Forgetting how long the descent actually is, which is a duty cycle error. And leaving out temperature sensing and interlock to save cost, which is the one that keeps service managers up at night.

There is a fourth, quieter one: matching the resistor to the motor instead of the vehicle. The motor's regen rating is not the sizing input. The grade is.

## When a braking resistor is the wrong answer

Not every vehicle needs one. A light delivery van running flat city routes will rarely fill its battery on regen, and the friction brakes handle the rest. Adding a resistor there is weight and cost for no benefit. Short, mild grades with plenty of battery headroom are fine without it too.

The honest test: does your route include descents long enough and steep enough that regen alone cannot hold speed once the battery is full? If yes, size the resistor. If no, spend the money elsewhere.

## What to send us

If you want us to check the sizing, send four things: vehicle weight, typical grade and speed, bus voltage, and your longest descent. Our engineers will run the numbers and come back with a resistance value and a configuration. No obligation, and we will tell you if you do not need one.

[CTA: 询盘表单 — Send us your vehicle weight, typical grade and speed, and bus voltage.]

## FAQ

**Can I use one resistor across different bus voltages?**
Only within its rated range. Resistance is wound for a voltage band. Our standard covers 450–850 V DC; outside that, the winding changes.

**What happens if the resistor is undersized?**
It overheats on long descents. Temperature sensing will derate or cut it, and the driver falls back to friction brakes on exactly the grade where they fade fastest.

**Does the chopper come with the resistor?**
Three options: resistor only, resistor plus a CAN-coordinated chopper controller, or a fully integrated chopper-brake unit. Chopper parameters are confirmed per project.

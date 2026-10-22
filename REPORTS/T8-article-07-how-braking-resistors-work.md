# How Braking Resistors Work in Electric Vehicles

**建议 URL slug:** /how-braking-resistors-work-electric-vehicles/
**SEO Title:** How Braking Resistors Work in Electric Vehicles | EVLINK
**Meta Description:** Regenerative braking has a limit: a full battery cannot take the energy back. Here is how a braking resistor works in an EV, step by step, with real numbers.
**目标关键词:** how braking resistors work in electric vehicles
**Category:** Guide

---

The question usually lands in our inbox about two weeks into a project: "We already have regenerative braking. Why is there a resistor on the BOM?"

Fair question. Regenerative braking is real, and on flat ground it does most of the work. But regen is a battery charging event, and a battery is not a hole you can pour unlimited energy into. There are three situations where the battery simply cannot take the energy back. The battery is full, and a full lithium pack accepts charge at close to zero rate. The descent is too long, so the energy arrives faster and longer than the pack's charge limit allows. Or the battery is faulted, cold, or derated, and the vehicle still has to slow down. In all three, the kinetic energy has nowhere to go. That is the gap the braking resistor fills.

## Step 1: The energy starts as mass and height

Braking energy is not an electrical quantity at first. It is a heavy vehicle at the top of a slope. The power involved is larger than most people expect.

Take a 40-tonne electric mining truck descending a 10% grade at 30 km/h. Gravity alone feeds power into the drivetrain at roughly m·g·v·sin(θ), which works out to about 325 kW, continuously, for as long as the grade lasts. A loaded 18-tonne city bus on an 8% grade at 40 km/h sees around 156 kW. Neither number cares what is written on a motor datasheet. The hill sets the power. Everything downstream of the wheels has to absorb it, convert it, or store it.

## Step 2: The traction motor turns into a generator

On the way down, the traction motor stops consuming power and starts producing it. The inverter controls the motor torque in the opposite direction: the wheels drive the motor, the motor generates AC, and the vehicle's speed is held by electromagnetic torque instead of brake pads.

This is the part every VFD textbook describes, and it works the same way in an industrial drive. What differs on a vehicle is scale and duration. A factory drive brakes a load for seconds. A truck on a mountain route brakes for twenty minutes at a stretch, and the energy keeps coming.

## Step 3: Energy arrives at the DC bus as current

The inverter rectifies the generated power onto the DC link. On the commercial EV platforms we work with, that bus lives somewhere in a 450–850 V window. If nothing draws the regenerated current away, bus voltage climbs. Left alone, it climbs until the inverter trips on overvoltage, and at that moment the vehicle loses electric braking entirely and falls back on friction brakes alone. Nobody wants that discovery at the top of a grade.

So the energy needs a load. The first choice is always the battery. Charge it, recover the energy, use it on the next climb. That is the efficient path, and the vehicle takes it whenever the battery can accept charge.

## Step 4: When the battery says no, the chopper opens

Here is where the braking resistor earns its place. The brake chopper is a power switch (an IGBT in most designs) sitting between the DC bus and the resistor. The controller watches bus voltage. When the battery cannot absorb the regenerated current and the bus voltage crosses a set threshold, the chopper starts switching the resistor across the bus in PWM pulses. More braking energy needed, longer pulses. Less needed, shorter pulses. The resistor becomes a controllable electrical load that the battery refused to be.

The physics at the resistor is plain Joule heating. Current through a resistance makes heat, at P = U²/R. Our HVH-R1402 is 2.24 Ω (cold, at 25°C, ±10%), so the numbers across the bus window look like this: at 850 V it draws about 379 A and converts roughly 322 kW; at 450 V it draws about 201 A and converts roughly 90 kW. The chopper's PWM duty cycle trims the average between those limits to whatever the descent actually demands.

One point the engineers argue about on forums, and they are right: the resistor itself controls nothing. It does not limit current in any smart sense. It sets the rate at which energy leaves the bus, given the voltage. The chopper and its controller do the thinking. The resistor does the absorbing, and it has to absorb at full rate for as long as the hill lasts.

## Step 5: The heat has to go somewhere

Converting electricity to heat is the easy half of the job. Getting rid of the heat is the hard half, and it is where EV braking resistors split from their industrial ancestors.

Run 140 kW for 20 minutes and you have produced 168 MJ of heat, about 46.7 kWh of energy. An air-cooled resistor under a truck floor cannot shed that in still, hot, dirty air. So on a vehicle like this, the resistor is liquid-cooled and plumbed into the vehicle's coolant circuit. The HVH-R1402 moves its heat into coolant through a DN32 interface, and holding the full 140 kW for the full 20 minutes requires at least 172 L/min of flow at the resistor ports.

From the coolant loop, the heat has two useful exits. The radiator rejects it to the air, which is the normal case. Or, on a cold morning, the warm coolant can be routed toward battery heating or cabin heat, so braking energy does a second job before it is thrown away. Heat recovery has its own design questions and we gave it its own article in this series. The point for this one: the resistor is not a bolt-on box. It is a node in the vehicle's thermal system.

## The safety loop wrapped around it

Two signals keep the whole arrangement honest. An NTC sensor inside the unit reports element temperature to the vehicle controller, so the vehicle can derate braking or blend in friction brakes before anything overheats. A high-voltage interlock loop confirms the HV connectors are fully seated; if a connector is disturbed, the vehicle knows before the chopper energizes the resistor. The resistor may be a simple device electrically, but on a vehicle it works inside a supervised loop, and it should. We covered sizing errors in detail in our [sizing mistakes guide](/braking-resistor-sizing-mistakes/), and forgetting to wire these two signals is on that list for a reason.

## Where to go next

If you are specifying a system, the working sequence is: calculate the resistance for your bus window with the [U²/P method](/braking-resistor-resistance-calculation/), check it against the top and bottom of that window using our [voltage matching walk-through](/matching-braking-resistor-resistance-dc-bus-voltage/), then size the continuous rating from your worst descent as shown in the [full sizing guide](/how-to-size-braking-resistor-electric-bus-truck/). The chopper architectures behind Step 4, and why we cool with liquid instead of air, get their own articles later in this series.

Or send us the descent: vehicle mass, grade, length, entry speed, and your bus voltage window. We will run the energy numbers against the HVH-R1402 (2.24 Ω, 450–850 V DC, 140 kW continuous for 20 minutes, IP6K9K, validated across 25 tests and 9,360 durability cycles) and tell you whether it fits your route. Production starts at 10 units, lead time one week. The product details are on our [braking resistor page](/products/braking-resistor/).

---

## FAQ

**Why does an electric vehicle need a braking resistor if it has regenerative braking?**
Because regenerative braking is battery charging, and a battery cannot always accept charge. At full state of charge the acceptance rate is close to zero, on long descents the energy arrives faster than the pack can take it, and a faulted or cold battery may accept nothing at all. The resistor gives that energy a controlled path to heat so the vehicle keeps full electric braking in all three cases.

**How much power does a braking resistor actually absorb?**
Whatever the descent produces and the battery cannot take. The instantaneous ceiling is set by P = U²/R: a 2.24 Ω resistor converts about 322 kW at 850 V bus voltage and about 90 kW at 450 V, with the chopper's PWM duty cycle setting the average in between. The continuous rating is a separate, thermal limit: 140 kW for 20 minutes on the HVH-R1402, set by how fast its coolant loop can carry heat away.

**Where does the heat from a liquid-cooled braking resistor go?**
Into the vehicle's coolant circuit. From there the radiator rejects it to the outside air, or the warm coolant can be routed to battery or cabin heating in cold conditions. Either way, the heat leaves through the same cooling system that serves the rest of the vehicle, which is why the resistor needs a guaranteed flow rate (at least 172 L/min on our unit) rather than a fan and a hope.

## 内链清单（正文已埋入）

| 锚文本 | 目标 URL | 所在段落 |
|--------|----------|----------|
| sizing mistakes guide | https://evbtms.com/braking-resistor-sizing-mistakes/ | 安全环一节（T8-6） |
| U²/P method | https://evbtms.com/braking-resistor-resistance-calculation/ | 结尾（T8-2） |
| voltage matching walk-through | https://evbtms.com/matching-braking-resistor-resistance-dc-bus-voltage/ | 结尾（T8-4） |
| full sizing guide | https://evbtms.com/how-to-size-braking-resistor-electric-bus-truck/ | 结尾（T8-1） |
| braking resistor page | https://evbtms.com/products/braking-resistor/ | 结尾 CTA（产品页） |

注：SERP 简报规划的 T8-8（chopper 架构）、T8-10（液冷 vs 风冷）尚未发布，正文只留文字钩子、未加链接，待两篇发布后回填互链，避免死链。

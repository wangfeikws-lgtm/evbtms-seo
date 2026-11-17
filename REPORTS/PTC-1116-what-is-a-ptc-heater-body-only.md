# What Is a PTC Heater? How It Heats EVs Without an Engine

A PTC heater is the simplest answer to a problem every electric vehicle has: there is no engine, so there is no waste heat to warm the cabin or the battery. A PTC heater makes heat directly from the traction battery, and it regulates itself while doing it. That self-regulation is the whole point of the design, and it is what separates a PTC heater from an ordinary resistance coil.

## What PTC actually means

PTC stands for Positive Temperature Coefficient. The heating element is a ceramic material, usually barium titanate, whose electrical resistance rises as it gets hotter. Current flows through the element and makes heat.

As the element warms up, its resistance climbs, the current falls, and the heat output drops back. Past a certain temperature the resistance rises sharply, so the element effectively throttles itself.

This matters because the safety is in the material, not in a control circuit. A thermostat can fail. A controller can lose its signal. The PTC element cannot forget how it behaves: hot means high resistance, high resistance means less current.

That is why the heater is hard to overheat even if the vehicle control has a fault. It still needs the vehicle's own protection systems, and we would never sell a heater on the material alone, but the self-limiting behaviour is a real second layer that a plain resistance heater does not have.

## How it heats an EV without an engine

A petrol car gets cabin heat almost for free. The engine throws away most of its fuel energy as heat, and the cooling system carries some of that into the cabin. An EV has nothing to throw away.

The traction motor is too efficient to produce useful residual heat fast enough, and there is no exhaust. So the vehicle has to make heat on purpose, from the battery, and a PTC heater is the most direct way to do it: high-voltage DC in, heat out, no moving parts in between.

That directness is also the trade-off, and it should be stated plainly. A PTC heater converts electricity into heat at a coefficient of performance of at most 1:1. One unit of battery energy becomes one unit of heat, never more.

A heat pump can do better because it moves heat instead of making it. So a PTC heater is cheap, compact and fast, and it costs range. On a cold day the heater can draw several kilowatts continuously.

Independent winter testing cited in heat-pump comparisons puts the range loss for PTC-only vehicles at 28–54% of rated range in sub-zero conditions. That number is why buyers ask about heat pumps, and why the honest answer is that PTC is the reliable baseline, not the efficient one.

## Air heater vs coolant heater: two different jobs

PTC heaters come in two forms, and buyers mix them up more often than any other detail.

An air PTC heater sits in the HVAC duct. Cold air is blown straight across the ceramic elements and into the cabin. It is the faster of the two: warm air within seconds of switch-on, no liquid loop to warm up first.

The job is cabin comfort only. Our [high-voltage PTC air heater](https://evbtms.com/high-voltage-ptc-air-heater/) works this way.

A coolant PTC heater, the type we build as the [HVCH series](https://evbtms.com/products/high-voltage-coolant-heater/), heats a glycol loop instead of air. The heated coolant goes to the HVAC heater core for cabin heat, or to the battery pack for preheating, or both. The loop is slower to respond than direct air, but it serves two loads from one heater, and it fits vehicles that already run a liquid thermal system. Battery preheating is the job that matters most for the vehicle itself: a cold pack charges slowly and delivers less power, and warming the coolant is how the pack is brought back into its working window.

The choice is not about which is better. It is about what the vehicle already has. A vehicle with a liquid loop and a battery to preheat wants the coolant type. A vehicle that only needs fast cabin air wants the air type.

Tell us which loop the heater serves before anything else, because the answer changes the power band and the control.

## PTC vs heat pump: when each one wins

The question behind most PTC enquiries is really this one: should we use PTC at all, or a heat pump? The answer depends on the coldest day the vehicle must work through.

A heat pump wins on efficiency in mild cold. It moves heat from outside air, from the motor and inverter, sometimes from the battery, into the cabin. In mild conditions it delivers several units of heat per unit of electricity. But its output falls as the outside temperature falls, roughly below −10 to −15 °C, and at some point it cannot keep up on its own.

A PTC heater does not have that fall-off. Its output is the same at −30 °C as at 0 °C, because it makes heat rather than moving it. That is why PTC is the standard backup or primary heat source in cold-climate EVs: it is the heater that still works on the worst day.

Many vehicles run both. The heat pump carries the mild days and saves range; the PTC covers the deep cold and the fast warm-up. A buyer who only ever drives in mild winters can lean on the heat pump. A buyer whose buses must start at −25 °C cannot do without PTC.

## How we build them: three series, two kinds of control

Our high voltage coolant heaters come in three series, and the difference that matters most is not power. It is control. The A series runs 6–18 kW on 400–800 V, and the Q series runs 15–35 kW on 400–1100 V.

Both take CAN plus an enable signal, so the vehicle controller decides when the heater runs and at what output. That fits a vehicle with a thermal management controller already on the bus, because the controller can coordinate the heater with the compressor, the pump and the fan.

The E series runs 20–24 kW on 400–800 V and works on a thermostat with no CAN at all. That fits a simpler vehicle or a retrofit, where there is nothing to integrate. The H series also exists; its model names and ratings are set per project, so we do not publish a fixed band for it.

| Series | Power | Voltage | Control |
|---|---|---|---|
| A | 6–18 kW | 400–800 V | CAN + enable |
| Q | 15–35 kW | 400–1100 V | CAN + enable |
| E | 20–24 kW | 400–800 V | Thermostat, no CAN |
| H | Per project | Per project | Per project |

The mistake we see most often is ordering on power alone and discovering the vehicle expects the other control. State the control the vehicle provides. If it has a CAN bus and a thermal controller, say so. If it has neither, say that too.

The power band picks itself once the loop, the voltage range and the control are known. The voltage check is the full min/max DC range at the heater terminals, not the nominal voltage: a platform that idles at 600 V and charges at 800 V needs a heater rated for the whole span. On larger vehicles the heater also works alongside the rest of the thermal system, including our [three-in-one controller](https://evbtms.com/products/three-in-one-controller/), which manages the compressor, the refrigeration system, and the high-voltage PTC heater as one unit.

## What to tell us before you order

A PTC heater is a simple device, but a wrong one is still a wrong one. Before the first sample ships, we ask for five things: the vehicle and application; the loop the heater serves, battery preheat, cabin heat, or both; the voltage platform as a min/max range; the control the vehicle provides, CAN plus enable or thermostat; and the lowest ambient temperature the vehicle must operate in. With those five, the series picks itself. Without them, any kW figure is a guess, and guesses get found out in the first cold week.

## FAQ

**What is PTC heating?**
PTC heating is resistance heating with a ceramic element whose resistance rises as it warms. Current makes heat, the heat raises the resistance, and the higher resistance cuts the current back. The heater regulates its own output instead of relying only on an external thermostat.

**Does a PTC heater use a lot of electricity?**
Yes, relative to a heat pump. A PTC heater turns one unit of electricity into one unit of heat at best. Cabin heating on a cold day can draw several kilowatts from the traction battery, which is why PTC-only vehicles lose a noticeable share of range in winter. The cost buys reliability in deep cold and heat within seconds.

**Can a PTC heater overheat?**
The element is self-limiting: as it gets hotter its resistance rises and its current falls, so it cannot run away the way a fixed resistance coil can. That does not replace the vehicle's own protection. The heater still runs under the vehicle's control and safety systems, and the installation still has to respect the rated voltage and flow.

**Do all EVs have PTC heaters?**
No. Many newer EVs use a heat pump as the main heater and keep a PTC heater as backup for deep cold or fast warm-up. Older and budget EVs often use PTC alone. Cold-climate buses and trucks almost always carry PTC, because the heat pump alone cannot cover their worst day.

**Is a PTC heater the same as a high voltage coolant heater?**
Not quite. A high voltage coolant heater is one kind of PTC heater: the type that heats a coolant loop. An air PTC heater heats cabin air directly. Both use the same PTC principle. The coolant type also serves battery preheating, which the air type cannot do.

**Do EVs still need a PTC heater if they have a heat pump?**
Often, yes. A heat pump loses efficiency in severe cold, and below about −10°C several manufacturers keep a PTC heater as backup for fast warm-up and defrosting. Laboratory testing has shown a heat pump using more energy than a PTC heater on a cold start at −10°C, then beating it once the cabin is warm. For cold-climate fleets, the two work as a pair.

**How do I choose the right PTC heater power for a bus or truck?**
Start with voltage platform, heat load, and control interface. Our A series covers 6 to 18 kW at 400 to 800 V over CAN, Q series 15 to 35 kW at 400 to 1100 V over CAN, and E series 20 to 24 kW at 400 to 800 V with a thermostat. Our sizing guide works through flow, temperature, and power, and our selection and quotation page takes your numbers from there.

### References & Sources

1. Texas Instruments, "Design Considerations for Automotive PTC Heater Modules," SLUAAY5A, revised October 2026 — PTC operating principle, power range, and the 1:1 COP limit of resistive heating.
2. DBK Group, "PTC Heating Technology" (dbk-group.co.uk) — self-regulating ceramic behavior and fail-safe characteristics.
3. Fraunhofer IKTS, "Compact PTC heaters made of foam ceramics" — PTC ceramic properties and self-regulation.
4. AUTODOC Blog, "Heat Pump vs PTC Heater in EVs: How Much Winter Range Do You Save?" — winter range figures, including ADAC 2023 and NAF El Prix 2026 test results.
5. MDPI, "Analysis of Heating System Impacts on Battery Electric Vehicle Operation at Cold Temperatures" (2026) — laboratory comparison of heat-pump and PTC-equipped vehicles at -10°C to 25°C.
6. EVLINK product specifications: A/Q/E series parameters from EVLINK official spec pages (recon 2026-11-09); Q series laboratory validation, Shanghai University of Engineering Science.

---

*If you are sizing a heater for a real vehicle, start with our [selection guide](https://evbtms.com/high-voltage-ptc-heater-selection-guide/), the [sizing article](https://evbtms.com/high-voltage-coolant-heater-sizing-evs/), and [how a high-voltage coolant heater works](https://evbtms.com/how-high-voltage-coolant-heater-works/), or send the five items above through the [selection and quotation page](https://evbtms.com/high-voltage-coolant-heater-selection-quote/) and we will confirm the series before you order samples.*

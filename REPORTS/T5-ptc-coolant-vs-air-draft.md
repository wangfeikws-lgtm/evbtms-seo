# T5: PTC Coolant Heater vs Air Heater: Which One Does Your Electric Vehicle Actually Need (Draft 2026-10-19 rewritten)

> 状态：草稿重写 2026-10-19（原稿丢失）。待 Peter 确认措辞后发布。
> 目标词：ptc coolant heater vs air heater / electric vehicle cabin heating options
> Slug 建议：/ptc-coolant-heater-vs-air-heater/
> SEO Title: PTC Coolant Heater vs Air Heater: Which EV Heating System to Choose | EVLINK

---

Every winter, we get the same RFQ: "We need heating for our electric bus. Should we use a PTC coolant heater or a PTC air heater?"

The honest answer is that most buyers ask the wrong question. It's not coolant vs air. It's what you're trying to heat, and what else the vehicle needs hot.

## The one-line answer

If you only need warm air in the cabin, an air heater is simpler and cheaper. If you need to heat the battery too — or you want one system doing both jobs — a coolant heater is the right call. Most electric buses and trucks end up with coolant heaters, not because air heaters are bad, but because the battery needs heating anyway.

## What each one actually does

A PTC air heater is exactly what it sounds like: electric heating elements with a fan blowing cabin air across them. Air in, warm air out. It's a space heater with a CAN bus. Simple, direct, no plumbing.

A PTC coolant heater heats a liquid loop instead. The hot coolant goes where you send it — to the cabin heater core, to the battery pack, to both. It's a boiler, not a space heater. More parts, more capability.

This is the fundamental trade-off, and everything else follows from it.

## Three things that actually decide it

**1. Does the battery need heating?**

This is the question that settles most RFQs. Lithium batteries don't charge well cold, don't discharge well cold, and age faster cold. If your vehicle operates where winter mornings drop below 5°C, the battery needs active heating.

An air heater can't help the battery. It's cabin-only. So you end up buying two systems: an air heater for people, something else for the pack.

A coolant heater does both from one unit. The same hot loop that warms the cabin runs through the battery thermal plate. One heater, two jobs, one CAN address, one warranty claim path.

For electric buses running year-round in northern China, northern Europe, or Canada — the battery answer alone picks the coolant heater. We stopped quoting air heaters for bus projects years ago for this reason.

**2. How much heat, and how fast?**

Air heaters top out lower. The physics is straightforward: air carries less heat per volume than liquid, so moving the same kilowatts through air needs either much higher airflow (noisy) or much larger elements (bulky). Most PTC air heaters for vehicles sit in the 2–5 kW range. That's fine for a van cabin. It's not enough for a 12-meter bus at -20°C.

Coolant heaters scale further. Our high-voltage coolant heater line runs 15–35 kW in single units — and we've shipped 210 kW per-truck configurations (six 35 kW units in parallel) for heavy dump trucks. The liquid loop doesn't care; it just moves more hot coolant.

If your heating load is under 5 kW and cabin-only, air is fine. Above that, or if the number keeps growing when you add battery heating, you're in coolant territory.

**3. What does the vehicle already have?**

This is the practical question buyers forget to ask. If the vehicle already has a coolant loop — for the motor, the inverter, the battery — adding a PTC coolant heater is plumbing, not architecture. Tap into the loop, add the heater, done.

If there's no liquid loop at all, an air heater avoids building one. No pumps, no hoses, no coolant, no leak points. For a small electric delivery van that only needs cabin heat, that's a real saving in complexity.

But here's the thing: most electric commercial vehicles already have a thermal management loop for the battery. The incremental cost of adding a coolant heater to an existing loop is small. The cost of *not* having battery heating in a cold climate is a dead vehicle.

## The cost comparison nobody shows you

Air heater unit cost is lower. No argument. A 3 kW PTC air heater costs less than a 15 kW coolant heater.

But compare systems, not units:

| | PTC Air Heater | PTC Coolant Heater |
|---|---|---|
| Cabin heating | Yes | Yes (via heater core) |
| Battery heating | No — needs separate system | Yes (same loop) |
| Typical power range | 2–5 kW | 15–35 kW (single unit) |
| Plumbing | None | Coolant loop required |
| Best for | Small EVs, cabin-only, mild climates | Buses, trucks, cold climates, battery + cabin |

The air heater looks cheaper until you add the battery heating system it can't replace. Then the coolant heater — one unit, one installation, one control strategy — usually wins on total system cost.

## What we'd recommend

For electric buses and heavy trucks: coolant heater. The battery needs heat, the power requirements exceed what air can practically deliver, and the vehicle already has a thermal loop. This isn't a close call.

For light commercial vehicles in mild climates with no battery heating requirement: air heater. Simpler, cheaper, does the job.

For anything in between: send us the vehicle type, the lowest ambient temperature, whether the battery needs active heating, and your voltage platform. We'll tell you honestly which one fits — including when the answer is "air is enough, don't overspend."

## FAQ

**Can I use both?**
You can, and some vehicles do — a coolant heater for the battery loop plus a small air heater for fast cabin warm-up. But most of the time it's unnecessary complexity. A properly sized coolant heater with a good heater core warms the cabin fast enough.

**Does a coolant heater use more energy?**
It delivers more heat because it's sized larger, not because it's less efficient. PTC is PTC — near 100% conversion efficiency either way. The energy question is really "how much heat does the vehicle need," not "which heater wastes less."

**What about heat pumps?**
Heat pumps are more efficient above freezing, but their capacity collapses in deep cold — exactly when you need heat most. Many cold-climate EVs pair a heat pump with a PTC coolant heater as backup. The PTC handles the -20°C mornings; the heat pump handles the -5°C days efficiently.

**How do I size the kW?**
Cabin volume, insulation, target warm-up time, lowest ambient, and whether the battery loop shares the heater. Send us those five numbers and we'll size it. Don't just match the old diesel heater's kW — electric thermal systems behave differently.

---

*Tell us your vehicle type, coldest operating temperature, and whether the battery needs heating. We'll recommend coolant or air — and tell you honestly when the simpler option is enough.*

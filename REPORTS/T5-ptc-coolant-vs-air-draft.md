# T5 初稿：PTC Coolant Heater vs Air Heater（待 Peter 确认）

> 状态：初稿完成 2026-10-08，待 Peter 确认内容 → 确认后 Codex 发布（发布走 WAITING_APPROVAL）
> 依据：REPORTS/serp-ptc-coolant-heater-vs-air-heater.md（SERP 决策：GO）
> 内链说明：文中落地页链接为规划 URL，页面上线后生效

---
**Suggested meta title:** PTC Coolant Heater vs Air Heater: Guide for Electric Buses & Trucks
**Suggested meta description:** Comparing PTC coolant heaters vs air heaters for electric commercial vehicles? We break down warm-up, battery conditioning, cost and sizing — from a manufacturer's perspective.

---

# PTC Coolant Heater vs Air Heater: How to Choose for Electric Commercial Vehicles

Fleet operators electrifying their buses and trucks run into the same question every winter: how do you heat the cabin — and the battery — without killing the range? With no engine waste heat to borrow, electric commercial vehicles need a dedicated heating strategy. The two mainstream PTC options are air heaters and coolant heaters, and choosing wrong means cold passengers, slow charging, or money wasted on overkill hardware.

This guide compares the two technologies head to head, from a manufacturer's perspective, so you can match the heater to your vehicle, climate, and operating reality.

## How a PTC Air Heater Works

A PTC (Positive Temperature Coefficient) air heater uses ceramic heating elements that self-regulate their temperature: as they get hotter, their electrical resistance rises and power draw falls. In practice this means they cannot overheat even if the blower fan fails — a built-in safety trait.

Installation is straightforward. The unit mounts inside the existing HVAC box or as an inline duct heater. The blower pushes air through the hot PTC core and into the cabin. Heat arrives within minutes, with no plumbing, no pump, and no coolant to maintain. Industry research puts typical cabin warm-up at 3 to 5 minutes.

The trade-off is scope: a PTC air heater warms cabin air and nothing else. It does nothing for the battery pack.

## How a PTC Coolant Heater Works

A PTC coolant heater warms a water-glycol mixture in a closed loop instead of heating air directly. An electric circulation pump moves the hot coolant through the vehicle's existing heater core for cabin heat — the same layout diesel buses have used for decades.

The decisive difference is that the same loop can also serve the battery and power electronics. One heat source does two jobs: cabin comfort plus battery preconditioning and temperature conditioning. For commercial EVs, where the battery is the most expensive component on the vehicle, that second job often matters more than the first.

The price of this versatility is complexity: pump, expansion tank, hoses, and controls add parts, weight, and installation time compared with a duct-mounted air heater.

## PTC Coolant Heater vs Air Heater: Head-to-Head Comparison

| Dimension | PTC Air Heater | PTC Coolant Heater |
|---|---|---|
| Cabin warm-up | Fast — typically 3–5 minutes | Slower initial cabin warm-up; loop must heat first |
| Battery conditioning | None | Yes — same loop preconditions and conditions the battery |
| Winter range protection | Cabin heat only; battery stays cold | Warm battery charges faster and delivers more usable capacity |
| System complexity | Low — mounts in HVAC duct, no plumbing | Higher — pump, tank, hoses, controls |
| Upfront cost | Lower | Higher |
| Maintenance | Minimal | Coolant checks, pump service |
| Best for | Mild climates, smaller vehicles, simple retrofits | Cold climates, large cabins, battery thermal management needs |

A note on the numbers: industry market data shows air-heating PTC systems holding roughly 56% of the high-voltage PTC heater market, with liquid (coolant) systems at about 44% but growing faster — around 13% annually — driven by battery conditioning requirements in newer EV platforms.

## When to Choose a PTC Air Heater

Choose air heating when the job is genuinely cabin-only:

- **Mild winter climates.** If your routes rarely see sustained temperatures below about −10 °C, the battery penalty of cold operation stays manageable and cabin heat is the main requirement.
- **Smaller vehicles and short routes.** Vans, minibuses, and urban delivery vehicles with modest cabin volumes heat quickly with duct-mounted PTC units.
- **Simple retrofits.** If the vehicle already has intact HVAC ducts and you want minimum downtime, an inline PTC air heater is the path of least resistance.
- **Tight budgets.** Lower hardware and installation cost makes air heating the economical choice when battery conditioning is not on the requirements list.

## When to Choose a PTC Coolant Heater

Choose coolant heating when the battery is part of the heating problem — which, for commercial EVs in real winter, it usually is:

- **Cold climates (below −15 °C).** At deep cold, an unconditioned battery loses significant usable capacity and charges slowly. A coolant loop that preconditions the pack before charging pays for itself in uptime.
- **Battery preconditioning requirements.** Fast opportunity charging on route only works if the battery is within its happy temperature window (generally 15–25 °C for lithium chemistries). Coolant heaters get it there.
- **Large cabins.** Full-size city buses and coaches need 10 kW-plus of heat; distributing it through the existing heater-core layout is more even and more practical than duct heaters alone.
- **Integrated thermal management.** If your platform strategy is one thermal system for cabin, battery, and power electronics, the coolant loop is the backbone it builds on.
- **High-voltage platforms.** Modern 800 V bus and truck platforms pair naturally with high-voltage coolant heaters that draw directly from the traction pack.

## What About Heat Pumps?

An honest comparison has to mention heat pumps. They move ambient heat into the cabin at two to three times the efficiency of resistive heating, which is a genuine range advantage in mild weather. The catch, confirmed across multiple engineering studies, is that heat pump capacity fades severely in deep cold — exactly when you need heat most — so a PTC heater is still required as backup or supplement.

For many commercial fleets, the pragmatic answer is a combination: heat pump for efficiency in shoulder seasons, PTC coolant heater for guaranteed heat and battery conditioning in true winter. The two are complements, not rivals.

## Sizing Guide for Commercial Vehicles

Size for the coldest day on your routes, not the average one. Undersizing leaves the cabin cold on winter mornings; oversizing wastes battery capacity every day. As a starting guideline:

| Vehicle type | Recommended heating power |
|---|---|
| City bus, 10–12 m | 10–15 kW |
| Coach / long-distance bus | 12–20 kW |
| Delivery van / light truck | 5–8 kW |
| Heavy-duty truck | 8–15 kW |
| Mining / special vehicles (high-voltage) | 15–25 kW+ |

These are starting points. Final sizing should account for cabin volume, insulation, door-opening frequency (city buses lose heat at every stop), operating climate, and whether the same loop serves battery conditioning.

## FAQ

**What is the main difference between PTC air and coolant heaters?**
Air heaters warm cabin air directly through the HVAC ducts — simple and fast. Coolant heaters warm a water-glycol loop that serves both the cabin heater core and the battery thermal circuit — more complex, but it conditions the battery as well as the cabin.

**Do coolant heaters help with battery preconditioning?**
Yes. That is their decisive advantage for commercial EVs. Circulating warm coolant through the battery loop brings cells into their efficient temperature window, which improves both driving range and charging speed in cold weather.

**How much range does winter heating consume?**
Industry data indicates heating can consume 20–30% of battery energy in temperatures below 5 °C. Keeping the battery warm — not just the cabin — is the most effective way to protect winter range.

**Which is better for electric buses?**
For full-size electric buses, especially in cold climates, coolant heaters are generally the better fit: the cabin volumes are large, door openings dump heat constantly, and battery conditioning directly affects fleet uptime. Air heaters suit smaller vehicles and mild climates.

**Can I combine a heat pump with a PTC heater?**
Yes, and many operators do. The heat pump handles efficient heating in mild conditions while the PTC unit — ideally a coolant heater — guarantees heat and battery conditioning when temperatures drop.

## Talk to a Manufacturer Before You Spec

Catalog comparisons only go so far. The right heater depends on your vehicle type, voltage platform, cabin layout, and the coldest route on your network. As a manufacturer of high-voltage PTC heating systems for electric commercial vehicles — including units deployed on electric bus and hydrogen fuel cell bus fleets — we size and configure heaters against real operating conditions, not just datasheets.

Share your vehicle type, voltage platform, and operating climate, and we will recommend a heating configuration with honest trade-offs.

---

### Sources & notes (for transparency, not published)
- Cabin heating energy share (20–30% below 5 °C), market shares, warm-up times: high-voltage PTC heater market research (Dataintelo, P.W. Consulting).
- Air vs water PTC heating principles, heat pump COP vs cold-weather fade: peer-reviewed BEV thermal management literature (MDPI Energies).
- Sizing bands and −15 °C threshold: commercial EV heater application guides; extended to coach/heavy-truck classes as engineering guideline.
- Product references kept generic (no model numbers invented); case mentions (bus / hydrogen fuel cell bus fleets) per existing company assets — Peter to confirm wording before publish.

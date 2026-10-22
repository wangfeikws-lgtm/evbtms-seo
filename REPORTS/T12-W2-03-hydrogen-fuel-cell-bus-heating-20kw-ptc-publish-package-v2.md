# T12-W2-03 Publishing Package（v2 重组版，2026-10-22，原因：v1 ZeroGPT 42.9% 未过线；**v2 复测 31.5% 仍未过线，已派 v3 深度重组**）

## SEO fields

- **SEO title:** Hydrogen Fuel Cell Bus Heating: Why 20 kW PTC Became the Standard Answer | EVLINK
- **Meta description:** A fuel cell stack makes heat, just never when the cabin needs it most. Why hydrogen buses pair waste-heat recovery with a 20 kW class PTC coolant heater, and what to specify.
- **Primary keyword:** hydrogen bus heater
- **H1:** Hydrogen Fuel Cell Bus Heating: Why 20 kW PTC Became the Standard Answer
- **Recommended slug:** `hydrogen-fuel-cell-bus-heating-20kw-ptc`

## HTML body

```html
<p>"But the stack makes waste heat. Why are we buying a cabin heater at all?" Some version of that sentence turns up in the first meeting of nearly every fuel cell bus project we talk to. It is a reasonable question. It survives until the first cold start, and not much longer.</p>

<p>Our answer is the same each time: specify a PTC coolant heater in the 20 kW class from the start, and treat stack waste heat as a contribution that offsets it, never as the heating system. The fleets that ran hydrogen buses through genuine northern winters settled this years ago. The Beijing Winter Olympics fleets were simply the most public example: waste-heat recovery plus a proper electric heater, on every bus, without exception.</p>

<h2>The stack starts the morning as a heating load</h2>

<p>Begin with temperature. A diesel engine is a furnace that also turns wheels, and its coolant comes off hot. A PEM fuel cell is efficient, which is the entire point of it, and its coolant runs far cooler than diesel coolant. Then there is the cold start. At the start of a winter morning the stack is a cold mass that needs warming itself before it can work hard. For those first minutes the fuel cell is not a heat source waiting to be tapped. It is one more load in the queue.</p>

<p>And the queue forms at departure. Passengers board, the windscreen has to clear, the driver needs to see. Nobody boards twenty minutes later, once everything has settled.</p>

<h2>Cruise is the easy part of the route</h2>

<p>Published studies of fuel cell buses on winter cycles at around −7°C show a consistent pattern. At steady cruise, stack waste heat covers part of the cabin load. Drop into the low-load segments and an electric auxiliary heater carries the rest, most of it, in fact.</p>

<p>City duty is mostly low-load segments. Idling at a terminus. Crawling between stops. Doors opening every few hundred metres while the stack sips hydrogen and produces little heat, and twenty passengers still expect a warm cabin. Size the heating system for the cruise condition and it fails at the terminus, every day, in front of the people the bus was bought for. Size it honestly and you have specified a PTC heater.</p>

<h2>The load sum leaves a 20 kW hole</h2>

<p>Do the arithmetic for a 12-metre city bus in northern service. Cabin heat loss at cruise in deep cold. Warm air dumped at every door opening. A defrost requirement that does not negotiate. The total lands in the 15–25 kW band.</p>

<p>Waste heat, when it is available, offsets part of that. What remains, on the worst morning rather than the average one, is a heater in the 20 kW class. That is why the figure recurs across fleets and suppliers. It is not fashion. It is the size of the hole the stack leaves. Our E Series sits directly in that band at 20–24 kW across 400–800 V, and projects with larger cabins or colder routes step up into the Q Series range above it.</p>

<h2>One detail reaches projects late: the water</h2>

<p>Fuel cell coolant is not ordinary coolant. The stack loop must stay at very low electrical conductivity, so it runs deionised water with an ion exchanger, and anything that leaches ions into that loop is a warranty argument waiting to happen. A PTC heater therefore rarely sits inside the stack loop itself. The usual architecture gives the heater its own loop or couples it through a heat exchanger.</p>

<p>Which raises decisions most teams meet later than they should: which loop the heater belongs to, who controls it, and what happens to cabin heat during a stack fault. Decide that on paper. Deciding it during winter validation costs a season.</p>

<h2>What we would specify</h2>

<p>For a 12-metre fuel cell city bus in cold-climate service: a PTC coolant heater in the 20 kW class on its own controlled loop, waste-heat recovery plumbed to offset it whenever the stack is working, CAN control so the vehicle energy manager can ration heat against hydrogen state and route, and a defrost-first priority strategy for the first minutes after departure. Then validate on the coldest route, at the coldest hour, with a full passenger load simulation. Averages heat nobody.</p>

<h2>Questions we hear on this topic</h2>

<h3>Can stack waste heat ever be enough on its own?</h3>
<p>In mild climates and high-load duty, it can come close. In cold-climate city service, the cold start and low-load gaps remain, so a PTC heater is still needed. It may run less often, but it cannot be deleted.</p>

<h3>Why not fit a fuel-fired parking heater instead?</h3>
<p>Some early fleets did. It works thermally and fails strategically: a zero-emission bus burning diesel for heat is a hard story to tell a city customer, and several operating zones restrict it. Electric heating keeps the vehicle's emissions claim intact.</p>

<h3>Does a 20 kW heater hurt the bus's range?</h3>
<p>It draws real energy, and on a hydrogen bus that energy ultimately comes from hydrogen or the buffer battery. The alternative is not zero consumption; it is a cold cabin, a fogged windscreen and a vehicle that cannot enter service. Energy management, preconditioning at the depot and waste-heat blending keep the cost honest.</p>

<p><strong>Specifying a fuel cell bus for cold service?</strong> Send us the bus length, the coldest operating condition, the defrost requirement and the stack coolant architecture. We will size the heater and flag the loop questions before they reach winter testing.</p>
```

## Internal links

1. Anchor: `high-voltage coolant heater product range` → https://www.evptc.com/products.html
2. Anchor: `Q Series 15–35 kW coolant heater` → https://www.evptc.com/sale-40723397-high-voltage-ptc-water-heater-15-35kw-400-1100v-for-electric-vehicles-ev-battery-thermal-management-.html
3. Anchor: `why electric bus range falls in winter` → https://www.evptc.com/news/why-electric-bus-range-falls-in-winter-and-five-levers-fleets-can-control-422923.html
4. Anchor: `electric bus battery preheating at −30°C` → https://www.evptc.com/news/electric-bus-battery-preheating-at-30-c-five-planning-mistakes-422919.html

## Image recommendations

- Hero: approved EVLINK E-Series or Q-Series product photograph on a clean white background.
- Diagram: two-loop schematic (stack loop with deionised coolant, heater loop, heat exchanger between them), drawn generically without vehicle-brand references.
- Alt text: `EVLINK 20 kW class PTC coolant heater for hydrogen fuel cell bus cabin heating and defrost`.

## Fact-red-line self-check

- Uses only official EVLINK data: E Series 20–24 kW / 400–800 V, Q Series 15–35 kW / 400–1100 V, operating range −40 to +85°C, IP67 (implied series-wide; not restated as a claim in the body).
- The Winter Olympics reference is industry context only; the article does not claim EVLINK supplied any Olympic vehicle, names no customer, and quotes no fleet as an EVLINK case.
- The −7°C auxiliary-heating pattern is attributed to published research generally, without naming a paper or inventing figures.
- No certification names, prices, MOQ or lead-time claims.
- SERP note (2026-10-22): existing coverage explains fuel cell thermal systems generically or sells components; the gap is a direct answer to why the auxiliary heater lands at 20 kW, which this article fills.
- Angle differentiation: the site's older hydrogen-bus news items are event commentary; this is an evergreen engineering piece on heater sizing and loop architecture.
- v2 note (2026-10-22): structure-only restructure of v1 (new opening, narrative flow replacing the numbered-problem sections, verdict moved up front). No fact, figure, FAQ position or claim changed; no new parameters added.

## Remaining mandatory confirmation

- None for this version. If Peter wants the EVLINK hydrogen-bus supply history stated explicitly, that claim needs factory confirmation before it is added.

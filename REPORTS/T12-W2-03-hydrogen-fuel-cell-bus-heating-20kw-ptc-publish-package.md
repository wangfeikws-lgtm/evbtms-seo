# T12-W2-03 Publishing Package

## SEO fields

- **SEO title:** Hydrogen Fuel Cell Bus Heating: Why 20 kW PTC Became the Standard Answer | EVLINK
- **Meta description:** A fuel cell stack makes heat, just never when the cabin needs it most. Why hydrogen buses pair waste-heat recovery with a 20 kW class PTC coolant heater, and what to specify.
- **Primary keyword:** hydrogen bus heater
- **H1:** Hydrogen Fuel Cell Bus Heating: Why 20 kW PTC Became the Standard Answer
- **Recommended slug:** `hydrogen-fuel-cell-bus-heating-20kw-ptc`

## HTML body

```html
<p>Every fuel cell bus project we talk to starts with the same assumption: the stack makes waste heat, so cabin heating is solved. By the first winter test, the assumption is dead. The stack does make heat. It makes it at the wrong temperature, at the wrong time, and in the wrong amount, and a 20 kW class PTC coolant heater ends up doing the work the brochure assigned to the fuel cell.</p>

<p>This is not a fuel cell failure. It is physics, and the fleets that ran hydrogen buses through real northern winters, including the fleets on public display at the Beijing Winter Olympics, settled the question years ago. Their answer was waste-heat recovery plus a proper electric heater, never waste heat alone.</p>

<h2>Problem one: the heat arrives late</h2>

<p>A diesel engine is a furnace that also turns wheels; most of its fuel becomes heat, and coolant leaves it hot. A PEM fuel cell is far more efficient, which is the point of it, and its coolant typically runs far cooler than diesel coolant. Worse, at a cold start the stack is a cold mass that needs warming itself before it can work hard. For the first minutes of a winter morning, the fuel cell is a heating load, not a heat source.</p>

<p>Passengers do not board in the first minutes after the stack reaches steady state. They board at departure. The cabin, the windscreen and the driver all need heat at exactly the moment the stack has none to spare.</p>

<h2>Problem two: the heat disappears at low load</h2>

<p>Published studies of fuel cell buses running winter cycles at around −7°C show the same pattern: stack waste heat covers part of the cabin load at steady cruise, and an electric auxiliary heater carries the rest, carrying most of it during low-load segments. City duty is mostly low-load segments. Idling at a terminus, crawling between stops, holding at a depot: the stack sips hydrogen, produces little heat, and twenty passengers still expect a warm cabin and a clear windscreen.</p>

<p>Size the heating system for the cruise condition and it fails at the terminus. Size it for the terminus and you have specified a PTC heater.</p>

<h2>Why the number lands near 20 kW</h2>

<p>Do the load sum for a 12-metre city bus in northern service. Cabin heat loss at cruise in deep cold, door openings every few hundred metres dumping warm air, and a defrost requirement that is not negotiable: the total lands in the 15–25 kW band. Waste heat, when it is available, offsets part of that. What remains for the electric heater, on the worst morning rather than the average one, is a unit in the 20 kW class.</p>

<p>That is why the figure keeps recurring across fleets and suppliers. It is not fashion. It is the size of the hole the stack leaves. Our E Series sits directly in that band at 20–24 kW across 400–800 V, and projects with larger cabins or colder routes step up into the Q Series range above it.</p>

<h2>The detail that catches projects out: the water</h2>

<p>Fuel cell coolant is not ordinary coolant. The stack loop must stay at very low electrical conductivity, so it runs deionised water with an ion exchanger, and anything that leaches ions into that loop is a warranty argument waiting to happen. A PTC heater therefore rarely sits inside the stack loop itself. The usual architecture gives the heater its own loop or couples it through a heat exchanger, which adds a design decision most teams meet later than they should: which loop the heater belongs to, who controls it, and what happens to cabin heat during a stack fault.</p>

<p>Decide that on paper. Deciding it during winter validation costs a season.</p>

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
4. Anchor: `electric bus battery preheating at −30°C` → https://www.evptc.com/news/electric-bus-battery-preheating-at-30c-five-planning-mistakes-422919.html

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

## Remaining mandatory confirmation

- None for this version. If Peter wants the EVLINK hydrogen-bus supply history stated explicitly, that claim needs factory confirmation before it is added.

<?php
// EVLINK Product schema (no offers) - 21 product pages.
// Rank Math's Product form forces an offers block with no price,
// which Google flags as a missing-price error. This snippet outputs
// Product JSON-LD directly, with no offers, price, SKU or rating.
// Added 2026-11-24, approved by site owner.
add_action( 'wp_head', 'evlink_product_schema_no_offers', 20 );
function evlink_product_schema_no_offers() {
    if ( is_admin() ) return;
    $id = get_queried_object_id();
    $products = array(
        2950 => array( 'name' => "High Voltage Coolant Heater for Electric Vehicles", 'description' => "Explore EVLINK high-voltage coolant heaters for battery and cabin heating in electric buses and trucks. Compare A and Q series by voltage, power and application.", 'url' => "https://evbtms.com/products/high-voltage-coolant-heater/" ),
        2946 => array( 'name' => "Battery Thermal Management System (3–12kW)", 'description' => "Explore EVLINK 3 kW, 5 kW and 12 kW BTMS units for electric buses and trucks, with liquid cooling, CAN control and model-dependent heating.", 'url' => "https://evbtms.com/products/battery-thermal-management-system/" ),
        3177 => array( 'name' => "12kW Battery Thermal Management System", 'description' => "Explore the EVLINK LDC280HA-12KW battery thermal management system with 12 kW cooling, 8 kW PTC heating, DC 400–800 V input and CAN 2.0 control.", 'url' => "https://evbtms.com/products/battery-thermal-management-system/12kw/" ),
        3172 => array( 'name' => "3kW Battery Thermal Management System (BTMS)", 'description' => "Explore the EVLINK LDC300HA 3 kW battery thermal management system with DC 400–750 V input, CAN 2.0 control, 30 L/min coolant flow and IP67 protection.", 'url' => "https://evbtms.com/products/battery-thermal-management-system/3kw/" ),
        3175 => array( 'name' => "5kW Battery Thermal Management System", 'description' => "Explore the EVLINK LDC560HA 5 kW battery thermal management system with 6 kW PTC heating, CAN 2.0 control, 40 L/min coolant flow and IP67 protection.", 'url' => "https://evbtms.com/products/battery-thermal-management-system/5kw/" ),
        10016 => array( 'name' => "Liquid-Cooled Braking Resistor for Buses & Trucks", 'description' => "EVLINK HVH-R1402 liquid-cooled braking resistors dissipate regenerative braking energy buses and trucks can't feed back: 140 kW, 450–850 V DC, IP6K9K.", 'url' => "https://evbtms.com/products/braking-resistor/" ),
        2948 => array( 'name' => "Three-in-One Thermal Management Controller", 'description' => "One controller for the compressor, the refrigeration ECU and PTC heating: EVLINK's three-in-one unit cuts boxes and wiring on electric buses and trucks.", 'url' => "https://evbtms.com/products/three-in-one-controller/" ),
        2952 => array( 'name' => "Electric Compressors for EV Thermal Management", 'description' => "EVLINK electric compressors support efficient EV thermal management for passenger cars, commercial vehicles and specialized electric equipment.", 'url' => "https://evbtms.com/products/electric-compressor/" ),
        10033 => array( 'name' => "800V PTC Coolant Heater for Electric Bus (6–18 kW, 400–800 V)", 'description' => "800V high-voltage PTC coolant heater for electric buses. 6–18 kW for cabin heating, battery preheating and windshield defrosting. CAN control, IP67. Send your specs for a quote.", 'url' => "https://evbtms.com/products/800v-ptc-coolant-heater-electric-bus/" ),
        4942 => array( 'name' => "A1 6-18kW High Voltage Coolant Heater", 'description' => "Explore the EVLINK A1 6–18 kW high voltage coolant heater with 400–800 V operation, IP67 protection, CAN communication and a 5.1 kg unit weight.", 'url' => "https://evbtms.com/products/high-voltage-coolant-heater/a1-series/" ),
        5041 => array( 'name' => "A2 6-18kW High Voltage Coolant Heater", 'description' => "Explore the EVLINK A2 6–18 kW high voltage coolant heater for 400–800 V EV systems, with IP67 protection, CAN communication and a 5.1 kg unit weight.", 'url' => "https://evbtms.com/products/high-voltage-coolant-heater/a2-series/" ),
        5095 => array( 'name' => "A3 6-18kW High Voltage Coolant Heater", 'description' => "Explore the EVLINK A3 6–18 kW high voltage coolant heater for 400–800 V EV systems, featuring IP67 protection, CAN communication and a 5.1 kg unit weight.", 'url' => "https://evbtms.com/products/high-voltage-coolant-heater/a3-series/" ),
        5157 => array( 'name' => "A4 6-18kW High Voltage Coolant Heater", 'description' => "Explore the EVLINK A4 6–18 kW high voltage coolant heater for 400–800 V EV systems, with IP67 protection, CAN communication and a 5.1 kg unit weight.", 'url' => "https://evbtms.com/products/high-voltage-coolant-heater/a4-series/" ),
        5213 => array( 'name' => "A5 8–18 kW High Voltage Coolant Heater", 'description' => "EVLINK A5 high-voltage coolant heater. A Series 8–18 kW, rated 600 or 800 V DC, with CAN and enable signal control.", 'url' => "https://evbtms.com/products/high-voltage-coolant-heater/a5-series/" ),
        5294 => array( 'name' => "A6 6-18kW High Voltage Coolant Heater", 'description' => "Explore the EVLINK A6 6–18 kW high voltage coolant heater for 400–800 V EV systems, featuring IP67 protection, CAN communication and a 5.1 kg unit weight.", 'url' => "https://evbtms.com/products/high-voltage-coolant-heater/a6-series/" ),
        5452 => array( 'name' => "A7 6-18kW High Voltage Coolant Heater", 'description' => "Explore the EVLINK A7 6–18 kW high voltage coolant heater for 400–800 V EV systems, with IP67 protection, CAN communication and a 5.1 kg unit weight.", 'url' => "https://evbtms.com/products/high-voltage-coolant-heater/a7-series/" ),
        4591 => array( 'name' => "Q3 15-35kW High Voltage Coolant Heater", 'description' => "Explore the EVLINK Q3 15–35 kW high voltage coolant heater with 400–1100 V operation, IP67 protection, CAN bus control and customizable integration.", 'url' => "https://evbtms.com/products/high-voltage-coolant-heater/ev-high-voltage-heating-q-3/" ),
        4919 => array( 'name' => "Q4 15-35kW High Voltage Coolant Heater", 'description' => "Explore the EVLINK Q4 15–35 kW high voltage coolant heater for 400–1100 V EV systems, with IP67 protection, CAN communication and customizable control", 'url' => "https://evbtms.com/products/high-voltage-coolant-heater/ev-high-voltage-heating-q-4/" ),
        4860 => array( 'name' => "High Voltage Coolant Heaters", 'description' => "Compare EVLINK high voltage coolant heater models by power, operating voltage and application to select a suitable heater for your EV thermal system.", 'url' => "https://evbtms.com/products/high-voltage-coolant-heater/high-voltage/" ),
        4736 => array( 'name' => "Q2 15-35kW High Voltage Coolant Heater", 'description' => "Explore the EVLINK Q2 15–35 kW high voltage coolant heater for 400–1100 V EV systems, featuring IP67 protection, CAN communication and a 12 kg unit weight", 'url' => "https://evbtms.com/products/high-voltage-coolant-heater/q-series-2/" ),
        4593 => array( 'name' => "Q1 15-35kW High Voltage Coolant Heater", 'description' => "Explore the EVLINK Q1 15–35 kW high voltage coolant heater with 400–1100 V operation, IP67 protection, CAN bus control and a 12 kg unit weight.", 'url' => "https://evbtms.com/products/high-voltage-coolant-heater/qseries/" ),
    );
    if ( ! isset( $products[ $id ] ) ) return;
    $p = $products[ $id ];
    $schema = array(
        '@context' => 'https://schema.org',
        '@type' => 'Product',
        'name' => $p['name'],
        'description' => $p['description'],
        'brand' => array( '@type' => 'Brand', 'name' => 'EVLINK' ),
        'url' => $p['url'],
    );
    echo '<script type="application/ld+json">' . wp_json_encode( $schema, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE ) . '</script>' . "\n";
}

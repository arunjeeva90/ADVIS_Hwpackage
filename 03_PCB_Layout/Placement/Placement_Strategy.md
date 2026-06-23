# ADVIS Component Placement Strategy

**Document ID:** ADVIS-PCB-PLC-001  
**Version:** 0.1.0  
**Status:** Draft  
**Last Updated:** 2024-01-15

---

## 1. Purpose

This document defines the component placement strategy for the ADVIS ECU carrier board.
Placement priorities are driven by signal integrity, thermal management, EMC performance,
and manufacturing constraints.

---

## 2. Placement Zone Architecture

The carrier board is organized into functional placement zones. Each zone groups
related components to minimize trace lengths, contain switching noise, and enable
independent shielding if required.

```
+------------------------------------------------------------------+
|  ZONE A: Power Entry / Protection                                 |
|  [J100] [Fuse] [TVS] [PMOS]                                     |
+------------------------------------------------------------------+
|  ZONE B: Power Tree              |  ZONE C: SOM Interface         |
|  [LM61460] [TPS62130A]          |  [SOM Connector J5]            |
|  [TLV75518] [Inductors]         |  [Level shifters]              |
|  [Output caps]                   |  [Decoupling]                  |
+----------------------------------+--------------------------------+
|  ZONE D: Camera / Deserializer   |  ZONE E: Communication         |
|  [J2/J3 Coax] [DS90UB954]      |  [TCAN1044AV] [CAN Term]      |
|  [PoC components]                |  [USB-C J4]                    |
+----------------------------------+--------------------------------+
|  ZONE F: Navigation / Sensing    |  ZONE G: Supervision           |
|  [NEO-M9N] [J7 Antenna]        |  [TPS3808] [TPS3431]           |
|  [BMI088]                        |  [LEDs] [Headers]              |
+----------------------------------+--------------------------------+
|  ZONE H: IR / Expansion                                           |
|  [J6 IR Header]                                                   |
+------------------------------------------------------------------+
```

---

## 3. Placement Priorities

Components are placed in priority order. Higher-priority placements constrain
the locations available for lower-priority items.

| Priority | Zone | Components | Placement Driver |
|----------|------|-----------|-----------------|
| 1 | A | Connectors (J100, J2, J3, J4) | Fixed by enclosure/connector access |
| 2 | B | LM61460-Q1 + inductor + caps | Tight hot loop for EMI |
| 3 | D | DS90UB954-Q1 | Close to camera connectors (minimize FPD-Link trace) |
| 4 | C | SOM connector | Close to deserializer (minimize CSI-2 trace) |
| 5 | B | TPS62130A-Q1 + inductor + caps | Tight loop, 5V input proximity |
| 6 | B | TLV75518-Q1 + caps | Near 3.3V load center |
| 7 | E | TCAN1044AV-Q1 | Close to vehicle connector J100 |
| 8 | G | TPS3808G33-Q1, TPS3431-Q1 | Near SOM for short reset/WDI traces |
| 9 | F | NEO-M9N-00B | Near antenna connector J7, away from switching |
| 10 | F | BMI088 | Away from vibration sources, known orientation |

---

## 4. Critical Placement Rules

### 4.1 Power Entry (Zone A)

- Vehicle connector J100 at board edge for harness access
- Fuse -> TVS -> PMOS in sequential linear flow from connector
- Minimal trace length between protection components (< 10mm each)
- Input capacitors between connector and first active component
- Power entry ground return via directly adjacent to connector

### 4.2 Buck Converter Hot Loops (Zone B)

- LM61460-Q1: Input cap -> VIN pin -> SW pin -> Inductor -> Output cap -> GND
  must form the tightest possible loop on a single layer
- No signal traces routed through the hot loop area
- Ground plane beneath LM61460-Q1 must be unbroken (no via penetrations in hot loop)
- Switching node trace minimized in area (EMI reduction)
- Thermal pad connected to internal ground plane through multiple thermal vias

### 4.3 Camera Deserializer (Zone D)

- DS90UB954-Q1 placed equidistant from J2 and J3 coax connectors
- CSI-2 output side facing SOM connector direction
- Clock crystal/oscillator within 5mm of XTAL pins
- All decoupling capacitors within 2mm of respective VDD pins
- FPD-Link input traces routed on same layer as connector pads (no vias)

### 4.4 SOM Interface (Zone C)

- SOM connector oriented for shortest CSI-2 path from deserializer
- Bulk decoupling for SOM power pins placed on connector back side
- High-speed signals exit connector on same layer (avoid immediate layer transitions)
- Reset and boot signals routed short (< 25mm) to supervision zone

### 4.5 CAN Transceiver (Zone E)

- TCAN1044AV-Q1 placed close to vehicle connector J100
- CAN_H/CAN_L differential pair short run to connector
- Split termination at board edge (between transceiver and connector)
- Common-mode choke (if used) between termination and connector
- Physical separation from camera high-speed signals (minimum 10mm)

### 4.6 GNSS Receiver (Zone F)

- NEO-M9N placed close to antenna connector J7
- RF trace from antenna connector to GNSS input minimized
- Ground plane beneath GNSS module must be solid (no routing underneath)
- Separation from switching power supplies (minimum 15mm from inductors)
- Separation from high-speed digital signals (minimum 10mm)

### 4.7 IMU (Zone F)

- BMI088 placed at known position with documented orientation to vehicle axes
- Mounting location should be at or near PCB center of mass
- Avoid placement near board edges (vibration mode coupling)
- Keep away from thermal sources (regulators, SOM)
- Orientation markers on silkscreen (X, Y, Z axes with arrows)

---

## 5. Keep-Out Zones

| Zone Type | Size | Purpose |
|-----------|------|---------|
| Connector mating area | Per connector datasheet | Clearance for mating/unmating |
| Antenna clearance | 10mm radius around RF trace | Ground plane only, no copper traces |
| SOM module footprint | Per SOM mechanical drawing | No tall components under SOM |
| Thermal relief | 5mm around power inductors | Airflow and thermal isolation |
| Mounting holes | 3mm radius no-copper zone | Mechanical stress isolation |
| Board edge | 0.5mm no-trace zone | Manufacturing panel routing clearance |

---

## 6. Thermal Placement Considerations

| Component | Power Dissipation (est.) | Thermal Strategy |
|-----------|-------------------------|-----------------|
| LM61460-Q1 | 1.5W (worst case) | Exposed pad with thermal via array |
| TPS62130A-Q1 | 0.5W (worst case) | Exposed pad, local ground pour |
| DS90UB954-Q1 | 0.8W (worst case) | Ground pad, thermal relief to L2 |
| SOM Module | 3-5W (SoC dependent) | SOM manages own thermal, carrier provides path |
| TCAN1044AV-Q1 | 0.3W | Standard pad, no special treatment |

### Thermal Design Rules

- Power components (Zone B) grouped but spaced for independent thermal paths
- Do not place temperature-sensitive components (GNSS, IMU) adjacent to power dissipators
- Thermal vias under exposed pads: minimum 4x per pad (0.3mm drill)
- Bottom-side ground pour acts as secondary thermal spreader
- No thermal vias in high-speed signal return path areas

---

## 7. Manufacturing Placement Constraints

| Constraint | Requirement | Rationale |
|-----------|-------------|-----------|
| Component clearance | Min 0.3mm between pads | Solder bridging prevention |
| Polarity marking | All polarized parts with visible silk | Assembly error prevention |
| Fiducial access | 3 global fiducials, unobstructed | Machine vision alignment |
| Testpad access | All critical nets accessible from one side | In-circuit test probe |
| Tombstone prevention | Orient small passives with same pad-facing reflow direction | Assembly yield |
| BGA/QFN via-in-pad | Via filled and capped if via-in-pad | Solder void prevention |

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1.0 | 2024-01-15 | -- | Initial placement strategy definition |

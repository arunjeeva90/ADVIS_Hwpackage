# ADVIS Ground Domain Architecture

## Version
v1.0 - June 2026

## Document ID
ARCH-GND-001

---

## 1. Overview

This document defines the ground domain architecture for the ADVIS ECU platform. Proper ground domain separation and interconnection is critical for EMC performance, ESD return paths, signal integrity, and safety compliance.

The ADVIS platform uses three distinct ground domains with controlled interconnection points.

---

## 2. Ground Domain Definitions

| Domain | Name | Symbol | Purpose |
|--------|------|--------|---------|
| 1 | Power Input Ground | PGND_IN | High-current return for input power stage |
| 2 | Board Ground | BOARD_GND | Signal and logic return for all on-board circuits |
| 3 | Chassis Ground | CHASSIS_GND | Enclosure, shield, and ESD reference |

---

## 3. Ground Domain Topology

```
    VEHICLE CHASSIS / BODY
    ==============================================
              |
              | (Connector shell, shield drain)
              v
    +-------------------+
    | CHASSIS_GND       |
    | (Enclosure, Shld) |
    +-------------------+
              |
              | Single-point bond (star ground)
              | (M4 stud or dedicated pad)
              v
    +====================================+
    |          STAR GROUND POINT         |
    |        (PCB ground star node)      |
    +====================================+
         |                       |
         v                       v
    +-----------+         +-----------+
    | PGND_IN   |         | BOARD_GND |
    | (Power)   |         | (Signal)  |
    +-----------+         +-----------+
         |                       |
         | High-current          | Low-current
         | return path           | signal returns
         |                       |
    +----------+           +-----------+--------+--------+
    | LM61460  |           | DS90UB954 | BMI088 | NEO-M9N|
    | TPS62130A|           | TCAN1044  | SoM    | USB    |
    | TLV75518 |           |           |        |        |
    | Input    |           |           |        |        |
    | filter   |           |           |        |        |
    +----------+           +-----------+--------+--------+
```

---

## 4. Domain Interconnection Rules

### 4.1 Star-Point Topology

All three ground domains connect at a single star point on the PCB. This star point:

- Is located geometrically near the center of the board
- Uses a dedicated copper area (minimum 5mm x 5mm exposed pad)
- Has via stitching to all internal ground planes
- Is the ONLY point where PGND_IN and BOARD_GND connect (no other bridges)

### 4.2 PGND_IN to BOARD_GND

| Rule | Requirement |
|------|-------------|
| Connection | Through star point ONLY |
| No direct bridges | Copper pour separation maintained everywhere else |
| Separation gap | Minimum 0.5mm moat between power and signal ground pours |
| Filter capacitors | Input filter caps return to PGND_IN, output caps return to BOARD_GND |

### 4.3 CHASSIS_GND to Star Point

| Rule | Requirement |
|------|-------------|
| Connection method | Single M4 mounting stud or connector shell ground pin |
| Bond impedance | < 5 milliohms at DC |
| ESD path | All connector shells bond to CHASSIS_GND |
| Shield drains | All cable shield terminations go to CHASSIS_GND |

### 4.4 BOARD_GND Internal Partitioning

Within BOARD_GND, the following partitioning practices apply:

| Zone | Components | Notes |
|------|-----------|-------|
| Digital core | SoM, DS90UB954 | High-speed switching, maximum decoupling |
| Analog/sensor | BMI088, NEO-M9N | Low-noise, separated from digital switching |
| Communication | TCAN1044AV, USB | Protected from digital noise |

These zones share a common BOARD_GND plane but use strategic via placement and routing to minimize return-current coupling.

---

## 5. ESD Return Paths

| Interface | ESD Event Source | Return Path |
|-----------|-----------------|-------------|
| J100 (Vehicle) | Connector mate/unmate | Shell -> CHASSIS_GND -> Star -> BOARD_GND |
| J200/J201 (Camera) | Cable shield discharge | Shell -> CHASSIS_GND -> Star -> BOARD_GND |
| J300 (USB-C) | Human body ESD | Shell -> CHASSIS_GND -> Star -> BOARD_GND |
| J800 (IR Board) | Board insertion | BOARD_GND direct (internal connector) |
| Enclosure touch | External human contact | Enclosure -> CHASSIS_GND -> Star |

### ESD Design Principles

1. ESD current must never flow through sensitive signal traces
2. All connector ground pins placed closest to shell for shortest return path
3. TVS/ESD clamp devices placed within 5mm of connector pins
4. Guard traces on sensitive signals adjacent to connector areas

---

## 6. PCB Layer Allocation for Ground

| Layer | Ground Usage |
|-------|-------------|
| Top | Component pads, ground vias, local ground pours |
| L2 (GND plane) | Continuous BOARD_GND reference plane |
| Internal | Power ground fills where needed, PGND_IN copper |
| Bottom | Ground vias, local pours, star point access |

### Ground Plane Integrity Rules

- No signal traces may split the L2 ground plane
- All high-speed signals (CSI-2, FPD-Link, USB) must have uninterrupted ground reference
- Return current path must be considered for every signal route
- Via stitching around board perimeter at maximum 3mm spacing

---

## 7. Ground Domain Verification Checklist

| Check | Method | Pass Criteria |
|-------|--------|---------------|
| Star point single-connection | Visual DRC | No copper bridges between PGND_IN and BOARD_GND outside star |
| Chassis bond impedance | 4-wire measurement | < 5 milliohms |
| Ground plane continuity | Gerber review | No unintended splits under high-speed signals |
| ESD path impedance | TDR measurement | < 1 ohm at DC from any connector to star point |
| PGND/BOARD separation gap | DRC rule | >= 0.5mm everywhere except star |

---

## 8. Grounding Best Practices (ADVIS-Specific)

1. **Camera interface**: FPD-Link III coax shield terminates to CHASSIS_GND at connector, with ferrite bead to BOARD_GND
2. **CAN bus**: CAN_H/CAN_L shield (if shielded cable used) terminates to CHASSIS_GND
3. **GNSS antenna**: Antenna ground plane references BOARD_GND; cable shield to CHASSIS_GND at entry
4. **SoM connector**: All SoM ground pins connect to BOARD_GND with short via paths
5. **Power stage**: Input capacitors return to PGND_IN; output capacitors return to BOARD_GND

---

## 9. Revision History

| Rev | Date | Author | Change |
|-----|------|--------|--------|
| 1.0 | 2026-06 | Architecture Team | Initial release |

# ADVIS Vehicle Connector Interface Specification

## Version
v1.0 - June 2026

## Document ID
ICD-VEH-001

---

## 1. Purpose

This Interface Control Document defines the vehicle harness connector (J100) interface specification for the ADVIS ECU. J100 is the primary connection between the ECU and the vehicle electrical system, carrying power, communication, and antenna signals.

---

## 2. Connector Overview

```
    VEHICLE HARNESS SIDE          ECU SIDE (J100)
    ====================          ===============

    +--[12V_BAT]----------+-------> 12V Input (to fuse + protection)
    |                      |
    +--[GND_RET]-----------+-------> PGND_IN (power ground return)
    |                      |
    +--[CAN_H]-------------+-------> CAN-FD High (to TCAN1044AV-Q1)
    |                      |
    +--[CAN_L]-------------+-------> CAN-FD Low (to TCAN1044AV-Q1)
    |                      |
    +--[IGN_SENSE]----------+-------> Ignition status input
    |                      |
    +--[WAKE]--------------+-------> Wake-up input (edge-triggered)
    |                      |
    +--[GNSS_ANT]----------+-------> GNSS antenna RF feed-through
    |                      |
    +--[SHIELD/CHASSIS]----+-------> CHASSIS_GND (connector shell)
    |                      |
    +--[SPARE_1]-----------+-------> Reserved for future use
    |                      |
    +--[SPARE_2]-----------+-------> Reserved for future use
    +----------------------+
```

---

## 3. Pin Function Definitions

| Pin Function | Signal Name | Direction | Type | Description |
|-------------|-------------|-----------|------|-------------|
| 12V Battery | 12V_BAT | Vehicle -> ECU | Power | Primary power supply (8-16V nom.) |
| Ground Return | GND_RET | Common | Power | High-current power return |
| CAN High | CAN_H | Bidirectional | Diff signal | ISO 11898-2 CAN-FD high |
| CAN Low | CAN_L | Bidirectional | Diff signal | ISO 11898-2 CAN-FD low |
| Ignition Sense | IGN_SENSE | Vehicle -> ECU | Logic | Ignition ON/OFF status |
| Wake Input | WAKE | Vehicle -> ECU | Logic | Edge wake-up trigger |
| GNSS Antenna | GNSS_ANT | Antenna -> ECU | RF coax | Antenna feed to NEO-M9N |
| Shield/Chassis | SHLD | Common | Ground | Connector shell to CHASSIS_GND |
| Spare 1 | SPARE_1 | TBD | TBD | Reserved for future (e.g., Ethernet) |
| Spare 2 | SPARE_2 | TBD | TBD | Reserved for future |

---

## 4. Power Interface

### 4.1 12V Battery Input

| Parameter | Specification |
|-----------|---------------|
| Nominal voltage | 12V (passenger vehicle) / 24V option with redesign |
| Operating range | 8V to 16V continuous |
| Transient survival | Per ISO 7637-2 (load dump up to 42V, 400ms) |
| Crank dip immunity | Down to 6V for 50ms (system must not reset) |
| Reverse polarity | Protected by 80V PMOS (no damage up to -16V) |
| Quiescent current (sleep) | < 5mA (target for always-connected operation) |
| Maximum operating current | 5A (fuse-protected) |

### 4.2 Ground Return

| Parameter | Specification |
|-----------|---------------|
| Wire gauge | Minimum 1.0mm^2 (16 AWG equivalent) |
| Connection | Directly to vehicle chassis ground point |
| Contact resistance | < 10 milliohms (connector + wire) |
| Current rating | Equal to or greater than 12V supply pin |

---

## 5. CAN-FD Interface

| Parameter | Specification |
|-----------|---------------|
| Standard | ISO 11898-2 (CAN-FD physical layer) |
| Arbitration bit rate | 500 kbps (default), configurable |
| Data phase bit rate | 2 Mbps (default), up to 5 Mbps |
| Bus termination | 120 ohm split-termination on ECU (configurable) |
| Common-mode voltage | -2V to +7V |
| Fault tolerance | +/-58V sustained on CAN_H or CAN_L |
| ESD protection | IEC 61000-4-2 Level 4 (+/-8kV contact) |
| Wire type | Twisted pair, shielded (recommended) |
| Wire gauge | 0.35mm^2 minimum |

---

## 6. Ignition Sense Input

| Parameter | Specification |
|-----------|---------------|
| Logic high (IGN ON) | > 6V (vehicle 12V rail present through ignition switch) |
| Logic low (IGN OFF) | < 2V |
| Input impedance | > 100k ohm (resistive divider on carrier) |
| Debounce | 100ms minimum (firmware-implemented) |
| Pull-down | 100k to GND (ensures defined low when disconnected) |
| Purpose | Determines system power state (run vs. sleep) |

---

## 7. Wake Input

| Parameter | Specification |
|-----------|---------------|
| Trigger type | Rising-edge or level-triggered (configurable) |
| Logic high | > 6V |
| Logic low | < 2V |
| Pulse width (minimum) | > 10ms for reliable detection |
| Input impedance | > 100k ohm |
| Pull-down | 100k to GND |
| Wake sources | CAN bus activity, door open, remote start |
| Purpose | Brings ECU from sleep to active when IGN is off |

---

## 8. GNSS Antenna Feed-Through

| Parameter | Specification |
|-----------|---------------|
| RF frequency | L1 band (1575.42 MHz) + L5 (optional) |
| Impedance | 50 ohm |
| Connector type | SMA or FAKRA (antenna-side) to board trace (ECU-side) |
| DC bias | 3.0V to 5.0V for active antenna LNA power |
| DC bias current | Up to 30mA |
| Insertion loss (connector) | < 0.5 dB |
| ESD protection | Gas discharge tube or TVS at antenna entry |
| Shield | Continuous shield from antenna connector to NEO-M9N input |

---

## 9. Connector Mechanical Requirements

| Parameter | Specification |
|-----------|---------------|
| Connector type | Sealed automotive (e.g., Molex MX150, TE MCP, or equivalent) |
| Sealing | IP67 at mated face |
| Pin count | 10 minimum (8 defined + 2 spare) |
| Contact type | Tin or gold plated (gold for signal pins) |
| Mating force | < 80N total insertion force |
| Retention (axial pull) | > 100N |
| Operating temperature | -40C to +125C |
| Vibration | Per ISO 16750-3, windshield-mount profile |
| Salt spray | 96 hours minimum (per connector spec) |
| Mating cycles | Minimum 25 (service life) |

---

## 10. Mating and Unmating Requirements

| Requirement | Specification |
|-------------|---------------|
| Power-off before disconnect | Recommended (hot unplug must not damage ECU) |
| Pin engagement order | Ground pins make first, break last |
| Connector locking | Positive lock with secondary lock (CPA) |
| Blind-mate capability | Not required (technician-installed) |
| Service access | Rear face of enclosure |
| Cable strain relief | Integrated into connector housing or separate clamp |

---

## 11. Wire Harness Requirements

| Parameter | Specification |
|-----------|---------------|
| Harness length | Vehicle-dependent (typically 1m to 5m) |
| Power wire gauge | 1.0mm^2 minimum (12V and GND) |
| Signal wire gauge | 0.35mm^2 minimum (CAN, IGN, WAKE) |
| CAN pair | Twisted, shielded |
| Overall shield | Braided, drain wire to vehicle chassis |
| Temperature rating | -40C to +105C |
| Abrasion protection | Corrugated conduit or tape wrap |

---

## 12. Electrical Safety

| Parameter | Specification |
|-----------|---------------|
| Maximum voltage at connector | < 60V DC (LV system, no HV hazard) |
| Short-circuit protection | Fuse on 12V input |
| Creepage (12V pins to chassis) | > 1mm |
| Clearance (12V pins to chassis) | > 0.5mm |

---

## 13. Revision History

| Rev | Date | Author | Change |
|-----|------|--------|--------|
| 1.0 | 2026-06 | Vehicle Integration Team | Initial release |

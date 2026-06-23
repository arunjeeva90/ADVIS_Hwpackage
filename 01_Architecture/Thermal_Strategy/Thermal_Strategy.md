# ADVIS Thermal Strategy

## Version
v1.0 - June 2026

## Document ID
ARCH-THM-001

---

## 1. Overview

This document defines the thermal management strategy for the ADVIS ECU platform. The system must operate reliably across the full automotive temperature range while dissipating heat from the SoM processor, power regulators, and camera deserializer.

**Operating temperature range:** -40C to +85C ambient (under-windshield mounting)

---

## 2. Thermal Budget Summary

| Component | Typical Power (W) | Peak Power (W) | Package | Thermal Path |
|-----------|-------------------|----------------|---------|--------------|
| SoM (TDA4VM/AM68A) | 5.0 | 8.0 | Module | Heatsink/thermal pad |
| LM61460-Q1 (5V buck) | 1.5 | 2.5 | HTSSOP-16 | Exposed pad to PCB |
| TPS62130A-Q1 (3.3V) | 0.2 | 0.3 | QFN-16 | Exposed pad to PCB |
| DS90UB954-Q1 | 0.8 | 1.2 | QFP-64 | Pad to PCB |
| TCAN1044AV-Q1 | 0.05 | 0.1 | SOIC-8 | Leads to PCB |
| BMI088 | 0.01 | 0.01 | LGA-16 | Pad to PCB |
| NEO-M9N | 0.05 | 0.08 | LCC-24 | Pad to PCB |
| TLV75518-Q1 | 0.03 | 0.04 | SOT-23-5 | Leads to PCB |
| PMOS (reverse pol.) | 0.3 | 0.5 | SO-8 | Pad to PCB |
| **TOTAL** | **7.94** | **12.73** | | |

---

## 3. Thermal Architecture

```
                    AMBIENT AIR (vehicle cabin)
                    ===========================
                              ^
                              | Natural convection
                              | (no forced air)
                              |
                    +-------------------+
                    |   ENCLOSURE LID   |
                    | (Aluminum/Plastic)|
                    +-------------------+
                              ^
                              | Radiation + Conduction
                              |
            +------+----------+-----------+-------+
            |      |          |           |       |
            v      v          v           v       v
          +----+ +----+ +---------+ +--------+ +----+
          |SoM | |Buck| |Deser    | | PMOS   | |3V3 |
          |Heat| |Pad | |Thermal  | | Pad    | |Pad |
          |Sink| |    | |Pad      | |        | |    |
          +----+ +----+ +---------+ +--------+ +----+
            |      |          |           |       |
            v      v          v           v       v
    +=======================================================+
    |              PCB (FR4, multi-layer)                    |
    |  Thermal vias under pads    Internal copper spreading |
    +=======================================================+
            |
            v
    +-------------------+
    |  ENCLOSURE BASE   |
    | (Thermal pad/gap  |
    |  filler to case)  |
    +-------------------+
            |
            v
    +-------------------+
    |   MOUNTING BRKT   |
    |  (Windshield/     |
    |   headliner)      |
    +-------------------+
```

---

## 4. Cooling Strategy by Product Tier

| Tier | Total Power (typ) | Cooling Method | Notes |
|------|-------------------|----------------|-------|
| ADVIS Assist | ~6W | Passive only | Low-power SoM variant, no heatsink fins needed |
| ADVIS Control | ~8W | Passive + thermal pad | Standard SoM, thermal interface to enclosure |
| ADVIS Fusion | ~10W | Passive + enhanced heatsink | Higher compute load for sensor fusion |
| ADVIS Fleet | ~6W | Passive only | Similar to Assist, logging-focused |

All tiers use the same carrier board. Thermal management differences are in the SoM selection and enclosure design.

---

## 5. Thermal Interface Materials

| Interface | Material Type | Thickness | Thermal Conductivity |
|-----------|--------------|-----------|---------------------|
| SoM to heatsink | Thermal pad (silicone) | 1.0mm nominal | > 3 W/m-K |
| Heatsink to enclosure lid | Thermal gap filler | 0.5-2.0mm (compressed) | > 2 W/m-K |
| PCB to enclosure base | Thermal pad (optional) | 1.0mm | > 1.5 W/m-K |
| Regulator exposed pad to PCB | Solder + thermal vias | N/A | Via array conductance |

---

## 6. Thermal Via Design

For components with exposed thermal pads (LM61460, TPS62130A, DS90UB954):

| Parameter | Specification |
|-----------|---------------|
| Via diameter | 0.3mm drill |
| Via pitch | 1.0mm grid |
| Via fill | Plugged and capped (prevents solder wicking) |
| Minimum via count | Per-component: see below |
| Target thermal resistance | < 20 C/W from pad to internal ground plane |

| Component | Pad Size | Via Count (min) |
|-----------|----------|-----------------|
| LM61460-Q1 | 5mm x 5mm | 16 (4x4 array) |
| TPS62130A-Q1 | 3mm x 3mm | 9 (3x3 array) |
| DS90UB954-Q1 | 7mm x 7mm | 25 (5x5 array) |

---

## 7. Temperature Derating

### 7.1 Junction Temperature Limits

| Component | Tj Max (datasheet) | Tj Target (design) | Derating |
|-----------|-------------------|--------------------|---------| 
| TDA4VM SoM | +125C | +105C | 20C margin |
| LM61460-Q1 | +150C | +125C | 25C margin |
| TPS62130A-Q1 | +150C | +125C | 25C margin |
| DS90UB954-Q1 | +125C | +105C | 20C margin |
| TCAN1044AV-Q1 | +150C | +125C | 25C margin |

### 7.2 Ambient to Junction Budget

At maximum ambient (+85C):

```
Tj = Ta + (P * Theta_JA)

SoM:      Tj = 85 + (8.0 * ~5)  = 125C  [WITH heatsink, Theta ~5 C/W]
LM61460:  Tj = 85 + (2.5 * 35)  = 172C  [EXCEEDS LIMIT without mitigation]
          With thermal vias: Theta_eff ~15 C/W
          Tj = 85 + (2.5 * 15) = 122.5C [OK with margin]
```

**Critical insight:** The LM61460-Q1 REQUIRES adequate thermal via arrays and copper spreading to stay within junction temperature at +85C ambient with maximum load.

---

## 8. Airflow Considerations

| Parameter | Specification |
|-----------|---------------|
| Forced airflow | NOT available (sealed enclosure) |
| Natural convection | Available from enclosure surfaces |
| Mounting orientation | Windshield-mount (vertical or angled) |
| Ventilation holes | NOT permitted (IP54 minimum requirement) |
| Internal air volume | Sufficient for natural convection assist |

---

## 9. Thermal Simulation Requirements

Before PCB layout release, the following thermal simulations must be completed:

| Simulation | Tool | Pass Criteria |
|-----------|------|---------------|
| Steady-state at +85C ambient | CFD or FEA | All Tj < target |
| Transient cold-start at -40C | Transient thermal | Condensation risk assessment |
| Hot-soak (engine-off, sun-load) | CFD | Enclosure internal temp < +95C |
| Power cycling | Transient thermal | Solder joint life > 10 years |

---

## 10. Thermal Test Points

| Test Point | Location | Purpose |
|-----------|----------|---------|
| TP_SOM | SoM heatsink surface | Monitor SoM case temperature |
| TP_BUCK | Near LM61460 exposed pad | Monitor buck converter temp |
| TP_DESER | Near DS90UB954 | Monitor deserializer temp |
| TP_AMB | PCB edge, away from heat | Reference ambient inside enclosure |

---

## 11. Thermal Protection Features

| Feature | Implementation | Action |
|---------|---------------|--------|
| SoM over-temp | SoM internal thermal sensor | Throttle clock frequency |
| Regulator OTP | LM61460 internal comparator | Shutdown and hiccup restart |
| Software monitoring | SoM reads thermal sensors | Log warning, reduce processing load |
| Watchdog interaction | If thermal shutdown resets SoM | Watchdog holds system in reset |

---

## 12. Revision History

| Rev | Date | Author | Change |
|-----|------|--------|--------|
| 1.0 | 2026-06 | Thermal Team | Initial release |

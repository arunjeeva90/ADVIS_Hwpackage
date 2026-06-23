# ADVIS PCB Stackup Definition

**Document ID:** ADVIS-PCB-STK-001  
**Version:** 0.1.0  
**Status:** Draft  
**Last Updated:** 2024-01-15

---

## 1. Overview

This document defines the target PCB layer stackup for the ADVIS ECU carrier board.
An 8-layer stackup is selected to accommodate high-speed differential routing (CSI-2,
FPD-Link III), controlled impedance requirements, power distribution, and EMC shielding
while maintaining production cost targets.

---

## 2. Layer Assignment

| Layer | Name | Type | Primary Function |
|-------|------|------|-----------------|
| L1 | TOP | Signal | Component placement, high-speed traces, test points |
| L2 | GND1 | Plane | Primary ground reference plane (unbroken) |
| L3 | SIG1 | Signal | Inner signal routing (low-speed, I2C, SPI, UART) |
| L4 | PWR1 | Plane | Power plane (5V_SYS, 3V3_IO split) |
| L5 | PWR2 | Plane | Power plane (1V8, SOM power domains) |
| L6 | SIG2 | Signal | Inner signal routing (CAN, GPIO, control signals) |
| L7 | GND2 | Plane | Secondary ground reference plane (unbroken) |
| L8 | BOT | Signal | Component placement, power traces, low-speed routing |

### Layer Purpose Notes

- **L1 (TOP):** Primary high-speed routing surface. CSI-2, FPD-Link III, and USB
  differential pairs routed here with immediate ground reference on L2.
- **L2 (GND1):** Unbroken ground plane. Critical for high-speed signal integrity.
  No cuts, splits, or vias through active signal areas.
- **L3 (SIG1):** Inner routing for moderate-speed signals. Referenced to GND1 (above)
  and PWR1 (below). Used for I2C, SPI, UART, and general control signals.
- **L4 (PWR1):** Primary power distribution. Split between 5V_SYS and 3V3_IO regions
  following component placement zones.
- **L5 (PWR2):** Secondary power. 1V8 region and SOM-specific power domains.
  Islands connected via plane stitching.
- **L6 (SIG2):** Inner routing for CAN bus, status signals, and GPIO. Referenced to
  PWR2 (above) and GND2 (below).
- **L7 (GND2):** Second unbroken ground plane. Reference for bottom-side signals.
  Stitched to GND1 with via farm at board perimeter.
- **L8 (BOT):** Secondary component placement (primarily passives, power components).
  Power bus routing for high-current paths.

---

## 3. Impedance Targets

### 3.1 Single-Ended Signals

| Target Impedance | Application | Trace Width (estimated) | Reference Layer |
|-----------------|-------------|------------------------|-----------------|
| 50 ohm | General digital signals | TBD per fab house DFM | GND1 or GND2 |

### 3.2 Differential Pairs

| Target Impedance | Application | Pair Spacing (estimated) | Reference Layer |
|-----------------|-------------|-------------------------|-----------------|
| 100 ohm differential | CSI-2 (4 lanes + clock) | Per fab house calc | GND1 (L2) |
| 100 ohm differential | FPD-Link III input | Per fab house calc | GND1 (L2) |
| 90 ohm differential | USB 2.0 (D+/D-) | Per fab house calc | GND1 (L2) |
| 120 ohm differential | CAN-FD (CAN_H/CAN_L) | Per fab house calc | GND2 (L7) |

### 3.3 Impedance Control Notes

- All impedance targets assume controlled dielectric material (see Section 4)
- Fab house to provide impedance test coupons on panel
- Target tolerance: +/- 10% on all controlled impedance traces
- Impedance calculated per IPC-2141 methodology
- Trace width and spacing to be finalized with fab house stackup simulation

---

## 4. Material Selection

### 4.1 Base Material Requirements

| Parameter | Requirement | Rationale |
|-----------|-------------|-----------|
| Material Type | FR4 (high-Tg) or equivalent | Automotive temperature range |
| Glass Transition (Tg) | >= 170C | Reflow soldering, -40 to +85C operation |
| Decomposition Temp (Td) | >= 340C | Lead-free reflow compatibility |
| Dk (Dielectric Constant) | 4.2 to 4.5 at 1GHz | Impedance calculation baseline |
| Df (Loss Tangent) | <= 0.02 at 1GHz | Acceptable for max data rates used |
| CTE (Z-axis) | <= 3.5% (50-260C) | Via reliability |
| CAF Resistance | Pass IPC-9691A | High voltage isolation reliability |
| Flammability | UL94 V-0 | Automotive safety requirement |

### 4.2 Candidate Materials

| Material | Manufacturer | Tg | Dk | Notes |
|----------|-------------|-----|-----|-------|
| IT-180A | ITEQ | 175C | 4.2 | Cost-effective high-Tg automotive |
| Megtron 4 | Panasonic | 175C | 3.8 | Lower loss, premium option |
| TU-862 HF | TUC | 170C | 4.3 | Widely available, competitive cost |

Final material selection per fab house availability and cost optimization.

---

## 5. Copper Weight

| Layer | Copper Weight | Thickness (nominal) | Rationale |
|-------|-------------|---------------------|-----------|
| L1 (TOP) | 1 oz (35um) | 35um finished | Fine-pitch component pads, high-speed traces |
| L2 (GND1) | 1 oz (35um) | 35um | Ground plane, thermal dissipation |
| L3 (SIG1) | 0.5 oz (17um) | 17um | Inner signal, finer trace capability |
| L4 (PWR1) | 1 oz (35um) | 35um | Power distribution, current handling |
| L5 (PWR2) | 1 oz (35um) | 35um | Power distribution, current handling |
| L6 (SIG2) | 0.5 oz (17um) | 17um | Inner signal, finer trace capability |
| L7 (GND2) | 1 oz (35um) | 35um | Ground plane, thermal dissipation |
| L8 (BOT) | 1 oz (35um) | 35um | Power routing, component pads |

---

## 6. Dielectric Thickness Targets

| Dielectric Layer | Between | Thickness Target | Notes |
|-----------------|---------|------------------|-------|
| Prepreg 1 | L1-L2 | 100um (nominal) | Critical for L1 impedance control |
| Core 1 | L2-L3 | 200um | Structural core |
| Prepreg 2 | L3-L4 | 100um | |
| Core 2 | L4-L5 | 200um | Central structural core |
| Prepreg 3 | L5-L6 | 100um | |
| Core 3 | L6-L7 | 200um | Structural core |
| Prepreg 4 | L7-L8 | 100um | Critical for L8 impedance control |

**Total Board Thickness Target:** 1.6mm +/- 10%

Note: Exact dielectric values to be refined with fab house stackup simulation to hit
impedance targets. Above values are starting points for simulation.

---

## 7. Via Specifications

| Via Type | Drill Size | Pad Size | Application |
|----------|-----------|----------|-------------|
| Through-hole (standard) | 0.25mm | 0.50mm | General signal, ground stitching |
| Through-hole (power) | 0.35mm | 0.65mm | Power rail connections |
| Micro-via (if needed) | 0.10mm | 0.25mm | BGA/fine-pitch escape (SOM area) |

### Via Constraints

- Minimum via-to-via spacing: per fab house DFM rules
- Ground stitching vias: placed at regular intervals around high-speed routes
- No vias within differential pair routing (transition between layers at endpoints only)
- Thermal vias under power pads: minimum 4 per exposed pad

---

## 8. Surface Finish

| Option | Application | Notes |
|--------|-------------|-------|
| ENIG (recommended) | Production boards | RoHS compliant, flat surface, good shelf life |
| HASL (lead-free) | Prototype only | Lower cost, less flat |
| OSP | Alternative | Shorter shelf life, limited reflow cycles |

**Selected: ENIG** for production (flat pad surface required for fine-pitch QFN/QFP).

---

## 9. Stackup Validation

Before PCB fabrication, the following must be verified:

1. Fab house confirms impedance targets achievable with proposed stackup
2. Impedance test coupons included on production panel
3. Cross-section analysis performed on first-article samples
4. TDR measurement on controlled-impedance test traces

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1.0 | 2024-01-15 | -- | Initial stackup definition for 8-layer board |

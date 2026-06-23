# ADVIS PCB Assembly Procedure

| Field | Value |
|-------|-------|
| Document ID | ADVIS-MFG-ASM-001 |
| Version | 0.1 |
| Status | Draft |
| Author | Manufacturing Engineering Team |
| Date | 2024-01-15 |
| Classification | CONFIDENTIAL |

---

## 1. Scope

This document defines the PCB assembly procedure for the ADVIS ECU, covering solder paste application through final assembly verification. The process uses lead-free (SAC305) surface-mount technology with selective soldering for through-hole connectors.

## 2. Assembly Overview

### 2.1 Process Flow

```
  +----------+    +---------+    +-----------+    +--------+    +--------+
  | Solder   | -> | Comp.   | -> | Reflow    | -> | AOI    | -> | X-ray  |
  | Paste    |    | Place   |    | Solder    |    | Insp.  |    | (BGA/  |
  | Print    |    | (SMT)   |    |           |    |        |    |  QFN)  |
  +----------+    +---------+    +-----------+    +--------+    +--------+
                                                                     |
                                                                     v
  +----------+    +---------+    +-----------+    +--------+    +--------+
  | Final    | <- | Conformal| <- | Selective | <- | THT    | <- | Visual |
  | Assembly |    | Coat    |    | Solder    |    | Insert |    | Insp.  |
  | (Housing)|    | (opt.)  |    | (connectors)|  |        |    |        |
  +----------+    +---------+    +-----------+    +--------+    +--------+
                                                                     |
                                                                     v
                                                               +--------+
                                                               | ICT /  |
                                                               | Func.  |
                                                               | Test   |
                                                               +--------+
```

### 2.2 Board Characteristics

| Parameter | Value |
|-----------|-------|
| PCB layers | [8-12 layers, per stackup definition] |
| Board dimensions | [TBD per mechanical design] |
| Surface finish | ENIG (Electroless Nickel Immersion Gold) |
| Solder mask | Green, LPI (Liquid Photo-Imageable) |
| Panel format | [TBD - 2-up or 4-up panelization] |
| Fiducial marks | 3 global + local fiducials per fine-pitch IC |

## 3. Solder Paste Application

### 3.1 Stencil Specification

| Parameter | Specification |
|-----------|---------------|
| Material | Laser-cut stainless steel |
| Thickness | 100 um (standard) / 120 um (for large thermal pads) |
| Aperture reduction | Per IPC-7525 guidelines |
| Fiducial recognition | Machine-vision aligned |
| Cleaning interval | Every 5 prints (underside wipe) |
| Replacement criteria | > 50,000 prints or visible wear |

### 3.2 Solder Paste Requirements

| Parameter | Specification |
|-----------|---------------|
| Alloy | SAC305 (Sn96.5/Ag3.0/Cu0.5) |
| Type | Type 4 (20-38 um particle size) for fine-pitch |
| Flux classification | ROL0 or ROL1 (per J-STD-004) |
| Shelf life | Per manufacturer specification (refrigerated) |
| Working life (after opening) | 24 hours maximum at 25C |
| Viscosity | 850-1050 kcps (Malcom viscometer) |

### 3.3 Print Parameters

| Parameter | Target | Tolerance |
|-----------|--------|-----------|
| Print speed | 40-60 mm/s | Per paste recommendation |
| Squeegee pressure | 3-5 kg | Adjust for full pad coverage |
| Separation speed | 1-3 mm/s | Slow for fine-pitch |
| Stencil gap | 0 mm (contact print) | - |
| Print direction | Consistent (unidirectional preferred) | - |

### 3.4 SPI (Solder Paste Inspection)

100% inspection after paste print:

| Measurement | Specification | Action on Fail |
|-------------|---------------|----------------|
| Volume | 80% - 130% of nominal | Rework or reject |
| Height | 75% - 125% of stencil thickness | Rework or reject |
| Area | 70% - 130% of aperture | Rework or reject |
| Position offset | < 25% of pad width | Rework or reject |
| Bridging detection | No bridges between adjacent pads | Clean and reprint |

## 4. Component Placement

### 4.1 Placement Sequence

| Order | Component Group | Machine | Speed |
|-------|-----------------|---------|-------|
| 1 | Chip components (0402, 0603) | High-speed mounter | 40,000 CPH |
| 2 | Passive components (0805+) | High-speed mounter | 40,000 CPH |
| 3 | SOICs, QFPs | Precision mounter | 15,000 CPH |
| 4 | Fine-pitch (QFN, BGA) | Precision mounter | 8,000 CPH |
| 5 | Large ICs (DS90UB954, power modules) | Precision mounter | 5,000 CPH |
| 6 | SoM connector (high pin count) | Precision mounter | Manual verify |
| 7 | Odd-form / large connectors | Manual or selective | As needed |

### 4.2 Critical Component Placement Requirements

| Component | Placement Accuracy | Special Requirements |
|-----------|-------------------|--------------------|
| DS90UB954-Q1 (QFN-64) | +/- 50 um | Paste-in-pad for exposed pad; X-ray verify |
| BMI088 (LGA-16) | +/- 50 um | Orientation critical (dot marker) |
| LM61460-Q1 (HTSSOP-20) | +/- 75 um | Exposed pad thermal connection |
| TDA4VM SoM connector | +/- 50 um | High pin count; verify all pins seated |
| NEO-M9N (LCC) | +/- 100 um | Ground pad connection critical for RF |
| USB-C connector | +/- 100 um | Shield tab alignment |

### 4.3 Moisture Sensitivity Level (MSL)

| Component | MSL Level | Floor Life (at < 30C/60%RH) | Action if Exceeded |
|-----------|-----------|-----------------------------|--------------------|
| DS90UB954-Q1 | MSL-3 | 168 hours | Bake 24h at 125C |
| BMI088 | MSL-3 | 168 hours | Bake 24h at 125C |
| LM61460-Q1 | MSL-3 | 168 hours | Bake 24h at 125C |
| NEO-M9N | MSL-3 | 168 hours | Bake 24h at 125C |
| SoM module | [Per SoM spec] | [Per SoM spec] | Per manufacturer guide |

## 5. Reflow Soldering

### 5.1 Reflow Profile (Lead-Free SAC305)

```
  Temperature (C)
  260 |                          ___
      |                         /   \        Peak: 245C +5/-0
  245 |......................../.....\....... (max 245-250C)
      |                      /       \
  220 |....................../.........\...... Liquidus (217C)
  217 |                   /|   TAL    |\
      |                  / |  60-90s  | \
  200 |................./..|...........|..\...
      |               /   |           |   \
  150 |............../....|...........|....\..  Soak zone
      |             /     |           |     \   (150-200C)
      |            / Soak |           |      \  (60-120s)
  100 |.........../  zone |           |       \.........
      |          /        |           |
   25 |_________/         |           |_________________
      0    60   120  180  210  240  270  300  360  420
                        Time (seconds)
```

### 5.2 Reflow Profile Limits

| Zone | Parameter | Minimum | Maximum |
|------|-----------|---------|---------|
| Preheat | Ramp rate | 1.0 C/s | 3.0 C/s |
| Soak | Temperature | 150C | 200C |
| Soak | Duration | 60 s | 120 s |
| Reflow | Ramp to peak | 1.0 C/s | 3.0 C/s |
| Reflow | Peak temperature | 240C | 250C |
| Reflow | Time above liquidus (TAL) | 60 s | 90 s |
| Cooling | Ramp rate | -2.0 C/s | -6.0 C/s |
| Overall | Total profile time | 300 s | 480 s |

### 5.3 Reflow Atmosphere

| Parameter | Specification |
|-----------|---------------|
| Atmosphere | Nitrogen (N2) |
| O2 concentration | < 1000 ppm (target < 500 ppm) |
| Purpose | Reduce oxidation, improve wetting, minimize voiding |

## 6. Inspection Criteria

### 6.1 Automated Optical Inspection (AOI)

100% inspection post-reflow:

| Defect Type | Detection Method | Accept/Reject |
|-------------|-----------------|---------------|
| Missing component | Presence check | Reject |
| Wrong component | Value/marking recognition | Reject |
| Tombstone | Height measurement | Reject |
| Solder bridge | Pattern recognition | Reject |
| Insufficient solder | Fillet inspection | Reject |
| Component rotation | Orientation check | Reject (> 5 deg) |
| Polarity (ICs, caps, diodes) | Marking/pin 1 detection | Reject |

### 6.2 X-Ray Inspection

Required for hidden-joint components:

| Component | Inspection Criteria | Accept Level |
|-----------|--------------------|-|
| DS90UB954-Q1 (QFN exposed pad) | Voiding in thermal pad | < 25% void area |
| BMI088 (LGA) | Pad coverage | > 75% wet area per pad |
| LM61460-Q1 (exposed pad) | Voiding | < 30% void area |
| SoM connector (if BGA) | All balls connected | 100% coverage |
| USB-C shield tabs | Solder coverage | > 80% tab area |

### 6.3 Visual Inspection Criteria (IPC-A-610 Class 3)

ADVIS assemblies are inspected to IPC-A-610 Class 3 (high-reliability electronic assemblies):

| Feature | Class 3 Requirement |
|---------|---------------------|
| Solder fillet (gull-wing) | Toe, heel, and side fillets present |
| Solder fillet (chip component) | End cap coverage > 75% height |
| Solder balls | None > 0.13 mm diameter |
| Flux residue | Clean (if no-clean flux: residue acceptable if non-conductive) |
| Marking legibility | Component values readable |
| Board cleanliness | No contamination visible at 4x |

## 7. Selective Soldering (Through-Hole Components)

### 7.1 Components Requiring Selective Solder

| Component | Type | Reason for THT |
|-----------|------|----------------|
| Power input connector | Through-hole | Mechanical strength for harness |
| CAN bus connector | Through-hole | Mechanical strength |
| Camera connectors | Through-hole / press-fit | Vibration resistance |
| Mounting hardware | Through-hole | Structural |

### 7.2 Selective Solder Parameters

| Parameter | Specification |
|-----------|---------------|
| Solder alloy | SAC305 (same as SMT) |
| Pot temperature | 260C - 270C |
| Contact time | 3 - 5 seconds |
| Preheat (bottom) | 100C - 130C board temperature |
| Flux | Low-residue, halide-free |
| Nozzle type | Component-specific tooling |

## 8. Cleaning

### 8.1 Cleaning Requirements

| Process | Method | Criteria |
|---------|--------|----------|
| Post-reflow (if required) | Aqueous wash or vapor degrease | Ionic contamination < 1.56 ug/cm^2 NaCl equiv. |
| Post-selective solder | Local cleaning if flux residue visible | Visual inspection |
| Pre-conformal coat | Full board wash | ROSE test pass |

### 8.2 Ionic Contamination Testing

| Method | Specification | Frequency |
|--------|---------------|-----------|
| ROSE (Resistivity of Solvent Extract) | < 1.56 ug NaCl equiv./cm^2 | 1 per lot (minimum) |
| Ion chromatography | Per IPC-TM-650, 2.3.28 | Weekly (production) |
| SIR (Surface Insulation Resistance) | > 100 Mohm at 85C/85%RH/100V | Qualification only |

## 9. Conformal Coating (If Applicable)

### 9.1 Coating Requirements

*Note: Conformal coating applicability depends on OEM enclosure design and environmental protection requirements.*

| Parameter | Specification |
|-----------|---------------|
| Material | Acrylic (AR) or silicone (SR) per IPC-CC-830 |
| Thickness | 25 - 75 um (per material recommendation) |
| Coverage | All SMT components; mask connectors and test points |
| Cure | UV or thermal per material specification |
| Inspection | UV fluorescence (100% visual) |

### 9.2 Keep-Out Areas (No Coating)

| Area | Reason |
|------|--------|
| Connectors (all) | Mating surface must remain clean |
| Test points (ICT) | Probe access required |
| Thermal interface areas | Thermal conductivity path |
| Mounting holes | Mechanical contact |
| Switches / jumpers (if any) | Operational access |

## 10. Final Assembly

### 10.1 Mechanical Assembly Steps

| Step | Operation | Torque/Force | Verification |
|------|-----------|-------------|--------------|
| 1 | Install thermal interface material (TIM) | N/A | Coverage check |
| 2 | Mount PCB in enclosure (if applicable) | [TBD] Nm | Torque wrench |
| 3 | Connect internal cables (if any) | Hand force | Latch engagement |
| 4 | Install camera lens covers (if included) | N/A | Visual |
| 5 | Apply labels (serial, regulatory) | N/A | Barcode scan verify |
| 6 | Final closure | [TBD] Nm | Torque wrench |

### 10.2 Traceability

| Data | Method | Storage |
|------|--------|---------|
| PCB serial number | Laser-marked on board | MES database |
| Assembly date/time | MES timestamp | MES database |
| Component lot codes (critical) | Barcode scan at placement | MES database |
| Test results | Automated data collection | MES database |
| Operator ID | Badge scan at each station | MES database |
| Firmware version (programmed) | Flash log | MES database |

## 11. Process Control

### 11.1 SPC Requirements

| Parameter | Control Method | Cp/Cpk Target |
|-----------|---------------|---------------|
| Solder paste volume (SPI) | X-bar/R chart | Cpk >= 1.33 |
| Reflow peak temperature | Individual/Moving Range | Cpk >= 1.67 |
| Reflow TAL | Individual/Moving Range | Cpk >= 1.33 |
| Placement accuracy (X,Y) | X-bar/R chart | Cpk >= 1.67 |
| AOI false call rate | P-chart | < 5% |
| First-pass yield | P-chart | >= 98% |

### 11.2 Process Change Control

Any change to the assembly process requires:
1. Engineering Change Order (ECO) approval
2. First Article Inspection (FAI) per AS9102 (3 units minimum)
3. Process capability study (30 units minimum)
4. Customer notification (if PPAP-controlled)

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | 2024-01-15 | Manufacturing Engineering Team | Initial draft |

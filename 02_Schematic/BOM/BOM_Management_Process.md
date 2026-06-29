# ADVIS BOM Management Process

**Document ID:** ADVIS-BOM-PROC-001  
**Version:** 0.1.0  
**Status:** Draft  
**Last Updated:** 2024-01-15

---

## 1. Purpose

This document defines the lifecycle management process for the ADVIS Bill of Materials,
from initial seed through production release and ongoing maintenance. It establishes
rules for component selection, variant handling, alternate sourcing, and obsolescence
management to ensure uninterrupted production availability.

---

## 2. BOM Lifecycle Phases

```
+----------+     +-------------+     +-----------+     +------------+
|  Seed    | --> | Development | --> | Validated | --> | Production |
|  BOM     |     |    BOM      |     |    BOM    |     |   BOM      |
+----------+     +-------------+     +-----------+     +------------+
     |                 |                   |                  |
  Key ICs         Full passive        Sample builds      Released to
  identified      values defined      verified            CM/EMS
```

### Phase Definitions

| Phase | Entry Criteria | Exit Criteria | Owner |
|-------|---------------|---------------|-------|
| Seed BOM | Architecture complete | All active ICs identified with MPN | HW Architect |
| Development BOM | Schematic capture started | All components have values, packages, MPNs | Schematic Designer |
| Validated BOM | Prototype build complete | All components verified on hardware | HW Test Engineer |
| Production BOM | DVT sign-off | Full AVL qualification, alternates confirmed | Production Engineer |

---

## 3. Component Selection Rules

### 3.1 Mandatory Requirements

1. **Automotive Qualification**: All components must be AEC-Q100 (ICs) or AEC-Q200 (passives)
2. **Temperature Range**: -40C to +125C junction (or +85C ambient per thermal analysis)
3. **Voltage Derating**: Minimum 50% derating on capacitor voltage rating
4. **Current Derating**: Maximum 80% of rated current for inductors and fuses
5. **Lifecycle Status**: Only "Active" or "NRND with 5+ year supply commitment" parts allowed
6. **Package Availability**: Minimum 2 distributor sources required

### 3.2 Preferred Vendor Strategy

- Power management: Texas Instruments (primary), Analog Devices (secondary)
- Interface ICs: Texas Instruments (primary)
- GNSS: u-blox (single-source, monitored)
- MEMS: Bosch Sensortec (primary), STMicroelectronics (secondary)
- Passives: Murata, Samsung EM, Yageo (multi-source)
- Connectors: TE Connectivity, Molex, Amphenol (application-specific)

---

## 4. Variant Handling

### 4.1 Product Tier Variants

The ADVIS v0.4.4 SOM-based platform supports three product tiers from a single carrier PCB design (carrier board is SoC-agnostic because the SoC resides on the SoM). For the v0.5 direct-SoC architecture, PCB commonality is a decision output of the pinout compatibility analysis (see OD-003), not an assumption:

| Tier | Target Application | BOM Strategy |
|------|-------------------|--------------|
| Entry (Assist) | Basic forward ADAS | DNI: GNSS, IMU, IR header |
| Mid (Control) | Full ADAS + DMS | Full BOM populated |
| High (Fusion) | Sensor fusion + logging | Full BOM + high-grade passives |

### 4.2 DNI Implementation Rules

1. DNI components MUST have pads on PCB (no PCB variant needed)
2. DNI resistors: populate 0-ohm jumper OR leave empty per variant
3. DNI ICs: leave completely unpopulated, decoupling caps also DNI
4. Assembly house receives tier-specific DNI list per production order
5. Test procedures account for DNI variants (no false failures)

### 4.3 SoC Variant Handling

The carrier board BOM is SoC-agnostic. SoM selection does not change carrier BOM.
Interface compatibility is handled through:
- Level shifters (if voltage domain differs)
- 0-ohm configuration resistors for pin-mux options
- DNI alternate pull-up/pull-down networks

---

## 5. Alternate Sourcing Rules

### 5.1 Second-Source Requirements

| Component Type | Second Source Required? | Criteria |
|---------------|----------------------|----------|
| Custom/Sole-source IC | No (monitor lifecycle) | Must have 5-year availability commitment |
| Standard IC (regulator, supervisor) | Yes | Pin-compatible or functional equivalent |
| Passive components | Yes | Same value, package, rating from different mfr |
| Connectors | Case-by-case | Mating compatibility critical |

### 5.2 Alternate Qualification Process

1. Identify candidate alternate (same or equivalent specifications)
2. Verify pin compatibility and parametric equivalence
3. Simulate in critical circuits (power loop, filter response)
4. Build minimum 5 units with alternate for bench validation
5. Document in BOM "Alternate PN" column
6. Notify CM/EMS of approved alternate list

---

## 6. Obsolescence Monitoring

### 6.1 Monitoring Process

- Quarterly lifecycle check on all active BOM components
- Subscribe to Product Change Notifications (PCN) from all vendors
- Flag any component entering "Not Recommended for New Design" (NRND) status
- Trigger last-time-buy evaluation when End-of-Life (EOL) announced

### 6.2 Risk Classification

| Risk Level | Criteria | Action |
|------------|----------|--------|
| Low | Multiple sources, high-volume commodity | Annual review |
| Medium | Single-source but active lifecycle | Quarterly review, identify alternates |
| High | NRND status or sole-source specialty IC | Immediate alternate search, consider redesign |
| Critical | EOL announced, no alternate exists | Last-time-buy calculation, redesign initiation |

### 6.3 Last-Time-Buy Calculation

```
LTB Quantity = (Annual Demand x Remaining Product Years) x 1.3 safety factor
             + Prototype/Development reserve (50 units minimum)
             + Field repair reserve (5% of total)
```

---

## 7. BOM Configuration Management

### 7.1 Version Control

- BOM versioned alongside schematic (same revision letter)
- Every schematic change that affects component values/types increments BOM version
- BOM stored in version control alongside design files
- Production releases tagged with date-stamped export

### 7.2 Change Control

| Change Type | Approval Required | Examples |
|-------------|-------------------|----------|
| Value change (passive) | Peer review | Capacitor value adjustment |
| Component swap (same function) | HW Lead + Test verification | Different regulator part number |
| New component addition | Design review + BOM review | Adding debug header |
| Component removal | Architecture review | Removing unused interface |

---

## 8. BOM Export Formats

| Format | Audience | Contents |
|--------|----------|----------|
| Markdown (this repo) | Engineering team | Full BOM with design notes |
| CSV | EMS/CM procurement | RefDes, MPN, Qty, Alternate PN |
| Pick-and-Place | Assembly house | RefDes, X/Y, Rotation, Side, MPN |
| Centroid | SMT machine | Machine-readable placement data |

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1.0 | 2024-01-15 | -- | Initial BOM management process definition |

# ADVIS Hardware Platform - Version History

## Version Numbering Scheme

```
Format: v{MAJOR}.{MINOR}.{PATCH}

MAJOR (0): Pre-production development phase
MINOR: Significant design milestone advancement
PATCH: Incremental refinement within a milestone

Release States:
  - Draft: Working document, not baselined
  - Baselined: Formally reviewed and approved
  - Locked: No changes without ECO approval
  - Superseded: Replaced by newer version
```

---

## Version Register

| Version | Date | Status | Phase | Approval |
|---------|------|--------|-------|----------|
| v0.1.0 | January 2026 | Superseded | Concept | Hardware Lead |
| v0.2.0 | February 2026 | Superseded | Architecture Exploration | Hardware Lead + Systems |
| v0.3.0 | March 2026 | Superseded | Component Selection | Hardware Lead + Systems |
| v0.3.5 | April 2026 | Superseded | Interface Definition | Hardware Lead + Firmware |
| v0.4.0 | May 2026 | Superseded | Near-Final Architecture | Hardware Lead + Systems + Safety |
| v0.4.4 | June 2026 | **LOCKED** | A-Sample Baseline | Full Review Board |

---

## Detailed Version History

### v0.1.0 - Initial Concept Exploration

| Field | Value |
|-------|-------|
| **Date** | January 2026 |
| **Author** | Hardware Lead |
| **Approver** | Hardware Lead |
| **Status** | Superseded by v0.2.0 |

**Scope of Changes:**
- Project initiated as vehicle-mounted ADAS + DMS edge compute ECU
- Target market defined: OEM Tier-1 supply and aftermarket fleet safety
- Core functional requirements captured from initial OEM discussions
- Preliminary form factor and environmental requirements established
- Three-tier product concept proposed (Entry / Mid / High)
- Safety philosophy established: ADVIS does not directly actuate brake, steering, throttle or powertrain; generates safety-supervised actuation requests only
- Patent strategy initiated (two initial invention disclosures identified)
- Initial cost targets set per product tier
- Decision: combined ADAS+DMS in single ECU
- Decision: Linux-based software stack for AI/ML workloads

**Key Deliverables:**
- System requirements document (draft)
- Preliminary block diagram (conceptual)
- Market positioning and product family definition

---

### v0.2.0 - Architecture Exploration

| Field | Value |
|-------|-------|
| **Date** | February 2026 |
| **Author** | Hardware Lead, Systems Architect |
| **Approver** | Hardware Lead, Systems Engineer |
| **Status** | Superseded by v0.3.0 |

**Scope of Changes:**
- SoC candidate evaluation completed (TDA4VM, AM68A, SA8295, S32V, V3H)
- TDA4VM/AM68A class selected as mid-tier baseline
- Phytec phyCORE-AM68A SOM selected as compute module platform
- Two-track hardware strategy formalized:
  - Track 1: Compact production module (cost-down path)
  - Track 2: Modular IP platform (OEM-configurable, current focus)
- Camera interface architecture options evaluated
- FPD-Link III selected for Track 2 (cable length, PoC capability)
- Power architecture options identified (4 candidates)
- Product family formally defined: Assist, Control, Fleet, Fusion
- SoC tier structure established: AM62A (Entry), AM68A/TDA4VM (Mid), TDA4VH (High)
- SOM-based approach confirmed (vs custom SoC board)

**Key Deliverables:**
- SoC selection trade study (TN-002)
- Camera architecture analysis (TN-003)
- Preliminary system block diagram
- Product variant definitions

---

### v0.3.0 - Key Component Selections

| Field | Value |
|-------|-------|
| **Date** | March 2026 |
| **Author** | Hardware Lead, Power Electronics Engineer |
| **Approver** | Hardware Lead, Systems Engineer |
| **Status** | Superseded by v0.3.5 |

**Scope of Changes:**
- All critical-path active components selected with manufacturer part numbers:
  - DS90UB954-Q1: Dual FPD-Link III deserializer
  - LM61460-Q1: Primary buck converter (12V to 5V, 6A)
  - TPS62130A-Q1: Secondary buck (5V to 3.3V, 3A)
  - TLV75518-Q1: LDO (3.3V to 1.8V, 500mA)
  - TPS3808G33-Q1: Voltage supervisor
  - TPS3431-Q1: External watchdog timer
  - TCAN1044AV-Q1: CAN-FD transceiver
  - NEO-M9N-00B: Multi-constellation GNSS receiver
  - BMI088: 6-axis automotive IMU
- Power architecture trade study completed and documented
- Discrete cascaded topology selected over integrated PMIC
- 80V PMOS reverse-polarity protection topology defined
- Input protection strategy finalized (fuse + TVS + PMOS)

**Key Deliverables:**
- Power architecture trade study (TN-001)
- Component selection summary with justification
- Preliminary BOM (active components)
- Vendor engagement initiated for key parts

---

### v0.3.5 - Interface Definitions

| Field | Value |
|-------|-------|
| **Date** | April 2026 |
| **Author** | Hardware Lead, Firmware Lead |
| **Approver** | Hardware Lead, Firmware Lead |
| **Status** | Superseded by v0.4.0 |

**Scope of Changes:**
- All SOM-to-peripheral interfaces fully defined:
  - I2C address map (DS90UB954=0x30, NEO-M9N=0x42)
  - SPI bus assignment for BMI088 (dual CS architecture)
  - UART assignments (debug console, GNSS data)
  - GPIO map for control/status signals
- Ground domain strategy defined:
  - PGND (power stage)
  - DGND (digital logic)
  - AGND (analog/RF)
  - Star-point interconnection topology
- GNSS interface: UART primary, I2C secondary, 1PPS timing output
- FPD-Link III virtual channel mapping: VC0=Forward, VC1=DMS
- Antenna bias-T topology for active GNSS antenna defined
- Camera PoC specifications confirmed

**Key Deliverables:**
- Interface Control Document (ICD) drafts
- SOM signal map (all allocated pins)
- Ground domain architecture diagram
- I2C/SPI address allocation table

---

### v0.4.0 - Near-Final Architecture

| Field | Value |
|-------|-------|
| **Date** | May 2026 |
| **Author** | Hardware Lead, Safety Engineer |
| **Approver** | Hardware Lead, Systems Engineer, Safety Lead |
| **Status** | Superseded by v0.4.4 |

**Scope of Changes:**
- Safety boundary formally documented and approved:
  - ADVIS does not directly actuate brake, steering, throttle or powertrain
  - ADVIS Assist provides warning/advisory outputs
  - ADVIS Control may generate safety-supervised actuation request messages over CAN/CAN-FD
- ASIL decomposition analysis completed
- Reset/watchdog topology finalized:
  - TPS3808G33 supervisor monitors 3V3_IO
  - TPS3431 watchdog with SOM_BOOT_OK gating
  - Boot-aware enable prevents reset loops
- CAN transceiver mode locked: Normal Mode (STB=LOW)
- TXD recessive pull-up strategy (10k to 3V3_CAN)
- USB-C device mode confirmed (5.1k CC pull-downs)
- MicroSD interface added for field diagnostics
- Debug UART access point defined (3-pin header, 115200 baud)
- Automotive Ethernet deferred to High tier / future phase

**Key Deliverables:**
- Safety concept document
- Reset/watchdog architecture diagram
- Updated system block diagram
- Interface specification updates

---

### v0.4.4 - Architecture Lock / A-Sample Baseline

| Field | Value |
|-------|-------|
| **Date** | June 2026 |
| **Author** | Hardware Team |
| **Approver** | Full Review Board (Hardware, Systems, Safety, Firmware, Program) |
| **Status** | **LOCKED** |

**Scope of Changes:**
- Architecture formally locked via Concept Design Review
- Consolidated handoff document finalized (authoritative technical reference)
- All component selections baselined with verified part numbers
- Power sequencing strategy locked (cascaded EN/PG chain)
- Connector pinout intent documented (pending mechanical validation)
- Complete SOM signal map with all GPIO assignments
- Ground domain star-point locations defined
- IR daughterboard interface specification complete
- Open items list formalized with owners and due dates
- Design review record created with all decision rationale
- Version history and configuration management established
- ECO process defined for future changes to locked items

**Key Deliverables:**
- Consolidated Hardware Handoff Document
- Architecture Review Record (signed)
- Open Items Tracker
- Full BOM (active + passive components)
- Design review sign-off

**Lock Criteria Met:**
- All major component selections validated
- Power budget analysis: adequate margin (25W budget, ~18W estimated)
- SI feasibility confirmed for CSI-2 at 1.6Gbps/lane
- Thermal analysis: passive cooling feasible for mid-tier
- No critical open issues at architecture level
- Cost estimate within mid-tier BOM target

---

## Next Planned Version

### v0.5.0 - Schematic Complete (Target: TBD)

**Planned Scope:**
- ERC-clean schematic (all sheets)
- Final BOM with all passive values
- Netlist generation
- Schematic Design Review (SDR) gate passage

---

*ADVIS Hardware Platform - Configuration Management*

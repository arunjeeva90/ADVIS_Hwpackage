# ADVIS Exact Part Verification Rules

**Classification:** CONFIDENTIAL - ENGINEERING USE ONLY  
**Status:** ACTIVE - Mandatory for all SoC/component specification entries  
**Version:** v1.1 - June 2026  
**Document ID:** TN-005

---

## 1. Purpose

This document establishes verification discipline rules for all component specifications used in ADVIS design documents. These rules prevent specification errors caused by:

- Confusing family-level marketing text with orderable-part specifications
- Using community forum posts or third-party summaries as authoritative sources
- Assuming that a family-level capability applies equally to all variants within that family
- Treating "up to" values as confirmed values for a specific orderable part

---

## 2. Core Verification Principles

### Principle 1: Product Headline Is the Primary Reference

The TI product page headline for a specific orderable part number is the most reliable publicly available specification source. If the product headline states a value, that value takes precedence over family-level text for conservative planning purposes.

### Principle 2: Family-Level Text Does Not Confirm Part-Level Specs

Text that applies to an entire product family (e.g., "J721S2 family" or "TDA4VE/TDA4AL/TDA4VL") may describe the maximum capability across all variants. It does not confirm that every variant in the family achieves that maximum.

### Principle 3: Ambiguity Requires Explicit Documentation

When a conflict exists between the product headline and family-level text for any specification, the conflict must be documented explicitly in design documents. The conservative value (product headline) must be used for planning until resolved.

### Principle 4: Only Official Sources Are Acceptable

Acceptable sources (in priority order):
1. Official TI datasheet (orderable-part-specific tables)
2. Official TI product page headline and key features
3. Official TI family technical reference manual (with part-specific applicability noted)
4. TI FAE written confirmation (email or formal response)
5. TI E2E official forum responses from TI employees (with caveats)

Unacceptable sources:
- Third-party blogs or review sites
- Community forum posts (non-TI employees)
- Distributor marketing pages
- Competitor comparison tables
- Conference presentations (unless citing specific datasheets)
- AI-generated summaries

### Principle 5: Every Numerical Spec Needs a Source Tag

All numerical specifications in ADVIS SoC selection documents must include:
- The source type (product page, datasheet table, family TRM, FAE confirmation)
- Confidence level (HIGH = part-specific confirmed, MEDIUM = family text with reasonable applicability, LOW = inferred or estimated)
- Whether the value is confirmed for the specific orderable part number

---

## 3. Verification Checklist for New SoC Entries

Before adding or updating any SoC specification in ADVIS documents:

| Step | Action | Pass Criteria |
|------|--------|---------------|
| 1 | Identify the exact orderable part number (e.g., TDA4VL-Q1, not "TDA4VL family") | Specific -Q1 or equivalent automotive variant identified |
| 2 | Locate the official product page for that exact part | URL documented, page accessed and confirmed current |
| 3 | Record the product headline verbatim | Headline copied character-for-character |
| 4 | For each spec, identify whether source is part-specific or family-level | Each spec tagged with source type |
| 5 | If family-level text contradicts product headline, flag as AMBIGUOUS | Conflict documented with both values |
| 6 | Use product headline value as conservative planning value | Conservative value explicitly stated |
| 7 | Create resolution action item in OD register if ambiguity affects design decisions | OD entry created with TI FAE action |

---

## 4. Known Ambiguities Register

| Part | Specification | Product Headline Value | Family Text Value | Status | Resolution Owner |
|------|--------------|----------------------|-------------------|--------|-----------------|
| TDA4VL-Q1 | AI Accelerator TOPS | 4 TOPS | "MMA up to 8 TOPS (8b) at 1.0GHz" | OPEN - Ambiguous | Systems Engineering + TI FAE |
| TDA4VL-Q1 | R5F core partition | Not explicit | "Up to 4x Arm Cortex-R5F" with partition detail in family text | OPEN - Requires confirmation | Systems Engineering + TI FAE |

---

## 5. Consequences of Non-Compliance

Specifications entered without proper source verification may result in:
- Incorrect SoC selection (inaccurate TOPS budget for AI models)
- Incorrect power budget (thermal design based on inaccurate TDP)
- Incorrect safety partitioning (inaccurate R5F core count for ASIL allocation)
- PCB design rework (inaccurate pin count or package assumptions)
- Supply chain issues (ordering an unintended variant)

Source verification discipline prevents these outcomes and ensures all design decisions are based on traceable, vendor-confirmed data.

---

## 6. Process Integration

These verification rules apply to:
- All entries in ARCH-SOC-002 (SoC Selection Matrix)
- All SoC references in architecture documents
- All power budget assumptions
- All AI performance claims in product tier definitions
- All component specifications in BOM documents
- All sensor specifications (image sensors, IMU, GNSS)
- All PMIC and power component selections
- All transceiver and interface component specifications

Any engineer adding or modifying component specifications must follow this checklist before committing changes to the repository.

---

## 7. Component-Specific Verification Examples

### 7.1 Image Sensors (Forward Camera, DMS Camera)

| Verification Item | Example | Accept Criteria |
|-------------------|---------|-----------------|
| Resolution | "1936x1100" for IMX390 | Matches sensor product brief or datasheet |
| Interface | "MIPI CSI-2, 2 or 4 lanes" | Confirmed in datasheet pin table |
| HDR Mode | "DOL-HDR, up to 120dB" | Confirmed in features section, not inferred from family |
| Automotive Grade | "AEC-Q100 Grade 2" | Confirmed on product page for exact part number |
| Power | "~250 mW typical" | From datasheet typical operating conditions, not estimated |
| Frame Rate | "60 fps at full resolution (4-lane)" | Confirmed for stated lane count and resolution mode |

### 7.2 PMIC (Power Management IC)

| Verification Item | Example | Accept Criteria |
|-------------------|---------|-----------------|
| Output Rails | "5 configurable bucks + 4 LDOs" for TPS6594-Q1 | Matches datasheet block diagram |
| Sequencing | "Programmable power-up/down sequencing" | Confirmed in datasheet functional description |
| I2C/SPI Address | Specific slave address or address pin configuration | Confirmed in datasheet register map |
| PMIC-SoC Compatibility | "Supported PMIC for J721S2 family" | Confirmed in TI SoC power design guide or EVM schematic |
| Functional Safety | "Supports ASIL-D system power management" | Confirmed in PMIC safety manual |

### 7.3 CAN-FD Transceiver

| Verification Item | Example | Accept Criteria |
|-------------------|---------|-----------------|
| Data Rate | "CAN-FD up to 8 Mbps" for TCAN1044AV-Q1 | Matches datasheet maximum data rate spec |
| Supply Voltage | "4.5V to 5.5V Vcc" | Confirmed in absolute maximum ratings |
| Bus Fault Tolerance | "+/-58V bus fault" | Confirmed in datasheet electrical characteristics |
| Standby Current | Specific value in microamps | From datasheet typical/max standby current row |
| Operating Mode Pins | STB, EN pin logic levels | Confirmed in datasheet truth table |

### 7.4 Watchdog Timer

| Verification Item | Example | Accept Criteria |
|-------------------|---------|-----------------|
| Timeout Period | "Programmable 200ms to 2.5s" for TPS3431-Q1 | Matches datasheet timing table |
| Reset Pulse Width | Specific milliseconds value | From datasheet output characteristics |
| Window Mode | "Open-window or closed-window" | Confirmed in datasheet functional modes |
| Input Threshold | WDI trigger voltage levels | From datasheet electrical specifications |
| Enable Control | "EN pin or VDD ramp" | Confirmed in datasheet application section |

---

## 8. Revision History

| Rev | Date | Author | Change |
|-----|------|--------|--------|
| 1.0 | 2026-06 | Systems Engineering | Initial release; establishes verification discipline for all component specifications |
| 1.1 | 2026-06 | Systems Engineering | Expanded scope to all components (sensors, PMIC, CAN transceiver, watchdog). Added component-specific verification examples. Cleaned language to current-state professional format. |

---

*This document is mandatory for all ADVIS hardware specification activities.*

*End of Document*

# ADVIS v0.5 TDA4VL vs TDA4VM Pinout Compatibility Checklist

**Classification:** CONFIDENTIAL - ENGINEERING USE ONLY  
**Status:** PRELIMINARY - Requires vendor datasheet/NDA data to complete  
**Version:** v0.1 - June 2026  
**Document ID:** ARCH-SOC-003  
**Related Decision:** OD-003 (Single PCB vs. Dual PCB Strategy)

---

## 1. Purpose

This checklist documents the pinout compatibility analysis between TDA4VL-Q1 (770-pin FCBGA, ALZ package) and TDA4VM-Q1 (827-pin FCBGA, ALF package) to determine whether a single ADVIS v0.5 PCB design can support both SoC variants via BOM population options.

A compatible pinout would enable a single PCB revision for both ADVIS Assist (TDA4VL-Q1, 4 TOPS conservative per product headline) and ADVIS Control (TDA4VM-Q1, confirmed 8 TOPS), reducing NRE and simplifying the product platform.

---

## 2. Package Comparison Summary

| Parameter | TDA4VL-Q1 | TDA4VM-Q1 | Compatible? |
|-----------|-----------|-----------|-------------|
| Package type | FCBGA | FCBGA | Same type |
| Package designator | ALZ | ALF | Different |
| Package dimensions | 23mm x 23mm | 24mm x 24mm | **DIFFERENT - 1mm larger per side** |
| Ball pitch | 0.8mm | 0.8mm | Same |
| Ball count | 770 pins | 827 pins | Different (57 more on TDA4VM) |
| Process node | 16nm FinFET | 16nm FinFET | Same |

**Initial Assessment:** Different package size (23mm vs 24mm) and different pin count (770 vs 827) strongly suggest these are NOT pin-compatible packages. A superset footprint approach may be possible but requires detailed ball map analysis.

---

## 3. Signal Group Compatibility Checklist

The following checklist must be completed using official TI datasheet ball map data (requires NDA or published datasheet).

### 3.1 Power and Ground

| Check Item | TDA4VL-Q1 | TDA4VM-Q1 | Status |
|------------|-----------|-----------|--------|
| VDD_CORE ball positions | TBD - requires datasheet | TBD - requires datasheet | NOT VERIFIED |
| VDD_IO ball positions | TBD - requires datasheet | TBD - requires datasheet | NOT VERIFIED |
| VSS (ground) ball positions | TBD - requires datasheet | TBD - requires datasheet | NOT VERIFIED |
| LPDDR4 VDD ball positions | TBD - requires datasheet | TBD - requires datasheet | NOT VERIFIED |
| PMIC interface pins | TBD - requires datasheet | TBD - requires datasheet | NOT VERIFIED |

### 3.2 LPDDR4 Memory Interface

| Check Item | TDA4VL-Q1 | TDA4VM-Q1 | Status |
|------------|-----------|-----------|--------|
| DDR bus width | 32-bit (one bus) | 32-bit with inline ECC | Functionally similar |
| DDR data pin locations | TBD - requires datasheet | TBD - requires datasheet | NOT VERIFIED |
| DDR address/command pin locations | TBD - requires datasheet | TBD - requires datasheet | NOT VERIFIED |
| DDR clock pin locations | TBD - requires datasheet | TBD - requires datasheet | NOT VERIFIED |
| DDR termination/reference pins | TBD - requires datasheet | TBD - requires datasheet | NOT VERIFIED |

### 3.3 CSI-2 Camera Interfaces

| Check Item | TDA4VL-Q1 | TDA4VM-Q1 | Status |
|------------|-----------|-----------|--------|
| CSI-2 RX0 lane positions | TBD - requires datasheet | TBD - requires datasheet | NOT VERIFIED |
| CSI-2 RX1 lane positions | TBD - requires datasheet | TBD - requires datasheet | NOT VERIFIED |
| CSI-2 TX port positions | TBD - requires datasheet | TBD - requires datasheet | NOT VERIFIED |
| D-PHY power/reference pins | TBD - requires datasheet | TBD - requires datasheet | NOT VERIFIED |

### 3.4 CAN-FD Interface

| Check Item | TDA4VL-Q1 | TDA4VM-Q1 | Status |
|------------|-----------|-----------|--------|
| MCAN TX/RX pin locations | TBD - requires datasheet | TBD - requires datasheet | NOT VERIFIED |
| Number of MCAN instances | 20 modules | 16 modules | TDA4VL has more |

### 3.5 General Purpose I/O and Control

| Check Item | TDA4VL-Q1 | TDA4VM-Q1 | Status |
|------------|-----------|-----------|--------|
| GPIO bank locations | TBD - requires datasheet | TBD - requires datasheet | NOT VERIFIED |
| I2C controller pin locations | TBD - requires datasheet | TBD - requires datasheet | NOT VERIFIED |
| UART pin locations | TBD - requires datasheet | TBD - requires datasheet | NOT VERIFIED |
| SPI pin locations | TBD - requires datasheet | TBD - requires datasheet | NOT VERIFIED |
| Boot mode strap pins | TBD - requires datasheet | TBD - requires datasheet | NOT VERIFIED |

### 3.6 Storage Interface

| Check Item | TDA4VL-Q1 | TDA4VM-Q1 | Status |
|------------|-----------|-----------|--------|
| eMMC/SD interface pins | TBD - requires datasheet | TBD - requires datasheet | NOT VERIFIED |
| OSPI/QSPI pins | TBD - requires datasheet | TBD - requires datasheet | NOT VERIFIED |

### 3.7 Clock and Reset

| Check Item | TDA4VL-Q1 | TDA4VM-Q1 | Status |
|------------|-----------|-----------|--------|
| System clock input pins | TBD - requires datasheet | TBD - requires datasheet | NOT VERIFIED |
| POR/Reset pins | TBD - requires datasheet | TBD - requires datasheet | NOT VERIFIED |
| JTAG/Debug port pins | TBD - requires datasheet | TBD - requires datasheet | NOT VERIFIED |

---

## 4. Superset Footprint Feasibility Assessment

| Criterion | Assessment | Notes |
|-----------|------------|-------|
| Package size delta | 1mm per side (23mm vs 24mm) | PCB footprint must accommodate 24mm (larger) |
| Ball pitch identical? | Yes (both 0.8mm) | Favorable for superset approach |
| Ball grid alignment | TBD - requires overlay analysis | Critical: must check if common signals share same grid positions |
| Extra pins (TDA4VM) | 57 additional pins | Must verify these are on outer ring only |
| PCB routing impact | TBD | Larger footprint may impact board area budget |
| BGA escape routing | TBD - requires ball map | May need different via fanout for each SoC |

---

## 5. Actions Required

| # | Action | Owner | Status | Blocking |
|---|--------|-------|--------|----------|
| 1 | Obtain TDA4VL-Q1 (ALZ) datasheet with full ball map | SoC Lead / TI FAE | NOT STARTED | All pin compatibility checks |
| 2 | Obtain TDA4VM-Q1 (ALF) datasheet with full ball map | SoC Lead / TI FAE | NOT STARTED | All pin compatibility checks |
| 3 | Overlay ball maps and identify common pin positions | Layout Engineering | BLOCKED on #1, #2 | Superset feasibility |
| 4 | Identify signal groups that can share routing | SI Engineering | BLOCKED on #3 | PCB design strategy |
| 5 | Assess DDR routing compatibility (length matching) | SI Engineering | BLOCKED on #3 | Memory design |
| 6 | Determine if single BGA fanout pattern works for both | Layout Engineering | BLOCKED on #3 | Via strategy |
| 7 | Cost comparison: single superset PCB vs. two dedicated PCBs | Hardware Lead | BLOCKED on #4, #5, #6 | OD-003 decision |

---

## 6. Preliminary Recommendation

Given the different package sizes (23mm vs 24mm) and different pin counts (770 vs 827), **full pin-for-pin compatibility is unlikely**. However, a superset footprint approach may still be viable if:

1. Common signal groups (CSI-2, DDR, CAN, I2C, eMMC) share overlapping ball positions
2. The 57 additional TDA4VM pins are concentrated on the outer ring
3. Power delivery requirements can be met by a common power plane design

**Until official ball maps are obtained and overlaid, the single-PCB strategy (OD-003) cannot be resolved.**

---

## 7. Alternative Strategies if Incompatible

| Strategy | Pros | Cons |
|----------|------|------|
| Two dedicated PCB designs (one per SoC) | Optimized per SoC, smaller board possible for TDA4VL | Higher NRE (two sets of Gerbers, two qualifications) |
| Single PCB with superset footprint | One NRE, BOM-variant flexibility | May be larger than needed for TDA4VL, potential SI compromises |
| TDA4VL-only PCB, separate TDA4VM board later | Ships Assist tier faster, defers Control investment | Two PCB programs eventually needed |
| TDA4VL for both tiers (if A72@1.2GHz sufficient) | Single SoC, single PCB, maximum cost-down | May limit Control tier performance; requires benchmarking |

---

## 8. Revision History

| Rev | Date | Author | Change |
|-----|------|--------|--------|
| 0.1 | 2026-06 | Systems Engineering | Initial checklist creation; all items pending datasheet data |

---

*PRELIMINARY - This document cannot be completed without official TI datasheet ball map data. All "NOT VERIFIED" items require vendor engagement.*

*End of Document*

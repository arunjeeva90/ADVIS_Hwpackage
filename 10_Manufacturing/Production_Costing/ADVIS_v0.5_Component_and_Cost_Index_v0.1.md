# ADVIS v0.5 Component and Cost Index

**Classification:** CONFIDENTIAL - ENGINEERING USE ONLY  
**Status:** PRELIMINARY - Placeholder for vendor quotes  
**Version:** v0.1 - June 2026  
**Document ID:** MFG-COST-001

---

## 1. Purpose

This document provides a structured component and cost index for the ADVIS v0.5 Compact Module. It tracks key BOM components by category, identifies cost drivers, and establishes a framework for production cost estimation as vendor quotes and volume pricing are obtained.

**Note:** Actual pricing is highly sensitive to volume, contract terms, and market conditions. This document uses relative cost classes ($, $$, $$$) until vendor quotes are obtained. No specific dollar amounts are listed without confirmed quotes.

---

## 2. Cost Tier Definitions

| Tier | Description | Target Volume |
|------|-------------|---------------|
| ADVIS Assist (entry) | Lowest BOM cost, TDA4VL-Q1, cost-optimized sensors | 100k+ units/year |
| ADVIS Assist (premium) | TDA4VL-Q1 with premium forward sensor | 50k+ units/year |
| ADVIS Control | Higher-performance SoC (TDA4VM-Q1), premium sensors | 20k+ units/year |
| Single-Camera DMS | AM62A7, single DMS sensor, lowest cost | 200k+ units/year |

---

## 3. Component Cost Index by Category

### 3.1 SoC and Compute

| Component | Part Number | Tier(s) | Cost Class | Volume Pricing Status | Notes |
|-----------|-------------|---------|------------|----------------------|-------|
| SoC (Assist) | TDA4VL-Q1 | Assist (entry/premium) | $$ | NOT QUOTED - requires TI engagement | 770-pin FCBGA, J721S2 family |
| SoC (Control) | TDA4VM-Q1 | Control | $$$ | NOT QUOTED - requires TI engagement | 827-pin FCBGA, J721E family |
| SoC (Single-cam) | AM62A7-Q1 | Single-Camera | $ | NOT QUOTED - requires TI engagement | 484-pin FCBGA, lowest cost |
| LPDDR4 2GB | TBD vendor/PN | Assist (entry) | $ | NOT QUOTED | 32-bit, single die |
| LPDDR4 4GB | TBD vendor/PN | Assist (premium), Control | $$ | NOT QUOTED | 32-bit, may need dual die |
| eMMC 16GB | TBD vendor/PN | Assist (entry) | $ | NOT QUOTED | eMMC 5.1 |
| eMMC 32GB | TBD vendor/PN | Assist (premium), Control | $ | NOT QUOTED | eMMC 5.1 |
| PMIC | TPS6594-Q1 | All TDA4x tiers | $$ | NOT QUOTED | Required for TDA4VL and TDA4VM |

### 3.2 Image Sensors

| Component | Part Number | Tier(s) | Cost Class | Volume Pricing Status | Notes |
|-----------|-------------|---------|------------|----------------------|-------|
| Forward sensor (cost) | OX03C10 (OmniVision) | Assist (entry) | $$ | NOT QUOTED | 2.5MP HDR, AEC-Q100 |
| Forward sensor (premium) | IMX390 (Sony) | Assist (premium), Control | $$$ | NOT QUOTED | 2.12MP, best night vision |
| Forward sensor (alt) | AR0233 (onsemi) | Assist (entry alt) | $$ | NOT QUOTED | 2.5MP, excellent LFM |
| DMS sensor (entry) | OX01N1B (OmniVision) | Assist (entry/premium) | $ | NOT QUOTED | 1.0MP NIR, smallest die |
| DMS sensor (control) | OX01H1B (OmniVision) | Control | $ | NOT QUOTED | 1.3MP NIR, higher resolution |
| Lens module (forward) | TBD | All dual-cam tiers | $-$$ | NOT QUOTED | Depends on FoV and quality |
| Lens module (DMS) | TBD | All dual-cam tiers | $ | NOT QUOTED | NIR-optimized, compact |

### 3.3 Power Management

| Component | Part Number | Tier(s) | Cost Class | Volume Pricing Status | Notes |
|-----------|-------------|---------|------------|----------------------|-------|
| 12V to 5V buck | LM61460-Q1 | All | $ | NOT QUOTED | Automotive buck converter |
| 5V to 3.3V buck | TPS62130A-Q1 | All | $ | NOT QUOTED | Low-noise buck |
| 3.3V to 1.8V LDO | TLV75518-Q1 | All | $ | NOT QUOTED | Low-dropout regulator |
| Sensor LDO(s) | TBD | All | $ | NOT QUOTED | 1.2V, 2.8V for sensors |
| Watchdog timer | TPS3431-Q1 | All | $ | NOT QUOTED | Boot-gated watchdog |
| Reset supervisor | TPS3808G33-Q1 | All | $ | NOT QUOTED | 3.3V rail monitor |

### 3.4 Vehicle Interface

| Component | Part Number | Tier(s) | Cost Class | Volume Pricing Status | Notes |
|-----------|-------------|---------|------------|----------------------|-------|
| CAN-FD PHY | TCAN1044AV-Q1 | All | $ | NOT QUOTED | Normal mode CAN-FD |
| Input protection (TVS) | TBD | All | $ | NOT QUOTED | Automotive TVS diode |
| Reverse polarity MOSFET | TBD | All | $ | NOT QUOTED | 80V PMOS |
| Input fuse | TBD | All | $ | NOT QUOTED | 3A automotive fuse |
| Vehicle connector (J100) | TBD | All | $ | NOT QUOTED | Sealed automotive connector |

### 3.5 IR Illumination (DMS)

| Component | Part Number | Tier(s) | Cost Class | Volume Pricing Status | Notes |
|-----------|-------------|---------|------------|----------------------|-------|
| IR LEDs (940nm) | TBD | All with DMS | $ | NOT QUOTED | 2-4 LEDs per module |
| LED driver IC | TBD (e.g., TPS92610-Q1) | All with DMS | $ | NOT QUOTED | Constant-current driver |
| IR bandpass filter | TBD | All with DMS | $ | NOT QUOTED | Optical window filter |

### 3.6 PCB and Mechanical

| Component | Description | Tier(s) | Cost Class | Volume Pricing Status | Notes |
|-----------|-------------|---------|------------|----------------------|-------|
| Main PCB | 6-8 layer, automotive grade | All | $$-$$$ | NOT QUOTED | Cost depends on layer count and HDI |
| DMS flex/rigid-flex | ~50mm, controlled impedance | All with DMS | $ | NOT QUOTED | 4-layer rigid-flex |
| Housing (plastic shell) | Injection-molded PC/ABS | All | $ | NOT QUOTED | Tooling amortized over volume |
| Housing (aluminum plate) | Die-cast or stamped aluminum | All | $ | NOT QUOTED | Thermal spreader + structural |
| Thermal interface material | Graphite or thermal pad | All | $ | NOT QUOTED | 0.5-1.0mm TIM |
| Windshield bracket | Aluminum or glass-filled nylon | All | $ | NOT QUOTED | OEM-specific variants |
| FPC connector(s) | 0.3mm or 0.5mm pitch ZIF | All with DMS | $ | NOT QUOTED | Automotive-rated |

### 3.7 Optional Components (DNI by Default)

| Component | Part Number | Tier(s) | Cost Class | Volume Pricing Status | Notes |
|-----------|-------------|---------|------------|----------------------|-------|
| GNSS module | NEO-M9N (u-blox) | Fleet/Fusion only | $$ | NOT QUOTED | DNI pads on all boards |
| IMU | BMI088 (Bosch) | Fleet/Fusion only | $ | NOT QUOTED | DNI pads on all boards |
| GNSS antenna | Active patch | Fleet/Fusion only | $ | NOT QUOTED | Integrated or U.FL |

---

## 4. Cost Driver Analysis

| Cost Driver | Impact | Mitigation Strategy |
|-------------|--------|---------------------|
| SoC selection | Largest single BOM item; TDA4VM significantly more expensive than TDA4VL | Use TDA4VL-Q1 for Assist tier (same 8 TOPS MMA at lower cost) |
| Forward image sensor | Second largest cost item; IMX390 premium over OX03C10/AR0233 | Use OX03C10 for cost-optimized Assist; reserve IMX390 for premium/Control |
| PCB layer count | 8-10 layers for TDA4VM significantly more expensive than 6-layer | TDA4VL (0.8mm pitch, 770 pins) may escape on fewer layers |
| Flex cable | Controlled-impedance rigid-flex adds cost vs. standard FPC | Minimize flex length; optimize layer count |
| Housing tooling | One-time NRE amortized over volume | Design for high-volume injection molding; minimize variants |
| PMIC (TPS6594-Q1) | Required companion IC for TDA4x family | No alternative; cost is fixed |
| SerDes elimination | Major cost reduction vs. v0.4.4 | DS90UB954 + UB953 + FAKRA connectors + coax cables eliminated |

---

## 5. Estimated BOM Cost Class by Tier

| Tier | SoC Class | Sensor Class | PCB Class | Total BOM Class | vs. v0.4.4 |
|------|-----------|-------------|-----------|-----------------|-------------|
| ADVIS Assist (entry) | $$ | $$ | $$ | $$$ | Significantly lower (no SerDes, no SOM) |
| ADVIS Assist (premium) | $$ | $$$ | $$ | $$$$ | Lower (no SerDes, no SOM) |
| ADVIS Control | $$$ | $$$ | $$$ | $$$$$ | Comparable or slightly lower |
| Single-Camera DMS | $ | $ | $ | $$ | Much lower |

*Relative cost classes only. Actual pricing requires vendor engagement at target volumes.*

---

## 6. Volume Pricing Milestones

| Milestone | Action | Owner | Status | Target Date |
|-----------|--------|-------|--------|-------------|
| TI SoC pricing inquiry | Request budgetary pricing for TDA4VL-Q1, TDA4VM-Q1, AM62A7-Q1 at 50k/100k/200k volumes | Procurement | NOT STARTED | TBD |
| Sensor pricing inquiry | Request budgetary pricing for OX03C10, IMX390, OX01N1B, OX01H1B | Procurement | NOT STARTED | TBD |
| PCB vendor RFQ | Request quotes for 6-layer and 8-layer automotive PCB at target dimensions | Procurement | NOT STARTED | TBD |
| Flex cable vendor RFQ | Request quotes for controlled-impedance rigid-flex (~50mm) | Procurement | NOT STARTED | TBD |
| Housing tooling estimate | Request injection molding tooling and piece-price estimates | Procurement | NOT STARTED | TBD |
| Full BOM cost roll-up | Compile complete BOM with all line items priced | Hardware Lead | BLOCKED on above | TBD |

---

## 7. Cost Reduction Opportunities (Future)

| Opportunity | Potential Savings | Feasibility | Risk |
|-------------|-------------------|-------------|------|
| TDA4VL for both Assist AND Control | Eliminates TDA4VM BOM variant | Requires benchmarking A72@1.2GHz for Control workloads | May limit Control tier performance |
| 6-layer PCB for Assist tier | PCB cost reduction | Feasible if TDA4VL BGA escapes on 6 layers | Requires layout feasibility study |
| Single forward sensor for all tiers | Reduces sensor qualification effort | OX03C10 adequate for all but premium night vision | May not meet premium tier night performance |
| Eliminate DMS flex (rigid-mount DMS) | Flex cable cost elimination | Requires housing redesign with DMS on main PCB | Limits optical architecture flexibility |
| AM62A7 for DMS-only module | Lowest SoC cost for single-camera | Only viable for single-camera products | Cannot do dual-camera |

---

## 8. Revision History

| Rev | Date | Author | Change |
|-----|------|--------|--------|
| 0.1 | 2026-06 | Systems Engineering | Initial cost index structure; all pricing TBD pending vendor engagement |

---

*PRELIMINARY - No actual pricing included. All cost classes are relative estimates. Vendor engagement required for production cost planning.*

*End of Document*

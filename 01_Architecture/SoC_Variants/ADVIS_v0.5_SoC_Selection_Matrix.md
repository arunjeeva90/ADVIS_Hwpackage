# ADVIS v0.5 SoC Selection Matrix

**Classification:** CONFIDENTIAL - ENGINEERING USE ONLY  
**Status:** PRELIMINARY - Subject to vendor/datasheet confirmation  
**Version:** v0.2 - June 2026  
**Document ID:** ARCH-SOC-002

---

## 1. Overview

This document provides the SoC selection decision matrix for the ADVIS v0.5 Compact Module. Unlike the v0.4.4 SOM-based architecture, the v0.5 places the SoC directly on the carrier PCB. SoC selection is therefore a one-time board-level commitment per PCB revision.

The matrix evaluates candidates across AI performance, camera interface capability, power, cost, and product-tier suitability.

**Data Integrity Note:** All specifications in this document are sourced from official TI product pages (ti.com) as of June 2026. Values not publicly confirmed are explicitly marked. No approximate values are used unless the source datasheet itself provides a range.

---

## 2. Source References

| SoC | Official TI Product Page | SDK Family | EVM / Starter Kit |
|-----|--------------------------|------------|-------------------|
| TDA4VM-Q1 | [ti.com/product/TDA4VM](https://www.ti.com/product/TDA4VM) | Processor SDK Linux/RTOS/QNX for J721E | SK-TDA4VM, J721EXCPXEVM + J721EXSOMXEVM |
| TDA4VL-Q1 | [ti.com/product/TDA4VL-Q1](https://www.ti.com/product/TDA4VL-Q1) | Processor SDK Linux/QNX/RTOS for J721S2 | J721EXCPXEVM + J721S2XSOMXEVM; PHYTEC phyCORE-AM68 |
| AM62A7 | [ti.com/product/AM62A7](https://www.ti.com/product/AM62A7) | Processor SDK Linux for AM62A, MCU+ SDK | SK-AM62A-LP |
| J722S / AM67A | Not publicly confirmed | Not publicly confirmed | Not publicly confirmed |

---

## 3. SoC Comparison Matrix (Verified Official Data)

| Parameter | TDA4VL-Q1 | TDA4VM-Q1 | AM62A7 | J722S / AM67A |
|-----------|-----------|-----------|--------|---------------|
| **Vendor** | Texas Instruments | Texas Instruments | Texas Instruments | Texas Instruments |
| **Official Description** | Targeted at Smart Vision Camera applications | 8 TOPS of AI | 2 TOPS vision SoC with RGB-IR ISP for 1-2 cameras, driver monitoring | Not publicly confirmed |
| **CPU** | 2x Arm Cortex-A72 at up to 1200 MHz | 2x Arm Cortex-A72 at up to 2.0 GHz | Up to Quad Arm Cortex-A53 at up to 1.4 GHz | Not publicly confirmed |
| **Coprocessors** | Up to 4x Arm Cortex-R5F at up to 1.0 GHz (2x in TDA4VL variant) | 6x Arm Cortex-R5F at up to 1.0 GHz | 1x Arm Cortex-R5F at up to 800 MHz (MCU island) + 1x Cortex-R5F (device mgmt) | Not publicly confirmed |
| **DSP** | Two C7x at up to 1.0 GHz, 160 GFLOPS, 512 GOPS | C7x up to 1.0 GHz (80 GFLOPS, 256 GOPS) + Two C66x at up to 1.35 GHz | Single C7x at 1.0 GHz, 40 GFLOPS | Not publicly confirmed |
| **AI Accelerator** | MMA deep-learning accelerator, up to 8 TOPS (8b) at 1.0 GHz | MMA deep-learning accelerator, up to 8 TOPS (8b) at 1.0 GHz | MMA up to 2 TOPS (8b) at 1.0 GHz | Not publicly confirmed - requires vendor NDA/datasheet confirmation |
| **Vision Processing** | VPAC with ISP + DMPAC | VPAC with ISP + DMPAC | VPAC with ISP, 315 MPixel/s, up to 5MP@60fps, supports 12-bit RGB-IR | Not publicly confirmed |
| **GPU** | IMG BXS-4-64, up to 800 MHz, 50 GFLOPS | PowerVR Rogue 8XE GE8430, up to 750 MHz | None listed on product page | Not publicly confirmed |
| **CSI-2 RX Ports** | Two CSI2.0 4L RX + Two CSI2.0 4L TX with DPHY | Two CSI2.0 4L RX + One CSI2.0 4L TX | **ONE CSI-2 Receiver with 4-Lane D-PHY (CRITICAL: single port only)** | Not publicly confirmed |
| **CSI-2 Lane Speed** | Up to 2.5 Gbps per lane | Up to 2.5 Gbps per lane | Up to 2.5 Gbps per lane | Not publicly confirmed |
| **Virtual Channel Support** | Yes | Yes | Yes (up to 16 VCs on single port) | Not publicly confirmed |
| **CAN-FD Controllers** | Twenty MCAN modules with full CAN-FD | Sixteen MCAN modules with full CAN-FD | 3x CAN modules with CAN-FD (up to 8 Mbps) | Not publicly confirmed |
| **Ethernet** | Two RMII/RGMII interfaces | Integrated switch supporting up to 8 external ports (2.5Gb SGMII) | Integrated switch with 2 external ports (RMII/RGMII, TSN) | Not publicly confirmed |
| **Memory** | LPDDR4, One 32-bit bus, up to 4266 MT/s, up to 4MB L3 RAM | LPDDR4, 32-bit with inline ECC, up to 4266 MT/s | LPDDR4, 32-bit with inline ECC, up to 3733 MT/s, max 8GB | Not publicly confirmed |
| **Video Codec** | H.264/H.265 Encode/Decode up to 240MP/s | Yes (details per datasheet) | H.265/H.264 encode/decode, up to 4K UHD | Not publicly confirmed |
| **Storage** | Per datasheet (eMMC, SD, OSPI) | Per datasheet (eMMC, SD, OSPI) | eMMC 5.1, SD 3.0, OSPI/QSPI | Not publicly confirmed |
| **Package** | 23mm x 23mm, 0.8mm pitch, 770-pin FCBGA (ALZ) | 24mm x 24mm, 0.8mm pitch, 827-pin FCBGA (ALF) | 18mm x 18mm, 0.8mm pitch, 484-pin FCBGA (AMB) or FCCSP (ANF) | Not publicly confirmed |
| **Safety Certification** | ISO 26262/IEC 61508 certified up to ASIL D/SC 3 by TUV SUD | ISO 26262 certified up to ASIL D (MCU domain), ASIL B (Main domain), by TUV SUD | Functional Safety-Compliant targeted, ASIL D systematic, ASIL B HW integrity targeted, ISO 26262 by TUV SUD planned | Not publicly confirmed |
| **AEC-Q100** | Yes (Q1 variants) | Yes (Q1 variants) | Yes (AM62A7-Q1 automotive variant) | Not publicly confirmed |
| **Operating Temperature** | -40 to 125C | -40 to 105C | -40 to 125C | Not publicly confirmed |
| **Process Node** | 16nm FinFET | 16nm FinFET | 16nm FinFET | Not publicly confirmed |
| **PMIC** | TPS6594-Q1 | TPS6594-Q1 | Per datasheet | Not publicly confirmed |
| **Official Source / Evidence** | ti.com/product/TDA4VL-Q1 | ti.com/product/TDA4VM | ti.com/product/AM62A7 | Requires NDA/vendor confirmation for detailed specs |

---

## 4. Critical Finding: AM62A7 Single CSI-2 Port Limitation

**CRITICAL CONSTRAINT FOR DUAL-CAMERA ADVIS:**

The AM62A7 has **only ONE CSI-2 Receiver** (4-lane D-PHY). For the ADVIS dual-camera architecture (forward + DMS), this creates a fundamental constraint:

| Workaround Option | Feasibility | Impact on Cost-Down Goal |
|-------------------|-------------|--------------------------|
| Virtual Channels through external mux/splitter | Requires additional hardware (CSI-2 mux IC) | Partially defeats direct-MIPI cost-down purpose |
| Time-multiplex cameras on single port | Reduces effective frame rate per camera | May not meet 30fps simultaneous requirement |
| External SerDes hub to combine streams | Adds SerDes components back | Completely defeats cost-down architecture |
| Accept single camera only (DMS-only or FWD-only) | Limits product to single-camera use case | Product scope reduction |

**Recommendation:** AM62A7 should be evaluated only for single-camera product variants (e.g., standalone DMS module or standalone forward camera module). For dual-camera ADVIS, TDA4VL-Q1 or TDA4VM-Q1 remain the viable candidates with two native CSI-2 RX ports.

---

## 5. Critical Finding: TDA4VL-Q1 AI Performance Correction

**CORRECTION FROM PREVIOUS REVISION (v0.1):**

The v0.1 SoC matrix incorrectly stated TDA4VL has "~1 TOPS (C7x DSP only, no MMA)". This was WRONG.

**Official TI data confirms:** TDA4VL-Q1 has an MMA deep-learning accelerator with up to 8 TOPS (8b) at 1.0 GHz - the same AI accelerator class as TDA4VM-Q1.

Key differences between TDA4VL-Q1 and TDA4VM-Q1 per official product pages:
- Fewer R5F cores: 2 (TDA4VL) vs. 6 (TDA4VM)
- Lower A72 clock: 1200 MHz (TDA4VL) vs. 2000 MHz (TDA4VM)
- Smaller package: 23x23mm (TDA4VL) vs. 24x24mm (TDA4VM)
- Fewer Ethernet ports: 2 RMII/RGMII (TDA4VL) vs. 8-port switch (TDA4VM)
- Two C7x DSPs (TDA4VL) vs. one C7x + two C66x (TDA4VM)
- **SAME** MMA AI performance: 8 TOPS (8b)

This makes TDA4VL-Q1 significantly more attractive for ADVIS than previously assessed.

---

## 6. ADVIS Product Tier Suitability (Revised Assessment)

| Product Tier | TDA4VL-Q1 | TDA4VM-Q1 | AM62A7 | J722S / AM67A |
|-------------|-----------|-----------|--------|---------------|
| **ADVIS Assist** (FCW, LDW, TSR, PCW, DMS) | **Strong candidate** - 8 TOPS MMA with lower cost/power than TDA4VM | Capable but higher cost/power than needed for this tier | **CRITICAL: Single CSI-2 port limits dual-camera use** | Cannot assess - specs not publicly confirmed |
| **ADVIS Control** (AEB, ACC, LKA requests) | **Viable** - same 8 TOPS MMA; lower A72 clock may limit non-MMA workloads | **Strong candidate** - higher A72 clock, more R5F cores for safety partitioning | Not viable for dual-camera; 2 TOPS may be limiting for safety-critical inference | Cannot assess - specs not publicly confirmed |
| **ADVIS Fleet** (logging, scoring, events) | Capable (may be over-specified for logging workload) | Capable but higher cost/power than needed | Viable for single-camera fleet use (e.g., forward-only dash-cam) | Cannot assess - specs not publicly confirmed |
| **Single-Camera DMS Module** | Over-specified for single-camera DMS | Over-specified for single-camera DMS | **Good fit** - 2 TOPS adequate for DMS, single CSI-2 port sufficient | Cannot assess - specs not publicly confirmed |

### Tier Rationale (Revised)

- **ADVIS Assist:** TDA4VL-Q1 provides 8 TOPS MMA (same as TDA4VM) at lower power and cost, with two CSI-2 RX ports for simultaneous dual-camera operation. This is now the leading candidate for Assist tier.
- **ADVIS Control:** Both TDA4VL-Q1 and TDA4VM-Q1 provide 8 TOPS MMA. TDA4VM-Q1 offers higher CPU clock (2.0 vs 1.2 GHz) and more R5F cores (6 vs 2), which may benefit safety-critical partitioning and non-MMA workloads. The selection depends on whether the additional CPU headroom and R5F cores justify the power/cost increase.
- **ADVIS Fleet:** If dual-camera is required, TDA4VL-Q1 is the cost-effective choice. If single-camera logging is acceptable, AM62A7 offers the lowest cost.
- **AM62A7 for ADVIS dual-camera:** Not recommended due to single CSI-2 RX port constraint. Workarounds (mux, time-multiplex) add complexity that defeats the cost-down architecture goal.

---

## 7. DMS + Forward Simultaneous Load Analysis (Revised)

| Workload Scenario | TDA4VL-Q1 | TDA4VM-Q1 | AM62A7 | J722S / AM67A |
|-------------------|-----------|-----------|--------|---------------|
| FWD 2MP @ 30fps capture | Supported (CSI-2 RX port 0) | Supported (CSI-2 RX port 0) | Supported (single port, single camera) | Cannot assess |
| DMS 1MP @ 30fps capture | Supported (CSI-2 RX port 1) | Supported (CSI-2 RX port 1) | **NOT NATIVELY SUPPORTED** - requires mux or time-sharing on single port | Cannot assess |
| Both cameras simultaneous ISP | Supported (VPAC + ISP) | Supported (VPAC + ISP) | **Single port constraint prevents true simultaneous operation** | Cannot assess |
| FWD object detection (CNN on MMA) | 8 TOPS available | 8 TOPS available | 2 TOPS available (if single-camera) | Cannot assess |
| DMS face/gaze (CNN on MMA) | 8 TOPS shared with FWD | 8 TOPS shared with FWD | 2 TOPS (if single-camera) | Cannot assess |
| Both CNNs simultaneous on MMA | Feasible - 8 TOPS shared across both models | Feasible - 8 TOPS + higher CPU assists scheduling | N/A - dual camera not natively supported | Cannot assess |
| Headroom for future models | Moderate (A72 at 1.2 GHz may limit pre/post-processing) | Significant (A72 at 2.0 GHz + C66x assist) | Limited (2 TOPS, A53 cores) | Cannot assess |

---

## 8. Power Budget Comparison

### 8.1 Power Targets by Tier

| Power Tier | Target (Typical) | Maximum (Absolute) | Thermal Constraint |
|------------|-------------------|---------------------|-------------------|
| ADVIS Assist (TDA4VL-Q1) | Less than 6W module total | Less than 8W absolute max | Standard windshield-mount thermal (compact spreader) |
| ADVIS Control (TDA4VM-Q1) | Less than 14W module total | Less than 18W absolute max | Requires large thermal spreader, possible DVFS limiting |
| Single-Camera (AM62A7) | Less than 5W module total | Less than 7W absolute max | Minimal thermal challenge |

### 8.2 Detailed Power Breakdown

| Parameter | TDA4VL-Q1 | TDA4VM-Q1 | AM62A7 | J722S / AM67A |
|-----------|-----------|-----------|--------|---------------|
| SoC typical power (per TI product page context) | TBD - requires datasheet power tables | TBD - requires datasheet power tables; TI lists 10-15W class | TBD - requires datasheet power tables | Not publicly confirmed |
| DDR power (estimate based on bus width) | Estimate 0.5-1W (32-bit LPDDR4) | Estimate 1-2W (32-bit LPDDR4) | Estimate 0.5-1W (32-bit LPDDR4) | Not publicly confirmed |
| Camera sensors (2x) | ~0.5W | ~0.5W | ~0.25W (single camera) | N/A |
| IR LED subsystem | 0.3-0.5W (pulsed) | 0.3-0.5W (pulsed) | 0.3-0.5W (pulsed) | N/A |
| CAN PHY + misc | ~0.3W | ~0.3W | ~0.3W | N/A |
| **Estimated module total** | **TBD pending datasheet** | **~12-18W (estimated)** | **TBD pending datasheet** | **Not publicly confirmed** |
| Windshield thermal feasibility | Expected good (smaller package, lower power class) | Challenging (requires large spreader, DVFS may be needed) | Expected good (smallest package, low power) | Cannot assess |

*Note: Exact SoC power figures require per-use-case datasheet power tables or TI power estimation tools. Values listed as "TBD" should not be assumed without vendor confirmation.*

---

## 9. PCB Complexity and Board Area Impact

| Factor | TDA4VL-Q1 | TDA4VM-Q1 | AM62A7 | J722S / AM67A |
|--------|-----------|-----------|--------|---------------|
| Package size | 23x23mm, 0.8mm pitch | 24x24mm, 0.8mm pitch | 18x18mm, 0.8mm pitch | Not publicly confirmed |
| Ball count | 770-pin FCBGA (ALZ) | 827-pin FCBGA (ALF) | 484-pin FCBGA (AMB) | Not publicly confirmed |
| Required PCB layers (estimate) | 6-8 (0.8mm pitch is standard via escapable) | 8-10 (larger BGA, more signals) | 6 (fewer pins, standard escape) | Cannot assess |
| DDR routing complexity | 32-bit single bus | 32-bit with inline ECC | 32-bit with inline ECC | Cannot assess |
| Thermal pad area | 23x23mm package footprint | 24x24mm package footprint | 18x18mm package footprint | Cannot assess |
| Board area estimate | Depends on full schematic | Depends on full schematic | Depends on full schematic | Cannot assess |

---

## 10. Software Ecosystem and SDK Assessment

| Criterion | TDA4VL-Q1 | TDA4VM-Q1 | AM62A7 | J722S / AM67A |
|-----------|-----------|-----------|--------|---------------|
| SDK name | Processor SDK Linux/QNX/RTOS for J721S2 | Processor SDK Linux/RTOS/QNX for J721E | Processor SDK Linux for AM62A + MCU+ SDK | Not publicly confirmed |
| EVM availability | J721S2XSOMXEVM; PHYTEC phyCORE-AM68 | SK-TDA4VM; J721EXCPXEVM + J721EXSOMXEVM | SK-AM62A-LP | Not publicly confirmed |
| Related variants | TDA4VE-Q1 (more cores, dual LPDDR4), TDA4AL-Q1 (no GPU, encode only) | J721E family | AM62A3, AM62A7-Q1 (automotive) | Not publicly confirmed |
| Functional safety (ASIL) | ASIL D/SC 3 certified by TUV SUD | ASIL D (MCU domain), ASIL B (Main domain) certified by TUV SUD | ASIL D systematic, ASIL B HW integrity targeted | Not publicly confirmed |
| Deep learning support | MMA + C7x | MMA + C7x | MMA + C7x (smaller) | Not publicly confirmed |
| Software ecosystem maturity | Good (J721S2 family, derivative of J721E) | Excellent (flagship J721E platform, longest in market) | Good (broad AM62A Linux community, newer) | Cannot assess - insufficient public data |
| Long-term availability | Expected 10+ years (automotive-qualified) | Expected 10+ years (automotive-qualified) | Expected 10+ years (automotive-qualified) | Cannot assess |

---

## 11. Forward Camera Sensor Comparison

| Parameter | IMX390 (Sony) | OX03C10 (OmniVision) | AR0233 (onsemi) | AR0234 (onsemi) |
|-----------|---------------|----------------------|-----------------|-----------------|
| Resolution | 2.12 MP (1936x1100) | 2.5 MP (1920x1280) | 2.5 MP (1920x1280) | 2.3 MP (1920x1200) |
| Optical format | 1/2.7" | 1/2.5" | 1/2.7" | 1/2.6" |
| Shutter type | Rolling shutter | Rolling shutter | Rolling shutter | Global shutter |
| HDR capability | Yes (DOL-HDR, up to 120dB) | Yes (HDR, up to 120dB) | Yes (up to 120dB) | No native HDR |
| Low-light performance | Excellent (large pixel, 3um) | Good (2.1um pixel) | Good (2.1um pixel) | Moderate |
| LED flicker mitigation (LFM) | Yes | Yes | Yes (excellent) | N/A |
| MIPI CSI-2 lanes | 2 or 4 lanes | 2 or 4 lanes | 2 or 4 lanes | 2 or 4 lanes |
| Max frame rate (full res) | 60 fps (4-lane) | 60 fps (4-lane) | 60 fps (4-lane) | 120 fps (4-lane) |
| Power (typical) | ~250 mW | ~200 mW | ~200 mW | ~250 mW |
| Automotive grade | AEC-Q100 Grade 2 | AEC-Q100 Grade 2 | AEC-Q100 Grade 2 | AEC-Q100 Grade 2 |
| Cost class | $$$ | $$ | $$ | $$ |
| **ADVIS suitability** | Premium Assist/Control (best night) | Cost-optimized Assist | LED-heavy environments | Motion-critical (niche) |

---

## 12. DMS Camera Sensor Comparison

| Parameter | OX01N1B (OmniVision) | OX01H1B (OmniVision) | RGB-IR Option | AR0144 (onsemi) |
|-----------|---------------------|---------------------|---------------|-----------------|
| Resolution | 1.0 MP (1280x800) | 1.3 MP (1280x1024) | 1-2 MP (varies) | 1.0 MP (1280x800) |
| Shutter type | Rolling shutter | Rolling shutter | Rolling shutter | Global shutter |
| NIR sensitivity | Optimized (850nm/940nm) | Optimized (850nm/940nm) | Moderate (RGB-IR Bayer) | Moderate (broadband) |
| MIPI CSI-2 lanes | 1 or 2 lanes | 1 or 2 lanes | 2 lanes | 1 or 2 lanes |
| Frame rate (typical DMS) | 30 fps | 30 fps | 30 fps | 60 fps (global shutter) |
| Power (typical) | ~100 mW | ~120 mW | ~150 mW | ~200 mW |
| IR illumination required | Yes (850/940nm LED) | Yes (850/940nm LED) | Optional | Yes (with NIR filter) |
| Automotive grade | AEC-Q100 | AEC-Q100 | Varies | AEC-Q100 |
| Cost class | $ | $ | $$ | $$ |
| **ADVIS suitability** | Assist/Fleet (cost-down) | Control (higher res DMS) | Cabin monitoring (day+night) | High-motion tolerance |

---

## 13. Recommended SoC + Sensor Combinations (Revised)

| Product Tier | SoC | Forward Sensor | DMS Sensor | Rationale |
|-------------|-----|----------------|------------|-----------|
| ADVIS Assist (cost-optimized) | TDA4VL-Q1 | OX03C10 | OX01N1B | 8 TOPS MMA in smaller/lower-power package; two CSI-2 ports |
| ADVIS Assist (premium) | TDA4VL-Q1 | IMX390 | OX01N1B | Same SoC, premium sensor for better night performance |
| ADVIS Control | TDA4VM-Q1 | IMX390 | OX01H1B | Higher CPU clock and more R5F cores for safety partitioning |
| ADVIS Control (cost-explore) | TDA4VL-Q1 | IMX390 | OX01H1B | Evaluate if 1.2 GHz A72 + 2x R5F is sufficient for Control tier |
| Single-Camera DMS | AM62A7 | N/A | OX01N1B or RGB-IR | Single CSI-2 port sufficient; lowest cost for DMS-only product |
| Single-Camera Forward | AM62A7 | OX03C10 | N/A | Single CSI-2 port sufficient; lowest cost for forward-only product |

---

## 14. Selection Risks and Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| TDA4VL A72 at 1.2 GHz may limit non-MMA workloads | Pre/post-processing throughput for complex pipelines | Benchmark on J721S2 EVM; if limiting, evaluate TDA4VM for Control tier |
| TDA4VM thermal in windshield mount | Potential throttling or reliability concern | Large thermal spreader, DVFS power-aware scheduling, CFD simulation required |
| AM62A7 single CSI-2 port for dual-camera | Cannot natively support dual-camera ADVIS | Restrict AM62A7 to single-camera product variants only |
| J722S specifications not publicly confirmed | Cannot make informed selection decision | Defer J722S evaluation until official product page or NDA data available |
| Sensor end-of-life risk | Supply disruption | Dual-source sensor footprint where pinout-compatible alternatives exist |
| Direct-mount SoC limits future flexibility | Locked to one SoC per PCB revision | Accept: v0.5 is production cost-down, not flexible development platform |
| TDA4VL vs TDA4VM pinout compatibility unknown | May prevent single-PCB strategy | Conduct BGA pinout compatibility analysis (see separate checklist document) |

---

## 15. Decision Summary (Revised)

| Decision | Status | Recommendation |
|----------|--------|----------------|
| Primary SoC for ADVIS Assist v0.5 | OPEN | TDA4VL-Q1 (8 TOPS MMA, lower cost/power, two CSI-2 RX ports) |
| Primary SoC for ADVIS Control v0.5 | OPEN | TDA4VM-Q1 (8 TOPS MMA + higher CPU clock + more R5F for safety partitioning); TDA4VL-Q1 as cost-explore alternative |
| AM62A7 for dual-camera ADVIS | **NOT RECOMMENDED** | Single CSI-2 RX port is a critical constraint for dual-camera architecture |
| AM62A7 for single-camera variant | OPEN | Viable for DMS-only or forward-only single-camera products |
| J722S / AM67A evaluation | DEFERRED | Cannot assess until official specifications are publicly available or NDA data obtained |
| Forward sensor (Assist) | OPEN | OX03C10 (cost-optimized) or IMX390 (premium) |
| Forward sensor (Control) | OPEN | IMX390 (best night/HDR, mature ISP tuning) |
| DMS sensor (Assist) | OPEN | OX01N1B (lowest cost, good NIR) |
| DMS sensor (Control) | OPEN | OX01H1B (higher resolution for gaze accuracy) |

All selections are PRELIMINARY and require vendor engagement, datasheet confirmation, and evaluation sample testing before commitment.

---

## 16. Revision History

| Rev | Date | Author | Change |
|-----|------|--------|--------|
| 0.1 | 2026-06 | Systems Engineering | Initial PRELIMINARY release for v0.5 compact module |
| 0.2 | 2026-06 | Systems Engineering | MAJOR CORRECTION: TDA4VL-Q1 confirmed 8 TOPS MMA (not ~1 TOPS); AM62A7 single CSI-2 port identified as critical dual-camera constraint; all specs updated to verified TI product page data; removed unverified approximate values; added source references |

---

*PRELIMINARY - All values subject to datasheet/vendor confirmation. Specifications sourced from ti.com product pages as of June 2026.*

*End of Document*

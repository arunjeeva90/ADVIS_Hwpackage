# ADVIS v0.5 SoC Selection Matrix

**Classification:** CONFIDENTIAL - ENGINEERING USE ONLY  
**Status:** PRELIMINARY - Subject to vendor/datasheet confirmation  
**Version:** v0.1 - July 2026  
**Document ID:** ARCH-SOC-002

---

## 1. Overview

This document provides the SoC selection decision matrix for the ADVIS v0.5 Compact Module. Unlike the v0.4.4 SOM-based architecture, the v0.5 places the SoC directly on the carrier PCB. SoC selection is therefore a one-time board-level commitment per PCB revision.

The matrix evaluates candidates across AI performance, camera interface capability, power, cost, and product-tier suitability.

---

## 2. SoC Comparison Matrix

| Parameter | TDA4VL-Q1 | TDA4VM-Q1 | AM62A | J722S / AM67A / TDA4VEN-class |
|-----------|-----------|-----------|-------|-------------------------------|
| **Vendor** | Texas Instruments | Texas Instruments | Texas Instruments | Texas Instruments |
| **AI TOPS** | ~1 TOPS (C7x DSP only, no MMA) | ~8 TOPS (C7x + MMA) | ~2 TOPS (C7x + limited accelerator) | ~4 TOPS (C7x + MMA) |
| **Deep Learning Accelerator** | None (C7x scalar only) | MMA (matrix multiply accelerator) | Limited DLA | MMA (smaller than TDA4VM) |
| **CSI-2 RX Ports** | 2x CSI-2 RX | 2-4x CSI-2 RX | 1-2x CSI-2 RX | 2x CSI-2 RX |
| **Max CSI-2 Lanes (per port)** | 4 lanes | 4 lanes | 4 lanes | 4 lanes |
| **ISP / Vision Processing** | VPAC (single pipeline) | VPAC3 (dual camera support) | Single ISP | VPAC (dual camera capable) |
| **Simultaneous FWD + DMS** | Yes (2 ports) | Yes (dedicated per camera) | Marginal (shared ISP bandwidth) | Yes (2 ports) |
| **CPU Cores** | 2x A53 (or 1x A53 + R5F) | 2x A72 + 4x A53 + R5F | 4x A53 | 4x A53 + R5F |
| **LPDDR4/4X Support** | Yes (16-bit, 2GB typ) | Yes (32-bit, up to 8GB) | Yes (16-bit, up to 4GB) | Yes (32-bit, up to 4GB) |
| **CAN-FD Controllers** | 2x MCAN | 3x MCAN | 2x MCAN | 2-3x MCAN |
| **Typical Power** | 3-5W | 10-15W | 3-5W | 5-8W |
| **Package Size** | 17x17mm or 15x15mm BGA | 23x23mm BGA | Small BGA (~15x15mm) | Mid-size BGA (~17x17mm) |
| **PCB Complexity** | Low-medium (6-8 layer) | High (8-10 layer, HDI) | Low (6 layer) | Medium (6-8 layer) |
| **Automotive Qualification** | AEC-Q100 Grade 2 | AEC-Q100 Grade 2 | AEC-Q100 Grade 2 | AEC-Q100 Grade 2 (pending) |
| **Operating Temp (Tj)** | -40C to +125C | -40C to +125C | -40C to +125C | -40C to +125C |
| **TI SDK Support** | TI Edge AI SDK | TI Edge AI SDK (most mature) | TI Processor SDK (Linux focus) | TI Edge AI SDK (newer, maturing) |
| **Software Ecosystem Maturity** | Good (derivative of TDA4VM) | Excellent (flagship platform) | Good (broad Linux community) | Moderate (newer silicon, less field data) |
| **Model Zoo / Reference Models** | Limited (C7x only inference) | Extensive (full DL support) | Limited | Growing |
| **Cost Class** | $ | $$$ | $ | $$ |

---

## 3. ADVIS Product Tier Suitability

| Product Tier | TDA4VL-Q1 | TDA4VM-Q1 | AM62A | J722S / TDA4VEN-class |
|-------------|-----------|-----------|-------|------------------------|
| **ADVIS Assist** (FCW, LDW, TSR, PCW, DMS) | **BEST FIT** | Overkill (cost/power) | Marginal (dual-cam ISP sharing) | Good fit |
| **ADVIS Control** (AEB, ACC, LKA requests) | Insufficient AI | **BEST FIT** | Insufficient AI | Marginal (4 TOPS may suffice for basic) |
| **ADVIS Fleet** (logging, scoring, events) | Good fit | Overkill | **BEST FIT** | Good fit |
| **ADVIS Fusion** (camera + radar fusion) | Insufficient | Marginal | Insufficient | Insufficient |

### Tier Rationale

- **ADVIS Assist:** Requires ~1-2 TOPS for FCW/LDW/TSR plus DMS at 30fps. TDA4VL provides sufficient compute with lowest cost/power. AM62A is marginal due to ISP bandwidth sharing between two cameras.
- **ADVIS Control:** Requires ~6-8 TOPS for AEB/ACC/LKA request generation with safety margins. TDA4VM is the only candidate with sufficient AI headroom and mature SDK for safety-critical inference.
- **ADVIS Fleet:** Primary workload is video encoding, event logging, and driver scoring. Minimal real-time AI needed. AM62A provides adequate performance at lowest cost.
- **ADVIS Fusion:** Requires radar point cloud processing plus camera perception. Beyond v0.5 compact scope (future platform).

---

## 4. DMS + Forward Simultaneous Load Analysis

| Workload Scenario | TDA4VL-Q1 | TDA4VM-Q1 | AM62A | J722S / TDA4VEN-class |
|-------------------|-----------|-----------|-------|------------------------|
| FWD 2MP @ 30fps capture | OK | OK | OK | OK |
| DMS 1MP @ 30fps capture | OK | OK | OK | OK |
| Both cameras simultaneous ISP | OK (2 CSI ports) | Excellent (VPAC3 dual) | Constrained (1 ISP pipeline) | OK (2 CSI ports) |
| FWD object detection (CNN) | Marginal (~1 TOPS) | Comfortable | Marginal | OK (~4 TOPS) |
| DMS face/gaze (CNN) | Marginal (time-shared) | Comfortable | Marginal | OK |
| Both CNNs simultaneous | Constrained | Comfortable | Insufficient | Marginal |
| Headroom for future models | None | Significant | None | Some |

---

## 5. Power Budget Comparison

| Parameter | TDA4VL-Q1 | TDA4VM-Q1 | AM62A | J722S / TDA4VEN-class |
|-----------|-----------|-----------|-------|------------------------|
| SoC typical power | 3-5W | 10-15W | 3-5W | 5-8W |
| DDR power (estimate) | 0.5-1W | 1-2W | 0.5-1W | 1-1.5W |
| Camera sensors (2x) | 0.5W | 0.5W | 0.5W | 0.5W |
| IR LED subsystem | 0.3-0.5W | 0.3-0.5W | 0.3-0.5W | 0.3-0.5W |
| CAN PHY + misc | 0.3W | 0.3W | 0.3W | 0.3W |
| **Total module (typical)** | **~5-7W** | **~12-18W** | **~5-7W** | **~7-11W** |
| Windshield thermal feasibility | Good | Challenging (needs large spreader) | Good | Acceptable |
| 12V input current (typical) | ~0.5A | ~1.2A | ~0.5A | ~0.8A |

---

## 6. PCB Complexity and Board Area Impact

| Factor | TDA4VL-Q1 | TDA4VM-Q1 | AM62A | J722S / TDA4VEN-class |
|--------|-----------|-----------|-------|------------------------|
| BGA pitch | 0.65-0.8mm | 0.65mm | 0.65-0.8mm | 0.65mm |
| Ball count | ~400-600 | ~800-1000 | ~300-500 | ~500-700 |
| Required PCB layers | 6-8 | 8-10 (HDI recommended) | 6 | 6-8 |
| DDR routing complexity | 16-bit (simple) | 32-bit (complex) | 16-bit (simple) | 32-bit (medium) |
| Power delivery complexity | Low (few rails) | High (many rails, high current) | Low | Medium |
| Thermal pad area | Small | Large (23x23mm minimum) | Small | Medium |
| Board area estimate | 40x50mm achievable | 50x60mm minimum | 35x45mm achievable | 45x55mm achievable |
| Via technology | Standard through-hole | Microvias / blind vias | Standard through-hole | Standard or microvia |

---

## 7. Software Ecosystem and SDK Assessment

| Criterion | TDA4VL-Q1 | TDA4VM-Q1 | AM62A | J722S / TDA4VEN-class |
|-----------|-----------|-----------|-------|------------------------|
| SDK name | TI Edge AI SDK | TI Edge AI SDK | TI Processor SDK | TI Edge AI SDK |
| Linux BSP maturity | Good | Excellent | Good | Moderate (newer) |
| RTOS (FreeRTOS on R5F) | Yes | Yes | Limited | Yes |
| Deep learning frameworks | TFLite (C7x only) | TFLite, ONNX, TVM | TFLite (limited) | TFLite, ONNX |
| Pre-trained model zoo | Small | Large | Small | Growing |
| Camera ISP tuning tools | Available | Mature | Basic | Available |
| OpenCV / OpenVX support | Yes | Yes (HW-accelerated) | Yes (CPU only) | Yes |
| Functional safety (ASIL) | ASIL-B capable (R5F) | ASIL-B capable (R5F) | QM only | ASIL-B capable (R5F) |
| Community / ecosystem | Moderate | Large | Large (Linux) | Small (new) |
| Long-term availability | 10+ years (automotive) | 10+ years (automotive) | 10+ years (automotive) | TBD (confirm with TI) |
| Reference design availability | Limited | Yes (SK-TDA4VM) | Yes (SK-AM62A) | Limited |

---

## 8. Forward Camera Sensor Comparison

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
| TI ISP support (VPAC) | Mature (reference tuning) | Good | Good | Good |
| Power (typical) | ~250 mW | ~200 mW | ~200 mW | ~250 mW |
| Automotive grade | AEC-Q100 Grade 2 | AEC-Q100 Grade 2 | AEC-Q100 Grade 2 | AEC-Q100 Grade 2 |
| Cost class | $$$ | $$ | $$ | $$ |
| Ecosystem maturity | Excellent (widely deployed) | Good (production OEM use) | Good (production OEM use) | Niche (specific applications) |
| **Best for ADVIS** | Premium Assist/Control | Cost-down Assist | LED-heavy environments | Motion-critical (less common) |

### Forward Sensor Recommendation (PRELIMINARY)

- **ADVIS Assist (cost-down):** OX03C10 or AR0233 -- good HDR, lower cost than IMX390
- **ADVIS Control (performance):** IMX390 -- best night vision, most mature TI ISP tuning
- **ADVIS Fleet (balanced):** OX03C10 -- adequate quality at lower cost

---

## 9. DMS Camera Sensor Comparison

| Parameter | OX01N1B (OmniVision) | OX01H1B (OmniVision) | RGB-IR Option | AR0144 (onsemi) |
|-----------|---------------------|---------------------|---------------|-----------------|
| Resolution | 1.0 MP (1280x800) | 1.3 MP (1280x1024) | 1-2 MP (varies) | 1.0 MP (1280x800) |
| Optical format | Small die | Small die | Varies | 1/4" |
| Shutter type | Rolling shutter | Rolling shutter | Rolling shutter | Global shutter |
| NIR sensitivity | Optimized (850nm/940nm) | Optimized (850nm/940nm) | Moderate (RGB-IR Bayer) | Moderate (broadband) |
| NIR quantum efficiency | High (dedicated NIR pixel) | High (dedicated NIR pixel) | Medium (shared pixel) | Medium |
| Dual-mode (visible + NIR) | NIR only | NIR only | Yes (RGB + NIR) | Broadband (with filter) |
| MIPI CSI-2 lanes | 1 or 2 lanes | 1 or 2 lanes | 2 lanes | 1 or 2 lanes |
| Frame rate (typical DMS) | 30 fps | 30 fps | 30 fps | 60 fps (global shutter) |
| Power (typical) | ~100 mW | ~120 mW | ~150 mW | ~200 mW |
| IR illumination required | Yes (850/940nm LED) | Yes (850/940nm LED) | Optional (works in visible too) | Yes (with NIR filter) |
| Die size / module cost | Very small / lowest | Small / low | Medium / medium | Small / higher |
| TI ISP support | Good | Good | Requires custom tuning | Good |
| Automotive grade | AEC-Q100 | AEC-Q100 | Varies by vendor | AEC-Q100 |
| Cost class | $ | $ | $$ | $$ |
| **Best for ADVIS** | Assist/Fleet (cost-down) | Control (higher res DMS) | Cabin monitoring (day+night) | High-motion tolerance |

### DMS Sensor Recommendation (PRELIMINARY)

- **ADVIS Assist (cost-down):** OX01N1B -- smallest die, lowest cost, excellent NIR for basic DMS
- **ADVIS Control (accuracy):** OX01H1B -- higher resolution for gaze/attention accuracy
- **ADVIS Fleet (cabin monitoring):** RGB-IR option -- dual-mode allows visible cabin recording + NIR DMS
- **Special cases:** AR0144 if global shutter needed for fast head movements (higher cost)

---

## 10. Recommended SoC + Sensor Combinations

| Product Tier | SoC | Forward Sensor | DMS Sensor | Total Power | Cost Class |
|-------------|-----|----------------|------------|-------------|------------|
| ADVIS Assist (entry) | TDA4VL-Q1 | OX03C10 | OX01N1B | ~5-6W | $ |
| ADVIS Assist (premium) | TDA4VL-Q1 | IMX390 | OX01N1B | ~5-7W | $$ |
| ADVIS Control | TDA4VM-Q1 | IMX390 | OX01H1B | ~13-16W | $$$ |
| ADVIS Fleet | AM62A | OX03C10 | OX01N1B | ~5-6W | $ |
| ADVIS Assist/Control (sweet spot) | J722S | OX03C10 or AR0233 | OX01H1B | ~8-10W | $$ |

---

## 11. Selection Risks and Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| TDA4VL 1 TOPS insufficient for future models | Cannot run larger networks | Design PCB to accept J722S as alternate population |
| TDA4VM thermal in windshield mount | Throttling or reliability risk | Large thermal spreader, power-aware scheduling |
| AM62A single ISP pipeline for two cameras | Frame-rate or latency impact | Time-multiplex ISP, accept lower DMS rate |
| J722S SDK immaturity | Delayed software bring-up | Start development on TDA4VM SDK, port later |
| Sensor end-of-life risk | Supply disruption | Dual-source sensor footprint (compatible pinout) |
| Direct-mount SoC limits future flexibility | Locked to one SoC per PCB rev | Accept: v0.5 is production cost-down, not flexible dev platform |

---

## 12. Decision Summary

| Decision | Status | Recommendation |
|----------|--------|----------------|
| Primary SoC for ADVIS Assist v0.5 | OPEN | TDA4VL-Q1 (lowest cost, adequate for warnings) |
| Primary SoC for ADVIS Control v0.5 | OPEN | TDA4VM-Q1 (only candidate with sufficient AI) |
| Alternate/future SoC consideration | OPEN | J722S (watch SDK maturity, potential Assist/Control bridge) |
| Forward sensor (Assist) | OPEN | OX03C10 (cost-down) or IMX390 (premium) |
| Forward sensor (Control) | OPEN | IMX390 (best night/HDR, mature ISP tuning) |
| DMS sensor (Assist) | OPEN | OX01N1B (lowest cost, good NIR) |
| DMS sensor (Control) | OPEN | OX01H1B (higher resolution) |

All selections are PRELIMINARY and require vendor engagement, datasheet confirmation, and evaluation sample testing before commitment.

---

## 13. Revision History

| Rev | Date | Author | Change |
|-----|------|--------|--------|
| 0.1 | 2026-07 | Systems Engineering | Initial PRELIMINARY release for v0.5 compact module |

---

*PRELIMINARY - All values subject to datasheet/vendor confirmation*

*End of Document*

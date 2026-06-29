# ADVIS Cost-Down BOM Comparison v0.1

**Classification:** Confidential - Engineering Use Only  
**Version:** 0.1  
**Date:** June 2026

---

## 1. Purpose

This document compares the bill-of-materials between the v0.4.4 A-sample SerDes/SOM architecture and the v0.5 compact direct-MIPI production-cost-down architecture. It identifies cost drivers, size impacts, and risk/validation trade-offs to support the production cost reduction decision.

---

## 2. Comparison Table

| Block | v0.4.4 A-sample SerDes/SOM | v0.5 Compact Direct-MIPI | Cost Impact | Size Impact | Risk / Validation Impact |
|-------|---------------------------|--------------------------|-------------|-------------|--------------------------|
| **Compute** | Phytec phyCORE SOM module (TDA4VM/AM68A) | Direct SoC placement (TDA4VL/TDA4VM/AM62A) on carrier PCB | Major saving (SOM markup eliminated) | Significant reduction (no SOM connector area) | Higher carrier PCB complexity; requires own DDR/eMMC layout |
| **DS90UB954** | Present (dual FPD-Link III deserializer) | Removed (not needed for co-located cameras) | Saving: ~$8-15 per unit | Major reduction (QFN48 + passives removed) | Removes SerDes validation; reduces link debug capability |
| **UB953 serializers** | Two assumed (one per remote camera module) | Removed (cameras connect directly via MIPI) | Saving: ~$6-10 per camera module | Camera module board size reduction | Eliminates remote camera cable length validation |
| **FAKRA/HSD connectors** | Two (one per camera coax link) | Removed (no coaxial links) | Saving: ~$3-6 per connector | Major reduction (connector footprint + keep-out) | Eliminates connector mating cycle and vibration test |
| **PoC inductors/filters** | Present (bias-T per FPD-Link port) | Removed (no power-over-coax needed) | Minor saving (~$1-2 total) | Minor reduction | Eliminates PoC power budget analysis |
| **MicroSD** | Present (UHS-I slot, card detect) | Removed (eMMC sufficient for production) | Minor saving (~$0.50-1) | Minor reduction | Loses removable storage debug convenience |
| **USB-C** | Present (device mode, firmware update) | Removed (UART/JTAG via test pads instead) | Minor saving (~$1-2 with ESD/connector) | Minor reduction | Loses convenient USB update; production uses fixture |
| **Ethernet** | Optional header present | Removed | Minor saving | Minor reduction | No impact for production use case |
| **GNSS** | Present (NEO-M9N-00B + antenna path) | Optional DNI (populate for Fleet/Fusion only) | Saving when DNI: ~$8-12 | Moderate (module + antenna + SAW) | Fleet variant requires separate validation |
| **IMU** | Present (BMI088 + SPI interface) | Optional DNI (populate for Fleet/Fusion only) | Saving when DNI: ~$3-5 | Minor (small QFN) | Fleet variant requires separate validation |
| **Debug headers** | Large multi-pin headers (JTAG, GPIO, SPI probe) | Removed (replaced by test pads) | Minor saving (~$1-3) | Moderate board area saving | Requires pogo-pin fixture for debug access |
| **LEDs/buttons** | Multiple status LEDs, reset button | Removed or minimized (single status LED optional) | Negligible | Minor | Reduces visual diagnostic capability |
| **IR illumination** | External daughterboard connector + off-board LEDs | Integrated IR LEDs on main PCB/DMS pod | Minor saving (eliminates connector) | Reduction (no separate board/cable) | Requires thermal integration; no field-swap of IR board |
| **Memory** | 4 GB DDR + 32 GB eMMC (SOM-provided) | 2 GB DDR + 16 GB eMMC (entry tier); 4 GB/32 GB (high tier) | Saving at entry tier: ~$5-15 | N/A (on-board either way) | Entry tier must validate with reduced memory |
| **PCB layer count** | 10-layer (TBD, wide board, many high-speed interfaces) | 6-8 layer (compact, fewer high-speed SerDes traces) | Saving: 20-40% on bare PCB cost | Smaller overall board dimensions | Requires new stackup SI analysis |
| **Enclosure and thermal** | Larger enclosure, separate heatsink | Compact housing with integrated aluminum spreader | Tooling cost; per-unit savings at volume | Major reduction in overall module volume | New thermal analysis required for windshield mount |

---

## 3. Important Notes

### 3.1 Conditions for Removal

- DS90UB954, UB953, PoC, and FAKRA/HSD connectors are removed ONLY when cameras are integrated in the same windshield module with direct MIPI connection.
- Optional SerDes architecture remains valid for remote-camera OEM variants where cameras are separated from the ECU by long cable runs.
- A separate PCB revision or add-on module may be created if an OEM requires FPD-Link support.

### 3.2 Items NOT Removed in v0.5

The following items must remain in the compact v0.5 architecture regardless of cost pressure:

| Item | Reason |
|------|--------|
| 12V input protection (fuse, TVS, reverse-polarity MOSFET) | Automotive electrical environment protection |
| Watchdog (TPS3431-Q1) | Safety supervisor, independent timeout |
| Reset supervisor (TPS3808G33-Q1) | Rail monitoring, controlled POR |
| CAN-FD transceiver (TCAN1044AV-Q1) | Vehicle communication interface |
| ESD protection on all external/flex connector pins | Automotive ESD compliance |
| EMC input filtering | Automotive EMC compliance |
| Power tree (5V/3.3V/1.8V topology) | Proven, validated in v0.4.4 |
| Sensor power rails | Required for image sensors |
| IR LED control circuit | DMS illumination |

### 3.3 Cost Estimate Summary

| Category | Estimated Per-Unit Saving (v0.5 vs v0.4.4) |
|----------|---------------------------------------------|
| SerDes removal (DS90UB954 + UB953 + PoC + FAKRA) | $20-35 |
| SOM to direct SoC | $15-40 (depends on SOM pricing) |
| Memory reduction (entry tier) | $5-15 |
| PCB simplification (fewer layers, smaller board) | $5-15 |
| Debug/service interface removal | $3-8 |
| GNSS/IMU DNI (non-fleet variants) | $11-17 |
| **Total estimated saving (entry tier)** | **$60-130 per unit** |

*Note: Estimates are order-of-magnitude for planning purposes. Actual savings depend on volume, vendor negotiations, and final component selection.*

---

## 4. Non-Recurring Engineering (NRE) Considerations

| Item | v0.4.4 | v0.5 |
|------|--------|------|
| PCB design complexity | Moderate (SOM simplifies compute area) | Higher (direct SoC requires DDR/eMMC layout) |
| Thermal design | Standard (larger enclosure, forced air option) | Challenging (compact, windshield, passive only) |
| Mechanical tooling | Standard enclosure | Custom housing mold (plastic + aluminum) |
| Optical design | Not applicable (no integrated optics) | New (dual optical path, baffle, IR window) |
| SI/PI analysis | FPD-Link + CSI-2 | MIPI + DDR (more critical due to direct SoC) |
| Validation effort | Standard subsystem-by-subsystem | New camera integration + thermal + optical tests |

---

## 5. Decision Criteria

Use this table to decide which baseline applies to a given project:

| Criterion | Use v0.4.4 A-sample | Use v0.5 Compact |
|-----------|--------------------|--------------------|
| Cameras remote from ECU (long cable) | Yes | No |
| Engineering validation / bring-up | Yes | No |
| Maximum debug access needed | Yes | No |
| Production high-volume OEM | No | Yes |
| Cost-sensitive deployment | No | Yes |
| Windshield-mount required | No | Yes |
| Compact form factor required | No | Yes |
| GNSS/IMU always needed | Yes (populated) | Variant-dependent (DNI option) |

---

*End of Document*

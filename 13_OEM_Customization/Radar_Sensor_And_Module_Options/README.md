# Radar Sensor and Module Options

## Purpose

This package is the **SoC-agnostic automotive radar product, module, chipset, sourcing and feature-deployment reference** for ADVIS.

The radar layer is deliberately independent from TI TDA, AM62A, TDA4, NXP, Renesas, Qualcomm, Ambarella, Horizon Robotics, NVIDIA, Rockchip or any other central compute platform.

The preferred production boundary is:

```text
Radar RF + antenna + radar processing + tracking + diagnostics
        ↓
Smart radar object list over CAN-FD
and/or radar point cloud over Automotive Ethernet
        ↓
ADVIS Radar HAL
        ↓
Camera-radar fusion, feature logic and safety gating
        ↓
OEM vehicle controllers / HMI
```

A radar that only exposes raw ADC or range-FFT data is **not plug-and-play and not truly SoC-agnostic**. Such platforms are retained in this package for algorithm research and custom radar development, but they are kept separate from complete smart sensors.

## Folder contents

| File / folder | Purpose |
|---|---|
| `01_SoC_Agnostic_Radar_Architecture_And_Selection_Strategy.md` | Universal radar product boundary, normalized HAL, interface tiers and development strategy |
| `02_ADAS_Radar_Product_Master_Reference.md` | Ranked comparison from Tier-1 automotive imaging radars to the cheapest usable development modules |
| `03_Supplier_Sourcing_And_Price_Reference.md` | Observed public prices, seller/platform, MOQ and sourcing risk |
| `04_Alternative_Manufacturers_And_Startups.md` | Tier-1s, independent specialists, startups, Chinese alternatives and chipset suppliers |
| `05_Interface_Output_And_Compute_Compatibility.md` | CAN/CAN-FD, Automotive Ethernet, USB/UART and raw-data compatibility policy |
| `06_ADAS_Feature_To_Radar_Deployment_Matrix.md` | Radar placement and capability needed for FCW, ACC, AEB, BSD, LCA, RCTA, MOIS and other functions |
| `07_Supplier_RFQ_And_Sample_Buying_Checklist.md` | Exact technical, quality and commercial questions before purchase |
| `08_Recommended_Procurement_Shortlist.md` | Recommended sample/RFQ actions for ADVIS Vision, Fusion, Fleet and two-wheeler ARAS paths |
| `data/` | Spreadsheet-ready CSV copies of all main comparison tables |
| `sources/Official_And_Supplier_Source_Index.md` | Official manufacturer, distributor and marketplace links |

## Current engineering recommendation

1. **Start ADVIS Fusion with one complete front smart radar**, not a raw radar board.
2. Require **CAN-FD object-list output** as the minimum universal interface. Add **100BASE-T1 point-cloud output** when richer fusion or recording is needed.
3. For a fast professional PoC, prioritize **Ainstein K-77**, **smartmicro DRVEGRD**, or a verified **Continental ARS408/ARS548 reference sensor**.
4. For cost exploration, RFQ **Nanoradar**, **Calterah-based module suppliers**, **CUB**, and other validated 77 GHz module houses.
5. For in-house radar learning and custom-product development, use **TI AWRL1432/AWR1843/AWR2944**, **NXP SAF85xx**, or **Infineon CTRX car kits**.
6. Use low-cost Alibaba BSD/FCW kits only for **packaging, HMI and warning-demo work** unless the seller provides an open object-data ICD, diagnostic concept, traceability and qualification evidence.
7. Do not treat 24/60 GHz human-presence modules as exterior ADAS radars. They are useful only for bench learning, cabin sensing or near-field experiments.
8. Production selection must be based on measured range/FOV/resolution, false-target behaviour, interference robustness, environmental validation, safety evidence, lifecycle and complete system cost.

## ADVIS radar deployment ladder

| Stage | Sensor set | Feature intent |
|---|---|---|
| `R0 — Bench` | One EVK / USB-UART radar | Learn radar data, visualization and fusion interfaces |
| `R1 — Front Fusion` | One front smart radar + forward camera | FCW/ACC/AEB confirmation, lead tracking and cut-in robustness |
| `R2 — Rear Safety` | Two rear corner radars | BSD, LCA, RCTA and DOW |
| `R3 — 360° Fusion` | Front + four corners | FCTA, side VRU, enhanced AEB/ACC and low-speed coverage |
| `R4 — Imaging` | Front 4D imaging radar + corners | L2+/L3 research, stationary-object/free-space and high-resolution perception |

## Core sourcing rule

Compare the complete usable radar cost:

> Radar IC/front end + antenna PCB/waveguide + processor + memory + power protection + housing/radome + connector + CAN/Ethernet PHY + firmware + tracker + object-data license + calibration + mounting bracket + harness + diagnostics + safety documentation + PPAP + validation support.

A cheap radar IC, used OEM radar or marketplace warning kit is not equivalent to an OEM-ready universal smart radar.

## Data status

- Global sourcing scan date: **20 July 2026**
- Public automotive radar pricing is rare; most Tier-1 and startup products are RFQ or OEM-programme only.
- Prices are indicative observations and may exclude GST, freight, customs, duty, harnesses, software licences, NRE, calibration and support.
- Manufacturer range/FOV figures are vendor-stated and must be reproduced in an ADVIS-controlled test setup before selection.
- Marketplace entries are sourcing evidence, not approved suppliers or safety claims.

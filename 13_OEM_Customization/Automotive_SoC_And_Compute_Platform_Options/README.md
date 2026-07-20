# Automotive SoC and Compute Platform Options

## Purpose

This package is the **vendor-neutral automotive compute, AI accelerator, development-board, sourcing and ADVIS feature-scaling reference** for Forward Vision, Driver Monitoring, camera-radar fusion and future surround perception.

The selection is deliberately not locked to Texas Instruments. TI remains the current development baseline because the project already has Jacinto/TDA software and hardware work, but the production architecture shall preserve model, sensor and vehicle-interface portability across TI, Renesas, NXP, Ambarella, Qualcomm, NVIDIA, Mobileye, Horizon Robotics, Black Sesame, Nextchip, indie, Telechips and other qualified platforms.

## Critical distinction

The package separates four categories:

```text
1. Automotive ADAS SoC
   ISP + AI/CV + safety island + automotive interfaces + safety documentation

2. Automotive edge vision processor / AI accelerator
   Efficient DNN or ISP processing, but may require a separate host and safety MCU

3. Automotive central compute
   Multi-camera/radar/lidar domain controller, usually high cost and power

4. Prototype SBC / industrial AI module
   Useful for model development but not evidence of automotive compliance
```

A processor advertised as “automotive,” an AEC-Q100 IC, and a complete ISO 26262-capable ECU are not equivalent. Qualification must be checked at the **exact orderable part, board, BSP, PMIC, memory and software-package level**.

## Folder contents

| File / folder | Purpose |
|---|---|
| `01_ADVIS_Compute_Architecture_And_Selection_Strategy.md` | Portable compute architecture, abstraction boundaries and down-selection method |
| `02_Automotive_ADAS_SoC_Master_Reference.md` | Ranked 60-platform master reference from entry smart-camera SoCs to premium central compute and prototype devices |
| `03_Prototype_And_Low_Cost_Compute_Platforms.md` | Cheapest usable boards, accelerators and host-plus-NPU combinations |
| `04_Manufacturers_Startups_And_Regional_Ecosystem.md` | Global vendors, emerging suppliers and less-utilized candidates |
| `05_Camera_Radar_And_Sensor_Interface_Compatibility.md` | Camera/SerDes/radar/CAN/Ethernet/PCIe requirements and portability rules |
| `06_Software_Toolchain_OS_And_Model_Portability.md` | TIDL, RKNN, eIQ, CVflow, R-Car, TensorRT, Hailo and portable model workflow |
| `07_Functional_Safety_Cybersecurity_And_Qualification.md` | AEC-Q100, ISO 26262, ISO 21434, safety islands and evidence checklist |
| `08_ADVIS_Workload_And_Feature_Scaling_Matrix.md` | Compute envelopes for DMS, Forward Vision, radar fusion and surround |
| `09_Supplier_RFQ_And_Evaluation_Checklist.md` | Exact commercial, technical, safety and software questions |
| `10_Recommended_Procurement_And_Benchmark_Plan.md` | Immediate boards/RFQs and objective benchmark sequence |
| `11_BOM_Power_Thermal_And_Lifecycle_Guide.md` | Complete usable compute cost and production constraints |
| `data/` | CSV copies of the master list, prices, manufacturers and feature-fit matrix |
| `sources/Official_And_Supplier_Source_Index.md` | Official product, documentation and sourcing links |

## Current ADVIS recommendation

1. **Do not replace the working RK3588 prototype path immediately.** Keep Vicharak AXON for rapid Linux/RKNN development and dataset/model validation.
2. **Use TDA4VM/AM68A-class hardware as the migration and headroom platform**, because the current ECU architecture and camera path are already aligned with it.
3. **Benchmark TDA4VL-Q1 as the first production cost-down candidate**, but only after the complete Forward Vision + DMS workload runs at target frame rates, temperature and latency.
4. Run a parallel production RFQ and technical benchmark for **Renesas R-Car V3H/V4M, Ambarella CV22FS/CV2FS, Nextchip APACHE5/next generation, and Hailo-8 automotive plus a safety-capable host**.
5. Keep **AM62A7-Q1** for DMS-only, fleet, or aggressively reduced warning features unless the shared dual-camera workload proves acceptable.
6. Use **TDA4AL/TDA4VE/TDA4VM or R-Car V4M** when 4 TOPS is insufficient or radar fusion and future camera expansion must be retained.
7. Reserve **TDA4AP/VH, R-Car V4H, Snapdragon Ride, Horizon Journey 5/6 and NVIDIA DRIVE** for multi-camera domain controllers, premium L2+ or benchmark/reference work.
8. Treat **Mobileye EyeQ** as a complete closed-stack alternative/competitor, not as an open ADVIS compute target.
9. Treat RK3588, Jetson, Axera, Sophgo, Raspberry Pi/Hailo and Coral as **prototype-only** unless a separate automotive productization and safety programme is established.

## Recommended compute ladder

| ADVIS stage | Candidate class | Intended workload |
|---|---|---|
| `C0 — Software PoC` | RK3588 / Jetson / x86 | Model development, visualization, logging and rapid integration |
| `C1 — Entry automotive` | AM62A7-Q1 / TDA4VEN / APACHE5 / Hailo-15 | DMS-only or reduced single-camera warning functions |
| `C2 — Dual-vision smart ECU` | TDA4VL / TDA4AL / R-Car V3H / CV22FS-CV2FS | Forward Vision + DMS, CAN-FD, diagnostics and safety supervision |
| `C3 — Fusion ECU` | TDA4VM / R-Car V4M / Ambarella CV3 / Hailo-8+host | Dual camera + radar fusion, richer logging and future feature headroom |
| `C4 — Surround domain` | TDA4AP/VH / R-Car V4H / Journey 6 / Ride / DRIVE | 4–8 cameras, multiple radars, parking and L2+ |

## Selection rule

Compare the complete usable compute platform cost:

> SoC + PMIC + LPDDR/eMMC/NOR + safety MCU/island + clock + Ethernet/CAN PHYs + camera deserializers + PCB layers + cooling + BSP/SDK licences + compiler/tool licences + model-porting effort + safety manuals + cybersecurity support + lifecycle + PPAP + supplier engineering support.

A cheap NPU or a high headline TOPS number does not automatically produce the lowest-cost ADAS ECU.

## Data status

- Global scan date: **20 July 2026**
- Master reference: **60 SoCs, processors and accelerator paths**
- Manufacturer map: **22 vendors/ecosystems**
- Public board and price observations: **25 entries**
- AI performance numbers are vendor-stated and are not directly comparable across precision, sparsity, accelerator utilization or benchmark conditions.
- RFQ-only entries require NDA-level confirmation before architecture freeze.

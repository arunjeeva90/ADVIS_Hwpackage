# 13 - OEM Customization

## Purpose

This folder defines how the ADVIS platform scales and customizes for different OEM requirements. The modular architecture enables multiple product variants from a single carrier, sensor and software architecture.

Camera, radar and compute selections in this folder are **vendor-agnostic**. TI platforms are current implementation candidates, not a permanent platform lock. Products are adapted through normalized camera, radar, compute-runtime and vehicle-interface boundaries using standard MIPI CSI-2, FPD-Link, GMSL, USB, CAN-FD, Automotive Ethernet, PCIe and portable model formats where practical.

## Sub-folders

| Folder | Contents |
|--------|----------|
| Variant_Matrix/ | Full matrix of platform variants vs. features/components |
| Automotive_SoC_And_Compute_Platform_Options/ | Vendor-neutral automotive SoC, AI accelerator, prototype-board, pricing, safety and ADVIS workload reference |
| Feature_Scaling_Tiers/ | Entry / Mid / High tier definitions |
| Customer_Requirements/ | Per-OEM requirement capture and compliance tracking |
| Forward_Vision_Sensor_Options/ | SoC-agnostic forward-camera sensor, module and sourcing reference |
| DMS_OMS_In_Cabin_Sensor_Options/ | SoC-agnostic DMS/OMS camera, NIR and sourcing reference |
| Radar_Sensor_And_Module_Options/ | SoC-agnostic front, corner, imaging, prototype and DIY radar reference |

## Platform Scaling Tiers

### Entry Tier
- One or two cameras depending measured workload
- AM62A/TDA4VEN/APACHE5/Hailo-class compute or equivalent
- DMS, OMS, fleet monitoring or reduced warning ADAS
- CAN/CAN-FD monitoring
- Passive cooling
- Lowest recurring BOM target

### Mid Tier — Dual-Vision Smart ECU
- Forward camera + DMS camera
- TDA4VL/TDA4AL, R-Car V3H, Ambarella CV22FS/CV2FS or equivalent
- Shared Forward Vision + DMS runtime
- CAN-FD, diagnostics, optional GNSS/IMU
- Passive cooling preferred
- Primary ADVIS Assist/Control cost-performance tier

### Fusion Tier
- Two to six cameras plus front/corner radar inputs
- TDA4VM, R-Car V4M, Ambarella CV3 or equivalent
- CAN-FD + Automotive Ethernet
- Camera-radar fusion, richer logging and future feature headroom
- Passive or active cooling according to enclosure and ambient targets

### High Tier — Surround / L2+
- Four to twelve or more cameras
- TDA4AP/VH, R-Car V4H, Snapdragon Ride, Horizon Journey, NVIDIA DRIVE or equivalent
- Multiple radars and optional lidar/V2X
- Multi-gigabit Automotive Ethernet
- Active cooling normally required
- Surround perception, parking and premium L2+ domain-controller scope

## Compute Compatibility Matrix

The table below is illustrative. Detailed current options, prices, software ecosystems, qualification status and workload fit are maintained under `Automotive_SoC_And_Compute_Platform_Options/`.

| Compute class | Typical camera scope | Vendor-stated AI range | ADVIS tier |
|---|---:|---:|---|
| AM62A / TDA4VEN / APACHE5 class | 1–2 | ~1.5–4 TOPS | Entry |
| TDA4VL / TDA4AL / R-Car V3H / CV22FS class | 2 | ~4–8 effective TOPS or vendor CV engine | Dual Vision |
| TDA4VM / R-Car V4M / CV3 class | 2–6 | ~8–24 TOPS | Fusion |
| TDA4AP/VH / R-Car V4H / Journey / Ride / DRIVE class | 4–12+ | ~24–1000+ TOPS | Surround / L2+ |

TOPS values are not directly comparable across precision, sparsity, accelerator utilization, memory bandwidth or supported operators. Selection must be based on the complete ADVIS workload running at target latency, temperature and power.

## Customization Without Redesign

The platform architecture allows these customizations through BOM, carrier, harness, adapter, runtime and configuration changes:

- Compute module/SoC class behind a normalized ADVIS platform adapter
- Camera count and sensor class
- Native MIPI, FPD-Link, GMSL, Ethernet or USB prototype camera transport
- Front radar, rear corner radar pair, four-corner radar set or no radar
- CAN-FD object-list radar or Automotive-Ethernet point-cloud radar
- Model compiler/runtime backend while preserving a common model source and validation set
- Linux/QNX/AUTOSAR/RTOS partitioning according to SoC and safety concept
- CAN termination and OEM-specific DBC/diagnostic mapping
- GNSS/IMU population and synchronization method
- IR illumination and DMS/OMS feature population
- Memory/storage population, cooling and feature unlocks

## Portability Rule

ADVIS portability is not achieved by claiming that one binary runs on every SoC. It is achieved by freezing:

1. sensor and vehicle interface contracts,
2. timestamp and coordinate conventions,
3. common perception tensor and metadata contracts,
4. safety/capability outputs,
5. model-source and validation datasets,
6. a replaceable SoC-specific BSP, camera adapter and inference backend.

Every production SoC candidate must still pass the same ADVIS benchmark, thermal, functional-safety, cybersecurity and lifecycle gates before selection.

# 13 - OEM Customization

## Purpose

This folder defines how the ADVIS platform scales and customizes for different OEM requirements. The modular architecture enables multiple product variants from a single carrier design.

Sensor and radar selections in this folder are **SoC-agnostic**. TI platforms are current implementation candidates, not a permanent platform lock. Camera and radar products are adapted through normalized HALs and standard MIPI/SerDes/USB/CAN-FD/Automotive-Ethernet interfaces.

## Sub-folders

| Folder | Contents |
|--------|----------|
| Variant_Matrix/ | Full matrix of platform variants vs. features/components |
| SoC_Option_Packages/ | Supported SoC modules and their capability profiles |
| Feature_Scaling_Tiers/ | Entry / Mid / High tier definitions |
| Customer_Requirements/ | Per-OEM requirement capture and compliance tracking |
| Forward_Vision_Sensor_Options/ | SoC-agnostic forward-camera sensor, module and sourcing reference |
| DMS_OMS_In_Cabin_Sensor_Options/ | SoC-agnostic DMS/OMS camera, NIR and sourcing reference |
| Radar_Sensor_And_Module_Options/ | SoC-agnostic front, corner, imaging, prototype and DIY radar reference |

## Platform Scaling Tiers

### Entry Tier
- Single camera (DMS only)
- AM62A or equivalent low-cost SoC
- CAN monitoring only
- No GNSS/IMU (or GNSS only)
- Passive cooling
- Target BOM: lowest cost

### Mid Tier (Current v0.4.4 Baseline)
- Dual camera (Forward + DMS)
- TDA4VM / AM68A or equivalent SoC
- CAN-FD monitoring
- GNSS + IMU fusion
- Passive or active cooling
- Full feature set

### High Tier
- 4-8 cameras (surround view + DMS)
- TDA4VH, Qualcomm, Renesas, NVIDIA, Ambarella, NXP or equivalent high-performance platform
- Multi-CAN + Automotive Ethernet
- Optional front/corner/imaging radar set
- GNSS + IMU + V2X
- Active cooling as required
- L2+ perception capable

## SoC Compatibility Matrix

The table below is illustrative. Detailed and current options are maintained under `SoC_Option_Packages/`.

| SoC Family | Camera Inputs | AI Performance | Power Budget | Tier |
|------------|---------------|----------------|--------------|------|
| AM62A or equivalent | 1 | Low | <5W | Entry |
| AM68A / TDA4VM or equivalent | 2-4 | Medium | 10-15W | Mid |
| TDA4VH / R-Car / CV3 class | 4-8 | High | 20-30W | High |
| Qualcomm SA8295 / NVIDIA DRIVE class | 8+ | Very High | 25-40W+ | High+ |

## Customization Without Redesign

The platform architecture allows these customizations through BOM, harness, interface and configuration changes:

- Camera count and sensor class
- Native MIPI, FPD-Link, GMSL, Ethernet or USB prototype camera transport
- Front radar, rear corner radar pair, four-corner radar set or no radar
- CAN-FD object-list radar or Automotive-Ethernet point-cloud radar
- CAN termination (end-node vs. mid-bus via DNI resistors)
- GNSS antenna bias (active vs. passive antenna support)
- IR illumination (populate or omit daughterboard connector)
- Boot mode (strap resistor swap for different boot media)
- Feature unlocks and OEM-specific calibration without changing the normalized camera/radar HAL contracts

# 13 - OEM Customization

## Purpose

This folder defines how the IND-VIAS platform scales and customizes for different OEM requirements. The modular architecture enables multiple product variants from a single carrier design.

## Sub-folders

| Folder | Contents |
|--------|----------|
| Variant_Matrix/ | Full matrix of platform variants vs. features/components |
| SoC_Option_Packages/ | Supported SoC modules and their capability profiles |
| Feature_Scaling_Tiers/ | Entry / Mid / High tier definitions |
| Customer_Requirements/ | Per-OEM requirement capture and compliance tracking |

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
- TDA4VM / AM68A SoC
- CAN-FD monitoring
- GNSS + IMU fusion
- Passive or active cooling
- Full feature set

### High Tier
- 4-8 cameras (surround view + DMS)
- TDA4VH or multi-SoM configuration
- Multi-CAN + Automotive Ethernet
- GNSS + IMU + V2X
- Active cooling required
- L2+ perception capable

## SoC Compatibility Matrix

| SoC Family | Camera Inputs | AI Performance | Power Budget | Tier |
|------------|---------------|----------------|--------------|------|
| AM62A | 1 | Low | <5W | Entry |
| AM68A / TDA4VM | 2-4 | Medium | 10-15W | Mid |
| TDA4VH | 4-8 | High | 20-30W | High |
| Qualcomm SA8295 | 8+ | Very High | 25-40W | High+ |

## Customization Without Redesign

The platform architecture allows these customizations via BOM/config changes only:
- Camera count (populate/depopulate deserializer channels)
- CAN termination (end-node vs. mid-bus via DNI resistors)
- GNSS antenna bias (active vs. passive antenna support)
- IR illumination (populate or omit daughterboard connector)
- Boot mode (strap resistor swap for different boot media)

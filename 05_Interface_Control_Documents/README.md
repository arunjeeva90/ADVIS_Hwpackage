# 05 - Interface Control Documents (ICDs)

## Purpose

ICDs define the exact electrical, mechanical, and protocol boundaries between subsystems. These are the contracts that allow modular development and multi-vendor integration.

## Sub-folders

| Folder | Contents |
|--------|----------|
| SoM_Carrier_ICD/ | Defines the SoM-to-carrier connector interface (THE key platform IP) |
| Camera_ICD/ | Camera module interface: connector, cable, power, data rate, shielding |
| Vehicle_Connector_ICD/ | J100 vehicle harness interface: power, ignition, wake, ground |
| IR_Daughterboard_ICD/ | J800 IR illumination board interface: power, control, fault |
| Pin_Mux_Maps/ | SoC pin multiplexing allocations per variant |

## ICD Status

| ICD | Status |
|-----|--------|
| SoM-Carrier | Logical signals defined; physical pin numbers PENDING |
| Camera | PENDING - waiting for camera module vendor ICD |
| Vehicle Connector | Intent defined; exact connector PN to finalize |
| IR Daughterboard | Signal list defined; connector PN selected (8-pin) |
| Pin Mux Maps | PENDING - requires SOM pinout document |

## Why ICDs Are IP

The SoM-Carrier ICD is the most critical IP document in this platform. It defines:
- Which signals cross the SoM boundary
- Power rail requirements for any compatible SoM
- Sequencing requirements
- Mechanical constraints

Any SoM vendor wanting to be compatible with the IND-VIAS carrier must conform to this ICD. This creates platform lock-in and ecosystem value.

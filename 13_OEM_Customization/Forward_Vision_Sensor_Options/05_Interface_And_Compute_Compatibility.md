# Interface and Compute Compatibility

## Core rule

A camera sensor is not intrinsically tied to TI, NVIDIA, Qualcomm, Renesas, Ambarella, NXP, Rockchip, Horizon, Axera, Black Sesame or another compute vendor.

Compatibility depends on:

- Physical receiver and transport
- CSI-2 lane count and lane rate
- RAW data type and bit depth
- Bayer/RCCB/RCCC pattern
- HDR/PWL/decompanding support
- Driver and ISP tuning
- Frame synchronization and safety diagnostics

| Transport option | Universal architecture | Compatible compute families | Advantages | Constraints |
| --- | --- | --- | --- | --- |
| Native MIPI CSI-2 RAW | Sensor connects to SoC CSI receiver when electrical lanes, data type, clock, bit depth and ISP/PWL support match. | TI Jacinto/AM6x, NVIDIA Jetson, Qualcomm Ride, Renesas R-Car, Ambarella CV, NXP vision processors, Rockchip, Horizon, Axera, Black Sesame, Nextchip and others | Lowest camera BOM and latency | Short cable only; custom driver, ISP tuning and EMC design required |
| FPD-Link III camera | Sensor MIPI → serializer at camera → coax/STP → deserializer → MIPI CSI-2 to SoC. | Any SoC with compatible CSI receiver behind a matching TI deserializer/bridge | Automotive cable reach, PoC, diagnostics and EMI robustness | Not TI-SoC-specific; TI brand applies to SerDes transport only |
| GMSL2/GMSL3 camera | Sensor MIPI → Maxim/ADI serializer → coax → deserializer → CSI-2 to SoC. | Any SoC with compatible CSI receiver behind the selected ADI deserializer | Large camera-module ecosystem; rugged prototypes | Serializer/deserializer generations and drivers must match |
| Automotive Ethernet camera | Camera performs local ISP/compression and streams via 100/1000BASE-T1. | Any SoC/domain controller with Ethernet, decoder and time-sync support | Long cable, scalable architecture, zonal/domain ECUs | Added camera compute, latency, compression and software complexity |
| USB/UVC prototype camera | Camera module includes bridge/ISP and presents standard USB video. | Windows/Linux boards including AXON, Jetson, x86, RK3588 and many development platforms | Fastest algorithm/demo bring-up | Usually not deterministic, not automotive, and RAW/exposure control may be restricted |
| Parallel DVP/LVDS sensor | Sensor uses legacy parallel or vendor LVDS interface; bridge/FPGA may convert to CSI-2. | SoCs with native DVP/LVDS or external bridge support | Low-cost/legacy sensors and custom research | Less universal; board routing and driver effort can exceed sensor savings |

## Compute-family examples

The same camera can be adapted to multiple compute families when a supported transport and ISP path exists:

- TI Jacinto / AM6x
- NVIDIA Jetson / DRIVE development platforms
- Qualcomm Ride / Snapdragon automotive platforms
- Renesas R-Car
- Ambarella CV families
- NXP vision-capable processors and accelerators
- Rockchip RK/RV prototype platforms
- Horizon Robotics Journey
- Axera
- Black Sesame Technologies
- Nextchip Apache
- x86/Linux development systems

Do not claim compatibility merely because the SoC has MIPI CSI-2. The exact sensor output mode, receiver limits, ISP support and software driver must be validated.

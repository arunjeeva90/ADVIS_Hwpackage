# Interface, Output and Compute Compatibility

## 1. Compatibility principle

Radar portability is determined mainly by the **sensor output boundary**, not by the central SoC brand.

| Radar output | SoC portability | Data richness | Integration effort | Production recommendation |
|---|---:|---:|---:|---|
| CAN object list | Very high | Medium | Low | Preferred minimum interface |
| CAN-FD object/detection list | Very high | Medium-high | Low-medium | Preferred cost/product interface |
| 100BASE-T1 detections/point cloud | High | High | Medium | Preferred rich-fusion interface |
| 1000BASE-T1 radar cube | Medium-high | Very high | High | Imaging radar / recording / R&D |
| USB-UVC-like / USB serial | High for Linux prototypes | Low-medium | Low | Prototype only |
| UART/SPI module output | High for MCU/bench | Low | Low | DIY/near-field only |
| MIPI CSI-2 raw ADC | Low-medium | Very high | Very high | Custom radar design |
| LVDS raw ADC + capture card | Low | Very high | Very high | Laboratory only |

## 2. Central compute compatibility

A smart CAN-FD or Ethernet radar can be fused by:

- TI TDA4VM/TDA4VL/TDA4VH and AM62A
- NXP S32G/S32R and i.MX platforms
- Renesas R-Car V4H/V4M and related automotive SoCs
- Qualcomm Snapdragon Ride
- NVIDIA DRIVE Orin
- Ambarella CV3/CV7 families
- Horizon Robotics Journey
- Rockchip and other Linux SoCs for prototype
- x86/PC/ROS2 development systems
- A small standalone MCU for warning-only corner functions

Required host capabilities are modest for CAN object-list fusion. Dense point-cloud and radar-cube processing require much more memory bandwidth, Ethernet and accelerator/CPU performance.

## 3. CAN-FD contract

Recommended ADVIS messages:

| Message group | Contents |
|---|---|
| Radar status | software version, mode, temperature, voltage, blockage, interference, internal fault |
| Frame header | timestamp, frame counter, object count, detection count and cycle status |
| Object data | ID, position, velocity, acceleration, existence, covariance/quality and flags |
| Detection data optional | range, angle, radial velocity, RCS/SNR and quality |
| Configuration | mode, range/FoV profile, mounting pose, output filter and update rate |
| Diagnostics | DTC, snapshot, reset, reprogramming and calibration status |

Use:
- alive counters
- CRC/E2E
- explicit invalid values
- timeout monitoring
- endian/scaling definition
- deterministic object truncation rule
- documented coordinate frame

## 4. Ethernet contract

For 100BASE-T1/1000BASE-T1:
- UDP is common for high-rate detections/point cloud.
- SOME/IP may be used for service-oriented production integration.
- PTP/gPTP or a hardware trigger should align camera and radar time.
- Define packet sequence, fragmentation, loss behaviour and data-age limits.
- Separate engineering raw-data streams from safety-relevant object streams.
- Protect configuration/update paths with cybersecurity controls.

## 5. Radar-to-camera fusion requirements

The adapter shall provide:
- sensor-to-vehicle extrinsic transform
- synchronized time
- ego velocity/yaw rate
- consistent covariance
- radar track age and source
- association gates
- sensor disagreement reason
- fallback state

Camera functions:
- object class
- lane and road association
- traffic-sign/semantic context
- vulnerable-road-user appearance
- stationary object relevance

Radar functions:
- metric range
- radial velocity
- weather/visibility robustness
- approach speed
- crossing motion
- independent confirmation of camera TTC

## 6. Platform-specific caution

- A radar module with CAN is not automatically open; many expose only warning bits.
- An Ethernet port does not guarantee point-cloud access; vendor licences may restrict data.
- TI/NXP/Infineon EVKs expose development data but require a complete product around them.
- Used OEM radars may require proprietary vehicle messages before they transmit.
- Raw radar algorithms, antenna calibration and tracking are safety-relevant and cannot be treated as a generic driver swap.

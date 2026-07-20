# ADVIS Compute Architecture and Selection Strategy

## 1. Product objective

The compute platform must support the same ADVIS software and sensor architecture across multiple price and feature tiers:

```text
Forward HDR camera
+ DMS NIR camera
+ optional smart radars
+ future surround cameras
        ↓
Portable sensor services and synchronized frame transport
        ↓
Portable pre-processing and model-runtime boundary
        ↓
ADAS perception + DMS + fusion + confidence
        ↓
Function-specific safety gates
        ↓
CAN-FD / Automotive Ethernet / HMI / OEM controllers
```

The SoC is replaceable. The sensor contracts, model behaviour, diagnostics and vehicle outputs are the long-life product interfaces.

## 2. Required abstraction layers

### 2.1 Board Support and Sensor HAL

Abstract:

- camera power/reset and SerDes programming
- CSI-2 virtual channels
- exposure, gain, HDR/PWL and NIR strobe
- timestamps and frame counters
- CAN-FD and Ethernet
- GPIO, watchdog, EEPROM, GNSS and IMU
- PMIC health and thermal sensors

### 2.2 Image and tensor contract

Freeze canonical formats before vendor-specific acceleration:

- RAW12/RAW16 or PWL input metadata
- NV12/YUV and RGB tensors
- lens distortion and crop metadata
- calibration version
- tensor layout, quantization scale/zero point and dynamic shape policy
- object, lane, depth, DMS and quality outputs

### 2.3 Model-runtime adapter

Implement adapters such as:

```text
ONNX reference runtime
├── TI TIDL / OpenVX
├── Renesas DRP-AI / R-Car runtime
├── NXP eIQ / Neutron
├── Ambarella CVflow
├── NVIDIA TensorRT / DLA
├── Qualcomm SNPE / Ride SDK
├── Horizon BPU toolchain
├── Hailo Dataflow Compiler / HailoRT
├── Nextchip SDK
└── Rockchip RKNN
```

The reference model must remain trainable and testable outside any vendor compiler.

### 2.4 Safety and capability boundary

The AI result is never directly equated with a vehicle function. Every platform shall expose:

- data age and execution time
- model/version identity
- inference success and accelerator fault
- input-image quality
- calibration health
- confidence/covariance
- thermal and power throttling state
- feature capability state
- deterministic timeout behaviour

## 3. Selection gates

A candidate is not approved by TOPS alone. It must pass:

1. Two-camera ingest at required bit depth and frame rate.
2. Forward and DMS pipelines concurrently without skipped safety cycles.
3. Sensor-to-output latency under the ADVIS target.
4. Worst-case 85–105°C junction/ambient strategy.
5. Real model compilation without unacceptable fallback to CPU.
6. Memory bandwidth and capacity under logging/OTA load.
7. Hardware safety mechanisms and supplier safety manual.
8. Secure boot, authenticated update, key storage and debug control.
9. QNX/Linux/RTOS/AUTOSAR partition feasibility.
10. Camera sensor/SerDes drivers and ISP tuning ownership.
11. CAN-FD and Automotive Ethernet support.
12. Minimum 10–15 year lifecycle or written programme support.
13. Exact part availability in India/ASEAN and second-source risk.
14. Complete recurring BOM and NRE.
15. Supplier willingness to support fault injection, PPAP and production issues.

## 4. Platform classes

### Class A — Integrated automotive smart-camera SoC

Includes ISP, NPU/CV accelerators, Arm application cores, real-time/safety island and automotive interfaces.

Preferred for the first ADVIS product because it minimizes BOM and latency.

Examples:

- TI TDA4VL/TDA4AL
- Renesas R-Car V3H/V4M
- Ambarella CV22FS/CV2FS
- Nextchip APACHE5

### Class B — Host plus automotive AI accelerator

A host provides camera/vehicle/safety services and a low-power accelerator runs neural networks.

Examples:

- NXP i.MX95 + Hailo-8 automotive
- safety-capable host + DEEPX DX-M1 automotive-grade option
- TI/NXP host + PCIe accelerator

This can be cost-effective, but adds PCIe, memory movement, boot, watchdog and supplier-integration complexity.

### Class C — Automotive central compute

Designed for many cameras, radars and mixed-critical workloads.

Examples:

- TDA4AP/VH
- R-Car V4H
- Snapdragon Ride/Flex
- NVIDIA DRIVE
- Horizon Journey 5/6

Use only when the sensor set and feature roadmap justify the cost, power and validation load.

### Class D — Prototype compute

RK3588, Jetson, Axera, Sophgo, Raspberry Pi/Hailo, Coral and x86.

Use for development and model benchmarking. Do not use their results as evidence for automotive qualification.

## 5. ADVIS down-selection scorecard

| Category | Weight |
|---|---:|
| Real ADVIS workload performance and latency | 22% |
| Complete production BOM | 18% |
| Functional safety evidence and partitioning | 15% |
| Camera/ISP/SerDes readiness | 12% |
| Software portability and tool maturity | 10% |
| Power and thermal margin | 8% |
| Lifecycle, supply and regional support | 7% |
| Cybersecurity and OTA support | 5% |
| Future radar/surround scalability | 3% |

## 6. Mandatory benchmark

Every candidate shall run the same package:

- Forward object/lane/road/quality network
- object-centric depth/TTC
- tracking and fusion
- face/head/eye/gaze network
- phone/seatbelt/driver-state tasks
- image-quality and camera-blockage monitors
- CAN/Ethernet input and output
- event logging
- watchdog and thermal telemetry

Report:

- FPS, p50/p95/p99 latency
- NPU/DSP/CPU utilization
- DDR bandwidth and peak memory
- power at idle/nominal/worst case
- temperature and throttling
- model accuracy delta from ONNX reference
- unsupported operators and CPU fallbacks
- camera drops and timestamp jitter
- boot time and recovery behaviour

## 7. Decision philosophy

Start with one working platform, but preserve architectural portability.

The current pragmatic sequence is:

```text
RK3588 prototype
        ↓
TDA4VM migration/headroom implementation
        ↓
TDA4VL cost-down benchmark
        ↓
R-Car / Ambarella / Nextchip / Hailo challenger benchmark
        ↓
Production selection from measured scorecard
```

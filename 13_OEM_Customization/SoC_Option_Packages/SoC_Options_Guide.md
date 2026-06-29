# ADVIS SoC Option Packages Guide

## 1. Purpose

This guide helps OEM customers select the appropriate SoC tier for their ADVIS integration. Each option package defines the compute capability, camera support, power budget, and software ecosystem available.

---

## 2. SoC Options Overview

| Parameter | AM62A (Entry) | TDA4VL-Q1 (Assist) | AM68A / TDA4VM (Control) | TDA4VH (High) |
|-----------|---------------|---------------------|---------------------|----------------|
| **AI Performance** | 2 TOPS (per AM62A7 product headline) | 4 TOPS (per TDA4VL-Q1 product headline, H speed grade) | 8 TOPS (per TDA4VM product headline) | 32 TOPS |
| **CPU Cores** | 1x Cortex-A53 | 2x Cortex-A72 | 2x Cortex-A72 | 4x Cortex-A72 |
| **CPU Clock** | 1.4 GHz | 1.2 GHz | 2.0 GHz | 2.0 GHz |
| **Safety MCU** | Cortex-M4F | Cortex-R5F (4 cores) | Cortex-R5F (6 cores) | 2x Cortex-R5F |
| **Camera Support** | 1 (CSI-2, 2-lane) | 2 (CSI-2, 4-lane) | 2-4 (CSI-2, 4-lane) | 4-8 (multiple CSI-2) |
| **Max Resolution** | 5MP | 8MP | 8MP | 8MP per port |
| **Memory** | 1-2GB LPDDR4 | 2-4GB LPDDR4 | 2-4GB LPDDR4 | 4-8GB LPDDR4x |
| **Storage** | 4-8GB eMMC | 16-32GB eMMC | 16-32GB eMMC | 32-64GB eMMC |
| **Power Budget** | <5W | <8W | 10-15W | 20-30W |
| **Package** | 18x18mm | 23x23mm | 23x23mm (TDA4VM: 24x24mm) | 29x29mm |
| **Automotive Grade** | AEC-Q100 Grade 2 | AEC-Q100 Grade 2 | AEC-Q100 Grade 2 | AEC-Q100 Grade 2 |
| **Temperature** | -40 to +125C | -40 to +125C | -40 to +105C | -40 to +105C Tj |

**Comparison Candidates (not automatically selected for ADVIS):**
- TDA4AL-Q1: 8 TOPS, no GPU, video encode only, analytics-focused
- TDA4VE-Q1: 8 TOPS, GPU, higher resources than TDA4VL-Q1

---

## 3. AM62A - Entry Tier

### 3.1 Capability Profile

| Attribute | Specification |
|-----------|--------------|
| **Target Application** | Single-camera DMS, basic monitoring |
| **AI Accelerator** | 1x C7x DSP (limited DL) |
| **Vision Processing** | Hardware ISP for single camera |
| **Concurrent DNNs** | 1 (DMS only) |
| **Inference Frame Rate** | 30fps single model |
| **Video Encode** | H.264 1080p30 |

### 3.2 Camera Support

| Configuration | Supported |
|---------------|-----------|
| 1x 2MP @ 30fps (DMS) | Yes |
| 1x 5MP @ 15fps | Yes |
| 2x cameras simultaneous | No (insufficient bandwidth/compute) |
| FPD-Link III (via UB954) | Yes (single port) |
| Direct MIPI CSI-2 | Yes (preferred for cost-down) |

### 3.3 Memory Configuration

| Parameter | Specification |
|-----------|--------------|
| LPDDR4 | 1-2GB (16-bit, single channel) |
| eMMC | 4-8GB (Linux rootfs + application) |
| External storage | MicroSD (log files, updates) |
| Bandwidth | Sufficient for single camera pipeline |

### 3.4 Power Budget

| State | Power |
|-------|-------|
| Idle (Linux booted, no inference) | ~1.5W |
| Active (DMS inference @ 30fps) | ~3.5W |
| Maximum (all peripherals active) | ~5W |
| Thermal solution required | Natural convection (no heatsink at <50C ambient) |

### 3.5 Software Ecosystem

| Component | Availability |
|-----------|-------------|
| Linux kernel | TI Processor SDK (upstream mainline) |
| AI runtime | TIDL (TI Deep Learning) |
| Camera framework | V4L2 / GStreamer |
| CAN stack | SocketCAN |
| Build system | Yocto (Dunfell/Kirkstone) |
| Debug tools | CCS, GDB, trace |

### 3.6 Carrier Compatibility

The AM62A SOM connects to the ADVIS carrier via the standard SOM interface connector. When used in Entry configuration:
- Forward camera port DNI (or single port only on UB954)
- Reduced power delivery (LM61460 operates at ~1A average)
- GNSS/IMU components optional (DNI for minimum cost)
- Same carrier PCB as Mid tier (BOM variant only)

---

## 4. AM68A / TDA4VM - Mid Tier (Baseline)

### 4.1 Capability Profile

| Attribute | Specification |
|-----------|--------------|
| **Target Application** | Dual-camera ADAS + DMS, full safety advisory |
| **AI Accelerator** | C7x DSP + MMA (Matrix Multiply Accelerator) |
| **Vision Processing** | Dual ISP, hardware stereo (if needed) |
| **Concurrent DNNs** | 2-3 (ADAS + DMS + optional tracking) |
| **Inference Frame Rate** | 2x 30fps concurrent models |
| **Video Encode** | H.264/H.265 1080p60 |

### 4.2 Camera Support

| Configuration | Supported |
|---------------|-----------|
| 2x 2MP @ 30fps (Forward + DMS) | Yes (primary use case) |
| 2x 5MP @ 30fps | Yes |
| 4x 2MP @ 30fps | Yes (with additional deserializer) |
| FPD-Link III dual-port (UB954) | Yes (recommended) |
| Direct MIPI CSI-2 (4-lane) | Yes (Track 1 cost-down) |
| Virtual channel multiplexing | Yes (VC0 + VC1 on single CSI-2) |

### 4.3 Memory Configuration

| Parameter | Specification |
|-----------|--------------|
| LPDDR4 | 2-4GB (32-bit, dual channel) |
| eMMC | 16-32GB (OS + application + model storage) |
| External storage | MicroSD (logs, updates, diagnostics) |
| Bandwidth | 12.8 GB/s (sufficient for dual camera + DNN) |

### 4.4 Power Budget

| State | Power |
|-------|-------|
| Idle (Linux booted, no inference) | ~4W |
| Active (dual inference @ 30fps) | ~12W |
| Maximum (all peripherals, peak AI load) | ~18W |
| Thermal solution required | Passive heatsink (aluminum, ~10C/W) |

### 4.5 Software Ecosystem

| Component | Availability |
|-----------|-------------|
| Linux kernel | TI Processor SDK Linux (6.x) |
| AI runtime | TIDL + TVM (model compilation) |
| Vision SDK | TI Vision Apps (OpenVX-based) |
| Camera framework | V4L2 / GStreamer / OpenCV |
| RTOS (R5F) | FreeRTOS / TI-RTOS |
| CAN stack | SocketCAN (Linux) + MCAN (RTOS) |
| GNSS/IMU drivers | Standard Linux subsystem |
| Build system | Yocto (Kirkstone), Docker-based |
| Debug tools | CCS, JTAG, ETM trace, UART console |
| Model tools | TIDL model compilation, ONNX import |

### 4.6 Carrier Compatibility

The AM68A/TDA4VM is the baseline SOM for ADVIS v0.4.4 carrier design:
- All carrier interfaces fully utilized
- Full dual-camera capability via DS90UB954-Q1
- All peripherals populated (GNSS, IMU, CAN, IR, USB)
- Passive thermal solution (heatsink on SOM module)
- Standard form factor carrier PCB

---

## 5. TDA4VH - High Tier

### 5.1 Capability Profile

| Attribute | Specification |
|-----------|--------------|
| **Target Application** | Multi-camera surround view, sensor fusion |
| **AI Accelerator** | Enhanced C7x + MMA (4x mid-tier throughput) |
| **Vision Processing** | Multi-ISP, hardware stereo, optical flow |
| **Concurrent DNNs** | 6-8 (multi-camera + tracking + planning) |
| **Inference Frame Rate** | 4-8x 30fps concurrent models |
| **Video Encode** | H.264/H.265 4K30 or multi-stream 1080p |

### 5.2 Camera Support

| Configuration | Supported |
|---------------|-----------|
| 2x 2MP @ 30fps | Yes (minimum config) |
| 4x 2MP @ 30fps (surround) | Yes |
| 8x 2MP @ 30fps (full surround + DMS) | Yes |
| 2x 8MP @ 30fps (high-res forward + rear) | Yes |
| Multiple deserializers (UB954/UB960) | Yes |
| Direct MIPI CSI-2 (multiple ports) | Yes |

### 5.3 Memory Configuration

| Parameter | Specification |
|-----------|--------------|
| LPDDR4x | 4-8GB (64-bit, quad channel) |
| eMMC | 32-64GB (OS + multi-model storage) |
| External storage | MicroSD + NVMe (optional via M.2) |
| Bandwidth | 25.6 GB/s (multi-camera + multi-DNN) |

### 5.4 Power Budget

| State | Power |
|-------|-------|
| Idle (Linux booted, no inference) | ~8W |
| Active (multi-camera inference) | ~22W |
| Maximum (all cameras, all DNNs, radar fusion) | ~30W |
| Thermal solution required | Active cooling (fan or TEC, <5C/W) |

### 5.5 Software Ecosystem

| Component | Availability |
|-----------|-------------|
| Linux kernel | TI Processor SDK Linux (6.x) |
| AI runtime | TIDL + TVM + custom C7x kernels |
| Vision SDK | TI Vision Apps (enhanced pipeline) |
| Sensor fusion | Multi-sensor fusion framework |
| Radar interface | CAN-based object list input |
| Ethernet | TSN-capable 100BASE-T1 stack |
| Safety framework | SafeTI diagnostic library |
| Build system | Yocto (Kirkstone), Docker-based |
| Simulation | Hardware-in-the-loop (HIL) support |

### 5.6 Carrier Compatibility

The TDA4VH requires enhanced carrier features:
- Additional deserializer IC(s) populated
- Secondary CAN transceiver populated
- Ethernet PHY populated
- Active cooling interface (fan header or TEC connector)
- Extended PCB size may be required
- Higher current draw on all power rails
- Carrier PCB revision may be needed for additional routing channels

---

## 6. Migration and Upgrade Paths

```
AM62A (Entry)
    |
    | [SOM swap + BOM populate]
    | [No carrier PCB change]
    v
AM68A/TDA4VM (Mid)
    |
    | [SOM swap + additional ICs + carrier rev]
    | [May require PCB revision for routing]
    v
TDA4VH (High)
```

### 6.1 Key Migration Considerations

| Migration | Hardware Changes | Software Changes |
|-----------|-----------------|-----------------|
| Entry to Mid | SOM swap, populate GNSS/IMU/IR, enable both camera ports | Add ADAS models, enable fusion, update device tree |
| Mid to High | SOM swap, add deserializer/CAN/Ethernet, active cooling | Add surround models, enable radar fusion, multi-pipeline |

### 6.2 Software Portability Guarantees

- TIDL models compiled for AM68A run on TDA4VH (forward compatible)
- Common HAL API across all tiers (peripheral abstraction)
- Configuration-driven feature enable (no code changes for tier selection)
- Common OTA update infrastructure across all tiers

---

## 7. Selection Guide for OEMs

### 7.1 Decision Criteria

| If you need... | Select... |
|----------------|-----------|
| DMS-only, lowest cost | AM62A (Entry) |
| Dual-camera ADAS+DMS, Euro NCAP (cost-optimized) | TDA4VL-Q1 (Assist) - 4 TOPS |
| AEB/ACC/LKA request outputs | TDA4VM-Q1 (Control) - 8 TOPS |
| Fleet monitoring + driver behavior | TDA4VL-Q1 (Assist) with ADVIS Fleet |
| Multi-camera surround view | TDA4VH (High) |
| Radar fusion | TDA4VH (High) with ADVIS Fusion |
| L2+ perception platform | TDA4VH (High) |
| Fleet-lite (single-camera forward only) | AM62A (Entry) |

### 7.2 Volume Pricing Guidance

| Tier | SOM Unit Cost (10k qty) | Carrier Delta Cost |
|------|------------------------|--------------------|
| Entry (AM62A) | Low | -$21 vs baseline (DNI savings) |
| Mid (AM68A) | Moderate (reference) | $0 (baseline) |
| High (TDA4VH) | Premium | +$17.50 (additional components) |

*Contact ADVIS sales engineering for volume-specific pricing.*

---

*ADVIS Hardware Platform - OEM Customization*

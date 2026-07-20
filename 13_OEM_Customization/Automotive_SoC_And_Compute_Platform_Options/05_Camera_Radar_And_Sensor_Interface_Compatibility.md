# Camera, Radar and Sensor Interface Compatibility

## 1. Minimum interface set for ADVIS Assist

| Interface | Minimum requirement |
|---|---|
| Camera | Two synchronized camera streams through native CSI-2 or one deserializer CSI output with virtual channels |
| ISP | Automotive RAW/PWL/HDR support, RGB-IR/NIR support, exposure metadata and deterministic output |
| DMS illumination | Strobe/PWM timing support or deterministic GPIO/timer interface |
| CAN | At least one CAN-FD controller plus external automotive transceiver |
| Diagnostics | UDS transport, bootloader/update path and DTC storage |
| Storage | eMMC + boot NOR/OSPI; optional microSD only for engineering |
| Memory | ECC-capable LPDDR where required by safety concept |
| Time | hardware timestamps, frame counters and synchronization |
| Safety | watchdog, fault collection, reset partition and safe-state output |
| Security | secure boot, key storage, debug lock and authenticated update |

## 2. Camera topology options

### Native MIPI

```text
Camera module → MIPI CSI-2 → SoC
```

Lowest BOM, but short cable and EMC/package constraints.

### FPD-Link III / GMSL

```text
Camera sensor → serializer → coax/STP
→ deserializer → CSI-2 virtual channels → SoC
```

Preferred for separate forward and DMS camera heads. The SoC sees CSI-2, so the software adapter must isolate the SerDes choice.

### Ethernet camera

Useful for central compute and surround. Requires:

- 100/1000BASE-T1
- PTP/gPTP
- packet-loss handling
- bandwidth and cybersecurity policy

## 3. Radar compatibility

Smart radar object lists over CAN-FD require little AI compute. The key needs are:

- deterministic message cycle
- timestamp/data-age
- ego-motion input
- coordinate transform
- object covariance/quality
- health and blockage state

Dense Ethernet point clouds and radar cubes require:

- 100/1000BASE-T1
- higher DDR bandwidth
- vector/DSP/GPU processing
- synchronized camera-radar timestamps

## 4. Future surround requirements

For 4–8 cameras, evaluate:

- aggregate input pixel rate, not only number of CSI ports
- ISP contexts and supported RAW formats
- concurrent HDR/PWL pipelines
- deserializer virtual channels
- memory bandwidth under neural and video encode load
- hardware dewarp/LDC/scaler
- Ethernet switch and PCIe
- power/thermal throttling behaviour

## 5. Portability traps

- A SoC may have four CSI lanes but only one receiver/context.
- A board may expose only one connector despite the silicon supporting more cameras.
- An ISP may not support the chosen sensor PWL/HDR format without tuning.
- Automotive SerDes drivers may be NDA or tied to one SDK release.
- A high-TOPS accelerator may lack an ISP and require copying frames over PCIe.
- A consumer board may have an NPU but no deterministic camera timestamping.
- Ethernet camera support does not guarantee PTP or safety-qualified networking.

# Software Toolchain, OS and Model Portability

## 1. Portable source of truth

Maintain:

- PyTorch training repository
- ONNX export
- floating-point reference outputs
- INT8 calibration dataset
- per-layer accuracy report
- model-card and dataset version
- target-specific compiled artifacts generated in CI

Do not allow a vendor binary to become the only source of the model.

## 2. Vendor runtime map

| Platform | Runtime/toolchain | Strength | Main risk |
|---|---|---|---|
| TI TDA/AM62A | TIDL, OpenVX, Edge AI SDK | automotive examples, C7x/DSP/ISP integration | operator support and graph partitioning |
| Renesas R-Car | R-Car SDK/RoX, DRP/CNN runtimes | safety and smart-camera ecosystem | proprietary accelerator mapping |
| NXP | eIQ, Neutron NPU, GStreamer | open Linux and ONNX/TFLite flow | lower NPU headroom |
| Ambarella | CVflow SDK | excellent vision efficiency | NDA/closed compiler and smaller community |
| NVIDIA | TensorRT, CUDA, DLA, DriveWorks | broadest model support and profiling | cost/power and different Jetson/DRIVE products |
| Qualcomm | Ride SDK, SNPE/QNN | strong heterogeneous compute | restricted access and stack coupling |
| Horizon | BPU compiler/SDK | production China ecosystem | export/tool access and portability |
| Hailo | Dataflow Compiler, HailoRT | efficient multi-network inference | supported-layer and host-integration constraints |
| Nextchip | APACHE SDK | low-power automotive edge | smaller ecosystem |
| Rockchip | RKNN Toolkit2/RKNNLite | cheap boards and accessible INT8 | conversion quirks and BSP fragmentation |
| Kneron | Kneron PLUS | low-power accessible devices | eTOPS/limited network scale |
| DEEPX | DX SDK | broad framework claims, low power | young compiler ecosystem |

## 3. OS partition strategy

### Entry platform

```text
Linux
+ R5F/RTOS or external watchdog MCU
```

Suitable for DMS and warning ADAS if the safety concept permits.

### Mid automotive platform

```text
Linux/QNX on application cores
+ RTOS/AUTOSAR on safety island
+ shared-memory IPC with E2E protection
```

Preferred for ADVIS Assist/Control.

### High central platform

```text
Safety hypervisor
├── Linux perception
├── QNX/RTOS safety services
├── AUTOSAR vehicle interface
└── diagnostics/OTA partition
```

Use only when mixed-criticality consolidation is justified.

## 4. Model-portability gates

A target compiler must report:

- every unsupported operator
- CPU/GPU fallback
- quantization error by output head
- memory allocation
- peak scratch buffer
- graph partition
- estimated and measured latency
- deterministic behaviour for dynamic shapes

## 5. CI benchmark artifacts

For each SoC commit:

```text
platform/
├── compiler_version.txt
├── model_hashes.json
├── operator_support.csv
├── accuracy_delta.csv
├── latency_power_thermal.json
├── camera_drop_report.csv
└── known_limitations.md
```

## 6. Licensing

Check:

- compiler and runtime redistribution
- per-unit royalty
- model encryption licence
- safety-certified BSP/MCAL cost
- QNX/INTEGRITY/VxWorks licences
- camera ISP tuning ownership
- source-code access
- field-debug entitlement
- SDK maintenance after SOP

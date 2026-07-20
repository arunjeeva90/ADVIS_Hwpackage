# Automotive ADAS SoC Master Reference

The full 60-platform engineering database is maintained in:

- `data/Automotive_SoC_Master.csv`

It contains vendor, product, platform class, AI performance, CPU architecture, camera/ISP capability, vehicle interfaces, safety/qualification status, operating range, best ADVIS use, limitations, access, price status and source.

## Interpretation

- `A1` — automotive smart-camera or edge-sensing compute.
- `A2` — balanced automotive ADAS compute with dual-camera/fusion headroom.
- `A3/A4` — central/domain compute for surround and advanced L2+.
- `B` — emerging accelerator, adaptive-compute or safety-companion path.
- `C` — prototype or non-automotive platform.
- TOPS are not normalized. Precision, sparsity, supported operators, memory traffic and sustained thermal utilization differ.
- “ASIL capable/compliant” must be resolved to the exact orderable part and supplier safety package; it is not a complete ECU certification.

## ADVIS shortlists

### Entry DMS / reduced warning functions

| Candidate | Why it matters | Main gate |
|---|---|---|
| TI AM62A7-Q1 | 2-TOPS automotive MPU with ISP and safety ecosystem | Prove dual-camera limit and operator coverage |
| TI TDA4VEN-Q1 | Newer 4-TOPS smart-camera direction | Board, pricing and software maturity |
| Nextchip APACHE5 | Low-power ASIL-oriented automotive vision processor | 1.6-TOPS headroom and compiler access |
| Hailo-15 automotive | Camera-centric efficient AI path | Exact automotive/safety SKU and vehicle I/O |
| Kneron KL730 | Very-low-power emerging AI/ISP option | Safety evidence and real model performance |

### Integrated Forward Vision + DMS

| Candidate | Why it matters | Main gate |
|---|---|---|
| TI TDA4VL-Q1 | Primary 4-TOPS production cost-down target | Run complete dual-camera workload under heat |
| TI TDA4AL-Q1 | 8-TOPS balanced TI alternative | Complete recurring BOM versus TDA4VL |
| Renesas R-Car V3H | Strong non-TI smart-camera/sensor-fusion candidate | Model-porting effort and toolchain access |
| Renesas R-Car V4M | 17-TOPS future-scalable low-power ADAS SoC | RFQ pricing and evaluation-board access |
| Ambarella CV22FS/CV2FS | Camera-first ISP/CV efficiency and automotive safety | NDA compiler, pricing and support |
| Hailo-8 automotive + host | 26-TOPS low-power accelerator architecture | Host/ISP/safety/PCIe total cost |

### Camera-radar fusion and four-camera growth

| Candidate | Why it matters | Main gate |
|---|---|---|
| TI TDA4VM-Q1 | Current migration/headroom platform | Higher PMIC, memory and thermal cost |
| Renesas R-Car V4M | Good dual-camera-to-surround scalability | Low-volume access and SDK maturity |
| Ambarella CV3-AD | Efficient centralized vision/fusion direction | Closed programme access |
| Horizon Journey 6 entry variants | Broad performance ladder and China production ecosystem | Export, support, tool and safety access |
| Black Sesame A1000 family | Alternative automotive domain-controller path | Global support and transparent specifications |

### Surround and premium L2+

| Candidate | Appropriate use |
|---|---|
| TI TDA4AP/TDA4VH | 4–8 cameras, radar fusion and parking |
| Renesas R-Car V4H | Production multi-sensor ADAS domain control |
| Qualcomm Snapdragon Ride/Flex | High-volume mixed-criticality OEM platform |
| NVIDIA DRIVE Orin/Thor | Premium research and high-performance automated-driving programmes |
| Horizon Journey 5/6 | China-focused 360-degree ADAS and scalable domain compute |
| Mobileye EyeQ6/Ultra | Closed full-stack competitor/partner alternative |

## Prototype-only reference

The master CSV also records RK3588/RK3576, Jetson, Axera, Sophgo, Allwinner, SigmaStar, i.MX 8M Plus, Qualcomm RB5 and Coral. These are useful for model development, cost intelligence or teacher-model research, but they shall not become the ADVIS production baseline without a separate automotive safety, EMC, environmental, cybersecurity and lifecycle programme.

## Practical selection rule

A production shortlist must contain at least:

1. one TI automotive target,
2. one non-TI integrated automotive vision SoC,
3. one host-plus-automotive-accelerator architecture,
4. the existing RK3588 prototype as the low-cost software reference.

All candidates run the same ADVIS camera streams, models, logging, vehicle interfaces and thermal test. Selection is made from measured latency, accuracy, sustained power, complete BOM, safety evidence, supplier support and lifecycle—not from peak TOPS.

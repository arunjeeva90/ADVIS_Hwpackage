# Prototype and Low-Cost Compute Platforms

## Purpose

This file separates **cheap and useful engineering platforms** from production automotive candidates.

## Public and indicative price observations

| Vendor | Product | Item_Type | Region | Observed_or_Indicative_Price | Risk_or_Interpretation | Source |
|---|---|---|---|---|---|---|
| Texas Instruments | TDA4VL-Q1 chip | Automotive SoC | Global | US$84.95 at low quantity; US$68.60 at 250–999 previously observed | Indicative; verify live quote and volume LTSA | https://www.ti.com/product/TDA4VL-Q1/part-details/TDA4VL21HGAALZRQ1 |
| Texas Instruments | SK-TDA4VM / J721EXSKG01EVM | Development starter kit | Global | US$326.81 observed | Non-automotive starter-kit PCB; useful ADVIS migration baseline | https://www.digikey.com/en/products/filter/evaluation-boards/embedded-mcu-dsp-evaluation-boards/786 |
| Texas Instruments | SK-AM62A-LP | Development starter kit | Global | Typically US$249 class when available | Availability has been intermittent; verify stock | https://www.ti.com/tool/SK-AM62A-LP |
| NVIDIA | Jetson Orin Nano Super Developer Kit | Prototype AI SBC | Global | US$249 official launch price | 67-TOPS prototype value; no automotive safety qualification | https://developer.nvidia.com/blog/?p=93942 |
| NVIDIA | Jetson AGX Orin 64GB Developer Kit | Prototype AI system | Global | US$1,999 official | High-end model and multi-camera development; not DRIVE automotive ECU | https://developer.nvidia.com/embedded/faq |
| Vicharak | Axon 8GB/32GB RK3588 | Prototype SBC | India | ₹18,290 observed | Current ADVIS prototype board; 6-TOPS RKNN path | https://www.tradeindia.com/products/single-board-computers-rk3588-9007870.html |
| Vicharak | Axon 16GB/64GB RK3588 | Prototype SBC | India | ₹23,010 observed | Higher-memory prototype; no automotive qualification | https://www.tradeindia.com/products/axon-16gb-lpddr4x-variant-64gb-emmc-variant-motherboard-9007878.html |
| Orange Pi | Orange Pi 5 Plus RK3588 | Prototype SBC | Global | US$120–220 typical by RAM/storage | Price varies widely; verify camera connectors and BSP | https://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-5-plus.html |
| Radxa | ROCK 5B RK3588 | Prototype SBC | Global | US$130–250 typical by RAM | Strong community; no automotive grade | https://radxa.com/products/rock5/5b/ |
| NXP | i.MX 95 EVK | Development board | Global | RFQ / distributor; often >US$1,000 class | Safety-enabled general edge platform, not dedicated ADAS EVM | https://www.nxp.com/products/i.MX95 |
| Renesas | R-Car V3H Starter Kit | Automotive development kit | Global | RFQ / order-now channel | Professional automotive kit; likely high cost | https://www.renesas.com/en/design-resources/boards-kits/y-ask-rcar-v3h |
| Hailo | Hailo-8 M.2 Starter Kit | AI accelerator kit | Global/India | US$180–300 typical | Add 26 TOPS to host; automotive IC option differs from dev module | https://hailo.ai/products/shop/product/hailo-8-starter-kit/ |
| Raspberry Pi | AI HAT+ 13 TOPS (Hailo-8L) | Prototype accelerator | Global | US$70 class | Very cheap DMS/detection experiment; not automotive | https://www.raspberrypi.com/products/ai-hat/ |
| Raspberry Pi | AI HAT+ 26 TOPS (Hailo-8) | Prototype accelerator | Global | US$110 class | Good low-cost multi-model prototype | https://www.raspberrypi.com/products/ai-hat/ |
| Google | Coral USB Accelerator | Prototype accelerator | Global | US$59.99 class | 4 TOPS; constrained TFLite models | https://coral.ai/products/accelerator/ |
| AMD | Kria KV260 Vision AI Starter Kit | FPGA/AI development kit | Global | US$249 class | Good custom video pipeline research; not automotive-qualified board | https://www.amd.com/en/products/system-on-modules/kria/k26/kv260-vision-starter-kit.html |
| Qualcomm | RB5 Robotics Kit | Robotics AI development kit | Global | US$449–500 class | Rich camera/AI prototype; no automotive safety release | https://www.qualcomm.com/developer/hardware/rb5-robotics-kit |
| Kneron | KNEO Pi / KL730 board | Edge AI SBC | Global | Price varies / RFQ | 4 eTOPS class; evaluate real model latency | https://kneo.kneron.com/kneo-pi |
| DEEPX | DX-M1 M.2 module | AI accelerator module | Global | RFQ | 25 TOPS at 1–5 W; automotive grade upon contract/request | https://deepx.ai/products/dx-m1/ |
| Nextchip | APACHE5 EVK/module | Automotive vision development | Korea/global | RFQ | Strong low-cost automotive candidate; request camera kit and compiler | https://www.nextchip.com/en/adas/adas.php?idx=5 |
| Ambarella | CV22FS/CV2FS development platform | Automotive vision development | Global | RFQ / NDA | Professional design-in, not retail | https://www.ambarella.com/products/automotive/ |
| Horizon Robotics | Journey 6 / Matrix reference platform | Automotive domain controller | China/global JV | RFQ | Validate export/tool access and safety evidence | https://www.horizon.auto/en/solutions/horizon-journey/horizon-journey6?tp=1 |
| Black Sesame | A1000 development platform | Automotive domain controller | China | RFQ | Validate global support and tool licensing | https://www.blacksesame.com/en/ |
| Renesas | R-Car V4M/V4H development platform | Automotive ADAS development | Global | RFQ | Strong production path; newer low-volume access limited | https://www.renesas.com/en/about/newsroom/renesas-leads-adas-innovation-power-efficient-4th-generation-r-car-automotive-socs |
| Qualcomm | Snapdragon Ride / Ride Flex platform | Automotive ADAS platform | Global | RFQ / OEM nomination | Not a retail evaluation platform | https://www.qualcomm.com/automotive/solutions/snapdragon-ride |

## Recommended prototype roles

### Existing Vicharak AXON / RK3588

Keep for:

- camera capture and GStreamer
- RKNN conversion and INT8 validation
- DMS and object detector integration
- GUI, logging, diagnostics and web demo
- initial dual-camera scheduling
- low-cost field data collection

Do not use it to claim:

- ISO 26262 readiness
- automotive temperature or EMC
- guaranteed 10–15 year supply
- deterministic safety timing
- production camera/SerDes support

### Jetson Orin Nano/AGX Orin

Use for:

- fast CUDA/TensorRT model benchmarking
- transformer/BEV/occupancy teacher models
- multi-camera algorithm exploration
- profiling before distillation

Do not confuse Jetson with NVIDIA DRIVE. Jetson developer kits are robotics/edge products, while DRIVE is the automotive safety platform.

### Raspberry Pi + Hailo

Use for:

- inexpensive multi-model inference
- DMS classifier and phone/seatbelt detector
- host-plus-accelerator architecture experiments
- compiler compatibility screening

The Raspberry Pi carrier remains non-automotive. Hailo automotive qualification applies only to the exact automotive IC/product and contracted safety package.

### TI starter kits

Use:

- SK-AM62A-LP for 2-TOPS entry workload
- SK-TDA4VM for full ADVIS pipeline and migration
- Jacinto EVMs for production-relevant camera, RTOS and safety work

### Low-cost China boards

Axera, Sophgo, Allwinner and SigmaStar can be useful for cost intelligence. Approve only after:

- full SDK access
- reproducible model compilation
- camera driver source/support
- thermal testing
- lifecycle evidence
- security/update evidence
- supplier identity and export support

## Cheapest meaningful ladder

| Budget level | Platform | What it proves |
|---:|---|---|
| `< US$100` | Coral, Raspberry Pi accelerator, RV1126-class module | Single model or simple DMS/detection |
| `US$100–250` | RK3588 SBC, Hailo module, Kria KV260 | Multiple models and camera pipeline |
| `US$249–500` | Jetson Orin Nano, SK-TDA4VM, RB5 | Serious AI and integration work |
| `US$1,000+` | automotive EVM, AGX Orin, R-Car/NXP kit | production-relevant interfaces or large-model headroom |
| `RFQ/NDA` | Ambarella, Nextchip, Journey, Black Sesame, Ride | true automotive design-in |

## Buying rule

A development board is selected for the question it answers. No single board should be expected to prove model accuracy, production cost, functional safety, camera EMC, vehicle integration and thermal performance at once.

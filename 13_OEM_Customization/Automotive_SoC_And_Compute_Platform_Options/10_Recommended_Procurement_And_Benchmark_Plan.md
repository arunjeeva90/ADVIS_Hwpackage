# Recommended Procurement and Benchmark Plan

## 1. Keep current assets

### Vicharak AXON RK3588

Continue for:

- DMS model and camera development
- dual-pipeline scheduler
- data collection and GUI
- RKNN optimization
- low-cost demo

### TDA4VM/AM68A-class evaluation platform

Use as:

- production-relevant migration target
- camera/SerDes integration baseline
- full dual-camera workload headroom reference
- safety island and vehicle-interface platform

## 2. Immediate benchmark purchases

| Priority | Platform | Purpose |
|---:|---|---|
| 1 | SK-TDA4VM or equivalent TDA4VM SoM | Full ADVIS reference and migration |
| 2 | SK-AM62A-LP | Establish true lower compute boundary |
| 3 | Jetson Orin Nano Super | Fast TensorRT reference and transformer experiments |
| 4 | Hailo-8 M.2 starter kit | Host-plus-accelerator feasibility |
| 5 | Optional second RK3588 board | Dual-camera/field logging redundancy |

## 3. Immediate production RFQs

1. TI: TDA4VL, TDA4VEN and TDA4AL pricing, safety package and module partners.
2. Renesas: R-Car V3H and V4M starter/reference hardware, compiler trial and production price.
3. Ambarella: CV22FS/CV2FS platform for dual-camera ADAS+DMS.
4. Nextchip: APACHE5 and next-generation device, EVK, camera kit and exact ASIL evidence.
5. Hailo: automotive Hailo-8/Hailo-15, host reference and safety package.
6. NXP: i.MX95 automotive plus Hailo/other accelerator architecture.
7. indie: iND881/iND880 for DMS or distributed surround edge nodes.
8. DEEPX: DX-M1 automotive grade, safety roadmap and M.2/IC samples.
9. Horizon and Black Sesame: ASEAN/global support and cost-performance reference.
10. Telechips: Dolphin5 ADAS capability and safety documents.

## 4. Benchmark waves

### Wave A — Software conversion

Run all models through each compiler and reject platforms with:

- major unsupported operators
- large accuracy loss
- hidden CPU fallback
- no profiler
- no deterministic build/version control

### Wave B — Single workload

Measure Forward Vision and DMS separately.

### Wave C — Concurrent ADVIS

Run both with logging, CAN, GNSS/IMU and diagnostics.

### Wave D — Thermal

Soak at elevated ambient and solar-load-equivalent enclosure conditions.

### Wave E — Fusion and expansion

Add smart radar object lists, then two additional cameras.

## 5. Recommended decision points

### ADVIS Assist cost-down

Primary comparison:

- TDA4VL-Q1
- R-Car V3H
- CV22FS/CV2FS
- TDA4VEN-Q1
- APACHE5/next generation

### ADVIS Control/Fusion

Primary comparison:

- TDA4AL/VE/VM
- R-Car V4M
- Ambarella CV3
- NXP i.MX95 + Hailo-8
- A1000/Journey 6 only if regional support is credible

### Surround/L2+ research

- TDA4AP/VH
- R-Car V4H
- DRIVE Orin
- Snapdragon Ride
- Journey 5/6

## 6. Final recommendation

Do not select the final SoC before the same two-camera workload is benchmarked on:

1. the current RK3588 prototype,
2. one TI automotive target,
3. one non-TI integrated automotive SoC,
4. one host-plus-automotive-accelerator path.

This provides a credible cost, performance and lock-in comparison.

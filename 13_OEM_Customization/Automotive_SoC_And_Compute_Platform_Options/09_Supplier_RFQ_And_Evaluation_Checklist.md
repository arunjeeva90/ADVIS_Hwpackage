# Supplier RFQ and Evaluation Checklist

## 1. Commercial identity

- exact orderable part and silicon revision
- automotive/industrial/commercial grade
- sample availability: 2, 5, 10 units
- price at 100, 1k, 10k, 50k and 100k
- MOQ, NRE and annual licence
- production lead time and allocation policy
- PCN/EOL and minimum support period
- India/ASEAN distributor and FAE
- export-control limitations
- module, PMIC and carrier partners

## 2. Compute and memory

- INT8/INT16/FP16 performance and test conditions
- sparsity assumptions
- supported network families
- on-chip SRAM/cache
- LPDDR4/4X/5 width, speed and ECC
- maximum memory size
- sustained performance at 105/125°C junction
- measured power by workload
- thermal throttling modes
- boot time and recovery

## 3. Camera and ISP

- number of physical CSI receivers and aggregate lanes
- virtual channels and simultaneous ISP contexts
- maximum aggregate MPixel/s
- RAW10/12/14/16 and PWL/decompanding
- RCCB/RCCC/RGB-IR/monochrome support
- HDR/LFM and exposure count
- sensor/SerDes reference drivers
- FPD-Link/GMSL partners
- ISP tuning tool and ownership
- hardware LDC/dewarp/scaler
- frame timestamp and trigger synchronization

## 4. AI software

Request a no-cost compiler trial using ADVIS ONNX models.

Require:

- operator list
- quantization formats
- calibration tools
- dynamic shape policy
- CPU/GPU fallback report
- profiler
- multi-network scheduling
- safety/reproducible compiler mode
- Linux/QNX/RTOS support
- Docker/Yocto integration
- OTA and model encryption
- runtime redistribution terms

## 5. Vehicle interfaces

- CAN/CAN-FD controllers
- 100/1000BASE-T1 and TSN
- PCIe
- hardware timestamp/PTP
- SPI/I2C/UART/GPIO/PWM
- GNSS PPS and IMU synchronization
- UDS/DoIP and AUTOSAR support

## 6. Safety and cybersecurity

- ISO 26262 certificate and scope
- safety manual/FMEDA
- ASIL systematic capability
- safety island and lockstep
- ECC/parity/firewalls
- fault injection
- secure boot and debug
- HSM/root of trust
- ISO 21434 evidence
- CVE/security update commitment
- qualified MCAL/RTOS/compiler

## 7. Evaluation acceptance

The supplier platform must run:

1. Forward camera at target HDR mode.
2. DMS camera with NIR timing.
3. Both ADVIS model groups concurrently.
4. CAN-FD and Ethernet traffic.
5. Event logging and OTA partition.
6. 30-minute nominal test and 4-hour thermal soak.
7. Fault injection for camera loss, NPU timeout and DDR error.
8. Accuracy comparison to ONNX reference.
9. Recovery from watchdog reset.
10. Complete power measurement.

## Supplier message

> We are evaluating a compute platform for ADVIS, an integrated Forward Vision + Driver Monitoring smart-camera ECU with future camera-radar fusion and surround expansion. Please provide the exact automotive SoC/SoM, AI performance by precision, sustained thermal performance, camera/ISP capacity, safety manual and ISO 26262 scope, cybersecurity features, Linux/QNX/RTOS/AUTOSAR support, model compiler trial, SerDes camera references, PMIC/memory design, lifecycle and pricing at sample through 100k volumes. The first benchmark will use two concurrent camera pipelines and our ONNX models.

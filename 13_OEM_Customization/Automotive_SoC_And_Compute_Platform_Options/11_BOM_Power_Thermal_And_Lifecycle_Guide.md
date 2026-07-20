# BOM, Power, Thermal and Lifecycle Guide

## 1. Complete compute BOM

The SoC price is only part of the platform:

| Cost area | Typical content |
|---|---|
| Compute | SoC/SoM, safety MCU or island |
| Power | pre-regulator, PMIC, supervisor, watchdog, rails |
| Memory | LPDDR, eMMC, OSPI NOR, EEPROM |
| Camera | serializer/deserializer, PoC, connectors |
| Networking | CAN-FD, Ethernet PHY/switch, PCIe |
| PCB | layer count, HDI/BGA fanout, impedance control |
| Thermal | spreader, TIM, housing, fan if required |
| Software | BSP, compiler, QNX/RTOS, MCAL, model licence |
| Safety/security | documents, HSM provisioning, audits |
| Manufacturing | programming, calibration, traceability, EOL test |

## 2. Architecture cost patterns

### Integrated smart-camera SoC

Lowest recurring BOM and latency, but possible vendor lock-in.

### Host plus accelerator

Can use a cheaper host, but adds:

- accelerator IC/module
- PCIe and power rail
- duplicated memory movement
- safety supervision across devices
- extra compiler/runtime
- larger PCB

### Central compute

Amortizes across many functions, but is inappropriate if ADVIS is only a two-camera ECU.

## 3. Power targets

| Product | Compute-platform power target |
|---|---:|
| DMS/entry warning | 2–4 W |
| Dual-camera ADVIS Assist | 4–8 W |
| ADVIS Control/Fusion | 7–15 W |
| Surround domain | 15–35 W+ |
| Premium central ADAS/AD | 30–100 W+ |

These are platform goals, not guaranteed device specifications.

## 4. Thermal evaluation

Measure:

- junction estimate and board sensors
- enclosure internal ambient
- DDR and PMIC temperature
- sustained FPS under heat
- thermal throttling entry/exit
- recovery without reboot
- solar load and windshield soak
- camera sensor self-heating
- NIR LED contribution
- fan failure if active cooling is used

## 5. Memory sizing

### Prototype

- 4–8 GB LPDDR
- 32–128 GB storage for logs

### Production dual camera

- 2 GB possible only after profiling
- 4 GB preferred for OTA, logging and model headroom
- 16–32 GB eMMC
- separate recovery boot and calibration storage

### Surround

- 8–16 GB+ depending BEV/occupancy and camera buffering

## 6. Lifecycle

Request:

- minimum 10–15 year availability
- PCN notification period
- last-time-buy policy
- mask-revision compatibility
- BSP security support
- compiler/runtime backward compatibility
- PMIC and memory second-source plan
- safety-document update after errata
- regional allocation and LTSA

## 7. Cost-down order

1. Measure and remove unused compute/memory.
2. Select integrated ISP/codec/vehicle interfaces.
3. Reduce external companion ICs.
4. Consolidate camera links.
5. Optimize LPDDR/eMMC population.
6. Simplify PCB only after SI/PI validation.
7. Use passive cooling where measured.
8. Negotiate volume and licences.
9. Avoid a second accelerator unless it lowers total system cost.

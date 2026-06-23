# 01 - Architecture

## Purpose

This folder contains the locked system architecture for the IND-VIAS ECU platform. All architectural decisions documented here are considered **frozen** for the v0.4.4 baseline.

## Sub-folders

| Folder | Contents |
|--------|----------|
| System_Block_Diagrams/ | Top-level block diagrams showing all subsystems and their interconnections |
| Power_Tree/ | Complete power distribution architecture from 12V input to all rails |
| Ground_Domains/ | PGND_IN, BOARD_GND, CHASSIS_GND domain definitions and connection rules |
| Signal_Flow/ | Signal routing between subsystems (CSI-2, FPD-Link, SPI, I2C, UART, CAN) |
| Thermal_Strategy/ | Thermal budget, cooling approach, heat path definitions |
| Mechanical_Envelope/ | Target form factor, enclosure constraints, mounting strategy |
| Modular_Platform_Definition/ | Carrier-to-SoM interface standard, modularity rules |
| SoC_Variants/ | Supported SoC options and their carrier compatibility matrix |

## Architecture Lock Rules

- Changes to documents in this folder require a formal Architecture Change Request (ACR)
- Implementation-closure items (exact part numbers, strap values) are NOT architecture changes
- Architecture changes require full team review and re-baseline

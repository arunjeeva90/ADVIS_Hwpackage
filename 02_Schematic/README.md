# 02 - Schematic

## Purpose

Schematic capture files for the ADVIS ECU. Organized by sheet hierarchy matching the architectural decomposition.

## Sub-folders

| Folder | Contents |
|--------|----------|
| Sheets/ | Individual schematic sheet files (by subsystem) |
| Symbols/ | Custom component symbols and library |
| BOM/ | Bill of Materials (seed, intermediate, production-release) |
| Net_Lists/ | Exported netlists for PCB handoff |
| ERC_Reports/ | Electrical Rules Check reports and waiver logs |
| Review_Checklists/ | Schematic review checklists per subsystem |

## Target Sheet Hierarchy

1. Top / Integration sheet
2. Power input and surge protection
3. Power tree and sequencing
4. SOM interface sheet
5. Camera / deserializer sheet
6. Camera module assumptions / ICD sheet
7. CAN-FD sheet
8. USB / storage / debug sheet
9. GNSS / IMU sheet
10. Watchdog / reset / HMI sheet
11. IR daughterboard sheet
12. Connector / harness summary sheet

## Capture Status

- Phase 1 (can begin now): All sheets EXCEPT SOM physical pin numbers
- Phase 2 (blocked): Final ERC-clean release pending SOM pinout, PoC values, camera ICD

## CAD Tool

EDA tool: [TBD - Altium / OrCAD / KiCad to be determined]

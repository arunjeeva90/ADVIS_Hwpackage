# 03 - PCB Layout

## Purpose

PCB layout files, manufacturing outputs, and design-for-manufacturing documentation.

## Sub-folders

| Folder | Contents |
|--------|----------|
| Stackup/ | Layer stackup definition, impedance targets, material selection |
| Placement/ | Component placement strategy and constraints |
| Routing_Constraints/ | High-speed routing rules (CSI-2, FPD-Link, USB, CAN) |
| Gerbers/ | Manufacturing output files |
| Assembly_Drawings/ | Assembly reference drawings, pick-and-place data |
| DFM_Reports/ | Design-for-Manufacturing analysis reports |

## Layout Priorities

1. Power entry and protection stage — tight loop, low inductance
2. Buck converter loops — minimize hot loop area
3. CSI-2 differential pairs — length-matched, impedance-controlled
4. FPD-Link III input — controlled impedance, PoC isolation
5. Ground domain separation — clear star-point topology
6. SOM connector — high-density routing escape

## Layout Status

**BLOCKED** — Cannot begin PCB layout until ERC-clean schematic is released.

# IND-VIAS ECU v0.4.4 Consolidated Hardware Handoff Document

## 1. Document Status

**Project:** IND-VIAS ADAS + DMS ECU  
**Version:** v0.4.4  
**Status:** A-sample production-intent architecture and schematic capture baseline  
**Architecture:** Locked  
**Schematic skeleton capture:** Can begin immediately  
**ERC-clean schematic / final BOM / PCB layout release:** Blocked until implementation-closure items are completed

This document consolidates the complete current hardware definition into one place: what is being built, the target architecture, the selected major components, the power tree, the interfaces, the default strap states, the connector intent, the net and signal map, and the remaining implementation-closure items that must be finished before final PCB release.

---

## 2. What Is Being Built

The IND-VIAS ECU is a vehicle-mounted ADAS + DMS edge compute unit intended to receive two camera streams, run perception and monitoring workloads on a TDA4VM/AM68A-class SOM, log or observe CAN-FD traffic, receive GNSS and IMU data, and expose engineering/service interfaces such as UART, USB, and removable storage.

### Functional scope

- Forward camera input through FPD-Link III
- Driver Monitoring System (DMS) camera input through FPD-Link III
- Single deserializer hub aggregating both camera channels to CSI-2 into the SOM
- GNSS position/time input
- IMU motion sensing
- CAN-FD monitoring / advisory logging
- Service/debug interfaces: UART, USB device, microSD
- External IR daughterboard support for DMS illumination

### Explicit non-scope / safety boundary

This ECU does NOT provide:

- Brake actuation
- Steering actuation
- Throttle actuation
- Powertrain actuation
- Safety-critical vehicle control outputs

It is an observation / processing / logging ECU, not an actuation ECU.

---

## 3. Architecture Lock Statement

IND-VIAS ECU v0.4.4 is locked as the A-sample production-intent architecture and schematic capture baseline.

Refer to the complete v0.4.4 consolidated handoff document for full technical details including:
- Power tree and sequencing
- Ground domain definitions
- Complete component list with RefDes
- All passive/support component values
- PMOS reverse-polarity topology
- Reset/watchdog topology
- Camera/SerDes subsystem
- CAN-FD subsystem
- GNSS/IMU subsystem
- USB/Storage/Debug interfaces
- IR daughterboard interface
- Complete SOM signal map
- External connector definitions
- Open items blocking PCB release

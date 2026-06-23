# Invention Disclosure: ID-001

## Title
Auto-Adapting Power Sequencing for Multi-SoC Carrier Platform

## Date
June 2026

## Inventors
[To be filled]

## Status
DRAFT - Awaiting prior art search

---

## Problem Statement

Current automotive ECU designs require a complete power tree redesign when the SoC module is changed. Different SoC families have different voltage rail requirements, different power-up sequencing constraints, and different timing budgets. This forces OEMs to redesign the carrier board for each SoC variant, increasing NRE cost and time-to-market.

## Proposed Solution

A carrier board power architecture that:

1. Detects the installed SoM identity at power-on (via ID straps, I2C EEPROM, or resistor coding)
2. Reads the SoM's power profile requirements from an on-board configuration store
3. Adjusts regulator enable sequencing, voltage setpoints (if applicable), and timing delays to match the detected SoM
4. Accomplishes this without firmware intervention (hardware-autonomous configuration)

## Key Novel Elements

- Hardware-level SoM detection that operates before any software runs
- Configurable sequencing logic that adapts enable chain based on module identity
- Single carrier PCB supporting multiple SoC power profiles without hardware modification
- Fail-safe behavior: if SoM identity cannot be read, defaults to most conservative sequencing

## Prior Art Considerations

- Standard power sequencing controllers (TPS65218, etc.) have fixed sequences
- FPGA-based power sequencers exist but add cost/complexity
- No known automotive carrier platform implements SoM-identity-driven adaptive sequencing

## Potential Claims (Draft - For Attorney Review)

1. A method of automatically configuring power sequencing in a modular computing platform...
2. An apparatus comprising a carrier board with identity-detection circuitry...
3. A system for automotive edge computing with interchangeable processing modules...

## Next Steps

- [ ] Complete prior art search
- [ ] Confirm no blocking patents from TI, NXP, Qualcomm
- [ ] Develop detailed block diagram of detection mechanism
- [ ] Estimate implementation complexity
- [ ] Decision: file provisional or continue development in trade secret

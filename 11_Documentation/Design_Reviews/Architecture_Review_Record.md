# ADVIS Architecture Review Record - v0.4.4

## Review Information

| Field | Value |
|-------|-------|
| **Review Type** | Concept Design Review (CDR) / Architecture Lock |
| **Version** | v0.4.4 |
| **Date** | June 2026 |
| **Location** | Engineering Conference Room / Virtual |
| **Duration** | 3 hours |
| **Chair** | Hardware Engineering Manager |

## Attendees

| Name | Role | Organization | Sign-Off |
|------|------|-------------|----------|
| Hardware Lead | Design Owner / Presenter | Hardware Engineering | Approved |
| Senior EE (Peer 1) | Reviewer | Hardware Engineering | Approved |
| Power Electronics Eng | Reviewer | Hardware Engineering | Approved |
| Systems Engineer | Requirements Verification | Systems Engineering | Approved |
| Firmware Lead | SOM Interface Verification | Firmware/BSP | Approved |
| EMC Engineer | EMC Risk Assessment | Compliance | Approved with conditions |
| Mechanical Engineer | Thermal/Mechanical Feasibility | Mechanical Design | Approved |
| Program Manager | Schedule Assessment | Program Office | Acknowledged |

## Architecture Decisions Reviewed

### Decision 1: SoC Platform Selection

| Item | Detail |
|------|--------|
| **Decision** | TDA4VM/AM68A-class SOM (Phytec phyCORE) as baseline compute |
| **Rationale** | Optimal AI performance per watt for dual-camera ADAS+DMS; strong Linux/RTOS ecosystem; Phytec provides production-ready SOM reducing NRE |
| **Alternatives Considered** | Qualcomm SA8295 (over-specified, power), NXP S32V (insufficient AI), Renesas V3H (ecosystem maturity) |
| **Risk** | SOM supply continuity; mitigated by carrier design compatible with multiple SOM vendors |
| **Status** | APPROVED |

### Decision 2: Camera Architecture

| Item | Detail |
|------|--------|
| **Decision** | Single DS90UB954-Q1 dual FPD-Link III deserializer, aggregated to CSI-2 |
| **Rationale** | Minimizes SOM CSI-2 port usage; enables long cable runs (15m); PoC simplifies harness; TI automotive-qualified |
| **Alternatives Considered** | Direct MIPI (cost-down future), GMSL2 (Maxim ecosystem), dual deserializers |
| **Risk** | Single point of failure for both cameras; acceptable for observation-only ECU |
| **Status** | APPROVED (with Track 1 cost-down path noted for direct-MIPI option) |

### Decision 3: Power Tree Topology

| Item | Detail |
|------|--------|
| **Decision** | Discrete cascaded: LM61460 (5V) -> TPS62130A (3.3V) -> TLV75518 (1.8V) |
| **Rationale** | Higher efficiency than integrated PMIC; better thermal distribution; field-proven TI parts; easier second-sourcing |
| **Alternatives Considered** | Integrated PMIC (TPS65941), single-stage multi-output, GaN converters |
| **Risk** | More PCB area than integrated PMIC; acceptable given form factor targets |
| **Status** | APPROVED |

### Decision 4: Input Protection Strategy

| Item | Detail |
|------|--------|
| **Decision** | 80V PMOS reverse-polarity protection + bidirectional TVS + 5A fuse |
| **Rationale** | Low forward voltage drop (~100mV); handles reverse indefinitely; TVS clamps ISO 7637-2 transients |
| **Alternatives Considered** | Ideal diode controller (complex), series Schottky (high drop, thermal), P-FET with controller |
| **Risk** | PMOS SOA during load dump; verified with selected MOSFET characteristics |
| **Status** | APPROVED |

### Decision 5: Safety Boundary

| Item | Detail |
|------|--------|
| **Decision** | ECU is observation/processing/logging ONLY; generates actuation REQUESTS |
| **Rationale** | Avoids ASIL-B+ hardware requirements; reduces certification cost and timeline; OEM retains actuation authority |
| **Alternatives Considered** | ASIL-B rated actuator output stage (significant cost/complexity increase) |
| **Risk** | None - this simplifies the design significantly |
| **Status** | APPROVED |

### Decision 6: Watchdog Strategy

| Item | Detail |
|------|--------|
| **Decision** | TPS3431 external watchdog, disabled during boot, enabled by SOM_BOOT_OK |
| **Rationale** | Prevents reset loops during long Linux boot; independent of SOM internal WDT; provides system-level fault recovery |
| **Alternatives Considered** | SOM internal WDT only (insufficient independence), always-on external WDT (boot loop risk) |
| **Risk** | Window between boot and WDT enable is unmonitored; acceptable as power supervisor covers undervoltage |
| **Status** | APPROVED |

## Architecture Lock Rationale

The v0.4.4 architecture is locked based on the following criteria being met:

1. All major component selections validated against requirements
2. Power budget analysis shows adequate margin (25W budget, ~18W estimated max)
3. Signal integrity feasibility confirmed for CSI-2 at 1.6Gbps/lane
4. Thermal analysis indicates passive cooling feasible for mid-tier operation
5. No critical open issues remain at architecture level
6. Cost estimate within target range for mid-tier BOM

## Open Items from Review

| # | Item | Severity | Owner | Due Date | Status |
|---|------|----------|-------|----------|--------|
| 1 | Complete SI simulation for CSI-2 routing | Major | SI Engineer | Before LDR | Open |
| 2 | Finalize PCB stackup (8 vs 10 layer) | Major | Layout Lead | Before schematic release | Open |
| 3 | EMC pre-scan plan and filter strategy | Major | EMC Engineer | Before LDR | Open |
| 4 | Thermal simulation with enclosure model | Minor | Thermal Lead | Before LDR | Open |
| 5 | Second-source identification for DS90UB954 | Minor | Procurement | Before PPR | Open |
| 6 | GNSS antenna placement optimization | Minor | RF Engineer | Before LDR | Open |

## Conditions of Approval

1. EMC Engineer: Approval conditional on EMC pre-compliance plan being completed before Layout Design Review
2. All Critical/Major open items must be resolved before schematic review (SDR) gate

## Review Outcome

**Result:** ARCHITECTURE APPROVED AND LOCKED

The v0.4.4 architecture is approved for schematic capture. Changes to locked items require formal ECO with multi-stakeholder review.

---

*Review Record Version: 1.0 | ADVIS Hardware Platform*

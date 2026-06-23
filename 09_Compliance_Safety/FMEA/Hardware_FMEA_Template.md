# ADVIS Hardware FMEA (Failure Mode and Effects Analysis)

| Field | Value |
|-------|-------|
| Document ID | ADVIS-CS-FMEA-001 |
| Version | 0.1 |
| Status | Draft |
| Author | Quality & Reliability Team |
| Date | 2024-01-15 |
| Classification | CONFIDENTIAL |
| FMEA Type | Design FMEA (DFMEA) |
| Scope | ADVIS ECU Hardware |

---

## 1. Purpose

This Hardware FMEA identifies potential failure modes of the ADVIS ECU hardware, evaluates their effects and causes, and defines detection and prevention controls. The FMEA supports the QM (Quality Management) classification under ISO 26262 by demonstrating systematic analysis of hardware reliability risks.

## 2. FMEA Rating Scales

### 2.1 Severity (S)

| Rating | Effect | Description |
|--------|--------|-------------|
| 1 | None | No discernible effect |
| 2-3 | Minor | Slight degradation, user may not notice |
| 4-5 | Moderate | Noticeable performance reduction, user aware |
| 6-7 | High | Significant function loss, user dissatisfied |
| 8 | Very High | System inoperable, no safety impact |
| 9 | Hazardous with warning | Potential safety issue with prior warning |
| 10 | Hazardous without warning | Potential safety issue without warning |

*Note: For ADVIS (non-actuation ECU), maximum severity is typically 8 (system inoperable). Safety-related ratings (9-10) only apply if failure could cause distraction or incorrect information to driver.*

### 2.2 Occurrence (O)

| Rating | Probability | Failure Rate |
|--------|-------------|-------------|
| 1 | Remote | < 1 in 1,500,000 |
| 2 | Very Low | 1 in 150,000 |
| 3 | Low | 1 in 15,000 |
| 4 | Moderately Low | 1 in 2,000 |
| 5 | Moderate | 1 in 400 |
| 6 | Moderately High | 1 in 80 |
| 7 | High | 1 in 20 |
| 8 | Very High | 1 in 8 |
| 9 | Extremely High | 1 in 3 |
| 10 | Almost Certain | >= 1 in 2 |

### 2.3 Detection (D)

| Rating | Likelihood of Detection | Method |
|--------|------------------------|--------|
| 1 | Almost Certain | Proven design verification |
| 2 | Very High | Design review + simulation |
| 3 | High | Bench testing at component level |
| 4 | Moderately High | DVT testing |
| 5 | Moderate | System-level functional test |
| 6 | Low | Production screening (HASS) |
| 7 | Very Low | Inspection/audit |
| 8 | Remote | Random quality sampling |
| 9 | Very Remote | Not specifically tested |
| 10 | Impossible | No detection method exists |

### 2.4 RPN Calculation

**RPN = Severity x Occurrence x Detection**

| RPN Range | Priority | Action |
|-----------|----------|--------|
| 1 - 50 | Low | Monitor, no immediate action |
| 51 - 100 | Medium | Improvement recommended |
| 101 - 200 | High | Corrective action required |
| > 200 | Critical | Immediate corrective action |

## 3. FMEA Worksheet

### Power Supply Subsystem

| # | Item / Function | Potential Failure Mode | Potential Effect(s) | S | Potential Cause(s) | O | Current Design Controls | D | RPN | Recommended Action |
|---|----------------|----------------------|--------------------|----|-------------------|---|------------------------|---|-----|-------------------|
| 1 | LM61460-Q1 (5V buck) | Output overvoltage (> 5.5V) | Damage to downstream 3.3V/1.8V regulators and SoM; total system failure | 8 | Internal FET short, feedback resistor open | 2 | OVP circuit on LM61460; TPS3808 supervisor monitors 3V3; SoM has internal protection | 3 | 48 | Add external OVP (crowbar or clamp) on 5V rail for defense-in-depth |
| 2 | LM61460-Q1 (5V buck) | Output undervoltage (< 4.5V) | 3.3V and 1.8V rails droop; system brownout reset; loss of all functions | 7 | Overload, inductor saturation at high temp, input voltage below minimum (< 6V) | 3 | UVLO on LM61460; TPS3808 monitors 3V3; watchdog resets SoM on hang | 3 | 63 | Add power-good monitoring on 5V rail reported via CAN diagnostic message |
| 3 | LM61460-Q1 (5V buck) | Excessive output ripple (> 50mV) | Camera image noise, CAN bit errors, GNSS sensitivity degradation | 5 | Output capacitor degradation (MLCC aging), increased ESR at low temperature | 4 | DVT ripple measurement; margin in capacitor selection (derated) | 4 | 80 | Specify X5R or X7R MLCC with < 20% capacitance loss at rated voltage; add ripple budget allocation |
| 4 | TPS62130A-Q1 (3.3V buck) | Open circuit (no output) | Loss of 3.3V rail; supervisor resets system; 1.8V LDO has no input; total loss of digital functions | 8 | Solder joint failure (thermal cycling), component defect | 2 | TPS3808G33 monitors 3V3; system detects loss via watchdog timeout | 2 | 32 | AEC-Q100 Grade 1 component; solder joint reliability per IPC-9701 |
| 5 | TLV75518-Q1 (1.8V LDO) | Thermal shutdown | Loss of 1.8V core rail; SoM processor halts; system non-functional | 7 | Excessive SoM core current at high ambient temperature | 3 | Thermal design with adequate copper pour; LDO thermal pad soldered; airflow path in enclosure | 4 | 84 | Verify thermal margin at 85C ambient with maximum SoM load; consider alternative LDO with lower dropout |
| 6 | Input PMOS (reverse protection) | Short circuit (drain-source) | Reverse polarity protection defeated; -16V reaches downstream regulators; catastrophic damage | 8 | Gate oxide failure, ESD event | 1 | AEC-Q100 qualified MOSFET; ESD protection on gate; input TVS clamps transients | 3 | 24 | Verify PMOS gate oxide rating > 20V; add series gate resistor for ESD |
| 7 | Input TVS diode | Open circuit failure | Loss of transient protection; subsequent load dump (40V) damages downstream components | 8 | Surge event exceeds TVS energy rating; TVS degrades open | 2 | TVS energy rating selected > 2x worst-case automotive transient; AEC-Q101 qualified | 5 | 80 | Verify TVS energy rating per ISO 7637-2 pulse 5b; consider redundant TVS for critical protection |

### Camera Subsystem

| # | Item / Function | Potential Failure Mode | Potential Effect(s) | S | Potential Cause(s) | O | Current Design Controls | D | RPN | Recommended Action |
|---|----------------|----------------------|--------------------|----|-------------------|---|------------------------|---|-----|-------------------|
| 8 | DS90UB954-Q1 (deserializer) | Loss of FPD-Link lock (VC0 forward camera) | No forward camera image; ADAS perception unavailable; system reports fault via CAN | 7 | Cable damage, connector contact degradation, EMI interference on cable | 4 | Lock status register polled by SoM; fault reported on CAN; automatic re-lock attempt | 3 | 84 | Implement link health monitoring with predictive warning (error count trending); define cable strain relief |
| 9 | DS90UB954-Q1 (deserializer) | Loss of FPD-Link lock (VC1 DMS camera) | No DMS image; driver monitoring unavailable; DMS fault reported via CAN | 6 | Cable damage, connector oxidation, thermal expansion mismatch at connector | 4 | Lock status monitored; fault reported on CAN; IR LEDs disabled if no DMS | 3 | 72 | Same as #8; add connector specification with gold-plated contacts for reliability |
| 10 | DS90UB954-Q1 (deserializer) | I2C configuration failure | Deserializer not configured; no camera output; system fails to initialize | 7 | SDA/SCL line stuck (solder bridge, pull-up failure), address conflict | 2 | I2C bus scan during boot; timeout detection; retry mechanism in firmware | 3 | 42 | Add I2C bus isolator; implement fallback configuration via GPIO strapping |
| 11 | CSI-2 interface (SoM side) | Data corruption (CRC errors) | Corrupted camera frames; image artifacts; potential false ADAS detections if not caught | 7 | SI degradation (impedance mismatch), crosstalk, connector mismating | 3 | CSI-2 protocol CRC per frame; frames with CRC error discarded by ISP; error counter monitored | 2 | 42 | Specify connector insertion force and mating cycle count; SI validation in DVT at temperature extremes |

### CAN Communication Subsystem

| # | Item / Function | Potential Failure Mode | Potential Effect(s) | S | Potential Cause(s) | O | Current Design Controls | D | RPN | Recommended Action |
|---|----------------|----------------------|--------------------|----|-------------------|---|------------------------|---|-----|-------------------|
| 12 | TCAN1044AV-Q1 (CAN-FD transceiver) | Bus-off state | CAN communication lost; ADVIS requests not received by OEM ECU; vehicle loses ADVIS advisory function | 7 | Excessive bus errors from EMI, ground offset between ADVIS and vehicle CAN, faulty bus termination | 3 | Auto bus-off recovery enabled (ISO 11898-1 recovery sequence); error counters monitored by SoM; fault logged | 3 | 63 | Implement fast bus-off recovery (< 2s); log bus error statistics for field analysis; verify ground offset immunity |
| 13 | TCAN1044AV-Q1 (CAN-FD transceiver) | Permanent short (CAN_H to CAN_L) | Entire CAN bus disrupted (affects other vehicle ECUs); ADVIS output silenced | 8 | Internal transceiver failure, ESD damage to CAN pins | 1 | AEC-Q100 qualified; ESD protection per ISO 10605; split termination for CM filtering | 4 | 32 | Verify ESD protection exceeds ISO 10605 requirements; consider CAN bus guardian (if required by OEM) |
| 14 | TCAN1044AV-Q1 (CAN-FD transceiver) | Stuck dominant (TXD low) | Bus held dominant; all other ECUs unable to transmit; potential vehicle system disruption | 8 | TXD path shorted to GND, transceiver internal fault, SoM GPIO stuck | 2 | TXD dominant timeout (TXD recessive pull-up resistor); transceiver has internal dominant timeout | 3 | 48 | Verify TXD recessive pull-up value per TCAN1044AV-Q1 recommendation; add external watchdog on TXD activity |

### Watchdog/Supervisor Subsystem

| # | Item / Function | Potential Failure Mode | Potential Effect(s) | S | Potential Cause(s) | O | Current Design Controls | D | RPN | Recommended Action |
|---|----------------|----------------------|--------------------|----|-------------------|---|------------------------|---|-----|-------------------|
| 15 | TPS3431-Q1 (watchdog) | Watchdog fails to reset (stuck inactive) | SoM firmware hang goes undetected; system outputs stale data; stale CAN messages could mislead OEM ECU | 7 | Internal WD IC failure, WDI line stuck toggling (oscillation from noise) | 2 | TPS3431 is AEC-Q100 qualified; message alive counter in CAN frame (detected by receiver); SoM internal WDT as backup | 4 | 56 | Add periodic self-test of watchdog path (force single missed toggle, verify reset); implement diversity (external WD + SoM internal WDT) |
| 16 | TPS3431-Q1 (watchdog) | False reset (spurious trigger) | Unexpected system reboot; temporary loss of ADVIS function (30s boot time); driver warning gap | 6 | Noise on WDI line, power supply glitch during normal operation, incorrect timeout configuration | 3 | RC filtering on WDI signal; clean power to watchdog IC; timeout configured with margin | 4 | 72 | Verify WDI signal integrity at temperature extremes; add hysteresis/filtering on WDI; log all reset events with cause |
| 17 | TPS3808G33-Q1 (supervisor) | Fails to assert RESET during brownout | SoM operates with marginal voltage; unpredictable behavior; possible data corruption | 7 | Supervisor threshold drift over temperature; supply voltage just at boundary | 2 | Supervisor threshold set 5% below nominal (3.135V typ); SoM has internal POR; DVT validates trip point | 3 | 42 | Measure supervisor threshold at -40C and +85C; verify hysteresis prevents chatter; add second voltage monitor if margin insufficient |

### GNSS Subsystem

| # | Item / Function | Potential Failure Mode | Potential Effect(s) | S | Potential Cause(s) | O | Current Design Controls | D | RPN | Recommended Action |
|---|----------------|----------------------|--------------------|----|-------------------|---|------------------------|---|-----|-------------------|
| 18 | NEO-M9N-00B (GNSS) | Loss of satellite fix | No position/velocity data; reduced ADAS context (no speed, no location); system operates in degraded mode | 4 | Antenna obstruction (windshield metallization), RF interference from ECU self-emission, antenna cable fault | 4 | Fix status reported in NMEA data; SoM uses IMU dead-reckoning as backup; CAN speed as secondary input | 3 | 48 | Perform self-interference test (GNSS sensitivity vs. system operating mode); specify antenna placement requirements in ICD |
| 19 | NEO-M9N-00B (GNSS) | Position output error (> 10m) | Incorrect location context; potential misjudgment of road type; degraded risk assessment | 4 | Multipath in urban canyons, poor GDOP, ionospheric error | 5 | Receiver reports accuracy estimate (HDOP, EPE); SoM fuses with IMU and CAN data; plausibility check | 3 | 60 | Implement GNSS + IMU tight coupling for improved urban accuracy; define position quality threshold for feature activation |

### IR Illumination Subsystem

| # | Item / Function | Potential Failure Mode | Potential Effect(s) | S | Potential Cause(s) | O | Current Design Controls | D | RPN | Recommended Action |
|---|----------------|----------------------|--------------------|----|-------------------|---|------------------------|---|-----|-------------------|
| 20 | IR LED array (daughterboard) | LED open circuit (single LED fails) | Uneven illumination on driver face; DMS image quality degraded; potential facial recognition accuracy loss | 5 | Bond wire failure, thermal overstress, EOS (electrical overstress) | 3 | Series/parallel LED topology limits single-LED-failure impact; DMS algorithm tolerant of non-uniform illumination | 5 | 75 | Implement LED current monitoring for each string; define minimum illumination threshold for DMS function |
| 21 | IR LED driver | Stuck ON (IR_LED_EN failure, always high) | IR LEDs continuously illuminated; exceeds eye safety thermal budget; potential IEC 62471 exceedance over long exposure | 6 | GPIO driver failure (stuck high), solder bridge on enable trace | 2 | Watchdog timeout disables IR if no SoM heartbeat; thermal protection reduces current at high temperature; hardware timeout circuit | 4 | 48 | Add independent hardware timer that disables IR after maximum continuous-on period (e.g., 60s without software refresh) |

## 4. RPN Summary and Priority

| Priority | RPN Range | Count | Items |
|----------|-----------|-------|-------|
| Critical (> 200) | - | 0 | None |
| High (101-200) | - | 0 | None |
| Medium (51-100) | 51-100 | 9 | #2, #3, #5, #7, #8, #9, #12, #15, #16, #19, #20 |
| Low (1-50) | 1-50 | 12 | #1, #4, #6, #10, #11, #13, #14, #17, #18, #21 |

### Top 5 RPNs (Prioritized for Action)

| Rank | # | Item | RPN | Key Action |
|------|---|------|-----|------------|
| 1 | #5 | TLV75518 thermal shutdown | 84 | Verify thermal margin at 85C |
| 2 | #8 | DS90UB954 forward camera lock loss | 84 | Link health monitoring |
| 3 | #3 | LM61460 excessive ripple | 80 | Capacitor aging specification |
| 4 | #7 | TVS open circuit | 80 | Energy rating verification |
| 5 | #20 | IR LED open circuit | 75 | Current monitoring per string |

## 5. Action Tracking

| Item # | Recommended Action | Owner | Target Date | Status | New RPN |
|--------|-------------------|-------|-------------|--------|---------|
| 5 | Thermal simulation at 85C max load | Thermal Engineer | [TBD] | Open | - |
| 8 | Implement link error trending | Firmware Team | [TBD] | Open | - |
| 3 | Specify X7R capacitors, document aging | Component Engineer | [TBD] | Open | - |
| 7 | Verify TVS per ISO 7637-2 pulse 5b | EMC Engineer | [TBD] | Open | - |
| 20 | LED string current monitoring design | Hardware Designer | [TBD] | Open | - |

## 6. FMEA Review and Maintenance

| Activity | Frequency | Responsible |
|----------|-----------|-------------|
| Initial FMEA creation | Design phase | Hardware Lead |
| FMEA review (design changes) | Each ECO | Cross-functional team |
| FMEA update (DVT findings) | Post-DVT | Quality Engineer |
| FMEA update (field returns) | Quarterly (post-SOP) | Reliability Engineer |
| Annual FMEA review | Yearly | Cross-functional team |

## 7. Assumptions and Limitations

1. This FMEA covers hardware failure modes only. Software/firmware FMEA is a separate document.
2. Severity ratings assume ADVIS is non-actuation (QM). If OEM integration changes safety boundary, ratings must be reassessed.
3. Occurrence ratings are estimates based on component reliability data and automotive field experience. They will be refined with field data.
4. Single-fault analysis. Common-cause failures (e.g., power supply failure affecting multiple subsystems) are addressed in the safety concept, not individual FMEA lines.

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | 2024-01-15 | Quality & Reliability Team | Initial draft - 21 failure modes |

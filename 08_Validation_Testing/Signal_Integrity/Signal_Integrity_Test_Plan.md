# ADVIS Signal Integrity Test Plan

| Field | Value |
|-------|-------|
| Document ID | ADVIS-VT-SI-001 |
| Version | 0.1 |
| Status | Draft |
| Author | Hardware Validation Team |
| Date | 2024-01-15 |
| Classification | CONFIDENTIAL |

---

## 1. Scope

This document defines the signal integrity test plan for all high-speed interfaces on the ADVIS ECU. Measurements validate compliance with interface specifications and confirm adequate signal margin across the operating temperature range (-40C to +85C).

## 2. Interfaces Under Test

| Interface | Standard | Data Rate | Lanes/Lines | Connected Device |
|-----------|----------|-----------|-------------|-----------------|
| CSI-2 (MIPI) | MIPI D-PHY v1.2 | 1.5 Gbps/lane | 4 data + 1 clock | TDA4VM SoM |
| FPD-Link III | TI DS90UB954-Q1 | 4.16 Gbps (aggregate) | 2 differential pairs (VC0+VC1) | Camera modules |
| CAN-FD | ISO 11898-2 | 5 Mbps (data phase) | 1 differential pair | Vehicle bus |
| USB 2.0 | USB 2.0 HS | 480 Mbps | 1 differential pair | Host/device |
| SPI (IMU) | SPI Mode 0/3 | 10 MHz | 4 signals (SCLK, MOSI, MISO, CS) | BMI088 |

## 3. Equipment Required

| Equipment | Specification | Purpose |
|-----------|---------------|---------|
| Real-Time Oscilloscope | >= 6 GHz BW, >= 25 GSa/s | Eye diagram, jitter |
| Differential Probes | >= 6 GHz, < 0.5 pF loading | High-speed signal probing |
| BERT / Pattern Generator | Up to 6 Gbps | CSI-2 / FPD-Link stress |
| Vector Network Analyzer | 10 MHz - 8 GHz, 4-port | S-parameter measurement |
| TDR Module | < 30 ps rise time | Impedance profiling |
| CAN Bus Analyzer | ISO 11898-2 compliant | CAN physical layer analysis |
| USB Protocol Analyzer | USB 2.0 HS capable | USB compliance |
| SPI Logic Analyzer | >= 100 MHz sample rate | SPI timing |
| Thermal Chamber | -40C to +125C | Temperature sweep |

## 4. Test Procedures

### 4.1 CSI-2 MIPI D-PHY Eye Diagram

**Objective:** Verify CSI-2 data lanes meet MIPI D-PHY eye diagram mask at 1.5 Gbps/lane.

**Test Setup:**
```
  Camera Module --> FPD-Link III --> DS90UB954 --> CSI-2 4-lane --> TDA4VM SoM
                                                       |
                                                  [Probe Point]
                                                  (SoM connector)
```

**Measurement Points:**
- Probe at SoM connector pads (receiver end)
- Use differential probe with < 0.5 pF capacitive loading
- Measure all 4 data lanes individually

**Procedure:**
1. Configure camera to output maximum resolution/frame rate (continuous streaming)
2. Set oscilloscope to eye diagram mode with MIPI D-PHY mask
3. Accumulate minimum 10,000 unit intervals per lane
4. Record eye height, eye width, jitter (Tj, Rj, Dj)
5. Verify compliance at 25C, then repeat at -40C and +85C

**Pass/Fail Criteria:**

| Parameter | Specification | Limit |
|-----------|---------------|-------|
| Eye height (differential) | MIPI D-PHY HS | >= 140 mV |
| Eye width | MIPI D-PHY HS | >= 0.35 UI |
| Total jitter (Tj) | At BER 10^-12 | <= 0.30 UI |
| Random jitter (Rj, rms) | Per lane | <= 15 ps rms |
| Rise/Fall time (20%-80%) | HS mode | 150 ps - 400 ps |
| Common mode voltage | HS mode | 150 mV - 250 mV |
| Differential voltage (Vod) | HS mode | 140 mV - 270 mV |

### 4.2 FPD-Link III Signal Quality

**Objective:** Verify FPD-Link III link quality for both camera channels (VC0: Forward, VC1: DMS).

**Test Setup:**
```
  Imager -----[Serializer]----(Coax/STP)----[DS90UB954-Q1]---- CSI-2 out
                                                  |
                                             [Probe Point]
                                          (deser input pins)
```

**Procedure:**
1. Connect reference camera modules with known-good cables
2. Enable built-in link diagnostics on DS90UB954-Q1
3. Read link status registers: lock indicator, bit error count
4. Measure input signal at deserializer pins:
   - Differential amplitude
   - Jitter (using oscilloscope CDR and eye diagram)
   - Cable loss compensation (adaptive equalizer setting)
5. Run BER test for minimum 10 minutes per channel

**Pass/Fail Criteria:**

| Parameter | Specification | Limit |
|-----------|---------------|-------|
| Link lock time | From power-up | < 500 ms |
| BER (bit error rate) | Sustained operation | < 10^-12 |
| Differential amplitude (at deser) | After cable loss | >= 100 mV differential |
| Jitter (Tj at deser input) | Per TI spec | <= 0.3 UI |
| Cable length margin | With reference cable | >= 5 m (shielded STP) |
| Link recovery | After cable disconnect/reconnect | < 1 s |

### 4.3 CAN-FD Physical Layer

**Objective:** Verify CAN-FD physical layer compliance per ISO 11898-2.

**Test Setup:**
```
  TDA4VM (MCAN) --> TCAN1044AV-Q1 --> CAN_H/CAN_L --> [120-ohm term] --> Bus
                                            |
                                       [Probe Point]
                                    (connector pins)
```

**Procedure:**
1. Configure CAN-FD at 500 kbps arbitration / 5 Mbps data phase
2. Transmit continuous frames (standard and extended ID)
3. Measure at connector pins using differential probe:
   - V_CANH_dominant, V_CANL_dominant
   - V_CANH_recessive, V_CANL_recessive
   - V_diff_dominant, V_diff_recessive
   - Rise/fall time (dominant-to-recessive, recessive-to-dominant)
   - Bit timing (sample point position)
   - Symmetry (t_rec_dom vs t_dom_rec)
4. Verify with external CAN analyzer (frame decode, error frames)

**Pass/Fail Criteria (per ISO 11898-2):**

| Parameter | Min | Typ | Max | Unit |
|-----------|-----|-----|-----|------|
| V_CANH (dominant) | 2.75 | 3.5 | 4.5 | V |
| V_CANL (dominant) | 0.5 | 1.5 | 2.25 | V |
| V_diff (dominant) | 1.5 | 2.0 | 3.0 | V |
| V_diff (recessive) | -0.5 | 0 | 0.05 | V |
| Rise time (CAN-FD, 5Mbps) | - | - | 40 | ns |
| Fall time (CAN-FD, 5Mbps) | - | - | 40 | ns |
| Symmetry (delta t) | - | - | 10 | ns |
| Bus load (maximum) | - | - | 70 | % |
| TXD recessive pull-up | Applied | - | - | - |

### 4.4 USB 2.0 High-Speed Signal Quality

**Objective:** Verify USB 2.0 HS signal quality at the USB-C connector.

**Test Setup:**
```
  TDA4VM (USB) --> ESD Protection --> USB-C Connector (Device mode)
                                           |
                                      [Probe Point]
                                    (connector pads)
```

**Procedure:**
1. Enumerate USB device at High-Speed (480 Mbps)
2. Send continuous test packet (Test_Packet, USB 2.0 compliance mode)
3. Measure eye diagram at connector using differential probe
4. Verify signal levels, timing, and impedance

**Pass/Fail Criteria (per USB 2.0 HS Electrical Spec):**

| Parameter | Specification | Limit |
|-----------|---------------|-------|
| Differential amplitude | HS signaling | 360 mV - 440 mV (into 45-ohm) |
| Eye height | USB 2.0 mask | >= 250 mV |
| Eye width | USB 2.0 mask | >= 0.75 UI |
| Rise/fall time (20%-80%) | HS | 500 ps +/- 250 ps |
| Total jitter | At receiver | <= 0.35 UI |
| D+/D- crossover voltage | During transition | 250 mV - 450 mV |
| CC pull-down resistance | Device mode (5.1k) | 4.59 kohm - 5.61 kohm |

### 4.5 SPI (BMI088 IMU Interface)

**Objective:** Verify SPI interface timing at maximum clock rate to BMI088 IMU.

**Test Setup:**
```
  TDA4VM (SPI) --> Level Shifter (if any) --> BMI088 (dual-die, dual CS)
                                                   |
                                              [Probe Point]
                                           (IMU IC pins)
```

**Procedure:**
1. Configure SPI clock at maximum rate (10 MHz)
2. Perform continuous read of accelerometer and gyroscope registers
3. Capture SCLK, MOSI, MISO, CS_ACC, CS_GYRO with logic analyzer
4. Measure setup time, hold time, propagation delay
5. Verify data integrity (compare read values to expected register contents)

**Pass/Fail Criteria (per BMI088 SPI Timing):**

| Parameter | Min | Max | Unit |
|-----------|-----|-----|------|
| SCLK frequency | - | 10 | MHz |
| CS setup time (before SCLK) | 10 | - | ns |
| CS hold time (after SCLK) | 10 | - | ns |
| MOSI setup (before SCLK rising) | 5 | - | ns |
| MOSI hold (after SCLK rising) | 5 | - | ns |
| MISO valid (after SCLK falling) | - | 25 | ns |
| SCLK high time | 40 | - | ns |
| SCLK low time | 40 | - | ns |
| Data read error rate | - | 0 | errors/10^6 reads |

## 5. Impedance Verification (TDR)

**Objective:** Verify controlled-impedance traces meet design targets.

| Trace Type | Target | Tolerance | Measurement Method |
|------------|--------|-----------|-------------------|
| Single-ended (general) | 50 ohm | +/- 10% | TDR at via-less test coupon |
| Differential (CSI-2) | 100 ohm | +/- 10% | TDR differential mode |
| Differential (USB) | 90 ohm | +/- 10% | TDR differential mode |
| Differential (CAN) | 120 ohm (bus) | +/- 5% | Network analyzer |
| Differential (FPD-Link) | 100 ohm | +/- 10% | TDR differential mode |

## 6. S-Parameter Measurement (Critical Channels)

**Objective:** Characterize insertion loss and return loss of high-speed channels.

| Channel | Frequency Range | Insertion Loss Limit | Return Loss Limit |
|---------|-----------------|---------------------|-------------------|
| CSI-2 (lane, connector to SoM) | DC - 1.5 GHz | < 3 dB at Nyquist | > 10 dB |
| FPD-Link III (connector to deser) | DC - 2.5 GHz | < 5 dB at Nyquist | > 8 dB |
| USB 2.0 (connector to SoC) | DC - 480 MHz | < 3 dB at Nyquist | > 10 dB |

## 7. Temperature and Voltage Sensitivity Matrix

All signal integrity measurements shall be repeated at corner conditions:

| Condition | VIN | Temperature | Note |
|-----------|-----|-------------|------|
| Nominal | 13.5V | 25C | Baseline |
| Cold | 6V | -40C | Worst-case low |
| Hot | 16V | +85C | Worst-case high |
| Load dump | 36V | 25C | Transient survival only |

## 8. Reporting

For each interface, the SI test report shall include:
- Eye diagram screenshots (with mask overlay)
- Jitter decomposition (Rj, Dj, Tj)
- Statistical measurements (minimum eye opening over N acquisitions)
- Temperature trend plots
- S-parameter plots (if applicable)
- Pass/Fail summary

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | 2024-01-15 | Hardware Validation Team | Initial draft |

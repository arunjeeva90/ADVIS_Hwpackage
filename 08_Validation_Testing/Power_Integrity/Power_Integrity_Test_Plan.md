# ADVIS Power Integrity Test Plan

| Field | Value |
|-------|-------|
| Document ID | ADVIS-VT-PI-001 |
| Version | 0.1 |
| Status | Draft |
| Author | Hardware Validation Team |
| Date | 2024-01-15 |
| Classification | CONFIDENTIAL |

---

## 1. Scope

This document defines the power integrity test plan for the ADVIS ECU. All on-board power rails are characterized for static accuracy, dynamic performance, noise, and protection features. Testing covers the full operating temperature range (-40C to +85C) per AEC-Q100 Grade 2 requirements.

## 2. References

| Standard / Document | Relevance |
|---------------------|-----------|
| ISO 16750-2 | Supply voltage requirements |
| ISO 7637-2 | Electrical transient immunity |
| AEC-Q100 Grade 2 | IC qualification temperature range |
| ADVIS Power Tree Architecture | System power rail definitions |
| LM61460-Q1 datasheet | 5V buck converter specifications |
| TPS62130A-Q1 datasheet | 3.3V buck converter specifications |
| TLV75518-Q1 datasheet | 1.8V LDO specifications |

## 3. Equipment Required

| Equipment | Specification | Purpose |
|-----------|---------------|---------|
| DC Power Supply | 0-60V, 10A programmable | Input supply simulation |
| Digital Oscilloscope | >= 1 GHz BW, >= 5 GSa/s | Ripple/noise measurement |
| Digital Multimeter | 6.5-digit | Static voltage accuracy |
| Electronic Load | 0-20A, dynamic mode (1 us slew) | Load regulation / transient |
| Thermal Chamber | -40C to +125C | Temperature characterization |
| Current Probe | DC-100 MHz, 30A | Current measurement |
| Spectrum Analyzer | 9 kHz - 3 GHz | Noise spectral analysis |
| Data Logger | 16+ channels, 1 ms sampling | Long-term stability |

## 4. Test Points

```
                        TP1          TP2          TP3           TP4
  VIN_BATT ---[FUSE]---+---[PMOS]---+---[BUCK1]--+---[BUCK2]---+---[LDO]--- TP5
              (5A)      |            |   LM61460  |  TPS62130A  |  TLV75518
                        |            |            |             |
                     V_IN_RAW    V_PROT        5V_SYS       3V3_IO      1V8_CORE
                     (6-40V)     (post-RP)     (5.0V)       (3.3V)      (1.8V)

  TP_GND: Board ground reference (star ground point near SoM connector)
```

| Test Point | Net Name | Location | Probe Type |
|------------|----------|----------|------------|
| TP1 | VIN_RAW | Post-fuse, pre-PMOS | Kelvin sense |
| TP2 | VIN_PROT | Post-PMOS reverse protection | Kelvin sense |
| TP3 | 5V_SYS | LM61460-Q1 output capacitor | 50-ohm tip, ground spring |
| TP4 | 3V3_IO | TPS62130A-Q1 output capacitor | 50-ohm tip, ground spring |
| TP5 | 1V8_CORE | TLV75518-Q1 output capacitor | 50-ohm tip, ground spring |
| TP_GND | BOARD_GND | Star ground reference | Ground spring |

## 5. Test Procedures

### 5.1 Static Voltage Accuracy

**Objective:** Verify each rail meets accuracy specification at nominal input and full load.

**Setup:**
- Input voltage: 13.5V (nominal automotive battery)
- Temperature: 25C (room), then sweep -40C to +85C
- Load: Full rated current per rail

**Procedure:**
1. Set input supply to 13.5V
2. Apply rated load to each rail:
   - 5V_SYS: 6.0A (LM61460 rated)
   - 3V3_IO: 3.0A (TPS62130A rated)
   - 1V8_CORE: 0.5A (TLV75518 rated)
3. Measure output voltage with 6.5-digit DMM using Kelvin connection
4. Record ambient temperature
5. Repeat at -40C, 0C, 25C, 55C, 85C

**Pass/Fail Criteria:**

| Rail | Nominal | Tolerance | Min | Max |
|------|---------|-----------|-----|-----|
| 5V_SYS | 5.000V | +/- 2% | 4.900V | 5.100V |
| 3V3_IO | 3.300V | +/- 3% | 3.201V | 3.399V |
| 1V8_CORE | 1.800V | +/- 3% | 1.746V | 1.854V |

### 5.2 Load Regulation

**Objective:** Verify output voltage remains within specification from no-load to full-load.

**Procedure:**
1. Set input to 13.5V
2. Sweep load from 10% to 100% of rated current in 10% steps
3. Measure output voltage at each step
4. Calculate load regulation: (V_no_load - V_full_load) / V_nominal x 100%

**Pass/Fail Criteria:**

| Rail | Load Regulation Limit |
|------|-----------------------|
| 5V_SYS | <= 1.0% (0A to 6A) |
| 3V3_IO | <= 1.5% (0A to 3A) |
| 1V8_CORE | <= 2.0% (0A to 0.5A) |

### 5.3 Line Regulation

**Objective:** Verify output remains within specification across the full input voltage range.

**Procedure:**
1. Set load to 50% rated current (typical operating point)
2. Sweep input voltage: 6V, 8V, 10V, 12V, 13.5V, 16V, 24V, 28V, 36V
3. Measure output voltage at each input level
4. Calculate line regulation: (V_out_max - V_out_min) / V_nominal x 100%

**Pass/Fail Criteria:**

| Rail | Input Range | Line Regulation Limit |
|------|-------------|----------------------|
| 5V_SYS | 6V - 36V | <= 0.5% |
| 3V3_IO | 6V - 36V (via 5V_SYS) | <= 0.3% |
| 1V8_CORE | 6V - 36V (via 3V3_IO) | <= 0.3% |

### 5.4 Ripple and Noise

**Objective:** Measure output ripple/noise under rated load conditions.

**Measurement Method:**
- Oscilloscope: 20 MHz bandwidth limit (per JESD22-A114 methodology)
- Probe: Tip-and-barrel or ground spring (no ground lead wire)
- Measurement point: Directly at output capacitor
- Coupling: AC, 20 MHz BW limit
- Time base: Capture minimum 10 switching cycles
- Statistics: Record Vpp over 1000 acquisitions

**Pass/Fail Criteria:**

| Rail | Ripple Limit (Vpp, 20 MHz BW) | Switching Frequency |
|------|-------------------------------|---------------------|
| 5V_SYS | < 50 mV pk-pk | 2.1 MHz (LM61460) |
| 3V3_IO | < 30 mV pk-pk | 2.5 MHz (TPS62130A) |
| 1V8_CORE | < 20 mV pk-pk | N/A (LDO, no switching) |

### 5.5 Transient Response (Load Step)

**Objective:** Verify output recovers within specification after sudden load change.

**Procedure:**
1. Set input to 13.5V
2. Apply load step: 25% to 75% of rated current, 1A/us slew rate
3. Capture output waveform on oscilloscope (single-shot, pre-trigger)
4. Measure: overshoot, undershoot, recovery time (to within 2% of nominal)

**Pass/Fail Criteria:**

| Rail | Max Undershoot | Max Overshoot | Recovery Time |
|------|----------------|---------------|---------------|
| 5V_SYS | < 200 mV | < 200 mV | < 50 us |
| 3V3_IO | < 150 mV | < 150 mV | < 30 us |
| 1V8_CORE | < 100 mV | < 100 mV | < 100 us |

### 5.6 Power Sequencing Verification

**Objective:** Verify correct power-up and power-down rail ordering.

**Expected Sequence (Power-Up):**
```
Time -->
VIN_PROT   __|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
5V_SYS     ____|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^  (t1 = VIN stable + 2ms)
3V3_IO     ________|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^  (t2 = t1 + 5ms typ)
1V8_CORE   ____________|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^   (t3 = t2 + 2ms typ)
PG_ALL     ________________|^^^^^^^^^^^^^^^^^^^^^^^^^   (t4 = all PG asserted)
SOM_PWR_EN __________________|^^^^^^^^^^^^^^^^^^^^^^^   (t5 = t4 + 1ms)
```

**Procedure:**
1. Connect oscilloscope channels to all rail outputs and PG signals
2. Apply input voltage step (0V to 13.5V)
3. Capture all channels simultaneously (single-shot trigger on VIN)
4. Verify monotonic rise on each rail
5. Verify sequencing order matches specification
6. Verify no rail exceeds its nominal + 5% during power-up transient

**Pass/Fail Criteria:**
- Sequence order maintained: 5V_SYS -> 3V3_IO -> 1V8_CORE -> PG_ALL -> SOM_PWR_EN
- No reverse sequencing events
- Monotonic rise (no voltage dips during startup)
- Total power-up time (VIN applied to SOM_PWR_EN): < 50 ms

### 5.7 Over-Current Protection (OCP)

**Objective:** Verify over-current protection activates within specified limits.

**Procedure:**
1. Gradually increase load current beyond rated value
2. Monitor output voltage and input current
3. Record trip point (output collapses or hiccups)
4. Verify no permanent damage after OCP event
5. Verify auto-recovery when overload is removed

**Pass/Fail Criteria:**

| Rail | OCP Trip Point | Recovery | Damage |
|------|----------------|----------|--------|
| 5V_SYS | 7.0A - 9.0A (hiccup mode) | Auto-restart | No damage |
| 3V3_IO | 4.0A - 5.5A (hiccup mode) | Auto-restart | No damage |
| 1V8_CORE | 0.6A - 0.8A (current limit) | Auto-restart | No damage |

### 5.8 Thermal Shutdown

**Objective:** Verify thermal protection prevents permanent damage.

**Procedure:**
1. Operate at full load in thermal chamber
2. Increase ambient temperature beyond rated maximum
3. Monitor junction temperature (via thermal test point or IR camera)
4. Record shutdown temperature
5. Verify restart after cool-down

**Pass/Fail Criteria:**
- Thermal shutdown activates before T_J = 150C (typical for TI converters)
- No permanent damage after thermal event
- Automatic restart when junction temperature falls below hysteresis threshold

### 5.9 Input Transient Immunity

**Objective:** Verify survival of automotive input transients per ISO 7637-2.

**Procedure:**
1. Apply ISO 7637-2 test pulses (1, 2a, 2b, 3a, 3b, 4, 5a, 5b)
2. Monitor all output rails during transient events
3. Verify system operation during and after each pulse

**Pass/Fail Criteria:**
- No permanent damage from any ISO 7637-2 pulse
- Output rails remain within specification during Pulse 3a/3b (superimposed AC)
- System recovers within 100 ms after Pulse 1 (battery disconnect)
- Load dump (40V, Pulse 5b): TVS clamps, no component failure

## 6. Temperature Characterization Matrix

| Parameter | -40C | -20C | 0C | 25C | 55C | 85C |
|-----------|------|------|-----|------|------|------|
| 5V accuracy | | | | | | |
| 5V ripple | | | | | | |
| 3V3 accuracy | | | | | | |
| 3V3 ripple | | | | | | |
| 1V8 accuracy | | | | | | |
| 1V8 ripple | | | | | | |
| Efficiency | | | | | | |
| Sequencing time | | | | | | |

## 7. Efficiency Measurement

**Procedure:**
1. Measure input power: P_in = V_in x I_in
2. Measure output power per rail: P_out = V_out x I_out
3. Calculate total efficiency: eta = (P_out_total / P_in) x 100%
4. Sweep load from 10% to 100%

**Target Efficiency:**

| Condition | Minimum Efficiency |
|-----------|-------------------|
| 5V_SYS at 50% load | >= 90% |
| 5V_SYS at full load | >= 88% |
| System total (all rails) at typical load | >= 82% |

## 8. Reporting

Test results shall be recorded in the DVT Report (ADVIS-VT-DVT-001) with:
- Raw measurement data
- Statistical analysis (mean, std dev, Cpk where applicable)
- Temperature plots
- Oscilloscope screenshots for ripple and transient tests
- Pass/Fail summary matrix

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | 2024-01-15 | Hardware Validation Team | Initial draft |

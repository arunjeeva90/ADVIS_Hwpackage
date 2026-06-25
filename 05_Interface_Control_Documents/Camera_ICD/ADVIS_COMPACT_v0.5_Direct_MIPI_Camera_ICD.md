# ADVIS v0.5 Compact Direct-MIPI Camera Interface Control Document

**Classification:** Confidential - Engineering Use Only  
**Version:** 0.1 (Draft)  
**Date:** July 2026  
**Applies to:** ADVIS v0.5 Compact Production-Cost-Down Module

---

## 1. Scope

This ICD defines the camera interfaces for the ADVIS v0.5 compact windshield-mounted module. Both cameras connect to the shared SoC via direct MIPI CSI-2 interfaces. No serializer/deserializer (SerDes) or FPD-Link is used in the default compact variant.

---

## 2. Forward Camera Interface

### 2.1 MIPI CSI-2 Data Interface

| Parameter | Specification |
|-----------|--------------|
| Protocol | MIPI CSI-2 |
| Lane count | 2-lane or 4-lane (TBD based on sensor and SoC port availability) |
| Data rate per lane | Up to 2.5 Gbps (MIPI D-PHY v2.1 class) |
| Differential impedance | 85-100 ohm (controlled impedance, target 90 ohm) |
| Trace length | Short (under 50 mm on PCB, sensor co-located in module) |
| Connector | Direct PCB trace or short rigid-flex to sensor PCB |
| Signal pairs | CLK+/CLK-, D0+/D0-, D1+/D1- [, D2+/D2-, D3+/D3- if 4-lane] |
| Virtual channel | VC0 (Forward camera) |

### 2.2 I2C Control Interface

| Parameter | Specification |
|-----------|--------------|
| Bus | I2C (400 kHz standard, 1 MHz fast-mode optional) |
| Lines | SCL, SDA |
| Pull-ups | 4.7k to sensor I/O voltage (1.8V or 3.3V depending on sensor) |
| Address | Sensor-specific default (may require reprogramming if conflicts) |
| Purpose | Sensor register configuration, mode control, status readback |

### 2.3 Control Signals

| Signal | Direction | Description |
|--------|-----------|-------------|
| FWCAM_RESET_N | SoC to sensor | Active-low hardware reset |
| FWCAM_PWDN | SoC to sensor | Power-down control (active polarity sensor-dependent) |
| FWCAM_MCLK | SoC to sensor | Master clock output (24 MHz or 27 MHz, sensor-dependent) |
| FWCAM_FSYNC | SoC to sensor | Frame synchronization trigger (optional, for synchronized capture) |

### 2.4 Power Rails

| Rail | Voltage | Purpose |
|------|---------|---------|
| AVDD | 2.8V or 2.9V (sensor-dependent) | Analog supply |
| DVDD | 1.05V or 1.2V (sensor-dependent) | Digital core supply |
| DOVDD | 1.8V | Digital I/O supply (I2C, MIPI I/O) |

### 2.5 Sensor Candidate Placeholders

| Candidate | Resolution | Interface | Key Feature |
|-----------|-----------|-----------|-------------|
| Sony IMX390 | 2.45 MP | 4-lane MIPI CSI-2 | HDR, automotive qualified, LED flicker mitigation |
| OmniVision OX03C10 | 3.0 MP | 4-lane MIPI CSI-2 | HDR, automotive, low-light |
| ON Semi AR0233 | 2.3 MP | 4-lane MIPI CSI-2 | HDR, automotive, LED flicker |

*Final sensor selection is an open item. Interface definition must accommodate all candidates.*

---

## 3. DMS Camera Interface

### 3.1 MIPI CSI-2 Data Interface

| Parameter | Specification |
|-----------|--------------|
| Protocol | MIPI CSI-2 |
| Lane count | 1-lane or 2-lane (TBD based on sensor resolution and frame rate) |
| Data rate per lane | Up to 2.5 Gbps (MIPI D-PHY v2.1 class) |
| Differential impedance | 85-100 ohm (controlled impedance, target 90 ohm) |
| Trace/flex length | Up to 50 mm (short flex or rigid-flex from main PCB to DMS sensor) |
| Connector | ZIF flex connector or soldered rigid-flex |
| Signal pairs | CLK+/CLK-, D0+/D0- [, D1+/D1- if 2-lane] |
| Virtual channel | VC1 (DMS camera) |

### 3.2 I2C Control Interface

| Parameter | Specification |
|-----------|--------------|
| Bus | I2C (400 kHz standard) |
| Lines | SCL, SDA (routed through flex connector) |
| Pull-ups | 4.7k to sensor I/O voltage on main PCB side |
| Address | Sensor-specific default |
| Purpose | Sensor register configuration, mode control, IR mode settings |

### 3.3 Control Signals

| Signal | Direction | Description |
|--------|-----------|-------------|
| DMS_RESET_N | SoC to sensor | Active-low hardware reset |
| DMS_PWDN | SoC to sensor | Power-down control |
| DMS_MCLK | SoC to sensor | Master clock output (24 MHz or 27 MHz) |
| DMS_STROBE | SoC to sensor | IR LED strobe sync (optional, for synchronized IR illumination) |

### 3.4 Power Rails

| Rail | Voltage | Purpose |
|------|---------|---------|
| AVDD | 2.8V (sensor-dependent) | Analog supply |
| DVDD | 1.2V (sensor-dependent) | Digital core supply |
| DOVDD | 1.8V | Digital I/O supply |

*All DMS power rails routed through flex connector from main PCB regulators.*

### 3.5 Optional Flex Connector (~5 cm)

| Parameter | Specification |
|-----------|--------------|
| Type | ZIF (zero insertion force) or soldered rigid-flex |
| Length | Approximately 50 mm (adjustable per housing geometry) |
| Width | TBD (depends on signal count and layer count) |
| Layers | Minimum 4-layer (signal-ground-ground-signal) for impedance control |
| Signals carried | MIPI data lanes, MIPI clock, I2C (SCL, SDA), reset, MCLK, strobe, power rails, GND |
| Impedance | 90 ohm differential (MIPI pairs) |
| Shielding | Ground planes in flex provide shielding |
| Bend radius | Minimum 1 mm for flex portions |
| Mating cycles | Minimum 20 cycles (production + service) for ZIF type |

### 3.6 Sensor Candidate Placeholders

| Candidate | Resolution | Interface | Key Feature |
|-----------|-----------|-----------|-------------|
| OmniVision OX01N1B | 1.0 MP | 1-lane MIPI CSI-2 | NIR-optimized, automotive DMS |
| OmniVision OX01H1B | 1.0 MP | 1-lane MIPI CSI-2 | NIR-optimized, compact package |
| RGB-IR sensor (vendor TBD) | 1-2 MP | 1 or 2-lane MIPI CSI-2 | Combined visible + NIR capture |
| ON Semi AR0144 | 1.0 MP | 1-lane MIPI CSI-2 | Global shutter, NIR-enhanced |

*Final sensor selection is an open item.*

---

## 4. Direct MIPI Design Assumptions

### 4.1 Short Trace/Flex Length

- MIPI CSI-2 operates at multi-Gbps per lane; trace/flex length must be minimized
- Maximum combined trace + flex length: 50 mm (DMS), 30 mm (forward)
- Short lengths relax signal integrity requirements and reduce ESD/EMI risk
- No equalization or retiming required at these lengths

### 4.2 Controlled Impedance

- All MIPI differential pairs routed as controlled-impedance pairs
- Target: 90 ohm differential (45 ohm single-ended)
- Impedance tolerance: +/- 10%
- Reference planes must be continuous under all MIPI traces
- No trace routing over plane splits or voids

### 4.3 ESD Protection

- ESD protection diodes on all MIPI lanes at the flex connector interface
- Component: Low-capacitance TVS array (under 0.5 pF per line)
- Placement: Close to connector/flex transition point
- Required for DMS flex connector; optional for forward camera if fully enclosed

### 4.4 Connector/Flex Constraints

- Flex connector must support impedance-controlled differential pairs
- ZIF connector pitch: 0.3 mm or 0.5 mm (depending on signal count)
- Connector rated for automotive temperature range (-40 C to +85 C)
- Connector vibration rating per ISO 16750-3

### 4.5 No PoC (Power-over-Coax)

- No Power-over-Coax network in the compact variant
- Camera sensors powered directly from local PCB regulators
- Eliminates PoC inductors, DC blocking caps, and bias network

### 4.6 No FPD-Link Serializer/Deserializer

- No DS90UB954 or DS90UB953 in the default compact variant
- No FPD-Link coaxial cable interface
- No FAKRA or HSD connectors
- SerDes is only used in the separate v0.4.4 A-sample or remote-camera OEM variants

---

## 5. SoC CSI Port Mapping (Preliminary)

| SoC Port | Assigned Camera | Lane Config | Notes |
|----------|----------------|-------------|-------|
| CSI2-RX0 | Forward camera | 4-lane (or 2-lane TBD) | Primary perception input |
| CSI2-RX1 | DMS camera | 2-lane (or 1-lane TBD) | Driver monitoring input |

*Exact port mapping depends on SoC selection (TDA4VL / TDA4VM / AM62A).*

---

## 6. Power Sequencing (Camera)

### 6.1 Forward Camera Power-On Sequence

```
1. 1.8V DOVDD stable
2. 1.05V/1.2V DVDD stable (sensor-dependent)
3. 2.8V/2.9V AVDD stable (sensor-dependent)
4. Wait t_stable (sensor datasheet)
5. Release RESET_N (drive HIGH)
6. Provide MCLK
7. I2C configuration begins
8. MIPI CSI-2 stream starts
```

### 6.2 DMS Camera Power-On Sequence

Same as forward camera, applied to DMS rails. DMS power-on may be staggered after forward camera to limit inrush current.

### 6.3 Power-Off Sequence

Reverse order of power-on. Assert RESET_N before removing power rails.

---

## 7. Open Items

| # | Item | Owner | Status |
|---|------|-------|--------|
| 1 | Final forward sensor selection | Systems | Open |
| 2 | Final DMS sensor selection | Systems | Open |
| 3 | MIPI lane count per sensor (1/2/4) | Systems/SoC | Open |
| 4 | SoC CSI port availability and pin assignment | SoC Lead | Open |
| 5 | Clocking strategy (MCLK source, frequency) | Electrical | Open |
| 6 | Flex connector part number | Mechanical/Electrical | Open |
| 7 | Camera module mechanical ICD (sensor PCB dimensions, mounting) | Mechanical | Open |
| 8 | Image sensor power sequencing timing values | Power/Electrical | Open |
| 9 | ESD protection component selection | Electrical | Open |
| 10 | MIPI signal integrity simulation | SI Engineer | Open |
| 11 | Flex impedance characterization | SI Engineer | Open |
| 12 | Camera module thermal contribution to system budget | Thermal | Open |
| 13 | I2C address conflict resolution (if both sensors share bus) | Electrical | Open |
| 14 | Frame sync strategy (free-running vs. triggered) | Systems | Open |

---

*End of Document*

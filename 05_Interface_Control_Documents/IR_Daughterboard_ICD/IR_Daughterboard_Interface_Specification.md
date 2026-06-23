# ADVIS IR Daughterboard Interface Specification

## Version
v1.0 - June 2026

## Document ID
ICD-IR-001

---

## 1. Purpose

This Interface Control Document defines the interface between the ADVIS carrier board and the IR (infrared) illumination daughterboard via the J800 connector. The IR board provides near-infrared illumination for the Driver Monitoring System (DMS) camera in low-light and nighttime conditions.

---

## 2. Interface Overview

```
    ADVIS CARRIER BOARD                    IR DAUGHTERBOARD
    ====================                   ================

    +----------------+                     +------------------+
    |                |    J800 (8-pin)     |                  |
    |  SoM           |----- IR_LED_EN ---->| IR LED Driver    |
    |  (GPIO)        |----- IR_PWM ------->| (PWM dimming)    |
    |                |                     |                  |
    |  5V_SYS        |----- VCC_IR ------->| Power Input      |
    |  (current      |                     | (filtered)       |
    |   limited)     |                     |                  |
    |                |<---- FAULT_N -------| Fault Output     |
    |                |                     | (open-drain)     |
    |                |                     |                  |
    |  BOARD_GND     |----- GND ---------->| Ground           |
    |  BOARD_GND     |----- GND ---------->| Ground (return)  |
    |                |                     |                  |
    |  CHASSIS_GND   |----- SHIELD ------->| Shield/EMI       |
    |                |                     |                  |
    +----------------+                     +------------------+
```

---

## 3. J800 Connector Pin Allocation

| Pin | Signal Name | Direction | Type | Description |
|-----|-------------|-----------|------|-------------|
| 1 | VCC_IR | Carrier -> IR Board | Power | 5V supply (current limited) |
| 2 | GND | Common | Power | Power and signal ground |
| 3 | IR_LED_EN | Carrier -> IR Board | 3.3V Logic | Enable IR LED driver |
| 4 | IR_PWM | Carrier -> IR Board | 3.3V PWM | LED intensity control |
| 5 | FAULT_N | IR Board -> Carrier | Open-drain | Fault indicator (active low) |
| 6 | GND | Common | Power | Additional ground return |
| 7 | SHIELD | Common | Ground | EMI/ESD shield connection |
| 8 | RESERVED | N/A | N/A | Reserved for future use |

---

## 4. Power Supply (VCC_IR)

| Parameter | Specification |
|-----------|---------------|
| Nominal voltage | 5.0V (from 5V_SYS rail) |
| Voltage range | 4.75V to 5.25V |
| Maximum current | 500mA (carrier-side current limit) |
| Current limit method | PTC resettable fuse or active current limiter |
| Inrush current | < 1A for < 1ms (capacitor charge) |
| Ripple (max) | < 100mV pk-pk at IR board input |
| Power dissipation (IR board) | Maximum 2.5W (500mA at 5V) |

---

## 5. IR_LED_EN (Enable Signal)

| Parameter | Specification |
|-----------|---------------|
| Signal type | Digital logic output from SoM GPIO |
| Logic high (LEDs enabled) | 2.4V to 3.6V (3.3V CMOS) |
| Logic low (LEDs disabled) | 0V to 0.4V |
| Default state (power-up) | LOW (LEDs disabled) |
| Source impedance | < 100 ohm |
| Enable delay | IR board must enable LEDs within 1ms of EN high |
| Disable delay | IR board must disable LEDs within 100us of EN low |

### Enable/Disable Logic

```
IR_LED_EN = HIGH  AND  IR_PWM active  -->  LEDs illuminated
IR_LED_EN = HIGH  AND  IR_PWM = LOW   -->  LEDs OFF (but driver ready)
IR_LED_EN = LOW   (any IR_PWM state)  -->  LEDs OFF, driver shutdown
```

---

## 6. IR_PWM (Intensity Control)

| Parameter | Specification |
|-----------|---------------|
| Signal type | PWM output from SoM timer/PWM peripheral |
| Frequency range | 1 kHz to 50 kHz (nominal 20 kHz) |
| Duty cycle range | 0% (off) to 100% (maximum brightness) |
| Logic high | 2.4V to 3.6V (3.3V CMOS) |
| Logic low | 0V to 0.4V |
| Rise/fall time | < 50ns |
| PWM resolution | Minimum 8-bit effective (256 steps) |
| Linearity | Optical output approximately linear with duty cycle |

### PWM to Brightness Mapping

| Duty Cycle | IR Output | Use Case |
|-----------|-----------|----------|
| 0% | Off | Daylight (camera uses ambient) |
| 10-30% | Low | Dawn/dusk, some ambient light |
| 30-70% | Medium | Nighttime, normal cabin |
| 70-100% | High | Nighttime, sunglasses, dark skin tones |

---

## 7. FAULT_N (Fault Indicator)

| Parameter | Specification |
|-----------|---------------|
| Signal type | Open-drain output from IR board |
| Active state | LOW (fault present) |
| Inactive state | HIGH (pulled up on carrier, no fault) |
| Pull-up resistor | 10k ohm to 3.3V (on carrier board) |
| Fault conditions | Over-temperature, LED open, LED short, overcurrent |
| Fault assertion delay | < 10ms from fault occurrence |
| Fault deassert | After fault condition clears AND re-enable cycle |

### Fault Handling by ADVIS Firmware

| Fault Type | Detection | Response |
|-----------|-----------|----------|
| FAULT_N asserted | GPIO interrupt on SoM | Disable IR_LED_EN, log event |
| Persistent fault | FAULT_N stays low after re-enable attempt | Disable IR permanently until reset |
| Thermal fault | FAULT_N + temperature threshold | Reduce duty cycle or disable |

---

## 8. Thermal Protection

| Parameter | Specification |
|-----------|---------------|
| IR board max operating temp | +85C (board-level) |
| LED junction temp limit | Per LED datasheet (typically +125C) |
| Thermal shutdown | IR board driver IC handles internally |
| Thermal feedback to carrier | Via FAULT_N assertion |
| Carrier software response | Reduce PWM duty cycle or disable EN |

---

## 9. EMC and Safety Considerations

### 9.1 EMC

| Parameter | Specification |
|-----------|---------------|
| PWM frequency | > 1 kHz to stay above audible range |
| EMI filtering | Ferrite bead on VCC_IR at connector |
| Shield connection | Pin 7 to CHASSIS_GND through connector shell |
| Cable length (J800) | < 100mm (board-to-board, internal to enclosure) |

### 9.2 Eye Safety

| Parameter | Specification |
|-----------|---------------|
| Wavelength | 850nm or 940nm (near-infrared) |
| Eye safety class | IEC 62471 Risk Group 1 (Low Risk) maximum |
| Maximum irradiance | Must comply with IEC 62471 at 200mm distance |
| Labeling | IR emission warning label on enclosure |
| Fail-safe | IR disabled by default, requires active enable |

---

## 10. Mechanical Interface

| Parameter | Specification |
|-----------|---------------|
| Connector type | Board-to-board, 8-pin, 1.0mm pitch |
| Stacking height | 5mm to 8mm (allows IR board above carrier PCB) |
| Alignment | Polarized connector (cannot be inserted reversed) |
| Retention force | > 10N (internal, no vibration risk) |
| Mating cycles | Minimum 50 (factory assembly + service) |

---

## 11. IR Board Functional Requirements

| Requirement | Specification |
|-------------|---------------|
| LED count | 2 to 6 IR LEDs (per illumination requirement) |
| LED driver topology | Constant-current driver with PWM dimming input |
| Current regulation | +/- 5% accuracy per LED |
| Turn-on time | < 1ms from EN high + PWM first pulse |
| Turn-off time | < 100us from EN low |
| Operating temperature | -40C to +85C ambient |
| MTBF target | > 50,000 hours (LED + driver combined) |

---

## 12. Revision History

| Rev | Date | Author | Change |
|-----|------|--------|--------|
| 1.0 | 2026-06 | Interface Team | Initial release |

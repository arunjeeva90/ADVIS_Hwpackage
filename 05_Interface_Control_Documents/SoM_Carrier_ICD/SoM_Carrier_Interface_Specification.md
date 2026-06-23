# ADVIS SoM-Carrier Interface Specification

## Version
v1.0 - June 2026

## Document ID
ICD-SOM-001

## Classification
CONFIDENTIAL - Logical interface only. Physical pin assignments are TRADE SECRET and maintained separately.

---

## 1. Purpose

This Interface Control Document defines the logical interface between the ADVIS carrier board and any compatible System-on-Module (SoM). It specifies signal groups, electrical requirements, power rails, sequencing, and directionality.

**Note:** This document intentionally omits physical pin numbers, connector pin assignments, and pinout diagrams. Those are maintained in a separate trade-secret-protected document.

---

## 2. Interface Philosophy

The SoM-Carrier interface is the core platform IP boundary. Any SoM module that conforms to this logical interface specification can be integrated with the ADVIS carrier board without hardware modification (assuming compatible connector form factor).

---

## 3. Signal Groups

### 3.1 Power Rails (Carrier to SoM)

| Signal Name | Direction | Voltage | Max Current | Description |
|-------------|-----------|---------|-------------|-------------|
| 5V_SOM | Carrier -> SoM | 5.0V +/- 3% | 4A | Primary power input to SoM PMIC |
| 3V3_SOM | Carrier -> SoM | 3.3V +/- 3% | 500mA | I/O power for 3.3V interfaces |
| 1V8_SOM | Carrier -> SoM | 1.8V +/- 3% | 200mA | I/O power for 1.8V interfaces |
| GND | Common | 0V | N/A | Power and signal return (multiple pins) |

### 3.2 Camera Interface (Carrier to SoM)

| Signal Name | Direction | Type | Description |
|-------------|-----------|------|-------------|
| CSI2_CLK_P | Carrier -> SoM | MIPI D-PHY | CSI-2 clock positive |
| CSI2_CLK_N | Carrier -> SoM | MIPI D-PHY | CSI-2 clock negative |
| CSI2_D0_P | Carrier -> SoM | MIPI D-PHY | CSI-2 data lane 0 positive |
| CSI2_D0_N | Carrier -> SoM | MIPI D-PHY | CSI-2 data lane 0 negative |
| CSI2_D1_P | Carrier -> SoM | MIPI D-PHY | CSI-2 data lane 1 positive |
| CSI2_D1_N | Carrier -> SoM | MIPI D-PHY | CSI-2 data lane 1 negative |
| CSI2_D2_P | Carrier -> SoM | MIPI D-PHY | CSI-2 data lane 2 positive |
| CSI2_D2_N | Carrier -> SoM | MIPI D-PHY | CSI-2 data lane 2 negative |
| CSI2_D3_P | Carrier -> SoM | MIPI D-PHY | CSI-2 data lane 3 positive |
| CSI2_D3_N | Carrier -> SoM | MIPI D-PHY | CSI-2 data lane 3 negative |

### 3.3 I2C Bus (SoM Master)

| Signal Name | Direction | Type | Description |
|-------------|-----------|------|-------------|
| I2C_SCL | Bidirectional | Open-drain, 3.3V | I2C clock (SoM is master) |
| I2C_SDA | Bidirectional | Open-drain, 3.3V | I2C data |

### 3.4 SPI Bus (SoM Master)

| Signal Name | Direction | Type | Description |
|-------------|-----------|------|-------------|
| SPI_SCLK | SoM -> Carrier | 1.8V CMOS | SPI clock |
| SPI_MOSI | SoM -> Carrier | 1.8V CMOS | SPI master-out slave-in |
| SPI_MISO | Carrier -> SoM | 1.8V CMOS | SPI master-in slave-out |
| SPI_CS_ACCEL | SoM -> Carrier | 1.8V CMOS | Chip select for BMI088 accelerometer |
| SPI_CS_GYRO | SoM -> Carrier | 1.8V CMOS | Chip select for BMI088 gyroscope |

### 3.5 UART Interfaces

| Signal Name | Direction | Type | Description |
|-------------|-----------|------|-------------|
| UART_GNSS_TX | SoM -> Carrier | 3.3V CMOS | UART transmit to GNSS module |
| UART_GNSS_RX | Carrier -> SoM | 3.3V CMOS | UART receive from GNSS module |
| UART_DBG_TX | SoM -> Carrier | 3.3V CMOS | Debug console transmit |
| UART_DBG_RX | Carrier -> SoM | 3.3V CMOS | Debug console receive |

### 3.6 CAN-FD Interface

| Signal Name | Direction | Type | Description |
|-------------|-----------|------|-------------|
| CAN_TXD | SoM -> Carrier | 3.3V/5V tolerant | CAN transmit data to PHY |
| CAN_RXD | Carrier -> SoM | 3.3V CMOS | CAN receive data from PHY |

### 3.7 USB Interface

| Signal Name | Direction | Type | Description |
|-------------|-----------|------|-------------|
| USB_DP | Bidirectional | USB 2.0 | USB data positive |
| USB_DM | Bidirectional | USB 2.0 | USB data negative |

### 3.8 SD/MMC Interface

| Signal Name | Direction | Type | Description |
|-------------|-----------|------|-------------|
| SD_CLK | SoM -> Carrier | 3.3V CMOS | SD clock |
| SD_CMD | Bidirectional | 3.3V CMOS | SD command |
| SD_DAT0 | Bidirectional | 3.3V CMOS | SD data bit 0 |
| SD_DAT1 | Bidirectional | 3.3V CMOS | SD data bit 1 |
| SD_DAT2 | Bidirectional | 3.3V CMOS | SD data bit 2 |
| SD_DAT3 | Bidirectional | 3.3V CMOS | SD data bit 3 |
| SD_CD_N | Carrier -> SoM | 3.3V CMOS | Card detect (active low) |

### 3.9 GPIO and Control

| Signal Name | Direction | Type | Description |
|-------------|-----------|------|-------------|
| SOM_BOOT_OK | SoM -> Carrier | 3.3V CMOS | SoM firmware ready indicator |
| RESET_N | Carrier -> SoM | Open-drain | System reset (active low) |
| IR_LED_EN | SoM -> Carrier | 3.3V CMOS | IR LED enable command |
| IR_PWM | SoM -> Carrier | 3.3V CMOS | IR LED intensity PWM |
| CAN_STB | SoM -> Carrier | 3.3V CMOS | CAN standby control |
| IMU_INT_A | Carrier -> SoM | 1.8V CMOS | BMI088 accelerometer interrupt |
| IMU_INT_G | Carrier -> SoM | 1.8V CMOS | BMI088 gyroscope interrupt |
| GNSS_PPS | Carrier -> SoM | 3.3V CMOS | GNSS 1PPS timing pulse |

---

## 4. Electrical Requirements

### 4.1 Voltage Levels

| Domain | Voltage | Tolerance | Rise Time |
|--------|---------|-----------|-----------|
| Power (5V) | 5.0V | +/- 3% | < 5ms (soft-start) |
| I/O (3.3V) | 3.3V | +/- 3% | < 2ms |
| I/O (1.8V) | 1.8V | +/- 3% | < 1ms |
| MIPI D-PHY | Per MIPI spec | N/A | N/A |
| USB 2.0 | Per USB spec | N/A | N/A |

### 4.2 Signal Integrity

| Interface | Impedance | Length Matching | Notes |
|-----------|-----------|----------------|-------|
| CSI-2 | 100 ohm diff | 0.5mm intra-pair | AC-coupled at SoM |
| USB | 90 ohm diff | 0.15mm intra-pair | ESD at connector |
| SPI | 50 ohm SE | Not critical | Keep < 50mm total |
| I2C | Not controlled | Not critical | 2.2k pull-ups on carrier |
| UART | Not controlled | Not critical | Standard routing |

---

## 5. Power Sequencing Requirements

The SoM must accept the following power-up sequence:

1. 5V_SOM applied first (carrier 5V_SYS available)
2. 3V3_SOM applied after 5V stable (PG_5V asserted)
3. 1V8_SOM applied after 3V3 stable (PG_3V3 asserted)
4. SoM internal PMIC sequences after all external rails stable
5. SoM asserts SOM_BOOT_OK when firmware is ready to service watchdog

### Power-Down Sequence

Reverse order: SoM shuts down internally, then 1V8, then 3V3, then 5V removed.

---

## 6. Reset Behavior

| Signal | Condition | Action |
|--------|-----------|--------|
| RESET_N asserted (low) | 3V3 UV or watchdog timeout | SoM enters reset state |
| RESET_N deasserted (high) | Power good and WDG OK | SoM boots |
| Minimum reset pulse | > 10ms | Ensures clean reset |

---

## 7. Watchdog Interface

| State | SOM_BOOT_OK | Watchdog | Behavior |
|-------|-------------|----------|----------|
| Boot in progress | LOW | Disabled | SoM booting, no WDG requirement |
| Firmware running | HIGH | Enabled | SoM must toggle WDI within timeout |
| SoM fault/hang | HIGH (stuck) | Timeout | RESET_N asserted by TPS3431 |

---

## 8. Connector Requirements

| Parameter | Specification |
|-----------|---------------|
| Connector type | High-density board-to-board |
| Minimum pin count | 120 pins (to accommodate all signals + ground) |
| Current rating | 1A per power pin, multiple power pins for high current |
| Mating cycles | Minimum 50 cycles |
| Operating temperature | -40C to +85C |
| Contact resistance | < 50 milliohms |

---

## 9. Revision History

| Rev | Date | Author | Change |
|-----|------|--------|--------|
| 1.0 | 2026-06 | Platform Team | Initial logical interface release |

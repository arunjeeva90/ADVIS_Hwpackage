# TN-002: SoC Selection Analysis

## Document Information

| Field | Value |
|-------|-------|
| **Number** | TN-002 |
| **Title** | SoC Selection Analysis for ADVIS Platform |
| **Author** | Systems Architect |
| **Date** | February 2026 |
| **Status** | Complete - Decision Implemented |
| **Applies To** | ADVIS ECU v0.2.0+ |

---

## 1. Objective

Select the optimal System-on-Chip platform for the ADVIS mid-tier (dual camera ADAS+DMS) product, considering AI inference performance, camera interface capability, power budget, software ecosystem, cost, and long-term scalability.

## 2. Requirements

| Requirement | Specification |
|-------------|--------------|
| Camera inputs | 2 minimum (forward + DMS), 4+ for high tier |
| AI inference | 2+ TOPS for dual DNN (ADAS + DMS) |
| Video processing | 2x 2MP @ 30fps minimum |
| CPU | Cortex-A class, Linux capable |
| Real-time core | Cortex-R or equivalent for safety functions |
| Memory | 2GB+ LPDDR4 |
| Power budget | 10-15W TDP (mid tier) |
| Interface | CSI-2 (4-lane), CAN-FD, SPI, I2C, UART, USB |
| OS support | Linux (Yocto/Ubuntu), TI RTOS |
| Temperature | -40C to +105C junction |
| Automotive grade | AEC-Q100 or equivalent |
| Supply longevity | 10+ year availability commitment |

## 3. Candidates Evaluated

### 3.1 Texas Instruments TDA4VM / AM68A

| Parameter | Specification |
|-----------|--------------|
| AI Accelerator | C7x DSP + MMA (8 TOPS) |
| CPU | 2x Cortex-A72 @ 2GHz |
| MCU/Safety | Cortex-R5F (lockstep capable) |
| Camera | Up to 8MP, 4x CSI-2 Rx ports |
| Memory | LPDDR4, up to 4GB |
| Power | 10-15W typical |
| Package | 23x23mm FCBGA |
| Automotive | AEC-Q100 Grade 2 (-40 to +105C) |
| Ecosystem | TI Edge AI SDK, Processor SDK Linux, TIDL |
| SOM Availability | Phytec phyCORE, Toradex, custom |

### 3.2 Qualcomm SA8295P

| Parameter | Specification |
|-----------|--------------|
| AI Accelerator | Hexagon DSP (30+ TOPS) |
| CPU | Kryo (8-core, up to 3.2GHz) |
| MCU/Safety | Integrated safety island |
| Camera | Up to 18 cameras, 8x CSI-2 |
| Memory | LPDDR5, up to 16GB |
| Power | 25-40W typical |
| Package | Large FCBGA |
| Automotive | AEC-Q100 equivalent |
| Ecosystem | QNX/Android Automotive, Snapdragon Ride |
| SOM Availability | Limited (Thundercomm, custom) |

### 3.3 NXP S32V344

| Parameter | Specification |
|-----------|--------------|
| AI Accelerator | APEX-2 (limited DL capability) |
| CPU | 4x Cortex-A53 @ 1GHz |
| MCU/Safety | Cortex-M7 (lockstep) |
| Camera | Up to 4x CSI-2, ISP included |
| Memory | DDR3L/LPDDR4, up to 2GB |
| Power | 5-8W typical |
| Package | 21x21mm FCBGA |
| Automotive | AEC-Q100 Grade 2 |
| Ecosystem | S32 Design Studio, GreenBox |
| SOM Availability | Limited |

### 3.4 Renesas R-Car V3H

| Parameter | Specification |
|-----------|--------------|
| AI Accelerator | CNN-IP (4.4 TOPS) |
| CPU | 2x Cortex-A53 @ 1.0GHz |
| MCU/Safety | Cortex-R7 |
| Camera | Up to 4x CSI-2 |
| Memory | LPDDR4, up to 4GB |
| Power | 8-12W typical |
| Package | FCBGA |
| Automotive | AEC-Q100 Grade 2 |
| Ecosystem | R-Car SDK, limited Linux community |
| SOM Availability | Very limited |

## 4. Comparison Matrix

| Criterion | Weight | TDA4VM/AM68A | SA8295P | S32V344 | R-Car V3H |
|-----------|--------|--------------|---------|---------|-----------|
| AI Performance | 20% | 8 | 10 | 4 | 6 |
| Power Efficiency | 15% | 9 | 4 | 8 | 8 |
| Camera Support | 10% | 9 | 10 | 7 | 7 |
| CPU Performance | 10% | 8 | 10 | 5 | 5 |
| Cost (SoC + SOM) | 15% | 7 | 3 | 8 | 6 |
| Ecosystem/Tools | 10% | 9 | 7 | 5 | 4 |
| SOM Availability | 10% | 9 | 4 | 4 | 3 |
| Supply Longevity | 5% | 8 | 6 | 8 | 7 |
| Safety (ASIL) | 5% | 8 | 7 | 9 | 7 |
| **Weighted Score** | **100%** | **8.25** | **6.55** | **5.95** | **5.85** |

## 5. Detailed Assessment

### 5.1 Why TDA4VM/AM68A Wins

1. **Best performance-per-watt**: 8 TOPS AI in 10-15W envelope hits the sweet spot for dual-camera processing without requiring active cooling in most automotive environments.

2. **Mature SOM ecosystem**: Phytec phyCORE-AM68A is production-ready with Linux BSP, validated thermal solution, and 10+ year supply commitment. This eliminates SOM NRE and reduces time-to-market by 6+ months.

3. **TI ecosystem synergy**: Using TI SoC alongside TI power (LM61460, TPS62130A), TI deserializer (DS90UB954), and TI CAN transceiver (TCAN1044AV) provides integrated tool support, unified FAE relationship, and validated reference designs.

4. **Scalability**: The TDA4x family spans from TDA4AL (low-cost) through TDA4VM (mid) to TDA4VH (high), allowing software reuse across the ADVIS product family with carrier PCB changes only.

5. **Open-source friendly**: TI provides open-source Linux kernel support, upstream contributions, and community documentation - critical for long-term maintenance.

### 5.2 Why SA8295P Was Rejected

- Significantly over-specified for dual-camera ADAS+DMS
- Power budget (25-40W) requires active cooling and larger enclosure
- BOM cost exceeds mid-tier target by 3-4x
- Limited SOM availability forces custom board design (higher NRE)
- Suitable for ADVIS Fusion high-tier (future consideration)

### 5.3 Why S32V344 Was Rejected

- AI performance insufficient for dual concurrent DNNs at target frame rate
- Limited deep learning support compared to dedicated AI accelerators
- SOM ecosystem immature; would require custom module design
- Better suited for simpler single-function applications

### 5.4 Why R-Car V3H Was Rejected

- Ecosystem maturity concerns (limited community, regional FAE support)
- SOM availability extremely limited (would require custom module)
- CNN-IP performance adequate but toolchain less mature than TIDL
- No clear upgrade path equivalent to TDA4x family scaling

## 6. Platform Scaling Strategy

The TDA4x family enables ADVIS to scale across product tiers:

| ADVIS Tier | SoC | AI Performance | Camera Count | Use Case |
|------------|-----|----------------|--------------|----------|
| Entry | AM62A | 2 TOPS (per AM62A7 product headline) | 1 | DMS only, fleet monitoring |
| Mid (baseline) | AM68A/TDA4VM | 8 TOPS | 2 | Full ADAS+DMS, ADVIS Assist/Control |
| High | TDA4VH | 32 TOPS | 4-8 | Surround view, sensor fusion, ADVIS Fusion |

Software IP (neural network models, safety functions) is portable across all tiers via TIDL runtime compatibility.

## 7. Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|-----------|
| TDA4VM end-of-life | Low | High | AM68A is long-life industrial variant of same silicon |
| Phytec SOM discontinuation | Low | Medium | Carrier designed for standard SODIMM-style connector; alternative SOMs available |
| AI performance insufficient | Medium | Medium | TIDL optimization ongoing; C7x+MMA architecture headroom exists |
| Thermal limit in harsh environments | Medium | Low | Active cooling option defined for high-ambient applications |

## 8. Decision

**Selected: TDA4VM/AM68A via Phytec phyCORE-AM68A SOM**

This selection provides the optimal balance of AI capability, power efficiency, ecosystem maturity, and cost for the ADVIS mid-tier platform while enabling clear upgrade paths for Entry and High tier variants.

---

*ADVIS Hardware Platform - Technical Note*

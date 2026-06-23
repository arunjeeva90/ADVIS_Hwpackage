# TN-001: Power Architecture Trade Study

## Document Information

| Field | Value |
|-------|-------|
| **Number** | TN-001 |
| **Title** | Power Architecture Trade Study |
| **Author** | Power Electronics Engineer |
| **Date** | March 2026 |
| **Status** | Complete - Decision Implemented |
| **Applies To** | ADVIS ECU v0.3.0+ |

---

## 1. Objective

Evaluate and select the optimal power architecture for the ADVIS ECU carrier board, converting vehicle 12V input to the required system rails (5V, 3.3V, 1.8V) while meeting automotive environmental, efficiency, and cost requirements.

## 2. Requirements Summary

| Parameter | Requirement |
|-----------|-------------|
| Input voltage | 9V - 16V continuous, 27V cranking (100ms), -16V reverse |
| Output rails | 5V (6A), 3.3V (3A), 1.8V (500mA) |
| Efficiency target | >85% at typical load |
| Operating temperature | -40C to +85C ambient |
| Automotive qualification | AEC-Q100 Grade 1 |
| EMI compliance | CISPR 25 Class 5 |
| Total BOM cost target | <$5 (power section, 10k qty) |
| PCB area budget | <15 cm^2 (power section) |

## 3. Options Evaluated

### Option A: Integrated PMIC (TPS65941-based)

**Architecture:**
```
12V -> [TPS65941 integrated PMIC] -> 5V, 3.3V, 1.8V, 0.85V (SoC core)
```

**Pros:**
- Minimal external components
- Smallest PCB area (~5 cm^2)
- Pre-validated power sequencing
- Single vendor solution with SoC

**Cons:**
- Tightly coupled to specific SoC family
- Limited current per rail (shared thermal budget)
- Single point of failure
- Difficult to second-source
- Requires SoC-specific register programming

**Cost Estimate:** $4.50 (PMIC) + $1.50 (passives) = $6.00

### Option B: Single Wide-Input Buck + LDOs

**Architecture:**
```
12V -> [Single 12V-to-3.3V Buck] -> 3.3V
                                       |-> [LDO] -> 1.8V
     -> [Separate 12V-to-5V Buck] -> 5V
```

**Pros:**
- Simple topology
- Two independent converters, partial redundancy

**Cons:**
- Two wide-input converters (more expensive, larger)
- LDO from 3.3V to 1.8V wastes power at higher currents
- Each converter must handle full input range independently
- Higher total component count vs cascaded

**Cost Estimate:** $3.00 (buck x2) + $0.80 (LDO) + $2.00 (passives) = $5.80

### Option C: Cascaded Discrete (Selected)

**Architecture:**
```
12V -> [LM61460-Q1 Buck, 6A] -> 5V_SYS
                                    |-> [TPS62130A-Q1 Buck] -> 3.3V
                                    |                            |-> [TLV75518-Q1 LDO] -> 1.8V
                                    |-> SOM 5V input
                                    |-> DS90UB954 VCC
```

**Pros:**
- High efficiency at each stage (>90% for bucks)
- Only one converter handles wide input range
- Downstream converters see stable 5V input (simpler, cheaper)
- Excellent thermal distribution across PCB
- Each part individually second-sourceable
- Field-proven TI automotive-qualified parts
- 1.8V LDO has minimal power dissipation (1.5V drop x 500mA = 750mW max)

**Cons:**
- More PCB area than PMIC (~12 cm^2)
- Requires explicit power sequencing (EN chain with PG signals)
- Three separate components to qualify

**Cost Estimate:** $2.20 (LM61460) + $1.40 (TPS62130A) + $0.45 (TLV75518) + $1.50 (passives) = $5.55

### Option D: GaN-Based Single Stage

**Architecture:**
```
12V -> [GaN half-bridge + digital controller] -> 5V (regulated)
                                                    |-> [Buck] -> 3.3V
                                                    |-> [LDO] -> 1.8V
```

**Pros:**
- Highest efficiency possible (>95%)
- Smallest inductor (high switching frequency)
- Future-looking technology

**Cons:**
- Limited automotive-qualified GaN FETs available
- Higher BOM cost ($8+)
- EMI challenges at high switching frequency
- Limited design community / reference designs
- Supply chain risk (single-source components)

**Cost Estimate:** $5.00 (GaN + controller) + $1.40 (buck) + $0.45 (LDO) + $2.00 (passives) = $8.85

## 4. Trade Matrix

| Criterion | Weight | Option A (PMIC) | Option B (Dual Buck) | Option C (Cascaded) | Option D (GaN) |
|-----------|--------|-----------------|---------------------|--------------------|----|
| Efficiency | 20% | 7 | 7 | 9 | 10 |
| Cost | 20% | 5 | 6 | 7 | 3 |
| PCB Area | 15% | 10 | 6 | 7 | 8 |
| Thermal | 15% | 5 | 7 | 9 | 8 |
| Second-source | 10% | 3 | 7 | 9 | 2 |
| Qualification | 10% | 8 | 8 | 9 | 4 |
| Flexibility | 5% | 3 | 6 | 8 | 7 |
| Risk | 5% | 6 | 7 | 8 | 4 |
| **Weighted Score** | **100%** | **6.15** | **6.70** | **8.20** | **6.05** |

## 5. Selection Rationale

**Option C (Cascaded Discrete)** is selected for the following reasons:

1. **Best weighted score** across all evaluation criteria
2. **Excellent second-sourcing**: Each component has multiple pin-compatible alternatives
3. **Thermal distribution**: Power dissipation spread across PCB area rather than concentrated
4. **Proven topology**: Cascaded buck conversion is well-understood with extensive reference designs
5. **Flexibility**: Individual rails can be upgraded independently for different product tiers
6. **Cost-competitive**: Meets BOM target at volume pricing
7. **Automotive ecosystem**: All three parts are TI automotive-qualified (AEC-Q100 Grade 1)

## 6. Implementation Details

### 6.1 LM61460-Q1 (12V to 5V)

| Parameter | Value |
|-----------|-------|
| Input range | 3.5V to 36V |
| Output | 5.0V |
| Max current | 6A |
| Switching frequency | 400kHz (default) to 2.2MHz |
| Efficiency | ~92% at 3A, 12Vin |
| Package | VQFN-13 (4x4mm) |

### 6.2 TPS62130A-Q1 (5V to 3.3V)

| Parameter | Value |
|-----------|-------|
| Input range | 3V to 17V |
| Output | 3.3V |
| Max current | 3A |
| Switching frequency | 2.5MHz (default) |
| Efficiency | ~93% at 1.5A, 5Vin |
| Package | QFN-16 (3x3mm) |

### 6.3 TLV75518-Q1 (3.3V to 1.8V)

| Parameter | Value |
|-----------|-------|
| Input range | 1.5V to 5.5V |
| Output | 1.8V (fixed) |
| Max current | 500mA |
| Dropout | 160mV at 500mA |
| Noise | 20uVrms |
| Package | SOT-23-5 |

## 7. Risk Mitigation

| Risk | Mitigation |
|------|-----------|
| LM61460 supply shortage | MPS MP8759 as pin-incompatible but function-compatible alternative |
| TPS62130A obsolescence | TPS62132 as drop-in replacement |
| Thermal limit at max load | Power budget analysis shows 18W typical (well under 25W absolute max) |
| EMI at switching frequency | Spread-spectrum option available on LM61460; layout optimization |

---

*ADVIS Hardware Platform - Technical Note*

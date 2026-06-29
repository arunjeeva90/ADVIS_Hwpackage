# TN-003: Camera Architecture Options Analysis

## Document Information

| Field | Value |
|-------|-------|
| **Number** | TN-003 |
| **Title** | Camera Interface Architecture Options |
| **Author** | Hardware Architect |
| **Date** | February 2026 |
| **Status** | Complete - Decision Implemented |
| **Applies To** | ADVIS ECU v0.2.0+ |

---

## 1. Objective

Evaluate camera interface architectures for the ADVIS dual-camera system (forward ADAS + DMS), selecting the optimal solution for the modular IP platform (Track 2) while defining a production cost-down path (Track 1).

## 2. System Requirements

| Parameter | Requirement |
|-----------|-------------|
| Camera count | 2 (forward + DMS), expandable to 4+ for high tier |
| Resolution | 2MP minimum per camera |
| Frame rate | 30 fps per camera (simultaneous) |
| Cable length | Up to 15m (forward camera at windshield) |
| Power delivery | Power-over-cable to remote camera modules |
| EMI immunity | Automotive EMC environment (near ignition, motors) |
| Temperature | -40C to +85C at connector |
| Connector count | Minimize harness complexity |
| Cost target | <$8 total camera interface BOM (ECU side) |

## 3. Options Evaluated

### Option A: FPD-Link III with DS90UB954-Q1 (Selected for Track 2)

**Architecture:**
```
Camera 1 [UB953 Serializer] --coax 15m-- [DS90UB954 Port0] --+
                                                               |-- CSI-2 4-lane --> SOM
Camera 2 [UB953 Serializer] --coax 15m-- [DS90UB954 Port1] --+
```

**Pros:**
- Long cable runs (up to 15m over single coax)
- Power-over-Coax eliminates separate power wires to cameras
- Single coax per camera simplifies vehicle harness
- Bidirectional I2C back-channel for camera configuration
- TI ecosystem synergy (same vendor as SoC, power, CAN)
- Dual-port aggregation to single CSI-2 output
- Virtual channel multiplexing (VC0=Forward, VC1=DMS)
- Automotive-qualified (AEC-Q100)
- Proven in production ADAS systems (millions deployed)

**Cons:**
- Higher BOM cost than direct MIPI (~$6 for deserializer + passives)
- Requires matching serializers at camera end (customer cost)
- Fixed to TI ecosystem (serializer must be UB953/UB933)
- Additional latency (~5us per link, negligible for 30fps)

**Cost Estimate (ECU side):** DS90UB954 ($4.50) + passives/ESD ($1.50) = $6.00

### Option B: Direct MIPI CSI-2 (Track 1 Cost-Down Path)

**Architecture:**
```
Camera 1 [MIPI CSI-2 direct] --FFC 10cm-- SOM CSI-2 Port 0
Camera 2 [MIPI CSI-2 direct] --FFC 10cm-- SOM CSI-2 Port 1
```

**Pros:**
- Lowest BOM cost (no serializer/deserializer IC)
- Lowest latency (direct connection)
- Simplest design (just connector + ESD protection)
- Native SOM interface (no driver complexity)

**Cons:**
- Cable length limited to ~10cm (PCB trace) or ~30cm (FFC/FPC)
- Not suitable for remote-mounted cameras (windshield, cabin pillar)
- Requires camera module physically attached to or very near ECU
- No power-over-cable (separate power routing needed)
- Uses two SOM CSI-2 ports (limits expansion)
- EMI susceptibility over longer cables
- No bidirectional control channel (separate I2C bus needed)

**Cost Estimate (ECU side):** Connectors + ESD ($1.50) = $1.50

### Option C: GMSL2 (Maxim/ADI)

**Architecture:**
```
Camera 1 [MAX96705 Serializer] --coax 15m-- [MAX9296A Port0] --+
                                                                 |-- CSI-2 --> SOM
Camera 2 [MAX96705 Serializer] --coax 15m-- [MAX9296A Port1] --+
```

**Pros:**
- Long cable runs (up to 15m)
- Power-over-coax support
- Higher bandwidth than FPD-Link III Gen2
- Wide adoption in autonomous driving (robotaxi platforms)

**Cons:**
- Maxim/ADI ecosystem (different vendor from rest of design)
- Higher component cost (~$7-8 for deserializer)
- Less mature automotive production ecosystem vs FPD-Link III
- Fewer automotive camera module partners use GMSL vs FPD-Link
- Limited FAE support outside major accounts
- Overkill bandwidth for 2MP@30fps application

**Cost Estimate (ECU side):** MAX9296A ($6.50) + passives/ESD ($1.50) = $8.00

### Option D: Ethernet-Based (LVDS over Ethernet)

**Architecture:**
```
Camera 1 [ISP + Ethernet PHY] --UTP/coax-- [Ethernet Switch] -- SOM Ethernet
Camera 2 [ISP + Ethernet PHY] --UTP/coax-- [Ethernet Switch] -- SOM Ethernet
```

**Pros:**
- Standard networking infrastructure
- Long cable runs (100m+ over UTP)
- Scalable to many cameras via switches
- Packetized data enables network diagnostics

**Cons:**
- High latency (frame packetization + depacketization)
- Complex camera modules (need ISP + encoder + Ethernet PHY)
- Expensive camera modules ($50+ each at low volume)
- SOM requires Ethernet CSI-2 bridge for vision pipeline
- Not suitable for real-time ADAS at 30fps requirement
- Immature for automotive vision (emerging, not production-proven)

**Cost Estimate (ECU side):** Ethernet switch ($8.00) + PHY ($3.00) + passives ($2.00) = $13.00

## 4. Trade Matrix

| Criterion | Weight | FPD-Link III | Direct MIPI | GMSL2 | Ethernet |
|-----------|--------|-------------|-------------|-------|----------|
| Cable Length | 20% | 10 | 2 | 10 | 10 |
| Cost (ECU) | 20% | 7 | 10 | 5 | 3 |
| EMI Robustness | 15% | 9 | 4 | 9 | 8 |
| Ecosystem/Support | 15% | 9 | 8 | 6 | 3 |
| PoC Capability | 10% | 10 | 0 | 10 | 5 |
| Latency | 5% | 8 | 10 | 8 | 4 |
| Scalability | 10% | 7 | 5 | 8 | 10 |
| Maturity | 5% | 9 | 10 | 7 | 3 |
| **Weighted Score** | **100%** | **8.55** | **5.60** | **7.55** | **5.55** |

## 5. Decision

### Track 2 (Modular IP Platform): FPD-Link III with DS90UB954-Q1

Selected for the IP platform due to:
- Best overall weighted score
- Long cable length essential for vehicle-mounted cameras
- PoC eliminates power harness complexity
- TI ecosystem alignment with rest of design
- Proven automotive production track record

### Track 1 (Production Cost-Down): Direct MIPI CSI-2

Defined as future cost-down option for applications where:
- Camera modules are co-located with ECU (integrated module)
- Cable length <30cm is acceptable
- Maximum BOM cost reduction is priority
- Direct MIPI saves ~$5 on ECU BOM + eliminates serializer cost at camera

## 6. Implementation Notes

### 6.1 DS90UB954-Q1 Key Configuration

| Setting | Value | Rationale |
|---------|-------|-----------|
| I2C Address | 0x30 | Default, non-conflicting |
| CSI-2 Lanes | 4 | Maximum bandwidth headroom |
| PoC Enable | Both ports | Power to remote serializers |
| Back-channel | I2C passthrough | Camera register access |
| Virtual Channels | VC0=Port0, VC1=Port1 | SOM can demux by VC |

### 6.2 Migration Path (Track 2 to Track 1)

For production cost-down, the carrier PCB can be designed with:
1. DS90UB954 footprint populated (Track 2 / FPD-Link variant)
2. DS90UB954 footprint DNI + direct MIPI connector populated (Track 1 / direct variant)
3. Both share same SOM CSI-2 port via board-level mux or alternate routing layer

This enables single carrier PCB design serving both tracks via BOM variant management (applicable to v0.4.4 SOM-based architecture where the carrier board is SoC-agnostic).

## 7. PoC (Power-over-Coax) Considerations

| Parameter | Specification |
|-----------|--------------|
| PoC Voltage | Typically 9-12V |
| PoC Current | Up to 200mA per port |
| Injection | Via bias-T at deserializer port |
| Extraction | At serializer (remote camera) |
| Protection | Current limiting + short-circuit protection built into UB954 |

PoC eliminates dedicated power wires in the vehicle harness, reducing:
- Connector pin count (1 coax per camera vs 1 coax + 2 power wires)
- Harness weight and cost
- Installation complexity

---

*ADVIS Hardware Platform - Technical Note*

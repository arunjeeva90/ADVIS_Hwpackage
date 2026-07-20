# Recommended Procurement Shortlist

## 1. Immediate purchases / RFQs

| Objective | Candidate | Why | Action |
|---|---|---|---|
| Best SoC-agnostic front PoC | Ainstein K-77 | Complete smart sensor, long range and dual CAN-FD | Ask for sample, DBC, logger, harness, firmware and automotive evidence |
| Best professional multi-role radar | smartmicro DRVEGRD 171/152 | CAN-FD + Automotive Ethernet; object and optional radar-cube paths | Request front and corner quotation plus ROS2/Autoware package |
| Mature benchmark | Verified Continental ARS408-21 or ARS548 RDI | Large research ecosystem and known object/point data | Buy only from traceable supplier with harness/ICD; do not freeze for new production |
| Cost-first front alternative | Nanoradar MR76 | Enclosed 170 m-class smart radar and China sourcing | RFQ 2/5/100/1k; require DBC and ADVIS test before recommendation |
| Cost-first corner alternative | Ainstein T-79 / Nanoradar SR73F or SR75 | Compact corner roles | Compare BSD/LCA/RCTA on identical fixture |
| Commercial vehicle regulation | CUB turn-assist / smartmicro side radar | Finished BSIS/turn-assist direction | Obtain ECE/AIS mapping, installation manual and object-data access |
| Custom low-cost radar learning | TI AWRL1432BOOST-BSD or AWR1843BOOST | Lowest barrier to radar algorithms and custom prototype | Purchase EVK; keep outside production smart-sensor decision |
| Higher-performance custom radar | TI AWR2944EVM / NXP SAF85xx / Infineon CTRX CARKIT | Automotive radar processing and richer arrays | Use only if ADVIS will own radar product IP and NRE |
| Cheapest warning demo | Verified dual 77 GHz aftermarket BSD kit | Quick HMI/vehicle packaging demonstration | Never represent as OEM-grade perception; ask for object interface |
| Cheapest radar interface learning | DFRobot C4001 | US$12.90–13.90 and simple UART/I2C | Bench only; no road-safety conclusions |

## 2. Recommended front-radar path

### PoC

```text
Ainstein K-77 or smartmicro DRVEGRD
        ↓ CAN-FD object list
ADVIS Radar HAL
        ↓
Forward-camera association
        ↓
TTC / cut-in / lead-object fusion
```

### Production RFQ set

Run parallel commercial/technical RFQs for:

1. Tier-1 current radar through OEM/Tier-1 channel
2. Ainstein or smartmicro independent smart radar
3. Nanoradar or validated China finished module
4. Calterah/TI/NXP/Infineon-based custom module from a radar design house

## 3. Recommended corner-radar path

Compare at least:

- Ainstein T-79
- smartmicro DRVEGRD corner model
- Nanoradar SR73F/SR75
- TI AWRL1432/AWR2944 custom reference
- one Tier-1 SRR benchmark
- one low-cost aftermarket kit for warning/HMI comparison only

## 4. ADVIS decision by product variant

| ADVIS variant | Radar recommendation |
|---|---|
| ADVIS Assist | No radar required; keep radar HAL and harness option |
| ADVIS Control | One front smart radar strongly recommended for ACC/AEB robustness |
| ADVIS Fusion Entry | Front CAN-FD smart radar + forward camera + DMS |
| ADVIS Fusion Safety | Front radar + two rear corners |
| ADVIS Fusion 360 | Front + four corners; Ethernet optional |
| ADVIS Fleet | Front radar plus side/turn-assist radar depending truck/bus regulation |
| ADVIS Ride / ARAS | Compact front radar optional; one or two rear corner radars for BSD/LCA |

## 5. What not to buy as the main ADVIS radar

- Bare 77 GHz transceiver without antenna/processor/SDK
- Used OEM radar without known DBC and wake/config sequence
- Retrofit BSD kit with only buzzer/LED outputs
- 24/60 GHz human-presence module for exterior FCW/BSD
- Obsolete Renesas radar platform
- Any radar whose supplier will not provide update rate, latency, object limit, timestamp, health and diagnostic behaviour

## 6. Final recommendation

The lowest-risk starting point is **not the cheapest radar**. It is the cheapest radar that provides:

- open object data
- deterministic timing
- known coordinate frame
- stable tracks
- health and interference status
- usable harness/logger
- supplier support

For ADVIS Fusion, the first engineering purchase should be one professional CAN-FD smart radar and one lower-cost challenger, tested side-by-side with the same camera and vehicle logs.

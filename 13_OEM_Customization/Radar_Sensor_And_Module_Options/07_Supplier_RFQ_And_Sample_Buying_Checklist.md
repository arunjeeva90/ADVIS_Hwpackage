# Supplier RFQ and Sample-Buying Checklist

## 1. Product identity and commercial status

| Area | Mandatory question / evidence |
|---|---|
| Identity | Exact product, hardware and firmware part number |
| Product type | Complete smart radar, reference design, EVK, chipset, retrofit warning kit or used OEM sensor |
| Lifecycle | SOP date, planned support period, PCN/EOL policy and current production status |
| Traceability | Serial number, manufacturing lot, firmware trace and country of origin |
| Sample | Lead time and price for 1, 2, 5 and 10 units |
| Production | Price/MOQ at 100, 1k, 10k, 50k and 100k units |
| NRE | Firmware, antenna, radome, connector, DBC, housing, tooling, calibration and certification NRE |
| Support | Named FAE, SDK access, issue response SLA and training |

## 2. RF and perception performance

Ask for performance by defined target RCS, probability of detection and false-alarm rate:

- Frequency band and occupied bandwidth
- Tx/Rx/virtual channel count
- Modulation and chirp profiles
- Minimum and maximum range
- Range resolution and accuracy
- Azimuth/elevation FoV, resolution and accuracy
- Radial velocity range, resolution and accuracy
- Update rate and end-to-end latency
- Maximum detections and tracked objects
- Stationary-object performance
- close-target recovery
- multi-path and guardrail handling
- rain, spray, wet-road and tunnel performance
- interference mitigation and status reporting
- blockage/contamination detection
- RCS/SNR output and covariance/quality

## 3. Data interface

Require sample frames and the full ICD before purchase:

- CAN 2.0 / CAN-FD bitrate
- DBC and scaling
- Ethernet PHY: 100BASE-T1 or 1000BASE-T1
- UDP/SOME-IP format
- object list, detections, point cloud or radar-cube access
- timestamp source and synchronization
- update rate
- packet loss/timeout behaviour
- configuration/service messages
- raw data licence or feature licence
- ROS/ROS2 driver availability
- Linux/Windows logging tool
- firmware update mechanism

## 4. Electrical and mechanical

- 9–16 V or 9–32 V input
- nominal/peak power
- reverse battery/load dump/cold crank claims
- connector, mating part and pinout
- harness availability
- dimensions, mass and CAD
- mounting tolerances
- radome/fascia material constraints
- paint/metallic-flake restrictions
- IP6K7/IP6K9K evidence
- operating/storage temperature
- vibration/shock
- EMC and ESD reports
- pressure vent and condensation strategy

## 5. Automotive quality and safety

Request:
- AEC-Q evidence for key ICs
- IATF 16949 manufacturing
- PPAP level and sample documentation
- DFMEA/PFMEA availability
- control plan and EOL test
- ISO 26262 work products or safety manual
- FMEDA assumptions and diagnostic mechanisms
- ASIL capability claim scope: IC, sensor hardware, firmware or complete function
- cybersecurity engineering, secure boot and update
- ISO 21434 evidence
- UDS diagnostics and DTC list
- E2E/CRC/counter support
- calibration and service process

## 6. Sample acceptance test

Do not accept a sample based only on a desktop GUI screenshot. Require:

1. Live object list over the intended interface.
2. Known-target range and velocity test.
3. Two targets at similar range but different azimuth.
4. motorcycle/bicycle/pedestrian observation.
5. stationary vehicle and metal roadside object.
6. cut-in/cut-out track continuity.
7. close-object and far-object simultaneous test.
8. interference test with another 77 GHz radar.
9. heating and supply-voltage variation.
10. at least one vehicle drive with raw log export.

## 7. Supplier message

> We need a complete SoC-agnostic automotive radar sensor for ADVIS. The preferred interface is CAN-FD object list, with optional 100BASE-T1 detections or point cloud. Please quote front long-range and corner variants. Provide exact model and firmware, range/FoV/resolution, object and detection limits, latency/update rate, full DBC/Ethernet ICD, timestamp and diagnostics, power/connector/harness, IP/temperature/EMC, automotive qualification and functional-safety evidence. Quote 2, 5, 100, 1k, 10k and 100k units, including NRE, SDK/data licences and customization lead time.

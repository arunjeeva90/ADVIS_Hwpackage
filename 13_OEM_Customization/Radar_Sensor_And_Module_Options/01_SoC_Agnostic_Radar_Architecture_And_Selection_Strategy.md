# SoC-Agnostic Radar Architecture and Selection Strategy

## 1. Architecture position

ADVIS shall not be locked to one radar semiconductor, sensor vendor, central SoC, middleware stack or vehicle network.

The radar shall be treated as a replaceable sensor ECU behind a normalized integration boundary:

```text
Radar transceiver + antenna + waveform
        ↓
Range/Doppler/angle processing
        ↓
CFAR / clustering / tracking / health monitoring
        ↓
Object list and/or point cloud
        ↓
CAN-FD / Automotive Ethernet transport
        ↓
ADVIS Radar HAL
        ↓
Time alignment + ego-motion compensation
        ↓
Camera-radar fusion
        ↓
FCW / ACC / AEB / BSD / LCA / RCTA / MOIS logic
```

## 2. Four radar integration classes

### Class A — Complete smart radar over CAN-FD

The radar internally performs signal processing and tracking and sends a compact object list.

**Best for:**
- Lowest integration effort
- SoC-independent ADVIS Fusion
- FCW, ACC, AEB confirmation
- BSD/LCA/RCTA/DOW
- Fleet and commercial-vehicle retrofit

**Mandatory outputs:**
- Timestamp/frame counter
- Object ID and age
- Range, azimuth and radial velocity
- Optional elevation
- Longitudinal/lateral position and velocity
- RCS/SNR
- Covariance or quality/confidence
- Sensor health, temperature and interference state

**Limitations:**
- Vendor tracking/filtering can hide raw information.
- CAN bandwidth limits point-cloud density.
- Some retrofit kits expose only warnings, not objects.

### Class B — Smart radar over Automotive Ethernet

The radar outputs a denser point cloud, detections, objects or radar cube through 100BASE-T1/1000BASE-T1.

**Best for:**
- Rich camera-radar fusion
- Dataset capture
- 4D radar and elevation
- Centralized/zonal architectures
- Future L2+/L3 work

**Limitations:**
- Higher ECU, switch, PHY and logging cost.
- Requires time synchronization, bandwidth management and cybersecurity.
- Vendor data formats can remain proprietary.

### Class C — USB/UART/Ethernet development radar

Professional or maker modules expose easy PC/Linux data but are not production automotive sensors.

**Best for:**
- Algorithm and GUI bring-up
- Radar HAL development
- Range/speed visualization
- Indoor/cabin/near-field experiments

**Limitations:**
- No automotive enclosure, EMC, safety or lifecycle.
- Usually low channel count and limited road-object performance.

### Class D — Raw ADC / range-FFT chipset or EVK

The host receives ADC samples or low-level detections and performs the radar pipeline.

**Best for:**
- Custom radar IP
- Waveform research
- Imaging-radar experiments
- Ultimate cost optimization at high volume

**Limitations:**
- Highest RF, antenna, DSP, calibration and safety NRE.
- Strong coupling to the chosen radar SoC and SDK.
- Not a universal plug-and-play product.

## 3. Recommended universal ADVIS radar product boundary

For the first product, freeze the following external contract rather than a specific radar vendor:

| Area | Universal requirement |
|---|---|
| Power | 9–16 V passenger vehicle; optional 9–32 V commercial variant; protected against reverse battery and transients |
| Primary data | CAN-FD object list at deterministic cycle time |
| Optional rich data | 100BASE-T1 point cloud/detection stream |
| Diagnostics | UDS or documented service protocol; DTCs, live data, reset and software identification |
| Time | Sensor timestamp plus host synchronization; PTP/gPTP for Ethernet variant where supported |
| Configuration | Mounting pose, region, range mode, FoV mode, object filtering and output-rate configuration |
| Health | Temperature, supply state, blocked/radome state, interference/jamming state, internal memory/processor status |
| Calibration | Factory antenna calibration and vehicle mounting/yaw alignment status |
| Safety communication | Alive counter, CRC/E2E protection and timeout behaviour |
| Mechanical | IP6K7/IP6K9K target by application; radome compatibility; vibration-stable bracket |
| Cybersecurity | Secure boot/update, authenticated diagnostics and controlled firmware access for production |
| Lifecycle | PCN/EOL policy, traceability, serial number and firmware version management |

## 4. Normalized ADVIS Radar HAL

Suggested software-independent contract:

```text
RadarFrame
├── sensor_id
├── timestamp_ns
├── frame_counter
├── mounting_pose_version
├── firmware_version
├── operating_mode
├── health_state
├── temperature_c
├── interference_state
├── blockage_state
├── detections[]
└── objects[]

RadarDetection
├── range_m
├── azimuth_rad
├── elevation_rad_optional
├── radial_velocity_mps
├── rcs_dbsm
├── snr_db
├── range_variance
├── angle_variance
└── detection_flags

RadarObject
├── object_id
├── age
├── x_m / y_m / z_m
├── vx_mps / vy_mps / vz_mps
├── ax_mps2 / ay_mps2_optional
├── covariance
├── existence_probability
├── motion_state
├── class_optional
└── source_flags
```

The fusion stack must not depend on vendor-specific object numbers, coordinate frames or invalid-value encodings.

## 5. Sensor-selection gates

1. The radar must publish an **open and testable object/detection ICD**.
2. Range and FoV claims must be reproduced using defined target RCS, mounting height and weather.
3. Minimum range and close-target recovery must match the intended feature.
4. Longitudinal and lateral velocity accuracy must support TTC and crossing-traffic logic.
5. Track latency, update rate and data age must fit the ADVIS safety timing budget.
6. Multipath, guardrail, bridge, tunnel, rain, standing-water and dense-traffic false targets must be measured.
7. Mutual radar interference and jamming detection must be tested.
8. Mounting behind fascia/radome must be validated for material, paint, thickness, angle and contamination.
9. Object-list stability and ID continuity must be measured during cut-in, overtaking and partial occlusion.
10. Automotive qualification of the IC does not automatically qualify the complete sensor.
11. Safety manual, FMEDA assumptions, diagnostic coverage and communication protection must be available for production candidates.
12. A second source or alternative mounting/interface path should be identified before design freeze.

## 6. Development sequence

### Stage 1 — Radar HAL and fusion bring-up

Use one readily available smart radar or development sensor. Implement:
- CAN/Ethernet decoder
- Coordinate normalization
- Time synchronization
- ego-motion compensation
- visualization and logging
- camera-radar association

### Stage 2 — Front fusion PoC

Install one front smart radar and forward camera. Validate:
- lead vehicle
- cut-in/cut-out
- stationary target
- TTC
- rain/night/glare robustness
- sensor disagreement and fallback

### Stage 3 — Corner functions

Add two rear corner radars. Validate:
- motorcycle approach
- BSD zone occupancy
- lane-change time-to-collision
- RCTA
- DOW
- guardrail and adjacent-lane false alarms

### Stage 4 — Production RFQ

Run identical test cases across:
- Tier-1 benchmark sensor
- independent smart radar
- cost-down China radar
- custom chipset reference design where justified

### Stage 5 — Freeze by measured score

Selection must use an ADVIS-owned scorecard:
- performance 30%
- safety/quality/lifecycle 25%
- interface/software openness 15%
- complete recurring cost 15%
- development/NRE/support 10%
- packaging/power 5%

## 7. Platform policy

- The central ADVIS SoC may change without changing the radar product when CAN-FD/Ethernet and the HAL contract remain stable.
- Vendor-specific radar DSP software stays inside the radar ECU or a replaceable adapter package.
- Raw radar data shall never be put on the safety-critical path until its processing stack has a defined safety concept.
- Warning-only retrofit kits are not acceptable as production perception sensors unless an open object interface and diagnostic concept are provided.
- 77–81 GHz is the preferred exterior automotive band for new ADVIS designs.
- 24/60 GHz maker modules remain research tools or cabin/near-field sensors, not front/corner ADAS substitutes.

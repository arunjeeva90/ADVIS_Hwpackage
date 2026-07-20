# ADVIS Workload and Feature Scaling Matrix

## Feature-fit matrix

| ADVIS_Use_Case | Sensor_Load | Estimated_Compute_Envelope | Candidate_Platforms | Feature_Scope | Engineering_Note |
|---|---|---|---|---|---|
| DMS-only entry | 1 NIR camera, 720p/1MP, 20–30fps | 0.5–1.5 effective TOPS plus ISP | AM62A7-Q1; APACHE5; Hailo-15; KL730; RK3588 prototype | Face/head/eye/gaze, drowsiness, distraction | Automotive path needs safety monitor and NIR control |
| Forward warning ADAS | 1 HDR forward camera, 2–3MP, 25–30fps | 1.5–4 effective TOPS plus ISP/CV | TDA4VL; TDA4VEN; R-Car V3H; CV22FS; APACHE5 with compact models | FCW, LDW, TSR, PCW, lane/road, TTC | 4 TOPS assumes shared backbone, INT8, ROI depth and bounded logging |
| Integrated Forward Vision + DMS | 2 cameras, 2.5MP + 1MP | 3–8 effective TOPS | TDA4VL after benchmark; TDA4AL/VE/VM; R-Car V3H/V4M; CV2FS; Hailo-8+host | ADVIS Assist full dual-camera workload | Primary ADVIS selection case |
| Forward radar fusion | 2 cameras + CAN-FD radar objects | 4–8 TOPS | TDA4AL/VE/VM; R-Car V3H/V4M; Ambarella CV3; NXP i.MX95+Hailo | Radar association, TTC robustness, cut-in tracking | CAN object fusion adds modest AI but significant timing/safety work |
| Rear-corner radar functions | Dual camera + 2 corner radars | 4–10 TOPS | TDA4AL/VM; R-Car V4M; Qualcomm/Horizon entry | BSD/LCA/RCTA/DOW fusion and HMI | Radar may remain smart and output object lists |
| 4-camera surround + DMS | 5 cameras total | 8–24 TOPS plus high ISP bandwidth | TDA4VM/AP; R-Car V4M/V4H; Ambarella CV3; Horizon Journey 6; Qualcomm Ride | Surround view, parking, side VRU, DMS | Memory bandwidth and camera deserialization matter more than headline TOPS |
| 8-camera surround + radar | 8+ cameras, 4–5 radars | 24–150+ TOPS | TDA4AP/VH; R-Car V4H; Horizon Journey 5/6; Ride; DRIVE Orin | L2+ highway/urban, occupancy/free-space, fusion | Domain controller, active cooling and Ethernet required |
| Research foundation models | Multi-camera logs and large networks | 60–250+ TOPS | Jetson Orin NX/AGX Orin; DRIVE Orin; high-end Journey/Ride | Teacher models, transformers, BEV and end-to-end research | Not production-cost baseline; distill to target SoC |

## Baseline dual-camera workload

### Forward pipeline

- HDR/PWL ISP and lens correction
- object detection and ground contact
- lane/road segmentation
- scene quality
- object-centric depth/TTC
- tracking and cut-in logic
- calibration monitoring

### DMS pipeline

- face/head detection
- eye state and landmarks
- gaze/head pose
- phone/seatbelt/hand features
- temporal drowsiness/distraction state
- DMS quality and blockage
- NIR control

### Shared platform services

- CAN-FD and diagnostics
- logging and event recorder
- thermal/power policy
- watchdog and safety monitor
- OTA and secure boot
- GNSS/IMU optional

## Compute-sizing rule

Headline TOPS is only a first filter.

Use:

```text
usable accelerator throughput
× supported-operator ratio
× sustained thermal duty
× memory-efficiency factor
× safety reserve
```

A nominal 4-TOPS device may be sufficient with a shared backbone, task staggering and object-centric depth. An 8-TOPS device can still fail if unsupported layers fall back to CPU or camera/DDR bandwidth is inadequate.

## Recommended reserve

At production freeze:

- average compute utilization ≤70%
- p95 accelerator utilization ≤85%
- no mandatory safety cycle skipped under logging
- thermal throttling does not violate feature latency
- 20–30% memory headroom
- defined reduced-capability mode for overtemperature and camera degradation

## Phase mapping

| Product | Minimum credible compute class |
|---|---|
| ADVIS DMS / Fleet Entry | 1–2 TOPS automotive + ISP |
| ADVIS Assist warning | 3–4 TOPS effective |
| ADVIS Assist dual camera | 4 TOPS stretch; 6–8 TOPS preferred |
| ADVIS Control + radar objects | 6–10 TOPS plus safety headroom |
| ADVIS Fusion 4-camera | 12–24 TOPS and high ISP/DDR |
| ADVIS Surround/L2+ | 24–100+ TOPS depending model architecture |

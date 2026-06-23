# Patent Claim Draft: ID-003

## Disclosure Reference

| Field | Value |
|-------|-------|
| **Disclosure ID** | ID-003 |
| **Title** | Risk-Coupled ADAS+DMS Decision Fusion |
| **Version** | Draft 1.0 |
| **Date** | January 2025 |
| **Status** | DRAFT - For Attorney Review |

---

## Independent Claims

### Claim 1 (Method)

A method of generating safety-supervised actuation requests in an automotive vision system, comprising:

(a) receiving, from a forward-facing image sensor mounted in a vehicle, image data representative of a scene external to the vehicle;

(b) processing said external scene image data to compute a scene risk score, said scene risk score representing a continuous measure of external driving risk on a normalized scale;

(c) receiving, from a cabin-facing image sensor mounted in said vehicle, image data representative of a vehicle occupant;

(d) processing said occupant image data to compute a driver attention score, said driver attention score representing a continuous measure of driver engagement on a normalized scale;

(e) computing a coupled risk metric by applying a risk coupling function to said scene risk score and said driver attention score, wherein said risk coupling function produces a coupled risk metric that increases when both said scene risk score increases and said driver attention score decreases;

(f) modulating at least one intervention threshold of an advanced driver assistance feature based on said coupled risk metric, such that said intervention threshold decreases as said coupled risk metric increases; and

(g) generating an actuation request and transmitting said actuation request to a vehicle electronic control unit via a vehicle communication bus when a condition determined by said modulated intervention threshold is satisfied;

wherein said vehicle electronic control unit retains final authority over vehicle actuation and said actuation request is a safety-supervised request that does not directly control vehicle brakes, steering, or throttle.

### Claim 2 (System)

A dual-camera automotive safety system, comprising:

a forward-facing image sensor configured to capture road scene imagery from a position within a vehicle;

a cabin-facing image sensor configured to capture occupant imagery from a position within said vehicle;

a processing unit communicatively coupled to said forward-facing image sensor and said cabin-facing image sensor, said processing unit configured to execute:

(i) a scene risk assessment module that receives image data from said forward-facing image sensor and outputs a continuous scene risk score;

(ii) a driver attention assessment module that receives image data from said cabin-facing image sensor and outputs a continuous driver attention score;

(iii) a risk coupling module that receives said scene risk score and said driver attention score and computes a coupled risk metric using a coupling function, wherein said coupled risk metric is greater when said scene risk score is higher and said driver attention score is lower; and

(iv) a request generator module that produces graded actuation requests based on said coupled risk metric and transmits said requests to a vehicle electronic control unit;

wherein said graded actuation requests include an urgency parameter that scales proportionally with said coupled risk metric; and

wherein said vehicle electronic control unit retains final authority to execute, modify, or reject said actuation requests.

### Claim 3 (Computer-Readable Medium)

A non-transitory computer-readable medium storing instructions that, when executed by a processor in a vehicle-mounted camera module, cause said processor to:

(a) compute a scene risk score from image data received from a forward-facing camera, said scene risk score representing a continuous measure of external driving risk;

(b) compute a driver attention score from image data received from a cabin-facing camera, said driver attention score representing a continuous measure of driver engagement;

(c) determine a coupled risk value by applying a coupling function to said scene risk score and said driver attention score, said coupling function being configured such that said coupled risk value increases multiplicatively when scene risk increases and driver attention decreases simultaneously;

(d) adjust at least one intervention threshold for an advanced driver assistance feature based on said coupled risk value, said adjusting comprising lowering said threshold as said coupled risk value increases; and

(e) transmit graded actuation requests to a separate vehicle electronic control unit over a vehicle communication bus when said adjusted intervention threshold is exceeded, said separate vehicle electronic control unit maintaining final actuation authority.

---

## Dependent Claims

### Claims Dependent on Claim 1 (Method)

**Claim 4.** The method of claim 1, wherein said risk coupling function is multiplicative such that the coupled risk metric is computed as a product of the scene risk score and a decreasing function of the driver attention score.

**Claim 5.** The method of claim 4, wherein said decreasing function of the driver attention score is a complement function raised to a configurable exponent, such that the coupled risk metric equals zero when the driver attention score is at maximum regardless of scene risk score.

**Claim 6.** The method of claim 1, wherein said processing of external scene image data to compute said scene risk score comprises evaluating at least two of: time-to-collision with a detected object, proximity to a lane boundary, and density of objects in a forward path.

**Claim 7.** The method of claim 1, wherein said processing of occupant image data to compute said driver attention score comprises evaluating at least two of: gaze direction relative to the forward road, eye closure state, and head pose orientation.

**Claim 8.** The method of claim 1, wherein said actuation request includes a plurality of parameters comprising: a feature identifier indicating which ADAS function triggered the request, an urgency level on a discrete scale, a requested action type, and a confidence score indicating reliability of underlying perception data.

**Claim 9.** The method of claim 1, further comprising adapting at least one parameter of said risk coupling function based on a vehicle speed, such that coupling sensitivity increases at higher vehicle speeds.

**Claim 10.** The method of claim 1, wherein said forward-facing image sensor and said cabin-facing image sensor are both coupled to a single system-on-chip processor that executes both said scene risk score computation and said driver attention score computation with shared memory access.

**Claim 11.** The method of claim 1, further comprising generating a plurality of graded actuation requests with escalating urgency levels as said coupled risk metric increases over time, comprising at least: a visual advisory, an audible warning, and an urgent actuation request.

---

### Claims Dependent on Claim 2 (System)

**Claim 12.** The system of claim 2, wherein said processing unit is a single system-on-chip that processes both forward-facing image data and cabin-facing image data, enabling zero-latency data sharing between said scene risk assessment module and said driver attention assessment module.

**Claim 13.** The system of claim 2, further comprising a safety watchdog circuit configured to monitor health of said processing unit and to disable actuation request generation if said processing unit is determined to be malfunctioning.

**Claim 14.** The system of claim 2, wherein said vehicle communication bus is a CAN-FD bus and said actuation requests are transmitted as defined message frames including at least an urgency field and a confidence field.

**Claim 15.** The system of claim 2, further comprising an inertial measurement unit providing vehicle dynamics data to said scene risk assessment module for incorporation into said scene risk score computation.

**Claim 16.** The system of claim 2, wherein said forward-facing image sensor and said cabin-facing image sensor are mounted within a single compact housing attached to an interior surface of a vehicle windshield.

---

### Claims Dependent on Claim 3 (Computer-Readable Medium)

**Claim 17.** The non-transitory computer-readable medium of claim 3, wherein said coupling function is configured such that when the driver attention score indicates full driver engagement, the coupled risk value is zero regardless of the scene risk score.

**Claim 18.** The non-transitory computer-readable medium of claim 3, wherein said instructions further cause the processor to compute said scene risk score and said driver attention score at a rate of at least 10 times per second, providing continuous coupled risk assessment.

**Claim 19.** The non-transitory computer-readable medium of claim 3, wherein said instructions further cause the processor to log said coupled risk value, said scene risk score, and said driver attention score for post-drive analysis.

**Claim 20.** The non-transitory computer-readable medium of claim 3, wherein said instructions further cause the processor to modulate a visual indicator visible to the driver based on said coupled risk value, said visual indicator intensity increasing proportionally with said coupled risk value.

---

## Claim Dependency Map

```
Claim 1 (Method - Independent)
  |-- Claim 4 (multiplicative coupling)
  |     |-- Claim 5 (complement function with exponent)
  |-- Claim 6 (scene risk inputs: TTC, lane, density)
  |-- Claim 7 (attention inputs: gaze, eyes, head)
  |-- Claim 8 (request parameters)
  |-- Claim 9 (speed-adaptive coupling)
  |-- Claim 10 (single SoC processing)
  |-- Claim 11 (escalating urgency levels)

Claim 2 (System - Independent)
  |-- Claim 12 (single SoC, zero latency)
  |-- Claim 13 (safety watchdog)
  |-- Claim 14 (CAN-FD implementation)
  |-- Claim 15 (IMU integration)
  |-- Claim 16 (single windshield housing)

Claim 3 (Medium - Independent)
  |-- Claim 17 (full attention = zero coupled risk)
  |-- Claim 18 (10Hz+ computation rate)
  |-- Claim 19 (data logging)
  |-- Claim 20 (visual indicator modulation)
```

---

## Claim Notes for Attorney

### Novelty Basis

The primary novelty lies in:
1. **Continuous coupling** (not binary) of driver attention and scene risk
2. **Multiplicative relationship** capturing exponential danger of combined inattention + high risk
3. **Dynamic threshold modulation** driven by the coupled metric
4. **Graded request generation** (proportional, not binary)
5. **Safety boundary** maintained throughout (requests only)

### Anticipated Rejections

- **Obviousness (103)**: Examiner may combine DMS patent + ADAS patent + general control theory. Response: the specific multiplicative coupling and continuous modulation are non-obvious combinations.
- **Indefiniteness (112)**: "continuous measure" and "normalized scale" should be supported by specification examples.
- **Prior art**: Seeing Machines gaze patents + Mobileye FCW patents. Our distinction: coupling function and dynamic threshold modulation.

### Critical Safety Boundary Language

Every claim involving vehicle response MUST include: "vehicle electronic control unit retains final authority" or equivalent. This prevents product liability exposure and maintains regulatory compliance.

### Trade Secret Boundary

NO claim may include:
- Specific values of the coupling exponent (alpha)
- Specific threshold values for intervention
- Training data descriptions
- Model architecture details beyond functional description

---

**Document Version:** 1.0  
**Last Updated:** 2025-01  
**Classification:** CONFIDENTIAL - Attorney-Client Privilege

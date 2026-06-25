# ADVIS v0.5 Compact Module - Mechanical and Optical Envelope

**Classification:** Confidential - Engineering Use Only  
**Status:** Concept Definition  
**Date:** July 2026

---

## 1. Product Form

The ADVIS v0.5 is a compact windshield-mounted dual-facing camera module designed for high-volume OEM passenger vehicle deployment. It mounts behind the rearview mirror or in the upper windshield region. The module integrates both a forward road-facing perception camera and a cabin-facing DMS camera into a single compact housing.

---

## 2. Optical Architecture

### 2.1 Forward Camera Optical Path

| Parameter | Specification |
|-----------|--------------|
| Direction | Outward through windshield toward road scene |
| Field of view | Determined by lens selection (typically 100-120 deg H for ADAS) |
| Optical window | Flat or molded plastic window, AR-coated |
| Mounting angle | Aligned to vehicle forward axis (adjustable during calibration) |
| Windshield interface | Clear optical path through windshield glass; bonding pad or bracket ensures alignment |
| Environmental | Protected from rain/debris by windshield; solar load managed by IR-cut filter in lens stack |

### 2.2 DMS Camera Optical Path

| Parameter | Specification |
|-----------|--------------|
| Direction | Inward toward driver/cabin |
| Field of view | Determined by lens selection (typically 70-90 deg for driver face coverage) |
| Offset | DMS camera may be offset from main PCB by approximately 5 cm using flex/rigid-flex |
| Optical window | IR-pass filter window (blocks visible, passes NIR for eye-safe illumination) |
| Mounting angle | Aimed toward driver eye/face region |
| Environmental | Protected from cabin dust by sealed window; no rain/splash exposure |

### 2.3 Optical Baffle

An optical baffle is required between the forward and DMS optical paths to prevent:

- **IR leakage:** DMS NIR illumination must not reach the forward camera sensor or reflect off the windshield back into the forward camera
- **NIR reflection control:** Windshield glass partially reflects NIR from DMS LEDs; baffle blocks internal reflection paths
- **Stray light:** Prevents ambient light cross-talk between forward and cabin optical channels
- **Ghost images:** Prevents internal reflections within the housing from creating artifacts

Baffle material: opaque black plastic or sheet metal with matte finish (low reflectance at 850 nm and 940 nm).

### 2.4 IR LED / IR Window Placement

| Parameter | Specification |
|-----------|--------------|
| IR LED position | Adjacent to or surrounding DMS camera lens |
| IR wavelength | 940 nm preferred (invisible to human eye) or 850 nm (faint red glow, higher efficiency) |
| IR window | Bandpass filter window over LED array (passes NIR, blocks visible) |
| Eye safety | IEC 62471 compliance required; power budget limited by eye-safe exposure limits |
| Beam pattern | Wide flood pattern to cover driver face region |
| Thermal | IR LEDs generate heat; thermal path to housing or spreader required |

---

## 3. Thermal Management

### 3.1 Thermal Spreader

| Parameter | Specification |
|-----------|--------------|
| Location | Behind SoC area on PCB rear side |
| Material | Aluminum plate (primary) or copper spreader (high-performance variant) |
| Attachment | Thermal interface material (TIM) between SoC package top and spreader |
| Function | Spreads SoC heat across larger surface area for convective/radiative dissipation |
| Area | Minimum 30x30 mm coverage over SoC die area |

### 3.2 Thermal Challenges

- Windshield-mount location receives direct solar radiation through glass
- Enclosed housing limits airflow (natural convection only)
- SoC power dissipation (2-6W typical depending on AI workload)
- IR LED power dissipation (0.5-2W during active illumination)
- Camera sensor self-heating (minor contribution)

### 3.3 Thermal Design Approach

- Aluminum rear plate of housing doubles as heat sink and structural element
- TIM path from SoC to aluminum rear plate
- Housing ventilation slots or permeable regions for convective flow (if appearance-compatible)
- Solar load on windshield side managed by:
  - IR-reflective coating on forward-facing surfaces
  - Light-colored forward housing surface
  - Thermal isolation between windshield-facing surface and PCB
- SoC thermal throttling as last-resort protection

---

## 4. Housing Concept

### 4.1 Construction

| Element | Material | Function |
|---------|----------|----------|
| Rear plate | Die-cast or stamped aluminum | Structural + thermal spreader |
| Front shell | Injection-molded black plastic (PC/ABS, UL94 V-0) | Optical windows, appearance |
| Forward optical window | Optical-grade polycarbonate or glass, AR-coated | Forward camera aperture |
| DMS optical window | IR-pass filter glass/plastic | DMS camera + IR LED aperture |
| Internal baffle | Opaque molded plastic or sheet metal | Optical isolation |
| Windshield bracket | Aluminum or reinforced plastic | Vehicle mounting interface |
| Service cover | Snap-fit plastic panel on rear | Production test / calibration access |

### 4.2 Appearance and OEM Grade

- Sleek, compact form factor suitable for passenger car interior
- Matte black or dark gray finish typical for rearview mirror area
- No visible screws from driver perspective
- LED indicators (if any) recessed and diffused
- Brand/model marking area on top or side surface
- OEM-customizable housing color and finish

### 4.3 Overall Dimensions (Target)

| Dimension | Target | Maximum |
|-----------|--------|---------|
| Width | 80 mm | 100 mm |
| Height | 35 mm | 45 mm |
| Depth (from windshield) | 30 mm | 40 mm |
| Weight (without bracket) | 120 g | 180 g |

*Note: Final dimensions depend on SoC selection, thermal solution, and lens stack height.*

---

## 5. Windshield Bracket Concept

### 5.1 Mounting Interface

| Parameter | Specification |
|-----------|--------------|
| Primary attachment | Adhesive pad bonded to windshield glass (3M VHB class) |
| Secondary retention | Mechanical clip or slide-lock to bracket |
| Adjustment | Limited tilt adjustment for camera alignment during installation |
| Service removal | Module detachable from bracket without removing adhesive from windshield |
| Bracket material | Aluminum or glass-filled nylon |

### 5.2 Alignment

- Bracket provides coarse alignment to vehicle coordinate frame
- Fine alignment performed in software via calibration procedure
- Bracket design accounts for windshield rake angle variation across vehicle models
- OEM-specific bracket variants may be required for different windshield geometries

---

## 6. DMS Camera Offset

### 6.1 Flex/Rigid-Flex Connection

When the DMS camera is offset from the main PCB (approx. 5 cm):

| Parameter | Specification |
|-----------|--------------|
| Connection type | Flex cable or rigid-flex extension |
| Length | Approximately 50 mm (adjustable per housing geometry) |
| Signals carried | MIPI CSI-2 data lanes, I2C (SCL/SDA), reset, clock, power rails |
| Impedance | Controlled differential impedance for MIPI lanes (85-100 ohm) |
| Connector | Board-to-flex connector (ZIF type) or soldered rigid-flex |
| Shielding | Ground plane in flex stackup for EMI control |

### 6.2 DMS Pod

- The DMS camera + IR LED assembly may form a small "pod" that extends from the main housing
- Pod orientation is angled toward driver face
- Pod is mechanically supported by housing structure and flex cable
- Pod design is a candidate for design patent protection (distinctive appearance)

---

## 7. Service Cover and Production Test Access

| Feature | Description |
|---------|-------------|
| Service cover location | Rear or bottom of housing |
| Access method | Snap-fit or single-screw panel |
| Exposes | Test pads for UART, JTAG, power measurement, variant ID |
| Production use | EOL calibration fixture alignment, functional test pogo-pin access |
| Field use | Firmware reflash via UART, diagnostic readout |
| Sealing | IP rating maintained when cover is closed (gasket or labyrinth seal) |

---

## 8. Design Patent Hooks

The following visual/ornamental elements of the ADVIS v0.5 compact module are candidates for design patent filings:

| Element | Description |
|---------|-------------|
| Overall housing shape | Compact dual-window camera module form factor |
| DMS pod geometry | Distinctive offset pod or integrated angled DMS window |
| IR window styling | Integrated IR filter window appearance around DMS lens |
| Mounting bracket | Distinctive windshield bracket clip/slide mechanism |
| Service cover | Concealed access panel integrated into housing lines |
| Optical baffle visible styling | External indicator of dual-camera nature |
| Forward window bezel | Shaped surround for forward camera aperture |

---

## 9. Environmental and Reliability Considerations

| Parameter | Requirement | Standard |
|-----------|-------------|----------|
| Operating temperature | -40 C to +85 C | ISO 16750-4 |
| Storage temperature | -40 C to +105 C | ISO 16750-4 |
| Humidity | 85% RH, 85 C, 1000h | ISO 16750-4 |
| Vibration | Random and sinusoidal per vehicle mounting point | ISO 16750-3 |
| Solar radiation | Windshield-mount solar load (up to 1000 W/m2 through glass) | Custom test |
| Thermal shock | -40 C to +85 C cycling, 1000 cycles | ISO 16750-4 |
| Dust/water ingress | IP54 minimum (sealed housing) | IEC 60529 |
| Mechanical shock | 50g, 6ms half-sine | ISO 16750-3 |

---

## 10. Open Items

| # | Item | Owner | Status |
|---|------|-------|--------|
| 1 | SoC die size and package selection (determines thermal area) | Systems | Open |
| 2 | Lens stack height for forward and DMS cameras | Optics | Open |
| 3 | Bracket variants for target vehicle windshield angles | Mechanical | Open |
| 4 | IR LED array layout and thermal path | Electrical/Thermal | Open |
| 5 | Optical baffle geometry and material | Optics/Mechanical | Open |
| 6 | DMS flex length finalization | Mechanical | Open |
| 7 | Housing tooling cost estimate | Manufacturing | Open |
| 8 | Windshield adhesive qualification | Materials | Open |
| 9 | IP rating test plan | Validation | Open |
| 10 | Design patent drawings preparation | IP/Legal | Open |

---

*End of Document*

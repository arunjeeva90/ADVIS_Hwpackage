# Interface, Illumination and Compute Compatibility

## Transport options

| Transport | Advantages | Limitations | Compute compatibility | Recommended use |
| --- | --- | --- | --- | --- |
| Native MIPI CSI-2 | Lowest recurring BOM; direct RAW access | Sensor-specific driver, ISP tuning and board pinout required | Any SoC with supported CSI receiver and ISP: TI, Rockchip, NXP, Qualcomm, Renesas, Ambarella, Horizon, NVIDIA, MediaTek | Best for custom production module after software support is proven |
| FPD-Link III | Automotive coax, power-over-coax, long cable, TI ecosystem | Serializer/deserializer and PoC cost; sensor config and virtual channels | Any SoC behind compatible DS90UB95x/96x deserializer outputting MIPI | Good for distributed camera and ECU architecture |
| GMSL2/GMSL3 | Broad professional automotive camera-module ecosystem | Higher sample price and Maxim/ADI SerDes integration | Any SoC accepting deserializer MIPI output | Good for professional prototypes and OEM designs |
| USB 2/3 UVC | Most SoC-agnostic and driver-free under Linux; rapid PoC | May hide RAW, ISP and precise trigger; USB is not production automotive transport | Any Linux/Android/Windows compute with USB host | Recommended first OV9281/AR0234 prototype path |
| DVP / parallel | Simple for low-end MCU/ISP and legacy sensors | Many pins, limited bandwidth, uncommon on modern AI SoCs | Low-cost SoCs/MCUs with camera parallel port or bridge | Use only for extreme cost or legacy module |
| Automotive Ethernet camera | Long cable, networkable and central compute friendly | Camera ISP/encoder, latency, time sync and cost; less available for cheap sensors | Any SoC with Ethernet and video stack | Future centralized architecture, not cheapest PoC |

## NIR illumination strategy

### 850 nm

- Higher effective sensitivity on many low-cost sensors.
- Easier and cheaper for first PoC.
- May show a faint red glow and is less visually discreet.

### 940 nm

- Preferred for production DMS because it is less visible to occupants.
- Requires a sensor with strong 940 nm QE and careful optical-power design.
- Illumination current, pulse timing, thermal behavior and eye safety must be validated.

### Filter choices

- **No IR-cut:** cheapest and flexible for laboratory tests, but visible and NIR content mix.
- **850/940 nm band-pass:** improves eye/face contrast and sunlight rejection for mono DMS.
- **RGB-IR CFA:** enables aligned visible cabin context and NIR driver monitoring, but needs ISP/CFA support.

## Lens guidance

| Scope | Typical HFOV | Focus guidance |
|---|---:|---|
| Focused driver-only DMS | 50–75° | Optimize 50–90 cm, both eyes resolved across head box |
| Driver + front passenger | 75–100° | Optimize 50 cm–1.5 m |
| Whole-cabin OMS | 100–140° | Multi-row coverage; distortion and corner resolution become critical |

For the first ADVIS prototype, avoid extreme 140–160° fisheye lenses unless whole-cabin OMS is explicitly required. A cheap sensor with a correct lens can outperform a premium sensor with the wrong FOV.

## Compute portability

The normalized camera HAL should expose the same image geometry and metadata whether the back end is TI, Rockchip, NXP, Qualcomm, Renesas, Ambarella, Horizon, NVIDIA, MediaTek or another SoC. Sensor-specific register scripts and ISP tuning remain separate packages.

## Eye-safety boundary

IR illumination must default off until the camera is initialized and supervision is active. Production use requires an IEC 62471 assessment covering wavelength, radiant intensity, pulse width, duty cycle, viewing distance, fault behavior and thermal derating.

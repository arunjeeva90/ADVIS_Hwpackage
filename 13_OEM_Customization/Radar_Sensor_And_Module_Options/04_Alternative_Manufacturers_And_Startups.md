# Alternative Manufacturers and Startups

The radar market should not be reduced to Continental, Bosch and TI. ADVIS should maintain separate RFQs for:

- Current global Tier-1 production radars
- Independent smart-radar specialists
- Imaging-radar startups
- China/Taiwan cost-down suppliers
- Radar semiconductor/reference-design suppliers
- Open development-module vendors

## Manufacturer map

| Manufacturer | Position | Relevant_Families | Strengths | Risks | ADVIS_Role | Official_Link |
|---|---|---|---|---|---|---|
| Bosch | Global Tier-1 | New front radar; heavy-CV radar | Series automotive maturity, in-house SoC, strong safety and OEM support | Restricted access, OEM volume and high programme cost | Benchmark / strategic OEM RFQ | https://www.bosch-mobility.com/en/solutions/sensors/radar-sensor/ |
| Continental | Global Tier-1 | ARS540, ARS548 RDI, ARS408 legacy | Strong 4D portfolio; professional reference products available | New production parts remain OEM-access; ARS408 grey market risk | Benchmark / high-performance RFQ | https://www.continental-automotive.com/en/components/radars/ |
| Aptiv | Global Tier-1 | SRR7, SRR7+, FLR7 | Compact common Gen-7 family; 4D front/corner; scalable Ethernet/CAN-FD | OEM nomination required | Benchmark / strategic RFQ | https://www.aptiv.com/en/solutions/intelligent-perception/radars/gen-7-radar-family |
| ZF | Global Tier-1 | 4D Imaging Radar | 192-channel 350 m production imaging radar | Premium and closed programme | Premium benchmark | https://press.zf.com/press/en/releases/release_48960.html |
| Magna | Global Tier-1 | ICON Digital Radar; Radar Belt; corner/front portfolio | Broad production radar portfolio and high-end digital imaging | Limited open specs and sample access | OEM RFQ only | https://www.magna.com/products/electrical-electronics/adas-automated-driving/complete-radar-portfolio |
| Valeo | Global Tier-1 | High Definition Radar; corner radar suite | Large-scale automotive industrialization and Mobileye imaging-radar partnership | Closed programme and limited open technical data | OEM RFQ only | https://www.valeo.com/en/catalogue/cda/high-definition-radar-sensor/ |
| smartmicro | Independent radar specialist | DRVEGRD 152/166/169/171; UMRR families | CAN-FD/Ethernet, object and radar-cube options, ROS/Autoware, low-volume access | Professional pricing; exact automotive safety package by agreement | Highest-priority plug-and-play professional candidate | https://www.smartmicro.com/automotive-radar-sensors/ |
| Ainstein | Independent radar specialist | K-77, T-79, I-79, O-79 | Accessible smart modules, CAN-FD, rugged industrial/vehicle options | Qualification/PPAP and current lifecycle must be confirmed | Highest-priority SoC-agnostic PoC RFQ | https://ainstein.ai/ |
| Uhnder | Digital radar startup | S80/S81 digital radar | Excellent interference and contrast resolution; digital code modulation | Design-in access and pricing; ecosystem less open than TI | Premium alternative/startup RFQ | https://www.uhnder.com/ |
| Arbe Robotics | Imaging radar startup/platform | Phoenix / 2,304-channel platform | Very high virtual-channel count and dense detections | Usually chipset/partnership rather than inexpensive standalone module | High-end imaging radar roadmap | https://arberobotics.com/ |
| bitsensing | Korean radar startup | AIR 4D and mobility radars | Automotive 4D focus; raw point-cloud and Doppler access; agile supplier | New-product maturity, safety package, pricing and module availability to validate | High-priority startup RFQ | https://bitsensing.com/ |
| Vayyar | Wide-FOV radar specialist | XRR | 0–300 m and very wide field of view; high antenna count; on-chip processing | Commercial ICD/price/qualification require engagement | Wide-FOV architecture research / RFQ | https://vayyar.com/automotive/ |
| Altos Radar | 4D radar startup | Altos V2/V4/RF families | Long-range dense point cloud; research-friendly | Automotive production/safety status and cost need validation | Algorithm benchmark / research sensor | https://altosradar.com/ |
| Provizio | Radar perception startup | 5D radar perception and sensor systems | Software-defined radar and perception focus | Hardware product availability and production model less transparent | Software/perception partnership scouting | https://provizio.ai/ |
| Spartan Radar | Radar software/product startup | Clarify software; Hoplo; Phalanx | Platform-agnostic radar enhancement; works across TI/NXP/NVIDIA and commercial-vehicle products | Some offerings are software or camera-radar systems rather than bare radar sensors | Radar software and commercial-vehicle partnership | https://spartanradar.com/ |
| Nanoradar | China radar specialist | MR76, SR71/SR73F/SR75, AFM711 | Low-cost enclosed radar range; direct supplier access | Safety/lifecycle, English SDK, false-target and PPAP evidence need deep audit | Cost-first smart radar RFQ | https://www.nanoradar.com/ |
| Calterah | China automotive radar semiconductor | Alps/Alps-Pro/Andes/Kunlun | Automotive-oriented low-cost radar SoCs and reference designs; CAN/Ethernet options through partners | Not a finished sensor; needs module partner, antenna and safety engineering | Custom low-cost production radar path | https://www.calterah.com/ |
| CUB / CUBTEK | Taiwan automotive electronics | 77 GHz turn-assist/BSIS systems | Commercial-vehicle safety products and ECE R151 positioning | Object-data access and modularity must be negotiated | Truck/bus regulatory product RFQ | https://www.cub.com.tw/en/product/adas/ |
| NXP | Automotive semiconductor | SAF85xx, TEF82xx + S32R | Strong automotive safety and high-performance radar processor ecosystem | NDA/selected-customer access; high development NRE | Custom OEM-grade radar platform | https://www.nxp.com/applications/automotive/adas-and-highly-automated-driving/radar |
| Texas Instruments | Automotive/industrial semiconductor | AWRL1432, AWR1843, AWR2944, AWR2243 | Best open EVK/demo ecosystem; processors integrated; broad community | Productization, antenna, enclosure, calibration and safety remain ADVIS/vendor work | Best low-cost radar learning/custom prototype path | https://www.ti.com/sensors/mmwave-radar/automotive/overview.html |
| Infineon | Automotive semiconductor | CTRX8188F/8191F; 77/79 GHz front ends; CARKIT | New 8Tx8Rx production-intent silicon and vehicle-test kits | Design-in access and substantial custom-sensor work | High-resolution custom radar path | https://www.infineon.com/cms/en/product/sensor/radar-sensors/automotive-radar/ |
| OmniPreSense | Small radar module vendor | OPS243 family | Open, simple USB/UART/SPI APIs and low sample cost | 24 GHz, limited angular resolution, not automotive-grade | Bench/interface prototype only | https://omnipresense.com/ |
| Acconeer | Pulsed coherent radar specialist | A121, XM125/XM126, XE125 | Low-power compact 60 GHz modules with developer ecosystem | Near-field/IoT, not high-speed road ADAS | Cabin/parking/near-field research | https://acconeer.com/products/ |

## Highest-priority less-utilized candidates

### 1. Ainstein

A complete smart-radar approach with CAN-FD is highly aligned with the ADVIS universal boundary. The K-77 is the strongest front-radar PoC candidate, while T-79-class corner products deserve an RFQ for BSD/LCA/RCTA.

### 2. smartmicro

More expensive than marketplace alternatives, but unusually strong for low-volume engineering because the product family supports CAN-FD, Automotive Ethernet, object data, optional radar-cube streaming, ROS/ROS2 and multiple front/corner roles.

### 3. Nanoradar

Worth testing for a cost-first emerging-market product, provided the exact model, firmware, DBC, target limits, environmental qualification and supplier support are audited.

### 4. Calterah ecosystem

A strong custom production-cost path when ADVIS or a module partner is ready to own antenna, radar firmware, enclosure, calibration, safety and PPAP. It is not a plug-and-play sensor shortcut.

### 5. CUB / CUBTEK

Relevant for buses, trucks and regulatory blind-side/turn-assist systems, particularly when a finished HMI/system is more important than raw perception access.

### 6. bitsensing, Uhnder, Arbe, Vayyar and Altos

These are premium or emerging imaging-radar paths. They are valuable for benchmarking and future L2+/L3 architecture, but are unlikely to be the cheapest first ADVIS Fusion radar.

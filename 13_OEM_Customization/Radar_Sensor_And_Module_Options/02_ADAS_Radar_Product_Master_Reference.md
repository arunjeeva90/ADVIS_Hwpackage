# ADAS Radar Product Master Reference

This file provides a readable master shortlist. The full engineering comparison with frequency, FoV, strengths, limitations, access and sourcing fields is in:

- `data/Radar_Product_Master.csv`

## Interpretation rules

- `A` — current global Tier-1/OEM automotive radar.
- `B` — automotive specialist or imaging-radar startup.
- `C` — accessible finished sensor or cost-oriented alternative.
- `D` — chipset/EVM requiring productization.
- `E` — prototype/DIY only.
- `F` — legacy/obsolete; avoid for new design.
- Vendor maximum-range claims are not directly comparable without identical RCS, probability-of-detection, false-alarm and waveform conditions.
- Public prices are observations, not approved quotations.

## Master reference

| Rank | Tier | Vendor | Product | Range | Output_Interface | Best_ADAS_Use | Observed_Price |
|---|---|---|---|---|---|---|---|
| 1 | A — Current Tier-1 front | Bosch | New-generation front radar | Up to 530 m | OEM vehicle network / central fusion | Premium front ACC/AEB/L2+/L3 benchmark | RFQ / OEM nomination |
| 2 | A — Commercial vehicle Tier-1 | Bosch | Front radar sensor for heavy commercial vehicles | Up to 210 m | OEM vehicle network | Truck/bus AEBS, FCW, ACC and urban VRU detection | RFQ / OEM nomination |
| 3 | A — Tier-1 imaging | Continental | ARS540 | 300 m | OEM interface; data package by programme | Premium L2+/L3 front sensing, stationary object and VRU discrimination | RFQ / OEM nomination |
| 4 | A/B — Professional reference | Continental | ARS548 RDI | 0.2–300 m | 100BASE-T1 / BroadR-Reach Ethernet | Benchmarking, autonomous research, off-highway and engineering validation | Quote only |
| 5 | A — Tier-1 corner | Aptiv | SRR7 | 160 m for motorbike-size target | 100 Mbit/s Ethernet and CAN-FD by configuration | BSD, LCA, RCTA, DOW, side VRU and zonal architectures | RFQ / OEM nomination |
| 6 | A — Tier-1 premium corner | Aptiv | SRR7+ | 200 m for motorbike-size target | 100 Mbit/s Ethernet and CAN-FD by configuration | Premium corner, dual-corner ACC, low-speed automation and 360° fusion | RFQ / OEM nomination |
| 7 | A — Tier-1 front | Aptiv | FLR7 | 290–300 m class | 100 Mbit/s Ethernet and CAN-FD by configuration | ACC, FCW, AEB and base 4D front perception | RFQ / OEM nomination |
| 8 | A — Tier-1 imaging | ZF | 4D Imaging Radar | Up to 350 m | OEM interface | L2+/L3/L4 front or surround imaging radar benchmark | RFQ / OEM nomination |
| 9 | A — Tier-1 imaging | Magna | ICON Digital / Imaging Radar | Vendor publicly cited pedestrian detection up to 150 m | OEM interface | High-end front perception and automated driving | RFQ / OEM nomination |
| 10 | A — Tier-1 imaging | Valeo | High Definition Radar Sensor | 300 m and beyond stated for Mobileye/Valeo programme | OEM interface | Premium highway pilot and imaging-radar benchmark | RFQ / OEM nomination |
| 11 | B — Independent automotive | smartmicro | DRVEGRD 171 | Passenger car 240 m; pedestrian 98 m in product sheet | CAN-FD; 100BASE-T1; optional 1000BASE-T1 radar cube | Plug-and-play professional front radar, research, specialty vehicles and possible low-volume production | Quote only |
| 12 | B — Independent automotive | smartmicro | DRVEGRD 152 | Passenger car 178 m; pedestrian 65 m in product sheet | CAN-FD; 100BASE-T1; optional 1000BASE-T1 radar cube | Corner/front ADAS, specialty vehicles and scalable 360° coverage | Quote only |
| 13 | B — Independent automotive | smartmicro | DRVEGRD 169 | Vendor configuration dependent | CAN-FD and Automotive Ethernet by configuration | BSD/LCA/RCTA/DOW, parking and near-field VRU | Quote only |
| 14 | B — Digital radar startup | Uhnder | S80 / S81 | Vendor states pedestrian detection around 300 m for high-end configurations | Automotive Ethernet / product-specific | High-resolution front/side radar and difficult close-target discrimination | Quote only |
| 15 | B — Imaging radar startup | Arbe | Phoenix / Radar Processor platform | Configuration dependent | Automotive Ethernet / vendor platform | Premium imaging radar development, L2+ through L4 | Quote only |
| 16 | B — Startup smart radar | bitsensing | AIR 4D | Vendor configuration dependent | Raw point cloud, Doppler and optional raw data | L2+/L3 perception, dataset capture and radar-camera fusion | Quote only |
| 17 | B — Wide-FOV imaging | Vayyar | XRR | 0–300 m | On-chip processed output / programme-specific | Multi-role front/corner/near-field sensing and compact 360° concepts | Quote only |
| 18 | B — Startup development radar | Altos Radar | Altos V2 / V4 family | V2 vendor states cars 400 m and pedestrians ~200 m; V4 up to 600 m | Ethernet / SDK | Research, long-range fusion, robotics and algorithm benchmarking | Quote only |
| 19 | B/C — Accessible smart front | Ainstein | K-77 | 0.2–220 m | 2 × CAN-FD | Best candidate for SoC-agnostic front-radar PoC: ACC/FCW/AEB confirmation | Quote only |
| 20 | B/C — Accessible smart corner | Ainstein | T-79 | 0.3–110 m | CAN-FD / product-specific | BSD, LCA, RCTA, DOW and side VRU prototype | Quote only |
| 21 | C — China smart front | Nanoradar | MR76 | 0.2–170 m | CAN / serial by model | Cost-sensitive front FCW/ACC experiments, commercial vehicle and robotics | Quote only |
| 22 | C — China smart short range | Nanoradar | SR73F | 0.2–40 m | CAN / serial by model | Low-speed obstacle warning, side/rear detection and commercial vehicle blind zone | Quote only |
| 23 | C — China 4D alternative | Nanoradar | SR75 | Model/configuration dependent | CAN/Ethernet by configuration | Corner fusion and emerging-market cost-down evaluation | Quote only |
| 24 | B/C — Commercial vehicle | CUB / CUBTEK | 77 GHz Turn Assist Radar | Application dependent | CAN / system harness / HMI | Truck/bus BSIS, turn assist and retrofit programme benchmark | Quote only |
| 25 | C — Mature professional benchmark | Continental | ARS408-21 | Up to 250 m | CAN | Fast reference PoC, dataset capture and algorithm integration | US$499.10 observed complete retail listing; lower grey-market prices exist |
| 26 | C/D — China chipset reference | Calterah | Alps-Pro forward radar solution | Up to 240 m | CAN/CAN-FD/Ethernet depending module design | Low-cost custom front smart radar product development | RFQ |
| 27 | C/D — China chipset reference | Calterah | Alps corner radar solution | Up to 180 m | CAN/CAN-FD/Ethernet depending module | BSD/LCA/RCTA/DOW custom production radar | RFQ |
| 28 | D — Automotive radar chipset EVK | NXP | SAF85xx Evaluation Kit | Application waveform dependent | CAN-FD; 100/1000BASE-T1 | Custom automotive radar development and vendor-independent fusion stack | NDA / RFQ |
| 29 | D — Automotive raw radar EVK | NXP | TEF82xx CAB + S32R41/S32R45 | Waveform and antenna dependent | MIPI CSI-2 raw ADC plus processor interfaces | Advanced radar algorithm and custom sensor development | S32R boards around US$1,400 observed; full kit quote-dependent |
| 30 | D — Automotive chipset car kit | Infineon | CARKIT with CTRX8191F / CTRX8188F | Waveform/antenna dependent | Gigabit Ethernet data output; processed/raw modes by kit | 4D radar prototype and custom product development | Quote / sample |
| 31 | D — TI automotive EVK | Texas Instruments | AWR2944EVM | Waveform dependent | CAN, Ethernet/USB debug and TI tooling | BSD, corner radar, front radar algorithms and custom smart-sensor prototype | Approx. ₹74,302.82 observed |
| 32 | D — TI automotive EVK | Texas Instruments | AWR1843BOOST | Waveform dependent | UART/USB; CAN connector; DCA1000 optional | Low-cost radar algorithm learning, object tracking and first vehicle bench PoC | Approx. ₹45,693.69 observed |
| 33 | D — TI low-power EVK | Texas Instruments | AWRL1432BOOST / BSD variant | Waveform dependent | USB/UART; point cloud; DCA1000 support | BSD, parking/near-field and two-wheeler/low-cost sensor exploration | Quote / distributor price varies |
| 34 | D — TI raw front-end EVK | Texas Instruments | AWR2243BOOST / Cascade Imaging Radar EVM | Waveform/array dependent | Raw data via DCA1000 / processor board | Raw ADC and custom 4D radar algorithm development | Quote / distributor |
| 35 | D/E — Universal bench module | OmniPreSense | OPS243-C | Up to ~100 m application dependent | USB/UART/SPI; Wi-Fi variant | Speed/range bench tests, low-speed obstacle experiments and interface prototyping | US$244 observed |
| 36 | D/E — Universal Doppler module | OmniPreSense | OPS243-A | Speed-detection range application dependent | USB/UART/SPI; Wi-Fi variant | Approach-speed demonstrator and simple warning logic | US$224 observed |
| 37 | E — 60 GHz research | Acconeer | XE125 / XM125 | Up to 20 m in Acconeer product documentation | USB-C on EVK; module MCU API | Near-field parking, cabin, gesture, material/occupancy and very-low-speed experiments | ₹11,283.17 for XE125 observed |
| 38 | E — 60 GHz IoT research | Infineon | BGT60TR13C Demo / Shield | Short range; application dependent | USB through baseboard / SDK | Cabin/occupancy, gesture, short-range research | Distributor price varies |
| 39 | E — Cheapest FMCW learning | DFRobot | C4001 24 GHz | 12 m version; 25 m version also sold | I2C / UART | Very cheap interface/HMI, parking-distance and bench experiments | US$12.90 (12 m); US$13.90 (25 m) observed |
| 40 | E — DIY presence | DFRobot | SEN0395 | 9 m | UART / digital I/O | DIY parking/presence demo only | US$29 observed |
| 41 | E — Marketplace front warning | Generic China suppliers | 77 GHz front FCW/AEB radar module | Often claimed 150–250 m | Usually CAN / proprietary harness | Packaging/HMI trial, non-safety fleet warning prototype after bench validation | US$155–160 typical observed; some US$255–270 |
| 42 | E — Marketplace BSD kit | Generic China suppliers | Dual 77 GHz BSD/LCA/RCTA kit | Commonly 50–80 m claimed | Proprietary harness / CAN-like or direct HMI | BSD/LCA/RCTA/DOW retrofit demo and packaging study | US$70–150 observed depending kit |
| 43 | E — Marketplace two-radar kit | RoadPassion / Alibaba seller | Dual 77 GHz BSD system | Around 70 m claimed | Complete harness/HMI | Fast vehicle demonstration without central SoC integration | ₹12,819.87–₹13,769.49 observed by quantity |
| 44 | F — Legacy/avoid new design | Renesas | RAA270205 / related radar SoC | Design dependent | MIPI CSI-2 / chipset interfaces | Legacy comparison only | Obsolete |
| 45 | F — Legacy/avoid new design | Renesas | SRIR144V3 radar system | Legacy design dependent | Legacy interfaces | Reverse engineering / archived benchmark only | Obsolete |

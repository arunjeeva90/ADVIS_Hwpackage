# Supplier and Price Sourcing Reference

## Interpretation rules

- Prices were observed during the scan on **20 July 2026** and are not approved quotations.
- Confirm whether a listing is a bare sensor, lens module, MIPI board, USB-UVC camera, serialized camera or complete enclosed product.
- One marketplace page may advertise several optional sensors. Require the exact populated sensor and photograph of its marking.
- Verify whether the stated frame rate is actually available over the advertised interface and pixel format.
- USB MJPEG/H.264 output is not equivalent to RAW access.
- Automotive-grade sensor qualification does not qualify the lens, PCB, serializer, connector, cable or enclosure.

| Sensor | Item type | Seller/platform | Region | Price seen | MOQ | Status | Risk / interpretation | Product link |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| OV2312 | 2 MP RGB-IR global-shutter MIPI module | Alibaba marketplace | China | US$23.35–56.50 | MOQ 5 | Open marketplace | Exact sensor, pinout, RGB-IR output, lens and IR filter must be confirmed | https://www.alibaba.com/showroom/camera-module-global-shutter.html |
| OV2312 | 2 MP MIPI night-vision module SF3V2312BA | Sincere First / Made-in-China | China | US$53.50 (5–99); $33.50 (100–999); $25.35 (1k–9999); $23.35 (10k+) | MOQ 5 | Listed July 2026 | Extreme 149° HFOV listing is not ideal for focused DMS; request 60–75° lens | https://sincerefirst.en.made-in-china.com/product/wpWroMsvwekh/China-Ov2312-Mipi-Camera-Module-2MP-Night-Vision-for-Lpr-System-and-Security-Monitoring.html |
| OV2311 | Professional GMSL2 camera module | Mouser India / Leopard Imaging | India / global | Approx. ₹38,540–39,974 | 1 | Distributor / professional module | Traceable and convenient but expensive; verify deserializer board and lens | https://www.mouser.in/c/embedded-solutions/engineering-tools/video-modules/?q=OV2311 |
| OV2311 | USB3 + GMSL2 evaluation kit | Mouser India / Leopard Imaging | India | Approx. ₹48,424 | 1 | Distributor / evaluation kit | Useful professional benchmark, not cost-first procurement | https://www.mouser.in/c/embedded-solutions/engineering-tools/video-modules/?q=OV2311 |
| OV2311 | Dual-camera stereo board | ElectronicsComp | India | ₹13,199 excluding GST observed | 1 | Out of stock observed | Stereo product; verify whether two OV2311 sensors and Linux support match need | https://www.electronicscomp.com/ |
| AR0234CS | 2.3 MP high-speed global-shutter module | Alibaba marketplace | China | US$31.99–33.61 | MOQ 1 | Marketplace | Confirm MIPI versus bare board, color/mono, trigger and lens | https://www.alibaba.com/showroom/global-shutter-camera-module.html |
| AR0234CS | 2 MP USB2 global-shutter module | Sincere First / Made-in-China | China | US$35.50 (5–99); $29.50 (100–999); $24.35 (1k+) | MOQ 5 | Listed in stock | USB2 may not expose full 120 fps or RAW; request UVC mode table | https://sincerefirst.en.made-in-china.com/product/ZrFpQUuSfWkO/China-Ar0234-2MP-1080P-Imx225-Wide-Angle-High-Dynamic-Range-Color-Sensor-Global-Shutter-USB2-0-Camera-Module.html |
| AR0234CS | ELP USB global-shutter camera | Alibaba | China | US$60.59–73.75 | MOQ 2 | Retail marketplace | More complete UVC option; verify NIR sensitivity and manual controls | https://www.alibaba.com/showroom/global-shutter-camera-module.html |
| AR0144 / OV9281 | 24-pin global-shutter MIPI module family | Alibaba | China | US$8.66–10.55 | MOQ 20 | Marketplace | Page may cover multiple sensors; require exact populated part and pin map | https://www.alibaba.com/showroom/global-shutter-camera-module-ov9281.html |
| AR0144 | ELP 720p USB UVC global-shutter camera | Alibaba | China | US$39.27–43.58 | MOQ 1 | Retail marketplace | Industrial prototype only; check monochrome/NoIR and manual exposure | https://www.alibaba.com/showroom/global-shutter-camera-module.html |
| OV9281 | 1 MP USB-UVC M12 industrial camera | Alibaba | China | US$22.99 (1–199); $21.99 (200–499); $20.89 (500+) | MOQ 1 | Listed | Best price/compatibility starting point; confirm NoIR and Linux UVC controls | https://www.alibaba.com/product-detail/OV9281-1MP-Global-Shutter-USB-Camera_1601715788861.html |
| OV9281 | Industrial USB camera listings | Alibaba showroom | China | US$24–26 typical | MOQ 1 | Many sellers | Compare frame modes, actual 120 fps transport, lens and IR-cut filter | https://www.alibaba.com/showroom/global-shutter-camera-module-ov9281.html |
| OV9281 | MIPI/DVP fixed-focus module | Alibaba | China | US$7–15 | MOQ 1 | Marketplace | Cheap module but driver/pinout integration is entirely on buyer | https://www.alibaba.com/showroom/global-shutter-camera-module-ov9281.html |
| OV9281 | UVC monochrome global-shutter module | Made-in-China | China | US$25 | MOQ 1 | Listed in stock | Good low-quantity alternative; request 850/940 nm response and UVC controls | https://www.made-in-china.com/price/prodetail_Security-Camera_SpHUoJwLXsWf.html |
| OV9281 | USB global-shutter camera | ThinkRobotics | India | ₹3,299.99 observed | 1 | Out of stock / preorder observed | Convenient India option when stocked; verify NoIR and lens FOV | https://thinkrobotics.com/products/arducam-ov9281-usb-camera |
| OV9281 | Waveshare OV9281-120 MIPI module | ElectronicsComp | India | ₹3,226 excluding GST observed | 1 | Low stock observed | Board-specific CSI; verify target SBC driver | https://www.electronicscomp.com/ |
| OV9281 | Arducam OV9281 module | ElectronicsComp | India | ₹2,159 excluding GST observed | 1 | Out of stock observed | Low-cost India listing; check interface and included lens | https://www.electronicscomp.com/ |
| OV9281 | Arducam NoIR MIPI camera | ElectronicsComp | India | ₹5,659 excluding GST observed | 1 | Out of stock observed | More complete NoIR option; check host support | https://www.electronicscomp.com/ |
| OV9782 | 1 MP color global-shutter MIPI module | Alibaba | China | US$12.35–23.35 | MOQ 5 | Marketplace | Good cheap color GS option; confirm RAW and IR filter | https://www.alibaba.com/showroom/camera-module-global-shutter.html |
| OV9782 | USB2 color global-shutter module | Alibaba | China | US$47–60 | MOQ 5 | Marketplace | Convenient but expensive relative to OV9281 mono | https://www.alibaba.com/showroom/global-shutter-camera-module-ov9281.html |
| OV9732 | 720p night-vision / tiny module | Alibaba | China | US$6.35–21.50 | MOQ 5 | Marketplace | Cheapest acceptable 720p; rolling shutter and inconsistent ISP | https://www.alibaba.com/showroom/global-shutter-camera-module-ov9281.html |
| OV9732 | USB 720p module | Alibaba | China | US$12.50 | MOQ 1 | Marketplace | Very low-cost UVC face/head demo | https://www.alibaba.com/showroom/ov9281-usb-camera-module.html |
| OV7251 | VGA global-shutter MIPI module | Alibaba | China | US$5–9 | MOQ 2 | Marketplace | Eye ROI / optical flow only | https://www.alibaba.com/showroom/global-shutter-camera-module-ov9281.html |
| OV7251 | USB global-shutter module | Alibaba | China | US$17–19 | MOQ 5 | Marketplace | Easy but too low resolution for complete DMS | https://www.alibaba.com/showroom/global-shutter-camera-module-ov9281.html |
| IMX296 / IMX287 | Global-shutter MIPI industrial module | Alibaba | China | US$6–12 | MOQ 500 | High-MOQ marketplace | Price is not representative of a supported low-quantity camera | https://www.alibaba.com/showroom/global-shutter-camera-module-ov9281.html |
| IMX462 | Low-light / NIR camera module | Alibaba | China | Approx. US$39.90 sample | MOQ varies | Marketplace | Excellent night comparison; often compressed output | https://www.alibaba.com/showroom/imx462-camera-module.html |
| IMX462 | Camera module | ElectronicsComp | India | Approx. ₹5,675 observed | 1 | Availability variable | Verify USB/MIPI, lens and IR-cut configuration | https://www.electronicscomp.com/ |
| IMX219 NoIR | Raspberry Pi NoIR Camera V2 | Robocraze | India | ₹1,565 including GST observed | 1 | Retail | Cheapest convenient India night-DMS option for Raspberry Pi | https://robocraze.com/products/raspberry-pi-noir-camera-module-v2 |
| IMX219 | Generic / Pi-compatible camera | Robu | India | Approx. ₹949–1,945 depending module | 1 | Retail | Board connector and NoIR status vary | https://robu.in/product-category/camera-and-displays/camera-modules/ |
| OV5647 | 5 MP Raspberry Pi camera | Robocraze | India | ₹285 including GST observed | 1 | Retail | Absolute-cheapest daylight/software demo only | https://robocraze.com/products/raspberry-pi-camera-module-5mp |
| OV5647 / IR camera | Generic Pi IR camera listings | Robu | India | Approx. ₹529–880 observed | 1 | Retail | Check whether LEDs are included and eye-safety/current control | https://robu.in/product-category/camera-and-displays/camera-modules/ |
| OV5640 NoIR | 5 MP MIPI/DVP camera module | Made-in-China | China | Approx. US$18–25 | Often MOQ 100 | B2B | Fixed focus preferred; require exact pinout/driver | https://www.made-in-china.com/products-search/hot-china-products/OV5640_Camera_Module.html |
| OV7670 | VGA parallel camera module | Robu | India | Approx. ₹128 observed | 1 | Retail | Learning only; not a DMS evaluation camera | https://robu.in/product/ov7670-camera-module/ |

## Cheapest meaningful procurement ladder

1. **OV7670 / OV5647:** only camera/AI software bring-up.
2. **OV9732 / IMX219 NoIR:** cheapest usable face/head/night demo.
3. **OV9281 USB-UVC:** cheapest serious, motion-robust DMS prototype.
4. **AR0234CS USB/MIPI:** higher-resolution and high-speed industrial validation.
5. **OV2312 / OV2311:** best prototype-to-automotive DMS bridge.
6. **OX01H1B / VB56G4A / AR0144AT / SC233AT:** production RFQ rather than retail purchase.

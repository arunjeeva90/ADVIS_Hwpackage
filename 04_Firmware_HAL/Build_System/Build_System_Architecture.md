# ADVIS Build System Architecture

**Document ID:** ADVIS-FW-BLD-001  
**Version:** 0.1.0  
**Status:** Draft  
**Last Updated:** 2024-01-15

---

## 1. Purpose

This document defines the build system architecture for the ADVIS firmware, covering
the Yocto/Buildroot layer structure, cross-compilation targets, CI/CD integration,
artifact management, and version tagging strategy.

---

## 2. Build System Selection

### 2.1 Primary: Yocto Project

| Aspect | Choice | Rationale |
|--------|--------|-----------|
| Build framework | Yocto (Poky + OE-Core) | Industry standard for embedded Linux |
| Release | Kirkstone LTS or newer | Long-term support, automotive adoption |
| SoC BSP layer | meta-ti (TI Processor SDK) | Official TI support for Jacinto/Sitara |
| SoM layer | meta-phytec | Phytec phyCORE SoM support |
| ADVIS layer | meta-advis | Custom carrier board recipes |

### 2.2 Alternative: Buildroot (Rapid Prototyping)

For early bring-up and rapid iteration, a Buildroot configuration is maintained:

| Use Case | Framework | Build Time |
|----------|-----------|------------|
| Production firmware | Yocto | 2-4 hours (clean) |
| Prototype/debug | Buildroot | 30-60 minutes (clean) |
| CI smoke test | Buildroot | Fastest validation loop |

---

## 3. Yocto Layer Structure

```
sources/
+-- poky/                    (Yocto reference distribution)
+-- meta-openembedded/       (Community recipes)
+-- meta-ti/                 (TI BSP - kernel, U-Boot, firmware)
+-- meta-arm/                (ARM toolchain and support)
+-- meta-phytec/             (SoM-specific BSP)
+-- meta-advis/              (ADVIS carrier board layer)
    +-- conf/
    |   +-- layer.conf
    |   +-- machine/
    |       +-- advis-am68a.conf
    |       +-- advis-tda4vm.conf
    |       +-- advis-am62a.conf
    +-- recipes-bsp/
    |   +-- u-boot/
    |   |   +-- u-boot-advis_%.bbappend
    |   +-- linux/
    |   |   +-- linux-advis_%.bbappend
    |   +-- device-trees/
    |       +-- advis-device-trees_1.0.bb
    +-- recipes-advis/
    |   +-- advis-hal/
    |   |   +-- advis-hal_1.0.bb
    |   +-- advis-app/
    |   |   +-- advis-perception_1.0.bb
    |   |   +-- advis-dms_1.0.bb
    |   |   +-- advis-logging_1.0.bb
    |   +-- advis-watchdog/
    |   |   +-- advis-watchdog_1.0.bb
    |   +-- advis-config/
    |       +-- advis-soc-profiles_1.0.bb
    +-- recipes-connectivity/
    |   +-- can-utils/
    |       +-- can-utils_%.bbappend
    +-- recipes-core/
    |   +-- images/
    |       +-- advis-image-base.bb
    |       +-- advis-image-dev.bb
    |       +-- advis-image-production.bb
    +-- wic/
        +-- advis-sdcard.wks
        +-- advis-emmc.wks
```

---

## 4. Machine Configurations

### 4.1 Machine Definition (advis-am68a.conf)

```bitbake
# Machine configuration for ADVIS with AM68A SoC
#@TYPE: Machine
#@NAME: ADVIS AM68A ECU
#@DESCRIPTION: ADVIS carrier board with phyCORE-AM68A SoM

require conf/machine/include/phytec-am68a.inc

MACHINE_FEATURES += "can wifi bluetooth usb"

# Kernel and bootloader
PREFERRED_PROVIDER_virtual/kernel = "linux-ti-staging"
PREFERRED_PROVIDER_virtual/bootloader = "u-boot-ti-staging"

# Device tree
KERNEL_DEVICETREE += "ti/advis-carrier-v1.dtbo"
KERNEL_DEVICETREE += "ti/advis-carrier-v1-am68a.dtbo"

# Serial console
SERIAL_CONSOLE = "115200 ttyS2"

# Image features
IMAGE_INSTALL:append = " advis-hal advis-watchdog advis-soc-profiles"
```

---

## 5. Cross-Compilation Targets

| SoC | Architecture | Toolchain | Target Triple |
|-----|-------------|-----------|---------------|
| AM68A | ARMv8-A (Cortex-A72) | GCC aarch64 | aarch64-poky-linux |
| TDA4VM | ARMv8-A (Cortex-A72) | GCC aarch64 | aarch64-poky-linux |
| AM62A | ARMv8-A (Cortex-A53) | GCC aarch64 | aarch64-poky-linux |
| R5F MCU (TI) | ARMv7-R | GCC arm-none-eabi | arm-none-eabi |

### 5.1 SDK Generation

```bash
# Generate cross-compilation SDK for host development
bitbake advis-image-dev -c populate_sdk

# Install SDK
./tmp/deploy/sdk/poky-*.sh -d /opt/advis-sdk

# Source SDK environment
source /opt/advis-sdk/environment-setup-aarch64-poky-linux
```

---

## 6. Image Types

| Image | Purpose | Contents | Size (approx) |
|-------|---------|----------|---------------|
| advis-image-base | Minimal production | Kernel + HAL + WDT + App | 200 MB |
| advis-image-dev | Development | Base + SSH + GDB + strace + tools | 500 MB |
| advis-image-production | Release candidate | Base + OTA agent + secure boot | 250 MB |

### 6.1 Production Image Features

```bitbake
# advis-image-production.bb
IMAGE_FEATURES += "read-only-rootfs"
IMAGE_INSTALL += " \
    advis-hal \
    advis-watchdog \
    advis-perception \
    advis-dms \
    advis-logging \
    advis-soc-profiles \
    advis-ota-agent \
    advis-diagnostics \
"
IMAGE_INSTALL:remove = "ssh-server-dropbear debug-tools"
```

---

## 7. CI/CD Integration

### 7.1 Pipeline Stages

```
+----------+     +--------+     +---------+     +--------+     +---------+
|  Commit  | --> | Build  | --> |  Test   | --> | Stage  | --> | Release |
+----------+     +--------+     +---------+     +--------+     +---------+
                      |              |               |
                  Yocto build    Unit tests      Artifact
                  (all targets)  HIL tests       repository
                                 Smoke tests     Tag + sign
```

### 7.2 Build Triggers

| Trigger | Action | Targets |
|---------|--------|---------|
| Commit to develop | Build all images | AM68A (primary) |
| Merge to main | Full build + test | All SoC targets |
| Tag (vX.Y.Z) | Release build | All targets, signed |
| Nightly | Buildroot smoke test | AM68A only |

### 7.3 Build Caching

| Cache Type | Scope | Retention |
|-----------|-------|-----------|
| sstate-cache | Per-recipe build state | 30 days |
| DL_DIR | Source downloads | Permanent |
| Docker layer cache | Build environment | Per-branch |
| Artifact cache | Final images | Per-release tag |

---

## 8. Artifact Management

### 8.1 Build Outputs

| Artifact | Format | Naming Convention |
|----------|--------|-------------------|
| Root filesystem | ext4, wic | advis-image-{type}-{machine}-{version}.wic.gz |
| Kernel image | Image.gz | Image-{version}-{machine} |
| Device tree blobs | .dtb, .dtbo | advis-carrier-v1-{soc}.dtb |
| U-Boot binary | u-boot.img | u-boot-{machine}-{version}.img |
| SDK installer | .sh | poky-advis-sdk-{version}.sh |
| Debug symbols | .tar.gz | advis-dbg-{version}.tar.gz |

### 8.2 Artifact Repository Structure

```
releases/
+-- v1.0.0/
|   +-- am68a/
|   |   +-- advis-image-production-am68a-v1.0.0.wic.gz
|   |   +-- advis-image-production-am68a-v1.0.0.wic.gz.sha256
|   |   +-- advis-image-production-am68a-v1.0.0.manifest
|   +-- tda4vm/
|       +-- ...
+-- v1.1.0/
    +-- ...
```

---

## 9. Version Tagging Strategy

### 9.1 Semantic Versioning

Format: `vMAJOR.MINOR.PATCH[-prerelease][+build]`

| Version Component | Increment When |
|------------------|---------------|
| MAJOR | Breaking API change in Platform Abstraction |
| MINOR | New feature (new SoC support, new peripheral) |
| PATCH | Bug fix, security patch |
| Pre-release | alpha, beta, rc1 |
| Build metadata | Git commit hash, build number |

### 9.2 Version Embedding

The firmware embeds version information accessible at runtime:

```c
/* Auto-generated at build time */
#define ADVIS_FW_VERSION_MAJOR  1
#define ADVIS_FW_VERSION_MINOR  0
#define ADVIS_FW_VERSION_PATCH  0
#define ADVIS_FW_VERSION_STRING "1.0.0"
#define ADVIS_FW_BUILD_HASH     "a1b2c3d"
#define ADVIS_FW_BUILD_DATE     "2024-01-15"
```

### 9.3 Traceability

Every production image can be traced back to:
- Git commit hash (all layers)
- Yocto manifest (exact recipe versions)
- Build host and toolchain version
- Signing key fingerprint (for secure boot)

---

## 10. Reproducible Builds

### 10.1 Requirements

| Requirement | Implementation |
|-------------|----------------|
| Deterministic source | Git submodules or repo manifest |
| Fixed toolchain | Docker build container with pinned versions |
| Reproducible timestamps | SOURCE_DATE_EPOCH set from git log |
| No network during build | All sources pre-fetched to DL_DIR |
| Locked dependencies | Yocto layer index lock file |

### 10.2 Build Container

```dockerfile
# Build environment container
FROM ubuntu:22.04
RUN apt-get update && apt-get install -y \
    build-essential git python3 python3-pip \
    chrpath diffstat gawk texinfo \
    # ... (full Yocto host dependencies)
WORKDIR /build
```

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1.0 | 2024-01-15 | -- | Initial build system architecture |

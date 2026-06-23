# 12 - Configuration Management

## Purpose

Version control, engineering change orders, BOM variant management, and platform configuration tracking for the ADVIS hardware platform.

## Sub-folders

| Folder | Contents |
|--------|----------|
| Version_History/ | Baseline version records and delta summaries |
| ECO_Tracker/ | Engineering Change Order log and approval status |
| BOM_Variants/ | BOM variant definitions (Entry/Mid/High tier) |
| Platform_Configurations/ | Platform configuration files per OEM/variant |

## Current Baseline

**Project:** ADVIS (Adaptive Driver & Vehicle Intelligence System)  
**Version:** v0.4.4  
**Date:** June 2026  
**Status:** Architecture locked, schematic capture baseline

## Version Numbering

```
v{MAJOR}.{MINOR}.{PATCH}
  MAJOR = Architectural generation (0 = pre-production)
  MINOR = Significant design milestone
  PATCH = Incremental refinement
```

## Configuration Control

All changes to locked baseline items require a formal Engineering Change Order (ECO). See ECO_Tracker/ECO_Process.md for the full approval workflow.

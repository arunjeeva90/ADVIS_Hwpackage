#!/usr/bin/env python3
"""Restore the exact ADVIS DMS/OMS Excel workbook from ordered Base64 chunks."""

from __future__ import annotations

import base64
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PARTS_DIR = ROOT / "workbook_parts"
OUTPUT = ROOT / "ADVIS_DMS_OMS_In_Cabin_Sensor_Sourcing_Reference.xlsx"

parts = sorted(PARTS_DIR.glob("part_*.b64"))
if not parts:
    raise FileNotFoundError(f"No workbook chunks found in {PARTS_DIR}")
encoded = "".join(p.read_text(encoding="ascii").strip() for p in parts)
try:
    data = base64.b64decode(encoded, validate=True)
except ValueError as exc:
    raise ValueError("Workbook Base64 chunks are incomplete or corrupted") from exc
OUTPUT.write_bytes(data)
print(f"Restored: {OUTPUT}")
print(f"Parts used: {len(parts)}")
print(f"Workbook size: {len(data)} bytes")

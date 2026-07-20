#!/usr/bin/env python3
"""Restore the exact Excel workbook from ordered Base64 chunk files."""

from __future__ import annotations

import base64
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PARTS_DIR = ROOT / "workbook_parts"
OUTPUT = ROOT / "ADVIS_Forward_Vision_Sensor_Sourcing_Reference.xlsx"

parts = sorted(PARTS_DIR.glob("part_*.b64"))
if not parts:
    raise FileNotFoundError(f"No workbook chunks found in {PARTS_DIR}")

encoded = "".join(part.read_text(encoding="ascii").strip() for part in parts)
try:
    workbook_bytes = base64.b64decode(encoded, validate=True)
except ValueError as exc:
    raise ValueError("Workbook Base64 chunks are incomplete or corrupted") from exc

OUTPUT.write_bytes(workbook_bytes)
print(f"Restored: {OUTPUT}")
print(f"Parts used: {len(parts)}")
print(f"Workbook size: {len(workbook_bytes)} bytes")

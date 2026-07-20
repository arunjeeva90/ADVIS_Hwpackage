#!/usr/bin/env python3
"""Restore the exact Excel workbook stored as Base64 text in this folder."""

from pathlib import Path
import base64

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "ADVIS_Forward_Vision_Sensor_Sourcing_Reference.xlsx.base64"
OUTPUT = ROOT / "ADVIS_Forward_Vision_Sensor_Sourcing_Reference.xlsx"

OUTPUT.write_bytes(base64.b64decode(SOURCE.read_text(encoding="ascii")))
print(f"Restored: {OUTPUT}")

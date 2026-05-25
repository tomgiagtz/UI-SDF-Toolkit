from __future__ import annotations

import sys
from pathlib import Path

if getattr(sys, "frozen", False):
    _BASE_DIR = Path(sys._MEIPASS) / "sdf_toolkit_gui" / "resources"  # type: ignore[attr-defined]
else:
    _BASE_DIR = Path(__file__).parent


def resource_path(relative: str | Path) -> Path:
    return _BASE_DIR / relative

from __future__ import annotations

import numpy as np
from pathlib import Path
from PIL import Image


def load_r_channel(path: Path) -> np.ndarray:
    """Return the R channel of an image as a float32 array in [0.0, 1.0]."""
    img = Image.open(path).convert("RGBA")
    return np.array(img)[:, :, 0].astype(np.float32) / 255.0


def save_grayscale(array: np.ndarray, path: Path) -> None:
    """Save a float32 array [0.0, 1.0] as an 8-bit grayscale PNG."""
    u8 = np.clip(array * 255.0, 0, 255).astype(np.uint8)
    Image.fromarray(u8, mode="L").save(path)
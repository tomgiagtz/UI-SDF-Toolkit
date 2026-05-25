from __future__ import annotations

import numpy as np
from scipy.ndimage import distance_transform_edt


def generate_sdf(mask: np.ndarray, spread: float = 32.0) -> np.ndarray:
    """Generate a normalized SDF from a float32 mask [0.0, 1.0].

    Returns float32 in [0.0, 1.0] where 0.5 is the boundary,
    values > 0.5 are inside, values < 0.5 are outside.
    """
    binary = mask >= 0.5
    dist_inside = distance_transform_edt(binary)
    dist_outside = distance_transform_edt(~binary)
    sdf = (dist_inside - dist_outside) / spread
    return np.clip(sdf * 0.5 + 0.5, 0.0, 1.0).astype(np.float32)
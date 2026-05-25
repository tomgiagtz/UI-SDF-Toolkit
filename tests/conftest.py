from __future__ import annotations

from pathlib import Path

import pytest
from PIL import Image, ImageDraw

FIXTURES_DIR = Path(__file__).parent / "fixtures"


@pytest.fixture
def fixtures_dir() -> Path:
    return FIXTURES_DIR


@pytest.fixture
def sample_png(tmp_path: Path) -> Path:
    path = tmp_path / "sample.png"
    img = Image.new("RGBA", (64, 64), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    draw.circle((32, 32), 16, fill=(255, 0, 0, 0))

    img.save(path)
    return path

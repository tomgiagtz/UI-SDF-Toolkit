from __future__ import annotations

from pathlib import Path

import pytest
from click.testing import CliRunner

from sdf_toolkit.cli import main


@pytest.fixture
def runner() -> CliRunner:
    return CliRunner()


def test_copy_creates_output_file(runner: CliRunner, sample_png: Path, tmp_path: Path) -> None:
    out_dir = tmp_path / "out"
    result = runner.invoke(
        main, ["copy", "--input-image", str(sample_png), "--output-dir", str(out_dir)]
    )
    assert result.exit_code == 0
    assert (out_dir / sample_png.name).exists()


def test_copy_creates_output_dir_if_missing(
    runner: CliRunner, sample_png: Path, tmp_path: Path
) -> None:
    out_dir = tmp_path / "nested" / "out"
    result = runner.invoke(
        main, ["copy", "--input-image", str(sample_png), "--output-dir", str(out_dir)]
    )
    assert result.exit_code == 0
    assert out_dir.is_dir()


def test_sdf_creates_output_file(runner: CliRunner, sample_png: Path, tmp_path: Path) -> None:
    out_dir = tmp_path / "out"
    result = runner.invoke(
        main, ["sdf", "--input-image", str(sample_png), "--output-dir", str(out_dir)]
    )
    assert result.exit_code == 0
    assert (out_dir / sample_png.name).exists()

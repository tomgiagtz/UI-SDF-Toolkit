from __future__ import annotations

import shutil
from pathlib import Path

import click

from sdf_toolkit import image_io
from sdf_toolkit import sdf as sdf_lib


def _image_input_option(f: click.decorators.FC) -> click.decorators.FC:
    return click.option(
        "--input-image",
        required=True,
        type=click.Path(exists=True, dir_okay=False, path_type=Path),
        help="Path to the source image.",
    )(f)


def _output_dir_option(f: click.decorators.FC) -> click.decorators.FC:
    return click.option(
        "--output-dir",
        required=True,
        type=click.Path(file_okay=False, path_type=Path),
        help="Directory to write the output image into.",
    )(f)


@click.group()
def main() -> None:
    pass


@main.command()
@_image_input_option
@_output_dir_option
def copy(input_image: Path, output_dir: Path) -> None:
    """Copy an image to the output directory unchanged."""
    output_dir.mkdir(parents=True, exist_ok=True)
    dest = output_dir / input_image.name
    shutil.copy2(input_image, dest)
    click.echo(f"Copied {input_image} -> {dest}")


@main.command()
@_image_input_option
@_output_dir_option
def sdf(input_image: Path, output_dir: Path) -> None:
    """Generate a signed distance field texture from an image."""
    output_dir.mkdir(parents=True, exist_ok=True)
    dest = output_dir / input_image.name
    mask = image_io.load_r_channel(input_image)
    result = sdf_lib.generate_sdf(mask)
    image_io.save_grayscale(result, dest)
    click.echo(f"SDF generated {input_image} -> {dest}")
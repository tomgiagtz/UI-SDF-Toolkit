# sdf-toolkit

A CLI tool for generating 2D signed distance field textures from raster images, aimed at game engine UI workflows (Unreal Engine, Unity).

## Goals

- Convert raster images into SDF textures suitable for GPU-side UI rendering
- Support 8-bit PNG, 16-bit TIFF, and 32-bit float EXR output
- Provide a PyQt6 GUI (`sdf-toolkit-gui`) that wraps the CLI with interactive controls

## Requirements

- Python 3.11+
- PyQt6 6.6+ *(GUI only)*

## Installation

```bash
# CLI only
pip install -e ".[dev]"

# CLI + GUI
pip install -e ".[gui,dev]"
```
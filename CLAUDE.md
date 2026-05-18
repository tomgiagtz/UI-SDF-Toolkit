# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**UI-SDF-Toolkit** generates 2D signed distance field (SDF) textures from raster images for game engine UI workflows (Unreal Engine, Unity). It has two components:

1. **`sdf-toolkit` (CLI)** — business logic: SDF generation, image I/O, and the `click`-based CLI entry point.
2. **`sdf-toolkit-gui` (Qt client)** — a thin PyQt6 GUI that drives the CLI; it does not reimplement logic.

Source code lives under `src/`.

## Architecture

The Qt client invokes the CLI rather than duplicating logic. All SDF and image-processing code belongs in the CLI layer; the GUI layer only translates user interactions into CLI calls and renders output.

Key modules in `src/sdf-toolkit/`:
- `cli.py` — `click` commands; entry point `sdf_toolkit.cli:main`
- `sdf.py` — SDF generation algorithms (numpy / scipy)
- `image_io.py` — raster I/O via Pillow, imageio, and opencv (PNG 8-bit, TIFF 16-bit, EXR 32-bit float)

Key modules in `src/sdf-toolkit-gui/`:
- `main.py` — application entry point `sdf_toolkit_gui.main:main`
- `widgets/` — reusable PyQt6 widget components

## Development Setup

```bash
# CLI only
pip install -e ".[dev]"

# CLI + GUI
pip install -e ".[gui,dev]"
```

## Common Commands

```bash
# Run CLI
sdf-toolkit [args]
# or
python -m sdf_toolkit.cli [args]

# Run Qt GUI
sdf-toolkit-gui
# or
python -m sdf_toolkit_gui.main

# Tests
pytest
pytest tests/path/to/test_file.py::test_name   # single test

# Lint
ruff check .
ruff check --fix .

# Type check
mypy src
```

## Code Style

- Line length: 100 characters (enforced by ruff).
- Type checking: mypy strict mode — all public functions must have full annotations.
- Python 3.11+ features are fine (target-version = py311).

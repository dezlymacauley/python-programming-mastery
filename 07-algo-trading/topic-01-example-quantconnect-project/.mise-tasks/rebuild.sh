#!/usr/bin/env bash
#MISE description="rebuild the virtual environment and project dependencies"
#MISE quiet=true

# Ensure that this is a clean build
rm -rf __pycache__
rm -rf .ruff_cache
rm -rf .venv

# Rebuild the the virtual environment and install the dependencies
uv sync

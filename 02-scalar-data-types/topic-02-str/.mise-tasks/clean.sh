#!/usr/bin/env bash
#MISE description="clean the '.ruff_cache/', '__pycache__' and '.venv/' directories"
#MISE quiet=true

rm -rf __pycache__
rm -rf .ruff_cache
rm -rf .venv

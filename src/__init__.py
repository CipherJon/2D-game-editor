"""
Root package for the 2D game editor.

This package contains all the core modules and utilities for the 2D game editor.
"""

# Import core modules to make them available at the package level
from . import assets, core, editor, rendering, scene, tools, ui, utils

__all__ = [
    "assets",
    "core",
    "editor",
    "rendering",
    "scene",
    "tools",
    "ui",
    "utils",
]

"""
Root package for the 2D game editor.

This package contains all the core modules and utilities for the 2D game editor.
"""

# Import core modules to make them available at the package level
from . import assets
from . import core
from . import editor
from . import rendering
from . import scene
from . import tools
from . import ui
from . import utils

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
```

Now, let's run the tests again to see if the issue is resolved.

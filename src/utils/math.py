# math.py
# Utility functions for mathematical operations in the 2D game editor.


def clamp(value, min_val, max_val):
    """
    Clamp a value between a minimum and maximum value.

    Args:
        value: The value to clamp.
        min_val: The minimum value.
        max_val: The maximum value.

    Returns:
        The clamped value.
    """
    return max(min_val, min(value, max_val))


def lerp(a, b, t):
    """
    Linear interpolation between two values.

    Args:
        a: The start value.
        b: The end value.
        t: The interpolation factor (0.0 to 1.0).

    Returns:
        The interpolated value.
    """
    return a + (b - a) * t


def snap_to_grid(value, grid_size):
    """
    Snap a value to the nearest grid size.

    Args:
        value: The value to snap.
        grid_size: The size of the grid.

    Returns:
        The snapped value.
    """
    return round(value / grid_size) * grid_size


def distance(x1, y1, x2, y2):
    """
    Calculate the Euclidean distance between two points.

    Args:
        x1: The x-coordinate of the first point.
        y1: The y-coordinate of the first point.
        x2: The x-coordinate of the second point.
        y2: The y-coordinate of the second point.

    Returns:
        The distance between the two points.
    """
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

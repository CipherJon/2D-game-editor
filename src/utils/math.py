"""
Utility functions for mathematical operations in the 2D game editor.

This module provides functions for common mathematical operations, such as
clamping values, linear interpolation, snapping to grids, and calculating distances.
"""


def clamp(value: float, min_val: float, max_val: float) -> float:
    """
    Clamp a value between a minimum and maximum value.

    Args:
        value (float): The value to clamp.
        min_val (float): The minimum value.
        max_val (float): The maximum value.

    Returns:
        float: The clamped value.

    Raises:
        ValueError: If min_val is greater than max_val.

    Examples:
        >>> clamp(5, 0, 10)
        5
        >>> clamp(-5, 0, 10)
        0
        >>> clamp(15, 0, 10)
        10
    """
    if min_val > max_val:
        raise ValueError("min_val must be less than or equal to max_val.")
    return max(min_val, min(value, max_val))


def lerp(a: float, b: float, t: float) -> float:
    """
    Linear interpolation between two values.

    Args:
        a (float): The start value.
        b (float): The end value.
        t (float): The interpolation factor (0.0 to 1.0).

    Returns:
        float: The interpolated value.

    Raises:
        ValueError: If t is not within the range [0.0, 1.0].

    Examples:
        >>> lerp(0, 10, 0.5)
        5.0
        >>> lerp(0, 10, 0.0)
        0.0
        >>> lerp(0, 10, 1.0)
        10.0
    """
    if not 0.0 <= t <= 1.0:
        raise ValueError("Interpolation factor t must be between 0.0 and 1.0.")
    return a + (b - a) * t


def snap_to_grid(value: float, grid_size: float) -> float:
    """
    Snap a value to the nearest grid size.

    Args:
        value (float): The value to snap.
        grid_size (float): The size of the grid.

    Returns:
        float: The snapped value.

    Raises:
        ValueError: If grid_size is zero or negative.

    Examples:
        >>> snap_to_grid(5.7, 2)
        6.0
        >>> snap_to_grid(-3.2, 2)
        -4.0
    """
    if grid_size <= 0:
        raise ValueError("grid_size must be positive.")
    return round(value / grid_size) * grid_size


def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """
    Calculate the Euclidean distance between two points.

    Args:
        x1 (float): The x-coordinate of the first point.
        y1 (float): The y-coordinate of the first point.
        x2 (float): The x-coordinate of the second point.
        y2 (float): The y-coordinate of the second point.

    Returns:
        float: The distance between the two points.

    Examples:
        >>> distance(0, 0, 3, 4)
        5.0
        >>> distance(1, 1, 1, 1)
        0.0
    """
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

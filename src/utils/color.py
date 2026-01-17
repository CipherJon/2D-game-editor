"""
Utility functions for color manipulation and conversion.

This module provides functions for converting between different color formats,
such as hex and RGB, and manipulating colors.
"""

from typing import Tuple


def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
    """
    Convert a hex color string to an RGB tuple.

    Args:
        hex_color (str): A hex color string (e.g., "#RRGGBB" or "RRGGBB").

    Returns:
        Tuple[int, int, int]: A tuple of integers representing the RGB values.

    Raises:
        ValueError: If the input string is not a valid hex color.

    Examples:
        >>> hex_to_rgb("#FF0000")
        (255, 0, 0)
        >>> hex_to_rgb("00FF00")
        (0, 255, 0)
    """
    hex_color = hex_color.lstrip("#")
    if len(hex_color) != 6:
        raise ValueError("Invalid hex color format. Expected 6 characters.")
    return (int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16))


def rgb_to_hex(rgb: Tuple[int, int, int]) -> str:
    """
    Convert an RGB tuple to a hex color string.

    Args:
        rgb (Tuple[int, int, int]): A tuple of integers representing the RGB values.

    Returns:
        str: A hex color string (e.g., "#RRGGBB").

    Raises:
        ValueError: If the RGB values are not within the valid range (0-255).

    Examples:
        >>> rgb_to_hex((255, 0, 0))
        "#ff0000"
        >>> rgb_to_hex((0, 255, 0))
        "#00ff00"
    """
    if any(not 0 <= value <= 255 for value in rgb):
        raise ValueError("RGB values must be between 0 and 255.")
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])


def rgba_to_rgba_int(rgba: Tuple[int, int, int, int]) -> int:
    """
    Convert an RGBA tuple to a 32-bit integer.

    Args:
        rgba (Tuple[int, int, int, int]): A tuple of integers representing the RGBA values.

    Returns:
        int: A 32-bit integer representing the RGBA color.

    Raises:
        ValueError: If the RGBA values are not within the valid range (0-255).

    Notes:
        The function assumes a specific byte order (RGBA) for the 32-bit integer.
        This may not be portable across all systems.

    Examples:
        >>> rgba_to_rgba_int((255, 0, 0, 255))
        4278190080
    """
    if any(not 0 <= value <= 255 for value in rgba):
        raise ValueError("RGBA values must be between 0 and 255.")
    r, g, b, a = rgba
    return (a << 24) | (r << 16) | (g << 8) | b

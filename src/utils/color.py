"""
Utility functions for color manipulation and conversion.
"""


def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    """
    Convert a hex color string to an RGB tuple.

    Args:
        hex_color: A hex color string (e.g., "#RRGGBB" or "RRGGBB").

    Returns:
        A tuple of integers representing the RGB values.
    """
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb: tuple[int, int, int]) -> str:
    """
    Convert an RGB tuple to a hex color string.

    Args:
        rgb: A tuple of integers representing the RGB values.

    Returns:
        A hex color string (e.g., "#RRGGBB").
    """
    return "#{:02x}{:02x}{:02x}".format(*rgb)


def rgba_to_rgba_int(rgba: tuple[int, int, int, int]) -> int:
    """
    Convert an RGBA tuple to a 32-bit integer.

    Args:
        rgba: A tuple of integers representing the RGBA values.

    Returns:
        A 32-bit integer representing the RGBA color.
    """
    r, g, b, a = rgba
    return (a << 24) | (r << 16) | (g << 8) | b

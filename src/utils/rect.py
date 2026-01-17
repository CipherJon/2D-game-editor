"""
Utility functions and classes for handling rectangles and related operations.

This module provides a simple rectangle class and utility functions for
manipulating rectangles, such as checking for intersections, containment,
and performing transformations.
"""

from typing import Optional


class Rect:
    """
    A simple rectangle class to represent a rectangular area with x, y, width, and height.

    Attributes:
        x (float): The x-coordinate of the top-left corner of the rectangle.
        y (float): The y-coordinate of the top-left corner of the rectangle.
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    """

    def __init__(self, x: float, y: float, width: float, height: float):
        """
        Initialize the rectangle with the given coordinates and dimensions.

        Args:
            x (float): The x-coordinate of the top-left corner of the rectangle.
            y (float): The y-coordinate of the top-left corner of the rectangle.
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.

        Raises:
            ValueError: If the width or height is negative.
        """
        if width < 0 or height < 0:
            raise ValueError("Width and height must be non-negative.")
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def contains(self, point_x: float, point_y: float) -> bool:
        """
        Check if the rectangle contains the given point.

        Args:
            point_x (float): The x-coordinate of the point to check.
            point_y (float): The y-coordinate of the point to check.

        Returns:
            bool: True if the point is inside the rectangle, False otherwise.
        """
        return (
            self.x <= point_x <= self.x + self.width
            and self.y <= point_y <= self.y + self.height
        )

    def intersects(self, other: "Rect") -> bool:
        """
        Check if this rectangle intersects with another rectangle.

        Args:
            other (Rect): The other rectangle to check for intersection.

        Returns:
            bool: True if the rectangles intersect, False otherwise.
        """
        return (
            self.x < other.x + other.width
            and self.x + self.width > other.x
            and self.y < other.y + other.height
            and self.y + self.height > other.y
        )

    def inflate(self, dx: float, dy: float) -> None:
        """
        Inflate the rectangle by the specified amounts.

        Args:
            dx (float): The amount to inflate the rectangle horizontally.
            dy (float): The amount to inflate the rectangle vertically.

        Raises:
            ValueError: If inflating the rectangle would result in negative width or height.
        """
        new_width = self.width + 2 * dx
        new_height = self.height + 2 * dy
        if new_width < 0 or new_height < 0:
            raise ValueError(
                "Inflating the rectangle would result in negative dimensions."
            )
        self.x -= dx
        self.y -= dy
        self.width = new_width
        self.height = new_height

    def deflate(self, dx: float, dy: float) -> None:
        """
        Deflate the rectangle by the specified amounts.

        Args:
            dx (float): The amount to deflate the rectangle horizontally.
            dy (float): The amount to deflate the rectangle vertically.

        Raises:
            ValueError: If deflating the rectangle would result in negative width or height.
        """
        new_width = self.width - 2 * dx
        new_height = self.height - 2 * dy
        if new_width < 0 or new_height < 0:
            raise ValueError(
                "Deflating the rectangle would result in negative dimensions."
            )
        self.x += dx
        self.y += dy
        self.width = new_width
        self.height = new_height

    def union(self, other: "Rect") -> "Rect":
        """
        Combine this rectangle with another rectangle to form the smallest rectangle that contains both.

        Args:
            other (Rect): The other rectangle to combine with.

        Returns:
            Rect: The smallest rectangle that contains both rectangles.
        """
        x = min(self.x, other.x)
        y = min(self.y, other.y)
        width = max(self.x + self.width, other.x + other.width) - x
        height = max(self.y + self.height, other.y + other.height) - y
        return Rect(x, y, width, height)

    def intersection(self, other: "Rect") -> Optional["Rect"]:
        """
        Calculate the intersection of this rectangle with another rectangle.

        Args:
            other (Rect): The other rectangle to intersect with.

        Returns:
            Optional[Rect]: The intersection rectangle, or None if the rectangles do not intersect.
        """
        if not self.intersects(other):
            return None
        x = max(self.x, other.x)
        y = max(self.y, other.y)
        width = min(self.x + self.width, other.x + other.width) - x
        height = min(self.y + self.height, other.y + other.height) - y
        return Rect(x, y, width, height)

    def __repr__(self) -> str:
        """
        Return a string representation of the rectangle.

        Returns:
            str: A string representation of the rectangle.
        """
        return f"Rect(x={self.x}, y={self.y}, width={self.width}, height={self.height})"

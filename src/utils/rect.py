"""
Utility functions and classes for handling rectangles and related operations.
"""


class Rect:
    """
    A simple rectangle class to represent a rectangular area with x, y, width, and height.
    """

    def __init__(self, x: float, y: float, width: float, height: float):
        """
        Initialize the rectangle with the given coordinates and dimensions.

        Args:
            x (float): The x-coordinate of the top-left corner of the rectangle.
            y (float): The y-coordinate of the top-left corner of the rectangle.
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
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

    def __repr__(self) -> str:
        """
        Return a string representation of the rectangle.

        Returns:
            str: A string representation of the rectangle.
        """
        return f"Rect(x={self.x}, y={self.y}, width={self.width}, height={self.height})"

# camera.py
"""
Camera module for handling view transformations in the 2D game editor.

This module provides a 2D camera that handles view transformations, zooming, and panning.
The camera can be used to navigate and view different parts of a scene.
"""

from typing import Optional, Tuple


class Camera:
    """
    A 2D camera that handles view transformations, zooming, and panning.

    Attributes:
        x (float): The x-coordinate of the camera's position.
        y (float): The y-coordinate of the camera's position.
        zoom (float): The zoom level of the camera.
        min_zoom (float): The minimum zoom level of the camera.
        max_zoom (float): The maximum zoom level of the camera.
        bounds (Optional[Tuple[float, float, float, float]]): The bounds of the camera's movement.
    """

    def __init__(
        self,
        x: float = 0.0,
        y: float = 0.0,
        zoom: float = 1.0,
        min_zoom: float = 0.1,
        max_zoom: float = 5.0,
        bounds: Optional[Tuple[float, float, float, float]] = None,
    ):
        """
        Initialize the camera with a position, zoom level, and optional bounds.

        Args:
            x (float): The x-coordinate of the camera's position.
            y (float): The y-coordinate of the camera's position.
            zoom (float): The zoom level of the camera.
            min_zoom (float): The minimum zoom level of the camera.
            max_zoom (float): The maximum zoom level of the camera.
            bounds (Optional[Tuple[float, float, float, float]]): The bounds of the camera's movement.

        Raises:
            ValueError: If min_zoom is greater than max_zoom.
        """
        if min_zoom > max_zoom:
            raise ValueError("min_zoom must be less than or equal to max_zoom.")
        self.x = x
        self.y = y
        self.zoom = zoom
        self.min_zoom = min_zoom
        self.max_zoom = max_zoom
        self.bounds = bounds

    def translate(self, dx: float, dy: float) -> None:
        """
        Move the camera by the specified offsets.

        Args:
            dx (float): The change in the x-coordinate.
            dy (float): The change in the y-coordinate.

        Raises:
            ValueError: If translating the camera would move it outside the bounds.
        """
        new_x = self.x + dx
        new_y = self.y + dy
        if self.bounds:
            if not (
                self.bounds[0] <= new_x <= self.bounds[2]
                and self.bounds[1] <= new_y <= self.bounds[3]
            ):
                raise ValueError(
                    "Translating the camera would move it outside the bounds."
                )
        self.x = new_x
        self.y = new_y

    def set_position(self, x: float, y: float) -> None:
        """
        Set the camera's position to the specified coordinates.

        Args:
            x (float): The new x-coordinate of the camera's position.
            y (float): The new y-coordinate of the camera's position.

        Raises:
            ValueError: If setting the position would move the camera outside the bounds.
        """
        if self.bounds:
            if not (
                self.bounds[0] <= x <= self.bounds[2]
                and self.bounds[1] <= y <= self.bounds[3]
            ):
                raise ValueError(
                    "Setting the position would move the camera outside the bounds."
                )
        self.x = x
        self.y = y

    def set_zoom(self, zoom: float) -> None:
        """
        Set the camera's zoom level.

        Args:
            zoom (float): The new zoom level of the camera.

        Raises:
            ValueError: If the zoom level is outside the allowed range.
        """
        if zoom < self.min_zoom or zoom > self.max_zoom:
            raise ValueError(
                f"Zoom level must be between {self.min_zoom} and {self.max_zoom}."
            )
        self.zoom = zoom

    def apply_transform(self, x: float, y: float) -> Tuple[float, float]:
        """
        Apply the camera's transformation to the given coordinates.

        Args:
            x (float): The x-coordinate to transform.
            y (float): The y-coordinate to transform.

        Returns:
            Tuple[float, float]: The transformed coordinates.
        """
        transformed_x = (x - self.x) * self.zoom
        transformed_y = (y - self.y) * self.zoom
        return transformed_x, transformed_y

    def screen_to_world(self, screen_x: float, screen_y: float) -> Tuple[float, float]:
        """
        Convert screen coordinates to world coordinates.

        Args:
            screen_x (float): The x-coordinate in screen space.
            screen_y (float): The y-coordinate in screen space.

        Returns:
            Tuple[float, float]: The corresponding world coordinates.
        """
        world_x = (screen_x / self.zoom) + self.x
        world_y = (screen_y / self.zoom) + self.y
        return world_x, world_y

    def set_bounds(self, bounds: Optional[Tuple[float, float, float, float]]) -> None:
        """
        Set the bounds of the camera's movement.

        Args:
            bounds (Optional[Tuple[float, float, float, float]]): The bounds of the camera's movement.

        Raises:
            ValueError: If the bounds are invalid (e.g., min_x > max_x or min_y > max_y).
        """
        if bounds:
            if bounds[0] > bounds[2] or bounds[1] > bounds[3]:
                raise ValueError(
                    "Invalid bounds: min_x must be less than max_x and min_y must be less than max_y."
                )
        self.bounds = bounds

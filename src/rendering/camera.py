# camera.py
"""
Camera module for handling view transformations in the 2D game editor.
"""


class Camera:
    """
    A 2D camera that handles view transformations, zooming, and panning.
    """

    def __init__(self, x: float = 0.0, y: float = 0.0, zoom: float = 1.0):
        """
        Initialize the camera with a position and zoom level.

        Args:
            x (float): The x-coordinate of the camera's position.
            y (float): The y-coordinate of the camera's position.
            zoom (float): The zoom level of the camera.
        """
        self.x = x
        self.y = y
        self.zoom = zoom

    def translate(self, dx: float, dy: float):
        """
        Move the camera by the specified offsets.

        Args:
            dx (float): The change in the x-coordinate.
            dy (float): The change in the y-coordinate.
        """
        self.x += dx
        self.y += dy

    def set_position(self, x: float, y: float):
        """
        Set the camera's position to the specified coordinates.

        Args:
            x (float): The new x-coordinate of the camera's position.
            y (float): The new y-coordinate of the camera's position.
        """
        self.x = x
        self.y = y

    def set_zoom(self, zoom: float):
        """
        Set the camera's zoom level.

        Args:
            zoom (float): The new zoom level of the camera.
        """
        self.zoom = max(0.1, zoom)  # Prevent zoom from becoming too small

    def apply_transform(self, x: float, y: float) -> tuple[float, float]:
        """
        Apply the camera's transformation to the given coordinates.

        Args:
            x (float): The x-coordinate to transform.
            y (float): The y-coordinate to transform.

        Returns:
            tuple[float, float]: The transformed coordinates.
        """
        transformed_x = (x - self.x) * self.zoom
        transformed_y = (y - self.y) * self.zoom
        return transformed_x, transformed_y

    def screen_to_world(self, screen_x: float, screen_y: float) -> tuple[float, float]:
        """
        Convert screen coordinates to world coordinates.

        Args:
            screen_x (float): The x-coordinate in screen space.
            screen_y (float): The y-coordinate in screen space.

        Returns:
            tuple[float, float]: The corresponding world coordinates.
        """
        world_x = (screen_x / self.zoom) + self.x
        world_y = (screen_y / self.zoom) + self.y
        return world_x, world_y

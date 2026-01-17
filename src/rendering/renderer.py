"""
High-level rendering helper for the 2D game editor.
This module provides utilities for drawing scenes, layers, and other visual elements.

This module includes functions for rendering scenes, layers, and grids, as well as
clearing the screen and managing camera offsets.
"""

from typing import Tuple

import pygame

from ..scene.layer import Layer
from ..scene.scene import Scene


class Renderer:
    """
    A high-level rendering helper for drawing scenes, layers, and other visual elements.

    Attributes:
        surface (pygame.Surface): The target surface to render to.
        camera_offset (Tuple[int, int]): The camera offset for scrolling.
    """

    def __init__(self, surface: pygame.Surface):
        """
        Initialize the renderer with a target surface.

        Args:
            surface (pygame.Surface): The target surface to render to.

        Raises:
            ValueError: If the surface is not a valid pygame.Surface.
        """
        if not isinstance(surface, pygame.Surface):
            raise ValueError("Invalid surface provided for renderer.")
        self.surface = surface
        self.camera_offset = (0, 0)

    def set_camera_offset(self, offset: Tuple[int, int]) -> None:
        """
        Set the camera offset for scrolling.

        Args:
            offset (Tuple[int, int]): The (x, y) offset for the camera.

        Raises:
            ValueError: If the offset is not a tuple of two integers.
        """
        if not isinstance(offset, tuple) or len(offset) != 2:
            raise ValueError("Offset must be a tuple of two integers.")
        self.camera_offset = offset

    def render_scene(self, scene: Scene) -> None:
        """
        Render the entire scene, including all layers.

        Args:
            scene (Scene): The scene to render.

        Raises:
            ValueError: If the scene is not a valid Scene object.
        """
        if not isinstance(scene, Scene):
            raise ValueError("Invalid scene provided for rendering.")
        for layer in scene.layers:
            self.render_layer(layer)

    def render_layer(self, layer: Layer) -> None:
        """
        Render a single layer.

        Args:
            layer (Layer): The layer to render.

        Raises:
            ValueError: If the layer is not a valid Layer object.
        """
        if not isinstance(layer, Layer):
            raise ValueError("Invalid layer provided for rendering.")
        if not layer.visible:
            return

        # Apply camera offset
        offset_x, offset_y = self.camera_offset

    def draw_grid(
        self, tile_size: int, grid_color: Tuple[int, int, int] = (50, 50, 50)
    ) -> None:
        """
        Draw a grid to assist with tile placement.

        Args:
            tile_size (int): The size of each grid cell.
            grid_color (Tuple[int, int, int]): The color of the grid lines.

        Raises:
            ValueError: If tile_size is not a positive integer.
        """
        if tile_size <= 0:
            raise ValueError("Tile size must be a positive integer.")
        width, height = self.surface.get_size()
        offset_x, offset_y = self.camera_offset

        # Adjust grid lines to align with the camera offset
        start_x = offset_x % tile_size
        start_y = offset_y % tile_size

        for x in range(start_x, width, tile_size):
            pygame.draw.line(self.surface, grid_color, (x, 0), (x, height), 1)

        for y in range(start_y, height, tile_size):
            pygame.draw.line(self.surface, grid_color, (0, y), (width, y), 1)

    def clear(self, color: Tuple[int, int, int] = (0, 0, 0)) -> None:
        """
        Clear the surface with a specified color.

        Args:
            color (Tuple[int, int, int]): The color to fill the surface with.

        Raises:
            ValueError: If the color is not a valid RGB tuple.
        """
        if not isinstance(color, tuple) or len(color) != 3:
            raise ValueError("Color must be a tuple of three integers.")
        self.surface.fill(color)

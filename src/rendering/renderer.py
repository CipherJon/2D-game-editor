# renderer.py
"""
High-level rendering helper for the 2D game editor.
This module provides utilities for drawing scenes, layers, and other visual elements.
"""

from typing import Optional, Tuple

import pygame

from ..core.types import Color
from ..scene.layer import Layer
from ..scene.scene import Scene


class Renderer:
    """
    A high-level rendering helper for drawing scenes, layers, and other visual elements.
    """

    def __init__(self, surface: pygame.Surface):
        """
        Initialize the renderer with a target surface.

        Args:
            surface (pygame.Surface): The target surface to render to.
        """
        self.surface = surface
        self.camera_offset = (0, 0)  # Camera offset for scrolling

    def set_camera_offset(self, offset: Tuple[int, int]):
        """
        Set the camera offset for scrolling.

        Args:
            offset (Tuple[int, int]): The (x, y) offset for the camera.
        """
        self.camera_offset = offset

    def render_scene(self, scene: Scene):
        """
        Render the entire scene, including all layers.

        Args:
            scene (Scene): The scene to render.
        """
        for layer in scene.layers:
            self.render_layer(layer)

    def render_layer(self, layer: Layer):
        """
        Render a single layer.

        Args:
            layer (Layer): The layer to render.
        """
        if not layer.visible:
            return

        # Apply camera offset
        offset_x, offset_y = self.camera_offset

        # Draw tiles or entities in the layer
        for tile in layer.tiles:
            tile_rect = pygame.Rect(
                tile.x * layer.tile_size - offset_x,
                tile.y * layer.tile_size - offset_y,
                layer.tile_size,
                layer.tile_size,
            )
            pygame.draw.rect(self.surface, tile.color, tile_rect)

    def draw_grid(self, tile_size: int, grid_color: Color = (50, 50, 50)):
        """
        Draw a grid to assist with tile placement.

        Args:
            tile_size (int): The size of each grid cell.
            grid_color (Color): The color of the grid lines.
        """
        width, height = self.surface.get_size()
        offset_x, offset_y = self.camera_offset

        # Adjust grid lines to align with the camera offset
        start_x = offset_x % tile_size
        start_y = offset_y % tile_size

        for x in range(start_x, width, tile_size):
            pygame.draw.line(self.surface, grid_color, (x, 0), (x, height), 1)

        for y in range(start_y, height, tile_size):
            pygame.draw.line(self.surface, grid_color, (0, y), (width, y), 1)

    def clear(self, color: Color = (0, 0, 0)):
        """
        Clear the surface with a specified color.

        Args:
            color (Color): The color to fill the surface with.
        """
        self.surface.fill(color)

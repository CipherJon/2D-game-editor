# grid_renderer.py
"""
Module for rendering grid lines and related functionality.
"""

from typing import Optional, Tuple

import pygame


class GridRenderer:
    """
    Handles the rendering of grid lines for the editor.
    """

    def __init__(
        self, cell_size: int = 16, grid_color: Tuple[int, int, int] = (100, 100, 100)
    ):
        """
        Initialize the GridRenderer.

        Args:
            cell_size: Size of each grid cell in pixels.
            grid_color: Color of the grid lines as an RGB tuple.
        """
        self.cell_size = cell_size
        self.grid_color = grid_color

    def render(
        self, surface: pygame.Surface, camera_offset: Tuple[int, int] = (0, 0)
    ) -> None:
        """
        Render the grid lines on the given surface.

        Args:
            surface: The Pygame surface to render the grid on.
            camera_offset: The offset of the camera to adjust grid rendering.
        """
        width, height = surface.get_size()
        start_x = (camera_offset[0] % self.cell_size) - self.cell_size
        start_y = (camera_offset[1] % self.cell_size) - self.cell_size

        for x in range(start_x, width, self.cell_size):
            pygame.draw.line(surface, self.grid_color, (x, 0), (x, height))

        for y in range(start_y, height, self.cell_size):
            pygame.draw.line(surface, self.grid_color, (0, y), (width, y))

    def set_cell_size(self, cell_size: int) -> None:
        """
        Set the size of the grid cells.

        Args:
            cell_size: New size of the grid cells in pixels.
        """
        self.cell_size = cell_size

    def set_grid_color(self, grid_color: Tuple[int, int, int]) -> None:
        """
        Set the color of the grid lines.

        Args:
            grid_color: New color of the grid lines as an RGB tuple.
        """
        self.grid_color = grid_color

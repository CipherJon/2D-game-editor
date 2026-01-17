# gizmos.py
"""
Gizmos module for rendering transform and selection gizmos in the 2D game editor.

This module provides utilities for drawing interactive gizmos that assist with
transformations, selections, and other visual aids in the editor.
"""

from typing import Tuple

import pygame


class Gizmos:
    """
    Handles the rendering of interactive gizmos for transforms, selections, and other visual aids.

    Attributes:
        color (Tuple[int, int, int]): The default color for gizmos.
        line_width (int): The default line width for gizmos.
    """

    def __init__(self, color: Tuple[int, int, int] = (255, 0, 0), line_width: int = 2):
        """
        Initialize the Gizmos class with default color and line width.

        Args:
            color (Tuple[int, int, int], optional): The default color for gizmos. Defaults to (255, 0, 0).
            line_width (int, optional): The default line width for gizmos. Defaults to 2.
        """
        self.color = color
        self.line_width = line_width

    def draw_transform_gizmo(
        self,
        surface: pygame.Surface,
        position: Tuple[float, float],
        rotation: float = 0.0,
        scale: Tuple[float, float] = (1.0, 1.0),
    ) -> None:
        """
        Draw a transform gizmo at the specified position, rotation, and scale.

        Args:
            surface (pygame.Surface): The surface to draw the gizmo on.
            position (Tuple[float, float]): The (x, y) position of the gizmo.
            rotation (float, optional): The rotation angle of the gizmo in degrees. Defaults to 0.0.
            scale (Tuple[float, float], optional): The (scale_x, scale_y) of the gizmo. Defaults to (1.0, 1.0).

        Example:
            >>> gizmos = Gizmos()
            >>> gizmos.draw_transform_gizmo(screen, (100, 100), 45.0, (1.5, 1.5))
        """
        # Draw a circle at the position
        pygame.draw.circle(
            surface,
            self.color,
            (int(position[0]), int(position[1])),
            10,
            self.line_width,
        )

        # Draw lines for rotation and scale
        end_x = position[0] + 50 * scale[0]
        end_y = position[1] + 50 * scale[1]
        pygame.draw.line(surface, self.color, position, (end_x, end_y), self.line_width)

    def draw_selection_gizmo(
        self,
        surface: pygame.Surface,
        rect: Tuple[float, float, float, float],
    ) -> None:
        """
        Draw a selection gizmo around the specified rectangle.

        Args:
            surface (pygame.Surface): The surface to draw the gizmo on.
            rect (Tuple[float, float, float, float]): The (x, y, width, height) of the selection rectangle.

        Example:
            >>> gizmos = Gizmos()
            >>> gizmos.draw_selection_gizmo(screen, (100, 100, 200, 150))
        """
        # Draw a rectangle around the selection
        pygame.draw.rect(surface, self.color, rect, self.line_width)

    def draw_grid_gizmo(
        self,
        surface: pygame.Surface,
        cell_size: int,
        grid_color: Tuple[int, int, int] = (100, 100, 100),
    ) -> None:
        """
        Draw a grid gizmo with the specified cell size and color.

        Args:
            surface (pygame.Surface): The surface to draw the gizmo on.
            cell_size (int): The size of each grid cell.
            grid_color (Tuple[int, int, int], optional): The RGB color of the grid lines. Defaults to (100, 100, 100).

        Example:
            >>> gizmos = Gizmos()
            >>> gizmos.draw_grid_gizmo(screen, 32, (150, 150, 150))
        """
        width, height = surface.get_size()

        # Draw vertical lines
        for x in range(0, width, cell_size):
            pygame.draw.line(surface, grid_color, (x, 0), (x, height), 1)

        # Draw horizontal lines
        for y in range(0, height, cell_size):
            pygame.draw.line(surface, grid_color, (0, y), (width, y), 1)

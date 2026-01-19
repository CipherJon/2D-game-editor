import pygame

from ...ui.theme import Theme
from ...utils.color import hex_to_rgb

"""
Tile Palette Panel
==================

A panel for managing and selecting tiles in the editor.
"""


class TilePalettePanel:
    def __init__(self):
        """Initialize the tile palette panel."""
        self.tiles = []
        self.selected_tile = None
        self.theme = Theme()
        self.tile_size = 32
        self.padding = 10
        self.margin = 10
        self.panel_width = 200
        self.panel_height = 300
        self.panel_x = 10
        self.panel_y = 10

    def add_tile(self, tile):
        """Add a tile to the palette."""
        self.tiles.append(tile)

    def remove_tile(self, tile):
        """Remove a tile from the palette."""
        if tile in self.tiles:
            self.tiles.remove(tile)

    def select_tile(self, tile):
        """Select a tile from the palette."""
        self.selected_tile = tile

    def clear_selection(self):
        """Clear the selected tile."""
        self.selected_tile = None

    def render(self, screen):
        """
        Render the tile palette.

        Args:
            screen (pygame.Surface): The screen surface to render to.
        """
        # Draw the panel background
        panel_bg_color = hex_to_rgb(self.theme.get_color("panel_bg"))
        pygame.draw.rect(
            screen,
            panel_bg_color,
            (self.panel_x, self.panel_y, self.panel_width, self.panel_height),
        )

        # Draw the panel border
        border_color = hex_to_rgb(self.theme.get_color("border"))
        pygame.draw.rect(
            screen,
            border_color,
            (self.panel_x, self.panel_y, self.panel_width, self.panel_height),
            2,
        )

        # Draw the panel label
        font = pygame.font.SysFont(None, 24)
        text_color = hex_to_rgb(self.theme.get_color("text"))
        label = font.render("Tile Palette", True, text_color)
        screen.blit(label, (self.panel_x + self.padding, self.panel_y + self.padding))

        # Draw the tiles
        tiles_per_row = (self.panel_width - 2 * self.padding) // self.tile_size
        for i, tile in enumerate(self.tiles):
            row = i // tiles_per_row
            col = i % tiles_per_row
            tile_x = self.panel_x + self.padding + col * self.tile_size
            tile_y = self.panel_y + self.padding + 30 + row * self.tile_size

            # Draw the tile
            if isinstance(tile, pygame.Surface):
                screen.blit(tile, (tile_x, tile_y))
            else:
                pygame.draw.rect(
                    screen,
                    (200, 200, 200),
                    (tile_x, tile_y, self.tile_size, self.tile_size),
                )

            # Highlight the selected tile
            if tile == self.selected_tile:
                highlight_color = hex_to_rgb(self.theme.get_color("primary"))
                pygame.draw.rect(
                    screen,
                    highlight_color,
                    (tile_x, tile_y, self.tile_size, self.tile_size),
                    2,
                )

    def handle_event(self, event):
        """
        Handles events for the tile palette panel.

        Args:
            event (pygame.event.Event): The pygame event.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if (
                    self.panel_x <= mouse_x <= self.panel_x + self.panel_width
                    and self.panel_y <= mouse_y <= self.panel_y + self.panel_height
                ):
                    # Check if a tile was clicked
                    tiles_per_row = (
                        self.panel_width - 2 * self.padding
                    ) // self.tile_size
                    for i, tile in enumerate(self.tiles):
                        row = i // tiles_per_row
                        col = i % tiles_per_row
                        tile_x = self.panel_x + self.padding + col * self.tile_size
                        tile_y = self.panel_y + self.padding + 30 + row * self.tile_size
                        if (
                            tile_x <= mouse_x <= tile_x + self.tile_size
                            and tile_y <= mouse_y <= tile_y + self.tile_size
                        ):
                            self.selected_tile = tile
                            break

    def update(self, delta_time):
        """
        Updates the tile palette panel.

        Args:
            delta_time (float): Time elapsed since the last frame.
        """
        pass

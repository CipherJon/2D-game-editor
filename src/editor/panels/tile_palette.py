import pygame

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
        # Draw a simple rectangle to represent the tile palette
        pygame.draw.rect(screen, (100, 100, 100), (10, 10, 200, 100))
        # Draw a label for the tile palette
        font = pygame.font.SysFont(None, 24)
        label = font.render("Tile Palette", True, (255, 255, 255))
        screen.blit(label, (20, 20))

    def handle_event(self, event):
        """
        Handles events for the tile palette panel.

        Args:
            event (pygame.event.Event): The pygame event.
        """
        pass

    def update(self, delta_time):
        """
        Updates the tile palette panel.

        Args:
            delta_time (float): Time elapsed since the last frame.
        """
        pass

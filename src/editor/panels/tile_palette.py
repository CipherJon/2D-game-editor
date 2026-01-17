```python
"""
Tile Palette Panel
==================

A panel for managing and selecting tiles in the editor.
"""

class TilePalette:
    def __init__(self):
        """Initialize the tile palette."""
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

    def render(self):
        """Render the tile palette."""
        print("Rendering Tile Palette")
        for tile in self.tiles:
            print(f"Tile: {tile}")
        if self.selected_tile:
            print(f"Selected Tile: {self.selected_tile}")

"""
Tilemap module for the 2D game editor.
Handles tilemap data, rendering, and manipulation.
"""

from typing import Dict, List, Optional, Tuple

import pygame

from ..assets.asset_manager import AssetManager
from ..core.types import Point
from .layer import Layer


class Tile:
    """Represents a single tile in the tilemap."""

    def __init__(self, tile_id: int, position: Point, tileset: str = "default"):
        self.tile_id = tile_id
        self.position = position
        self.tileset = tileset

    def __repr__(self):
        return f"Tile(id={self.tile_id}, pos={self.position}, tileset={self.tileset})"


class Tilemap:
    """Manages a grid of tiles for a 2D game level."""

    def __init__(
        self, width: int, height: int, tile_width: int = 32, tile_height: int = 32
    ):
        self.width = width
        self.height = height
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.tiles: Dict[Tuple[int, int], Tile] = {}
        self.layers: List[Layer] = []
        self.tilesets: Dict[str, pygame.Surface] = {}

    def add_tile(self, x: int, y: int, tile_id: int, tileset: str = "default"):
        """Add or update a tile at the specified position."""
        position = {"x": x, "y": y}
        self.tiles[(x, y)] = Tile(tile_id, position, tileset)

    def remove_tile(self, x: int, y: int):
        """Remove a tile at the specified position."""
        if (x, y) in self.tiles:
            del self.tiles[(x, y)]

    def get_tile(self, x: int, y: int) -> Optional[Tile]:
        """Get the tile at the specified position."""
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            raise IndexError("Tile coordinates out of bounds")
        return self.tiles.get((x, y))

    def clear(self):
        """Clear all tiles from the tilemap."""
        self.tiles.clear()

    def load_tileset(self, name: str, image_path: str, asset_manager: AssetManager):
        """Load a tileset image and store it for rendering."""
        tileset_image = asset_manager.load_image(image_path)
        self.tilesets[name] = tileset_image

    def render(self, surface: pygame.Surface, camera_offset: Point):
        """Render the tilemap to the given surface with camera offset."""
        for (x, y), tile in self.tiles.items():
            tileset = self.tilesets.get(tile.tileset)
            if tileset:
                # Calculate source rectangle for the tile in the tileset
                tile_x = (
                    tile.tile_id % (tileset.get_width() // self.tile_size)
                ) * self.tile_size
                tile_y = (
                    tile.tile_id // (tileset.get_width() // self.tile_size)
                ) * self.tile_size
                src_rect = pygame.Rect(tile_x, tile_y, self.tile_size, self.tile_size)

                # Calculate destination rectangle with camera offset
                dest_x = x * self.tile_size - camera_offset.x
                dest_y = y * self.tile_size - camera_offset.y
                dest_rect = pygame.Rect(dest_x, dest_y, self.tile_size, self.tile_size)

                surface.blit(tileset, dest_rect, src_rect)

    def to_dict(self) -> Dict:
        """Serialize the tilemap to a dictionary for saving."""
        return {
            "width": self.width,
            "height": self.height,
            "tile_size": self.tile_size,
            "tiles": [
                {"x": x, "y": y, "tile_id": tile.tile_id, "tileset": tile.tileset}
                for (x, y), tile in self.tiles.items()
            ],
            "layers": [layer.to_dict() for layer in self.layers],
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "Tilemap":
        """Deserialize a tilemap from a dictionary."""
        tilemap = cls(data["width"], data["height"], data["tile_size"])
        for tile_data in data["tiles"]:
            tilemap.add_tile(
                tile_data["x"],
                tile_data["y"],
                tile_data["tile_id"],
                tile_data["tileset"],
            )
        return tilemap

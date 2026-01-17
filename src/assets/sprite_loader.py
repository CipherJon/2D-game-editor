# Sprite Loader Module
# This module handles the loading and management of sprite assets for the 2D game editor.

from pathlib import Path
from typing import Dict, Optional

import pygame


class SpriteLoader:
    """
    A class to load and manage sprite assets.
    """

    def __init__(self):
        """
        Initialize the SpriteLoader.
        """
        self.sprites: Dict[str, pygame.Surface] = {}
        self.sprite_paths: Dict[str, Path] = {}

    def load_sprite(self, path: str, name: str) -> bool:
        """
        Load a sprite from the given path and store it with the specified name.

        Args:
            path (str): The path to the sprite file.
            name (str): The name to associate with the sprite.

        Returns:
            bool: True if the sprite was loaded successfully, False otherwise.
        """
        try:
            sprite_path = Path(path)
            if not sprite_path.exists():
                print(f"Error: Sprite file not found at {path}")
                return False

            sprite = pygame.image.load(path).convert_alpha()
            self.sprites[name] = sprite
            self.sprite_paths[name] = sprite_path
            return True
        except Exception as e:
            print(f"Error loading sprite: {e}")
            return False

    def get_sprite(self, name: str) -> Optional[pygame.Surface]:
        """
        Retrieve a sprite by its name.

        Args:
            name (str): The name of the sprite to retrieve.

        Returns:
            Optional[pygame.Surface]: The sprite if found, None otherwise.
        """
        return self.sprites.get(name)

    def unload_sprite(self, name: str) -> bool:
        """
        Unload a sprite by its name.

        Args:
            name (str): The name of the sprite to unload.

        Returns:
            bool: True if the sprite was unloaded successfully, False otherwise.
        """
        if name in self.sprites:
            del self.sprites[name]
            del self.sprite_paths[name]
            return True
        return False

    def clear_sprites(self) -> None:
        """
        Clear all loaded sprites.
        """
        self.sprites.clear()
        self.sprite_paths.clear()

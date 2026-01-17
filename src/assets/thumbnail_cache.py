# thumbnail_cache.py
"""
Thumbnail cache management for assets.
Handles generating, storing, and retrieving thumbnails for sprites and tiles.
"""

import hashlib
import os
from typing import Dict, Optional

import pygame
from PIL import Image, ImageOps


class ThumbnailCache:
    """
    Manages a cache of thumbnails for assets to improve performance.
    Thumbnails are stored in a dedicated directory and referenced by a hash of their source.
    """

    def __init__(self, cache_dir: str = "resources/cache/thumbnails"):
        """
        Initialize the thumbnail cache.

        Args:
            cache_dir: Directory where thumbnails will be stored.
        """
        self.cache_dir = cache_dir
        self.thumbnail_size = (64, 64)  # Default thumbnail size
        self.cache: Dict[str, str] = {}  # Maps asset paths to thumbnail paths
        self._ensure_cache_dir_exists()

    def _ensure_cache_dir_exists(self) -> None:
        """Ensure the cache directory exists."""
        os.makedirs(self.cache_dir, exist_ok=True)

    def _generate_thumbnail_path(self, asset_path: str) -> str:
        """
        Generate a unique thumbnail path based on the asset path.

        Args:
            asset_path: Path to the source asset.

        Returns:
            Path where the thumbnail should be stored.
        """
        # Create a hash of the asset path to use as the filename
        hash_object = hashlib.md5(asset_path.encode())
        hex_digest = hash_object.hexdigest()
        return os.path.join(self.cache_dir, f"{hex_digest}.png")

    def get_thumbnail(self, asset_path: str) -> Optional[pygame.Surface]:
        """
        Retrieve a thumbnail for the given asset.

        Args:
            asset_path: Path to the source asset.

        Returns:
            Pygame Surface containing the thumbnail, or None if not found.
        """
        thumbnail_path = self._generate_thumbnail_path(asset_path)

        # Check if thumbnail exists in cache
        if os.path.exists(thumbnail_path):
            try:
                thumbnail = pygame.image.load(thumbnail_path)
                return thumbnail
            except pygame.error:
                print(f"Error loading thumbnail: {thumbnail_path}")
                return None

        return None

    def generate_and_cache_thumbnail(self, asset_path: str) -> Optional[pygame.Surface]:
        """
        Generate a thumbnail for the given asset and cache it.

        Args:
            asset_path: Path to the source asset.

        Returns:
            Pygame Surface containing the generated thumbnail, or None if generation failed.
        """
        try:
            # Load the original image
            original_image = Image.open(asset_path)

            # Create thumbnail
            thumbnail = ImageOps.fit(
                original_image, self.thumbnail_size, method=Image.Resampling.LANCZOS
            )

            # Save thumbnail to cache
            thumbnail_path = self._generate_thumbnail_path(asset_path)
            thumbnail.save(thumbnail_path)

            # Convert to pygame Surface for immediate use
            pygame_thumbnail = pygame.image.load(thumbnail_path)
            return pygame_thumbnail

        except Exception as e:
            print(f"Error generating thumbnail for {asset_path}: {e}")
            return None

    def clear_cache(self) -> None:
        """Clear all cached thumbnails."""
        for filename in os.listdir(self.cache_dir):
            file_path = os.path.join(self.cache_dir, filename)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")

        self.cache.clear()
        print("Thumbnail cache cleared.")

    def set_thumbnail_size(self, size: tuple[int, int]) -> None:
        """
        Set the size for generated thumbnails.

        Args:
            size: Tuple of (width, height) for thumbnails.
        """
        self.thumbnail_size = size

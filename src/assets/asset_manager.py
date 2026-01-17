"""
Asset Manager Module

This module provides functionality for managing game assets such as sprites, textures, and other resources.
"""

import os
from typing import Any, Dict, Optional


class AssetManager:
    """
    A class to manage game assets, including loading, storing, and retrieving assets.
    """

    def __init__(self):
        """
        Initialize the AssetManager with an empty asset dictionary.
        """
        self.assets: Dict[str, Any] = {}

    def load_asset(self, asset_id: str, asset_path: str) -> None:
        """
        Load an asset from the specified path and store it in the asset dictionary.

        Args:
            asset_id (str): A unique identifier for the asset.
            asset_path (str): The path to the asset file.

        Raises:
            FileNotFoundError: If the asset file does not exist.
            PermissionError: If the asset file cannot be read due to permission issues.
            Exception: For other errors during asset loading.
        """
        if not os.path.exists(asset_path):
            raise FileNotFoundError(f"Asset file not found: {asset_path}")

        try:
            # Placeholder for asset loading logic
            self.assets[asset_id] = asset_path
            print(f"Asset '{asset_id}' loaded from '{asset_path}'.")
        except PermissionError as e:
            raise PermissionError(f"Permission denied while loading asset: {e}")
        except Exception as e:
            raise Exception(f"Error loading asset: {e}")

    def get_asset(self, asset_id: str) -> Optional[Any]:
        """
        Retrieve an asset by its unique identifier.

        Args:
            asset_id (str): The unique identifier of the asset to retrieve.

        Returns:
            The asset associated with the given ID, or None if the asset does not exist.
        """
        return self.assets.get(asset_id)

    def unload_asset(self, asset_id: str) -> None:
        """
        Unload an asset by removing it from the asset dictionary.

        Args:
            asset_id (str): The unique identifier of the asset to unload.

        Raises:
            KeyError: If the asset ID does not exist.
        """
        if asset_id not in self.assets:
            raise KeyError(f"Asset '{asset_id}' not found.")

        del self.assets[asset_id]
        print(f"Asset '{asset_id}' unloaded.")

    def list_assets(self) -> list:
        """
        List all loaded assets.

        Returns:
            A list of all asset IDs currently loaded.
        """
        return list(self.assets.keys())

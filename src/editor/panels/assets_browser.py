"""
Assets Browser Panel

This module provides the AssetsBrowser class, which is responsible for displaying
and managing assets in the editor's UI. It allows users to browse, select, and
manage assets such as sprites, tiles, and other resources.
"""


class AssetsBrowser:
    """
    A panel for browsing and managing assets in the editor.

    Attributes:
        assets (list): A list of available assets.
        selected_asset (str): The currently selected asset.
    """

    def __init__(self):
        """
        Initializes the AssetsBrowser with default values.
        """
        self.assets = []
        self.selected_asset = None

    def load_assets(self, asset_paths):
        """
        Loads assets from the specified paths.

        Args:
            asset_paths (list): A list of paths to asset files.
        """
        self.assets = asset_paths
        print(f"Loaded {len(asset_paths)} assets.")

    def select_asset(self, asset_name):
        """
        Selects an asset for use in the editor.

        Args:
            asset_name (str): The name of the asset to select.
        """
        if asset_name in self.assets:
            self.selected_asset = asset_name
            print(f"Selected asset: {asset_name}")
        else:
            print(f"Asset {asset_name} not found.")

    def display(self):
        """
        Displays the assets browser panel in the UI.
        """
        print("Displaying Assets Browser Panel")
        print(f"Available Assets: {self.assets}")
        print(f"Selected Asset: {self.selected_asset}")

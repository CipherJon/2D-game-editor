"""
Test cases for the asset_manager.py module.
This module tests the functionality of the AssetManager class, including error handling.
"""

import os
import tempfile
import unittest

from src.assets.asset_manager import AssetManager


class TestAssetManager(unittest.TestCase):
    def setUp(self):
        self.asset_manager = AssetManager()
        self.temp_dir = tempfile.mkdtemp()
        self.test_asset_path = os.path.join(self.temp_dir, "test_asset.txt")
        with open(self.test_asset_path, "w") as f:
            f.write("Test asset content")

    def tearDown(self):
        # Clean up temporary files
        for file in os.listdir(self.temp_dir):
            os.remove(os.path.join(self.temp_dir, file))
        os.rmdir(self.temp_dir)

    def test_load_asset_valid(self):
        """Test loading a valid asset."""
        self.asset_manager.load_asset("test_asset", self.test_asset_path)
        self.assertEqual(
            self.asset_manager.get_asset("test_asset"), self.test_asset_path
        )

    def test_load_asset_invalid(self):
        """Test loading an invalid asset."""
        invalid_asset_path = os.path.join(self.temp_dir, "invalid_asset.txt")
        with self.assertRaises(FileNotFoundError):
            self.asset_manager.load_asset("invalid_asset", invalid_asset_path)

    def test_get_asset_valid(self):
        """Test retrieving a valid asset."""
        self.asset_manager.load_asset("test_asset", self.test_asset_path)
        asset = self.asset_manager.get_asset("test_asset")
        self.assertEqual(asset, self.test_asset_path)

    def test_get_asset_invalid(self):
        """Test retrieving an invalid asset."""
        asset = self.asset_manager.get_asset("nonexistent_asset")
        self.assertIsNone(asset)

    def test_unload_asset_valid(self):
        """Test unloading a valid asset."""
        self.asset_manager.load_asset("test_asset", self.test_asset_path)
        self.asset_manager.unload_asset("test_asset")
        self.assertIsNone(self.asset_manager.get_asset("test_asset"))

    def test_unload_asset_invalid(self):
        """Test unloading an invalid asset."""
        with self.assertRaises(KeyError):
            self.asset_manager.unload_asset("nonexistent_asset")

    def test_list_assets(self):
        """Test listing all loaded assets."""
        self.asset_manager.load_asset("test_asset1", self.test_asset_path)
        self.asset_manager.load_asset("test_asset2", self.test_asset_path)
        assets = self.asset_manager.list_assets()
        self.assertEqual(len(assets), 2)
        self.assertIn("test_asset1", assets)
        self.assertIn("test_asset2", assets)


if __name__ == "__main__":
    unittest.main()

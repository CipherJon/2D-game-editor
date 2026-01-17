"""
Test cases for the thumbnail_cache.py module.
This module tests the functionality of the ThumbnailCache class, including performance.
"""

import os
import tempfile
import time
import unittest

from src.assets.thumbnail_cache import ThumbnailCache


class TestThumbnailCache(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.cache_dir = os.path.join(self.temp_dir, "cache")
        self.thumbnail_cache = ThumbnailCache(self.cache_dir)
        self.test_asset_path = os.path.join(self.temp_dir, "test_asset.png")
        # Create a simple test image
        from PIL import Image

        img = Image.new("RGB", (100, 100), color="red")
        img.save(self.test_asset_path)

    def tearDown(self):
        # Clean up temporary files
        for root, dirs, files in os.walk(self.temp_dir):
            for file in files:
                os.remove(os.path.join(root, file))
            for dir in dirs:
                os.rmdir(os.path.join(root, dir))
        os.rmdir(self.temp_dir)

    def test_generate_and_cache_thumbnail_valid(self):
        """Test generating and caching a valid thumbnail."""
        thumbnail = self.thumbnail_cache.generate_and_cache_thumbnail(
            self.test_asset_path
        )
        self.assertIsNotNone(thumbnail)
        self.assertTrue(
            os.path.exists(os.path.join(self.cache_dir, os.listdir(self.cache_dir)[0]))
        )

    def test_generate_and_cache_thumbnail_invalid(self):
        """Test generating and caching an invalid thumbnail."""
        invalid_asset_path = os.path.join(self.temp_dir, "invalid_asset.png")
        with self.assertRaises(FileNotFoundError):
            self.thumbnail_cache.generate_and_cache_thumbnail(invalid_asset_path)

    def test_get_thumbnail_valid(self):
        """Test retrieving a valid thumbnail."""
        self.thumbnail_cache.generate_and_cache_thumbnail(self.test_asset_path)
        thumbnail = self.thumbnail_cache.get_thumbnail(self.test_asset_path)
        self.assertIsNotNone(thumbnail)

    def test_get_thumbnail_invalid(self):
        """Test retrieving an invalid thumbnail."""
        thumbnail = self.thumbnail_cache.get_thumbnail("nonexistent_asset.png")
        self.assertIsNone(thumbnail)

    def test_clear_cache(self):
        """Test clearing the thumbnail cache."""
        self.thumbnail_cache.generate_and_cache_thumbnail(self.test_asset_path)
        self.thumbnail_cache.clear_cache()
        self.assertEqual(len(os.listdir(self.cache_dir)), 0)

    def test_performance_generate_thumbnails(self):
        """Test the performance of generating multiple thumbnails."""
        start_time = time.time()
        for i in range(10):
            test_asset_path = os.path.join(self.temp_dir, f"test_asset_{i}.png")
            from PIL import Image

            img = Image.new("RGB", (100, 100), color="red")
            img.save(test_asset_path)
            self.thumbnail_cache.generate_and_cache_thumbnail(test_asset_path)
        end_time = time.time()
        print(f"Time to generate 10 thumbnails: {end_time - start_time:.2f} seconds")

    def test_performance_retrieve_thumbnails(self):
        """Test the performance of retrieving multiple thumbnails."""
        # Generate thumbnails first
        for i in range(10):
            test_asset_path = os.path.join(self.temp_dir, f"test_asset_{i}.png")
            from PIL import Image

            img = Image.new("RGB", (100, 100), color="red")
            img.save(test_asset_path)
            self.thumbnail_cache.generate_and_cache_thumbnail(test_asset_path)

        # Retrieve thumbnails
        start_time = time.time()
        for i in range(10):
            test_asset_path = os.path.join(self.temp_dir, f"test_asset_{i}.png")
            self.thumbnail_cache.get_thumbnail(test_asset_path)
        end_time = time.time()
        print(f"Time to retrieve 10 thumbnails: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    unittest.main()

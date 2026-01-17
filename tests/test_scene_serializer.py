"""
Test cases for the scene_serializer.py module.
This module tests the functionality of the SceneSerializer class, including error handling.
"""

import os
import tempfile
import unittest
from src.scene.scene import Scene
from src.scene.layer import Layer
from src.scene.entity import Entity
from src.scene.tilemap import Tilemap
from src.scene.scene_serializer import SceneSerializer

class TestSceneSerializer(unittest.TestCase):
    def setUp(self):
        self.serializer = SceneSerializer()
        self.scene = Scene()
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Clean up temporary files
        for file in os.listdir(self.temp_dir):
            os.remove(os.path.join(self.temp_dir, file))
        os.rmdir(self.temp_dir)

    def test_serialize_valid_scene(self):
        """Test serializing a valid scene."""
        layer = Layer("Test Layer")
        self.scene.add_layer(layer)
        scene_data = self.serializer.serialize(self.scene)
        self.assertEqual(scene_data["name"], self.scene.name)
        self.assertEqual(len(scene_data["layers"]), 1)

    def test_serialize_invalid_scene(self):
        """Test serializing an invalid scene."""
        with self.assertRaises(ValueError):
            self.serializer.serialize("invalid_scene")

    def test_deserialize_valid_scene(self):
        """Test deserializing a valid scene."""
        scene_data = {
            "name": "Test Scene",
            "layers": [
                {
                    "name": "Test Layer",
                    "visible": True,
                    "opacity": 1.0,
                }
            ],
            "entities": [],
            "tilemaps": [],
        }
        scene = self.serializer.deserialize(scene_data)
        self.assertEqual(scene.name, "Test Scene")
        self.assertEqual(len(scene.layers), 1)

    def test_deserialize_invalid_scene(self):
        """Test deserializing an invalid scene."""
        with self.assertRaises(ValueError):
            self.serializer.deserialize("invalid_scene_data")

    def test_save_to_file_valid(self):
        """Test saving a valid scene to a file."""
        temp_file = os.path.join(self.temp_dir, "test_scene.json")
        self.serializer.save_to_file(self.scene, temp_file)
        self.assertTrue(os.path.exists(temp_file))

    def test_save_to_file_invalid(self):
        """Test saving a scene to an invalid file path."""
        invalid_file_path = os.path.join(self.temp_dir, "invalid_dir", "test_scene.json")
        with self.assertRaises(FileNotFoundError):
            self.serializer.save_to_file(self.scene, invalid_file_path)

    def test_load_from_file_valid(self):
        """Test loading a valid scene from a file."""
        temp_file = os.path.join(self.temp_dir, "test_scene.json")
        self.serializer.save_to_file(self.scene, temp_file)
        loaded_scene = self.serializer.load_from_file(temp_file)
        self.assertEqual(loaded_scene.name, self.scene.name)

    def test_load_from_file_invalid(self):
        """Test loading a scene from an invalid file path."""
        invalid_file_path = os.path.join(self.temp_dir, "nonexistent_scene.json")
        with self.assertRaises(FileNotFoundError):
            self.serializer.load_from_file(invalid_file_path)

if __name__ == "__main__":
    unittest.main()
```

### Summary of Changes:
1. **Added Test Cases**: Added comprehensive test cases for the `SceneSerializer` class, including serializing, deserializing, saving, and loading scenes.
2. **Tested Edge Cases**: Included tests for invalid inputs, such as invalid scene objects and file paths.
3. **Added Documentation**: Added detailed docstrings for the test class and methods.
4. **Improved Readability**: Used descriptive method names and comments to improve readability.

These changes ensure that the `scene_serializer.py` module is thoroughly tested and handles edge cases appropriately.

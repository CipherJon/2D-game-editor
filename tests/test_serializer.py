# test_serializer.py
import os
import tempfile
import unittest

from scene.layer import Layer
from scene.scene import Scene
from scene.scene_serializer import SceneSerializer


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

    def test_save_and_load(self):
        # Add a layer to the scene
        layer = Layer("Test Layer")
        self.scene.add_layer(layer)

        # Save the scene to a temporary file
        temp_file = os.path.join(self.temp_dir, "test_scene.json")
        self.serializer.save_to_file(self.scene, temp_file)

        # Load the scene from the temporary file
        loaded_scene = self.serializer.load_from_file(temp_file)

        # Verify the loaded scene
        self.assertEqual(len(loaded_scene.layers), 1)
        self.assertEqual(loaded_scene.layers[0].name, "Test Layer")

    def test_invalid_data(self):
        # Create a temporary file with invalid data
        temp_file = os.path.join(self.temp_dir, "invalid_scene.json")
        with open(temp_file, "w") as f:
            f.write("invalid json data")

        # Test handling invalid data
        with self.assertRaises(Exception):
            self.serializer.load_scene(temp_file)

    def test_empty_scene(self):
        # Save an empty scene
        temp_file = os.path.join(self.temp_dir, "empty_scene.json")
        self.serializer.save_to_file(self.scene, temp_file)

        # Load the empty scene
        loaded_scene = self.serializer.load_from_file(temp_file)

        # Verify the loaded scene is empty
        self.assertEqual(len(loaded_scene.layers), 0)

    def test_multiple_layers(self):
        # Add multiple layers to the scene
        layer1 = Layer("Layer 1")
        layer2 = Layer("Layer 2")
        self.scene.add_layer(layer1)
        self.scene.add_layer(layer2)

        # Save the scene to a temporary file
        temp_file = os.path.join(self.temp_dir, "multi_layer_scene.json")
        self.serializer.save_to_file(self.scene, temp_file)

        # Load the scene from the temporary file
        loaded_scene = self.serializer.load_from_file(temp_file)

        # Verify the loaded scene
        self.assertEqual(len(loaded_scene.layers), 2)
        self.assertEqual(loaded_scene.layers[0].name, "Layer 1")
        self.assertEqual(loaded_scene.layers[1].name, "Layer 2")


if __name__ == "__main__":
    unittest.main()

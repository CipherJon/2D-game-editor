import unittest

from src.scene.layer import Layer
from src.scene.scene import Scene
from src.scene.tilemap import Tilemap


class TestScene(unittest.TestCase):
    def setUp(self):
        self.scene = Scene()

    def test_add_layer(self):
        layer = Layer("Test Layer")
        self.scene.add_layer(layer)
        self.assertEqual(len(self.scene.layers), 1)

    def test_remove_layer(self):
        layer = Layer("Test Layer")
        self.scene.add_layer(layer)
        self.scene.remove_layer(layer)
        self.assertEqual(len(self.scene.layers), 0)


if __name__ == "__main__":
    unittest.main()

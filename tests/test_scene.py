import unittest

from scene.layer import Layer
from scene.scene import Scene
from scene.tilemap import Tilemap


class TestScene(unittest.TestCase):
    def setUp(self):
        self.scene = Scene()

    def test_add_layer(self):
        layer = Layer("Test Layer")
        self.scene.add_layer(layer)
        self.assertEqual(len(self.scene.layers), 1)
        self.assertEqual(self.scene.layers[0].name, "Test Layer")

    def test_remove_layer(self):
        layer = Layer("Test Layer")
        self.scene.add_layer(layer)
        self.scene.remove_layer(layer)
        self.assertEqual(len(self.scene.layers), 0)

    def test_add_multiple_layers(self):
        layer1 = Layer("Layer 1")
        layer2 = Layer("Layer 2")
        self.scene.add_layer(layer1)
        self.scene.add_layer(layer2)
        self.assertEqual(len(self.scene.layers), 2)
        self.assertEqual(self.scene.layers[0].name, "Layer 1")
        self.assertEqual(self.scene.layers[1].name, "Layer 2")

    def test_remove_nonexistent_layer(self):
        layer = Layer("Test Layer")
        with self.assertRaises(ValueError):
            self.scene.remove_layer(layer)

    def test_clear_layers(self):
        layer1 = Layer("Layer 1")
        layer2 = Layer("Layer 2")
        self.scene.add_layer(layer1)
        self.scene.add_layer(layer2)
        self.scene.clear_layers()
        self.assertEqual(len(self.scene.layers), 0)

    def test_get_layer_by_name(self):
        layer = Layer("Test Layer")
        self.scene.add_layer(layer)
        retrieved_layer = self.scene.get_layer_by_name("Test Layer")
        self.assertEqual(retrieved_layer.name, "Test Layer")

    def test_get_nonexistent_layer_by_name(self):
        with self.assertRaises(ValueError):
            self.scene.get_layer_by_name("Nonexistent Layer")


class TestLayer(unittest.TestCase):
    def setUp(self):
        self.layer = Layer("Test Layer")

    def test_layer_initialization(self):
        self.assertEqual(self.layer.name, "Test Layer")
        self.assertTrue(self.layer.visible)
        self.assertEqual(self.layer.opacity, 1.0)

    def test_set_layer_name(self):
        self.layer.name = "New Name"
        self.assertEqual(self.layer.name, "New Name")

    def test_set_layer_visibility(self):
        self.layer.visible = False
        self.assertFalse(self.layer.visible)

    def test_set_layer_opacity(self):
        self.layer.opacity = 0.5
        self.assertEqual(self.layer.opacity, 0.5)


class TestTilemap(unittest.TestCase):
    def setUp(self):
        self.tilemap = Tilemap(10, 10, 32, 32)

    def test_tilemap_initialization(self):
        self.assertEqual(self.tilemap.width, 10)
        self.assertEqual(self.tilemap.height, 10)
        self.assertEqual(self.tilemap.tile_width, 32)
        self.assertEqual(self.tilemap.tile_height, 32)

    def test_set_tile(self):
        self.tilemap.add_tile(0, 0, 1)
        self.assertEqual(self.tilemap.get_tile(0, 0).tile_id, 1)

    def test_get_tile_out_of_bounds(self):
        with self.assertRaises(IndexError):
            self.tilemap.get_tile(10, 10)

    def test_clear_tile(self):
        self.tilemap.add_tile(0, 0, 1)
        self.tilemap.remove_tile(0, 0)
        self.assertIsNone(self.tilemap.get_tile(0, 0))


if __name__ == "__main__":
    unittest.main()

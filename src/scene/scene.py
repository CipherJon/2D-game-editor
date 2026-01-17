# scene.py
"""
Module for managing the game scene, including layers, entities, and tilemaps.
"""


class Scene:
    """
    Represents a game scene containing layers, entities, and tilemaps.
    """

    def __init__(self, name: str = "Untitled Scene"):
        """
        Initialize a new scene.

        Args:
            name (str): The name of the scene.
        """
        self.name = name
        self.layers = []
        self.entities = []
        self.tilemaps = []

    def add_layer(self, layer):
        """
        Add a layer to the scene.

        Args:
            layer: The layer to add.
        """
        self.layers.append(layer)

    def remove_layer(self, layer):
        """
        Remove a layer from the scene.

        Args:
            layer: The layer to remove.
        """
        if layer in self.layers:
            self.layers.remove(layer)

    def add_entity(self, entity):
        """
        Add an entity to the scene.

        Args:
            entity: The entity to add.
        """
        self.entities.append(entity)

    def remove_entity(self, entity):
        """
        Remove an entity from the scene.

        Args:
            entity: The entity to remove.
        """
        if entity in self.entities:
            self.entities.remove(entity)

    def add_tilemap(self, tilemap):
        """
        Add a tilemap to the scene.

        Args:
            tilemap: The tilemap to add.
        """
        self.tilemaps.append(tilemap)

    def remove_tilemap(self, tilemap):
        """
        Remove a tilemap from the scene.

        Args:
            tilemap: The tilemap to remove.
        """
        if tilemap in self.tilemaps:
            self.tilemaps.remove(tilemap)

    def clear(self):
        """
        Clear all layers, entities, and tilemaps from the scene.
        """
        self.layers.clear()
        self.entities.clear()
        self.tilemaps.clear()

    def __str__(self):
        """
        Return a string representation of the scene.

        Returns:
            str: The scene's name and the number of layers, entities, and tilemaps.
        """
        return (
            f"Scene(name='{self.name}', "
            f"layers={len(self.layers)}, "
            f"entities={len(self.entities)}, "
            f"tilemaps={len(self.tilemaps)})"
        )

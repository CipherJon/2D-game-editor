import json
from typing import Any, Dict, Optional

from .entity import Entity
from .layer import Layer
from .scene import Scene
from .tilemap import Tilemap


class SceneSerializer:
    """
    Handles serialization and deserialization of Scene objects.
    Supports saving and loading scenes to/from JSON files.
    """

    @staticmethod
    def serialize(scene: Scene) -> Dict[str, Any]:
        """
        Convert a Scene object into a serializable dictionary.

        Args:
            scene: The Scene object to serialize.

        Returns:
            A dictionary representing the scene.
        """
        scene_data = {
            "name": scene.name,
            "layers": [],
            "entities": [],
            "tilemaps": [],
        }

        # Serialize layers
        for layer in scene.layers:
            layer_data = {
                "name": layer.name,
                "visible": layer.visible,
                "opacity": layer.opacity,
            }
            scene_data["layers"].append(layer_data)

        # Serialize entities
        for entity in scene.entities:
            entity_data = {
                "name": entity.name,
                "x": entity.x,
                "y": entity.y,
                "width": entity.width,
                "height": entity.height,
                "properties": entity.properties,
            }
            scene_data["entities"].append(entity_data)

        # Serialize tilemaps
        for tilemap in scene.tilemaps:
            tilemap_data = {
                "name": tilemap.name,
                "tile_width": tilemap.tile_width,
                "tile_height": tilemap.tile_height,
                "rows": tilemap.rows,
                "columns": tilemap.columns,
                "tiles": tilemap.tiles,
            }
            scene_data["tilemaps"].append(tilemap_data)

        return scene_data

    @staticmethod
    def deserialize(scene_data: Dict[str, Any]) -> Scene:
        """
        Convert a serialized dictionary back into a Scene object.

        Args:
            scene_data: The dictionary representing the scene.

        Returns:
            A Scene object.
        """
        scene = Scene(
            name=scene_data["name"],
        )

        # Deserialize layers
        for layer_data in scene_data["layers"]:
            layer = Layer(
                name=layer_data["name"],
                visible=layer_data["visible"],
                opacity=layer_data["opacity"],
            )
            scene.layers.append(layer)

        # Deserialize entities
        for entity_data in scene_data["entities"]:
            entity = Entity(
                name=entity_data["name"],
                x=entity_data["x"],
                y=entity_data["y"],
                width=entity_data["width"],
                height=entity_data["height"],
                properties=entity_data["properties"],
            )
            scene.entities.append(entity)

        # Deserialize tilemaps
        for tilemap_data in scene_data["tilemaps"]:
            tilemap = Tilemap(
                name=tilemap_data["name"],
                tile_width=tilemap_data["tile_width"],
                tile_height=tilemap_data["tile_height"],
                rows=tilemap_data["rows"],
                columns=tilemap_data["columns"],
                tiles=tilemap_data["tiles"],
            )
            scene.tilemaps.append(tilemap)

        return scene

    @staticmethod
    def save_to_file(scene: Scene, file_path: str) -> None:
        """
        Save a Scene object to a JSON file.

        Args:
            scene: The Scene object to save.
            file_path: The path to the JSON file.
        """
        scene_data = SceneSerializer.serialize(scene)
        with open(file_path, "w") as file:
            json.dump(scene_data, file, indent=4)

    @staticmethod
    def load_from_file(file_path: str) -> Optional[Scene]:
        """
        Load a Scene object from a JSON file.

        Args:
            file_path: The path to the JSON file.

        Returns:
            A Scene object if successful, None otherwise.
        """
        try:
            with open(file_path, "r") as file:
                scene_data = json.load(file)
            return SceneSerializer.deserialize(scene_data)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading scene: {e}")
            return None

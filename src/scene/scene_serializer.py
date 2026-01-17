import json
from typing import Any, Dict, List, Optional

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

        Raises:
            ValueError: If the scene object is invalid or cannot be serialized.
        """
        if not isinstance(scene, Scene):
            raise ValueError("Invalid scene object provided for serialization.")

        scene_data = {
            "name": scene.name,
            "layers": [],
            "entities": [],
            "tilemaps": [],
        }

        # Serialize layers
        for layer in scene.layers:
            if not isinstance(layer, Layer):
                raise ValueError("Invalid layer object in scene.")
            layer_data = {
                "name": layer.name,
                "visible": layer.visible,
                "opacity": layer.opacity,
            }
            scene_data["layers"].append(layer_data)

        # Serialize entities
        for entity in scene.entities:
            if not isinstance(entity, Entity):
                raise ValueError("Invalid entity object in scene.")
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
            if not isinstance(tilemap, Tilemap):
                raise ValueError("Invalid tilemap object in scene.")
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

        Raises:
            ValueError: If the scene data is invalid or cannot be deserialized.
        """
        if not isinstance(scene_data, dict):
            raise ValueError("Invalid scene data provided for deserialization.")

        scene = Scene(
            name=scene_data.get("name", "Untitled Scene"),
        )

        # Deserialize layers
        for layer_data in scene_data.get("layers", []):
            if not isinstance(layer_data, dict):
                raise ValueError("Invalid layer data in scene.")
            layer = Layer(
                name=layer_data.get("name", "Unnamed Layer"),
                visible=layer_data.get("visible", True),
                opacity=layer_data.get("opacity", 1.0),
            )
            scene.layers.append(layer)

        # Deserialize entities
        for entity_data in scene_data.get("entities", []):
            if not isinstance(entity_data, dict):
                raise ValueError("Invalid entity data in scene.")
            entity = Entity(
                name=entity_data.get("name", "Unnamed Entity"),
                x=entity_data.get("x", 0),
                y=entity_data.get("y", 0),
                width=entity_data.get("width", 1),
                height=entity_data.get("height", 1),
                properties=entity_data.get("properties", {}),
            )
            scene.entities.append(entity)

        # Deserialize tilemaps
        for tilemap_data in scene_data.get("tilemaps", []):
            if not isinstance(tilemap_data, dict):
                raise ValueError("Invalid tilemap data in scene.")
            tilemap = Tilemap(
                name=tilemap_data.get("name", "Unnamed Tilemap"),
                tile_width=tilemap_data.get("tile_width", 32),
                tile_height=tilemap_data.get("tile_height", 32),
                rows=tilemap_data.get("rows", 0),
                columns=tilemap_data.get("columns", 0),
                tiles=tilemap_data.get("tiles", {}),
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

        Raises:
            FileNotFoundError: If the directory for the file does not exist.
            PermissionError: If the file cannot be written due to permission issues.
            json.JSONEncodeError: If the scene data cannot be serialized to JSON.
        """
        scene_data = SceneSerializer.serialize(scene)
        try:
            with open(file_path, "w") as file:
                json.dump(scene_data, file, indent=4)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Directory not found: {e}")
        except PermissionError as e:
            raise PermissionError(f"Permission denied while saving scene: {e}")
        except json.JSONEncodeError as e:
            raise json.JSONEncodeError(f"Error encoding scene data: {e}")

    @staticmethod
    def load_from_file(file_path: str) -> Optional[Scene]:
        """
        Load a Scene object from a JSON file.

        Args:
            file_path: The path to the JSON file.

        Returns:
            A Scene object if successful, None otherwise.

        Raises:
            FileNotFoundError: If the file does not exist.
            PermissionError: If the file cannot be read due to permission issues.
            json.JSONDecodeError: If the file contains invalid JSON data.
        """
        try:
            with open(file_path, "r") as file:
                scene_data = json.load(file)
            return SceneSerializer.deserialize(scene_data)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"File not found: {e}")
        except PermissionError as e:
            raise PermissionError(f"Permission denied while loading scene: {e}")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Error decoding scene data: {e}")

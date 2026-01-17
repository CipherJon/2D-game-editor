# layer.py
"""
Layer module for the 2D game editor.
This module defines the Layer class, which represents a layer in a scene.
"""


class Layer:
    """
    A class representing a layer in a scene.

    Attributes:
        name (str): The name of the layer.
        visible (bool): Whether the layer is visible.
        locked (bool): Whether the layer is locked.
        opacity (float): The opacity of the layer (0.0 to 1.0).
    """

    def __init__(
        self,
        name: str,
        visible: bool = True,
        locked: bool = False,
        opacity: float = 1.0,
    ):
        """
        Initializes a new Layer instance.

        Args:
            name (str): The name of the layer.
            visible (bool, optional): Whether the layer is visible. Defaults to True.
            locked (bool, optional): Whether the layer is locked. Defaults to False.
            opacity (float, optional): The opacity of the layer (0.0 to 1.0). Defaults to 1.0.
        """
        self.name = name
        self.visible = visible
        self.locked = locked
        self.opacity = opacity

    def toggle_visibility(self):
        """
        Toggles the visibility of the layer.
        """
        self.visible = not self.visible

    def toggle_lock(self):
        """
        Toggles the lock status of the layer.
        """
        self.locked = not self.locked

    def set_opacity(self, opacity: float):
        """
        Sets the opacity of the layer.

        Args:
            opacity (float): The opacity value (0.0 to 1.0).
        """
        if 0.0 <= opacity <= 1.0:
            self.opacity = opacity
        else:
            raise ValueError("Opacity must be between 0.0 and 1.0.")

    def __repr__(self):
        """
        Returns a string representation of the Layer instance.

        Returns:
            str: A string representation of the Layer.
        """
        return f"Layer(name='{self.name}', visible={self.visible}, locked={self.locked}, opacity={self.opacity})"

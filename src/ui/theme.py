"""
Theme management for the 2D game editor UI.
This module handles color schemes, styles, and theming for the editor.
"""


class Theme:
    """
    A class to manage the UI theme of the editor.
    """

    def __init__(self):
        self.colors = {
            "background": "#2b2b2b",
            "foreground": "#ffffff",
            "primary": "#4a90e2",
            "secondary": "#50e3c2",
            "accent": "#f5a623",
            "error": "#d0021b",
            "success": "#7ed321",
            "border": "#4a4a4a",
            "panel_bg": "#3e3e3e",
            "button_bg": "#4a4a4a",
            "button_hover": "#5a5a5a",
            "text": "#ffffff",
            "text_disabled": "#888888",
        }

    def get_color(self, key):
        """
        Retrieve a color from the theme by its key.

        Args:
            key (str): The key of the color to retrieve.

        Returns:
            str: The hexadecimal color value.
        """
        return self.colors.get(key, "#ffffff")

    def set_color(self, key, value):
        """
        Set a color in the theme.

        Args:
            key (str): The key of the color to set.
            value (str): The hexadecimal color value.
        """
        self.colors[key] = value

    def apply_theme(self):
        """
        Apply the theme to the UI.
        """
        # Logic to apply the theme will go here
        pass

# toolbar.py
"""
Toolbar panel for the 2D game editor.
This module provides the toolbar UI for the editor.
"""


class Toolbar:
    """
    Represents the toolbar panel in the editor.
    The toolbar contains buttons for various tools and actions.
    """

    def __init__(self):
        """
        Initialize the toolbar.
        """
        self.tools = []
        self.active_tool = None

    def add_tool(self, tool):
        """
        Add a tool to the toolbar.

        Args:
            tool: The tool to add to the toolbar.
        """
        self.tools.append(tool)

    def set_active_tool(self, tool):
        """
        Set the active tool in the toolbar.

        Args:
            tool: The tool to set as active.
        """
        self.active_tool = tool

    def render(self):
        """
        Render the toolbar UI.
        """
        print("Rendering toolbar...")
        for tool in self.tools:
            print(f"Tool: {tool}")
        if self.active_tool:
            print(f"Active Tool: {self.active_tool}")

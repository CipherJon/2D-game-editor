import pygame

# toolbar.py
"""
Toolbar panel for the 2D game editor.
This module provides the toolbar UI for the editor.
"""


class ToolbarPanel:
    """
    Represents the toolbar panel in the editor.
    The toolbar contains buttons for various tools and actions.
    """

    def __init__(self):
        """
        Initialize the toolbar panel.
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

    def render(self, screen):
        """
        Render the toolbar UI.

        Args:
            screen (pygame.Surface): The screen surface to render to.
        """
        # Draw a simple rectangle to represent the toolbar
        pygame.draw.rect(screen, (100, 100, 100), (10, 120, 200, 50))
        # Draw a label for the toolbar
        font = pygame.font.SysFont(None, 24)
        label = font.render("Toolbar", True, (255, 255, 255))
        screen.blit(label, (20, 130))

    def handle_event(self, event):
        """
        Handles events for the toolbar panel.

        Args:
            event (pygame.event.Event): The pygame event.
        """
        pass

    def update(self, delta_time):
        """
        Updates the toolbar panel.

        Args:
            delta_time (float): Time elapsed since the last frame.
        """
        pass

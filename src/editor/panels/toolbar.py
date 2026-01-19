import pygame

from ...ui.theme import Theme
from ...utils.color import hex_to_rgb

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
        self.theme = Theme()
        self.button_width = 50
        self.button_height = 50
        self.padding = 10
        self.margin = 10
        self.panel_width = 200
        self.panel_height = 80
        self.panel_x = 10
        self.panel_y = 320

        # Initialize tools
        self._initialize_tools()

    def _initialize_tools(self):
        """
        Initialize the default tools for the toolbar.
        """
        # Import tools dynamically to avoid circular imports
        from ...tools.brush_tool import BrushTool
        from ...tools.entity_placer import EntityPlacerTool
        from ...tools.eraser_tool import EraserTool
        from ...tools.fill_tool import FillTool
        from ...tools.move_tool import MoveTool
        from ...tools.select_tool import SelectTool

        self.tools = [
            {"name": "Brush", "tool": BrushTool(), "icon": None},
            {"name": "Eraser", "tool": EraserTool(), "icon": None},
            {"name": "Select", "tool": SelectTool(), "icon": None},
            {"name": "Move", "tool": MoveTool(), "icon": None},
            {"name": "Fill", "tool": FillTool(), "icon": None},
            {"name": "Entity Placer", "tool": EntityPlacerTool(), "icon": None},
        ]

        # Set the default active tool
        if self.tools:
            self.active_tool = self.tools[0]["tool"]

    def add_tool(self, tool_name, tool_instance):
        """
        Add a tool to the toolbar.

        Args:
            tool_name (str): The name of the tool.
            tool_instance: The tool instance to add to the toolbar.
        """
        self.tools.append({"name": tool_name, "tool": tool_instance, "icon": None})

    def set_active_tool(self, tool_name):
        """
        Set the active tool in the toolbar.

        Args:
            tool_name (str): The name of the tool to set as active.
        """
        for tool in self.tools:
            if tool["name"] == tool_name:
                self.active_tool = tool["tool"]
                break

    def render(self, screen):
        """
        Render the toolbar UI.

        Args:
            screen (pygame.Surface): The screen surface to render to.
        """
        # Draw the panel background
        panel_bg_color = hex_to_rgb(self.theme.get_color("panel_bg"))
        pygame.draw.rect(
            screen,
            panel_bg_color,
            (self.panel_x, self.panel_y, self.panel_width, self.panel_height),
        )

        # Draw the panel border
        border_color = hex_to_rgb(self.theme.get_color("border"))
        pygame.draw.rect(
            screen,
            border_color,
            (self.panel_x, self.panel_y, self.panel_width, self.panel_height),
            2,
        )

        # Draw the panel label
        font = pygame.font.SysFont(None, 24)
        text_color = hex_to_rgb(self.theme.get_color("text"))
        label = font.render("Toolbar", True, text_color)
        screen.blit(label, (self.panel_x + self.padding, self.panel_y + self.padding))

        # Draw the tool buttons
        for i, tool in enumerate(self.tools):
            button_x = (
                self.panel_x + self.padding + i * (self.button_width + self.padding)
            )
            button_y = self.panel_y + 40

            # Draw the button background
            button_bg_color = hex_to_rgb(self.theme.get_color("button_bg"))
            if tool["tool"] == self.active_tool:
                button_bg_color = hex_to_rgb(self.theme.get_color("primary"))

            pygame.draw.rect(
                screen,
                button_bg_color,
                (button_x, button_y, self.button_width, self.button_height),
            )

            # Draw the button border
            button_border_color = hex_to_rgb(self.theme.get_color("border"))
            pygame.draw.rect(
                screen,
                button_border_color,
                (button_x, button_y, self.button_width, self.button_height),
                1,
            )

            # Draw the tool name (or icon if available)
            tool_font = pygame.font.SysFont(None, 12)
            tool_text_color = hex_to_rgb(self.theme.get_color("text"))
            tool_label = tool_font.render(tool["name"], True, tool_text_color)
            text_rect = tool_label.get_rect(
                center=(
                    button_x + self.button_width // 2,
                    button_y + self.button_height // 2,
                )
            )
            screen.blit(tool_label, text_rect)

    def handle_event(self, event):
        """
        Handles events for the toolbar panel.

        Args:
            event (pygame.event.Event): The pygame event.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if (
                    self.panel_x <= mouse_x <= self.panel_x + self.panel_width
                    and self.panel_y <= mouse_y <= self.panel_y + self.panel_height
                ):
                    # Check if a tool button was clicked
                    for i, tool in enumerate(self.tools):
                        button_x = (
                            self.panel_x
                            + self.padding
                            + i * (self.button_width + self.padding)
                        )
                        button_y = self.panel_y + 40
                        if (
                            button_x <= mouse_x <= button_x + self.button_width
                            and button_y <= mouse_y <= button_y + self.button_height
                        ):
                            self.active_tool = tool["tool"]
                            break

    def update(self, delta_time):
        """
        Updates the toolbar panel.

        Args:
            delta_time (float): Time elapsed since the last frame.
        """
        pass

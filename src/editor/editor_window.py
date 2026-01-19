# editor_window.py
"""
Main editor window composition and management.
This module handles the main window layout, panels, and user interactions.
"""

import pygame
from pygame.locals import *

from ..core.events import EventBus
from ..rendering.camera import Camera
from ..scene.scene import Scene
from ..ui.widgets import Button


class EditorWindow:
    """
    The main editor window that composes all UI panels and handles user interactions.
    """

    def __init__(self, window: pygame.Surface, event_bus: EventBus):
        """
        Initialize the editor window with the main window surface and event bus.

        Args:
            window (pygame.Surface): The main window surface.
            event_bus (EventBus): The event bus for handling events.
        """
        self.window = window
        self.event_bus = event_bus
        self.event_bus = EventBus()
        self.camera = Camera()
        self.scene = Scene()
        self.panels = []
        self.is_running = True

        # Initialize UI panels
        self._initialize_panels()

    def _initialize_panels(self):
        """
        Initialize all UI panels for the editor.
        """
        from ..editor.panels.assets_browser import AssetsBrowserPanel
        from ..editor.panels.hierarchy import HierarchyPanel
        from ..editor.panels.inspector import InspectorPanel
        from ..editor.panels.layer_panel import LayerPanel
        from ..editor.panels.tile_palette import TilePalettePanel
        from ..editor.panels.toolbar import ToolbarPanel

        self.panels = [
            HierarchyPanel(),
            InspectorPanel(),
            AssetsBrowserPanel(),
            TilePalettePanel(),
            LayerPanel(),
            ToolbarPanel(),
        ]

    def handle_events(self):
        """
        Handle all pygame events for the editor window.
        """
        for event in pygame.event.get():
            if event.type == QUIT:
                self.is_running = False
            elif event.type == KEYDOWN:
                self._handle_key_down(event)
            elif event.type == MOUSEBUTTONDOWN:
                self._handle_mouse_down(event)
            elif event.type == MOUSEBUTTONUP:
                self._handle_mouse_up(event)
            elif event.type == MOUSEMOTION:
                self._handle_mouse_motion(event)

            # Pass events to all panels
            for panel in self.panels:
                panel.handle_event(event)

    def _handle_key_down(self, event):
        """
        Handle key down events.

        Args:
            event (pygame.event.Event): The pygame event.
        """
        if event.key == K_ESCAPE:
            self.is_running = False
        elif event.key == K_s and event.mod & KMOD_CTRL:
            self.event_bus.emit("save_scene", {})

    def _handle_mouse_down(self, event):
        """
        Handle mouse button down events.

        Args:
            event (pygame.event.Event): The pygame event.
        """
        pass

    def _handle_mouse_up(self, event):
        """
        Handle mouse button up events.

        Args:
            event (pygame.event.Event): The pygame event.
        """
        pass

    def _handle_mouse_motion(self, event):
        """
        Handle mouse motion events.

        Args:
            event (pygame.event.Event): The pygame event.
        """
        pass

    def update(self, delta_time: float):
        """
        Update the editor window and all panels.

        Args:
            delta_time (float): Time elapsed since the last frame.
        """
        for panel in self.panels:
            panel.update(delta_time)

    def render(self):
        """
        Render the editor window and all panels.
        """
        # Clear the screen
        self.window.fill((30, 30, 30))

        # Render all panels
        for panel in self.panels:
            panel.render(self.window)

        # Flip the display
        pygame.display.flip()

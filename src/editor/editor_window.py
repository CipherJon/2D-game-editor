# editor_window.py
"""
Main editor window composition and management.
This module handles the main window layout, panels, and user interactions.
"""

import pygame
from pygame.locals import *

from ..core.app import App
from ..core.events import EventBus
from ..rendering.camera import Camera
from ..scene.scene import Scene
from ..ui.widgets import Button, Panel


class EditorWindow:
    """
    The main editor window that composes all UI panels and handles user interactions.
    """

    def __init__(self, app: App):
        """
        Initialize the editor window with the main application instance.

        Args:
            app (App): The main application instance.
        """
        self.app = app
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
            HierarchyPanel(self.app, self.event_bus, self.scene),
            InspectorPanel(self.app, self.event_bus, self.scene),
            AssetsBrowserPanel(self.app, self.event_bus),
            TilePalettePanel(self.app, self.event_bus),
            LayerPanel(self.app, self.event_bus, self.scene),
            ToolbarPanel(self.app, self.event_bus),
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

    def render(self, screen: pygame.Surface):
        """
        Render the editor window and all panels.

        Args:
            screen (pygame.Surface): The pygame screen surface.
        """
        # Clear the screen
        screen.fill((30, 30, 30))

        # Render all panels
        for panel in self.panels:
            panel.render(screen)

        # Flip the display
        pygame.display.flip()

    def run(self):
        """
        Main loop for the editor window.
        """
        clock = pygame.time.Clock()
        while self.is_running:
            self.handle_events()
            delta_time = clock.tick(60) / 1000.0
            self.update(delta_time)
            self.render(self.app.screen)

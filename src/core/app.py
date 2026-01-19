"""
Core application class for the 2D Game Editor.
Manages the main window, state, and high-level functionality.
"""

from typing import Optional

import pygame

from ..editor.editor_window import EditorWindow
from .config import Config
from .events import Event, EventBus
from .types import AppState


class App:
    """
    Main application class responsible for managing the editor's lifecycle,
    window, and global state.
    """

    def __init__(self):
        """Initialize the application."""
        self.config = Config()
        self.event_bus = EventBus()
        self.state: AppState = {
            "project_path": None,
            "current_scene": None,
            "is_running": False,
        }
        self.window: pygame.Surface | None = None
        self.clock = pygame.time.Clock()
        self.editor_window: Optional[EditorWindow] = None

    def initialize(self) -> bool:
        """
        Initialize the application and its dependencies.
        Returns True if initialization was successful, False otherwise.
        """
        pygame.init()

        # Initialize the window
        self.window = pygame.display.set_mode(
            (self.config.window_width, self.config.window_height),
            pygame.RESIZABLE,
        )
        pygame.display.set_caption(self.config.window_title)

        # Initialize other systems
        self._initialize_subsystems()

        self.state["is_running"] = True
        return True

    def _initialize_subsystems(self):
        """Initialize all subsystems (e.g., renderer, asset manager, etc.)."""
        if self.window is not None:
            self.editor_window = EditorWindow(self.window, self.event_bus)

    def run(self):
        """Main application loop."""
        if not self.initialize():
            return
        while self.state["is_running"]:
            self._handle_events()
            self._update()
            self._render()
            self.clock.tick(self.config.target_fps)

    def _handle_events(self):
        """Process all pending events."""
        if self.editor_window:
            self.editor_window.handle_events()
            if not self.editor_window.is_running:
                self.state["is_running"] = False

    def _update(self):
        """Update the application state."""
        if self.editor_window:
            self.editor_window.update(self.clock.get_time() / 1000.0)

    def _render(self):
        """Render the current frame."""
        if self.window and self.editor_window:
            self.editor_window.render()

    def shutdown(self):
        """Clean up resources and shut down the application."""
        self.state["is_running"] = False
        pygame.quit()

"""
Core application class for the 2D Game Editor.
Manages the main window, state, and high-level functionality.
"""

from typing import Optional

import pygame

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
        self.window: Optional[pygame.Surface] = None
        self.clock = pygame.time.Clock()

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
        # Placeholder for subsystem initialization
        pass

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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state["is_running"] = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.state["is_running"] = False
            self.event_bus.publish(Event(event.type, event))

    def _update(self):
        """Update the application state."""
        # Placeholder for update logic
        pass

    def _render(self):
        """Render the current frame."""
        if self.window:
            self.window.fill((0, 0, 0))  # Clear the screen
            pygame.display.flip()

    def shutdown(self):
        """Clean up resources and shut down the application."""
        self.state["is_running"] = False
        pygame.quit()

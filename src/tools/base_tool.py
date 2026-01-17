from abc import ABC, abstractmethod
from typing import Optional, Tuple

import pygame


class BaseTool(ABC):
    """
    Abstract base class for all editor tools.
    Defines the interface that all tools must implement.
    """

    def __init__(self, name: str):
        self.name = name
        self.active = False
        self.cursor: Optional[str] = None

    @abstractmethod
    def on_activate(self):
        """Called when the tool is activated."""
        pass

    @abstractmethod
    def on_deactivate(self):
        """Called when the tool is deactivated."""
        pass

    @abstractmethod
    def handle_event(self, event: pygame.event.Event) -> bool:
        """
        Handle pygame events.
        Returns True if the event was consumed by this tool.
        """
        pass

    @abstractmethod
    def update(self, delta_time: float):
        """Update the tool state."""
        pass

    @abstractmethod
    def draw(self, surface: pygame.Surface):
        """Draw tool-specific visuals."""
        pass

    def set_cursor(self, cursor: str):
        """Set the cursor for this tool."""
        self.cursor = cursor

    def get_cursor(self) -> Optional[str]:
        """Get the current cursor for this tool."""
        return self.cursor

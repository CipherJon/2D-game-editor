from .base_tool import BaseTool


class EntityPlacerTool(BaseTool):
    def __init__(self):
        super().__init__("Entity Placer")
        self.icon = "entity_icon.png"

    def on_activate(self):
        """Called when the tool is activated."""
        print("Entity Placer activated")

    def on_deactivate(self):
        """Called when the tool is deactivated."""
        print("Entity Placer deactivated")

    def handle_event(self, event):
        """
        Handle pygame events.
        Returns True if the event was consumed by this tool.
        """
        print(f"Entity Placer handling event: {event}")
        return False

    def update(self, delta_time):
        """Update the tool state."""
        pass

    def draw(self, surface):
        """Draw tool-specific visuals."""
        pass

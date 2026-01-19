from .base_tool import BaseTool


class FillTool(BaseTool):
    """
    A tool for filling areas with a specific tile or color.
    """

    def __init__(self):
        super().__init__("Fill Tool")
        self.icon = "fill_icon.png"

    def on_activate(self):
        """
        Called when the tool is activated.
        """
        print("Fill Tool activated")

    def on_deactivate(self):
        """
        Called when the tool is deactivated.
        """
        print("Fill Tool deactivated")

    def handle_event(self, event):
        """
        Handle pygame events.
        Returns True if the event was consumed by this tool.
        """
        print(f"Fill Tool handling event: {event}")
        return False

    def update(self, delta_time):
        """Update the tool state."""
        pass

    def draw(self, surface):
        """Draw tool-specific visuals."""
        pass

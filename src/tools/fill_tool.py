from .base_tool import BaseTool


class FillTool(BaseTool):
    """
    A tool for filling areas with a specific tile or color.
    """

    def __init__(self):
        super().__init__()
        self.name = "Fill Tool"
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

    def on_mouse_down(self, position):
        """
        Handle mouse down events.
        """
        print(f"Fill Tool: Mouse down at {position}")

    def on_mouse_up(self, position):
        """
        Handle mouse up events.
        """
        print(f"Fill Tool: Mouse up at {position}")

    def on_mouse_move(self, position):
        """
        Handle mouse move events.
        """
        print(f"Fill Tool: Mouse move to {position}")

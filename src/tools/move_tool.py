from .base_tool import BaseTool


class MoveTool(BaseTool):
    def __init__(self):
        super().__init__("Move Tool")

    def on_activate(self):
        print("Move Tool activated")

    def on_deactivate(self):
        print("Move Tool deactivated")

    def handle_event(self, event):
        print(f"Move Tool handling event: {event}")

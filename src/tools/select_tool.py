from .base_tool import BaseTool


class SelectTool(BaseTool):
    def __init__(self):
        super().__init__()

    def on_activate(self):
        print("Select tool activated")

    def on_deactivate(self):
        print("Select tool deactivated")

    def handle_event(self, event):
        print(f"Select tool handling event: {event}")

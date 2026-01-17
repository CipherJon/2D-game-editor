from .base_tool import BaseTool


class EntityPlacer(BaseTool):
    def __init__(self, editor):
        super().__init__(editor)
        self.name = "Entity Placer"
        self.icon = "entity_icon.png"

    def on_activate(self):
        print("Entity Placer activated")

    def on_deactivate(self):
        print("Entity Placer deactivated")

    def handle_event(self, event):
        pass

    def update(self, delta_time):
        pass

    def render(self, surface):
        pass

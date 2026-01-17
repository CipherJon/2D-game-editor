class EraserTool:
    """
    A tool for erasing tiles or entities in the editor.
    """

    def __init__(self):
        """
        Initialize the eraser tool.
        """
        self.name = "Eraser"
        self.icon = "eraser_icon.png"

    def on_activate(self):
        """
        Called when the tool is activated.
        """
        print(f"{self.name} tool activated.")

    def on_deactivate(self):
        """
        Called when the tool is deactivated.
        """
        print(f"{self.name} tool deactivated.")

    def on_mouse_down(self, position):
        """
        Handle mouse down events for erasing.

        Args:
            position (tuple): The (x, y) position of the mouse.
        """
        print(f"Erasing at position: {position}")

    def on_mouse_up(self, position):
        """
        Handle mouse up events for erasing.

        Args:
            position (tuple): The (x, y) position of the mouse.
        """
        print(f"Stopped erasing at position: {position}")

    def on_mouse_move(self, position):
        """
        Handle mouse move events for erasing.

        Args:
            position (tuple): The (x, y) position of the mouse.
        """
        print(f"Moving eraser to position: {position}")

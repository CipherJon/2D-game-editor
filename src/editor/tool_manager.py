# tool_manager.py
"""
Tool Manager Module
Manages the switching and activation of editor tools.
"""


class ToolManager:
    """
    Manages the switching and activation of editor tools.
    """

    def __init__(self):
        self.current_tool = None
        self.tools = {}

    def register_tool(self, tool_name, tool_instance):
        """
        Register a tool with the manager.

        Args:
            tool_name (str): The name of the tool.
            tool_instance: The tool instance to register.
        """
        self.tools[tool_name] = tool_instance

    def set_current_tool(self, tool_name):
        """
        Set the current tool to the specified tool.

        Args:
            tool_name (str): The name of the tool to activate.
        """
        if tool_name in self.tools:
            self.current_tool = self.tools[tool_name]
        else:
            raise ValueError(f"Tool '{tool_name}' is not registered.")

    def get_current_tool(self):
        """
        Get the currently active tool.

        Returns:
            The currently active tool instance.
        """
        return self.current_tool

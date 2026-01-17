# history.py
"""
Undo/Redo system for the editor.
"""


class History:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def push(self, action):
        """Push an action onto the undo stack."""
        self.undo_stack.append(action)
        self.redo_stack.clear()  # Clear redo stack on new action

    def undo(self):
        """Undo the last action."""
        if not self.undo_stack:
            return None
        action = self.undo_stack.pop()
        self.redo_stack.append(action)
        return action

    def redo(self):
        """Redo the last undone action."""
        if not self.redo_stack:
            return None
        action = self.redo_stack.pop()
        self.undo_stack.append(action)
        return action

    def clear(self):
        """Clear both undo and redo stacks."""
        self.undo_stack.clear()
        self.redo_stack.clear()

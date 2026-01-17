# history.py
"""
Undo/Redo system for the editor.
"""


class History:
    def __init__(self, max_states=10):
        self.undo_stack = []
        self.redo_stack = []
        self.max_states = max_states

    def push(self, action):
        """Push an action onto the undo stack."""
        self.undo_stack.append(action)
        self.redo_stack.clear()  # Clear redo stack on new action
        # Enforce the maximum number of states
        if len(self.undo_stack) > self.max_states:
            self.undo_stack.pop(0)

    def undo(self):
        """Undo the last action."""
        if not self.undo_stack:
            raise IndexError("No actions to undo")
        action = self.undo_stack.pop()
        self.redo_stack.append(action)
        return action

    def redo(self):
        """Redo the last undone action."""
        if not self.redo_stack:
            raise IndexError("No actions to redo")
        action = self.redo_stack.pop()
        self.undo_stack.append(action)
        return action

    def clear(self):
        """Clear both undo and redo stacks."""
        self.undo_stack.clear()
        self.redo_stack.clear()

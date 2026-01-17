# selection.py
"""
Module for handling selection logic in the editor.
"""


class Selection:
    """
    A class to manage the selection state in the editor.
    """

    def __init__(self):
        """
        Initialize the selection state.
        """
        self.selected_items = []

    def add_item(self, item):
        """
        Add an item to the selection.

        Args:
            item: The item to add to the selection.
        """
        if item not in self.selected_items:
            self.selected_items.append(item)

    def remove_item(self, item):
        """
        Remove an item from the selection.

        Args:
            item: The item to remove from the selection.
        """
        if item in self.selected_items:
            self.selected_items.remove(item)

    def clear_selection(self):
        """
        Clear the current selection.
        """
        self.selected_items.clear()

    def get_selected_items(self):
        """
        Get the list of selected items.

        Returns:
            list: The list of selected items.
        """
        return self.selected_items.copy()

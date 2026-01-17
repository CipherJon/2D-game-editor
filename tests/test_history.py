# test_history.py
import unittest

from src.editor.history import History


class TestHistory(unittest.TestCase):
    def setUp(self):
        self.history = History()

    def test_undo_redo(self):
        # Test undo and redo functionality
        self.history.push({"key": "value1"})
        self.history.push({"key": "value2"})

        # Undo the last action
        state = self.history.undo()
        self.assertEqual(state, {"key": "value2"})

        # Redo the undone action
        state = self.history.redo()
        self.assertEqual(state, {"key": "value2"})

    def test_history_limit(self):
        # Test history limit functionality
        for i in range(10):
            self.history.push({"key": f"value{i}"})

        # Ensure history does not exceed the limit
        self.assertEqual(len(self.history.undo_stack), 10)

        # Push one more state to exceed the limit
        self.history.push({"key": "value10"})
        self.assertEqual(len(self.history.undo_stack), 10)

    def test_clear_history(self):
        # Test clearing the history
        self.history.push({"key": "value1"})
        self.history.push({"key": "value2"})
        self.history.clear()

        # Ensure history is cleared
        self.assertEqual(len(self.history.undo_stack), 0)
        self.assertEqual(len(self.history.redo_stack), 0)

    def test_undo_empty_history(self):
        # Test undo on an empty history
        with self.assertRaises(IndexError):
            self.history.undo()

    def test_redo_empty_history(self):
        # Test redo on an empty history
        with self.assertRaises(IndexError):
            self.history.redo()


if __name__ == "__main__":
    unittest.main()

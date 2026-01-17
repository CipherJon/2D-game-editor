# widgets.py
# This file contains reusable UI components and widgets for the editor.


class Button:
    def __init__(self, label, on_click):
        self.label = label
        self.on_click = on_click

    def render(self):
        print(f"Button: {self.label}")


class Dropdown:
    def __init__(self, options, on_select):
        self.options = options
        self.on_select = on_select

    def render(self):
        print(f"Dropdown with options: {self.options}")

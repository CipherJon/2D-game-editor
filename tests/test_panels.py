"""
Test cases for the TilePalettePanel and ToolbarPanel.
This module tests the functionality and rendering of the panels.
"""

import unittest

import pygame

from src.editor.panels.tile_palette import TilePalettePanel
from src.editor.panels.toolbar import ToolbarPanel


class TestTilePalettePanel(unittest.TestCase):
    def setUp(self):
        """Set up the test environment."""
        pygame.init()
        self.screen = pygame.Surface((800, 600))
        self.panel = TilePalettePanel()

    def tearDown(self):
        """Clean up the test environment."""
        pygame.quit()

    def test_initialization(self):
        """Test that the TilePalettePanel initializes correctly."""
        self.assertEqual(len(self.panel.tiles), 0)
        self.assertIsNone(self.panel.selected_tile)
        self.assertIsNotNone(self.panel.theme)

    def test_add_tile(self):
        """Test adding a tile to the palette."""
        tile = pygame.Surface((32, 32))
        self.panel.add_tile(tile)
        self.assertEqual(len(self.panel.tiles), 1)
        self.assertEqual(self.panel.tiles[0], tile)

    def test_remove_tile(self):
        """Test removing a tile from the palette."""
        tile = pygame.Surface((32, 32))
        self.panel.add_tile(tile)
        self.panel.remove_tile(tile)
        self.assertEqual(len(self.panel.tiles), 0)

    def test_select_tile(self):
        """Test selecting a tile from the palette."""
        tile = pygame.Surface((32, 32))
        self.panel.add_tile(tile)
        self.panel.select_tile(tile)
        self.assertEqual(self.panel.selected_tile, tile)

    def test_clear_selection(self):
        """Test clearing the selected tile."""
        tile = pygame.Surface((32, 32))
        self.panel.add_tile(tile)
        self.panel.select_tile(tile)
        self.panel.clear_selection()
        self.assertIsNone(self.panel.selected_tile)

    def test_render(self):
        """Test rendering the tile palette panel."""
        self.panel.render(self.screen)
        # Check that the screen is not empty by checking a position within the rendered panel
        self.assertNotEqual(self.screen.get_at((15, 15)), (0, 0, 0, 255))

    def test_handle_event(self):
        """Test handling events for the tile palette panel."""
        # Create a mock event
        event = pygame.event.Event(
            pygame.MOUSEBUTTONDOWN, {"button": 1, "pos": (20, 20)}
        )
        self.panel.handle_event(event)
        # No assertion needed, just ensure no errors occur


class TestToolbarPanel(unittest.TestCase):
    def setUp(self):
        """Set up the test environment."""
        pygame.init()
        self.screen = pygame.Surface((800, 600))
        self.panel = ToolbarPanel()

    def tearDown(self):
        """Clean up the test environment."""
        pygame.quit()

    def test_initialization(self):
        """Test that the ToolbarPanel initializes correctly."""
        self.assertEqual(len(self.panel.tools), 6)
        self.assertIsNotNone(self.panel.active_tool)
        self.assertIsNotNone(self.panel.theme)

    def test_add_tool(self):
        """Test adding a tool to the toolbar."""
        initial_count = len(self.panel.tools)
        self.panel.add_tool("Test Tool", object())
        self.assertEqual(len(self.panel.tools), initial_count + 1)

    def test_set_active_tool(self):
        """Test setting the active tool in the toolbar."""
        self.panel.set_active_tool("Brush")
        self.assertIsNotNone(self.panel.active_tool)

    def test_render(self):
        """Test rendering the toolbar panel."""
        self.panel.render(self.screen)
        # Check that the screen is not empty by checking a position within the rendered panel
        self.assertNotEqual(self.screen.get_at((15, 325)), (0, 0, 0, 255))

    def test_handle_event(self):
        """Test handling events for the toolbar panel."""
        # Create a mock event
        event = pygame.event.Event(
            pygame.MOUSEBUTTONDOWN, {"button": 1, "pos": (20, 20)}
        )
        self.panel.handle_event(event)
        # No assertion needed, just ensure no errors occur


if __name__ == "__main__":
    unittest.main()

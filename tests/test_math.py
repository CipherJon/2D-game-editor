"""
Test cases for the math.py module.
This module tests the utility functions for mathematical operations.
"""

import unittest

from src.utils.math import clamp, distance, lerp, snap_to_grid


class TestMathFunctions(unittest.TestCase):
    def test_clamp_valid(self):
        """Test valid clamping operations."""
        self.assertEqual(clamp(5, 0, 10), 5)
        self.assertEqual(clamp(-5, 0, 10), 0)
        self.assertEqual(clamp(15, 0, 10), 10)
        self.assertEqual(clamp(0, 0, 10), 0)
        self.assertEqual(clamp(10, 0, 10), 10)

    def test_clamp_invalid(self):
        """Test invalid clamping operations."""
        with self.assertRaises(ValueError):
            clamp(5, 10, 0)  # min_val > max_val

    def test_lerp_valid(self):
        """Test valid linear interpolation operations."""
        self.assertEqual(lerp(0, 10, 0.5), 5.0)
        self.assertEqual(lerp(0, 10, 0.0), 0.0)
        self.assertEqual(lerp(0, 10, 1.0), 10.0)
        self.assertEqual(lerp(-5, 5, 0.5), 0.0)

    def test_lerp_invalid(self):
        """Test invalid linear interpolation operations."""
        with self.assertRaises(ValueError):
            lerp(0, 10, -0.5)  # t < 0.0
        with self.assertRaises(ValueError):
            lerp(0, 10, 1.5)  # t > 1.0

    def test_snap_to_grid_valid(self):
        """Test valid snap to grid operations."""
        self.assertEqual(snap_to_grid(5.7, 2), 6.0)
        self.assertEqual(snap_to_grid(-3.2, 2), -4.0)
        self.assertEqual(snap_to_grid(0, 2), 0.0)
        self.assertEqual(snap_to_grid(10.0, 2), 10.0)

    def test_snap_to_grid_invalid(self):
        """Test invalid snap to grid operations."""
        with self.assertRaises(ValueError):
            snap_to_grid(5, 0)  # grid_size = 0
        with self.assertRaises(ValueError):
            snap_to_grid(5, -1)  # grid_size < 0

    def test_distance_valid(self):
        """Test valid distance calculations."""
        self.assertEqual(distance(0, 0, 3, 4), 5.0)
        self.assertEqual(distance(1, 1, 1, 1), 0.0)
        self.assertEqual(distance(-1, -1, 1, 1), 2.8284271247461903)  # sqrt(8)

    def test_distance_invalid(self):
        """Test invalid distance calculations."""
        # Distance function should handle all valid float inputs
        pass


if __name__ == "__main__":
    unittest.main()

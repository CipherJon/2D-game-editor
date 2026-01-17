"""
Test cases for the color.py module.
This module tests the utility functions for color manipulation and conversion.
"""

import unittest
from src.utils.color import hex_to_rgb, rgb_to_hex, rgba_to_rgba_int

class TestColorFunctions(unittest.TestCase):
    def test_hex_to_rgb_valid(self):
        """Test valid hex color conversions."""
        self.assertEqual(hex_to_rgb("#FF0000"), (255, 0, 0))
        self.assertEqual(hex_to_rgb("00FF00"), (0, 255, 0))
        self.assertEqual(hex_to_rgb("#0000FF"), (0, 0, 255))
        self.assertEqual(hex_to_rgb("FFFFFF"), (255, 255, 255))
        self.assertEqual(hex_to_rgb("#000000"), (0, 0, 0))

    def test_hex_to_rgb_invalid(self):
        """Test invalid hex color conversions."""
        with self.assertRaises(ValueError):
            hex_to_rgb("#FF00")  # Too short
        with self.assertRaises(ValueError):
            hex_to_rgb("#FF00000")  # Too long
        with self.assertRaises(ValueError):
            hex_to_rgb("GGGGGG")  # Invalid characters

    def test_rgb_to_hex_valid(self):
        """Test valid RGB to hex conversions."""
        self.assertEqual(rgb_to_hex((255, 0, 0)), "#ff0000")
        self.assertEqual(rgb_to_hex((0, 255, 0)), "#00ff00")
        self.assertEqual(rgb_to_hex((0, 0, 255)), "#0000ff")
        self.assertEqual(rgb_to_hex((255, 255, 255)), "#ffffff")
        self.assertEqual(rgb_to_hex((0, 0, 0)), "#000000")

    def test_rgb_to_hex_invalid(self):
        """Test invalid RGB to hex conversions."""
        with self.assertRaises(ValueError):
            rgb_to_hex((256, 0, 0))  # Red out of range
        with self.assertRaises(ValueError):
            rgb_to_hex((0, 256, 0))  # Green out of range
        with self.assertRaises(ValueError):
            rgb_to_hex((0, 0, 256))  # Blue out of range
        with self.assertRaises(ValueError):
            rgb_to_hex((-1, 0, 0))  # Negative red
        with self.assertRaises(ValueError):
            rgb_to_hex((0, -1, 0))  # Negative green
        with self.assertRaises(ValueError):
            rgb_to_hex((0, 0, -1))  # Negative blue

    def test_rgba_to_rgba_int_valid(self):
        """Test valid RGBA to integer conversions."""
        self.assertEqual(rgba_to_rgba_int((255, 0, 0, 255)), 4278190080)
        self.assertEqual(rgba_to_rgba_int((0, 255, 0, 255)), 4278255360)
        self.assertEqual(rgba_to_rgba_int((0, 0, 255, 255)), 4278190335)
        self.assertEqual(rgba_to_rgba_int((255, 255, 255, 255)), 4294967295)
        self.assertEqual(rgba_to_rgba_int((0, 0, 0, 0)), 0)

    def test_rgba_to_rgba_int_invalid(self):
        """Test invalid RGBA to integer conversions."""
        with self.assertRaises(ValueError):
            rgba_to_rgba_int((256, 0, 0, 255))  # Red out of range
        with self.assertRaises(ValueError):
            rgba_to_rgba_int((0, 256, 0, 255))  # Green out of range
        with self.assertRaises(ValueError):
            rgba_to_rgba_int((0, 0, 256, 255))  # Blue out of range
        with self.assertRaises(ValueError):
            rgba_to_rgba_int((0, 0, 0, 256))  # Alpha out of range
        with self.assertRaises(ValueError):
            rgba_to_rgba_int((-1, 0, 0, 255))  # Negative red
        with self.assertRaises(ValueError):
            rgba_to_rgba_int((0, -1, 0, 255))  # Negative green
        with self.assertRaises(ValueError):
            rgba_to_rgba_int((0, 0, -1, 255))  # Negative blue
        with self.assertRaises(ValueError):
            rgba_to_rgba_int((0, 0, 0, -1))  # Negative alpha

if __name__ == "__main__":
    unittest.main()
```

### Summary of Changes:
1. **Added Test Cases**: Added comprehensive test cases for the `hex_to_rgb`, `rgb_to_hex`, and `rgba_to_rgba_int` functions.
2. **Tested Edge Cases**: Included tests for invalid inputs, such as out-of-range values and invalid formats.
3. **Added Documentation**: Added detailed docstrings for the test class and methods.
4. **Improved Readability**: Used descriptive method names and comments to improve readability.

These changes ensure that the `color.py` module is thoroughly tested and handles edge cases appropriately.

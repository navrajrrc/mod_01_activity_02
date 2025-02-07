"""This module defines the TestTriangle class.

Usage: 
    To execute all tests in the terminal execute the following command:

    $ python -m unittest tests/test_triangle.py
"""

__author__ = "Navraj singh"
__version__ = ""

import unittest
import math
from shape.triangle import Triangle

class Triangletests(unittest.TestCase):
    """
    This is a class for tests for the triangleclass.
    """
    def setup(self):
        """
        This method is to setup the attributes.
        """
        self.triangle = Triangle("black", 4, 5, 6)

    def test_blank_color(self):
        """
        This test will raise a valueError if the color is blank.
        """
        with self.assertRaises(ValueError):
            self.triangle = Triangle(" ", 4, 5, 6)
    
    def test_invalid_side_1(self):
        """
        This test will raise a ValueError if the side_1 is not an integar.
        """
        with self.assertRaises(ValueError):
            self.triangle = Triangle("black", "ns", 5, 6)
        
    def test_invalid_side_2(self):
        """
        This test will raise a ValueError if the side_2 is not an integar.
        """
        with self.assertRaises(ValueError):
            self.triangle = Triangle("black", 4, "ns", 6)

    def test_invalid_side_3(self):
        """
        This test will raise a ValueError if the side_3 is not an integar.
        """
        with self.assertRaises(ValueError):
            self.triangle = Triangle("black", 4, 5,"ns")

    def test_str_format(self):
        """
        This is a test to check the string is created in the expected format.
        """
        self.triangle = Triangle("black", 4, 5, 6)
        expected_str = ( "The shape color is black.\n This triangle has three sides with the lengths of 4, 5, and 6 centimeters.")
        self.assertEqual(str(self.triangle), expected_str)

    def test_calaculate_area(self):
        """
        This test is to check if it returns the correct calculated area.
        """
        self.triangle = Triangle("black", 4, 5, 6)
        perimeter = (4 + 5 + 6) / 2
        expected_area = math.sqrt(perimeter * (perimeter - 4) * (perimeter - 5) * (perimeter - 6))
        self.assertAlmostEqual(self.triangle.calcualte_area(), expected_area)

    def test_calculate_perimeter(self):
        """
        This test is to check if it returns the correct calculated perimeter.
        """
        self.triangle = Triangle("black", 4, 5, 6)
        expected_perimeter = 4 + 5 + 6
        self.assertEqual(self.triangle.calculate_perimeter(), expected_perimeter)

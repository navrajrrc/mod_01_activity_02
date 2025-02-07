"""This module defines the TestTriangle class.

Usage: 
    To execute all tests in the terminal execute the following command:

    $ python -m unittest tests/test_triangle.py
"""

__author__ = ""
__version__ = ""

import unittest
import math
from shape.triangle import Triangle

class Triangletests(unittest.TestCase):
    """
    
    """
    def setup(self):
        """
        
        """
        self.triangle = Triangle("black", 4, 5, 6)

    def test_blank_color(self):
        """
        
        """
        with self.assertRaises(ValueError):
            self.triangle = Triangle(" ", 4, 5, 6)
    
    def test_invalid_side_1(self):
        """
        
        """
        with self.assertRaises(ValueError):
            self.triangle = Triangle("black", "ns", 5, 6)
        
    def test_invalid_side_2(self):
        """
        
        """
        with self.assertRaises(ValueError):
            self.triangle = Triangle("black", 4, "ns", 6)

    def test_invalid_side_3(self):
        """
        
        """
        with self.assertRaises(ValueError):
            self.triangle = Triangle("black", 4, 5,"ns")

    def test_str_format(self):
        """
        
        """
        self.triangle = Triangle("black", 4, 5, 6)
        expected_str = ( "The shape color is black.\n This triangle has three sides with the lengths of 4, 5, and 6 centimeters.")
        self.assertEqual(str(self.triangle), expected_str)

    def test_calaculate_area(self):
        """
        
        """
        self.triangle = Triangle("black", 4, 5, 6)
        perimeter = (4 + 5 + 6) / 2
        expected_area = math.sqrt(perimeter * (perimeter - 4) * (perimeter - 5) * (perimeter - 6))
        self.assertAlmostEqual(self.triangle.calcualte_area(), expected_area)

    def test_calculate_perimeter(self):
        """
        
        """
        self.triangle = Triangle("black", 4, 5, 6)
        expected_perimeter = 4 + 5 + 6
        self.assertEqual(self.triangle.calculate_perimeter(), expected_perimeter)
        
"""This module defines the Rectangle class."""

__author__ = "Navraj singh"
__version__ = ""

from shape.shape import Shape
import math

class Rectangle(Shape):
    """
    This is a class for the shape rectangle.
    """
    def __init__(self, color: str, length:int, width:int):
        """
        Attributes:
            color: (str) color of the shape.
            length: (int) the length of the rectangle in centimeters.
            width: (int) the width of the rectangle in centimeters.
        """
        super().__init__(color)
        if not isinstance(length, int):
            raise ValueError("Length must be numeric.")
        self._length = length

        if not isinstance(width,int):
            raise ValueError("Width must be numeric")
        self._width = width

    def __str__(self) -> str:
        """
        this method will return the string in the formatted way.
        """
        value = super().__str__()
        value+= f"\nThis rectangle has four sides with the lengths of {self._length}, {self._width}, {self._length} and {self._width} centimeters."
        return value
    
    def calculate_area(self) -> float:
        """
        this method is to calcualte the area of the rectangle.
        """
        return self._length * self._width
    
    def calculate_perimeter(self) -> float:
        """
        this method is to calculate the perimeter of the rectangle.
        """
        return 2 * self._length + 2 * self._width
    

    


"""This module defines the Rectangle class."""

__author__ = "Navraj singh"
__version__ = ""

from shape.shape import Shape
import math

class rectangle(Shape):
    """
    This is a class for the shape rectangle.
    """
    def __init__(self, color: str, length:int, width:int):
        """
        
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
        
        """
        value = super().__str__()
        value+= f"\n This rectangle has four sides with the lengths of {{length}}, {{width}}, {{length}} and {{width}} centimeters."
        return value
    
    def _calculate_area(self) -> float:
        """
        
        """
        return self._length * self._width
    
    def calculate_perimeter(self) -> float:
        """
        
        """
        return 2 * self._length + 2 * self._width
    


"""This module defines the Triangle class."""

__author__ = "Navraj singh"
__version__ = ""

from shape.shape import Shape
import math

class Triangle(Shape):
    """
    This is a class for the triangle shape and will contain 
    its attributes and valuerrros.
    Attributes:
        side_1: Represents the length of the first side of the Triangle in centimeters.
        side_2: Represents the length of the second side of the Triangle in centimeters.
        side_3: Represents the lenght of the third side of the Triangle in centimeters.
    """
    def __init__(self, color: str, side_1:int, side_2: int, side_3:int):
        super().__init__(color)

        if not isinstance(side_1, int):
            raise ValueError("Side 1 must be numeric")
        if not isinstance(side_2, int):
            raise ValueError("Side 2 must be numeric")
        if not isinstance(side_3, int):
            raise ValueError("Side 3 must be numeric")
        
        if not (side_1 + side_2 > side_3 and
                side_1 + side_3 > side_2 and 
                side_2 + side_3 > side_1):
            raise ValueError("The sides do not satisfy the Triangle Inequality Theorem.")
        
        self._side_1 = side_1
        self._side_2 = side_2
        self._side_3 = side_3

    def __str__(self) -> str:
        """
        
        """
        value = super().__str__()
        value+= f"\n This triangle has three sides with the lenghts of {self._side_1}, {self._side_2}, and {self._side_3} centimeters."
        return value
    
    def calcualte_area(self) -> float:
        """
        
        """
        semi_perimeter = (self._side_1 + self._side_2 + self._side_3) / 2
        area = math.sqrt(semi_perimeter * (semi_perimeter - self._side_1) *
                         (semi_perimeter - self._side_2) * (semi_perimeter - self._side_3))
        return area 
    
    def calculate_perimeter(self) -> float:
        """
        
        """
        return (self._side_1 + self._side_2 + self._side_3)
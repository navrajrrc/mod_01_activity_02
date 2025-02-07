"""This module defines the Shape class."""

__author__ = "Navraj singh"
__version__ = ""

from abc import ABC, abstractmethod

class Shape(ABC): 
    """
    A shape class with color, str, calculate area and calculate perimeter
    """
    def __init__(self, color: str):
        """
        Attributes:
            
        """
        if len(color.strip()) == 0:
            raise ValueError("Color cannot be blank")
        self._color = color.strip()

    def __str__(self) -> str:
        return f"The shape color is {self._color}."
    
    @abstractmethod
    def calcualte_area(self) -> float:
        pass

    @abstractmethod
    def calculate_perimeter(Self) -> float:
        pass
""""A client program written to verify correctness of the activity 
classes.
"""

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Navraj singh"

from shape import *


def main():
    """
    Test the functionality of the methods encapsulated 
    in this project.
    """

    # In the statements coded below, ensure that any statement that 
    # could result in an exception is handled.  When exceptions are 
    # 'caught', display the exception message to the console.

    # *** PART 1 ***
    print("*************PART 1****************")

    # 1. Create an empty list of Shape objects.
    shapes = []


    # 2. Code a statement which creates an instance of the Triangle 
    # class.
    # Append the Triangle to the list of shapes.
    try:
        triangle = Triangle("black", 4, 5, 6)
        shapes.append(triangle)
    except ValueError:
        print(f"Error in creating a Triangle")

    # 3. Code a statement which creates an instance of the Rectangle 
    # class.
    # Append the Rectangle to the list of shapes.
    try:
        rectangle = Rectangle("white", 4, 6)
        shapes.append(rectangle)
    except ValueError:
        print(f"Error in creating a rectangle")



    # 4. Code 3 additional statements which creates an instance of 
    # Triangle or Rectangle classes (your choice).
    # Append these instances to the list of shapes.
    try:
        triangle1 = Triangle("red", 7, 6, 8)
        shapes.append(triangle1)

        triangle2 = Triangle("blue", 6, 8,10)
        shapes.append(triangle2)

        rectangle1 = Rectangle("Orange", 6,9)
        shapes.append(rectangle1)
    except ValueError:
        print(f"Error in creating the shapes.")

    # 5. Iterate through the list of shapes.  
    # On each iteration:
    # - print the shape
    # - print the area of the shape to 2 decimal places
    # - print the perimeter of the shape to 2 decimal places
    for shape in shapes:
        try:
            print(shape)
            print(f"Area: {shape.calcualte_area():.2f}cm2")
            print(f"Perimeter: {shape.calculate_perimeter():.2f} cm")
        except Exception:
            print(f"Error in the shape understanding")
    # *** END PART 1 ***


if __name__ == "__main__":
    main()
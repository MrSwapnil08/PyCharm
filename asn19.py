#Create Polygon class with a method that accepts the number of sides using inputSides() method.
# Derive Triangle class from Polygon class. Write area() method in the Triangle class.
# Create an object to Triangle class and call the inputSides() and pass number of sides as 3.
# Then display area of triangle by calling area().

import math

class Polygon:
    def __init__(self):
        self.sides = []

    def setSides(self, sides):
        num_sides = len(sides)
        if num_sides < 3:
            raise ValueError("A polygon must have at least 3 sides.")
        self.sides = sides

class Triangle(Polygon):
    def __init__(self):
        super().__init__()

    def area(self):
        if len(self.sides) != 3:
            raise ValueError("Triangle must have exactly 3 sides.")
        a, b, c = self.sides
        s = (a + b + c) / 2  # Semi-perimeter
        # Calculate area using Heron's formula
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area

# Create an object of the Triangle class
triangle = Triangle()

# Set sides for the triangle
triangle.setSides([3.0, 4.0, 5.0])

# Display the area of the triangle
try:
    print(f"The area of the triangle is: {triangle.area()} square units.")
except ValueError as e:
    print(e)

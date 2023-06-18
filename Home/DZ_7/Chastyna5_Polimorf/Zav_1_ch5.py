import math

class Figure:
    def calculate_area(self):
        pass

class Rectangle(Figure):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius**2

class RightTriangle(Figure):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def calculate_area(self):
        return 0.5 * self.base * self.height

class Trapezoid(Figure):
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height
    
    def calculate_area(self):
        return 0.5 * (self.base1 + self.base2) * self.height

rectangle = Rectangle(4, 5)
print("Площа прямокутника:", rectangle.calculate_area())

circle = Circle(3)
print("Площа кола:", circle.calculate_area())

triangle = RightTriangle(3, 4)
print("Площа прямокутного трикутника:", triangle.calculate_area())

trapezoid = Trapezoid(3, 6, 4)
print("Площа трапеції:", trapezoid.calculate_area())
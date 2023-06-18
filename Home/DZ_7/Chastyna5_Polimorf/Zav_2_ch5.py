import math

class Figure:
    def calculate_area(self):
        pass

    def __int__(self):
        return self.calculate_area()

    def __str__(self):
        return "Це фігура."

class Rectangle(Figure):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width
    
    def __int__(self):
        return int(self.calculate_area())
    
    def __str__(self):
        return f"Це прямокутник з шириною {self.width}, та довжиною {self.length}."

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius**2
    
    def __int__(self):
        return int(self.calculate_area())
    
    def __str__(self):
        return f"Це коло з радіусом {self.radius}."


class RightTriangle(Figure):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def calculate_area(self):
        return 0.5 * self.base * self.height
    
    def __int__(self):
        return int(self.calculate_area())
    
    def __str__(self):
        return f"Це прямокутний трикутник з основою {self.base}, та висотою {self.height}."


class Trapezoid(Figure):
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height
    
    def calculate_area(self):
        return 0.5 * (self.base1 + self.base2) * self.height
    
    def __int__(self):
        return int(self.calculate_area())
    
    def __str__(self):
        return f"Це трапеція з основами {self.base1},{self.base2} та висотою {self.height}."

rectangle = Rectangle(4, 5)
print("Площа прямокутника:", rectangle.calculate_area())
print(int(rectangle))
print(str(rectangle))
circle = Circle(4)
print("Площа кола:", circle.calculate_area())
print(int(circle))
print(str(circle))

triangle = RightTriangle(3, 4)
print("Площа прямокутного трикутника:", triangle.calculate_area())

trapezoid = Trapezoid(3, 6, 4)
print("Площа трапеції:", trapezoid.calculate_area())
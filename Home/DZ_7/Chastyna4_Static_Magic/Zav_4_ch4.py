class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __add__(self, other):
        new_radius = self.radius + other.radius
        return Circle(new_radius)

    def __sub__(self, other):
        new_radius = self.radius - other.radius
        return Circle(new_radius)

    def __iadd__(self, other):
        self.radius += other.radius
        return self

    def __isub__(self, other):
        self.radius -= other.radius
        return self

circle1 = Circle(5)
circle2 = Circle(7)
print(circle1 == circle2)
print(circle1 < circle2)
print(circle1 + circle2)
print(circle2 - circle1)
circle1 += circle2
print(circle1.radius)
circle2 -= circle1
print(circle2.radius)

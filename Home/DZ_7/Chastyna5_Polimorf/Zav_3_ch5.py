import pickle

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def Show(self):
        pass
    
    def Save(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
    
    @staticmethod
    def Load(filename):
        with open(filename, 'rb') as file:
            shape = pickle.load(file)
        return shape


class Square(Shape):
    def __init__(self, x, y, side_length):
        super().__init__(x, y)
        self.side_length = side_length
    
    def Show(self):
        print("Square:")
        print("Top-left coordinates:", self.x, self.y)
        print("Side length:", self.side_length)


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height
    
    def Show(self):
        print("Rectangle:")
        print("Top-left coordinates:", self.x, self.y)
        print("Width:", self.width)
        print("Height:", self.height)


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius
    
    def Show(self):
        print("Circle:")
        print("Center coordinates:", self.x, self.y)
        print("Radius:", self.radius)


class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height
    
    def Show(self):
        print("Ellipse:")
        print("Top-left coordinates:", self.x, self.y)
        print("Width:", self.width)
        print("Height:", self.height)



shapes = [
    Square(10, 10, 50),
    Rectangle(20, 20, 80, 40),
    Circle(30, 30, 25),
    Ellipse(40, 40, 60, 30)
]


filename = "shapes_data.bin"
with open(filename, 'wb') as file:
    pickle.dump(shapes, file)


loaded_shapes = []
with open(filename, 'rb') as file:
    loaded_shapes = pickle.load(file)


for shape in loaded_shapes:
    shape.Show()
    print()

class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        real_part = self.real + other.real
        imaginary_part = self.imaginary + other.imaginary
        return Complex(real_part, imaginary_part)

    def __sub__(self, other):
        real_part = self.real - other.real
        imaginary_part = self.imaginary - other.imaginary
        return Complex(real_part, imaginary_part)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imaginary_part = self.real * other.imaginary + self.imaginary * other.real
        return Complex(real_part, imaginary_part)

    def __truediv__(self, other):
        denominator = other.real**2 + other.imaginary**2
        real_part = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        imaginary_part = (self.imaginary * other.real - self.real * other.imaginary) / denominator
        return Complex(real_part, imaginary_part)

    def __str__(self):
        return f"{self.real} + {self.imaginary}"

complex1 = Complex(2, 3)
complex2 = Complex(4, 5)
sum_result = complex1 + complex2
print(f"Сума: {sum_result}")
difference_result = complex1 - complex2
print(f"Різниця: {difference_result}")
product_result = complex1 * complex2
print(f"Добуток: {product_result}")
quotient_result = complex1 / complex2
print(f"Частка: {quotient_result}")

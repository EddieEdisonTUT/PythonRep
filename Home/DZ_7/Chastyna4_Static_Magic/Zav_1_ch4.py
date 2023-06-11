class Fraction:
    count = 0

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        Fraction.count += 1

    def display(self):
        print(f"{self.numerator}/{self.denominator}")

    @staticmethod
    def get_count():
        return Fraction.count

fraction1 = Fraction(1, 2)
fraction2 = Fraction(3, 4)
fraction3 = Fraction(2, 5)

fraction1.display()
fraction2.display()
fraction3.display()
print(Fraction.get_count())

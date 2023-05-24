class calculation_area:
    count = 0

    @staticmethod
    def s_triangle(s1,h2):
        calculation_area.count += 1
        return s1 * h2 * 0.5

    @staticmethod
    def S_triangle(a,b):
        calculation_area.count += 1
        return a * b * 0.5

    @staticmethod
    def s_prymokut(a,b):
        calculation_area.count += 1
        return a * b

    @staticmethod
    def s_kvadrat(l):
        calculation_area.count += 1
        return l * l

    @staticmethod
    def s_romb(d1,d2):
        calculation_area.count += 1
        return d1 * d2 / 2

    @staticmethod
    def get_count():
        return calculation_area.count

s = calculation_area()
print(s)
c = calculation_area.s_triangle(2,3)
r = calculation_area.S_triangle(4,6)
print('Площа трикутника 1 метод: ', c, 'Площа трикутника 2 метод: ', r)
j = calculation_area.s_prymokut(4,6)
print('Площа прямокутника:', j)
k = calculation_area.s_kvadrat(8)
print('Площа квадрату:', k)
f = calculation_area.s_romb(2,5)
print('Площа ромбу:', f)
print(calculation_area.get_count())


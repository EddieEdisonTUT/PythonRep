def spylniy_dilnyk(a, b):
    if b == 0:
        return a
    else:
        return spylniy_dilnyk(b, a % b)

num1 = 15
num2 = 45
gcd = spylniy_dilnyk(num1, num2)
print("Найбільший загальний дільник чисел", num1, "і", num2, "=", gcd)

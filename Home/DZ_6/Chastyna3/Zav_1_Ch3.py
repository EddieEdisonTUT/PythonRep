def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)

num1 = 36
num2 = 24
gcd = gcd_recursive(num1, num2)
print("Найбільший загальний дільник чисел", num1, "і", num2, "=", gcd)

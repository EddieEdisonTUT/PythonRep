n = input('Введіть арифметичний вираз: ')

number1, operator, number2  = n.split()
number1 = float(number1)
number2 = float(number2)

if operator == '+':
    res = number1 + number2
elif operator == '-':
    res = number1 - number2
elif operator == '*':
    res = number1 * number2
elif operator == '/':
    res = number1 / number2
else:
    print('Невірний ввод')

print(res)
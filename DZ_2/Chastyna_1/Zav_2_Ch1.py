number1 = int(input('Перше число: '))
number2 = int(input('Друге число: '))
number3 = int(input('Третє число: '))

print('Зробіть вибір')
print('1: Максимум')
print('2: Мінімум')
print('3: Середне')
choise = int(input('Ваш вибір: '))
if choise == 1:
    if number1 > number2 and number1 > number3:
        print(number1)
    elif number2 > number1 and number2 > number3:
        print(number2)
    else:
        print(number3)
elif choise == 2:
    if number1 < number2 and number1 < number3:
        print(number1)
    elif number2 < number1 and number2 < number3:
        print(number2)
    else:
        print(number3)
elif choise == 3:
    print((number1 + number2 + number3) // 3)

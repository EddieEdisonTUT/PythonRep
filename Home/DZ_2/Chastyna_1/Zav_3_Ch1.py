number1 = int(input('Кількість метрів: '))

print('Зробіть вибір')
print('1: Милі')
print('2: Дюйми')
print('3: Ярди')
choise = int(input('Ваш вибір: '))
if choise == 1:
    print(number1 * 0.00062)
elif choise == 2:
    print(number1 * 39.37007)
elif choise == 3:
    print(number1 * 1.09361)
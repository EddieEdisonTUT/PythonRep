number1 = int(input('First number: '))
number2 = int(input('Second number: '))
print('Zrobit vybir')
print('1: summa')
print('2: riznytsya')
print('3: seredne')
print('4: mnoghennya')
choise = int(input('Ваш вибір: '))
if choise == 1:
    print(number1 + number2)
elif choise == 2:
    print(number1 - number2)
elif choise == 3:
    print((number1 + number2) / 2)
elif choise == 4:
    print(number1 * number2)
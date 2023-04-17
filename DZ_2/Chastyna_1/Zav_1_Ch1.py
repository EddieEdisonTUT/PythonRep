number1 = int(input('First number: '))
number2 = int(input('Second number: '))
number3 = int(input('Thrid number: '))
print('Zrobit vybir')
print('1: summa')
print('2: mnoghennya')
choise = int(input('Ваш вибір: '))
if choise == 1:
    print(number1 + number2 + number3)
elif choise == 2:
    print(number1 * number2 * number3)
number = int(input('Введіть ваше число:'))
print('Оберіть ступінь зведення')
print('1: 0')
print('2: 1')
print('3: 2')
print('4: 3')
print('5: 4')
print('6: 5')
print('7: 6')
print('8: 7')
choise = int(input('Ваш вибір:'))
if choise == 1:
    print(number ** 0)
elif choise == 2:
    print(number ** 1)
elif choise == 3:
    print(number ** 2)
elif choise == 4:
    print(number ** 3)
elif choise == 5:
    print(number ** 4)
elif choise == 6:
    print(number ** 5)
elif choise == 7:
    print(number ** 6)
elif choise == 8:
    print(number ** 7)
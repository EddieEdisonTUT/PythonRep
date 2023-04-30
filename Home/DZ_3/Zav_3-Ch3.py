stm = int(input('Введіть вартість розмови: '))
print('Оберіть операторів')
print('1)Київстар > Лайф')
print('2)Київстар > Водафон ')
print('3)Водафон > Лайф')

choise = int(input('Зробіть ваш вибір: '))
if choise == 1:
    print('Київстар > Лайф', stm, 'грн')
elif choise == 2:
    print('Київстар > Водафон', stm, 'грн')
elif choise == 3:
    print('Водафон > Лайф', stm, 'грн')

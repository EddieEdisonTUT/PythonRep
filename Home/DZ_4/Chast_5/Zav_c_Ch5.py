print('Створення фігур')

b = int(input('Оберіть розмір фігури: '))

for i in range(b):
    print(' ' * i, '*' * (b - 2 * i),' ' * i, sep='')
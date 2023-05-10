print('Створення фігур')

b = int(input('Оберіть розмір фігури: '))

for i in range(b,0,-1):
    print(' ' * i, '*' * (b - 2 * i),' ' * i, sep='')
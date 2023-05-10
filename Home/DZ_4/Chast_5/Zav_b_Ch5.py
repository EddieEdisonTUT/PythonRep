print('Створення фігур')

b = int(input('Оберіть розмір фігури: '))

for i in range(1,b+1):
    print('*' * i, ' ' * (b - i), sep='')
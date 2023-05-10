print('Створення фігур')

b = int(input('Оберіть розмір фігури: '))

for i in range(b):
    print(' ' * i,'*' * (b-i), sep='')

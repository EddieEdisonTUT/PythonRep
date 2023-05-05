print('Створення фігур')

b = int(input('Оберіть розмір фігури: '))

for i in range(b//2):
    print(' ' * i, '*' * (b - 2*i),' ' * i, sep='')
for i in range(b//2,-1,-1):
    print(' ' * i, '*' * (b - 2*i),' ' * i, sep='')
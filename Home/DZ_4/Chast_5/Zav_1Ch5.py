print('Створення фігур')
a = str(input('Оберіть символ яким запониться фігура: '))
b = int(input('Оберіть розмір фігури: '))

for i in range(b):
    print(' '*(b-i), a*i, sep='')
#Pryklad
for i in range(b//2):
    print('*'*(i+1),(b-2))
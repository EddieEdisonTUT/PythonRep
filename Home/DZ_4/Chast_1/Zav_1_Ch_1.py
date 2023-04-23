a = int(input('Введіть перше число: '))
b = int(input('Введіть друге число: '))

while a <= b:
    if a % 7 == 0:
       print(a, end=' ')
    a += 1  
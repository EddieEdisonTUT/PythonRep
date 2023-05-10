n = int(input('Введіть 1 число: '))
m = int(input('Введіть 2 число: '))

while n <= m:
    if n % 2 != 0:
       print(n, end=' ')
    n += 1  
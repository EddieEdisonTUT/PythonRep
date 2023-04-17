n = int(input('Введіть 1 число: '))
m = int(input('Введіть 2 число: '))
if n > m:
    n,m = m,n

while n <= m:
    if n % 2 != 0:
       print(n, end=' ')
    n += 1  

a = int(input('Введіть перше число: '))
b = int(input('Введіть друге число: '))
i = 0
j = b
k = a
while a <= b:
    print(a, end=' ')
    a += 1
    print(j, end=' ')
    j -= 1
if a % 7 == 0:
    print(k, end=' ')
    k += 1  
if a % 5 == 0:
    i += a
    print(i, end=' ')

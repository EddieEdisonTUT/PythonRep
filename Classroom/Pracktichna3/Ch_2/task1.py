n = int(input('Введіть 1 число: '))
m = int(input('Введіть 2 число: '))
sum = 0
y = n
while n <= m:
    #print(n, end=' ')
    n += 1
    sum += n
    # y += 1 
else:
    print('Сумма:', sum)
    print('Середне:', sum/(m-y+1))

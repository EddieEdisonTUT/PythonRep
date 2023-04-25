a = int(input('Введіть число: '))    #Варіант з вайл
b = int(input('Введіть число: '))
i = 1
for i in range(a,b+1):
    for j in range(1,11):
        print(i, '*',j,'=',j*i)
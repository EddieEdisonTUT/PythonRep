a = int(input('Введіть число: '))    #Варіант з вайл
b = int(input('Введіть число: '))
i = 1
while i < 11:
    if a <= b:
        a += 1
        print(a, '*',i,'=',a*i)
    i += 1
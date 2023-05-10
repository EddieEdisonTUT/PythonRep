a = int(input('Введіть число: '))   #Варіант з фор
for i in range(1,11):
    print(a, '*',i,'=',a*i)

a = int(input('Введіть число: '))    #Варіант з вайл
i = 1
while i < 11:
    print(a, '*',i,'=',a*i)
    i += 1
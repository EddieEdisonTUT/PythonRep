


n = int(input('Введіть кількість чисел: '))
lst = []
for i in range(n):
    lst.append(int(input('Номер['+str(i)+'] = ')))


print('Сумма = ',sum(lst))
print('Середне = ',sum(lst)/n)
n = int(input('Введіть кількість чисел: '))
lst = []
for i in range(n):
    lst.append(int(input('Номер['+str(i)+'] = ')))
number = int(input('Введіть число = '))
count = lst.count(number)

print(count)

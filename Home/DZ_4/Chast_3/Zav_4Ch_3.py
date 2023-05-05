n = int(input('Введіть ціле число: '))
m = ''

for i in str(n):
    if i != '3' and i != '6':
        m += i

print("Результат: ", m)

n = int(input('Ваше 1 число: '))
m = int(input('Ваше 2 число: '))
if n == m:
    print('Числа рівні')
elif n < m:
    print(n , m, sep=',')
elif n > m:
    print(m , n, sep=',')
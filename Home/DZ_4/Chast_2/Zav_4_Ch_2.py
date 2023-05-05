while True:
    n = int(input('Введіть число: '))
    m = int(input('Введіть число: '))
    while n != 7:
        if n > m:
            print('Максимум: ',n)
            print('Сумма: ',(n+m))
            print('Мінімум: ',m)
            break
        elif n < m:
            print('Максимум: ',m)
            print('Сумма: ',(n+m))
            print('Мінімум: ',n)
            break
        elif n == m:
            print('Сумма: ',(n+m))
            break
        else:
            pass
    else:
        print('Програма завершила роботу "Good bye!"')
        break
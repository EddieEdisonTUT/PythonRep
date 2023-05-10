while True:
    n = int(input('Введіть число:'))

    while n != 7:
        if n == 0:
            print('""Number is equal to zero"')
            break
        elif n > 0:
            print('"Number is positive"')
            break
        elif n < 0:
            print('"Number is negative"')
            break
        else:
            pass
    else:
        print('Програма завершила роботу "Good bye!"')
        break
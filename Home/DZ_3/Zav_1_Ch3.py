number = int(input('Введіть число: '))
if number < 1 or number > 100:
        print('Помилка вводу')
elif number % 3 == 0 and number % 5 == 0:
    print('Fizz Buzz')
else:
    if number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)
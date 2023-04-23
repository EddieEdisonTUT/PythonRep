a = int(input('Введіть перше число: '))
b = int(input('Введіть друге число: '))

while a <= b:
    if a % 3 == 0 and a % 5 == 0:
        print('Fizz Buzz', end='-')
        a += 1
    elif a % 3 == 0:
        print('Fizz', end='-')
        a += 1
    elif a % 5 == 0:
        print('Buzz', end='-')
        a += 1
    else:
        print(a, end='-')
        a += 1
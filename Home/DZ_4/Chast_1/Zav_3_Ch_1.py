a = int(input('Введіть перше число: '))
b = int(input('Введіть друге число: '))

while a <= b:
    if a % 3 == 0 and a % 5 == 0:
        print('FizzBuzz', end='\n')
        a += 1
    elif a % 3 == 0:
        print('Fizz', end='\n')
        a += 1
    elif a % 5 == 0:
        print('Buzz', end='\n')
        a += 1
    else:
        print(a, end='\n')
        a += 1
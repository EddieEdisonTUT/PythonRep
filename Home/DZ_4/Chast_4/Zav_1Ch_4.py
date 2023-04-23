a = int(input('number1: '))
b = int(input('number2: '))
i = 0
while a <= b:
    if i % a == 0 and i % 1 == 0:
        print(i)
    a += 1
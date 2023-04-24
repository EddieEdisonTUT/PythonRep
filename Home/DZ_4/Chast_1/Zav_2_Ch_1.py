a = int(input('Введіть перше число: '))
b = int(input('Введіть друге число: '))
a0 = a
b0 = b

i = 0

while a <= b:
    print(a, end=' ')
    a += 1

a = a0
print()
while a <= b:
    print(b, end=' ')
    b -= 1
a = a0
b = b0
print()
while a <= b:
    if a % 7 == 0:
        print(a, end=' ')
    a += 1
a = a0
b = b0
i = 0
print()
while a <= b:  
    if a % 5 == 0:
        i += 1
    a += 1
else:
    print(i, end=' ')
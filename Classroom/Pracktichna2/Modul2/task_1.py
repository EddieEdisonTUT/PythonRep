number1 = int(input('Time in seconds: ')) #7200 sec primer
print('Zrobit vybir')
print('1: godyny')
print('2: hvylyny')
print('3: seconds')
choice = int(input('Vash vybir: '))
if choice == 1:
    a = 43200 - number1
    b = a / 60
    c = b / 60
    print(c)
elif choice == 2:
    a = 43200 - number1
    b = a / 60
    print(b)
elif choice == 3:
    a = 43200 - number1
    print(a)
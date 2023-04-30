n = str(input('Введіть строку: '))

name1 = n[::1] 
name2 = n[::-1]
print(name1)
print(name2)
if name1 == name2:
    print('Паліндром')
else:
    print('Не паліндром')
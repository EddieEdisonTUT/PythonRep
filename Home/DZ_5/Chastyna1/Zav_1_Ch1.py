n = str(input('Введіть строку: '))
n2 = n.replace(' ', '')
name1 = n2[::1] 
name2 = n2[::-1]
print(name1)
print(name2)
if name1 == name2:
    print('Паліндром')
else:
    print('Не паліндром')
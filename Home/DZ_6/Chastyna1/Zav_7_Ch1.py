def number_digit(number):
    spysok = [number]

    name1 = spysok[::1] 
    name2 = spysok[::-1]
    print(name1)
    print(name2)
    if name1 == name2:
        print('Паліндром')
    else:
        print('Не паліндром')

res = number_digit(123421)
print(res)
def number_digit(number):
    spysok = str(number)
    name2 = spysok[::-1]
    print(spysok)
    print(name2)
    if spysok == name2:
        print('Паліндром')
        return True
    else:
        print('Не паліндром')
        return False

res1 = number_digit(546645)
print(res1)
res2 = number_digit(325278)
print(res2)
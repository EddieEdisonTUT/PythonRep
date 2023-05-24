def number_digit(number):
    spysok = [number]

    num1 = spysok[::1]
    count_number = spysok.count(num1)
    print(num1)
    print(count_number)

res = number_digit(3456)
print(res)
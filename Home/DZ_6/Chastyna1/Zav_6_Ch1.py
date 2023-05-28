def number_digit(number):
    spysok = [number]
    num1 = spysok[::1]
    
    print(num1)
    return len(str(number))

a = number_digit(3456)
print(a)
def display_even_numbers(n1,n2):
    if n1 > n2:
        small = n2
        larg = n1
    else:
        small = n1
        larg = n2

    for i in range(small+1,larg):
        if i % 2 == 0:
            print(i)

a = display_even_numbers(1,10)
print(a)
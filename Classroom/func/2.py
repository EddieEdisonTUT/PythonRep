
def display_odd_numbers(n1,n2):
    if n1 > n2:
        small = n2
        larg = n1
    else:
        small = n1
        larg = n2

    for i in range(small+1,larg):
        if i % 2 != 0:
            print(i, end = ' ')

display_odd_numbers(10,0)

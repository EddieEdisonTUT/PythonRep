def multipl_number(lower_bound, upper_bound):
    if lower_bound > upper_bound:
        lower_bound, upper_bound = upper_bound, lower_bound
    
    product = 1
    for i in range(lower_bound, upper_bound + 1):
        product *= i
    
    return product

res1 = multipl_number(1, 5)
res2 = multipl_number(7, 3)

print(res1)
print(res2)

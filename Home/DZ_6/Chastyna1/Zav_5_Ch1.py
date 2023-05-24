def multipl_number(lower_bound, upper_bound):
    if lower_bound > upper_bound:
        lower_bound, upper_bound = upper_bound, lower_bound
    
    product = 1
    for num in range(lower_bound, upper_bound + 1):
        product *= num
    
    return product

res1 = multipl_number(5, 25)
res2 = multipl_number(10, 3)

print(res1)
print(res2)

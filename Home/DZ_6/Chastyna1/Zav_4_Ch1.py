def min_number(number):
    min = number[0]
    for i in number:
        if i < min:
            min = i
    return min

number_list = [3, 6, 2, 8, 9]
res = min_number(number_list)
print(res)
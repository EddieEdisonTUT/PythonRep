def find_minimum(number):
    minimum = number[0] 
    for i in number:
        if i < minimum:
            minimum = i
    return minimum

numbers_list = [5, 3, 8, 2, 9, 7]
res = find_minimum(numbers_list)

print("Мінімум у списку:", res)

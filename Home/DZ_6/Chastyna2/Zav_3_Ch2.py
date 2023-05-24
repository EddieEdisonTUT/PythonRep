def count_simple(numbers):
    simple = numbers[0] 
    for i in numbers:
        if i // 2 != 0:
            simple = i
            
    return simple

numbers_list = [5, 3, 8, 2, 9, 1]
result = count_simple(numbers_list)

print("Прості числа у списку:", result)
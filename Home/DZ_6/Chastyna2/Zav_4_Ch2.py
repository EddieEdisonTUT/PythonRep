def remove_number_from_list(numbers, target):
    count = 0
    i = 0
    while i < len(numbers):
        if numbers[i] == target:
            numbers.pop(i)
            count += 1
        else:
            i += 1
    return count

num_list = [1, 2, 3, 4, 2, 5, 2]
target_num = 2
removed_count = remove_number_from_list(num_list, target_num)
print("Кількість видалених елементів:", removed_count)
print("Список після видалення:", num_list)

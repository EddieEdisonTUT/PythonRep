def calculate_multipl(numbers):
    multipl = 1
    for i in numbers:
        multipl *= i
    return multipl

numbers_list = [2, 3, 4, 5]
res = calculate_multipl(numbers_list)

print("Множення списку цілих:", res)

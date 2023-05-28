import random

def generate_random_list(length):
    return [random.randint(-10, 10) for i in range(length)]

numbers_list = generate_random_list(10)

minimum = min(numbers_list)
maximum = max(numbers_list)
negative_count = sum(1 for num in numbers_list if num < 0)
positive_count = sum(1 for num in numbers_list if num > 0)
zero_count = sum(1 for num in numbers_list if num == 0)

print("Список чисел:", numbers_list)
print("Мінімальний елемент:", minimum)
print("Максимальний елемент:", maximum)
print("Кількість від'ємних елементів:", negative_count)
print("Кількість додатніх елементів:", positive_count)
print("Кількість нульових елементів:", zero_count)

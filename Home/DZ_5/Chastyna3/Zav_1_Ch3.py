import random

def generate_random_list(length):
    return [random.randint(1, 100) for i in range(length)]

list1 = generate_random_list(10)
list2 = generate_random_list(10)

combined_list = list1 + list2
unique_list = list(set(combined_list))
common_list = list(set(list1) & set(list2))
unique_elements_list = list(set(list1) ^ set(list2))
min_max_list = [min(list1), max(list1), min(list2), max(list2)]

print("Перший список:", list1)
print("Другий список:", list2)
print("Третій список, що містить елементи обох списків:", combined_list)
print("Третій список без повторень:", unique_list)
print("Третій список, що містить спільні елементи:", common_list)
print("Третій список, що містить унікальні елементи кожного списку:", unique_elements_list)
print("Третій список, що містить мінімальні та максимальні значення кожного списку:", min_max_list)

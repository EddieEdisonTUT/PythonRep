def count_simple(numbers):
    count = 0
    for i in numbers:
         if i > 1:
            is_prime = True
            count += 1
            for h in range(2, i):
                if (i % h) == 0:
                    is_prime = False
                    break
            
    return count

numbers_list = [5, 3, 8, 2, 9, 1, 7]
result = count_simple(numbers_list)

print("Прості числа у списку:", result)
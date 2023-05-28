def power_calculation(numbers, power):
    powered_list = []
    for i in numbers:
        powered_list.append(i ** power)
    return powered_list

num_list = [1, 2, 3, 4, 2, 5, 2]
power_num = 2
res = power_calculation(num_list, power_num)
print('Список після піднесення до степеня: ',res)
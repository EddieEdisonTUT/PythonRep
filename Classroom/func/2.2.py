import random

def max_list(mas):
    return max(mas)
    
 
n = int(input('Введіть довжину списку: '))
mas = []

for i in range(n):

    mas.append(random.randrange(1,10))
print(mas)

# def max_list(mas2):
#     max(mas2)
#     return(max_list)


print(max_list(mas))
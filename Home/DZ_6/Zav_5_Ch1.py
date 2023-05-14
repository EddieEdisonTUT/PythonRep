number1 = int(input('Введіть початок діапазону: '))
number2 = int(input('Введіть кінець діапазону: '))
m = 0
dob = 0
while number1 <= number2:
    print(number1, end=' ')
    number1 += 1
    dob *= number1
    # y += 1 
else:
    print('Сумма:', dob)

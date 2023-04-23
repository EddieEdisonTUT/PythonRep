a = int(input('number1: '))
b = int(input('number2: '))
summa_chet = 0
summa_nechet = 0
summa_cr9 = 0
i = a
j = a
k = a
while a <= b:
    a += 1
    if a % 2 == 0:
        summa_chet += a
        i += 1
    if a % 2 != 0:
        summa_nechet += a
        j += 1
    if a % 9 == 0:
        summa_cr9 += a
        k += 1
else:
    print('Сума парних:', summa_chet)
    print('Середне:', summa_chet/(b-i+1))
    print("Сума не парних", summa_nechet)
    print('Середне:', summa_nechet/(b-j+1))
    print("Сума кратних дев'ятки", summa_cr9)
    print('Середне:', summa_cr9/(b-k+1))


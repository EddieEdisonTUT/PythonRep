count = 0

for i in range(100, 10000):
    digits = str(i)
    
    if digits[0] != digits[1] or digits[0] != digits[2] or digits[1] != digits[2]:
        count += 1

print('Кількість цілих чисел з усіма різними цифрами:', count)
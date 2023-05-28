text = "Это пример текста. В нем есть несколько предложений! Количество предложений нужно посчитать?"

punctuation = ['.', '!', '?']
count = 0

for char in text:
    if char in punctuation:
        count += 1

print('Кількість речень:', count)


text = input("Введіть текст: ")

delimiters = [".", "!", "?"]
count = 0

for i in text:
    if i in delimiters:
        count += 1

print("Кількість речень у тексті: ", count)

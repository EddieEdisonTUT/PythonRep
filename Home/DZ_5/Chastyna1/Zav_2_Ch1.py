text = input("Введіть текст: ")
reserved_words = input("Введіть зарезервовані слова через кому: ").split(",")

for i in reserved_words:
    text = text.replace(i, i.upper())

print(text)
text = input("Введіть текст: ")

delimiters = [".", "!", "?"]

rechennya = [rechennya.strip() for rechennya in text.split((delimiters), text) ]

num_sentences = len(rechennya)
print("Кількість речень у тексті: ", num_sentences)

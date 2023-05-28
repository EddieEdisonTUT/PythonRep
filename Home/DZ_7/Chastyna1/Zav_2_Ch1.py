class Book:
    def __init__(self, name, year_print, publisher, genre, author, price):
        self.name = name
        self.year_print = year_print
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def get_name(self):
        return self.name
    
    def get_year_print(self):
        return self.year_print
    
    def get_publisher(self):
        return self.publisher
    
    def get_genre(self):
        return self.genre
    
    def get_author(self):
        return self.author
    
    def get_price(self):
        return self.price
    
book = Book('Гаррі Поттер i філософський камінь', 2022, 'А-БА-БА-ГА-ЛА-МА-ГА', 'Fantasy', 'Katlin Roling', '400 грн')
print(book.get_name())
print(book.get_year_print())
print(book.get_genre())
print(book.get_publisher())
print(book.get_author())
print(book.get_price())
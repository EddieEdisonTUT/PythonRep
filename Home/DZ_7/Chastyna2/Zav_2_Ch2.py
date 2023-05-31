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

    def put_name(self, name2):
        self.name = name2
    
    def get_year_print(self):
        return self.year_print

    def put_year(self, date):
        date = list(self.year_print)
        date[2] = date
        self.year = tuple(date) 
    
    def get_publisher(self):
        return self.publisher

    def put_publisher(self, publish):
        self.publisher = publish
    
    def get_genre(self):
        return self.genre

    def __str__(self) -> str:
        return "This book has an adventure genre and " + str(self.genre)

    def put_genre(self, gem):
        self.genre = gem
    
    def get_author(self):
        return self.author

    def put_author(self, writer):
        self.author = writer
    
    def get_price(self):
        return self.price

    def put_price(self, pricing):
        self.price = pricing

    
book = Book('Гаррі Поттер i філософський камінь', 2022, 'А-БА-БА-ГА-ЛА-МА-ГА', 'Fantasy', 'Katlin Roling', '400 грн')
print(book.get_name())
print(book.get_year_print())
print(book.get_genre())
# print(book.put_genre('Adventure'))
print(book.__str__())
print(book.get_publisher())
print(book.get_author())
print(book.get_price())
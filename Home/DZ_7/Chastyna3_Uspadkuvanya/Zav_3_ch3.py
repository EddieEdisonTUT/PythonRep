class Money:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def display_amount(self):
        print(f"Amount: {self.dollars}.{self.cents}")

    def set_amount(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

money = Money(10, 50)
money.display_amount()

money.set_amount(15, 75)
money.display_amount()

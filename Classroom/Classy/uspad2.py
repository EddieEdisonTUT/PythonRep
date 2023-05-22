class Passport:
    def __init__(self, name, surname, birthday, country) -> None:
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.country = country
        self.city = 'Kryvyi Rig'

    def show_info(self):
         print(self.name, self.surname, self.birthday, self.country)

    def get_info(self):
        return self.city

class ForeignPassport(Passport):
    def __init__(self, name, surname, birthday, country, visa, number_pass) -> None:
        super().__init__(name, surname, birthday, country)
        self.visa = visa
        self.number_pass = number_pass

    def show_info(self):
        super().show_info()
        print('Visa', self.visa)

    def get_info(self):
        print('Numpber_Pass', self.number_pass)



Pass = Passport('Grigoriy', 'Limonov', '12.05.1995', 'Ukraine')
Pass.show_info()
Pass.get_info()
Forign = ForeignPassport('Grigoriy', 'Limonov', '12.05.1995', 'Ukraine', 'Poland', 'FN600500')
Forign.show_info()
Forign.get_info()
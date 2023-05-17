from tkinter import Y


class Human:
    def __init__(self,FIO, date, tel, city, country, address):
        self.FIO = FIO
        self.date = date

    def get_FIO(self):
        return self.FIO

    def get_year(self):
        return self.date

    def put_year(self, y):
        date = list(self.date)
        date[2] = y
        self.date = tuple(date) 

    def get_tel(self):
        return self.tel
        

man = Human('KSV',(12,7,1997),'+380970175942','Kryvyi Rih','Ukrain',4 )
print(man.get_FIO())
print(man.get_year())
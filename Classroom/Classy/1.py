# class Human:
#     def __init__(self,FIO, date, tel, city, country, address):
#         self.FIO = FIO
#         self.date = date
#         self.tel = tel

#     def get_FIO(self):
#         return self.FIO

#     def get_year(self):
#         return self.date

#     def put_year(self, y):
#         date = list(self.date)
#         date[2] = y
#         self.date = tuple(date) 

#     def get_tel(self):
#         return self.tel
        

# man = Human('KSV',(12,7,1997),'+380970175942','Kryvyi Rih','Ukrain',4 )
# print(man.get_FIO())
# print(man.get_year())




class Wheels:
    def __init__(self, count):
        self.count = count

    def rotate(self):
        print("Колеса вращаются")


class Engine:
    def start(self):
        print("Двигатель запущен")

    def stop(self):
        print("Двигатель остановлен")


class Doors:
    def open(self):
        print("Двери открыты")

    def close(self):
        print("Двери закрыты")


class Car(Wheels, Engine, Doors):
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(f"Автомобиль марки {self.brand}, цвета {self.color} едет")

    def stop(self):
        super().stop()
        print("Автомобиль остановлен")


# Пример использования
my_car = Car("Toyota", "синий")
my_car.start()
my_car.drive()
my_car.rotate()
my_car.open()
my_car.stop()
my_car.close()

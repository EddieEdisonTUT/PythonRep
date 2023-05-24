class Human:
    count = 0

    def __init__(self, name, surname, age, tel) -> None:
        self.name = name
        self.surname = surname
        self.age = age
        self.tel = tel
        self.__height = 186
        Human.count += 1

    def show_info(self):
        print(self.name, self.surname, self.age, self.tel)

    def get_info(self):
        print('Зріст:', self.__height)

    @staticmethod
    def counts():
        return Human.count

class Builder(Human):
    def __init__(self, name, surname, age, tel, spec):
        super().__init__(name, surname, age, tel)
        self.spec = spec
        self.__firma = 'Figma_Build'

    def show_info(self):
        super().show_info()
        print(self.spec)

    def get_info(self):
        print('Фірма:', self.__firma)
        print('Bilder', self.__height)

class Sailor(Human):
    def __init__(self, name, surname, age, tel, zvannya) -> None:
        super().__init__(name, surname, age, tel)
        self.zvannya = zvannya


    def show_info(self):
        super().show_info()
        print(self.zvannya)

class Pilot(Human):
    def __init__(self, name, surname, age, tel, litak) -> None:
        super().__init__(name, surname, age, tel)
        self.litak = litak

    def show_info(self):
        super().show_info()
        print(self.litak)

Hum = Human('Serhii', 'Kishchuk', 26, '+3880970175942')
Hum.show_info()
Hum.get_info()

Build = Builder('Trevor', 'Smit', 25, '+380000000001', 'Malyar')
Build.show_info()
Build.get_info()

Sailo = Sailor('Adam', 'Stone', 38, '+380000000002', 'Kapral')
Sailo.show_info()

Pilo = Pilot('Mayk', 'Vazovsky', 30, '+380000000003', 'F-16')
Pilo.show_info()
print(Pilot.mro())

print(Human.count)
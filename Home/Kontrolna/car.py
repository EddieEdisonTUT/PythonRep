from vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, type_engine, type_transportation, wheels, helm):
        super().__init__(type_engine, type_transportation)
        self.wheels = wheels
        self.helm = helm

    def show_info(self):
        print('Кількість колес:')
        return self.wheels
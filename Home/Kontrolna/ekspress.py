from train import Train


class Ekspress(Train):
    def __init__(self, type_engine, type_transportation, type_fuel, wagons, speed, travel_time):
        super().__init__(type_engine, type_transportation, type_fuel, wagons)
        self.speed = speed
        self.travel_time = travel_time

    def show_info(self):
        return self.speed
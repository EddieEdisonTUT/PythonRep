from vehicle import Vehicle


class Train(Vehicle):
    def __init__(self, type_engine, type_transportation, type_fuel, wagons):
        super().__init__(type_engine, type_transportation)
        self.fuel = type_fuel
        self.wagons = wagons

    def show_info(self):
        return self.fuel
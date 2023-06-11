class Ship:
    def __init__(self, name, length, displacement):
        self.name = name
        self.length = length
        self.displacement = displacement

    def sail(self):
        print(f"The ship {self.name} is sailing.")

    def anchor(self):
        print(f"The ship {self.name} is anchoring.")


class Frigate(Ship):
    def __init__(self, name, length, displacement, missile_capacity):
        super().__init__(name, length, displacement)
        self.missile_capacity = missile_capacity

    def launch_missile(self):
        print(f"The frigate {self.name} is launching a missile.")


class Destroyer(Ship):
    def __init__(self, name, length, displacement, torpedo_capacity):
        super().__init__(name, length, displacement)
        self.torpedo_capacity = torpedo_capacity

    def launch_torpedo(self):
        print(f"The destroyer {self.name} is launching a torpedo.")


class Cruiser(Ship):
    def __init__(self, name, length, displacement, weapon_system):
        super().__init__(name, length, displacement)
        self.weapon_system = weapon_system

    def fire_weapon(self):
        print(f"The cruiser {self.name} is firing its weapon.")


# Приклад використання класів
frigate = Frigate("Гетьман Сагайдачний", 100, 5000, 50)  #UA
frigate.sail()
frigate.launch_missile()
frigate.anchor()

destroyer = Destroyer("Саутгемтон", 150, 8000, 100)  #USA
destroyer.sail()
destroyer.launch_torpedo()
destroyer.anchor()

cruiser = Cruiser("Україна", 200, 10000, "Advanced Weapon System")  #UA
cruiser.sail()
cruiser.fire_weapon()
cruiser.anchor()

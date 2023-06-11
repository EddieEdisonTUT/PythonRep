class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def turn_on(self):
        print("Device is turned on.")

    def turn_off(self):
        print("Device is turned off.")

class CoffeeMachine(Device):
    def __init__(self, brand, model, capacity):
        super().__init__(brand, model)
        self.capacity = capacity

    def brew_coffee(self):
        print("Brewing coffee...")

class Blender(Device):
    def __init__(self, brand, model, speed_levels):
        super().__init__(brand, model)
        self.speed_levels = speed_levels

    def blend(self):
        print("Blending...")

class MeatGrinder(Device):
    def __init__(self, brand, model, power):
        super().__init__(brand, model)
        self.power = power

    def grind_meat(self):
        print("Grinding meat...")

coffee_machine = CoffeeMachine("Philips", "Series 2200", 12)
coffee_machine.turn_on()
coffee_machine.brew_coffee()
coffee_machine.turn_off()

blender = Blender("Bosch", "MSM2650B", 5)
blender.turn_on()
blender.blend()
blender.turn_off()

meat_grinder = MeatGrinder("Bosch", "MFW3640A", 1600)
meat_grinder.turn_on()
meat_grinder.grind_meat()
meat_grinder.turn_off()

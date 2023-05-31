class Device:
    def __init__(self, company, power, color) -> None:
        self.company = company
        self.power = power
        self.color = color

    
class CoffeMachine(Device):
    def __init__(self, company, power, color, type_coffe, bowl_capacity) -> None:
        super().__init__(company, power, color)
        self.type_coffe = type_coffe
        self.bowl_capacity = bowl_capacity

    def get_info(self):
        return self.type_coffe, self.bowl_capacity

    def put_coffe(self, types):
        self.type_coffe = types

class Blender(Device):
    def __init__(self, company, power, color, tips_sockets, blade_turns) -> None:
        super().__init__(company, power, color)
        self.tips_sockets = tips_sockets
        self.blade_turns = blade_turns

    def get_info(self):
        return self.tips_sockets, self.blade_turns

    def put_blender(self, tips):
        self.tips_sockets = tips

class MeatGrinder(Device):
    def __init__(self, company, power, color, types_blades, protection_class) -> None:
        super().__init__(company, power, color)
        self.types_blades = types_blades
        self.protection = protection_class

    def get_info(self):
        return self.types_blades, self.protection

    def put_grind(self, blades):
        self.types_blades = blades

dev = Blender('Braun', 1200, 'red', 'dive head', 1000)
print(dev.put_blender('cutting'))
print(dev.get_info())
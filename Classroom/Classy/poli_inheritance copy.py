class Wheels:
    def __init__(self, radius) -> None:
        self.size = radius

    def size_info(self):
        print(self.size)


class Engine:
    def __init__(self, capacity) -> None:
        self.capaciti = capacity
        self.type_fuel = 'Бензин'

    def show_info(self):
        return self.capaciti, self.type_fuel
    
    def put_fuel(self):
        return self.type_fuel
        
    
class Door:
    def __init__(self, h, w) -> None:
        self.height = h
        self.width = w
    def show_info(self):
        return self.height, self.width
    
    def up_window(self, up):
        self.up_windows = up
        
        return self.up_windows, print('Up window')


class Car(Wheels, Engine, Door):
    def __init__(self, size, capacity, h, w) -> None:
        Wheels.__init__(self,size)
        Engine.__init__(self, capacity)
        Door.__init__(self, h, w)
        

    def show_info(self):
        return Wheels.size_info(self), Engine.show_info(self), Door.show_info(self)

item = Car('20',2.0,1,1)
print(item.show_info())
door = Door(1,1)
print(door.up_window(1))
print(door.show_info())
engine = Engine(2.0)
print(engine.show_info())
print(engine.put_fuel())
wheels = Wheels(20)
print(wheels.size_info())
from car import Car
from ekspress import Ekspress
from train import Train
from vehicle import Vehicle


car = Car('Hybryd', 'human', 4, 'Cirle')
print(car.show_info())
exp = Ekspress('Elecktro', 'human', 'Energee', 10, 500, 30)
print(exp.show_info())
train = Train('DVS', 'human', 'Diesel', 10)
print(train.show_info())
vehic = Vehicle('DVS', 'Other')
print(vehic.show_info())
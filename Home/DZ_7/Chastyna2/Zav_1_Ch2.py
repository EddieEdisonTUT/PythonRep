class Car:
    def __init__(self, name, year, producer, V_engine, color, price):
        self.name = name
        self.year = year
        self.producer = producer
        self.v_engine = V_engine
        self.color = color
        self.price = price

    def get_name(self):
        return self.name

    def put_name(self, name2):
        self.name = name2

    def get_year(self):
        return self.year

    def put_year(self, y):
        year = list(self.year)
        year[2] = y
        self.year = tuple(year) 

    def get_producer(self):
        return self.producer

    def put_producer(self, prod):
        self.producer = prod
    
    def get_V_engine(self):
        return self.v_engine

    def put_engine(self, capacity):
        self.v_engine = capacity
    
    def get_color(self):
        return self.color

    def put_color(self, colored):
        self.color = colored
    
    def get_price(self):
        return self.price

    def put_price(self, value):
        self.price = value

    def __str__(self) -> str:
        col = 'Red'
        return col
        

car = Car('FH16', 2023, 'Volovo','2.0','Blue', '$4000' )
print(car.get_name())
print(car.put_name('Toyota'))
print(car.get_year())
print(car.get_producer())
print(car.get_V_engine())
print(car.get_color())
print(car.__str__())
print(car.get_price())
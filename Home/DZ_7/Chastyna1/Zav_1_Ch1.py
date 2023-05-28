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

    def get_year(self):
        return self.year

    def put_year(self, y):
        date = list(self.date)
        date[2] = y
        self.date = tuple(date) 

    def get_producer(self):
        return self.producer
    
    def get_V_engine(self):
        return self.v_engine
    
    def get_color(self):
        return self.color
    
    def get_price(self):
        return self.price
        

car = Car('FH16', 2023, 'Volovo','2.0','Blue', '$4000' )
print(car.get_name())
print(car.get_year())
print(car.get_producer())
print(car.get_V_engine())
print(car.get_color())
print(car.get_price())
class Stadion:
    def __init__(self, name, date_open, country, city, capacity):
        self.name = name
        self.date_open = date_open
        self.country = country
        self.city = city
        self.capacity = capacity

    def get_name(self):
        return self.name
    
    def get_date(self):
        return self.date_open
    
    def put_date(self, i):
        date = list(self.date_open)
        date[2] = i
        self.date_open = tuple(date)

    def get_country(self):
        return self.country
    
    def get_city(self):
        return self.city
    
    def get_capacity(self):
        return self.capacity
    
stad = Stadion('ДонбасАрена', (29,8,2009), 'Ukraine', 'Donetsk', 50000)
print(stad.get_name())
print(stad.get_date())
print(stad.get_country())
print(stad.get_city())
print(stad.get_capacity())
        
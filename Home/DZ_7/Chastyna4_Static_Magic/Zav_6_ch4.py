class Airplane:
    def __init__(self, airplane_type, max_passengers, current_passengers):
        self.airplane_type = airplane_type
        self.max_passengers = max_passengers
        self.current_passengers = current_passengers

    def __eq__(self, other):
        return self.airplane_type == other.airplane_type

    def __add__(self, passengers):
        self.current_passengers += passengers
        return self

    def __sub__(self, passengers):
        self.current_passengers -= passengers
        return self

    def __iadd__(self, passengers):
        self.current_passengers += passengers
        return self

    def __isub__(self, passengers):
        self.current_passengers -= passengers
        return self

    def __gt__(self, other):
        return self.max_passengers > other.max_passengers

    def __lt__(self, other):
        return self.max_passengers < other.max_passengers

    def __ge__(self, other):
        return self.max_passengers >= other.max_passengers

    def __le__(self, other):
        return self.max_passengers <= other.max_passengers

airplane1 = Airplane("Boeing 747", 500, 300)
airplane2 = Airplane("Airbus A380", 600, 400)

print(airplane1 == airplane2)
airplane1 += 100
print(airplane1.current_passengers)

airplane2 -= 50
print(airplane2.current_passengers)
print(airplane1 > airplane2)
print(airplane1 < airplane2)
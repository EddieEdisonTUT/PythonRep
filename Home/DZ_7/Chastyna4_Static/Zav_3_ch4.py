class LengthConverter:
    def __init__(self, length):
        self.length = length

    @staticmethod
    def meters_to_feet(meters):
        return meters * 3.28

    @staticmethod
    def feet_to_meters(feet):
        return feet * 0.30

length_in_meters = 10
length_in_feet = LengthConverter.meters_to_feet(length_in_meters)
print(f"{length_in_meters} метрів = {length_in_feet} футів")

length_in_feet = 30
length_in_meters = LengthConverter.feet_to_meters(length_in_feet)
print(f"{length_in_feet} футів = {length_in_meters} метрів")

class TemperatureConverter:
    count = 0

    def __init__(self, temperature):
        self.temp = temperature
        

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        TemperatureConverter.count += 1
        return celsius * 9/5 + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        TemperatureConverter.count += 1
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def get_conversion_count():
        return TemperatureConverter.count

temperature1 = TemperatureConverter.celsius_to_fahrenheit(25)
temperature2 = TemperatureConverter.fahrenheit_to_celsius(77)
print('C to F:', temperature1)
print('F to C:', temperature2)
print(TemperatureConverter.get_conversion_count())
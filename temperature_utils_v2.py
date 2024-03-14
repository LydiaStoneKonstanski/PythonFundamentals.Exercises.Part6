#Convert to Kelvin from fahrenheit and from celsius
from temperature_utils import convert_to_celsius


def convert_celsius_to_kelvin(celsius_temp: float):
    kelvin = celsius_temp + 273.15
    return round(kelvin, 2)

def convert_fahrenheit_to_kelvin(fahrenheit_temp: float):
    kelvin = convert_celsius_to_kelvin(convert_to_celsius(fahrenheit_temp))
    return round(kelvin, 2)
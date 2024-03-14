from typing import Iterable, Tuple


def convert_to_celsius(fahrenheit_temp: float) -> float:
    celsius = (fahrenheit_temp - 32) * 5 / 9
    return round(celsius, 2)

def convert_to_fahrenheit(celsius_temp: float) -> int:
    fahrenheit = celsius_temp * 9 / 5 + 32
    return round(fahrenheit, 2)



def temperature_tuple(temperatures: Iterable, input_unit_of_measurement: str) -> Tuple[Tuple[float, float]]:
    new_t = []
    if input_unit_of_measurement == "f":
        for temperature in temperatures:
            convert_value = convert_to_celsius(temperature)
            new_t.append((temperature, convert_value))
            return tuple(new_t)

    elif input_unit_of_measurement == "c":
        for temperature in temperatures:
            convert_value = convert_to_fahrenheit(temperature)
            new_t.append((temperature, convert_value))
    return tuple(new_t)


import unittest

import temperature_utils_v2


class TemperatureUtilsV2Test(unittest.TestCase):

    def test_convert_celsius_to_kelvin(self):
        test_cases = [
            (-17.7778, 255.37),
            (0, 273.15),
            (100, 373.15)
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils_v2.convert_celsius_to_kelvin(temp_in))

    def test_convert_fahrenheit_to_kelvin(self):
        test_cases = [
            (-17.7778, 245.5),
            (0, 255.37),
            (100, 310.93)
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils_v2.convert_fahrenheit_to_kelvin(temp_in))

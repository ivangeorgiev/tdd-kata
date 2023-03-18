import unittest
from parameterized import parameterized

from .roman_numerals import decimal_to_roman

class TestConvertFunction(unittest.TestCase):

    @parameterized.expand([
        ("1", 1, "I"),
        ("2", 2, "II"),
        ("3", 3, "III"),
        ("4", 4, "IV"),
        ("5", 5, "V"),
        ("6", 6, "VI"),
        ("8", 8, "VIII"),
        ("9", 9, "IX"),
        ("10", 10, "X"),
        ("11", 11, "XI"),
        ("19", 19, "XIX"),
        ("20", 20, "XX"),
        ("39", 39, "XXXIX"),
        ("40", 40, "XL"),
        ("41", 41, "XLI"),
        ("49", 49, "XLIX"),
        ("50", 50, "L"),
        ("90", 90, "XC"),
        ("95", 95, "XCV"),
        ("100", 100, "C"),
        ("400", 400, "CD"),
        ("500", 500, "D"),
        ("900", 900, "CM"),
        ("1000", 1000, "M"),
        ("Spanish flu", 1918, "MCMXVIII"),
        ("2023", 2023, 'MMXXIII')
    ])
    def test_convert(self, name, num, expected_result):
        result = decimal_to_roman(num)
        self.assertEqual(result, expected_result)

"""
Kata: Convert name from snake case to CamelCase.
"""

import re
import unittest

from parameterized import parameterized


def camel_to_snake(name, is_upper=True):
    name = re.sub(r"_(.?)", lambda m: m.group(1).upper(), name)
    if is_upper and name:
        name = name[0].upper() + name[1:]
    return name


class TestCamelToSnake(unittest.TestCase):
    @parameterized.expand(
        [
            ("single word lower", "python", False, "python"),
            ("single word with trailing underscoer lower", "python_", False, "python"),
            ("two words lower", "send_request", False, "sendRequest"),
            ("single word upper", "python", True, "Python"),
            ("single character upper", "p", True, "P"),
            ("two words upper", "http_printer", True, "HttpPrinter"),
        ]
    )
    def test_should_convert_camel_to_snake(self, _, name, is_upper, expected):
        actual = camel_to_snake(name, is_upper)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main(verbosity=3)

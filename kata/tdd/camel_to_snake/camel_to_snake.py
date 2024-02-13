import re
import unittest


def camel_to_snake(name: str):
    name = re.sub(r"(.)([A-Z][a-z])", r"\1_\2", name)
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name)
    return name.lower()


class TestCamelToSnake(unittest.TestCase):
    def test_single_lowercase_word(self):
        actual = camel_to_snake("something")
        self.assertEqual("something", actual)

    def test_single_capitalized_word(self):
        actual = camel_to_snake("Something")
        self.assertEqual("something", actual)

    def test_standard_words(self):
        actual = camel_to_snake("WelcomeHome")
        self.assertEqual("welcome_home", actual)

    def test_abbreviation(self):
        actual = camel_to_snake("retrieveHTTPResponse")
        self.assertEqual("retrieve_http_response", actual)


if __name__ == "__main__":
    unittest.main()

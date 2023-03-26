import unittest
import parameterized

from ..validators import is_email

class TestIsEmailFunction(unittest.TestCase):
    @parameterized.parameterized.expand([
        ('value is simple email address', 'example@example.com'),
        ('domian is a subdomain', 'example@subdomain.domain.com'),
        ('domain contains dashes', 'example@example-domain.com'),
        ('username contains digits', 'example123@example.com'),
    ])
    def test_should_return_true_when(self, name, value):
        self.assertTrue(is_email(value))

    @parameterized.parameterized.expand([
        ('domain is empty', 'example@'),
        ('host is empty', 'example@.com'),
        ('at character is missing', 'example.com'),
        ('domain ends with period', 'example@com.'),
        ('domain starts with period', 'example@.domain.com'),
        ('username is empty', '@domain.com'),
    ])
    def test_should_return_false_when(self, name, value):
        self.assertFalse(is_email(value))


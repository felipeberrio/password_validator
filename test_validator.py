import unittest
from validator import is_strong_password

class TestPasswordValidator(unittest.TestCase):

    def test_strong_password(self):
        self.assertTrue(is_strong_password("Str0ng!Pass"))

    def test_no_uppercase(self):
        self.assertFalse(is_strong_password("weakpass1!"))

    def test_no_lowercase(self):
        self.assertFalse(is_strong_password("WEAK123!"))

    def test_too_short(self):
        self.assertFalse(is_strong_password("S1!a"))

    def test_no_digit(self):
        self.assertFalse(is_strong_password("NoDigit!"))

    def test_no_special_char(self):
        self.assertFalse(is_strong_password("Password123"))

if __name__ == "__main__":
    unittest.main()

import unittest
from fizzbuzz import affiche

class TestFizzBuzz(unittest.TestCase):
    def test_affiche_nombre(self):
        self.assertEqual(affiche(1), "1")

    def test_affiche_fizz(self):
        self.assertEqual(affiche(3), "Fizz")

    def test_affiche_buzz(self):
        self.assertEqual(affiche(5), "Buzz")

if __name__ == "__main__":
    unittest.main()
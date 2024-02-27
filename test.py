import unittest
from main import Kalkulacka

class TestAddFunction(unittest.TestCase):
    def test_add_integers(self):
        calc = Kalkulacka()
        self.assertEqual(calc.sucetFunc(4, 6), 10)
    def test_add_integers(self):
        calc = Kalkulacka()
        self.assertEqual(calc.sucetFunc(-4, -6), -10)

    def test_add_Kv(self):
        calc = Kalkulacka()
        self.assertEqual(calc.defQuadRov(6.25,6, 1), (-1.0, -1.0))


if __name__ == "__main__":
    unittest.main()


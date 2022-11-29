import unittest2
from Calculator import Calculator
class TestCalculator(unittest2.TestCase):
    def setUp(self):
        self.calculator=Calculator()
    def test_sum(self):
        self.assertEqual(self.calculator.sum(4, 7), 11)
    def test_minus(self):
        self.assertEqual(self.calculator.minus(7, 4), 3)
    def test_div(self):
        self.assertEqual(self.calculator.div(8, 4), 2)
    def test_multi(self):
        self.assertEqual(self.calculator.multi(4, 4), 16)
if __name__ == "__main__":
    unittest2.main()

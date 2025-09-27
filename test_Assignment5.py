import unittest
from Assignment5 import to_celsius, fib

class TestAssignment5(unittest.TestCase):
    def test_to_cel(self):
        fah = 32
        self.assertEqual(to_celsius(fah), 5)

    def test_fib(self):
        n = 5
        self.assertEqual(fib(n), 5)
        
if __name__ == "__main__":
    unittest.main()
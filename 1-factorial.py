import unittest
import lib

class LibTest(unittest.TestCase):

    def test_factorial_plus(self):
        self.assertEqual(lib.factorial(1), 1)
        self.assertEqual(lib.factorial(2), 2)
        self.assertEqual(lib.factorial(0), 1)
        self.assertEqual(lib.factorial(3), 6)

    def test_factorial_minus(self):
        self.assertEqual(lib.factorial(-1), 1)

unittest.main(verbosity=2)

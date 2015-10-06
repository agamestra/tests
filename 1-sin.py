import unittest
import math
import lib

class LibTest(unittest.TestCase):

    def test_sin_0(self):
        self.assertEqual(lib.sin(0), 0)

    def test_sin_plus(self):
        self.assertEqual(lib.sin(math.pi), 0)
        self.assertEqual(lib.sin(math.pi/2), 1)

    def test_sin_minus(self):
        self.assertEqual(lib.sin(-math.pi), 0)
        self.assertEqual(lib.sin(-math.pi/2), -1)

unittest.main(verbosity=2)

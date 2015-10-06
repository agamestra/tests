import unittest
import lib

class LibTest(unittest.TestCase):

    def test_even_0(self):
        self.assertEqual(lib.even(0), True)

    def test_even_chet(self):
        self.assertEqual(lib.even(2), True)
        self.assertEqual(lib.even(8), True)

    def test_even_nechet(self):
        self.assertEqual(lib.even(9), False)
        self.assertEqual(lib.even(31), False)

    def test_even_chet_minus(self):
        self.assertEqual(lib.even(-22), True)
        self.assertEqual(lib.even(-4), True)

    def test_even_nechet_minus(self):
        self.assertEqual(lib.even(-1), False)
        self.assertEqual(lib.even(-47), False)

unittest.main(verbosity=2)


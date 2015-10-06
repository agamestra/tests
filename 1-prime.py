import unittest
import lib

class LibTest(unittest.TestCase):

    def test_prime_0(self):
        self.assertEqual(lib.prime(0), False)

    def test_prime_1(self):
        self.assertEqual(lib.prime(1), True)

    def test_prime_minus(self):
        self.assertEqual(lib.prime(-11), False)
        self.assertEqual(lib.prime(-36), False)

    def test_prime_2(self):
        self.assertEqual(lib.prime(2), True)

    def test_prime_prost(self):
        self.assertEqual(lib.prime(31), True)

    def test_prime_sost(self):
        self.assertEqual(lib.prime(6), False)

unittest.main(verbosity=2)

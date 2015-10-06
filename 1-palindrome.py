import unittest
import lib

class LibTest(unittest.TestCase):

    def test_palindrome_chet(self):
        self.assertEqual(lib.palindrome("shhh"), False)
        self.assertEqual(lib.palindrome("shhs"), True)

    def test_palindrome_nechet(self):
        self.assertEqual(lib.palindrome("shkhh"), False)
        self.assertEqual(lib.palindrome("shkhs"), True)

unittest.main(verbosity=2)


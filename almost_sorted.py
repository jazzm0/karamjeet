import unittest

# https://www.hackerrank.com/challenges/almost-sorted/

def almostSorted(arr):
    return "unsolved"


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(almostSorted([1, 2, 3, 5, 4]), 'yes')

    def test_b(self):
        self.assertEqual(almostSorted([1, 5, 4, 3, 2, 6]), 'yes')

    def test_c(self):
        self.assertEqual(almostSorted([1, 5, 3, 4, 6, 2]), 'no')

    def test_d(self):
        self.assertEqual(almostSorted([3, 1, 2]), 'no')


if __name__ == '__main__':
    unittest.main()

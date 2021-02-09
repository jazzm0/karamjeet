import unittest


# https://www.hackerrank.com/challenges/reduced-string/problem

def superReducedString(s):
    return s


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(superReducedString('aaabccddd'), 'abd')

    def test_b(self):
        self.assertEqual(superReducedString('aa'), 'Empty String')

    def test_c(self):
        self.assertEqual(superReducedString('baab'), 'Empty String')

    def test_d(self):
        self.assertEqual(superReducedString(
            'ppffccmmssnnhhbbmmggxxaaooeeqqeennffzzaaeeyyaaggggeessvvssggbbccnnrrjjxxuuzzbbjjrruuaaccaaoommkkkkxx'),
            'Empty String')


if __name__ == '__main__':
    unittest.main()

'''
    Testes unitários
'''

import unittest

def fatorial(n):
    fat = 1

    for i in range(2, (n + 1)):
        fat *= i

    return fat

class FatorialTestCase(unittest.TestCase):
    def test_fatorial(self):
        self.assertEqual(fatorial(0), 1)
        self.assertEqual(fatorial(1), 1)
        self.assertEqual(fatorial(2), 2)
        self.assertEqual(fatorial(3), 6)
        self.assertEqual(fatorial(4), 24)
        self.assertEqual(fatorial(5), 120)
        self.assertEqual(fatorial(6), 720)

unittest.main()

# n = int(input('Digite a quantidade desejada: '))
# print(fatorial(n))
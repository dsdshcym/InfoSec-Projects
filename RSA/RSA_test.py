import RSA as rsa
import unittest

class TestRSAAlgorithm(unittest.TestCase):
    def test_euclid(self):
        assert rsa.euclid(1, 2) == 1
        assert rsa.euclid(4, 11) == 1

        assert rsa.euclid(2, 4) == 2
        assert rsa.euclid(12, 18) == 6

    def test_extended_euclid(self):
        assert rsa.extended_euclid(30, 47) == (1, 11, -7)
        assert rsa.extended_euclid(1, 2) == (1, 1, 0)

    def test_coPrime(self):
        assert rsa.coPrime(3, 5)
        assert not rsa.coPrime(123, 6)
        assert not rsa.coPrime(2, 0)

    def test_extract_two_power(self):
        self.assertEqual(rsa.extract_two_power(0), (0, 0))
        self.assertEqual(rsa.extract_two_power(2), (1, 1))
        self.assertEqual(rsa.extract_two_power(12), (2, 3))

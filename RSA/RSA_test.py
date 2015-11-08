import RSA as rsa
import unittest

class TestRSAAlgorithm(unittest.TestCase):
    def test_euclid(self):
        assert rsa.euclid(1, 2) == 1
        assert rsa.euclid(4, 11) == 1

        assert rsa.euclid(2, 4) == 2
        assert rsa.euclid(12, 18) == 6

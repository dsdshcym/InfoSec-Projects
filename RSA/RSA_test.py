import RSA as rsa
from random import randint
import unittest

class TestRSAAlgorithm(unittest.TestCase):
    def setUp(self):
        self.n, self.e, self.d = rsa.generate_key(10 ** 100, 10 ** 101, 50)

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

    def test_mod_exp(self):
        self.assertEqual(rsa.mod_exp(2, 5, 10), 2)
        self.assertEqual(rsa.mod_exp(3, 5, 10), 3)
        self.assertEqual(rsa.mod_exp(2, 100, 3), 1)

    def test_Miller_Robin(self):
        self.assertTrue(rsa.Miller_Robin(2, 10))
        self.assertTrue(rsa.Miller_Robin(11, 10))
        self.assertTrue(rsa.Miller_Robin(12026655772210679470465581609002525329245773732132014742758935511187863487919026457076252932048619706498126046597130520643092209728783224795661331197604583, 50))
        self.assertFalse(rsa.Miller_Robin(4, 10))
        self.assertFalse(rsa.Miller_Robin(100, 10))

    def test_mul_inverse(self):
        self.assertEqual(rsa.mul_inverse(11, 15), 11)
        self.assertEqual(rsa.mul_inverse(11, 16), 3)

    def test_encrypt_decrypt(self):
        for i in xrange(50):
            plain = randint(1000, 10000)
            cipher = rsa.encrypt(plain, self.n, self.e)
            self.assertEqual(rsa.decrypt(cipher, self.n, self.d), plain)

suite = unittest.TestLoader().loadTestsFromTestCase(TestRSAAlgorithm)
unittest.TextTestRunner(verbosity=2).run(suite)

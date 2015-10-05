import des
import unittest

class TestDESAlgorithm(unittest.TestCase):
    def test_leftShift(self):
        bits = [1, 1, 0, 0, 1, 0, 1]
        self.assertEqual(des.leftShift(bits, 2), [0, 0, 1, 0, 1, 1, 1])
        self.assertEqual(des.leftShift(bits, 1), [1, 0, 0, 1, 0, 1, 1])
        self.assertEqual(des.leftShift(bits, 0), [1, 1, 0, 0, 1, 0, 1])

    def test_selfReplacement(self):
        bits = [1, 0, 1, 1, 1, 0, 1, 0]
        table = [2, 4, 5, 7, 1, 3, 0, 6]
        self.assertEqual(des.selfReplacement(bits, table), [1, 1, 0, 0, 0, 1, 1, 1])

    def test_xor(self):
        a = [1, 1, 0, 1, 1, 0, 1, 1]
        b = [0, 1, 1, 0, 1, 0, 1, 0]
        expected = [1, 0, 1, 1, 0, 0, 0, 1]
        self.assertEqual(des.xor(a, b), expected)

    def test_bits_to_int(self):
        bits = [0, 0, 0, 0]
        self.assertEqual(des.bits_to_int(bits), 0)
        bits = [0, 0, 0, 1]
        self.assertEqual(des.bits_to_int(bits), 1)
        bits = [0, 0, 1, 0]
        self.assertEqual(des.bits_to_int(bits), 2)
        bits = [0, 0, 1, 1]
        self.assertEqual(des.bits_to_int(bits), 3)
        bits = [0, 1, 0, 0]
        self.assertEqual(des.bits_to_int(bits), 4)
        bits = [0, 1, 0, 1]
        self.assertEqual(des.bits_to_int(bits), 5)
        bits = [0, 1, 1, 0]
        self.assertEqual(des.bits_to_int(bits), 6)
        bits = [0, 1, 1, 1]
        self.assertEqual(des.bits_to_int(bits), 7)

    def test_int_to_4bits(self):
        x = 0
        self.assertEqual(des.int_to_4bits(x), [0, 0, 0, 0])
        x = 1
        self.assertEqual(des.int_to_4bits(x), [0, 0, 0, 1])
        x = 2
        self.assertEqual(des.int_to_4bits(x), [0, 0, 1, 0])
        x = 3
        self.assertEqual(des.int_to_4bits(x), [0, 0, 1, 1])
        x = 4
        self.assertEqual(des.int_to_4bits(x), [0, 1, 0, 0])
        x = 5
        self.assertEqual(des.int_to_4bits(x), [0, 1, 0, 1])
        x = 6
        self.assertEqual(des.int_to_4bits(x), [0, 1, 1, 0])
        x = 7
        self.assertEqual(des.int_to_4bits(x), [0, 1, 1, 1])

suite = unittest.TestLoader().loadTestsFromTestCase(TestDESAlgorithm)
unittest.TextTestRunner(verbosity=2).run(suite)

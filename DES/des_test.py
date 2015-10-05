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

suite = unittest.TestLoader().loadTestsFromTestCase(TestDESAlgorithm)
unittest.TextTestRunner(verbosity=2).run(suite)

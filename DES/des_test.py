import des
import unittest

class TestDESAlgorithm(unittest.TestCase):
    def test_leftShift(self):
        bits = [1, 1, 0, 0, 1, 0, 1]
        self.assertEqual(des.leftShift(bits, 2), [0, 0, 1, 0, 1, 1, 1])
        self.assertEqual(des.leftShift(bits, 1), [1, 0, 0, 1, 0, 1, 1])
        self.assertEqual(des.leftShift(bits, 0), [1, 1, 0, 0, 1, 0, 1])

suite = unittest.TestLoader().loadTestsFromTestCase(TestDESAlgorithm)
unittest.TextTestRunner(verbosity=2).run(suite)

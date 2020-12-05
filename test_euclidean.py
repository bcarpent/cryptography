import unittest
import euclidean

# Full test suite can be run as follows:
#
# python -m unittest discover -v
#
class TestEuclidean(unittest.TestCase):

    def test_euclidean(self):
    	result = euclidean.gcd(36, 10)
    	self.assertEqual(result, 2)

    	result = euclidean.gcd(2740, 1760)
    	self.assertEqual(result, 20)

    def test_extendedEuclidean(self):
    	gcd, x0, y0 = euclidean.extendedEuclidean(161, 28)
    	self.assertEqual(gcd, 7)
    	self.assertEqual(x0, -1)
    	self.assertEqual(y0, 6)

    	gcd, x0, y0 = euclidean.extendedEuclidean(103927, 102313)
    	self.assertEqual(gcd, 1)
    	self.assertEqual(x0, -39239)
    	self.assertEqual(y0, 39858)

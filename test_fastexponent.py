import unittest
import fastexponent

# Full test suite can be run as follows:
# python -m unittest discover -v
#
# Or run this test alone:
# python -m unittest -v test_fastexponent
class TestFastExponent(unittest.TestCase):

    def test_calculateFastExponent(self):
    	result = fastexponent.calculate(2, 100, 71)
    	self.assertEqual(result, 20)

    	result = fastexponent.calculate(17, 22, 21)
    	self.assertEqual(result, 4)

    	result = fastexponent.calculate(2, 1000, 89)
    	self.assertEqual(result, 45)


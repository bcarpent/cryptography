import unittest
import math
import miller_rabin
import pollards_p_1
import pollards_rho

# This Pollards Rho test can be run as follows:
# python -m unittest -v test_pollards
#
# To run the full suite of unit tests:
# python3 -m unittest discover -v
class Test_Pollards(unittest.TestCase):

    def test_pollardsRho(self):
	    for i in range(0, 20):
	        # Get two prime numbers, 20 bits, in 5 rounds
	        p = miller_rabin.millerRabinTest(0, 5)
	        q = miller_rabin.millerRabinTest(0, 5)
	        n = p * q

	        result = pollards_rho.factor(n)
	        self.assertTrue(result == p or result == q)

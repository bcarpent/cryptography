import unittest
import miller_rabin

# Following tables were sourced from Garrett, "Making, Breaking Codes",
# Table 2: Primes Below 10,000
#
# To run:
# python3 -m unittest -v test_miller_rabin.py 
#
class TestMillerRabin(unittest.TestCase):

    def test_millerRabinTest(self):
        # Success test cases -- guesses which are true primes
        testcases_primes = [
            {
                "guess": 11,
                "rounds": 5,
                "result": 11
            },
            {
                "guess": 107,
                "rounds": 5,
                "result": 107
            },
            {
                "guess": 1619,
                "rounds": 5,
                "result": 1619
            },
            {
                "guess": 4483,
                "rounds": 5,
                "result": 4483 
            },
            {
                "guess": 9931,
                "rounds": 5,
                "result": 9931
            },
            {
                "guess": 104513,
                "rounds": 5,
                "result": 104513
            },
        ]

        # Guesses which are composites
        testcases_composites = [
            {
                "guess": 972133929835994161,   # Carmichael number
                "rounds": 1,
                "result": 0
            },
            {
                "guess": 2857191047211793,
                "rounds": 1,
                "result": 0
            },
            {
                "guess": 4465,
                "rounds": 1,
                "result": 0
            },
            {
                "guess": 9925,
                "rounds": 1,
                "result": 0 
            },
            {
                "guess": 8299,
                "rounds": 5,
                "result": 0
            },
            {
                "guess": 104515,
                "rounds": 5,
                "result": 0
            },
        ]

        for case in testcases_primes:
            result = miller_rabin.millerRabinTest(case["guess"], case["rounds"])
            self.assertEqual(result, case["result"])

        for case in testcases_composites:
            result = miller_rabin.millerRabinTest(case["guess"], case["rounds"])
            self.assertEqual(result, case["result"])



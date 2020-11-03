import unittest
import babystepgiantstep
import fastexponent

# Full test suite can be run as follows:
#
# python -m unittest discover -v
#
class TestBabyStepGiantStep(unittest.TestCase):

    def test_babyStepGiantStep(self):
        testcases = [
            {
                "b": 5,
                "a": 20,
                "mod": 53
            },
            {
                "b": 2,
                "a": 3,
                "mod": 29
            },
            {
                "b": 2,
                "a": 3,
                "mod": 101
            },
            {
                "b": 5,
                "a": 8,
                "mod": 43
            },
            {
                "b": 5,
                "a": 22,
                "mod": 53
            },
            {
                "b": 7,
                "a": 15,
                "mod": 131
            },
            {
                "b": 11,
                "a": 50,
                "mod": 997
            },
            {
                "b": 7,
                "a": 777,
                "mod": 14947
            },
        ]

        # Run baby-step, giant-step to get the logarithm: log base b of a in Z(n)
        # Then test the result with fast exponentiation: a = b^log mod n
        for case in testcases:
            log = babystepgiantstep.babyStepGiantStep(case["b"], case["a"], case["mod"])
            result = fastexponent.calculate(case["b"], log, case["mod"])
            self.assertEqual(case["a"], result)

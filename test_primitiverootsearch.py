import unittest
import primitiverootsearch

# Following table was sourced from Garrett, "Making, Breaking Codes"
# Table 3: Primitive Roots Under 100
# python -m unittest -v test_primitiverootsearch
class TestPrimitiveRootSearch(unittest.TestCase):

    # Success test cases, no guess
    def test_rootSearch(self):
        testcases = [
            {
                "mod": 3,
                "guess": 0,
                "roots": [2]
            },
            {
                "mod": 5,
                "guess": 0,
                "roots": [2, 3]
            },
            {
                "mod": 7,
                "guess": 0,
                "roots": [3, 5]
            },
            {
                "mod": 11,
                "guess": 0,
                "roots": [2, 6, 7, 8]
            },
            {
                "mod": 13,
                "guess": 0,
                "roots": [2, 6, 7, 11]
            },
            {
                "mod": 17,
                "guess": 0,
                "roots": [3, 5, 6, 7, 10, 11, 12, 14]
            },
            {
                "mod": 19,
                "guess": 0,
                "roots": [2, 3, 10, 13, 14, 15]
            },
            {
                "mod": 23,
                "guess": 0,
                "roots": [5, 7, 10, 11, 14, 15, 17, 19, 20, 21]
            },
            {
                "mod": 29,
                "guess": 0,
                "roots": [2, 3, 8, 10, 11, 14, 15, 18, 19, 21, 26, 27]
            },
            {
                "mod": 31,
                "guess": 0,
                "roots": [3, 11, 12, 13, 17, 21, 22, 24]
            },            
            {
                "mod": 37,
                "guess": 0,
                "roots": [2, 5, 13, 15, 17, 18, 19, 20, 22, 24, 32, 35]
            },
            {
                "mod": 41,
                "guess": 0,
                "roots": [6, 7, 11, 12, 13, 15, 17, 19, 22, 24, 26, 28, 29, 30, 34, 35]
            },
            {
                "mod": 43,
                "guess": 0,
                "roots": [3, 5, 12, 18, 19, 20, 26, 28, 29, 30, 33, 34]
            },
            {
                "mod": 47,
                "guess": 0,
                "roots": [5, 10, 11, 13, 15, 19, 20, 22, 23, 26, 29, 30, 31, 33, 35, 38, 39, 40, 41, 43, 44, 45]
            },
            {
                "mod": 53,
                "guess": 0,
                "roots": [2, 3, 5, 8, 12, 14, 18, 19, 20, 21, 22, 26, 27, 31, 32, 33, 34, 35, 39, 41, 45, 48, 50, 51]
            },
            {
                "mod": 59,
                "guess": 0,
                "roots": [2, 6, 8, 10, 11, 13, 14, 18, 23, 24, 30, 31, 32, 33, 34, 37, 38, 39, 40, 42, 43, 44, 47, 50, 52, 54, 55, 56]
            },
            {
                "mod": 61,
                "guess": 0,
                "roots": [2, 6, 7, 10, 17, 18, 26, 30, 31, 35, 43, 44, 51, 54, 55, 59]
            },
            {
                "mod": 67,
                "guess": 0,
                "roots": [2, 7, 11, 12, 13, 18, 20, 28, 31, 32, 34, 41, 44, 46, 48, 50, 51, 57, 61, 63]
            },
            {
                "mod": 71,
                "guess": 0,
                "roots": [7, 11, 13, 21, 22, 28, 31, 33, 35, 42, 44, 47, 52, 53, 55, 56, 59, 61, 62, 63, 65, 67, 68, 69]
            },
            {
                "mod": 73,
                "guess": 0,
                "roots": [5, 11, 13, 14, 15, 20, 26, 28, 29, 31, 33, 34, 39, 40, 42, 44, 45, 47, 53, 58, 59, 60, 62, 68]
            },
            {
                "mod": 79,
                "guess": 0,
                "roots": [3, 6, 7, 28, 29, 30, 34, 35, 37, 39, 43, 47, 48, 53, 54, 59, 60, 63, 66, 68, 70, 74, 75, 77]
            },
            {
                "mod": 83,
                "guess": 0,
                "roots": [2, 5, 6, 8, 13, 14, 15, 18, 19, 20, 22, 24, 32, 34, 35, 39, 42, 43, 45, 46, 47, 50, 52, 53, 54, 55, 56, 57, 58, 60, 62, 66, 67, 71, 72, 73, 74, 76, 79, 80]
            },
            {
                "mod": 89,
                "guess": 0,
                "roots": [3, 6, 7, 13, 14, 15, 19, 23, 24, 26, 27, 28, 29, 30, 31, 33, 35, 38, 41, 43, 46, 48, 51, 54, 56, 58, 59, 60, 61, 62, 63, 65, 66, 70, 74, 75, 76, 82, 83, 86]
            },
            {
                "mod": 97,
                "guess": 0,
                "roots": [5, 7, 10, 13, 14, 15, 17, 21, 23, 26, 29, 37, 38, 39, 40, 41, 56, 57, 58, 59, 60, 68, 71, 74, 76, 80, 82, 83, 84, 87, 90, 92]
            },
        ]

        # Success test cases with good guesses
        testcases_guess = [
            {
                "mod": 3,
                "guess": 2,
                "roots": [2]
            },
            {
                "mod": 5,
                "guess": 3,
                "roots": [2, 3]
            },
            {
                "mod": 89,
                "guess": 30,
                "roots": [3, 6, 7, 13, 14, 15, 19, 23, 24, 26, 27, 28, 29, 30, 31, 33, 35, 38, 41, 43, 46, 48, 51, 54, 56, 58, 59, 60, 61, 62, 63, 65, 66, 70, 74, 75, 76, 82, 83, 86]
            },
            {
                "mod": 97,
                "guess": 41,
                "roots": [5, 7, 10, 13, 14, 15, 17, 21, 23, 26, 29, 37, 38, 39, 40, 41, 56, 57, 58, 59, 60, 68, 71, 74, 76, 80, 82, 83, 84, 87, 90, 92]
            },
        ]            

        # Failure test cases with bad guesses
        testcases_badguess = [
            {
                "mod": 3,
                "guess": 3,
                "roots": [2]
            },
            {
                "mod": 5,
                "guess": 4,
                "roots": [2, 3]
            },
            {
                "mod": 89,
                "guess": 2,
                "roots": [3, 6, 7, 13, 14, 15, 19, 23, 24, 26, 27, 28, 29, 30, 31, 33, 35, 38, 41, 43, 46, 48, 51, 54, 56, 58, 59, 60, 61, 62, 63, 65, 66, 70, 74, 75, 76, 82, 83, 86]
            },
            {
                "mod": 97,
                "guess": 3,
                "roots": [5, 7, 10, 13, 14, 15, 17, 21, 23, 26, 29, 37, 38, 39, 40, 41, 56, 57, 58, 59, 60, 68, 71, 74, 76, 80, 82, 83, 84, 87, 90, 92]
            },
        ]

        for case in testcases:
            root = primitiverootsearch.rootSearch(case["mod"], case["guess"])
            self.assertIn(root, case["roots"])

        for case in testcases_guess:
            root = primitiverootsearch.rootSearch(case["mod"], case["guess"])
            self.assertIn(root, case["roots"])

        for case in testcases_badguess:
            root = primitiverootsearch.rootSearch(case["mod"], case["guess"])
            self.assertNotIn(root, case["roots"])

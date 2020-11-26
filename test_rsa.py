import unittest
import rsa_encrypt
import rsa_decrypt
import rsa_eavesdrop

# This RSA encrypt/decrypt/eavesdrop test can be run as follows:
# python3 -m unittest -v test_rsa.py 
#
# To run full suite of unit tests:
# python -m unittest discover -v
#
class Test_Rsa(unittest.TestCase):

    def test_rsaEncryptionDecryption(self):
        testcases = [
            {
                "p": 3,
                "q": 11,
                "x": 31
            },
            {
                "p": 11,
                "q": 13,
                "x": 141
            },

            # Test cases with n = 12091 and different messages x
            {
                "p": 107,
                "q": 113,
                "x": 3981
            },
            {
                "p": 107,
                "q": 113,
                "x": 4001
            },
            {
                "p": 107,
                "q": 113,
                "x": 11899
            },

            # Test cases with n = 15943
            {
                "p": 107,
                "q": 149,
                "x": 9611
            },
            {
                "p": 107,
                "q": 149,
                "x": 12035
            },

            # Test cases with higher primes taken from Garrett, Table 2: Primes Below 10,000
            {
                "p": 107,
                "q": 1619,
                "x": 23423
            },
            {
                "p": 4483,
                "q": 1619,
                "x": 101919 
            },
            {
                "p": 9931,
                "q": 9973,
                "x": 987345
            },
            {
                "p": 8707,
                "q": 9787,
                "x": 987345
            },
        ]

        # Test RSA encryption and decryption:
        # (1) Bob calculates the encryption and decryption keys
        # (2) Alice encrypts the message x
        # (3) Bob decrypts the encrypted message E_x
        # (4) Eve eavesdrops to find the plaintext message
        for case in testcases:
            e, d = rsa_decrypt.calculateEncryptionDecryptionKeys(case["p"], case["q"])
            n = case["p"] * case["q"]
            E_x = rsa_encrypt.rsaEncryption(n, e, case["x"])

            # Ensure Bob's decrypted result matches the input message x
            x = rsa_decrypt.rsaDecryption(E_x, d, n)
            self.assertEqual(case["x"], x)

            # Meanwhile Eve tries to eavesdrop but knows only encryption key e and the modulus n.
            # Can she factor into p and q and thus compute d to decrypt E_x?
            p, q = rsa_eavesdrop.factorModulus(n)
            d = rsa_eavesdrop.calculateDecryptionKey(p, q, e)
            x = rsa_eavesdrop.rsaDecryption(E_x, d, n)
            self.assertEqual(case["x"], x)

import unittest
import elgamal_encrypt
import elgamal_decrypt
import elgamal_eavesdrop

# This RSA encrypt/decrypt/eavesdrop test can be run as follows:
# python3 -m unittest -v test_elgamal.py 
#
# To run full suite of unit tests:
# python -m unittest discover -v
#
class Test_ElGamal(unittest.TestCase):

    def test_elGamalEncryptionDecryption(self):
        testcases = [
            # Test cases with higher primes taken from Garrett, Table 2: Primes Below 10,000
            {
                "p": 107,
                "x": 87
            },
            {
                "p": 4483,
                "x": 1234
            },
            {
                "p": 9931,
                "x": 9901
            },
            {
                "p": 8707,
                "x": 7654
            },
            {
                "p": 9973,
                "x": 9876
            },
        ]

        # Test ElGamal encryption and decryption:
        # (1) Bob computes his public key from a prime p
        # (2) Alice computes her public key and encrypts a message x
        # (3) Bob decrypts the encrypted message E_x
        # (4) Eve eavesdrops to find the plaintext message
        for case in testcases:
            b, b_l, l = elgamal_decrypt.computePublicKey(case["p"])

            # Alice computes per public key and encrypts a message x with
            # Bob's public key
            E_x, b_r = elgamal_encrypt.encrypt(case["p"], b, b_l, case["x"])

            # Bob decrypts the encrypted message using his private key (secret)
            decryptedMsg = elgamal_decrypt.decrypt(E_x, b_r, case["p"], l)
            self.assertEqual(case["x"], decryptedMsg)

            # Meanwhile Eve eavesdrops on the line. She can see both
            # Alice and Bob's public keys. She uses Baby Step Giant Step to
            # compute Bob's discrete log l. From there she can decrypt the
            # encrypted message using the ElGamal algorithm.
            log = elgamal_eavesdrop.computeDiscreteLog(case["p"], b, b_l)
            plaintext = elgamal_eavesdrop.decrypt(E_x, b_r, case["p"], log)
            self.assertEqual(case["x"], plaintext)

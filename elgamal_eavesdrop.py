#!/usr/bin/env python3

import babystepgiantstep
import elgamal_decrypt
import euclidean
import fastexponent

def computeDiscreteLog(p, base, b_l):
    # Find Bob's secret l, the log base b of b^l
    # We use the Baby-Step Giant-Step algorithm to compute the discrete log.
    l = babystepgiantstep.babyStepGiantStep(base, b_l, p)

    return l


# Use the ElGamal decrypt algorithm here given E(x), b^r, modulus p, and
# Bob's secret l.
def decrypt(E_x, b_r, p, l):
    # Bob computes (b^r)^l
    b_r_l = fastexponent.calculate(b_r, l, p)

    # Now use the Extended Euclidean algorithm to compute the
    # inverse of (b^r)^l, where
    # GCD (m, n) = (x0)m + (y0)n
    # and the inverse will be x0
    gcd, x0, y0 = euclidean.extendedEuclidean(b_r_l, p)

    # Decryted message x = ((b^r)^l)-1 * E(x)
    plaintext = (x0 * E_x) % p

    return plaintext


def main():
    print('ELGAMAL EAVESDROPPING ALGORITHM')
    print('Eve eavesdrops on Alice and Bob using Baby-Step, Giant-Step Algorithm\n')

    p    = int(input("From Bob's public key, enter prime modulus p: "))
    base = int(input("From Bob's public key, enter base b: "))
    b_l  = int(input("From Bob's public key, enter b^l: "))

    l = computeDiscreteLog(p, base, b_l)
    print ('\nEve computed secret l = %d' % l)

    b_r  = int(input("From Alice's public key, enter b^r: "))
    E_x = int(input("\nEnter encrypted message E(x): "))

    # Now we can decrypt the message with Bob's secret l
    plaintext = decrypt(E_x, b_r, p, l)

    print('\nDecrypted plaintext: %d' % plaintext)


if __name__ == '__main__':
    main()

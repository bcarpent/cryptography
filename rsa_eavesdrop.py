#!/usr/bin/env python3

import math
import fastexponent
import euclidean
import pollards_p_1
import pollards_rho
import smtplib
from getpass import getpass

def factorModulus(n):
    # Try factoring with Pollard's Rho method first. Failing that,
    # try factoring with Pollard's p-1 method.
    result = pollards_rho.factor(n)
    if (result != 0):
        p = result
        q = n / result
        print('Pollards Rho method factored %d into p = %d, q = %d' %(n, p, q))
        return p, q

    result = pollards_p_1.factor(n, 8)
    if (result != 0):
        p = result
        q = n / result
        print('Pollards P-1 method factored %d into p = %d, q = %d' %(n, p, q))
        return p, q

    return 0, 0


def computeGroupOrder(p, q):
    # Given p and q are primes, then the order using Euler's totient function
    # is (p - 1)(q - 1)
    order = (p - 1) * (q - 1)
    return order


def calculateDecryptionKey(p, q, e):
    # Get the order of the group given p and q
    n = p * q

    # Compute the order of the group
    order = computeGroupOrder(p, q)

    # Compute the multiplicativve inverse of e in Z*(order)
    # using the Extended Euclidean algorithm.
    gcd, x0, y0 = euclidean.extendedEuclidean(order, e)

    # Per the equation above, y0 is our inverse. If y0 is negative, simply
    # add the order to arrive at the positive integer inverse.
    if y0 < 0:
        d = order + y0
    else:
        d = y0

    return d


def rsaDecryption(E_x, d, n):
    # We now have the encryption exponent. Let's run fast exponentiation on
    # the message x
    result = fastexponent.calculate(E_x, d, n)
    print('Decrypted message: %d ^ %d mod %d = %d' %(E_x, d, n, result))
    print
    return result


def main():
    print('RSA EAVESDROPPING')
    print('Eve eavesdrops on Alice and Bob. From the public key, decrypt the message')

    n = int(input("From public key, enter modulus n:"))
    e = int(input("From public key, enter exponent e:"))

    print

    # Attempt to factor the modulus into p,q to break the encryption
    p, q = factorModulus(n)

    if (p == 0 or q == 0):
        print('Unable to factor modulus using Pollards Rho or p-1 method')
        return

    # Now compute the decryption key
    d = calculateDecryptionKey(p, q, e)

    print('Decryption key: %d' % d)

    # Now eavesdrop for the encrypted message
    print
    print('Eavesdrop for encrypted message...')
    E_x = int(input("Enter encrypted message E_x: "))

    # Now decrypt the message received
    decryptedMsg = rsaDecryption(E_x, d, n)

    print('Decrypted message: %d' % decryptedMsg)


if __name__ == '__main__':
    main()

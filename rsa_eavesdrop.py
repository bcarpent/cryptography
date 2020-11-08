#!/usr/bin/env python3

import math
import fastexponent
import euclidean
import smtplib
from getpass import getpass

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
    print('Decrypted message: ', E_x, '^', d, 'mod', n, '=', result)
    print
    return result


def factorModulus(n):

    # Initialize p and q to zero
    p = 0
    q = 0

    # Here we attempt to factor the modulus n into two primes p and q
    # by starting from a divisor of 3 and working up to n/2. 
    # Possible divisors are 3, 5, 7, etc, up to n.
    # So we step by 2 in this range.
    for i in range(3, int(n/2), 2):
        while n % i == 0:
            p = i
            q = int(n / i)
            print('Eve finds factors in primes p =', p, 'and q =', q, 'in modulus ', n)
            return p, q

    if p == 0:
        print('No prime factors found for n =', n)

    return p, q


def main():
    print('RSA EAVESDROPPING')
    print('Eve eavesdrops on Alice and Bob. From the public key, decrypt the message')
    print

    n = int(input("From public key, enter modulus n:"))
    e = int(input("From public key, enter exponent e:"))

    print

    # Attempt to factor the modulus into p,q to break the encryption
    p, q = factorModulus(n)

    # Now compute the decryption key
    d = calculateDecryptionKey(p, q, e)

    print('Decryption key: ', d)

    # Now eavesdrop for the encrypted message
    print
    print('Eavesdrop for encrypted message...')
    E_x = int(input("Enter encrypted message E_x: "))

    # Now decrypt the message received
    decryptedMsg = rsaDecryption(E_x, d, n)

    print('Decrypted message: ', decryptedMsg)


if __name__ == '__main__':
    main()

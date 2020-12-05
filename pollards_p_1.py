#!/usr/bin/env python3

import euclidean
import fastexponent
import math
import miller_rabin
import blumblumshub

def loop(p, g, b, B, n):
    # 5.  Loop
    # 5A. l = floor(log base p of n)
    # 5B. b = b^p^l mod n
    # 5C. g = gcd(b-1, n)
    # 5D. If g > 1, success, g is a factor of n
    #     Else try the next value of p in the factor base.
    factor = 0
    while (p <= B):
        l = math.floor(math.log(n, p))
        print('l =', l)
        b = fastexponent.calculate(b, (p ** l), n)
#        b = (b**(p**l)) % n
        print('b =', b)
        g = euclidean.gcd((b-1), n)
        print('g =', g)
        if (g > 1 and g < n):
            factor = g
            break
        else:
            if (p % 2 == 0):
                p += 1
            else:
                p += 2

    return factor


def factor(n, B):
    # 1. Choose a random smoothness bound.
    selectedB = False

    # First let's make sure this isn't a prime
    result = miller_rabin.millerRabinTest(n, 3)
    if (result != 0):
        print('The number', n, 'is a prime, cannot factor')
        return 0

    # 2. Calculate gcd(b,n).
    while (selectedB == False):
        b = blumblumshub.rand(2, n-1)
        gcd = euclidean.gcd(b, n)
        print('\nGCD (', b, ',', n, ') =', gcd)

        # 3. If gcd = n, try another B
        if (gcd == n):
            b = secrets.choice(range(2, n-1))
        elif (gcd == 1):
            selectedB = True
        else:
            return b              # We found a factor

    # 4. Initialize p = 2, g = 1, b = 3
    p = 2
    g = 1

    print('\nInitialization complete: B =', B)

    # INITIALIZATION COMPLETE

    factor = 0
    i = 0
    # Choose a random integer b
    print('Try b =', b)
    factor = loop(p, g, b, B, n)
    return factor


def main():
    print('POLLARDS P-1 METHOD')
    print('Factorization Algorithm')

    n = int(input("Enter modulus n to factor:"))
    B = int(input("Enter the smoothness bound B:"))

    p = factor(n, B)

    if (p == 0):
        print('\nPollard p-1 method failed to find a factor for n =', n)
    else:
	    print ('\nA factor of', n, 'is', p)
	    print ('p - 1 =', p - 1, 'is', B, '- smooth')


if __name__ == '__main__':
    main()

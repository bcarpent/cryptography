#!/usr/bin/env python3

import euclidean
import fastexponent
import math
import miller_rabin
import blumblumshub

def factor(n):
    # First let's make sure this isn't a prime
    result = miller_rabin.millerRabinTest(n, 3)
    if (result != 0):
        print('The number', n, 'is a prime, cannot factor')
        return 0

    # Initialization
    x = 2
    y = 2
    p = 1

    while (p == 1):
        x = fastexponent.calculate(x, 2, n)
        y = fastexponent.calculate(y, 2, n)
        y = fastexponent.calculate(y, 2, n)
        p = euclidean.gcd(x-y, n)

    print ('Pollards Rho found a factor of', n, ':', p)
    return p


def main():
    print('POLLARDS RHO METHOD')
    print('Factorization Algorithm')

    n = int(input("Enter modulus n to factor:"))

    result = factor(n)
    if (result == 0):
        print('\nPollards Rho method failed to find a factor for n =', result)
    else:
	    print ('\nPollards Rho found a factor of', n, ':', result)


if __name__ == '__main__':
    main()
